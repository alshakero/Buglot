$(document).ready(function() {
    $('#defects').DataTable( {
        "ajax": "/query/",
        "columns": [
            { "data": "_id" },
            { "data": "platform" },
            { "data": "release" },
            { "data": "exception_type" },
            { "data": "class" },
            { "data": "function" },
            { "data": "line_num" },
            { "data": "num_reports" },
            { "data": "status" },
        ]
    } );
} );
