$(document).ready(function(){
    function sortTable(columnIndex, order) {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("data-table");
        switching = true;

        while (switching) {
            switching = false;
            rows = table.rows;

            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[columnIndex];
                y = rows[i + 1].getElementsByTagName("td")[columnIndex];

                if (order === "asc" && x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                } else if (order === "desc" && x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }

            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }

    $("#data-table th").click(function() {
        var index = $(this).index();
        var sortOrder = $(this).hasClass("asc") ? "desc" : "asc";

        $("#data-table th").removeClass("asc desc");
        $(this).addClass(sortOrder);

        sortTable(index, sortOrder);
    });
});
