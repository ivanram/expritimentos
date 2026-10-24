// Spanish Simulator — prueba original de claude-pxl, 24-10-2026.
// Resolución nativa. Ninguna imagen importada ni reescalada para dibujar.
// Luz cálida arriba a la izquierda; cámara 3/4 suave, personaje sentado.
pal({
  k: '#302536', h: '#352c32', H: '#614045', J: '#98614f',
  S: '#985954', s: '#ca8065', f: '#eaaa7b', F: '#ffd39b',
  e: '#3a2940', w: '#fff1ce', r: '#c85b55', R: '#813e4c',
  o: '#dd9a4c', O: '#a26340', Y: '#f2c66c', d: '#65444a',
  b: '#668d99', B: '#416574', n: '#304453', l: '#9cb4b1',
  t: '#244c50', T: '#37706c', g: '#8b9c6e', G: '#536b55',
  q: '#538ca6', Q: '#32607f', c: '#9ed4cb', a: '#d8b398',
  v: '#c48a6a', V: '#a36c5a', z: '#222c37', j: '#79575d',
});
ramps('kSsfF', 'khHJ', 'kdOoY', 'knBbl', 'kRrw', 'kQqc');

const POSES = [
  { elbow: [59, 67], hand: [69, 68], lean: 0 },
  { elbow: [60, 67], hand: [68, 70], lean: 0 }, // pequeña anticipación
  { elbow: [62, 62], hand: [74, 58], lean: 0 },
  { elbow: [65, 56], hand: [77, 45], lean: -1 },
  { elbow: [66, 49], hand: [75, 31], lean: -1 },
  { elbow: [65, 45], hand: [70, 22], lean: -1 },
  { elbow: [64, 46], hand: [69, 24], lean: -1 }, // asentamiento
];
// Ciclo de demostración: reposo, subir, sostener, bajar. 3,6 segundos a 10 fps.
const TIMELINE = [0,0,0,0,0,0,1,2,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,4,3,2,1,0,0,0,0,0,0];

function legs(c, flat = false) {
  // Pierna lejana recogida, rodilla cercana abierta: siluetas diferentes.
  c.poly([28,74,42,76,43,84,33,94,34,100,26,101,22,94,27,84,22,81], flat ? 'Q' : 'B');
  if (!flat) {
    c.poly([29,78,36,80,35,86,28,94,29,98,26,97,25,93], 'b');
    c.line(31,86,28,91,'n');
  }
  c.poly([35,73,48,74,59,81,60,89,55,99,47,100,48,91,48,87,36,85,29,81], flat ? 'q' : 'b');
  if (!flat) {
    c.poly([38,76,47,77,55,82,55,87,51,93,48,93,50,85,38,82], 'l');
    c.poly([46,86,51,87,48,97,53,98,56,91,58,88,58,84,55,83], 'B');
    c.line(31,78,38,82,'B');
    c.line(49,95,53,96,'n');
  }
  // Calcetines y zapatillas, un pie apoyado más atrás que el otro.
  c.poly([26,98,33,98,33,102,25,103], flat ? 'w' : 'w');
  c.poly([46,98,54,97,55,101,46,103], 'w');
  c.poly([25,101,33,101,37,104,36,107,22,107,21,105], flat ? 'r' : 'R');
  c.poly([46,101,54,100,59,103,62,104,62,107,44,107,43,105], flat ? 'r' : 'r');
  if (!flat) {
    c.line(23,106,35,106,'w'); c.line(45,106,61,106,'w');
    c.line(26,102,30,103,'r'); c.line(47,102,51,103,'w');
    c.line(48,100,52,101,'k');
  }
}

