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
                        <td class="td-dashboard">${record.quest.title}</td>
                        <td class="td-dashboard">${new Date(record.completion_date).toLocaleDateString()}</td>
                        <td class="td-dashboard">${formatTime(record.completion_time)}</td>
                        <td class="td-dashboard">${record.pace.toFixed(1)} min/km</td>
                        <td class="td-dashboard">${record.tokens_earned}</td>
                        <td class="td-dashboard"><strong>${getStatusBadge(record)}</strong></td>
                        <td class="td-dashboard">
                            <button class="btn-edit btn btn-global" onclick="window.location.href='/quest/${record.quest.slug}/edit/${record.id}/'">Edit</button>
                            <button class="btn-delete btn btn-global" onclick="if(confirm('Delete this record?')) window.location.href='/quest/${record.quest.slug}/delete/${record.id}/'">Delete</button>
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