#!/usr/bin/env python3
"""Genera las figuras del Modelo ER y Relacional del SIGEDA.

Salida (carpeta fuentes/ y png/):
  Figura1_ER_General.dot, Figura1A/B/C_*.dot   (modelo entidad-relacion, conceptual)
  Figura2A/B/C_*.dot                            (modelo relacional, logico)
  Leyenda_*.dot                                 (simbolos de la notacion, seccion 2.1)
Herramienta: Graphviz (lenguaje DOT). Uso: python3 generar_figuras.py
"""
import os, subprocess, html, sys

OUT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(OUT, "fuentes")
PNG = os.path.join(OUT, "png")
os.makedirs(SRC, exist_ok=True)
os.makedirs(PNG, exist_ok=True)

FONT = "Carlito"
NAVY = "#0B2140"
BLUE = "#1F4E79"
LINE = "#34495E"
GREY = "#E9ECF1"
BODY = "#F7F9FC"

# cardinalidad -> forma de flecha de Graphviz (la primera forma toca la entidad)
CARD = {"1": "teetee", "0..1": "teeodot", "0..*": "crowodot", "1..*": "crowtee"}

def esc(s):
    return html.escape(s, quote=False)

# ----------------------------------------------------------------- MODELO ER
# atributos: (nombre, banderas) banderas: id, parcial, opc, der, nota
ER = {
 "Sector": ("fuerte", [("nombre", "id")]),
 "Abonado": ("fuerte", [("numero_paja", "id"), ("tipo_abonado", ""), ("estado", ""),
                        ("fecha_baja", "opc"), ("titular_vigente", "der"),
                        ("estado_completitud", "der")]),
 "Persona": ("fuerte", [("id_persona", "id"), ("nombre", ""),
                        ("identificacion", "opc compuesto")]),
 "TipoDocumento": ("fuerte", [("nombre", "id"), ("prioridad", ""), ("obligatoriedad", "opc"),
                              ("es_exigido_a_cotitulares", "")]),
 "GrupoAlternativas": ("fuerte", [("nombre", "id"), ("obligatoriedad", "")]),
 "Documento": ("fuerte", [("id_documento", "id"), ("nombre_identificador", "opc"),
                          ("estado", ""), ("motivo_anulacion", "opc"),
                          ("fecha_anulacion", "opc"), ("version_vigente", "der")]),
 "VersionDocumento": ("debil", [("numero_version", "parcial"), ("nombre_original", ""),
                                ("ruta_archivo", ""), ("formato", ""), ("tamano_bytes", ""),
                                ("fecha_documento", ""), ("fecha_carga", ""),
                                ("hash_sha256", "")]),
 "Cuenta": ("fuerte", [("usuario", "id"), ("hash_contrasena", ""), ("perfil", ""),
                       ("intentos_fallidos", ""), ("bloqueada_hasta", "opc"),
                       ("es_contrasena_temporal", "")]),
 "RegistroBitacora": ("fuerte", [("id_registro_bitacora", "id"), ("fecha_hora", ""),
                                 ("accion", ""), ("elemento_afectado", ""), ("origen", "")]),
 "RegistroModificacion": ("sub", [("campo_modificado", ""), ("valor_anterior", "opc"),
                                  ("valor_nuevo", "opc")]),
 "RegistroRestauracion": ("sub", [("nombre_paquete", ""), ("fecha_respaldo_restaurado", "")]),
 "Respaldo": ("fuerte", [("id_respaldo", "id"), ("fecha_hora", ""), ("tipo", ""), ("estado", ""),
                         ("nombre_paquete", "opc"), ("hash_sha256", "opc"),
                         ("tamano_bytes", "opc")]),
 "CopiaRespaldo": ("debil", [("destino", "parcial"), ("estado", ""),
                             ("fecha_hora_verificacion", "opc")]),
}