function torso(c, dx, flat = false) {
  const p = (pts, key) => c.poly(pts.map((v,i) => i % 2 ? v : v + dx), key);
  p([31,48,41,47,48,50,51,57,49,67,53,76,46,80,32,79,24,75,26,66,24,56,27,51], flat ? 'o' : 'O');
  if (flat) return;
  p([29,51,34,51,36,59,35,76,28,74,29,64,27,58], 'o');
  p([42,50,47,53,48,59,46,65,49,75,42,77,39,68,39,57], 'o');
  p([33,51,41,50,42,57,40,65,42,77,34,77,35,63], 'w');
  c.line(35+dx,60,40+dx,60,'r'); c.line(35+dx,66,40+dx,66,'r');
  c.line(35+dx,72,40+dx,72,'r');
  p([29,51,33,50,35,56,31,61,30,56], 'Y');
  p([42,50,46,52,44,59,41,56], 'Y');
  c.line(27+dx,65,29+dx,70,'d');
  c.line(44+dx,66,47+dx,65,'O'); c.line(44+dx,67,47+dx,66,'Y');
  c.px(43+dx,61,'Y'); c.px(44+dx,71,'Y');
  // Cuello dentro del cuello de la camisa: sin separación ni aro negro.
  p([33,44,42,44,42,49,39,53,35,52,33,49], 's');
  p([34,45,40,45,40,49,37,50,34,48], 'f');
}

function head(c, dx, blink = false, flat = false, happy = false) {
  const x = 23 + dx, y = 17;
  if (flat) { c.poly([x+5,y+3,x+23,y,x+30,y+8,x+28,y+26,x+19,y+32,x+8,y+29,x+2,y+20,x,y+10], 'Y'); return; }
  // Volumen posterior conectado, bajo cara y flequillo.
  c.poly([x+5,y+4,x+10,y+1,x+22,y+1,x+28,y+6,x+30,y+15,x+27,y+25,x+22,y+28,x+8,y+27,x+2,y+20,x+1,y+10], 'h');
  c.poly([x+6,y+12,x+12,y+7,x+23,y+9,x+27,y+15,x+26,y+25,x+21,y+30,x+13,y+31,x+7,y+28,x+4,y+23,x+1,y+21,x+4,y+18], 'S');
  c.poly([x+6,y+12,x+13,y+8,x+23,y+11,x+24,y+19,x+23,y+26,x+18,y+29,x+12,y+28,x+7,y+24,x+3,y+21,x+6,y+18], 'f');
  c.poly([x+8,y+14,x+15,y+11,x+21,y+13,x+20,y+17,x+14,y+18,x+12,y+22,x+7,y+20], 'F');
  c.ellipse(x+25,y+20,3,4,'s'); c.line(x+26,y+19,x+25,y+21,'S');
  // Rizos en masas pequeñas; no ruido ni pelo separado del cráneo.
  c.grid(x,y,`
........hhhhh.................
......hhHHHHhhhh..hhh.........
....hhHHJJHHHhHHhhHHHh........
...hHHJJHHHHHHHHHHJJHHh.......
..hHHJHHHhhHHJJHHHHHHHHh......
.hHHHHHhhHHhHHHHhhhHHHHHh.....
hHHHhhHHJJHHHHhhHHHHHHHh......
hHHhHHHHHHHHhhHHJJHHHHHHh.....
hHHHHHhhHHHhhHHHHHHHHHHHh.....
.hHHhhHHHHhhHHHhhHHhhHHHh.....
.hHhhHHHh..hHHh..hHH.hHHh.....
..hhHHHh....hh....hHh.hHHh....
..hHHHh...........hh..hHHh....
..hHHh.................hHh....
...hh..................hHh....
...h...................hh.....`);
  c.line(x+7,y+17,x+10,y+16,'H'); c.line(x+17,y+16,x+21,y+17,'H');
  if (blink) {
    c.line(x+7,y+19,x+10,y+19,'e'); c.line(x+17,y+19,x+20,y+20,'e');
  } else {
    c.grid(x+6,y+18,'eeee.......eee\nweew.......wee\n.eew.......ee.');
  }
  // Nariz y sonrisa desplazadas hacia el compañero de la izquierda.
  c.line(x+12,y+20,x+11,y+23,'s'); c.line(x+11,y+23,x+14,y+23,'S');
  c.line(x+8,y+25,x+16,y+26,'R');
  if (happy) { c.line(x+9,y+25,x+16,y+25,'w'); c.line(x+11,y+27,x+15,y+27,'R'); }
  else { c.line(x+10,y+25,x+14,y+25,'w'); }
  c.px(x+7,y+23,'r'); c.line(x+20,y+23,x+22,y+23,'s');
  c.ellipse(x+26,y+25,2,3,'Y',true); c.px(x+26,y+22,'w');
}

