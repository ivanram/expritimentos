// Spanish Simulator · estudio de estilo 2D a partir de la referencia de Ivan R.
// Originales dibujados a 1× mediante cuadrículas. Sin modelo 3D, gradientes,
// cápsulas, escalado de ilustraciones ni contorno automático alrededor de piezas.
pal({
  k:'#1d2324', h:'#303436', H:'#4a4945',
  s:'#d47736', f:'#fbb654', F:'#ffe799',
  r:'#c3361b', R:'#8b2727', o:'#f37029',
  t:'#384b51', T:'#607c78', l:'#9aafa2',
  b:'#3d6a84', B:'#1e3644', w:'#ffeece',
  g:'#75795a', G:'#4c5041',
  d:'#8a4120', D:'#5b2415', y:'#e1a022',
  a:'#c1b8c3', p:'#aa9fac', q:'#538e9f',
});
const gridRows=rows=>rows.map(row=>row.padEnd(32,'.')).join('\n');

// Nora: pelo corto despeinado, cazadora roja, camiseta oscura, pantalón oliva.
// Unos 46 px de alto. La cabeza se apoya directamente sobre el cuello/camiseta.
const NORA_HEAD=gridRows([
'..............kk',
'.............khk',
'..........kkkhhhkk',
'.........khhhhhhhhk',
'........khhHhhhhhhhk',
'........khHhhhhhhhhhk',
'.......khhhhhhhhhhhhk',
'........khhhhhhhhhhhhk',
'.......khhhhshhhhhhhhk',
'........khhfsfffshhhhk',
'........khfFFfffshhhkk',
'.........hfFFfffffhkhk',
'.........fsFffffffhfk',
'.........fsFkfffkffs',
'..........sFffffffs',
'..........sFffffsfs',
'...........sFfffFs',
'............ssffs',
'.............sk',
]);
const NORA_BODY=gridRows([
'...........Rrskkkk',
'..........Rorrtkktrk',
'.........RorrttktrRrk',
'........RorrtttkttrRrk',
'........RrrrtttkttRrrk',
'........RrrttttkttRrrk',
'........RrrttttktRRrk',
'.........RrrtttkRRRrk',
'.........RRrtttkRRRrk',
'.........RRrtkkkRRRk',
'.........RRrtkkkRRRk',
'..........RrrttkRRrk',
'..........RrrttkRrk',
'...........RrkkkRrk',
'...........GggggggG',
'...........GggggggG',
'...........GgggggG',
'...........GggGggG',
'............ggGGgg',
'............ggkGgg',
'............ggk.Gg',
'...........Ggg..Gg',
'...........Ggg...gg',
'...........sf....sf',
'...........sf....sf',
'...........kk....kk',
'..........kkk....kkk',
'..........kk.....kkk',
]);

