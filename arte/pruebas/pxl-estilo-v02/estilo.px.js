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

// Cada brazo es una pose de píxeles nueva; mismo hombro y tamaño de mano.
const ARM_POSES=[
  {hand:[25,34],rows:{27:[[21,'Rrr']],28:[[22,'rrr']],29:[[22,'Rrr']],30:[[23,'rr']],31:[[23,'rs']],32:[[23,'sff']],33:[[24,'ff']],34:[[24,'sf']]}},
  {hand:[27,32],rows:{27:[[21,'Rrr']],28:[[22,'rrr']],29:[[23,'rrr']],30:[[24,'rss']],31:[[25,'sff']],32:[[26,'sf']]}},
  {hand:[29,28],rows:{27:[[21,'Rrr'],[28,'sf']],28:[[22,'Rrr'],[28,'ff']],29:[[23,'Rrr'],[27,'ff']],30:[[24,'rrsff']],31:[[25,'rss']]}},
  {hand:[29,22],rows:{22:[[28,'sf']],23:[[28,'ff']],24:[[28,'ff']],25:[[28,'ff']],26:[[28,'ff']],27:[[21,'Rrr'],[28,'sf']],28:[[22,'Rrr'],[27,'ff']],29:[[23,'Rrrffs']],30:[[24,'rrss']]}},
  {hand:[27,16],rows:{16:[[26,'sf']],17:[[26,'ff']],18:[[26,'ff']],19:[[26,'ff']],20:[[26,'ff']],21:[[26,'ff']],22:[[26,'ff']],23:[[26,'ff']],24:[[26,'ff']],25:[[26,'ff']],26:[[26,'ff']],27:[[21,'Rrr'],[26,'sf']],28:[[22,'Rrrfs']],29:[[23,'rss']]}},
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
  sprite(`_nora_brazo_${i}`,{w:32,h:56,sockets:{mano:pose.hand}},runs(pose.rows));
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
const LOOP=[0,0,0,0,0,0,1,2,3,4,4,4,4,4,4,4,4,3,2,1,0,0,0,0];
anim('pago',{w:36,h:56,frames:24,fps:8,layers:true},
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
scene('poses',{w:218,h:78,bg:'a'},
  stamp('nora_0',8,13),stamp('nora_1',50,13),stamp('nora_2',92,13),stamp('nora_3',134,13),stamp('nora_4',176,13));
scene('animacion',{w:166,h:78,bg:'a'},
  stamp('ines',18,19),stamp('pago',66,13),stamp('teo',113,19));
sheet('personajes',['ines','nora_0','teo'],{pad:2});
