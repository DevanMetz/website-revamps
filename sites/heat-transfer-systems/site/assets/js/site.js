const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
const header = document.querySelector('.site-header');
function setMenu(open) {
  nav.classList.toggle('open', open);
  header.classList.toggle('menu-open', open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = open ? 'Close' : (matchMedia('(min-width: 1201px)').matches ? 'More' : 'Menu');
}
setMenu(false);
window.addEventListener('resize', () => { if (toggle.getAttribute('aria-expanded') === 'false') setMenu(false); });
toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    toggle.focus();
  }
});
const form = document.querySelector('#contact-form');
if (form) form.addEventListener('submit', event => {
  event.preventDefault();
  const body = Array.from(new FormData(form).entries()).map(([key, value]) => `${key}: ${value}`).join('\n');
  document.querySelector('#form-status').textContent = 'Your email application will open with your inquiry.';
  window.location.href = 'mailto:andrew.kwong@heattransfersys.com?subject=' + encodeURIComponent('Website inquiry') + '&body=' + encodeURIComponent(body);
});
