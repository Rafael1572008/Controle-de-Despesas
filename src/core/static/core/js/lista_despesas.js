document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.js-datatable').forEach((table) => {
        const config = {
            searching: false,
            lengthChange: false,
            pageLength: 5,
            order: [],
            language: {
                info: 'Mostrando _START_ a _END_ de _TOTAL_ registros',
                infoEmpty: 'Nenhum registro encontrado',
                zeroRecords: 'Nenhum registro encontrado',
                emptyTable: 'Nenhum registro disponível',
                paginate: { first: 'Primeiro', last: 'Último', next: 'Próximo', previous: 'Anterior' }
            },
            columnDefs: [{ targets: -1, orderable: false, searchable: false }]
        };

        if (table.dataset.dateColumn !== undefined) {
            config.columnDefs.push({
                targets: Number(table.dataset.dateColumn),
                type: 'date'
            });
        }

        const dataTable = new DataTable(table, config);
        const startInput = document.getElementById('date-filter-start');
        const endInput = document.getElementById('date-filter-end');
        const clearButton = document.getElementById('clear-date-filter');

        if (!startInput || !endInput || !clearButton) return;

        const dateColumn = Number(table.dataset.dateColumn ?? 2);

        const parseDate = (value) => {
            if (!value) return null;
            const [day, month, year] = value.split('/').map(Number);
            if (!day || !month || !year) return null;
            return new Date(year, month - 1, day);
        };

        const updateClearButton = () => {
            clearButton.hidden = !startInput.value && !endInput.value;
        };

        DataTable.ext.search.push((settings, searchData) => {
            if (settings.nTable !== table) return true;

            const start = startInput.value ? new Date(`${startInput.value}T00:00:00`) : null;
            const end = endInput.value ? new Date(`${endInput.value}T23:59:59`) : null;
            const rowDate = parseDate(searchData[dateColumn]);

            if (!rowDate) return false;
            if (start && rowDate < start) return false;
            if (end && rowDate > end) return false;
            return true;
        });

        const applyFilter = () => {
            dataTable.draw();
            updateClearButton();
        };

        startInput.addEventListener('change', applyFilter);
        endInput.addEventListener('change', applyFilter);

        clearButton.addEventListener('click', () => {
            startInput.value = '';
            endInput.value = '';
            applyFilter();
        });
    });
});
