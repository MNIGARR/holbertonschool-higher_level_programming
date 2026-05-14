const header = document.querySelector('header');
const clickToggleHeader = document.querySelector('#toggle_header');
function toggleClass()
{
if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
} else {
  header.classList.remove('green');
  header.classList.add('red')
}}
clickToggleHeader.addEventListener('click', toggleClass);
