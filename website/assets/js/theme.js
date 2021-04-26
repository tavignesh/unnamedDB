// this one is jut to wait for the page to load
document.addEventListener('DOMContentLoaded', () => {

    const themeStylesheet = document.getElementById('theme');
    const themeToggle = document.getElementById('theme-toggle');
    themeToggle.addEventListener('click', () => {
        // if it's light -> go dark
        if(themeStylesheet.href.includes('light')){
            themeStylesheet.href = '/assets/css/dark.css';
            themeToggle.innerText = 'Light mode';
        } else {
            // if it's dark -> go light
            themeStylesheet.href = '/assets/css/light.css';
            themeToggle.innerText = 'Dark mode';

        }
    })
    })