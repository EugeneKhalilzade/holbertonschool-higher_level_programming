// URL to fetch the character data
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Select the <div> with id 'character'
const characterDiv = document.querySelector('#character');

// Fetch the data from the API
fetch(url)
  .then(response => response.json()) // Convert response to JSON
  .then(data => {
    // Update the content of the div with the character's name
    characterDiv.textContent = data.name;
  })
  .catch(error => console.error('Error fetching character:', error));