'use strict';
const canvas=document.getElementById('scene'), ctx=canvas.getContext('2d');
const offer=document.getElementById('offer'), lower=document.getElementById('lower');
const pause=document.getElementById('pause'), scrub=document.getElementById('scrub');
const view=document.getElementById('view'), scale=document.getElementById('scale');
const paths={reposo:'anims/reposo',subir:'anims/subir',sostener:'anims/sostener',bajar:'anims/bajar',fondo:'sprites/fondo',sombras:'sprites/sombras',silla:'sprites/silla',mesa:'sprites/mesa',croquetas:'sprites/croquetas',aceitunas:'sprites/aceitunas'};
const images={},labels={reposo:'Reposo',subir:'Levantando la tarjeta',sostener:'Ofreciendo pagar',bajar:'Bajando la mano'};
let state='reposo', frame=0, elapsed=0, last=0, paused=false, ready=false;
function pose(){return state==='reposo'?0:state==='sostener'?6:state==='bajar'?6-frame:frame}
function setState(next,at=0){state=next;frame=at;elapsed=0;update()}
function update(){
  document.getElementById('state').textContent=labels[state]+(paused?' · pausa':'');
  document.getElementById('frame').textContent=`Pose ${pose()+1}/7 · fotograma ${frame+1}`;
  offer.disabled=state==='subir'||state==='sostener'; lower.disabled=state==='reposo'||state==='bajar';
  scrub.value=pose(); pause.textContent=paused?'Reanudar':'Pausar';
}
function resize(){const s=+scale.value;canvas.width=(view.value==='sprite'?96:208)*s;canvas.height=(view.value==='sprite'?112:144)*s;draw()}
function draw(){
  if(!ready)return;
  const s=+scale.value;ctx.setTransform(s,0,0,s,0,0);ctx.imageSmoothingEnabled=false;
  ctx.clearRect(0,0,canvas.width/s,canvas.height/s);
  if(view.value==='context'){
    ctx.drawImage(images.fondo,0,0);
    ctx.drawImage(images.sombras,0,0);
    ctx.drawImage(images.silla,117,64);ctx.drawImage(images.mesa,8,81);
    ctx.drawImage(images[state],frame*96,0,96,112,100,28,96,112);
    ctx.drawImage(images.croquetas,39,93);ctx.drawImage(images.aceitunas,78,91);
  }else{
    for(let y=0;y<112;y+=8)for(let x=0;x<96;x+=8){ctx.fillStyle=((x+y)/8)%2?'#35414b':'#303b45';ctx.fillRect(x,y,8,8)}
    ctx.drawImage(images[state],frame*96,0,96,112,0,0,96,112);
  }
}
function tick(now){
  const delta=last?Math.min(100,now-last):0;last=now;
  if(ready&&!paused){
    elapsed+=delta;const duration=state==='subir'||state==='bajar'?1000/12:100;
    while(elapsed>=duration){
      elapsed-=duration;frame++;
      if(frame>=images[state].width/96){
        if(state==='subir'){setState('sostener');break}
        if(state==='bajar'){setState('reposo');break}
        frame=0;
      }
    }
    update();draw();
  }
  requestAnimationFrame(tick);
}
offer.onclick=()=>{paused=false;setState('subir',pose());draw()};
lower.onclick=()=>{paused=false;setState('bajar',6-pose());draw()};
pause.onclick=()=>{paused=!paused;update()};
scrub.oninput=()=>{paused=true;setState('subir',+scrub.value);draw()};
view.onchange=resize;scale.onchange=resize;
Promise.all(Object.entries(paths).map(([name,path])=>new Promise((resolve,reject)=>{
  const img=new Image();img.onload=()=>{images[name]=img;resolve()};img.onerror=()=>reject(new Error(`No se pudo cargar ${path}.png`));img.src=`out/${path}.png`;
}))).then(()=>{ready=true;resize();update();requestAnimationFrame(tick)}).catch(e=>{document.getElementById('error').textContent=e.message});
