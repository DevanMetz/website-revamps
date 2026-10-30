const button = document.querySelector('.menu-button');
const nav = document.querySelector('#navigation');
function closeMenu(){nav.classList.remove('open');button.setAttribute('aria-expanded','false')}
button.addEventListener('click',()=>{const open=nav.classList.toggle('open');button.setAttribute('aria-expanded',String(open))});
document.addEventListener('keydown',event=>{if(event.key==='Escape'){closeMenu();button.focus()}});
document.querySelectorAll('[data-mail-form]').forEach(form=>form.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(form);const lines=[];for(const [key,value] of data){const label=form.querySelector(`[name="${key}"]`).labels[0].textContent;lines.push(`${label}: ${value}`)}const url='mailto:info@has-mor.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email app should open with your message ready to send.';window.location.href=url}));
