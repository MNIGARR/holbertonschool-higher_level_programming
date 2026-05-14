const header = document.querySelector('header');
const clickableElement = document.querySelector('#red_header');
function addRed()
{
    header.classList.add('red');
}
clickableElement.addEventListener('click', addRed);
