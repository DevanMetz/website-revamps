const menu=document.querySelector('.menu'),nav=document.querySelector('#nav');menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')==='true';menu.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open);menu.textContent=open?'Menu':'Close'});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){menu.setAttribute('aria-expanded','false');nav.classList.remove('open');menu.textContent='Menu';menu.focus()}});document.querySelector('#quote-form')?.addEventListener('submit',e=>{e.preventDefault();const form=e.currentTarget;const lines=Array.from(form.querySelectorAll('label')).map(label=>{const field=label.querySelector('input, textarea');return label.firstChild.textContent.trim()+': '+field.value});location.href='mailto:office@stevenswire.com?subject='+encodeURIComponent('Wire product inquiry')+'&body='+encodeURIComponent(lines.join('\n'));document.querySelector('#form-status').textContent='Your email application should open with your inquiry.'});

let copyToastTimer;
document.addEventListener('click', async event => {
  const link = event.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link) return;
  event.preventDefault();
  const value = decodeURIComponent(link.getAttribute('href').split(':').slice(1).join(':').split('?')[0]);
  const display = link.textContent.trim() || value;
  let copied = false;
  try {
    await navigator.clipboard.writeText(value);
    copied = true;
  } catch (_) {
    const field = document.createElement('textarea');
    field.value = value;
    field.style.cssText = 'position:fixed;left:-9999px;top:0';
    document.body.appendChild(field);
    field.select();
    try { copied = document.execCommand('copy'); } catch (_) {}
    field.remove();
  }
  let toast = document.querySelector('.copy-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'copy-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    document.body.appendChild(toast);
  }
  toast.textContent = copied ? 'Copied ' + display : 'Unable to copy';
  toast.hidden = false;
  clearTimeout(copyToastTimer);
  copyToastTimer = setTimeout(() => { toast.hidden = true; }, 1800);
});
