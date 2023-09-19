 // Get the current date
 const currentDate = new Date();

 // Format the date as desired (e.g., "MM/DD/YYYY")
 const formattedDate = `${currentDate.getMonth() + 1}/${currentDate.getDate()}/${currentDate.getFullYear()}`;

 // Update the content of the HTML element with the formatted date
 document.getElementById("currentDate").textContent = formattedDate;