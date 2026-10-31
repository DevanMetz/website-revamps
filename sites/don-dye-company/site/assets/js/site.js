const button=document.querySelector('.menu');const nav=document.querySelector('#navigation');button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open)});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&button.getAttribute('aria-expanded')==='true'){button.setAttribute('aria-expanded','false');nav.classList.remove('open');button.focus()}});const form=document.querySelector('#contact-form');if(form)form.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(form);const body=Array.from(data,([key,value])=>`${key}: ${value}`).join('\n');document.querySelector('#form-status').textContent='Your email app should open with your inquiry ready to send.';window.location.href=`mailto:info@dondyeco.com?subject=${encodeURIComponent('Product inquiry')}&body=${encodeURIComponent(body)}`});

document.querySelectorAll(".table-scroller").forEach(container=>{const wrap=container.querySelector(".table-wrap");const update=()=>container.classList.toggle("has-more",wrap.scrollLeft+wrap.clientWidth<wrap.scrollWidth-1);wrap.addEventListener("scroll",update,{passive:true});window.addEventListener("resize",update);update()});

let copyTimer;
document.addEventListener('click', async e => {
 const link = e.target.closest('a[href^="tel:"], a[href^="mailto:"]');
 if (!link) return;
 e.preventDefault();
 const value = decodeURIComponent(link.getAttribute('href').replace(/^(tel:|mailto:)/, '').split('?')[0]);
 const display = link.textContent.trim() || value;
 let copied = false;
 try { await navigator.clipboard.writeText(value); copied = true; } catch (_) {
  const field = document.createElement('textarea');
  field.value = value; field.setAttribute('readonly', '');
  field.style.cssText = 'position:fixed;left:-9999px;top:0';
  document.body.appendChild(field); field.select();
  try { copied = document.execCommand('copy'); } catch (_) {}
  field.remove();
 }
 let toast = document.querySelector('.copy-toast');
 if (!toast) { toast = document.createElement('div'); toast.className = 'copy-toast'; toast.setAttribute('role', 'status'); toast.setAttribute('aria-live', 'polite'); document.body.appendChild(toast); }
 toast.textContent = copied ? `Copied ${display}` : 'Copy failed';
 clearTimeout(copyTimer); copyTimer = setTimeout(() => { toast.textContent = ''; }, 1800);
});
