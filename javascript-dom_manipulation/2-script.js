// Select the <div> with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Select the <header> element
const header = document.querySelector('header');

// Add a click event listener to the redHeader element
redHeader.addEventListener('click', function() {
  // Add the 'red' class to the header
  header.classList.add('red');
});