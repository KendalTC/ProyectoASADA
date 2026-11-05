# -*- coding: utf-8 -*-
import copy, sys, os
import docx
from docx.shared import Inches, Pt, RGBColor, Emu
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.text import WD_ALIGN_PARAGRAPH
from PIL import Image
from contenido import *

SRC, OUT, CAPS, MAPA = sys.argv[1:5]
d = docx.Document(SRC)
T = list(d.tables)              # referencias fijas antes de borrar nada
PARAS = list(d.paragraphs)

PEND_COLOR = "C55A11"

def mkrun(p, text, size=18, bold=False, color=None, italic=False):
    r = p.add_run(text)
    rp = r._r.get_or_add_rPr()
    f = OxmlElement('w:rFonts')
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        f.set(qn(a), 'Calibri')
    rp.insert(0, f)
    r.font.size = Pt(size / 2)
    if bold: r.bold = True
    if italic: r.italic = True
    if color: r.font.color.rgb = RGBColor.from_string(color)
    return r

def write_lines(p_first, container_add, text, size):
    lines = text.split("\n")
    ps = [p_first]
    for _ in lines[1:]:
        newp = copy.deepcopy(p_first._p)
        for r in newp.findall(qn('w:r')): newp.remove(r)
        ps[-1]._p.addnext(newp)
        ps.append(docx.text.paragraph.Paragraph(newp, p_first._parent))
    for p, line in zip(ps, lines):
        if line.startswith("PENDIENTE"):
            mkrun(p, line, size, bold=True, color=PEND_COLOR)
        else:
            mkrun(p, line, size)

def clear_par(p):
    for r in list(p._p):
        if r.tag in (qn('w:r'), qn('w:hyperlink')):
            p._p.remove(r)

def set_cell(cell, text, size=18, bold=False):
    ps = cell.paragraphs
    for extra in ps[1:]:
        extra._p.getparent().remove(extra._p)
    p = ps[0]; clear_par(p)
    if bold:
        mkrun(p, text, size, bold=True)
    else:
        write_lines(p, None, str(text), size)

def set_par(p, text, size=21):
    clear_par(p)
    write_lines(p, None, text, size)

def fill(t, rows, start=1, cols=None):
    """Ajusta la cantidad de filas de datos y las llena."""
    need = start + len(rows)
    while len(t.rows) < need:
        t._tbl.append(copy.deepcopy(t.rows[-1]._tr))
    while len(t.rows) > need:
        t._tbl.remove(t.rows[-1]._tr)
    for i, row in enumerate(rows):
        cells = t.rows[start + i].cells
        for j, val in enumerate(row):
            c = j if cols is None else cols[j]
            set_cell(cells[c], val)

def par_with(prefix):
    for p in d.paragraphs:
        if p.text.strip().startswith(prefix):
            return p
    raise KeyError(prefix)

def img_par_replacing(table, path, max_w=6.5, max_h=8.2):
    """Sustituye una tabla de marcador por un párrafo centrado con la imagen."""
    newp = OxmlElement('w:p')
    table._tbl.addprevious(newp)
    p = docx.text.paragraph.Paragraph(newp, table._parent)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    w, h = Image.open(path).size
    width = max_w; height = width * h / w
    if height > max_h:
        height = max_h; width = height * w / h
    p.add_run().add_picture(path, width=Inches(width))
    table._tbl.getparent().remove(table._tbl)
    return p

def placeholder_text(table, text):
    set_cell(table.rows[0].cells[0], text)

# ---------------- Portada ----------------
for p in PARAS[:8]:
    if p.text.strip() == "Acueducto de Pilas y Bodegas":
        p.runs[0].text = "Acueducto Bodegas y Pilas"
        for r in p.runs[1:]: r.text = ""
    if p.text.strip().startswith("SIGEDA · Sistema de Gestión Documental"):
        p.runs[0].text = "SIGEDA · Sistema de Gestión Documental del Acueducto"
        for r in p.runs[1:]: r.text = ""
fill(T[0], PORTADA)
fill(T[1], VERSIONES)

# ---------------- 0 ----------------
set_par(par_with("[COMPLETAR]"), PROPOSITO)   # 0.1 (primer [COMPLETAR] suelto)
fill(T[3], RELACION)
defs = [[r.cells[0].text, r.cells[1].text] for r in T[4].rows[1:-1]]
for r in defs:
    if r[0] == "Severidad":
        r[1] = r[1] + " (Nielsen, 1993)."
        r[1] = r[1].replace(". (Nielsen", " (Nielsen")
fill(T[4], defs + DEFS_EXTRA)

# ---------------- 1 y 2 ----------------
fill(T[5], OBJETIVOS)
fill(T[7], PERFILES)
fill(T[8], ENTORNO)
fill(T[9], TAREAS)

