#!/usr/bin/node
document.getElementById('red_header').addEventListener('click', function () {
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
});