# (A, B, simbolo en el extremo A, simbolo en el extremo B, nombre, identificadora)
# El simbolo en el extremo X dice cuantas X hay por cada ocurrencia del otro extremo.
ER_REL = [
 ("Sector", "Abonado", "0..1", "0..*", "ubica_en", False),
 ("Abonado", "Documento", "1", "0..*", "tiene_documentos", False),
 ("Persona", "Documento", "0..1", "0..*", "aporta", False),
 ("TipoDocumento", "Documento", "1", "0..*", "clasifica", False),
 ("GrupoAlternativas", "TipoDocumento", "0..1", "1..*", "agrupa", False),
 ("Documento", "VersionDocumento", "1", "1..*", "contiene", True),
 ("Cuenta", "RegistroBitacora", "0..1", "0..*", "realiza", False),
 ("Abonado", "RegistroBitacora", "0..1", "0..*", "afecta_a", False),
 ("Cuenta", "Respaldo", "0..1", "0..*", "inicia", False),
 ("Respaldo", "CopiaRespaldo", "1", "0..*", "tiene_copias", True),
]
# relacion muchos a muchos con atributos propios (rombo)
VINCULO = ("Abonado", "Persona", "se_vincula_con",
           [("rol", ""), ("fecha_inicio", ""), ("fecha_fin", "opc"), ("es_vigente", "der")])
GENERALIZACIONES = [("RegistroModificacion", "RegistroBitacora"),
                    ("RegistroRestauracion", "RegistroBitacora")]

def attr_html(name, flags, weak=False):
    t = esc(name)
    f = flags.split()
    if "compuesto" in f:
        t += ' <FONT POINT-SIZE="8">[tipo + número]</FONT>'
    if "id" in f or "parcial" in f:
        t = "<U>%s</U>" % t
        if "parcial" in f:
            t += ' <FONT POINT-SIZE="8">(clave parcial)</FONT>'
    if "der" in f:
        t = "<I>/%s</I>" % t
    if "opc" in f:
        t += ' <FONT POINT-SIZE="8">(0..1)</FONT>'
    return '<TR><TD ALIGN="LEFT" CELLPADDING="2">%s</TD></TR>' % t

def er_node(name, only_name=False, ref=False):
    kind, attrs = ER[name]
    if ref:
        return ('%s [shape=plain, label=<<TABLE BORDER="1" STYLE="DASHED" CELLBORDER="0" CELLSPACING="0" '
                'CELLPADDING="5" BGCOLOR="%s" COLOR="#7F8C9A"><TR><TD><B>%s</B></TD></TR></TABLE>>];'
                % (name, GREY, name))
    head = ('<TR><TD BGCOLOR="%s" CELLPADDING="4"><FONT COLOR="white"><B>%s</B></FONT></TD></TR>'
            % (NAVY, name))
    rows = "" if only_name else "".join(attr_html(a, f) for a, f in attrs)
    inner = ('<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" COLOR="%s" BGCOLOR="%s">%s%s</TABLE>'
             % (NAVY, BODY, head, rows))
    if kind == "debil":
        label = ('<TABLE BORDER="2" CELLBORDER="0" CELLSPACING="0" CELLPADDING="3" COLOR="%s">'
                 '<TR><TD>%s</TD></TR></TABLE>' % (NAVY, inner))
    else:
        label = inner
    return "%s [shape=plain, label=<%s>];" % (name, label)

def er_edge(a, b, ca, cb, nombre, ident):
    return ('%s -> %s [dir=both, arrowtail="%s", arrowhead="%s", label=<<I>%s</I>>, '
            'penwidth=%s, fontsize=10, color="%s"];'
            % (a, b, CARD[ca], CARD[cb], esc(nombre), "2.2" if ident else "1.2", LINE))

def vinculo_nodes(prefix=""):
    a, b, nombre, attrs = VINCULO
    rows = "".join(attr_html(n, f) for n, f in attrs)
    box = ('vinculo_attrs [shape=plain, label=<<TABLE BORDER="1" STYLE="ROUNDED" CELLBORDER="0" '
           'CELLSPACING="0" CELLPADDING="1" COLOR="#7F8C9A" BGCOLOR="white">%s</TABLE>>];' % rows)
    dia = ('vinculo [shape=diamond, style=filled, fillcolor="#DCE3ED", color="%s", fontsize=10, '
           'label=<<I>%s</I>>, width=1.5, height=0.9];' % (NAVY, nombre))
    e1 = ('%s -> vinculo [dir=both, arrowtail="%s", arrowhead="none", color="%s", penwidth=1.2];'
          % (a, CARD["1..*"], LINE))
    e2 = ('vinculo -> %s [dir=both, arrowtail="none", arrowhead="%s", color="%s", penwidth=1.2];'
          % (b, CARD["1..*"], LINE))
    e3 = 'vinculo -> vinculo_attrs [arrowhead=none, style=dashed, color="#7F8C9A"];'
    return [dia, box, e1, e2, e3]

