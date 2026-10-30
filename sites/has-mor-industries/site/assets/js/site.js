document.querySelectorAll('[data-mail-form]').forEach(form=>form.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(form);const lines=[];for(const [key,value] of data){const label=form.querySelector(`[name="${key}"]`).labels[0].textContent;lines.push(`${label}: ${value}`)}const url='mailto:info@has-mor.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email app should open with your message ready to send.';window.location.href=url}));
const menu=document.querySelector('#navigation');
const toggle=document.querySelector('.menu-toggle');
const closeMenu=()=>{menu.classList.remove('open');toggle.setAttribute('aria-expanded','false')};
toggle.addEventListener('click',()=>{const open=menu.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));if(open) menu.querySelector('.menu-close').focus()});
menu.querySelector('.menu-close').addEventListener('click',()=>{closeMenu();toggle.focus()});
document.addEventListener('keydown',event=>{if(event.key==='Escape' && menu.classList.contains('open')){closeMenu();toggle.focus()}});
menu.addEventListener('click',event=>{if(event.target.closest('a')) closeMenu()});
