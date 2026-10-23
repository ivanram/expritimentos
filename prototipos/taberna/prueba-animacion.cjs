const {test}=require('node:test');
const assert=require('node:assert/strict');
const {Actor}=require('./animacion.js');
const tick=(a,seconds)=>{for(let t=0;t<seconds;t+=.01)a.step(.01,false);};

test('cada actor mantiene su propio reloj, accion y pausa',()=>{
  const a=new Actor({id:'a'},0),b=new Actor({id:'b'},1);
  a.startPay();b.setAction('talk');tick(a,.3);tick(b,.3);
  assert(a.progress>0&&a.progress<1);assert.equal(b.progress,0);assert.equal(b.state,'talk');
  const before={clock:a.clock,progress:a.progress,frame:a.frame};
  a.paused=true;tick(a,.8);tick(b,.8);
  assert.deepEqual({clock:a.clock,progress:a.progress,frame:a.frame},before);
  assert(b.clock>1);assert.equal(b.state,'talk');
});
test('cada uno de los cinco actores admite los tres objetos sin cambiarlos durante el pago',()=>{
  for(let i=0;i<5;i++)for(const object of ['card','wallet','cash']){
    const a=new Actor({id:String(i)},i);assert(a.setObject(object));a.startPay();tick(a,1);
    assert.equal(a.state,'hold');assert.equal(a.progress,1);assert.equal(a.object,object);
    assert(!a.setObject(object==='card'?'wallet':'card'));tick(a,3);
    assert.equal(a.state,'hold');assert.equal(a.object,object);assert([25,26].includes(a.frame));
    a.stopPay();tick(a,.6);assert.equal(a.progress,0);assert.equal(a.state,'idle');assert(a.setObject('cash'));
  }
});
test('cancelar en cualquier punto de la subida baja desde la pose actual',()=>{
  for(const t of [.03,.15,.29,.44]){
    const a=new Actor({});a.startPay();tick(a,t);const before=a.progress;const frame=a.frame;
    a.stopPay();assert.equal(a.progress,before);assert.equal(a.frame,frame);a.step(.01);
    assert(a.progress<before);assert(a.frame<=frame);tick(a,.7);assert.equal(a.state,'idle');
  }
});
test('una accion ambiental solicitada durante el pago se ejecuta al bajar',()=>{
  const a=new Actor({});a.startPay();tick(a,1);a.setAction('talk');assert.equal(a.state,'lower');
  tick(a,.6);assert.equal(a.state,'talk');assert(a.frame>=4&&a.frame<=9);
});
test('comer termina en reposo y todos los indices de frame caben en la hoja',()=>{
  const a=new Actor({});a.setAction('eat');assert.equal(a.frame,10);tick(a,.6);assert(a.frame>=10&&a.frame<=15);
  tick(a,.8);assert.equal(a.state,'idle');
  for(let i=0;i<5;i++){const actor=new Actor({},i);for(let j=0;j<3000;j++){actor.step(.016,true);assert(actor.frame>=0&&actor.frame<27);}}
});
