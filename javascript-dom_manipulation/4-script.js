const ulselected = document.getElementById('add_item')

ulselected.addEventListener('click', () => {
const ul = document.querySelector('ul.my_list');
const li = document.createElement('li');
li.textContent = "Item";
ul.appendChild(li);
})

