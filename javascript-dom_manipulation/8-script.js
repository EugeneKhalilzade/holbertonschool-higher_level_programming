document.addEventListener('DOMContentLoaded', function () {
    // URL to fetch the French translation of "hello"
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    // Select the <div> with id 'hello'
    const helloDiv = document.querySelector('#hello');
  
    // Fetch the data from the API
    fetch(url)
      .then(response => response.json()) // Convert response to JSON
      .then(data => {
        // Update the content of the div with the translation
        helloDiv.textContent = data.hello;
      })
      .catch(error => console.error('Error fetching translation:', error));
  });