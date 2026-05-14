const ul = document.querySelector('ul');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json()
    .then(data => {
    const movies = data.results;
    for(let i = 0; i < movies.length; i++){
        const li = document.createElement('li');
        ul.append(li);
        li.innerText = movies[i].title;
    }
    })
    .catch(error => console.error('Error', error)));
