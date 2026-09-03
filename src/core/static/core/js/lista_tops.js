document.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('.js-datatable');
    if (!table) return;

    new DataTable(table, {
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
    });
});
