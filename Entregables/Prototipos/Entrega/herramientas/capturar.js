// Genera las capturas PNG de todas las pantallas, estados y diálogos, y verifica los enlaces contra NAV.
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
const OUT=process.argv[2]||'capturas'; fs.mkdirSync(OUT,{recursive:true});
const URL0='file://'+path.resolve('prototipo/index.html');
const slug=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
(async()=>{
 const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1366,height:768},deviceScaleFactor:2});
 await pg.goto(URL0+'?captura=1');
 const meta=await pg.evaluate(()=>({INVENTARIO,STATES,NAV,DIALOGOS,DLG_HOST}));
 fs.writeFileSync(path.join(OUT,'..','pantallas.json'),JSON.stringify(meta,null,1));
 const list=[]; const found={};
 for(const s of meta.INVENTARIO){
   for(const st of meta.STATES[s.id]){
     const f=`${s.id}_${slug(s.nombre)}_${st}.png`;
     await pg.goto(`${URL0}?captura=1#/${s.id}?estado=${st}`); await pg.waitForTimeout(120);
     await pg.screenshot({path:path.join(OUT,f),fullPage:true}); list.push(f);
     const gos=await pg.$$eval('[data-go]',a=>a.map(x=>x.dataset.go.split('?')[0]));
     const dl=await pg.$$eval('[data-dlg]',a=>a.map(x=>x.dataset.dlg).filter(Boolean));
     found[s.id]=new Set([...(found[s.id]||[]),...gos,...dl]);
   }
 }
 for(const k in meta.DLG_HOST){
   const h=meta.DLG_HOST[k]; const f=`${k}_${slug(meta.DIALOGOS[k])}.png`;
   await pg.goto(`${URL0}?captura=1#/${h}${h.includes('?')?'&':'?'}dlg=${k}`); await pg.waitForTimeout(120);
   await pg.screenshot({path:path.join(OUT,f)}); list.push(f);
   const gos=await pg.$$eval('.dlg [data-go]',a=>a.map(x=>x.dataset.go.split('?')[0]));
   found[k]=new Set(gos);
 }
 for(const id of ['PAN-03','PAN-04','PAN-05','PAN-07']){
   const f=`ALTA_${id}.png`; await pg.goto(`${URL0}?captura=1&hifi=1#/${id}`); await pg.waitForTimeout(120);
   await pg.screenshot({path:path.join(OUT,f),fullPage:true}); list.push(f);
 }
 // Verificación: cada arista de NAV existe en la pantalla, y cada enlace real está en NAV
 const side=new Set(meta.NAV.filter(e=>e[0]==='*').map(e=>e[1]));
 const navSet=new Set(meta.NAV.map(e=>e[0]+'>'+e[1]));
 const faltan=[],sobran=[];
 for(const e of meta.NAV){ if(e[0]==='*'||e[1].startsWith('D-0')&&e[0]==='*') continue; if(!(found[e[0]]&&found[e[0]].has(e[1]))) faltan.push(e.join(' → ')); }
 for(const k in found){ for(const t of found[k]){ if(t===k) continue; if(side.has(t)&&k.startsWith('PAN')) continue; if(!navSet.has(k+'>'+t)) sobran.push(k+' → '+t);} }
 console.log('capturas:',list.length); console.log('NAV sin enlace en pantalla:',faltan); console.log('Enlaces fuera de NAV:',[...new Set(sobran)]);
 await b.close();
})();
