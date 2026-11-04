import json,sys,subprocess,textwrap
m=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]
inv={s['id']:s['nombre'] for s in m['INVENTARIO']}
L=['digraph G {','graph [rankdir=LR, fontname="Arial", nodesep=0.35, ranksep=0.9, bgcolor="white", pad=0.3];',
   'node [fontname="Arial", fontsize=14, shape=box, style="rounded,filled", fillcolor="#F2F2F2", color="#555555", penwidth=1.2];',
   'edge [fontname="Arial", fontsize=12, color="#555555", fontcolor="#333333", arrowsize=0.7];']
def lab(i,n): return f'<<b>{i}</b><br/>{"<br/>".join(textwrap.wrap(n,22))}>'
for i,n in inv.items():
    extra=', fillcolor="#D9D9D9", penwidth=2' if i in ('PAN-03','PAN-04','PAN-05','PAN-06','PAN-07','PAN-08') else ''
    L.append(f'"{i}" [label={lab(i,n)}{extra}];')
for k,n in m['DIALOGOS'].items():
    L.append(f'"{k}" [label={lab(k,n)}, shape=box, style="rounded,dashed,filled", fillcolor="white", fontsize=13];')
L.append('"MENU" [label=<<b>Menú lateral</b><br/>(en todas las pantallas<br/>después de iniciar sesión)>, shape=folder, fillcolor="#FFFFFF"];')
L.append('"PAN-01" -> "MENU" [style=invis];')
side=[e for e in m['NAV'] if e[0]=='*']
for e in side:
    if e[1].startswith('D-'):
        L.append(f'"MENU" -> "{e[1]}" [label="{e[2]}", style=dotted];')
    else:
        L.append(f'"MENU" -> "{e[1]}" [label="{e[2]}", style=dashed, color="#999999", fontcolor="#777777"];')
seen=set()
for a,b,t in m['NAV']:
    if a=='*' or a==b: continue
    if (a,b) in seen: continue
    seen.add((a,b))
    st=', style=bold' if (a,b) in {('PAN-01','PAN-02'),('PAN-03','PAN-04'),('PAN-04','PAN-05'),('PAN-05','PAN-04'),('PAN-07','PAN-05')} else ''
    L.append(f'"{a}" -> "{b}" [label="{t}"{st}];')
L.append('}')
open(out+'.dot','w',encoding='utf-8').write('\n'.join(L))
for fmt in ('png','svg'):
    args=['dot','-T'+fmt,out+'.dot','-o',out+'.'+fmt]+(['-Gdpi=170'] if fmt=='png' else [])
    subprocess.run(args,check=True)
print('ok')
