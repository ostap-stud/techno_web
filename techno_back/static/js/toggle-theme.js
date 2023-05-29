document.addEventListener('DOMContentLoaded', function() {
  var theme = localStorage.getItem('theme');
  var body = document.querySelector('body');
  var img = document.getElementById('main-image');
  var btn = document.getElementById('theme-toggle-btn');
  if (theme === 'dark') {
    body.setAttribute('data-bs-theme', 'dark');
    btn.innerHTML = '<i class="bi bi-lightbulb-fill"></i>';
    img.setAttribute('src', 'https://img.icons8.com/ios/100/ffffff/dj.png');
    soundcloud.style.color = '#212529';
  }
});

document.getElementById('theme-toggle-btn').addEventListener('click', function() {
  var body = document.querySelector('body');
  var img = document.getElementById('main-image');
  var theme = body.getAttribute('data-bs-theme');
  
  if (theme === 'dark') {
    body.setAttribute('data-bs-theme', 'light');
    this.innerHTML = '<i class="bi bi-lightbulb"></i>';
    img.setAttribute('src', 'https://img.icons8.com/ios/100/dj.png');
    localStorage.setItem('theme', 'light');
  } else {
    body.setAttribute('data-bs-theme', 'dark');
    this.innerHTML = '<i class="bi bi-lightbulb-fill"></i>';
    img.setAttribute('src', 'https://img.icons8.com/ios/100/ffffff/dj.png');
    localStorage.setItem('theme', 'dark');
  }
});