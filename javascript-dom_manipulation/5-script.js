const headerElement = document.querySelector('header');
const update = document.querySelector('#update_header');

if (headerElement && update) {
  update.addEventListener('click', () => {
    headerElement.textContent = 'New Header!!!';
  });
}
