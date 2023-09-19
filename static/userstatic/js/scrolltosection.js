
// $(document).ready(function() {
//     // Get the section parameter from the URL
//     var section = "{{ section }}"; // This is where we retrieve it

//     // Scroll to the specified section
//     if (section) {
//         var target = $('#' + section);
//         if (target.length) {
//             $('html, body').animate({
//                 scrollTop: target.offset().top
//             }, 1000); // Adjust the duration as needed
//         }
//     }
// });


// Function to scroll to a specific section smoothly
// function scrollToSection(sectionId) {
//     var target = document.getElementById(sectionId);
//     if (target) {
//         window.scrollTo({
//             top: target.offsetTop,
//             behavior: 'smooth'
//         });
//     }
// }

// Handle clicks on links with fragment identifiers
// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//     anchor.addEventListener('click', function (e) {
//         e.preventDefault();
//         const sectionId = this.getAttribute('href').substring(1);
//         scrollToSection(sectionId);
//     });
// });
