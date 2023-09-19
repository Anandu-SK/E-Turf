$(document).ready(function() {
    // This function runs when the document (the web page) is fully loaded and ready.

    $("#inputdate").change(function() {
        // This function runs when the value of the input field with the id "inputdate" changes.

        var booking_id = $(this).val();
        // Get the value of the "inputdate" field when it changes and store it in the variable "booking_id."

        var url = "/get-time/?booking_id=" + booking_id;
        // Construct a URL for an HTTP GET request. It includes the value of "booking_id" as a query parameter.

        $.get(url, function(data, status) {
            // Send an HTTP GET request to the specified URL and provide a callback function to handle the response.

            console.log("Received data:", data); // Debugging line
            // Output the received data to the browser's console for debugging purposes.

            $("#inputtime").html(data);
            // Set the value of the input field with the id "inputtime" to the data received from the server.
        });
    });
});
