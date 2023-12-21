(function ($) {
    'use strict';

    $(document).ready(function () {
        $('#table1').DataTable({
            "paging": true,
            "lengthChange": true,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": false,
            "responsive": false,
            "language": {
                "emptyTable": "Aucune donnée",
                "info": " _START_ à _END_ sur _TOTAL_ lignes(s)",
                "infoEmpty": "Affichage de 0 à 0 sur 0 ligne(s)",
                "infoFiltered": "(filtré de _MAX_ lignes)",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": "Affichage _MENU_ Enregistrements",
                "loadingRecords": "Chargement encours...",
                "processing": "",
                "search": "Recherche",
                "zeroRecords": "Aucune correspondance de recherche",
                "paginate": {
                    "first": "Premier",
                    "last": "Dernier",
                    "next": "Suivant",
                    "previous": "Précédent"
                }
            },
            buttons: [{
                extend: 'print',
                text: '<i class="fas  fa-print"></i> Imprimer',
                autoPrint: true,
                title: '',

                /*For repeating heading.
                repeatingHead: {
                    logo: '<!?= base_url('public/images/logo/generris.jpg'); ?>',
                    logoPosition: 'center', //right, left
                    logoStyle: '',//width:50px!important; height:50px
                    title: company_infos
                }*/
            }, {
                extend: 'excel',
                text: '<i class="fas fa-file-excel"></i> Exporter en Excel',
                title: '',
            },
            {
                extend: 'pdf',
                text: '<i class="fas fa-file-pdf"></i> Générer en PDF',
                title: '',
                exportOptions: {
                    modifier: {
                        page: 'current'
                    }
                },
            }]
        });
        $('#table1_length select').addClass('form-select form-control');
        $('#table1_filter input').addClass('form-control bg-light text-dark mr-3');
        $('#table1_wrapper .dataTables_filter').find('input').each(function () {
            const $this = $(this);
            $this.attr("placeholder", "Recherche ...");
        });
    });
}(jQuery));