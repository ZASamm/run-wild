const editButtons = document.querySelectorAll(".btn-edit");
const uploadModal = new bootstrap.Modal(document.getElementById("uploadRunModal"));
const questForm = document.querySelector("#uploadRunForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const modalTitle = document.getElementById("uploadRunModalLabel");

/**
 * Gets CSRF token from cookies
 */
function getCsrfToken() {
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Initializes the edit functionality for the edit buttons
 */
for (let button of editButtons) {
    button.addEventListener("click", async (e) => {
        e.preventDefault();
        
        // Get the quest record ID from the data attribute
        let questRecordId = e.target.getAttribute("data-comment_id");
        
        try {
            // Fetch the run data from the server
            const response = await fetch(`/get-run-data/${questRecordId}/`);
            if (!response.ok) {
                throw new Error('Failed to fetch run data');
            }
            
            const data = await response.json();
            
            // Update form fields
            document.getElementById("id_completion_time").value = data.completion_time;
            document.getElementById("id_tokens_earned").value = data.tokens_earned;
            
            // Update modal title and button
            modalTitle.textContent = "Edit Your Run";
            submitButton.textContent = "Update";
            
            // Get the current URL path and update form action
            let pathArray = window.location.pathname.split('/');
            let slug = pathArray[pathArray.length - 2]; // Get the slug from the URL
            questForm.action = `/quest/${slug}/edit/${questRecordId}/`;
            
            // Show the modal
            uploadModal.show();
            
        } catch (error) {
            console.error('Error:', error);
            alert('There was an error loading the run data. Please try again.');
        }
    });
}

// Reset form when modal is closed
document.getElementById("uploadRunModal").addEventListener('hidden.bs.modal', function () {
    questForm.reset();
    modalTitle.textContent = "Upload Your Run";
    submitButton.textContent = "Submit";
    // Reset form action to default upload URL
    let pathArray = window.location.pathname.split('/');
    let slug = pathArray[pathArray.length - 2];
    questForm.action = `/quest/${slug}/`;
});

// Add CSRF token to all POST requests
document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = getCsrfToken();
    
    // Add CSRF token to form if it doesn't exist
    if (!questForm.querySelector('input[name="csrfmiddlewaretoken"]')) {
        const csrfInput = document.createElement('input');
        csrfInput.type = 'hidden';
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = csrfToken;
        questForm.appendChild(csrfInput);
    }
});