// Select the <div> with id 'red_header'
const redHeader = document.querySelector('#red_header');

// Select the <header> element
const header = document.querySelector('header');

// Add a click event listener to the redHeader element
redHeader.addEventListener('click', function() {
  // Change the text color of the header to red (#FF0000)
  header.style.color = '#FF0000';
});