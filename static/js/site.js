(function(){
  var d=document;
  // mobile nav
  var tg=d.querySelector('.nav-toggle'),nav=d.getElementById('nav');
  if(tg&&nav)tg.addEventListener('click',function(){var o=nav.classList.toggle('open');tg.setAttribute('aria-expanded',o)});
  // close language menu on outside click
  d.addEventListener('click',function(e){d.querySelectorAll('details.lang[open]').forEach(function(x){if(!x.contains(e.target))x.removeAttribute('open')})});
  // remember chosen language
  d.querySelectorAll('[data-lang]').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('cliave-lang',a.dataset.lang)}catch(e){}})});
  // theme toggle
  var tt=d.querySelector('.theme-toggle');
  if(tt)tt.addEventListener('click',function(){var r=d.documentElement,cur=r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'),n=cur==='dark'?'light':'dark';r.dataset.theme=n;try{localStorage.setItem('cliave-theme',n)}catch(e){}});
  // reading progress + toc highlight
  var bar=d.querySelector('.progress span'),art=d.querySelector('article.chapter');
  var links=[].slice.call(d.querySelectorAll('.toc a')),heads=links.map(function(a){return d.getElementById(a.getAttribute('href').slice(1))});
  if(bar&&art){var onScroll=function(){var r=art.getBoundingClientRect(),h=art.offsetHeight-innerHeight;bar.style.width=Math.max(0,Math.min(1,-r.top/Math.max(1,h)))*100+'%';
    var cur=-1;heads.forEach(function(h,i){if(h&&h.getBoundingClientRect().top<120)cur=i});links.forEach(function(a,i){a.classList.toggle('active',i===cur)})};
    addEventListener('scroll',onScroll,{passive:true});onScroll();}
  // collapse chapter nav on small screens
  if(innerWidth<860)d.querySelectorAll('.chapter-nav details').forEach(function(x){x.removeAttribute('open')});
  // quizzes
  d.querySelectorAll('.quiz .q').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();
    var sel=f.querySelector('input:checked');if(!sel)return;var ans=f.dataset.answer,qz=f.closest('.quiz'),fb=f.querySelector('.q-feedback');
    f.querySelectorAll('label').forEach(function(l){l.classList.remove('right','wrong')});
    var ok=sel.value===ans;sel.parentNode.classList.add(ok?'right':'wrong');
    if(!ok)f.querySelectorAll('input')[+ans].parentNode.classList.add('right');
    fb.textContent=(ok?qz.dataset.correct:qz.dataset.incorrect)+' '+fb.dataset.explain;fb.hidden=false;})});
})();
