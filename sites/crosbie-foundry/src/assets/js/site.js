const button=document.querySelector('.menu-button');
const nav=document.querySelector('#navigation');
function setMenu(open){
  button.setAttribute('aria-expanded',String(open));
  nav.classList.toggle('open',open);
}
button.addEventListener('click',()=>setMenu(button.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'&&button.getAttribute('aria-expanded')==='true'){
    setMenu(false);
    button.focus();
  }
});
window.matchMedia('(max-width:1000px)').addEventListener('change',event=>{
  if(!event.matches)setMenu(false);
});

const form=document.querySelector('#quote-form');
if(form)form.addEventListener('submit',event=>{
  event.preventDefault();
  if(!form.reportValidity())return;
  const body=Array.from(new FormData(form),([key,value])=>`${key}: ${value}`).join('\n');
  document.querySelector('#form-status').textContent='Your email app should open with your inquiry. Please send it from there.';
  window.location.href='mailto:crosbiefoundry@aol.com?subject='+encodeURIComponent('Casting quote request')+'&body='+encodeURIComponent(body);
});

const toast=document.createElement('div');
toast.className='copy-toast';
toast.setAttribute('role','status');
toast.setAttribute('aria-live','polite');
document.body.appendChild(toast);
let toastTimer;
document.addEventListener('click',async event=>{
  const link=event.target.closest('a[href^="tel:"],a[href^="mailto:"]');
  if(!link)return;
  event.preventDefault();
  const value=decodeURIComponent(link.getAttribute('href').split(':').slice(1).join(':').split('?')[0]);
  const display=link.textContent.trim()||value;
  try{
    if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(value);
  }catch(error){
    const focused=document.activeElement;
    const field=document.createElement('textarea');
    field.value=value;
    field.readOnly=true;
    field.style.cssText='position:fixed;top:0;left:0;opacity:0';
    document.body.appendChild(field);
    let copied=false;
    try{
      field.select();
      copied=document.execCommand('copy');
    }catch(error){
      copied=false;
    }finally{
      field.remove();
      focused?.focus({preventScroll:true});
    }
    if(!copied){
      window.location.href=link.href;
      return;
    }
  }
  toast.textContent='Copied '+display;
  clearTimeout(toastTimer);
  toastTimer=setTimeout(()=>{toast.textContent=''},1800);
});