function restingArm(c, dx, flat = false) {
  // Brazo lejano apoyado hacia la mesa; manga y mano se solapan.
  c.poly([26+dx,52,29+dx,58,25+dx,65,18,69,12,68,12,63,20,61,22+dx,54], flat ? 'r' : 'O');
  if (!flat) {
    c.poly([25+dx,53,27+dx,57,23+dx,62,20,64,17,63,22+dx,58], 'o');
    c.line(18,63,20,66,'Y');
  }
  c.poly([17,63,19,67,14,70,9,69,7,67,9,64,12,65,13,62], flat ? 'F' : 'f');
  if (!flat) { c.line(9,66,13,67,'F'); c.line(10,69,14,69,'s'); }
}

function payingArm(c, pose, flat = false) {
  const shoulder = [46 + pose.lean,54], [ex,ey] = pose.elbow, [hx,hy] = pose.hand;
  // La pose entera se dibuja de nuevo. No se rotan recortes ni se contornea cada hueso.
  c.capsule(...shoulder,5,ex,ey,4,flat ? 'r' : 'dOoY',{light:[-0.6,-1],rim:false});
  c.capsule(ex,ey,3.7,hx,hy,3.1,flat ? 'F' : 'SsfF',{light:[-0.6,-1],rim:false});
  if (!flat) {
    const vx=hx-ex, vy=hy-ey, len=Math.hypot(vx,vy), nx=-vy/len, ny=vx/len;
    c.line(Math.round(ex+nx*2),Math.round(ey+ny*2),Math.round(ex-nx*2),Math.round(ey-ny*2),'o');
  }
}

// La tarjeta tiene pivote en el punto de agarre. La mano se pinta encima.
sprite('_tarjeta', {w:14,h:10,pivot:[7,8]},
  poly([1,0,12,0,13,1,13,8,12,9,1,9,0,8,0,1],'Q'),
  rect(1,1,11,6,'q'), rect(1,1,11,1,'c'), rect(2,4,3,2,'Y'),
  line(7,6,10,6,'c'), px(11,7,'w'));

function grip(c, pose, flat = false) {
  const [hx,hy] = pose.hand;
  c.poly([hx-4,hy-1,hx-1,hy-3,hx+2,hy-2,hx+3,hy+1,hx+1,hy+4,hx-3,hy+3],flat ? 'F' : 'f');
  if (!flat) { c.line(hx-3,hy-1,hx,hy-1,'F'); c.line(hx+1,hy,hx+1,hy+2,'s'); }
}

for(let i=0;i<POSES.length;i++) {
  const pose=POSES[i];
  sprite(`_brazo_${i}`,{w:94,h:110,sockets:{mano:pose.hand}},c=>payingArm(c,pose));
  sprite(`_brazo_bloques_${i}`,{w:94,h:110,sockets:{mano:pose.hand}},c=>payingArm(c,pose,true));
}