// Hombro (19,27). El codo también sube: dos segmentos de unos 6–7 px.
// Las coordenadas de codo sirven para revisar el gesto, no para rotar recortes.
// Manga de cuatro píxeles, antebrazo de tres, muñeca de dos y pulgar en la tarjeta.
const ARM_POSES=[
  {elbow:[23,32],hand:[25,38],rows:{
    26:[[19,'rrR']],27:[[19,'rorr']],28:[[20,'rorr']],29:[[20,'Rrrr']],
    30:[[21,'Rrrr']],31:[[21,'Rrrr']],32:[[22,'Rssf']],
    33:[[22,'sff']],34:[[23,'sff']],35:[[23,'sff']],36:[[24,'sff']],
    37:[[24,'sff']],38:[[24,'sff']],39:[[25,'s']],
  }},
  {elbow:[25,30],hand:[30,34],rows:{
    26:[[19,'rrR']],27:[[19,'rorrr']],28:[[20,'Rrorrr']],
    29:[[21,'Rrrrff']],30:[[22,'RRrsfff']],31:[[24,'ssfff']],
    32:[[26,'sfff']],33:[[28,'sff']],34:[[29,'sff']],35:[[30,'s']],
  }},
  {elbow:[26,29],hand:[32,30],rows:{
    26:[[19,'rrR']],27:[[19,'rorrr']],28:[[20,'Rrorrrfff']],
    29:[[21,'Rrrrrfffffff']],30:[[23,'RRrssssfff']],31:[[30,'sf']],
  }},
  {elbow:[26,27],hand:[32,25],rows:{
    24:[[31,'sff']],25:[[19,'rrR'],[29,'ffff']],
    26:[[19,'rorrrrrfffff']],27:[[19,'Rrrrrrrffss']],
    28:[[20,'RRRRRsss']],
  }},
  {elbow:[26,25],hand:[31,20],rows:{
    20:[[30,'sff']],21:[[29,'sfff']],22:[[28,'sfff']],23:[[27,'sfff']],
    24:[[24,'rrrfff']],25:[[21,'rrorrffs']],26:[[19,'rrorrrs']],
    27:[[19,'RrrrrR']],28:[[20,'RRR']],
  }},
  {elbow:[25,23],hand:[28,17],rows:{
    17:[[27,'sff']],18:[[27,'sff']],19:[[26,'sfff']],
    20:[[26,'sff']],21:[[25,'sfff']],22:[[24,'rsff']],
    23:[[23,'rrrfs']],24:[[22,'rorrr']],25:[[20,'rrorr']],
    26:[[19,'rorrr']],27:[[19,'RrrR']],28:[[20,'RR']],
  }},
  {elbow:[24,22],hand:[26,15],rows:{
    15:[[25,'sff']],16:[[25,'sff']],17:[[25,'sff']],18:[[24,'sfff']],
    19:[[24,'sff']],20:[[23,'sfff']],21:[[23,'rsff']],
    22:[[22,'rrrfs']],23:[[21,'rorrr']],24:[[20,'rrorR']],
    25:[[19,'rrorR']],26:[[19,'rrrR']],27:[[19,'RrR']],
  }},
  {elbow:[23,21],hand:[24,14],rows:{
    14:[[23,'sff']],15:[[23,'sff']],16:[[23,'sff']],17:[[23,'sff']],
    18:[[22,'sfff']],19:[[22,'sff']],20:[[22,'rsff']],
    21:[[21,'rrrfs']],22:[[21,'rorR']],23:[[20,'rorr']],
    24:[[20,'rorR']],25:[[19,'rorR']],26:[[19,'rrrR']],27:[[19,'RrR']],
  }},
];
sprite('_nora_cabeza',{w:32,h:26},grid(0,5,NORA_HEAD));
sprite('_nora_cuerpo',{w:32,h:56,sockets:{hombro:[21,27]}},grid(0,24,NORA_BODY));
sprite('_nora_brazo_libre',{w:32,h:56},runs({
  27:[[9,'Rrr']],28:[[8,'Rorr']],29:[[8,'Rrrr']],30:[[7,'RRrr']],
  31:[[7,'Rrrr']],32:[[8,'Rrrfs']],33:[[9,'Rrfff']],34:[[11,'sf']],35:[[12,'f']],
}));
sprite('_tarjeta',{w:7,h:5,pivot:[3,4]},grid(0,0,'bbbbbb.\nbwwbbbB\nbbybbbB\nbbbbbbB\n.BBBBB.'));
for(let i=0;i<ARM_POSES.length;i++){
  const pose=ARM_POSES[i];
  sprite(`_nora_brazo_${i}`,{w:36,h:56,sockets:{mano:pose.hand}},runs(pose.rows));
  sprite(`nora_${i}`,{w:36,h:56,layers:true},
    layer('cuerpo',stamp('_nora_cuerpo',0,0)),
    layer('brazo_libre',stamp('_nora_brazo_libre',0,0)),
    layer('brazo_pago',stamp(`_nora_brazo_${i}`,0,0,{id:'brazo'})),
    layer('tarjeta',stamp('_tarjeta',0,0,{at:'brazo.mano'})),
    layer('agarre',px(pose.hand[0]-1,pose.hand[1]-1,'F'),px(pose.hand[0],pose.hand[1]-1,'f')),
    layer('cabeza',stamp('_nora_cabeza',0,0)));
}

