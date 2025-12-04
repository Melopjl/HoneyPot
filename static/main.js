let chart;
let labels = [];
let dataPoints = [];

function updateUI(stats) {
    document.getElementById("total").innerText = stats.total_attempts;

    const ipList = document.getElementById("top-ips");
    ipList.innerHTML = "";
    stats.top_ips.slice(0,5).forEach(i => {
        ipList.innerHTML += `<li>${i[0]} — ${i[1]}</li>`;
    });

    const userList = document.getElementById("top-users");
    userList.innerHTML = "";
    stats.top_usernames.slice(0,5).forEach(u => {
        userList.innerHTML += `<li>${u[0]} — ${u[1]}</li>`;
    });

    const now = new Date().toLocaleTimeString();
    labels.push(now);
    dataPoints.push(stats.total_attempts);

    if (labels.length > 20) {
        labels.shift();
        dataPoints.shift();
    }

    chart.data.labels = labels;
    chart.data.datasets[0].data = dataPoints;
    chart.update();
}

function fetchData(){
    fetch("/stats").then(r => r.json()).then(updateUI);

    fetch("/logs")
        .then(r => r.json())
        .then(j => {
            document.getElementById("logs").innerText = j.logs;
        });
}

function initChart(){
    const ctx = document.getElementById("chart").getContext('2d');

    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Tentativas',
                data: dataPoints,
                borderColor: '#00f7ff',
                backgroundColor: 'rgba(0,247,255,0.1)',
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

window.onload = () => {
    initChart();
    fetchData();
    setInterval(fetchData, 2000);
};
