const menu=document.querySelector('.menu'),nav=document.querySelector('#nav');
function setMenu(open){menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'Close':'Menu';nav.classList.toggle('open',open)}
menu.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){setMenu(false);menu.focus()}});
const form=document.querySelector('#inquiry');if(form)form.addEventListener('submit',e=>{e.preventDefault();const body=Array.from(new FormData(form),([key,value])=>`${key}: ${value}`).join('\n');document.querySelector('#status').textContent='Your email app will open with your inquiry.';window.location.href='mailto:bmrebuild@aol.com?subject='+encodeURIComponent('Machinery service inquiry')+'&body='+encodeURIComponent(body)});
