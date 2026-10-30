const menu = document.querySelector('.menu');
const nav = document.querySelector('#navigation');
if (menu && nav) {
  const close = () => { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); };
  menu.addEventListener('click', () => { const open = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(open)); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape') { close(); menu.focus(); } });
}
const form = document.querySelector('#inquiry');
if (form) form.addEventListener('submit', event => {
  event.preventDefault();
  const body = Array.from(new FormData(form), ([name, value]) => `${name}: ${value}`).join('\n');
  document.querySelector('#form-status').textContent = 'Your email app will open with your inquiry.';
  window.location.href = `mailto:info@fontanamachine.com?subject=${encodeURIComponent('Machining inquiry')}&body=${encodeURIComponent(body)}`;
});