function actorItems(poseIndex, flat = false, blink = false, happy = false) {
  const pose = POSES[poseIndex];
  return [
    layer('piernas', c=>legs(c,flat)),
    layer('brazo_apoyado', c=>restingArm(c,pose.lean,flat)),
    layer('torso', c=>torso(c,pose.lean,flat)),
    layer('cabeza', c=>head(c,pose.lean,blink,flat,happy)),
    layer('brazo_pago', {sort:'z'}, stamp(`_brazo_${flat?'bloques_':''}${poseIndex}`,0,0,{id:'brazo'}),
      stamp('_tarjeta',0,0,{at:'brazo.mano',id:'tarjeta'})),
    layer('agarre', c=>grip(c,pose,flat)),
  ];
}

for (let i=0;i<POSES.length;i++) {
  sprite(`pose_${i}`,{w:94,h:110,outline:'k',pivot:[41,108]},...actorItems(i));
  sprite(`bloques_${i}`,{w:94,h:110,pivot:[41,108]},...actorItems(i,true));
}
function characterAnimation(name, timeline, fps=10) {
  anim(name,{w:94,h:110,outline:'k',frames:timeline.length,fps,pivot:[41,108],layers:true},
  ...['piernas','brazo_apoyado','torso','cabeza','brazo_pago','tarjeta','agarre'].map(part=>layer(part,c=>{
    const poseIndex=timeline[c.frame], pose = POSES[poseIndex];
    if(part==='piernas') legs(c);
    if(part==='brazo_apoyado') restingArm(c,pose.lean);
    if(part==='torso') torso(c,pose.lean);
    if(part==='cabeza') head(c,pose.lean,timeline.length>12 && (c.frame===3 || c.frame===4),false,poseIndex>=4);
    if(part==='brazo_pago') c.stamp(`_brazo_${poseIndex}`,0,0,{id:'brazo'});
    if(part==='tarjeta') c.stamp('_tarjeta',0,0,{at:'brazo.mano'});
    if(part==='agarre') grip(c,pose);
  })));
}
characterAnimation('pago',TIMELINE);
characterAnimation('reposo',Array(24).fill(0));
characterAnimation('subir',[0,1,2,3,4,5,6],12);
characterAnimation('sostener',Array(24).fill(6));
characterAnimation('bajar',[6,5,4,3,2,1,0],12);
sheet('personaje',['reposo','subir','sostener','bajar'],{rows:'tag',pad:1});

