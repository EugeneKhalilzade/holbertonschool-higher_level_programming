// Select the <div> with id 'update_header'
const updateHeader = document.querySelector('#update_header');

// Select the <header> element
const header = document.querySelector('header');

// Add a click event listener to the updateHeader element
updateHeader.addEventListener('click', function() {
  // Update the text content of the header
  header.textContent = 'New Header!!!';
});