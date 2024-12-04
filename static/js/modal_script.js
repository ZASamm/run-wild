document.addEventListener("DOMContentLoaded", () => {
  // Get all our elements
  const editButtons = document.getElementsByClassName("btn-edit");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const runForm = document.getElementById("uploadRunForm");
  const uploadModal = new bootstrap.Modal("#uploadRunModal");
  const deleteModal = new bootstrap.Modal("#deleteModal");
  const modalTitle = document.getElementById("uploadRunModalLabel");
  const submitButton = document.getElementById("submitButton");
  const deleteConfirm = document.getElementById("deleteConfirm");

  // Setup edit buttons
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const runId = e.target.dataset.comment_id;
      const runContent = document.getElementById(`run_upload${runId}`).innerText;
      
      // Get the time values
      const timeMatch = runContent.match(/Completed in: ([\d.:]+)/);
      const [hours, minutes, seconds] = timeMatch ? timeMatch[1].split(':').map(Number) : [0, 0, 0];
      
      // Fill in the form
      document.getElementById('id_hours').value = hours || '';
      document.getElementById('id_minutes').value = minutes || '';
      document.getElementById('id_seconds').value = seconds || '';
      
      // Update modal content
      modalTitle.innerText = "Edit Your Run";
      submitButton.innerText = "Update";
      runForm.action = `${window.location.pathname}edit/${runId}/`;
      
      uploadModal.show();
    });
  }

  // Setup delete buttons
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      const runId = e.target.dataset.comment_id;
      deleteConfirm.href = `${window.location.pathname}delete/${runId}/`;
      deleteModal.show();
    });
  }

  // Reset form when upload modal is closed
  document.getElementById("uploadRunModal").addEventListener('hidden.bs.modal', () => {
    runForm.reset();
    modalTitle.innerText = "Upload Your Run";
    submitButton.innerText = "Submit";
    runForm.action = window.location.pathname;
  });
});