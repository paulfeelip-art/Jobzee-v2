const fs=require('fs');
function load(f){const src=fs.readFileSync(f,'utf8');const js=src.match(/data-dc-script[^>]*>([\s\S]*?)<\/script>/)[1];
 const DCLogic=class{constructor(p){this.props=p||{};this.state={}} setState(o){Object.assign(this.state,typeof o==='function'?o(this.state):o)}};
 const C=new Function('DCLogic','return ('+js.replace('class Component','class')+')')(DCLogic); return new C({});}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
function dump(c,label){const v=c.renderVals();console.log('--- '+label+' | view='+(v.isList?'list':'thread')+' sub="'+v.sub+'" quick=['+v.quick.map(q=>q.text).join(', ')+']');
 if(v.isThread||!v.isList) v.msgs.forEach(m=>console.log((m.isText? (m.style.includes('brand')?'   ME: ':'  JZ: '):m.isCard?'  [CARD] '+m.rows.map(r=>r.k+'='+r.v).join(' | ')+' est='+m.est: m.isSys?'  [SYS] ':m.isDiv?'  [DIV] ':'  [PHOTO]')+(m.isCard?'':m.text)));
 return v;}
async function say(c,t){c.send(t); await sleep(1500);}
(async()=>{
 const c=load('jobzee-design/project/Mesaje.dc.html');
 let v=c.renderVals(); console.log('ACTIVE:',v.act.map(r=>r.title+' / '+r.sub+' / '+r.last).join(' || ')); console.log('HIST:',v.hist.map(r=>r.title+' / '+r.sub+' / '+r.chip).join(' || '));
 v.act[0].open();
 await say(c,'Am de montat un birou IKEA și un dulap mic');
 c.send('Azi'); c.send('Azi'); c.send('Azi'); await sleep(1500); // dublu tap
 await say(c,'Altă adresă'); await say(c,'Str. Aviatorilor 12, ap. 4');
 await say(c,'__photo');
 await say(c,'blabla'); await say(c,'altceva'); await say(c,'Modific ceva'); await say(c,'Când'); await say(c,'Programez'); await say(c,'Mâine seară');
 dump(c,'before send');
 await say(c,'Trimite cererea');
 v=dump(c,'after send'); console.log('closed?',v.closed,'sent?',v.sent);
 c.send('alt mesaj'); await sleep(1000); console.log('msgs after send into closed:',c.renderVals().msgs.length);
 v.newJz(); await sleep(50); v=dump(c,'new conv');
 await say(c,'curățenie la 2 camere');
 v.back(); v=c.renderVals(); console.log('ACTIVE:',v.act.map(r=>r.title+' / '+r.sub+' / '+r.last).join(' || '));
 v.goH(); v=c.renderVals(); console.log('HIST:',v.hist.map(r=>r.title+' / '+r.sub+' / '+r.chip+' / '+r.when).join(' || '));
 v.goA(); v=c.renderVals(); v.act.find(r=>r.title==='Mihai I.').open(); 
 await say(c,'Sunt acasă'); await say(c,'Mulțumesc!'); await say(c,'mulțumesc din nou'); await say(c,'încă unul'); await say(c,'și încă unul');
 v=dump(c,'mihai'); v.doClose(); v=dump(c,'mihai closed'); console.log('chatClosed',v.chatClosed);
 v.again(); v=dump(c,'again'); console.log('draft:',c.state.draft);
 v.back(); v=c.renderVals(); v.goH(); v=c.renderVals(); console.log('HIST:',v.hist.map(r=>r.title+' / '+r.sub+' / '+r.chip).join(' || '));
 v.q='x'; c.state.q='elena'; v=c.renderVals(); console.log('search elena:',v.hist.map(r=>r.title).join(','));
 process.exit(0);
})();