// Vigneta pequeña de contexto. Elipse de mesa y platos comparten inclinación.
sprite('silla',{w:53,h:71}, c=>{
  c.poly([4,3,8,0,42,2,46,7,41,43,48,66,44,69,36,45,12,44,6,70,2,70,6,41], 'k');
  c.poly([8,4,40,6,39,11,8,9], 'O'); c.line(9,5,38,7,'o');
  c.poly([8,12,12,12,13,37,8,38], 'd');
  c.poly([36,13,40,13,37,38,33,38], 'd');
  c.line(9,16,36,18,'O'); c.line(9,25,35,27,'O');
  c.poly([6,37,36,38,43,44,8,46,2,42], 'O');
  c.line(5,40,36,41,'o'); c.line(8,45,41,44,'d');
  c.line(7,47,4,68,'O'); c.line(38,47,45,66,'O');
});
sprite('mesa',{w:120,h:61}, c=>{
  c.poly([55,25,63,25,64,50,79,55,79,59,44,59,42,56,54,50], 'k');
  c.poly([58,27,61,27,61,52,73,56,49,56,58,51], 'd');
  c.line(59,30,59,50,'j');
  c.ellipse(60,22,57,20,'k');
  c.ellipse(60,20,56,18,'d');
  c.ellipse(60,17,56,17,'O');
  c.ellipse(60,15,55,15,'o');
  c.ellipse(59,13,51,12,'Y');
  c.ellipse(59,14,50,11,'o');
  c.line(14,12,106,12,'Y'); c.line(8,19,111,19,'O');
  c.line(23,25,98,25,'O'); c.line(37,4,38,10,'O');
  c.line(82,13,81,18,'O'); c.line(48,20,47,26,'Y');
  c.line(20,29,38,33,'o'); c.line(76,32,99,28,'Y');
});
sprite('croquetas',{w:32,h:16}, c=>{
  c.ellipse(16,9,15,6,'d'); c.ellipse(16,7,15,6,'a');
  c.ellipse(16,6,14,5,'w'); c.ellipse(16,6,11,3,'a');
  for(const [x,y] of [[9,5],[17,3],[22,7]]) {
    c.ellipse(x,y+1,5,3,'O'); c.ellipse(x,y,4,2,'o');
    c.line(x-2,y-1,x,y-1,'Y'); c.px(x+2,y,'d');
  }
});
sprite('aceitunas',{w:22,h:13}, c=>{
  c.ellipse(11,7,10,5,'d'); c.ellipse(11,6,10,5,'r');
  c.ellipse(11,5,8,3,'R');
  for(const [x,y] of [[7,4],[12,3],[15,6],[9,7]]) {
    c.ellipse(x,y,3,2,'G'); c.line(x-1,y-1,x,y-1,'g'); c.px(x+1,y,'t');
  }
  c.line(4,9,14,10,'o');
});
sprite('fondo',{w:208,h:144},c=>{
  // Pared cálida y zócalo. Sin ruido de relleno ni gradientes de alta resolución.
  c.rect(0,0,208,93,'V'); c.rect(0,0,105,80,'v');
  c.poly([0,0,129,0,111,72,0,77],'a');
  c.rect(0,77,208,26,'t'); c.line(0,77,207,77,'Y');
  c.line(0,80,207,80,'d');
  for(let x=0;x<208;x+=16) {
    c.line(x,82,x,99,'T');
    c.poly([x+8,84,x+12,89,x+8,94,x+4,89],'T');
    c.px(x+8,86,'g');
  }
  c.rect(0,101,208,43,'j'); c.line(0,101,207,101,'d');
  // Ventana arqueada pequeña con profundidad y cielo azul de tarde.
  c.rect(12,25,48,41,'d'); c.ellipse(36,25,24,20,'d');
  c.rect(16,26,40,35,'n'); c.ellipse(36,25,20,16,'n');
  c.rect(20,27,32,31,'Q'); c.ellipse(36,26,16,12,'Q');
  c.poly([20,43,25,36,31,42,38,32,46,43,52,36,52,58,20,58],'B');
  c.rect(34,13,3,48,'O'); c.rect(18,41,36,3,'O');
  c.rect(10,62,52,5,'d'); c.line(11,62,60,62,'o');
  c.rect(24,46,2,3,'Y'); c.rect(43,43,2,3,'Y');
  // Cuadro torcido y enredadera: asimetría deliberada.
  c.poly([78,19,108,21,106,52,76,50],'d');
  c.poly([81,23,104,25,102,48,80,46],'Y');
  c.ellipse(91,35,7,7,'r'); c.line(92,26,94,28,'G');
  c.line(197,0,192,48,'G');
  for(const [x,y] of [[193,8],[188,18],[193,26],[184,35],[188,44]]) {
    c.ellipse(x,y,4,2,'G'); c.line(x-2,y-1,x,y-1,'g');
  }
  // Baldosas convergen hacia el horizonte, por encima del tablero.
  c.line(0,119,207,119,'d'); c.line(0,141,207,141,'d');
  c.line(54,102,31,143,'d'); c.line(146,102,172,143,'d');
  c.line(101,102,100,143,'d');
});
sprite('sombras',{w:208,h:144},ellipse(70,136,44,5,'d'),ellipse(140,136,34,4,'d'));
scene('contexto',{w:208,h:144,frames:36,fps:10},
  layer('fondo',stamp('fondo',0,0)),
  layer('sombras',stamp('sombras',0,0)),
  layer('silla',stamp('silla',117,64)),
  layer('mesa',stamp('mesa',8,81)),
  layer('personaje',stamp('pago',142,137)),
  layer('tapas',stamp('croquetas',39,93),stamp('aceitunas',78,91)));
