// AI Assisted code

// Format time duration from seconds to "Xh Ym"
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${minutes}m`;
}

// Create the status badge HTML
function getStatusBadge(record) {
    let badges = [];
    
    if (record.is_personal_best) {
        badges.push('<span class="status-badge status-pb">PB</span>');
    }
    
    if (record.approved) {
        badges.push('<span class="status-badge status-approved">Approved</span>');
    } else {
        badges.push('<span class="status-badge status-pending">Pending</span>');
    }
    
    return badges.join(' ');  // Join badges with a space between them
}

// Load and display the quest records
function loadQuestRecords() {
    fetch(DASHBOARD_DATA_URL)  // Use the URL passed from the template
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('questTableBody');
            tableBody.innerHTML = '';

            data.recent_records.forEach(record => {
                const row = `
                    <tr>
                        <td>${record.quest.title}</td>
                        <td>${new Date(record.completion_date).toLocaleDateString()}</td>
                        <td>${formatTime(record.completion_time)}</td>
                        <td>${record.pace.toFixed(1)} min/km</td>
                        <td>${record.tokens_earned}</td>
                        <td>${getStatusBadge(record)}</td>
                        <td>
                            <button class="btn-edit" onclick="window.location.href='/quest/${record.quest.slug}/edit/${record.id}/'">Edit</button>
                            <button class="btn-delete" onclick="if(confirm('Delete this record?')) window.location.href='/quest/${record.quest.slug}/delete/${record.id}/'">Delete</button>
                        </td>
                    </tr>
                `;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error('Error loading quest records:', error));
}

// Load records when page loads and every minute
loadQuestRecords();
setInterval(loadQuestRecords, 60000);