// Inés: silueta corta, pelo cobre recogido, camisa crema y peto azul ancho.
sprite('ines',{w:32,h:56,layers:true},
  layer('silueta',grid(0,9,gridRows([
'.................dd',
'................dood',
'............ddddooood',
'..........dooooodddod',
'.........doooooooodd',
'........doooooooood',
'........doooofoooood',
'........doodfFfooodd',
'........doodFFffoood',
'........dodfFFffodod',
'.........ddfFfffdod',
'.........dffkffkfdd',
'..........ffFffffd',
'..........sFfffsf',
'...........sffFfs',
'............ssfs',
'...........Ttssk',
'..........TbbwFwbbk',
'.........TwbwwFwbbtk',
'........Twwbwwwbbttk',
'........Twwbwwwbbttk',
'........twwbbwwbbttk',
'........ttbbbbbbbtfk',
'.........fbbbbbbbsff',
'........sfbbbbbbbkff',
'........ffbbbbbbbk',
'.........fbbbbbbbbk',
'..........bbbbbbbk',
'..........bBbbbbbBk',
'..........bBbbbBbBk',
'...........BBB.BBk',
'...........BBB.BB',
'...........BBB.BB',
'............sf.Bf',
'............sf..f',
'............kk..kk',
'...........kkk..kkk',
]))));

// Teo: silueta esbelta, rizos grandes, chaleco verde y pantalón ocre estrecho.
sprite('teo',{w:32,h:56,layers:true},
  layer('silueta',grid(0,1,gridRows([
'..............DDD',
'............DDddDD',
'..........DDdddddDD',
'.........DddddddddDD',
'........DDddddddddddD',
'........DdddddddddddD',
'.......DDdddddddddddDD',
'.......DddddddddddddDD',
'........DddddfdddddDD',
'.......DDdddfffddddDD',
'........DddfffffdddD',
'........DddFFfffddDD',
'.........DdfFfffdDD',
'.........DsFkffkfs',
'..........sFfffffs',
'..........sFffffs',
'...........sffFs',
'............sfs',
'...........ttsk',
'..........ttwktt',
'.........tTtwkwtt',
'........ttTtwkwtttk',
'........ttTtwkwttTk',
'........ttTtwkwttTk',
'........ttTtwkwttTk',
'........ttttwkwttTk',
'.........tttwkwtttk',
'.........tsttttttfk',
'..........fftttttff',
'...........ftttttf',
'...........kggggggk',
'...........gogggggk',
'...........goggoggg',
'...........gogggog',
'...........gogkgog',
'...........gogkgog',
'............ogkgog',
'............ogkgog',
'............ogk.gog',
'............og...gog',
'............og...gog',
'............og....og',
'............sf....sf',
'............kk....kk',
'...........kkk....kkk',
]))));

// Poses discretas, con pausas: no interpolación ni rotaciones de muñecos.
const LOOP=[...Array(6).fill(0),1,2,3,4,5,6,...Array(10).fill(7),6,5,4,3,2,1,...Array(8).fill(0)];
anim('pago',{w:36,h:56,frames:LOOP.length,fps:12,layers:true},
  layer('cuerpo',stamp('_nora_cuerpo',0,0)),
  layer('brazo_libre',stamp('_nora_brazo_libre',0,0)),
  layer('brazo_pago',c=>c.stamp(`_nora_brazo_${LOOP[c.frame]}`,0,0,{id:'brazo'})),
  layer('tarjeta',stamp('_tarjeta',0,0,{at:'brazo.mano'})),
  layer('agarre',c=>{
    const hand=ARM_POSES[LOOP[c.frame]].hand;
    c.px(hand[0]-1,hand[1]-1,'F');c.px(hand[0],hand[1]-1,'f');
  }),
  layer('cabeza',stamp('_nora_cabeza',0,0)));
scene('amigos',{w:166,h:78,bg:'a'},
  stamp('ines',18,19),stamp('nora_0',66,13),stamp('teo',113,19));
scene('poses',{w:176,h:144,bg:'a'},
  ...ARM_POSES.map((_,i)=>stamp(`nora_${i}`,8+(i%4)*42,8+Math.floor(i/4)*70)));
scene('animacion',{w:166,h:78,bg:'a'},
  stamp('ines',18,19),stamp('pago',66,13),stamp('teo',113,19));
sheet('personajes',['ines','nora_0','teo'],{pad:2});
