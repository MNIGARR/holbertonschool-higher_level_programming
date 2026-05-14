const ul = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item')

function clickAddItem(){
    const li = document.createElement('li');
    ul.appendChild(li);
    li.innerText = 'Item';
}
addItem.addEventListener('click', clickAddItem)