def dot_head(rankdir="LR", nodesep=0.5, ranksep=0.7):
    return ('digraph G {\n  graph [rankdir=%s, nodesep=%s, ranksep=%s, fontname="%s", splines=true, '
            'pad=0.15, dpi=220];\n  node [fontname="%s", fontsize=11];\n  edge [fontname="%s", fontsize=10];\n'
            % (rankdir, nodesep, ranksep, FONT, FONT, FONT))

def write(nombre, texto):
    p = os.path.join(SRC, nombre + ".dot")
    with open(p, "w", encoding="utf-8") as f:
        f.write(texto)
    subprocess.run(["dot", "-Tpng", p, "-o", os.path.join(PNG, nombre + ".png")], check=True)
    subprocess.run(["dot", "-Tsvg", p, "-o", os.path.join(PNG, nombre + ".svg")], check=True)
    print("ok", nombre)

def fig1_general():
    L = [dot_head("LR", 0.35, 0.6)]
    for n in ER:
        L.append("  " + er_node(n, only_name=True))
    for r in ER_REL:
        L.append("  " + er_edge(*r))
    d = VINCULO
    L.append('  vinculo [shape=diamond, style=filled, fillcolor="#DCE3ED", color="%s", fontsize=10, label=<<I>%s</I>>];' % (NAVY, d[2]))
    L.append('  Abonado -> vinculo [dir=both, arrowtail="%s", arrowhead=none, color="%s", penwidth=1.2];' % (CARD["1..*"], LINE))
    L.append('  vinculo -> Persona [dir=both, arrowtail=none, arrowhead="%s", color="%s", penwidth=1.2];' % (CARD["1..*"], LINE))
    for sub, sup in GENERALIZACIONES:
        L.append('  %s -> %s [arrowhead=onormal, arrowsize=1.4, color="%s", penwidth=1.4, label=<<I>es_un</I>>, fontsize=10];' % (sub, sup, LINE))
    L.append("}\n")
    write("Figura1_ER_General", "\n".join(L))

def fig1_a():
    L = [dot_head("LR", 0.5, 0.9)]
    for n in ("Sector", "Abonado", "Persona"):
        L.append("  " + er_node(n))
    L.append("  " + er_edge(*ER_REL[0]))
    L += ["  " + x for x in vinculo_nodes()]
    L.append("  { rank=same; vinculo; vinculo_attrs }")
    L.append("}\n")
    write("Figura1A_ER_Abonados_y_personas", "\n".join(L))

def fig1_b():
    L = [dot_head("TB", 0.5, 0.7)]
    for n in ("GrupoAlternativas", "TipoDocumento", "Documento", "VersionDocumento"):
        L.append("  " + er_node(n))
    L.append("  " + er_node("Abonado", ref=True))
    L.append("  " + er_node("Persona", ref=True))
    for r in ER_REL:
        if r[0] in ("GrupoAlternativas", "TipoDocumento", "Documento") or r[1] in ("Documento", "VersionDocumento"):
            L.append("  " + er_edge(*r))
    L.append("  { rank=same; Abonado; TipoDocumento; Persona }")
    L.append("}\n")
    write("Figura1B_ER_Documentos", "\n".join(L))

def fig1_c():
    L = [dot_head("TB", 0.45, 0.75)]
    for n in ("Cuenta", "RegistroBitacora", "RegistroModificacion", "RegistroRestauracion",
              "Respaldo", "CopiaRespaldo"):
        L.append("  " + er_node(n))
    L.append("  " + er_node("Abonado", ref=True))
    for r in ER_REL:
        if r[1] in ("RegistroBitacora", "Respaldo", "CopiaRespaldo") and r[0] in ("Cuenta", "Abonado", "Respaldo"):
            L.append("  " + er_edge(*r))
    for sub, sup in GENERALIZACIONES:
        lab = ', label=<<I>es_un</I>>'
        L.append('  %s -> %s [arrowhead=onormal, arrowsize=1.5, color="%s", penwidth=1.4%s, fontsize=10];' % (sub, sup, LINE, lab))
    L.append('  nota_gen [shape=plain, label=<<I>especialización parcial y disjunta</I>>, fontsize=9];')
    L.append("  { rank=same; Cuenta; Abonado }")
    L.append("  { rank=same; RegistroModificacion; RegistroRestauracion; Respaldo }")
    L.append("}\n")
    write("Figura1C_ER_Seguridad_bitacora_y_respaldos", "\n".join(L))

