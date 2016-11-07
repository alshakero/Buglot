$(document).ready(function() {
    $.getJSON("/query/", data, success);

    function data(_data) {
      if (_data.length > 0)
      {
        $(".loading").remove();
        $(".table").append('<tbody>');
        _data.forEach(handleDefectItem);
        $(".table").append('</tbody>');
      }
      else
      {
        $(".centeredText").html("There are no defects");
      }
    }

    function success(data) {
        /* nothing to be done in the meantime */
    }

    function handleDefectItem(defect) {
        $("tbody").append(
            '<tr class=' + getClassTypeFromStatus(defect.status) + '>' +
            '<td>' + defect._id + '</td>' +
            '<td>' + defect.platform + '</td>' +
            '<td>' + defect.exception_type + '</td>' +
            '<td>' + defect.class + '</td>' +
            '<td>' + defect.function+'</td>' +
            '<td>' + defect.line_num + '</td>' +
            '<td>' + defect.num_reports + '</td>' +
            '<td>' + defect.status + '</td>' +
            '/tr>'
        );
    }

    function getClassTypeFromStatus(status) {
        switch (status) {
            case "Reported":
                return "danger";
            case "Resolved":
                return "success";
            default:
                return "info";
        }
    }

    $(".ReloadButton").click(function() {
        $(this).fadeOut(function() {
            /*more specific search*/
        });
    });
});
