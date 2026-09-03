document.addEventListener('DOMContentLoaded', function () {
    const statusEl = document.getElementById('dashboard-status-data');
    const labelsEl = document.getElementById('dashboard-top-labels');
    const valuesEl = document.getElementById('dashboard-top-values');

    if (typeof Chart === 'undefined') return;

    const statusData = statusEl ? JSON.parse(statusEl.textContent) : [];
    const topLabels = labelsEl ? JSON.parse(labelsEl.textContent) : [];
    const topValues = valuesEl ? JSON.parse(valuesEl.textContent) : [];

    const formatBRL = value => new Intl.NumberFormat('pt-BR', {
        style: 'currency', currency: 'BRL'
    }).format(value);

    const statusCanvas = document.getElementById('statusChart');
    if (statusCanvas) {
        new Chart(statusCanvas, {
            type: 'doughnut',
            data: {
                labels: ['Baixado', 'Agendado'],
                datasets: [{ data: statusData, backgroundColor: ['#218c5a', '#9aa69f'], borderWidth: 0 }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '68%',
                plugins: {
                    legend: { display: false },
                    tooltip: { callbacks: { label: context => `${context.label}: ${formatBRL(context.raw)}` } }
                }
            }
        });
    }

    const topCanvas = document.getElementById('topChart');
    if (topCanvas) {
        new Chart(topCanvas, {
            type: 'bar',
            data: {
                labels: topLabels,
                datasets: [{ label: 'Valor', data: topValues, backgroundColor: '#218c5a', borderRadius: 7, barThickness: 22 }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: { beginAtZero: true, ticks: { callback: value => formatBRL(value) }, grid: { color: '#edf1ee' } },
                    y: { grid: { display: false } }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: { callbacks: { label: context => formatBRL(context.raw) } }
                }
            }
        });
    }
});
