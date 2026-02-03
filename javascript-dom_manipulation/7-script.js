// URL to fetch the movie data
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Select the <ul> with id 'list_movies'
const movieList = document.querySelector('#list_movies');

// Fetch the data from the API
fetch(url)
  .then(response => response.json()) // Convert response to JSON
  .then(data => {
    // Loop through each movie and create a <li> element
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error fetching movies:', error));