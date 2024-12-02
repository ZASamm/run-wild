const editButtons = document.getElementsByClassName("btn-edit");
const runForm = document.getElementById("uploadRunForm");
const uploadModalElement = document.getElementById("uploadRunModal");
const uploadModal = new bootstrap.Modal(uploadModalElement);
const submitButton = document.getElementById("submitButton");
const deleteModalElement = document.getElementById("deleteModal");
const deleteModal = new bootstrap.Modal(deleteModalElement);
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const modalTitle = document.getElementById("uploadRunModalLabel");



/**
 * Manages modal accessibility attributes
 */
function handleModalAccessibility(modalElement, isShowing) {
  if (isShowing) {
      modalElement.removeAttribute('inert');
      modalElement.removeAttribute('aria-hidden');
  } else {
      modalElement.setAttribute('inert', '');
      modalElement.removeAttribute('aria-hidden');
  }
}


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
      
      // Extract time from run content
      let timeMatch = runContent.match(/Completed in: ([\d.:]+)/);
      
      if (timeMatch) {
          // Parse the time string (expecting format like "HH:MM:SS" or similar)
          let timeStr = timeMatch[1];
          let timeParts = timeStr.split(':');
          
          // Find the form inputs
          const hoursInput = document.getElementById('id_hours');
          const minutesInput = document.getElementById('id_minutes');
          const secondsInput = document.getElementById('id_seconds');
          
          // Set the values based on time parts
          if (timeParts.length === 3) {
              if (hoursInput) hoursInput.value = parseInt(timeParts[0]);
              if (minutesInput) minutesInput.value = parseInt(timeParts[1]);
              if (secondsInput) secondsInput.value = parseInt(timeParts[2]);
          }
      }
      
      modalTitle.innerText = "Edit Your Run";
      submitButton.innerText = "Update";
      runForm.setAttribute("action", `${window.location.pathname}edit/${runId}/`);
      
      // Show modal
        uploadModal.show();
        handleModalAccessibility(uploadModalElement, true);

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
    handleModalAccessibility(deleteModalElement, true);
  });
}

/**
 * Modal event handlers
 */
uploadModalElement.addEventListener('hidden.bs.modal', function () {
  runForm.reset();
  modalTitle.innerText = "Upload Your Run";
  submitButton.innerText = "Submit";
  runForm.setAttribute("action", window.location.pathname);
  handleModalAccessibility(uploadModalElement, false);
});

deleteModalElement.addEventListener('hidden.bs.modal', function () {
  handleModalAccessibility(deleteModalElement, false);
});

