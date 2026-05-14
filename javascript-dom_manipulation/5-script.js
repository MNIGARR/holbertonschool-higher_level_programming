const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

function clickUpdateHeader(){
    header.textContent = 'New Header!!!'
}
updateHeader.addEventListener('click', clickUpdateHeader);
