async function fetchLogs() {
    const res = await fetch('/api/logs');
    const logs = await res.json();
    const logsDiv = document.getElementById('logs');
    logsDiv.innerHTML = logs.map(log => `
        <div class="log-entry ${log.severity}">
            <strong>${log.type}</strong> - ${log.message} (${log.timestamp})
        </div>
    `).join('');
}

fetchLogs();
setInterval(fetchLogs, 5000); // Refresh every 5s
