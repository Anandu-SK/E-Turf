$(document).ready(function() {
    $("#turfcategory").change(function() {
        var category_id = $(this).val();
        var url = "/get-price/?category_id=" + category_id;
        $.get(url, function(data, status) {
            console.log("Received data:", data); // Debugging line
            $("#turfprice").val(data); // Set the value of the input field
        });
    });
});