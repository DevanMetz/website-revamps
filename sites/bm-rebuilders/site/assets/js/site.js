const menu=document.querySelector('.menu'),nav=document.querySelector('#nav');
function setMenu(open){menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'Close':'Menu';nav.classList.toggle('open',open)}
menu.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){setMenu(false);menu.focus()}});
const form=document.querySelector('#inquiry');if(form)form.addEventListener('submit',e=>{e.preventDefault();const body=Array.from(new FormData(form),([key,value])=>`${key}: ${value}`).join('\n');document.querySelector('#status').textContent='Your email app will open with your inquiry.';window.location.href='mailto:bmrebuild@aol.com?subject='+encodeURIComponent('Machinery service inquiry')+'&body='+encodeURIComponent(body)});
let copyTimer;
document.addEventListener('click', async event => {
  const link = event.target.closest('a[href^="tel:"], a[href^="mailto:"]');
  if (!link) return;
  event.preventDefault();
  const value = link.textContent.trim() || decodeURIComponent(link.getAttribute('href').split(':')[1]);
  const fallback = () => {
    const input = document.createElement('textarea');
    input.value = value;
    input.setAttribute('readonly', '');
    input.style.cssText = 'position:fixed;left:-9999px;top:0';
    document.body.appendChild(input);
    input.select();
    const copied = document.execCommand('copy');
    input.remove();
    return copied;
  };
  let copied = false;
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(value);
      copied = true;
    } else copied = fallback();
  } catch { copied = fallback(); }
  let toast = document.querySelector('.copy-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'copy-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    document.body.appendChild(toast);
  }
  toast.textContent = copied ? `Copied ${value}` : 'Copy failed';
  toast.hidden = false;
  clearTimeout(copyTimer);
  copyTimer = setTimeout(() => { toast.hidden = true; }, 1800);
});
