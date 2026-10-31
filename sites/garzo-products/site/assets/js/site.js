const button=document.querySelector('.menu'),nav=document.querySelector('#nav');button?.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open)});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&button?.getAttribute('aria-expanded')==='true'){button.setAttribute('aria-expanded','false');nav.classList.remove('open');button.focus()}});document.querySelectorAll('form').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(form), lines=[];for(const [key,value] of data.entries())lines.push(`${key}: ${value}`);const url='mailto:info@garzoproducts.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email app will open with your information. Please send the message to complete your request.';window.location.href=url}));


let copyTimer;
document.addEventListener('click', async e => {
  const link = e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link) return;
  e.preventDefault();
  const value = decodeURIComponent(link.getAttribute('href').split(':').slice(1).join(':').split('?')[0]);
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(value);
  } catch (_) {
    const field = document.createElement('textarea');
    field.value = value; field.style.position = 'fixed'; field.style.left = '-9999px';
    document.body.appendChild(field); field.select();
    const copied = document.execCommand('copy'); field.remove();
    if (!copied) return;
  }
  let toast = document.querySelector('.copy-toast');
  if (!toast) { toast = document.createElement('div'); toast.className = 'copy-toast'; toast.setAttribute('role', 'status'); toast.setAttribute('aria-live', 'polite'); document.body.appendChild(toast); }
  toast.textContent = 'Copied ' + value; toast.hidden = false;
  clearTimeout(copyTimer); copyTimer = setTimeout(() => { toast.hidden = true; }, 1800);
});
