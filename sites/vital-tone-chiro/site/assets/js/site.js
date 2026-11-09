const button = document.querySelector('.menu');
const nav = document.querySelector('#nav');
function setMenu(open) {
  button?.setAttribute('aria-expanded', String(open));
  nav?.classList.toggle('open', open);
}
button?.addEventListener('click', () => setMenu(button.getAttribute('aria-expanded') !== 'true'));
nav?.addEventListener('click', event => {
  if (event.target.closest('a')) setMenu(false);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && button?.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    button.focus();
  }
});
matchMedia('(max-width:960px)').addEventListener('change', event => {
  if (!event.matches) setMenu(false);
});

// Squarespace's form endpoint cannot be used here, so the form opens a prepared email instead.
document.querySelectorAll('.contact-form').forEach(form => form.addEventListener('submit', event => {
  event.preventDefault();
  const lines = [];
  for (const [key, value] of new FormData(form).entries()) lines.push(`${key}: ${value}`);
  const address = form.getAttribute('action').replace('mailto:', '');
  form.querySelector('.status').textContent = `Your email app will open with your information. Please send the message to complete your request. If it does not open, email ${address}.`;
  window.location.href = `mailto:${address}?subject=${encodeURIComponent('Vital Tone Chiropractic website form')}&body=${encodeURIComponent(lines.join('\r\n'))}`;
}));
