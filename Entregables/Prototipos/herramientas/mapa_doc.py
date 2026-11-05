# Versión compacta del mapa para el documento: el menú lateral va como un recuadro con sus destinos.
import json,sys,subprocess,textwrap
m=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]
inv={s['id']:s['nombre'] for s in m['INVENTARIO']}
SHORT={"Aviso de respaldo → Ir a respaldos":"Aviso respaldo","Ver avance de digitalización":"Ver avance","Cargar documento":"Cargar","Últimos expedientes → Abrir":"Abrir reciente",
"Abrir expediente":"Abrir","Registrar abonado (sin resultados)":"Registrar","Cargar documento / Nueva versión":"Cargar / Nueva versión","Ver versiones":"Versiones",
"Modificar abonado / Cambiar titular":"Modificar","Ver qué falta":"Qué falta","Anular (confirmado)":"Anular","Dar de baja / Reactivar":"Baja / Reactivar","Confirmar":"Confirmar",
"Guardar / Cancelar":"Guardar / Cancelar","Cancelar con datos escritos":"Cancelar","Salir sin guardar":"Salir","Confirmar cambio":"Confirmar","Cargar documentos (tras registrar)":"Cargar docs.",
"Cargar lo que falta":"Cargar faltante","Asignar tipo (tipo pendiente)":"Asignar tipo","Restaurar…":"Restaurar","Restaurar (confirmado)":"Restaurar","Agregar o buscar persona":"Agregar persona","Agregar":"Agregar","Cancelar con archivos elegidos":"Cancelar",
"Ver abonados con tipo pendiente":"Tipo pendiente","Fusionar (confirmado)":"Unir","Fusionar":"Unir","Exportar / Volver":"Exportar / Volver","Volver al expediente":"Volver","Cargar nueva versión":"Nueva versión",
"Sesión cerrada":"Cierra sesión","Ingresar":"Ingresar"}
L=['digraph G {','graph [rankdir=LR, fontname="Arial", nodesep=0.15, ranksep=0.35, pad=0.15, newrank=true];',
   'node [fontname="Arial", fontsize=15, shape=box, style="rounded,filled", fillcolor="#F2F2F2", color="#444444", penwidth=1.3, margin="0.08,0.04"];',
   'edge [fontname="Arial", fontsize=13, color="#555555", fontcolor="#222222", arrowsize=0.7];']
def lab(i,n,w=16): return f'<<b>{i}</b><br/>{"<br/>".join(textwrap.wrap(n,w))}>'
for i,n in inv.items():
    extra=', fillcolor="#D9D9D9", penwidth=2.2' if i in ('PAN-03','PAN-04','PAN-05','PAN-06','PAN-07','PAN-08') else ''
    L.append(f'"{i}" [label={lab(i,n)}{extra}];')
for k,n in m['DIALOGOS'].items():
    L.append(f'"{k}" [label={lab(k,n,18)}, style="rounded,dashed,filled", fillcolor="white", fontsize=14];')
side=[e for e in m['NAV'] if e[0]=='*' and e[1].startswith('PAN')]
menu="<br/>".join(f'{e[2]} → {e[1]}' for e in side)
L.append(f'"MENU" [label=<<b>Menú lateral y barra superior</b><br/>(en todas las pantallas tras iniciar sesión)<br/><br/>{menu}<br/>15 min sin actividad → D-08>, shape=note, fillcolor="white", fontsize=14];')
L.append('"PAN-01" -> "MENU" [style=invis];')
pairs={}
order=[]
for a,b,t in m['NAV']:
    if a=='*' or a==b: continue
    t=SHORT.get(t,t)
    key=tuple(sorted((a,b)))
    if key not in pairs: pairs[key]={}; order.append(key)
    pairs[key][(a,b)]=t
bold={('PAN-01','PAN-02'),('PAN-03','PAN-04'),('PAN-04','PAN-05'),('PAN-07','PAN-05')}
for key in order:
    e=pairs[key]
    if len(e)==2:
        (a,b),t1=list(e.items())[0]; t2=e[(b,a)]
        st=', style=bold, penwidth=2' if (a,b) in bold or (b,a) in bold else ''
        L.append(f'"{a}" -> "{b}" [dir=both, label="{t1} ⇄ {t2}"{st}];')
    else:
        (a,b),t=list(e.items())[0]
        st=', style=bold, penwidth=2' if (a,b) in bold else ''
        L.append(f'"{a}" -> "{b}" [label="{t}"{st}];')
L.append('}')
open(out+'.dot','w',encoding='utf-8').write('\n'.join(L))
subprocess.run(['dot','-Tpng','-Gdpi=200',out+'.dot','-o',out+'.png'],check=True)
subprocess.run(['dot','-Tsvg',out+'.dot','-o',out+'.svg'],check=True)