# -------------------------------------------------------------- MODELO RELACIONAL
# columnas: (nombre, etiqueta) etiqueta: "PK", "PK FK:tabla", "FK:tabla", "FK:tabla opc", "UQ", "opc", ""
REL = {
 "sector": [("id_sector", "PK"), ("nombre", "UQ")],
 "abonado": [("id_abonado", "PK"), ("numero_paja", "UQ"), ("id_sector", "FK:sector opc"),
             ("tipo_abonado", "CHECK"), ("estado", "CHECK"), ("fecha_baja", "opc")],
 "persona": [("id_persona", "PK"), ("nombre", ""), ("tipo_identificacion", "CHECK opc"),
             ("identificacion", "opc")],
 "vinculo_abonado": [("id_abonado", "PK FK:abonado"), ("id_persona", "PK FK:persona"),
                     ("fecha_inicio", "PK"), ("rol", "CHECK"), ("fecha_fin", "opc")],
 "grupo_alternativas": [("id_grupo_alternativas", "PK"), ("nombre", "UQ"), ("obligatoriedad", "CHECK")],
 "tipo_documento": [("id_tipo_documento", "PK"), ("id_grupo_alternativas", "FK:grupo_alternativas opc"),
                    ("nombre", "UQ"), ("prioridad", ""), ("obligatoriedad", "CHECK opc"),
                    ("es_exigido_a_cotitulares", "")],
 "documento": [("id_documento", "PK"), ("id_abonado", "FK:abonado"), ("id_tipo_documento", "FK:tipo_documento"),
               ("id_persona", "FK:persona opc"), ("nombre_identificador", "opc"), ("estado", "CHECK"),
               ("motivo_anulacion", "opc"), ("fecha_anulacion", "opc")],
 "version_documento": [("id_documento", "PK FK:documento"), ("numero_version", "PK"),
                       ("nombre_original", ""), ("ruta_archivo", "UQ"), ("formato", "CHECK"),
                       ("tamano_bytes", ""), ("fecha_documento", ""), ("fecha_carga", ""),
                       ("hash_sha256", "")],
 "cuenta": [("id_cuenta", "PK"), ("usuario", "UQ"), ("hash_contrasena", ""), ("perfil", "CHECK"),
            ("intentos_fallidos", ""), ("bloqueada_hasta", "opc"), ("es_contrasena_temporal", "")],
 "registro_bitacora": [("id_registro_bitacora", "PK"), ("id_cuenta", "FK:cuenta opc"),
                       ("id_abonado", "REF:abonado opc"), ("fecha_hora", ""), ("accion", "CHECK"),
                       ("elemento_afectado", ""), ("origen", "CHECK")],
 "registro_modificacion": [("id_registro_bitacora", "PK FK:registro_bitacora"),
                           ("campo_modificado", ""), ("valor_anterior", "opc"), ("valor_nuevo", "opc")],
 "registro_restauracion": [("id_registro_bitacora", "PK FK:registro_bitacora"),
                           ("nombre_paquete", ""), ("fecha_respaldo_restaurado", "")],
 "respaldo": [("id_respaldo", "PK"), ("id_cuenta", "FK:cuenta opc"), ("fecha_hora", ""),
              ("tipo", "CHECK"), ("estado", "CHECK"), ("nombre_paquete", "UQ opc"),
              ("hash_sha256", "opc"), ("tamano_bytes", "opc")],
 "copia_respaldo": [("id_respaldo", "PK FK:respaldo"), ("destino", "PK CHECK"), ("estado", "CHECK"),
                    ("fecha_hora_verificacion", "opc")],
}
# (hija, padre, simbolo en padre, simbolo en hija)
REL_FK = [
 ("abonado", "sector", "0..1", "0..*"),
 ("vinculo_abonado", "abonado", "1", "1..*"),
 ("vinculo_abonado", "persona", "1", "1..*"),
 ("documento", "abonado", "1", "0..*"),
 ("documento", "persona", "0..1", "0..*"),
 ("documento", "tipo_documento", "1", "0..*"),
 ("tipo_documento", "grupo_alternativas", "0..1", "1..*"),
 ("version_documento", "documento", "1", "1..*"),
 ("registro_bitacora", "cuenta", "0..1", "0..*"),
 ("registro_modificacion", "registro_bitacora", "1", "0..1"),
 ("registro_restauracion", "registro_bitacora", "1", "0..1"),
 ("respaldo", "cuenta", "0..1", "0..*"),
 ("copia_respaldo", "respaldo", "1", "0..*"),
]

