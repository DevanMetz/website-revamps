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
matchMedia('(max-width:1000px)').addEventListener('change', event => {
  if (!event.matches) setMenu(false);
});

document.querySelectorAll('form').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(form), lines=[];for(const [key,value] of data.entries())lines.push(`${key}: ${value}`);const url='mailto:info@garzoproducts.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email app will open with your information. Please send the message to complete your request.';window.location.href=url}));


let copyTimer;
document.addEventListener('click', async e => {
  const link = e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
  e.preventDefault();
  const value = decodeURIComponent(link.getAttribute('href').split(':').slice(1).join(':').split('?')[0]);
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(value);
  } catch (_) {
    const focused = document.activeElement;
    const field = document.createElement('textarea');
    field.value = value;
    field.readOnly = true;
    field.style.position = 'fixed';
    field.style.left = '-9999px';
    document.body.appendChild(field);
    let copied = false;
    try {
      field.select();
      copied = document.execCommand('copy');
    } catch (_) {
      // The browser may also block the legacy clipboard API.
    } finally {
      field.remove();
      focused?.focus({preventScroll: true});
    }
    if (!copied) {
      window.location.href = link.href;
      return;
    }
  }
  let toast = document.querySelector('.copy-toast');
  if (!toast) { toast = document.createElement('div'); toast.className = 'copy-toast'; toast.setAttribute('role', 'status'); toast.setAttribute('aria-live', 'polite'); document.body.appendChild(toast); }
  toast.textContent = 'Copied ' + value; toast.hidden = false;
  clearTimeout(copyTimer); copyTimer = setTimeout(() => { toast.hidden = true; }, 1800);
});
