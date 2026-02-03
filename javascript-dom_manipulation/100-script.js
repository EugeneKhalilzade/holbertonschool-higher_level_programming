document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });

  removeItem.addEventListener('click', function () {
    if (myList.lastElementChild) {
      myList.removeChild(myList.lastElementChild);
    }
  });

  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});