const headerElement = document.querySelector('header');
const toggle = document.querySelector('#toggle_header');

if (headerElement && toggle) {
  toggle.addEventListener('click', () => {
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  });
}