# ---------------- 3 ----------------
set_cell(T[11].rows[0].cells[4], "RF (verificados)", bold=True)
fill(T[11], INVENTARIO)
pc = par_with("[COMPLETAR: respuesta a la pregunta de control]")
set_par(pc, CONTROL[0])
last = pc
for txt in CONTROL[1:]:
    newp = copy.deepcopy(last._p); last._p.addnext(newp)
    np_ = docx.text.paragraph.Paragraph(newp, last._parent); set_par(np_, txt); last = np_

# ---------------- 4 ----------------
mp = img_par_replacing(T[12], MAPA, max_w=6.5, max_h=7.7)
for _p in d.paragraphs:
    if _p.style.name.startswith('Heading 1') and _p.text.startswith('4. Mapa'):
        _p.paragraph_format.page_break_before = True; _p.paragraph_format.keep_with_next = True
reglas = [p for p in d.paragraphs if p.text.startswith("[COMPLETAR: regla")]
for p, txt in zip(reglas, REGLAS[:3]):
    set_par(p, txt)
last = reglas[-1]
for txt in REGLAS[3:]:
    newp = copy.deepcopy(last._p); last._p.addnext(newp)
    np_ = docx.text.paragraph.Paragraph(newp, last._parent); set_par(np_, txt); last = np_
fill(T[13], RECORRIDOS)

# ---------------- 5 ----------------
fill(T[14], ESTILO)

# ---------------- 6 (bocetos: pendientes) ----------------
for ti in (16, 18, 20):
    placeholder_text(T[ti], PEND_BOCETO)
for ti in (17, 19, 21):
    fill(T[ti], BOCETO_QA)

# ---------------- 7 ----------------
fill(T[22], NAVEGABLE)
fichas = [("PAN-03", 24), ("PAN-04", 29), ("PAN-05", 34), ("PAN-06", 39), ("PAN-07", 44), ("PAN-08", 49)]
traz_pars = [p for p in d.paragraphs if p.text.startswith("RF: [COMPLETAR]")]
for k, (pan, ti) in enumerate(fichas):
    F = FICHAS[pan]
    img_par_replacing(T[ti], os.path.join(CAPS, F["img"]), max_h=7.6)
    fill(T[ti + 1], F["elem"])
    fill(T[ti + 2], F["acc"])
    fill(T[ti + 3], [[ESTADOS_LABEL[i], F["est"][i]] for i in range(4)])
    qs = [r.cells[0].text for r in T[ti + 4].rows[1:]]
    fill(T[ti + 4], [[qs[i], F["preg"][i]] for i in range(5)])
    rf, rn, rnf, cu = F["traz"]
    set_par(traz_pars[k], f"RF: {rf}   ·   RN: {rn}   ·   RNF: {rnf}   ·   Paso del CU: {cu}")
fill(T[54], RESTO)
set_par(par_with("[COMPLETAR]"), ALTA)      # 7.8 (siguiente [COMPLETAR] suelto)

# ---------------- 8 ----------------
fill(T[55], VERTICAL)
img_par_replacing(T[56], "/home/claude/doc/vertical_fig.png", max_w=6.5)
fill(T[57], PRUEBAS)
set_par(par_with("[COMPLETAR]"), APRENDIZAJES)

# ---------------- 9 ----------------
fill(T[58], PLAN_SESION)
fill(T[59], RESULTADOS)
fill(T[60], HALLAZGOS)
fill(T[62], HEUR, cols=[0, 1, 2])

# ---------------- 10 a 13 ----------------
fill(T[63], DATOS_PERS)
fill(T[64], RF_TRAZ)
fill(T[65], RNF_TRAZ)
fill(T[66], [[str(i + 1)] + r for i, r in enumerate(PENDIENTES)])
crit = [r.cells[1].text for r in T[67].rows[1:]]
fill(T[67], [[str(i + 1), crit[i], CHECK[i][0], CHECK[i][1]] for i in range(18)])

# ---------------- 14 Referencias ----------------
import re as _re
for p in list(d.paragraphs):
    if p.text.startswith("Pressman"):
        p._p.getparent().remove(p._p)
ref_last = par_with("[COMPLETAR: otras referencias]")
ref_last._p.getparent().remove(ref_last._p)
model = par_with("Kendall, K. E.")
def ref_par(text, before):
    newp = copy.deepcopy(model._p); before._p.addprevious(newp)
    p = docx.text.paragraph.Paragraph(newp, model._parent); clear_par(p)
    m = _re.match(r"^(.*?\((?:2026[a-e]?|s\.f\.)\)\. )(.*?)( \(versión.*| \[.*)$", text)
    mkrun(p, m.group(1), 21); mkrun(p, m.group(2), 21, italic=True); mkrun(p, m.group(3), 21)
for txt in REFS_EXTRA[:6]:
    ref_par(txt, model)
for txt in REFS_EXTRA[6:]:
    ref_par(txt, par_with("Nielsen, J. (1993)"))

