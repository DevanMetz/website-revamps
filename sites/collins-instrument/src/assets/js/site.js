const menu=document.querySelector('.menu'),nav=document.querySelector('#nav');
function setMenu(open){
 if(!menu||!nav)return;
 menu.setAttribute('aria-expanded',String(open));
 nav.classList.toggle('open',open);
 menu.textContent=open?'Close':'Menu';
}
menu?.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){setMenu(false);menu.focus()}});
const desktop=window.matchMedia('(min-width:1001px)');
desktop.addEventListener('change',event=>{if(event.matches)setMenu(false)});
document.querySelectorAll('form[data-subject]').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const lines=Array.from(new FormData(form),([name,value])=>`${name}: ${value}`);const url='mailto:cic@collinsinst.com?subject='+encodeURIComponent(form.dataset.subject)+'&body='+encodeURIComponent(lines.join('\n'));form.querySelector('.status').textContent='Your email application will open with your inquiry. Please send the email to complete your request.';window.location.href=url}));

let copyToastTimer;
document.addEventListener('click',async event=>{
 const link=event.target.closest('a[href^="tel:"],a[href^="mailto:"]');
 if(!link)return;
 event.preventDefault();
 const value=decodeURIComponent(link.getAttribute('href').replace(/^(tel:|mailto:)/,'').split('?')[0]);
 const text=link.textContent.trim() === 'Call' ? value : (link.textContent.trim() || value);
 try {
  if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');
  await navigator.clipboard.writeText(value);
 } catch {
  const field=document.createElement('textarea');
  field.value=value; field.setAttribute('readonly',''); field.style.position='fixed'; field.style.left='-9999px';
  const focused=document.activeElement;
  document.body.appendChild(field);
  let copied=false;
  try{field.select();copied=document.execCommand('copy')}catch{}finally{field.remove();focused?.focus({preventScroll:true})}
  if(!copied){window.location.href=link.href;return}
 }
 let toast=document.querySelector('.copy-toast');
 if(!toast){toast=document.createElement('div');toast.className='copy-toast';toast.setAttribute('role','status');toast.setAttribute('aria-live','polite');document.body.appendChild(toast)}
 toast.textContent='Copied '+text; toast.hidden=false;
 clearTimeout(copyToastTimer); copyToastTimer=setTimeout(()=>{toast.hidden=true},1800);
});
