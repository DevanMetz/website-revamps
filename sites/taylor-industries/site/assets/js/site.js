const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#nav');
function setMenu(open){toggle.setAttribute('aria-expanded',String(open));toggle.querySelector('.menu-label').textContent=open?'Close':'Menu';nav.classList.toggle('open',open)}
toggle?.addEventListener('click',()=>setMenu(toggle.getAttribute('aria-expanded')!=='true'));
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true'){setMenu(false);toggle.focus()}});
document.querySelectorAll('.video-load').forEach(button=>button.addEventListener('click',()=>{const frame=document.createElement('iframe');frame.src='https://www.youtube-nocookie.com/embed/lV67T6aLGC0?autoplay=1';frame.title='ECG Electrode Production Machine';frame.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';frame.allowFullscreen=true;button.replaceWith(frame)}));
document.querySelectorAll('form[data-subject]').forEach(form=>form.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(form);const lines=[];for(const [key,value] of data.entries())lines.push(`${key}: ${value}`);const url=`mailto:sales@taylor-ind.com?subject=${encodeURIComponent(form.dataset.subject)}&body=${encodeURIComponent(lines.join('\n'))}`;form.querySelector('.form-status').textContent='Your email application should open with your answers ready to send.';window.location.href=url}));
if(location.pathname==='/contact/'){const value=(new URLSearchParams(location.search).get('product')||'').replace(/[\u0000-\u001f\u007f]/g,'').slice(0,60);if(value){const form=document.querySelector('form[data-subject]');form.querySelector('#comments').value=`Product: ${value}\n`;form.dataset.subject=`Quote / sample request: ${value}`}}
const categoryNav=document.querySelector('.category-nav');
const currentCategory=categoryNav?.querySelector('[aria-current="page"]');
if(currentCategory && matchMedia('(max-width:600px)').matches){
 const navBox=categoryNav.getBoundingClientRect(), currentBox=currentCategory.getBoundingClientRect();
 if(currentBox.right>navBox.right) categoryNav.scrollLeft+=currentBox.right-navBox.right+12;
}
// Phone numbers and email addresses copy to the clipboard instead of opening an app
(()=>{let toast,timer;
function show(msg){if(!toast){toast=document.createElement('div');toast.className='copy-toast';toast.setAttribute('role','status');toast.setAttribute('aria-live','polite');document.body.appendChild(toast)}toast.textContent=msg;toast.classList.add('show');clearTimeout(timer);timer=setTimeout(()=>toast.classList.remove('show'),1800)}
function fallback(text){const area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();let ok=false;try{ok=document.execCommand('copy')}catch(e){}area.remove();return ok}
document.addEventListener('click',event=>{const link=event.target.closest('a[href^="tel:"],a[href^="mailto:"]');if(!link||event.defaultPrevented||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
 const href=link.getAttribute('href');const isTel=href.startsWith('tel:');let text=link.textContent.trim();
 if(isTel){if(!/\d{3}.*\d{4}/.test(text))text=href.slice(4)}else{const addr=decodeURIComponent(href.slice(7).split('?')[0]);if(!text.includes('@'))text=addr}
 event.preventDefault();const done=()=>show(`Copied ${text}`);
 if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(done,()=>{fallback(text)?done():show(text)})}else{fallback(text)?done():show(text)}
});})();
