const editButtons = document.getElementsByClassName("btn-edit");
const runForm = document.getElementById("uploadRunForm");
const uploadModal = new bootstrap.Modal(document.getElementById("uploadRunModal"));
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const modalTitle = document.getElementById("uploadRunModalLabel");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated run's ID upon click
 * - Gets the content of the corresponding run div
 * - Shows the upload modal
 * - Populates the form with the run's data
 * - Updates the modal title and submit button
 * - Sets the form's action for editing
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let runId = e.target.getAttribute("data-comment_id");
    let runContent = document.getElementById(`run_upload${runId}`).innerText;
    
    // Extract data from run content
    let timeMatch = runContent.match(/Completed in: ([\d.]+)/);
    let tokensMatch = runContent.match(/Earning: (\d+)/);
    
    // Show modal and update form
    uploadModal.show();
    
    const completionTimeInput = runForm.querySelector('input[name="completion_time"]');
    const tokensEarnedInput = runForm.querySelector('input[name="tokens_earned"]');
    
    completionTimeInput.value = timeMatch[1];
    tokensEarnedInput.value = tokensMatch[1];
    
    modalTitle.innerText = "Edit Your Run";
    submitButton.innerText = "Update";
    runForm.setAttribute("action", `${window.location.pathname}edit/${runId}/`);
  });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated run's ID upon click
 * - Updates the deleteConfirm link's href to point to the deletion endpoint
 * - Shows the confirmation modal
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let runId = e.target.getAttribute("data-comment_id");
    deleteConfirm.href = `${window.location.pathname}delete/${runId}/`;
    deleteModal.show();
  });
}

/**
 * Reset form when modal is closed
 */
document.getElementById("uploadRunModal").addEventListener('hidden.bs.modal', function () {
    runForm.reset();
    modalTitle.innerText = "Upload Your Run";
    submitButton.innerText = "Submit";
    runForm.setAttribute("action", window.location.pathname);
});