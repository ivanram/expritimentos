/* Independent actor playback; uses exported native-resolution sprite sheets. */
(async function(){
  'use strict';
  const M=window.TABERNA,$=id=>document.getElementById(id),canvas=$('scene'),ctx=canvas.getContext('2d');
  const types=['card','wallet','cash'],typeNames={card:'tarjeta',wallet:'cartera',cash:'billetes'};
  const actions={idle:'En reposo',talk:'Charlando',eat:'Picando algo',raise:'Levantando la mano',hold:'Ofreciendo el pago',lower:'Bajando la mano'};
  const short={idle:'Reposo',talk:'Charla',eat:'Comida',raise:'Subiendo',hold:'Ofreciendo',lower:'Bajando'};
  const actors=M.people.map((p,i)=>new window.TabernaActor(p,i));
  let selected=0,globalPaused=false,ambient=true,speed=1,last=performance.now(),lastUI=0,assets={};
  function load(name){return new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=()=>reject(new Error('No se pudo cargar '+name));im.src='assets/'+name;});}
  function frameDraw(p,pass,frame){const sheet=assets[p.id+'_'+pass];ctx.drawImage(sheet,frame*M.cell.w,0,M.cell.w,M.cell.h,p.x,p.y,M.cell.w,M.cell.h);}
  function render(){
    ctx.imageSmoothingEnabled=false;ctx.clearRect(0,0,640,360);
    if($('show-bg').checked)ctx.drawImage(assets.background,0,0);
    else {for(let y=0;y<360;y+=12)for(let x=0;x<640;x+=12){ctx.fillStyle=((x+y)/12)%2?'#c8c5ba':'#dedbd0';ctx.fillRect(x,y,12,12);}}
    for(const a of actors)frameDraw(a.person,'body',a.frame);
    if($('show-table').checked){ctx.drawImage(assets.table,0,0);ctx.drawImage(assets.table_props,0,0);}
    for(const a of actors){
      const p=a.person,fi=a.frame,anchor=p.anchors[fi];frameDraw(p,'arm',fi);
      if(anchor.visible){
        const index=types.indexOf(a.object);
        ctx.drawImage(assets.payment_props,index*24,0,24,24,p.x+anchor.x-12,p.y+anchor.y-11,24,24);
        frameDraw(p,'grip_'+a.object,fi);
      }
      if($('show-anchors').checked){ctx.strokeStyle='#efeed1';ctx.lineWidth=1;const x=p.x+anchor.x,y=p.y+anchor.y;ctx.strokeRect(x-3.5,y-3.5,7,7);ctx.beginPath();ctx.moveTo(x-7,y+.5);ctx.lineTo(x+7,y+.5);ctx.moveTo(x+.5,y-7);ctx.lineTo(x+.5,y+7);ctx.stroke();}
    }
    const p=actors[selected].person;
    ctx.fillStyle='#e5d49d';ctx.fillRect(p.x+43,335,26,2);
    ctx.fillStyle=p.color;ctx.fillRect(p.x+49,339,14,2);
  }
  function ui(){
    const a=actors[selected];$('selected-name').textContent=a.person.name;$('person-number').textContent=String(selected+1).padStart(2,'0');
    const status=(a.paused?'En pausa · ':'')+actions[a.state]+((a.intent||a.progress>0)?' · '+typeNames[a.object]:'');
    if($('actor-status').textContent!==status)$('actor-status').textContent=status;
    const pay=$('pay');pay.classList.toggle('raised',a.intent);pay.innerHTML=a.intent?'Bajar la mano <span>↓</span>':'Yo invito <span>↑</span>';pay.disabled=a.paused;
    $('freeze').textContent=a.paused?'▶ Reanudar personaje':'Ⅱ Pausar personaje';$('freeze').setAttribute('aria-pressed',String(a.paused));
    document.querySelectorAll('[data-action]').forEach(b=>{b.classList.toggle('active',!a.intent&&a.progress===0&&a.mode===b.dataset.action);b.disabled=a.paused;});
    document.querySelectorAll('[data-object]').forEach(b=>{b.classList.toggle('active',a.object===b.dataset.object);b.setAttribute('aria-pressed',String(a.object===b.dataset.object));b.disabled=a.intent||a.progress>0;});
    $('object-hint').textContent=(a.intent||a.progress>0)?'Baja la mano antes de cambiar el objeto.':'El objeto acompaña a su mano durante todo el gesto.';
    document.querySelectorAll('.person').forEach((b,i)=>{b.classList.toggle('active',i===selected);b.setAttribute('aria-pressed',String(i===selected));b.querySelector('small').textContent=actors[i].paused?'En pausa':short[actors[i].state];});
    $('telemetry').innerHTML=actors.map((x,i)=>`<tr class="${selected===i?'selected':''}"><td>${x.person.name}</td><td>${x.paused?'Pausa':short[x.state]}</td><td>${x.frame+1}/27</td></tr>`).join('');
    $('pause-all').textContent=globalPaused?'▶ Reanudar escena':'Ⅱ Pausar escena';$('pause-all').setAttribute('aria-pressed',String(globalPaused));
  }
  function select(i){selected=i;ui();render();}
  function mixed(){
    ambient=false;$('ambient').checked=false;
    actors.forEach(a=>a.reset());
    actors[0].setAction('talk');actors[1].setAction('eat');
    actors.slice(2).forEach((a,i)=>{a.setObject(types[i]);a.startPay();});
    globalPaused=false;ui();
  }
  function tick(now){const dt=Math.min((now-last)/1000,.05)*speed;last=now;if(!globalPaused)actors.forEach(a=>a.step(dt,ambient));render();if(now-lastUI>120){ui();lastUI=now;}requestAnimationFrame(tick);}
  try{
    const staticNames=['background','table','table_props','payment_props'];
    const entries=[...staticNames,...M.people.flatMap(p=>M.passes.map(layer=>p.id+'_'+layer))];
    const loaded=await Promise.all(entries.map(async name=>[name,await load(name+'.png')]));assets=Object.fromEntries(loaded);
    for(const p of M.people){for(const pass of M.passes){const im=assets[p.id+'_'+pass];if(im.width!==M.frames*M.cell.w||im.height!==M.cell.h)throw new Error('Hoja de sprites con dimensiones inesperadas: '+p.id+'_'+pass);}}
    $('people').innerHTML=M.people.map((p,i)=>`<button class="person ${i===0?'active':''}" data-person="${i}" aria-pressed="${i===0}" aria-label="Seleccionar a ${p.name}"><span class="number">0${i+1}</span><canvas width="48" height="58" aria-hidden="true"></canvas><span><strong>${p.name}</strong><small>Reposo</small></span></button>`).join('');
    document.querySelectorAll('.person').forEach((b,i)=>{const cx=b.querySelector('canvas').getContext('2d');cx.imageSmoothingEnabled=false;cx.drawImage(assets[M.people[i].id+'_body'],30,38,52,63,0,0,48,58);b.addEventListener('click',()=>select(i));});
    document.querySelectorAll('[data-action]').forEach(b=>b.addEventListener('click',()=>{actors[selected].setAction(b.dataset.action);ui();}));
    document.querySelectorAll('[data-object]').forEach(b=>b.addEventListener('click',()=>{actors[selected].setObject(b.dataset.object);ui();}));
    $('pay').addEventListener('click',()=>{const a=actors[selected];a.intent?a.stopPay():a.startPay();ui();});
    $('freeze').addEventListener('click',()=>{actors[selected].paused=!actors[selected].paused;ui();});
    $('pause-all').addEventListener('click',()=>{globalPaused=!globalPaused;ui();});
    $('ambient').addEventListener('change',e=>{ambient=e.target.checked;if(ambient)actors.forEach(a=>{a.manual=false;a.nextAmbient=a.clock+1+a.index*.45;});});
    $('speed').addEventListener('change',e=>{speed=Number(e.target.value);});
    $('mixed').addEventListener('click',mixed);
    $('reset').addEventListener('click',()=>{actors.forEach(a=>a.reset());ambient=true;$('ambient').checked=true;globalPaused=false;speed=1;$('speed').value='1';ui();});
    canvas.addEventListener('pointerdown',e=>{const rect=canvas.getBoundingClientRect();const x=(e.clientX-rect.left)/rect.width*640;let i=0;let nearest=Infinity;actors.forEach((a,index)=>{const distance=Math.abs(x-(a.person.x+56));if(distance<nearest){i=index;nearest=distance;}});select(i);});
    let spaceActor=null;
    document.addEventListener('keydown',e=>{if(['INPUT','SELECT','TEXTAREA'].includes(e.target.tagName))return;if(/^[1-5]$/.test(e.key)){select(Number(e.key)-1);return;}if(e.code==='Space'&&!e.repeat&&e.target.tagName!=='BUTTON'){e.preventDefault();spaceActor=actors[selected];if(!spaceActor.paused)spaceActor.startPay();ui();}});
    document.addEventListener('keyup',e=>{if(e.code==='Space'&&spaceActor){e.preventDefault();spaceActor.stopPay();spaceActor=null;ui();}});
    window.addEventListener('blur',()=>{if(spaceActor){spaceActor.stopPay();spaceActor=null;}});
    actors[1].mode='talk';actors[2].mode='eat';actors[3].intent=true;actors[3].progress=.5;
    $('loading').remove();ui();last=performance.now();requestAnimationFrame(tick);
  }catch(error){$('loading').textContent='No se pudo preparar la escena.';$('error').hidden=false;$('error').textContent=error.message;console.error(error);}
})();
