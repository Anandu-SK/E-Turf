// Add this script to your main JavaScript file
document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a.page-link');

    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();

            const targetPage = event.target.getAttribute('href');
            const currentPage = document.querySelector('.page-enter');
            const nextPage = document.querySelector(targetPage);

            currentPage.classList.remove('page-enter');
            currentPage.classList.add('page-exit');

            nextPage.classList.remove('page-enter');
            nextPage.classList.add('page-enter-active');

            setTimeout(() => {
                currentPage.style.display = 'none';
            }, 300); // Adjust this time to match your CSS transition time
        });
    });
});
