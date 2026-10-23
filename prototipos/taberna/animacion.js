(function(root){
  'use strict';
  class Actor {
    constructor(person,index=0){this.person=person;this.index=index;this.reset();}
    reset(){this.mode='idle';this.afterPay='idle';this.clock=this.index*.317;this.elapsed=0;this.progress=0;this.intent=false;this.object=['card','wallet','cash'][this.index%3];this.paused=false;this.manual=false;this.nextAmbient=1.3+this.index*1.12;this.ambientCount=0;}
    setAction(mode){if(!['idle','talk','eat'].includes(mode))return;this.manual=true;this.mode=mode;this.afterPay=mode;this.elapsed=0;this.intent=false;}
    setObject(value){if(!['card','wallet','cash'].includes(value)||this.progress>0||this.intent)return false;this.object=value;return true;}
    startPay(){this.manual=true;this.afterPay='idle';this.intent=true;}
    stopPay(){this.manual=true;this.afterPay='idle';this.intent=false;}
    step(dt,ambient=false){
      if(this.paused)return;
      this.clock+=dt;this.elapsed+=dt;
      const old=this.progress;
      this.progress=Math.min(1,Math.max(0,this.progress+(this.intent?dt/.56:-dt/.5)));
      if(old>0&&this.progress===0){this.mode=this.afterPay;this.elapsed=0;}
      if(ambient&&!this.manual&&this.clock>this.nextAmbient){
        this.ambientCount++;this.nextAmbient=this.clock+2.5+(this.index%3)*.55;
        const state=(this.ambientCount+this.index)%5;
        if(state===3){this.intent=true;this.nextAmbient=this.clock+1.8;}
        else if(this.intent){this.intent=false;}
        else {this.mode=['idle','talk','eat','idle','talk'][state];this.elapsed=0;}
      }
      if(this.mode==='eat'&&this.elapsed>1.1&&this.progress===0){this.mode='idle';this.elapsed=0;}
    }
    get frame(){
      if(this.progress>=1)return this.clock%3.92>=3.8?26:25;
      if(this.progress>0||this.intent)return 16+Math.round(this.progress*8);
      if(this.mode==='talk')return 4+Math.floor(this.elapsed/.13)%6;
      if(this.mode==='eat')return 10+Math.min(5,Math.floor(this.elapsed/.17));
      const t=this.clock%2;return t<1.2?0:t<1.5?1:t<1.6?2:3;
    }
    get state(){return this.intent?(this.progress===1?'hold':'raise'):this.progress>0?'lower':this.mode;}
  }
  if(typeof module!=='undefined'&&module.exports)module.exports={Actor};
  else root.TabernaActor=Actor;
})(typeof window!=='undefined'?window:globalThis);
