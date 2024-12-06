from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from .models import QuestPost, QuestRecord
from django.views.generic import TemplateView
from .forms import QuestCompletionForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePage(generic.ListView):
    """
    Displays the home page with a list of quests and aggregated statistics.
    """

    model = QuestPost
    template_name = "index.html"
    context_object_name = "quests"

    def get_context_data(self, **kwargs):
        """
        Adds total kilometers
        total hours
        and total completions to the context.
        """
        context = super().get_context_data(**kwargs)

        # get all the approved QuestRecord
        approved_records = QuestRecord.objects.filter(approved=True)

        # calc total kilometer
        total_kilometers = (
            approved_records.aggregate(
                total_km=Sum("quest__distance")
                )["total_km"] or 0
        )

        # Calc total tokens
        total_tokens = (
            approved_records.aggregate(
                total_tokens=Sum("tokens_earned")
                )["total_tokens"] or 0
        )

        # Count total approved completions
        total_completions = approved_records.count()

        # Add to context
        context.update(
            {
                "total_kilometers": round(total_kilometers, 0),
                "total_completions": total_completions,
                "total_tokens": round(total_tokens, 0),
            }
        )

        return context


class QuestRecordList(generic.ListView):
    """
    Displays a list of quest records.
    """

    model = QuestRecord
    context_object_name = "quest_record"


class QuestList(generic.ListView):
    """
    Displays a paginated list of quests.
    """

    model = QuestPost
    template_name = "quests.html"
    context_object_name = "quests"
    paginate_by = 4


def quest_post(request, slug):
    """
    Handles the display and submission of quest completion forms.

    Args:
        request: The HTTP request object.
        slug: The slug of the quest.

    Returns:
        HttpResponseRedirect:
        Redirects to the quest post page after form submission.
        HttpResponse:
        Renders the quest post page.
    """

    quest = get_object_or_404(QuestPost, slug=slug)
    quest_record = quest.quest_records.all().order_by("-tokens_earned")
    quest_count = quest.quest_records.count()

    if request.method == "POST":
        quest_form = QuestCompletionForm(data=request.POST)
        if quest_form.is_valid():
            run_upload = quest_form.save(commit=False)
            run_upload.runner = request.user
            run_upload.quest = quest
            run_upload.save()

            calc = run_upload._calculation_values
            messages.success(
                request,
                f"""
                <div class='calculation-breakdown'>
                    <h5>Quest Completed Successfully!</h5>
                    <div class='token-details'>
                        <div>Base Tokens:
                        <span> {calc['base_tokens']}</span>
                        </div>
                        <div>Pace Bonus:
                        <span> +{calc['pace_tokens']}</span>
                        </div>
                        <div>Personal Best Bonus:
                        <span> +{calc['bonus_tokens']}</span>
                        </div>
                        <div>Difficulty Multiplier:
                        <span> {calc['multiplier']}x</span>
                        </div>
                        <div class='total'>Total Tokens:
                        <span> {run_upload.tokens_earned}</span></div>
                        <div> Smashed it! keep up the good work!</div>
                    </div>
                </div>
                """,
            )

        return HttpResponseRedirect(reverse("quest_post", args=[slug]))

    quest_form = QuestCompletionForm()

    return render(
        request,
        "quests/quest_post.html",
        {
            "quest": quest,
            "quest_record": quest_record,
            "quest_form": quest_form,
            "quest_count": quest_count,
        },
    )


# run upload

# adds view for editing run data


def record_edit(request, slug, quest_record_id):
    """
    Handles the editing of a quest record.

    Args:
        request: The HTTP request object.
        slug: The slug of the quest.
        quest_record_id: The ID of the quest record.

    Returns:
        HttpResponseRedirect:
        Redirects to the quest post page after form submission.
    """

    quest = get_object_or_404(QuestPost, slug=slug)
    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id)

    if request.method == "POST":
        quest_form = QuestCompletionForm(
            data=request.POST, instance=run_upload
            )

        if quest_form.is_valid() and run_upload.runner == request.user:
            run_upload = quest_form.save(commit=False)
            run_upload.quest = quest
            run_upload.approved = False
            run_upload.save()
            messages.add_message(
                request, messages.SUCCESS, "Run updated!"
                )
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating run!"
                )

    return HttpResponseRedirect(reverse("quest_post", args=[slug]))


# add delete view


def record_delete(request, slug, quest_record_id):
    """
    Handles the deletion of a quest record.

    Args:
        request: The HTTP request object.
        slug: The slug of the quest.
        quest_record_id: The ID of the quest record.

    Returns:
        HttpResponseRedirect: Redirects to the quest post page after deletion.
    """

    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id)

    if run_upload.runner == request.user:
        run_upload.delete()
        messages.add_message(request, messages.SUCCESS, "Run deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own run!"
        )

    return HttpResponseRedirect(reverse("quest_post", args=[slug]))


# Add a view to get run data for editing


def get_run_data(request, quest_record_id):
    run_upload = get_object_or_404(QuestRecord, pk=quest_record_id)

    if run_upload.runner != request.user:
        return JsonResponse({"error": "Not authorized"}, status=403)

    data = {
        "completion_time": run_upload.completion_time,
        "tokens_earned": run_upload.tokens_earned,
    }

    return JsonResponse(data)


# Dashboard view


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Displays the user's dashboard
    aggregated statistics and personal bests.
    """

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        """
        Adds total kilometers,
        total tokens,
        total completions,
        and personal bests to the context.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        approved_records = QuestRecord.objects.filter(
            runner=user, approved=True
            )

        context.update(
            {
                "total_kilometers": round(
                    approved_records.aggregate(total_km=Sum("quest__distance"))
                    [
                        "total_km"
                    ]
                    or 0,
                    0,
                ),
                "total_tokens":
                    QuestRecord.objects.filter(runner=user).aggregate(
                    Sum("tokens_earned")
                )["tokens_earned__sum"]
                or 0,
                "total_completions": approved_records.count(),
                "personal_bests": QuestRecord.objects.filter(
                    runner=user, is_personal_best=True
                ).count(),
            }
        )
        return context


class DashboardDataView(LoginRequiredMixin, View):
    """
    Provides recent quest records data for the user's dashboard.
    """

    def get(self, request):
        """
        Handles GET request to retrieve recent quest
        records for the logged-in user.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: A JSON response containing recent quest records data.
        """
        user = request.user
        recent_records = (
            QuestRecord.objects.filter(runner=user)
            .select_related("quest")
            .order_by("-completion_date")[:10]
        )

        data = {
            "recent_records": [
                {
                    "quest": {
                        "title": record.quest.title,
                        "difficulty": record.quest.difficulty,
                        "slug": record.quest.slug,
                    },
                    "id": record.id,
                    "completion_date": record.completion_date,
                    "completion_time": record.completion_time.total_seconds(),
                    "pace": record.pace,
                    "tokens_earned": record.tokens_earned,
                    "is_personal_best": record.is_personal_best,
                    "approved": record.approved,
                }
                for record in recent_records
            ]
        }

        return JsonResponse(data)