def rel_node(name, ref=False):
    if ref:
        return ('%s [shape=plain, label=<<TABLE BORDER="1" STYLE="DASHED" CELLBORDER="0" CELLSPACING="0" '
                'CELLPADDING="5" BGCOLOR="%s" COLOR="#7F8C9A"><TR><TD><B>%s</B></TD></TR></TABLE>>];'
                % (name, GREY, name))
    rows = ""
    for col, tag in REL[name]:
        tags = tag.split()
        pk = "PK" in tags
        txt = "<B>%s</B>" % col if pk else col
        t = []
        for x in tags:
            if x == "PK": t.append("PK")
            elif x.startswith("FK:"): t.append("FK→" + x[3:])
            elif x.startswith("REF:"): t.append("ref. lógica→" + x[4:])
            elif x == "UQ": t.append("UQ")
            elif x == "CHECK": t.append("CHECK")
            elif x == "opc": t.append("opc.")
        right = " · ".join(t) or "&#160;" 
        rows += ('<TR><TD ALIGN="LEFT" CELLPADDING="2">%s</TD><TD ALIGN="LEFT" CELLPADDING="2">'
                 '<FONT POINT-SIZE="8" COLOR="#5D6D7E">%s</FONT></TD></TR>' % (txt, right if right == "&#160;" else esc(right)))
    head = ('<TR><TD COLSPAN="2" BGCOLOR="%s" CELLPADDING="4"><FONT COLOR="white"><B>%s</B></FONT></TD></TR>'
            % (NAVY, name))
    return ('%s [shape=plain, label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" '
            'COLOR="%s" BGCOLOR="%s">%s%s</TABLE>>];' % (name, NAVY, BODY, head, rows))

def rel_edge(hija, padre, cp, ch):
    # flecha: padre -> hija ; extremo padre = arrowtail, extremo hija = arrowhead
    return ('%s -> %s [dir=both, arrowtail="%s", arrowhead="%s", color="%s", penwidth=1.2];'
            % (padre, hija, CARD[cp], CARD[ch], LINE))

def fig2(nombre, tablas, refs, rank_groups, rankdir="TB", sep=(0.5, 0.7), extra=()):
    L = [dot_head(rankdir, *sep)]
    for t in tablas:
        L.append("  " + rel_node(t))
    for r in refs:
        L.append("  " + rel_node(r, ref=True))
    todas = set(tablas) | set(refs)
    for h, p, cp, ch in REL_FK:
        if h in tablas and p in todas:
            L.append("  " + rel_edge(h, p, cp, ch))
    for g in rank_groups:
        L.append("  { rank=same; %s }" % "; ".join(g))
    for e in extra:
        L.append("  " + e)
    L.append("}\n")
    write(nombre, "\n".join(L))

