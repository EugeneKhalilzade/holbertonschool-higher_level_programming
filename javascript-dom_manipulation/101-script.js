document.addEventListener('DOMContentLoaded', function () {
  const button = document.querySelector('#btn_translate');
  const languageSelect = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  button.addEventListener('click', function () {
    const lang = languageSelect.value;

    if (lang === '') {
      helloDiv.textContent = '';
      return;
    }

    fetch('https://hellosalut.stefanbohacek.com/?lang=' + lang)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      });
  });
});