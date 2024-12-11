from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import NewQuestForm

# Create your views here.


def about_me(request):

    """
    Handle the about page view.

    If the request method is POST, process the new quest form submission.
    If the form is valid, save the form data and add a success message.

    Retrieve the latest 'About' object and initialize a new quest form.

    Args:
        request (HttpRequest): The request object used to generate this view.

    Returns:
        HttpResponse:
        The rendered about page with the latest 'About' object
        and new quest form.
    """

    if request.method == "POST":
        new_quest_form = NewQuestForm(request.POST, request.FILES)
        if new_quest_form.is_valid():
            new_quest_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                """
                <p>Your new quest has been received!</p>
                <p>Admin is reviewing your submission.</p>
                <p>We aim to respond to you within 3 working days.</p>
                """
                )

    about = About.objects.all().order_by('-updated_on').first()
    new_quest_form = NewQuestForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "new_quest_form": new_quest_form,
        },
    )
