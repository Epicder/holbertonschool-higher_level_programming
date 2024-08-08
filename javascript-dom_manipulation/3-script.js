const headerid = document.getElementById('toggle_header');

headerid.addEventListener('click', () => {
  const headerr = document.querySelector('header');
  if (headerr.classList.contains('red')) {
    headerr.classList.remove('red');
    headerr.classList.add('green');
  } else {
    headerr.classList.remove('green')
    headerr.classList.add('red');
  }
});