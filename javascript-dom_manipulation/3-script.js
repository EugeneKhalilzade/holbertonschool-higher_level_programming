// Select the <div> with id 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Select the <header> element
const header = document.querySelector('header');

// Add a click event listener to the toggleHeader element
toggleHeader.addEventListener('click', function() {
  // Check if the header currently has the 'red' class
  if (header.classList.contains('red')) {
    // Switch to 'green'
    header.classList.replace('red', 'green');
  } else {
    // Switch to 'red'
    header.classList.replace('green', 'red');
  }
});