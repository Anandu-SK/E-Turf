function validateForm() {
    // Check if all required fields are filled
    var nameField = document.querySelector('input[name="uName"]');
    var emailField = document.querySelector('input[name="uEmail"]');
    var phoneField = document.querySelector('input[name="uPhone"]');
    var categoryField = document.querySelector('select[name="uTurfCategory"]');
    var dateField = document.querySelector('input[name="uDate"]');

    if (
        nameField.value.trim() === '' ||
        emailField.value.trim() === '' ||
        phoneField.value.trim() === '' ||
        categoryField.value.trim() === '' ||
        dateField.value.trim() === ''
    ) {
        alert('Please fill in all required fields.');
    } else {
        showPrompt();
    }
}

function showPrompt() {
    var modal = document.getElementById("promptModal");
    modal.style.display = "block";

    event.preventDefault();
    // setTimeout(function() {
    //     modal.style.display = "none";
    // }, 1500);

 
}



document.addEventListener("DOMContentLoaded", function() {
    // Get a reference to the form element
    var form = document.getElementById("bookNowForm");

    // Get references to the Pay Now and Pay Later buttons
    var payNowButton = document.getElementById("payNowModalButton");
    var payLaterButton = document.getElementById("payLaterModalButton");

    // Add event listeners to the Pay Now and Pay Later buttons
    payNowButton.addEventListener("click", function() {
        document.getElementById("actionType").value = "action1";
        form.submit();
    });

    payLaterButton.addEventListener("click", function() {
        document.getElementById("actionType").value = "action2";
        form.submit();
        var modal = document.getElementById("promptModal");
        modal.style.display = "none"

    });

});

console.log("Script is loaded");
    
    function cancel() {
       
        var modal = document.getElementById("promptModal");
        modal.style.display = "none"
    }


