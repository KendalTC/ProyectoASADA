const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const AXE=fs.readFileSync(require.resolve('axe-core/axe.min.js'),'utf8');
const URL0='file://'+path.resolve('prototipo/index.html');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1366,height:768}});
await pg.goto(URL0);const meta=await pg.evaluate(()=>({STATES,DLG_HOST}));
const urls=[];for(const id in meta.STATES)for(const st of meta.STATES[id])urls.push(`#/${id}?estado=${st}`);
for(const k in meta.DLG_HOST){const h=meta.DLG_HOST[k];urls.push(`#/${h}${h.includes('?')?'&':'?'}dlg=${k}`);}
const agg={};
for(const hifi of ['','?hifi=1'])for(const u of urls){await pg.goto(URL0+hifi+u);await pg.waitForTimeout(80);await pg.addScriptTag({content:AXE});
const r=await pg.evaluate(async()=>(await axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21aa','wcag22aa','best-practice']})).violations.map(v=>({id:v.id,impact:v.impact,n:v.nodes.length,ex:v.nodes[0].target.join(' ')+' | '+(v.nodes[0].failureSummary||'').slice(0,160)})));
for(const v of r){const k=v.id;agg[k]=agg[k]||{impact:v.impact,count:0,pages:[],ex:v.ex};agg[k].count+=v.n;if(agg[k].pages.length<4)agg[k].pages.push((hifi?'H':'')+u);}}
console.log(JSON.stringify(agg,null,1));await b.close();})();
