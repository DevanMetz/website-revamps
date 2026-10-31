const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
const header = document.querySelector('.site-header');
function setMenu(open) {
  nav.classList.toggle('open', open);
  header.classList.toggle('menu-open', open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = open ? 'Close' : 'Menu';
}
setMenu(false);
window.addEventListener('resize', () => { if (window.innerWidth > 1000) setMenu(false); });
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

let copyTimer;
document.addEventListener('click', async event => {
  const link = event.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link) return;
  event.preventDefault();
  const value = link.textContent.trim() || decodeURIComponent(link.getAttribute('href').split(':')[1]);
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(value);
  } catch (_) {
    const field = document.createElement('textarea');
    field.value = value;
    field.style.cssText = 'position:fixed;left:-9999px;top:0';
    document.body.appendChild(field);
    field.select();
    const copied = document.execCommand('copy');
    field.remove();
    if (!copied) return;
  }
  let toast = document.querySelector('.copy-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'copy-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    document.body.appendChild(toast);
  }
  toast.textContent = 'Copied ' + value;
  toast.hidden = false;
  clearTimeout(copyTimer);
  copyTimer = setTimeout(() => { toast.hidden = true; }, 1800);
});
