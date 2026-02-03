// Select the <div> with id 'add_item'
const addItem = document.querySelector('#add_item');

// Select the <ul> element with class 'my_list'
const myList = document.querySelector('.my_list');

// Add a click event listener to the addItem element
addItem.addEventListener('click', function() {
  // Create a new <li> element
  const newItem = document.createElement('li');
  
  // Set its text content to 'Item'
  newItem.textContent = 'Item';
  
  // Append the new <li> element to the list
  myList.appendChild(newItem);
});