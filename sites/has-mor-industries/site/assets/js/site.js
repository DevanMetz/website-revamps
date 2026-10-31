document.querySelectorAll('[data-mail-form]').forEach(form=>form.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(form);const lines=[];for(const [key,value] of data){const label=form.querySelector(`[name="${key}"]`).labels[0].textContent;lines.push(`${label}: ${value}`)}const url='mailto:info@has-mor.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email app should open with your message ready to send.';window.location.href=url}));
const menu=document.querySelector('#navigation');
const toggle=document.querySelector('.menu-toggle');
const closeMenu=()=>{menu.classList.remove('open');toggle.setAttribute('aria-expanded','false')};
toggle.addEventListener('click',()=>{const open=menu.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));if(open) menu.querySelector('.menu-close').focus()});
menu.querySelector('.menu-close').addEventListener('click',()=>{closeMenu();toggle.focus()});
document.addEventListener('keydown',event=>{if(event.key==='Escape' && menu.classList.contains('open')){closeMenu();toggle.focus()}});
menu.addEventListener('click',event=>{if(event.target.closest('a')) closeMenu()});

let copyToastTimer;
document.addEventListener('click', async event => {
  const link = event.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link) return;
  event.preventDefault();
  const value = decodeURIComponent(link.getAttribute('href').replace(/^(tel:|mailto:)/i, '').split('?')[0]);
  const display = link.textContent.trim() || value;
  const fallback = () => {
    const field = document.createElement('textarea');
    field.value = value;
    field.setAttribute('readonly', '');
    field.style.cssText = 'position:fixed;left:-9999px;top:0';
    document.body.appendChild(field);
    field.select();
    const copied = document.execCommand('copy');
    field.remove();
    return copied;
  };
  let copied = false;
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(value);
      copied = true;
    } else copied = fallback();
  } catch (_) {
    try { copied = fallback(); } catch (_) { copied = false; }
  }
  let toast = document.querySelector('.copy-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'copy-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    document.body.appendChild(toast);
  }
  toast.textContent = copied ? `Copied ${display}` : 'Unable to copy';
  toast.classList.add('visible');
  clearTimeout(copyToastTimer);
  copyToastTimer = setTimeout(() => toast.classList.remove('visible'), 1800);
});
