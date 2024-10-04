document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.getElementById('burgerMenu');
    document.querySelector('.header__burger a').addEventListener('click', function(event) {
        event.preventDefault();
        burgerMenu.style.display = (burgerMenu.style.display === 'none' || burgerMenu.style.display === '') ? 'block' : 'none';
    });
});