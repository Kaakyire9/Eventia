// filepath: /workspace/Eventia/static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    alert('JavaScript is working!');
    
    const testButton = document.getElementById('testButton');
    if (testButton) {
        testButton.addEventListener('click', function() {
            testButton.textContent = 'Button Clicked!';
        });
    }
});