def leyendas():
    # simbolos sueltos para la seccion 2.1
    ent = ('digraph G { graph[dpi=220, pad=0.05]; node[fontname="%s", fontsize=11];\n %s\n}\n'
           % (FONT, er_node("Entidad").replace("Entidad [", "e [").replace('<B>Entidad</B>', '<B>Entidad</B>')
              if False else
              'e [shape=plain, label=<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" COLOR="%s" BGCOLOR="%s">'
              '<TR><TD BGCOLOR="%s" CELLPADDING="4"><FONT COLOR="white"><B>Entidad</B></FONT></TD></TR>'
              '<TR><TD ALIGN="LEFT">atributo</TD></TR></TABLE>>];' % (NAVY, BODY, NAVY)))
    write("Leyenda_entidad", ent)
    deb = ('digraph G { graph[dpi=220, pad=0.05]; node[fontname="%s", fontsize=11];\n'
           'e [shape=plain, label=<<TABLE BORDER="2" CELLBORDER="0" CELLSPACING="0" CELLPADDING="3" COLOR="%s"><TR><TD>'
           '<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1" COLOR="%s" BGCOLOR="%s">'
           '<TR><TD BGCOLOR="%s" CELLPADDING="4"><FONT COLOR="white"><B>Entidad débil</B></FONT></TD></TR>'
           '<TR><TD ALIGN="LEFT"><U>clave parcial</U></TD></TR></TABLE></TD></TR></TABLE>>];\n}\n'
           % (FONT, NAVY, NAVY, BODY, NAVY))
    write("Leyenda_entidad_debil", deb)
    write("Leyenda_identificador", 'digraph G { graph[dpi=220, pad=0.05]; node[fontname="%s", fontsize=11, shape=plain];\n e [label=<<U>numero_paja</U>>]; }\n' % FONT)
    write("Leyenda_derivado", 'digraph G { graph[dpi=220, pad=0.05]; node[fontname="%s", fontsize=11, shape=plain];\n e [label=<<I>/titular_vigente</I>>]; }\n' % FONT)
    write("Leyenda_opcional", 'digraph G { graph[dpi=220, pad=0.05]; node[fontname="%s", fontsize=11, shape=plain];\n e [label=<fecha_baja <FONT POINT-SIZE="8">(0..1)</FONT>>]; }\n' % FONT)
    rel = ('digraph G { graph[dpi=220, pad=0.05, rankdir=LR, nodesep=0.3, ranksep=1.0]; node[fontname="%s", fontsize=11, shape=box, style=filled, fillcolor="#F7F9FC", color="%s"];\n'
           'A; B; A -> B [dir=both, arrowtail="%s", arrowhead="%s", label=<<I>nombre</I>>, fontname="%s", fontsize=10, color="%s"];\n}\n'
           % (FONT, NAVY, CARD["1"], CARD["0..*"], FONT, LINE))
    write("Leyenda_relacion", rel)
    cardi = ('digraph G { graph[dpi=220, pad=0.05, rankdir=LR, nodesep=0.12, ranksep=0.9]; node[fontname="%s", fontsize=9, shape=plain];\n'
             'a1[label="X"]; b1[label="1"]; a2[label="X"]; b2[label="0..1"]; a3[label="X"]; b3[label="0..*"]; a4[label="X"]; b4[label="1..*"];\n'
             'b1 -> a1 [arrowhead="%s", arrowtail=none, dir=both]; b2 -> a2 [arrowhead="%s", dir=both, arrowtail=none]; '
             'b3 -> a3 [arrowhead="%s", dir=both, arrowtail=none]; b4 -> a4 [arrowhead="%s", dir=both, arrowtail=none];\n}\n'
             % (FONT, CARD["1"], CARD["0..1"], CARD["0..*"], CARD["1..*"]))
    write("Leyenda_cardinalidad", cardi)
    vin = ('digraph G { graph[dpi=220, pad=0.05, rankdir=LR, nodesep=0.3, ranksep=0.4]; node[fontname="%s", fontsize=10];\n'
           'A[shape=box, style=filled, fillcolor="#F7F9FC", color="%s"]; B[shape=box, style=filled, fillcolor="#F7F9FC", color="%s"];\n'
           'r[shape=diamond, style=filled, fillcolor="#DCE3ED", color="%s", label=<<I>vincula</I>>]; '
           'A -> r [dir=both, arrowtail="%s", arrowhead=none]; r -> B [dir=both, arrowtail=none, arrowhead="%s"];\n}\n'
           % (FONT, NAVY, NAVY, NAVY, CARD["1..*"], CARD["1..*"]))
    write("Leyenda_relacion_atributos", vin)
    gen = ('digraph G { graph[dpi=220, pad=0.05, rankdir=BT, nodesep=0.4, ranksep=0.45]; node[fontname="%s", fontsize=10, shape=box, style=filled, fillcolor="#F7F9FC", color="%s"];\n'
           'Supertipo; Subtipo1; Subtipo2; Subtipo1 -> Supertipo [arrowhead=onormal, arrowsize=1.3]; Subtipo2 -> Supertipo [arrowhead=onormal, arrowsize=1.3];\n}\n'
           % (FONT, NAVY))
    write("Leyenda_generalizacion", gen)