# ---------------- Anexos ----------------
fill(T[68], ANEXO_A)
fill(T[69], ANEXO_B)
gl = [p for p in d.paragraphs if p.style.name == "List Paragraph" and p.text.startswith("Al final:")][0]
newp = copy.deepcopy(gl._p); gl._p.addnext(newp)
set_par(docx.text.paragraph.Paragraph(newp, gl._parent), GUION_EXTRA)
first_guion = [p for p in d.paragraphs if p.style.name == "List Paragraph" and p.text.startswith("Agradecer y explicar")][0]
pre = copy.deepcopy(first_guion._p)
pPr = pre.find(qn('w:pPr'))
if pPr is not None:
    num = pPr.find(qn('w:numPr'))
    if num is not None: pPr.remove(num)
first_guion._p.addprevious(pre)
set_par(docx.text.paragraph.Paragraph(pre, first_guion._parent), GUION_TAREAS)

# ---------------- Limpieza: instrucciones grises y ejemplos ámbar ----------------
for p in list(d.paragraphs):
    r = p.runs[0] if p.runs else None
    if r is None: continue
    rp = r._r.rPr
    col = rp.find(qn('w:color')) if rp is not None else None
    colv = col.get(qn('w:val')) if col is not None else None
    if r.italic and colv == "595959" and not p.text.strip().startswith("Figura"):
        p._p.getparent().remove(p._p)
for t in list(d.tables):
    if t.rows[0].cells[0].text.strip().startswith("EJEMPLO RESUELTO"):
        t._tbl.getparent().remove(t._tbl)

# Cursivas grises que quedaron dentro de celdas de la plantilla (pistas)
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    rp = r._r.rPr
                    col = rp.find(qn('w:color')) if rp is not None else None
                    if r.italic and col is not None and col.get(qn('w:val')) == "595959":
                        r.italic = False; col.set(qn('w:val'), "000000")


# ---------------- Sin bocetos (indicación del docente, v0.3) ----------------
import re as _re2
body = d.element.body
h6 = [p for p in d.paragraphs if p.style.name.startswith('Heading 1') and p.text.startswith('6. Prototipos de baja fidelidad')][0]
el = h6._p
while True:
    nxt = el.getnext()
    body.remove(el)
    if nxt is None: break
    if nxt.tag == qn('w:p'):
        tp = docx.text.paragraph.Paragraph(nxt, h6._parent)
        if tp.style.name.startswith('Heading 1') and tp.text.startswith('7. Prototipo navegable'):
            break
    el = nxt
def _set_text(p, txt):
    runs = p.runs
    runs[0].text = txt
    for r in runs[1:]: r.text = ''
for p in d.paragraphs:
    if p.style.name.startswith('Heading'):
        m = _re2.match(r'^(\d+)((?:\.\d+)?)(\.?\s.*)$', p.text)
        if m and 7 <= int(m.group(1)) <= 14:
            _set_text(p, f"{int(m.group(1))-1}{m.group(2)}{m.group(3)}")
    m = _re2.match(r'^Figura (\d+)\.(.*)$', p.text)
    if m and int(m.group(1)) >= 5:
        _set_text(p, f"Figura {int(m.group(1))-3}.{m.group(2)}")
    if '(sección 9.3)' in p.text:
        for r in p.runs: r.text = r.text.replace('(sección 9.3)', '(sección 8.3)')
    if p.text.startswith('Snyder, C. (2003)'):
        p._p.getparent().remove(p._p)
alc = [t for t in d.tables if t.rows[0].cells[0].text.strip() == 'Nivel'][0]
for row in list(alc.rows):
    if row.cells[0].text.strip() == 'Bocetos en papel':
        alc._tbl.remove(row._tr)
for row in alc.rows[1:]:
    c = row.cells[4]; v = c.text.strip()
    nv = {'4 y 7': '4 y 6', '8': '7', '7.8': '6.8'}.get(v)
    if nv: _set_text(c.paragraphs[0], nv)

# Actualizar campos (tabla de contenido) al abrir en Word
st = d.settings.element
uf = st.find(qn('w:updateFields'))
if uf is None:
    uf = OxmlElement('w:updateFields')
    after = None
    for tag in ('w:hdrShapeDefaults','w:footnotePr','w:endnotePr','w:compat','w:docVars','w:rsids','m:mathPr','w:attachedSchema','w:themeFontLang','w:clrSchemeMapping','w:doNotIncludeSubdocsInStats','w:doNotAutoCompressPictures','w:forceUpgrade','w:captions','w:readModeInkLockDown','w:smartTagType','w:shapeDefaults','w:doNotEmbedSmartTags','w:decimalSymbol','w:listSeparator'):
        el = st.find(qn(tag))
        if el is not None: after = el; break
    if after is not None: after.addprevious(uf)
    else: st.append(uf)
uf.set(qn('w:val'), 'true')

d.save(OUT)
# Revisión de marcadores que quedaron
left = [p.text for p in d.paragraphs if "[COMPLETAR" in p.text]
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            if "[COMPLETAR" in c.text: left.append(c.text[:60])
print("COMPLETAR restantes:", len(left), left[:10])
