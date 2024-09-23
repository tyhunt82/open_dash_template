// assets/scripts.js

document.addEventListener('DOMContentLoaded', function () {
    var sidebar = document.getElementById('sidebar');
    var toggleButton = document.getElementById('sidebar-toggle');

    if (toggleButton) {
        toggleButton.addEventListener('click', function () {
            sidebar.classList.toggle('closed');
        });
    }
});
