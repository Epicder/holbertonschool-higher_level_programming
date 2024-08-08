const headerfilter = document.getElementById('red_header');

headerfilter.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.classList.add('red');
});