def fig1_general():
    L = [dot_head("TB", 0.3, 0.55)]
    for n in ER:
        L.append("  " + er_node(n, only_name=True))
    for r in ER_REL:
        L.append("  " + er_edge(*r))
    d = VINCULO
    L.append('  vinculo [shape=diamond, style=filled, fillcolor="#DCE3ED", color="%s", fontsize=10, label=<<I>%s</I>>];' % (NAVY, d[2]))
    L.append('  Abonado -> vinculo [dir=both, arrowtail="%s", arrowhead=none, color="%s", penwidth=1.2];' % (CARD["1..*"], LINE))
    L.append('  vinculo -> Persona [dir=both, arrowtail=none, arrowhead="%s", color="%s", penwidth=1.2];' % (CARD["1..*"], LINE))
    for sub, sup in GENERALIZACIONES:
        L.append('  %s -> %s [arrowhead=onormal, arrowsize=1.4, color="%s", penwidth=1.4, label=<<I>es_un</I>>, fontsize=10];' % (sub, sup, LINE))
    L.append("  { rank=same; Persona; TipoDocumento }")
    L.append("  { rank=same; RegistroModificacion; RegistroRestauracion }")
    L.append("}\n")
    write("Figura1_ER_General", "\n".join(L))

def fig1_a():
    L = [dot_head("TB", 0.6, 0.6)]
    for n in ("Sector", "Abonado", "Persona"):
        L.append("  " + er_node(n))
    L.append("  " + er_edge(*ER_REL[0]))
    L += ["  " + x for x in vinculo_nodes()]
    L.append("  { rank=same; vinculo; vinculo_attrs }")
    L.append("}\n")
    write("Figura1A_ER_Abonados_y_personas", "\n".join(L))

def fig1_c():
    L = [dot_head("TB", 0.45, 0.7)]
    for n in ("Cuenta", "RegistroBitacora", "RegistroModificacion", "RegistroRestauracion",
              "Respaldo", "CopiaRespaldo"):
        L.append("  " + er_node(n))
    L.append("  " + er_node("Abonado", ref=True))
    for r in ER_REL:
        if r[1] in ("RegistroBitacora", "Respaldo", "CopiaRespaldo") and r[0] in ("Cuenta", "Abonado", "Respaldo"):
            L.append("  " + er_edge(*r))
    for sub, sup in GENERALIZACIONES:
        L.append('  %s -> %s [arrowhead=onormal, arrowsize=1.5, color="%s", penwidth=1.4, label=<<I>es_un</I>>, fontsize=10];' % (sub, sup, LINE))
    L.append("  RegistroModificacion -> RegistroRestauracion [style=invis];")
    L.append("  { rank=same; Abonado; Cuenta }")
    L.append("  { rank=same; RegistroBitacora; Respaldo }")
    L.append("  { rank=same; RegistroModificacion; CopiaRespaldo }")
    L.append("}\n")
    write("Figura1C_ER_Seguridad_bitacora_y_respaldos", "\n".join(L))

if __name__ == "__main__":
    fig1_general()
    fig1_a(); fig1_b(); fig1_c()
    fig2("Figura2A_Relacional_Abonados_y_personas", ["sector", "abonado", "persona", "vinculo_abonado"], [],
         [["sector", "persona"]], "TB", (0.6, 0.8))
    fig2("Figura2B_Relacional_Documentos",
         ["grupo_alternativas", "tipo_documento", "documento", "version_documento"], ["abonado", "persona"],
         [["grupo_alternativas", "abonado", "persona"], ["tipo_documento", "documento"]], "TB", (0.5, 0.7))
    fig2("Figura2C_Relacional_Seguridad_bitacora_y_respaldos",
         ["cuenta", "registro_bitacora", "registro_modificacion", "registro_restauracion", "respaldo", "copia_respaldo"],
         [], [["registro_bitacora", "respaldo"],
                       ["registro_modificacion", "copia_respaldo"]], "TB", (0.45, 0.7),
         ("registro_modificacion -> registro_restauracion [style=invis];",))
    leyendas()
