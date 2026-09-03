document.addEventListener('DOMContentLoaded', () => {
    initializeDataTables();
});

function initializeDataTables() {
    document.querySelectorAll('.js-datatable').forEach((table) => {
        const config = {
            language: {
                search: 'Pesquisar:',
                lengthMenu: 'Mostrar _MENU_ registros',
                info: 'Mostrando _START_ a _END_ de _TOTAL_ registros',
                infoEmpty: 'Nenhum registro encontrado',
                infoFiltered: '(filtrado de _MAX_ registros)',
                zeroRecords: 'Nenhum registro encontrado',
                emptyTable: 'Nenhum registro disponível',
                paginate: { first: 'Primeiro', last: 'Último', next: 'Próximo', previous: 'Anterior' }
            },
            pageLength: 10,
            lengthMenu: [5, 10, 25, 50],
            order: [],
            columnDefs: [{ targets: -1, orderable: false, searchable: false }]
        };

        if (table.dataset.dateColumn !== undefined) {
            const dateColumn = Number(table.dataset.dateColumn);
            config.columnDefs.push({ targets: dateColumn, type: 'date', render: DataTable.render.text() });
        }

        const dataTable = new DataTable(table, config);

        document.querySelectorAll('[data-table-filter]').forEach((filter) => {
            if (filter.dataset.tableFilter !== table.id) return;
            filter.addEventListener('change', () => {
                const column = Number(filter.dataset.column);
                dataTable.column(column).search(filter.value).draw();
            });
        });
    });
}
