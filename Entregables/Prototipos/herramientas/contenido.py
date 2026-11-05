# -*- coding: utf-8 -*-
# Contenido para llenar la plantilla de Prototipos de Interfaz (SIGEDA).
# Fuentes: ERS v1.2, Modelos UML v1.0, Modelo ER/Relacional v1.1, DAS v1.1, Visión v1.1, reunión 21/09/2026.
P = "PENDIENTE"
EQUIPO = "Mariangel Arias Alfaro (C4C688)\nAlejandro Arias Rojas (C4C759)\nSebastián Alfaro Arias (C4C212)\nKendal Trejos Cubero (C4K374)"
AUTORES = "M. Arias Alfaro, A. Arias Rojas, S. Alfaro Arias y K. Trejos Cubero"
ENLACE = "https://kendaltc.github.io/sigeda-prototipo/"

PORTADA = [
    ["Integrantes", EQUIPO],
    ["Docente", "Mag. James Mcintosh Molina"],
    ["ASADA y proceso", "Acueducto Bodegas y Pilas · gestión documental de los expedientes de abonados (SIGEDA)"],
    ["Herramienta de prototipado", "HTML, CSS y JavaScript (un solo archivo), publicado en GitHub Pages · enlace de solo lectura: " + ENLACE],
    ["Versión del documento", "v1.0"],
    ["Fecha de entrega", "06/11/2026 · Mediación Virtual"],
]
VERSIONES = [
    ["v0.1", "04/11/2026", AUTORES, "Primer borrador: secciones 0 a 5, 7, 10 a 14 y anexos; prototipo navegable con 75 capturas y mapa de navegación."],
    ["v0.2", "04/11/2026", AUTORES, "Correcciones de la revisión del prototipo hecha por el docente (Mcintosh Molina, 2026b): se quita la revisión de posibles duplicados (PAN-15) por decisión del equipo; D-06 pasa a «Agregar persona asociada»; cuentas «Secretaría» y «Administración»; color solo en los estados; propuesta de que solo la Administración restaure; estados nuevos en PAN-06, PAN-08 y PAN-13; accesibilidad revisada con axe-core; 77 capturas."],
    ["v0.3", "04/11/2026", AUTORES, "Se elimina la sección de bocetos en papel (P-01) por indicación del docente; las secciones 7 a 14 pasan a ser 6 a 13 y las figuras se renumeran."],
    ["v1.0", "06/11/2026", AUTORES, "Entrega al profesor: se agrega el prototipo vertical construido (sección 7), con la prueba de terminado ejecutada y sus capturas. La evaluación con la administradora (sección 8) sigue PENDIENTE de fecha."],
]

PROPOSITO = ("Este documento presenta los prototipos de interfaz de SIGEDA, el sistema que digitaliza y organiza los expedientes de los "
    "1 015 abonados del Acueducto Bodegas y Pilas. Los prototipos sirven para comprobar, antes de programar todo, que la secretaría "
    "y la administradora encuentran cada función, entienden los mensajes y completan sus tareas reales en los tiempos de la ERS "
    "(RNF-01). Los evalúa la administradora del Acueducto (sección 8) y los revisa el docente del curso. Se distinguen los prototipos "
    "desechables, que solo responden una pregunta, del prototipo evolutivo del Incremento 1, que se conserva (Kendall y Kendall, 2011; "
    "Sommerville, 2016; Rogers et al., 2023).")

RELACION = [
    ["Documento de Visión", "v1.1 (25/09/2026)", "Usuarias (3.2) y entorno: una sola laptop, digitalización con fotocopiadoras multifuncionales (no hay escáner propio), respaldo en discos externos. La conexión es estable según la reunión del 21/09/2026 (B-03), no inestable como dice la Visión (Anexo B)."],
    ["ERS", "v1.2 (28/09/2026)", "RF-01 a RF-22 (qué hace cada pantalla), RN-01 a RN-12 (validaciones), RNF-01, RNF-02, RNF-05, RNF-06 y RNF-09 (usabilidad, rendimiento y seguridad), supuestos S-01 a S-21 y la resolución mínima de 1366 × 768 (3.4)."],
    ["Modelos UML", "v1.0 (02/10/2026)", "Casos de uso CU-01 a CU-18, especificación de CU-04 (flujos de PAN-05) y las 12 clases límite, una por pantalla. La v1.1 todavía no existe (Anexo B)."],
    ["DFD (Semana 9)", "Guía DFD de la Semana 9", "Almacenes D1 Abonados, D2 Documentos y D3 Bitácora de respaldos; el Modelo ER propone D4 Cuentas y D5 Bitácora. Cada pantalla que captura datos escribe en uno de ellos."],
    ["Documento de Arquitectura", "v1.1 (27/10/2026) y retroalimentación del 29/10/2026", "Capa de presentación (Next.js en Electron), fachadas IDocumentos e IConsultas, escenarios EC-03 y EC-04, respaldo y restauración (8.2), visor PDF.js y la propuesta de carga de varios archivos (Anexo B del DAS). El 04/11/2026 el equipo decidió construir sobre la base del sistema LICS (sección 7 y Anexo B)."],
    ["Modelo ER y Relacional", "v1.1 (03/11/2026)", "Nombres de tabla.columna de las fichas (sección 6), dominios CHECK, orden del expediente (RN-05), roles TITULAR, COTITULAR y APODERADA, tipo PENDIENTE de los importados y el índice único parcial de persona (tipo_identificacion, identificacion), que impide registrar dos veces la misma cédula. La consulta Q11 y la fusión de personas quedan fuera (Anexo B)."],
]

DEFS_EXTRA = [
    ["Abonado", "Paja de agua con su expediente. Se identifica por el número de paja (RN-01)."],
    ["Titular vigente", "Persona responsable hoy del abonado: vínculo con rol TITULAR y sin fecha de fin (RN-02)."],
    ["Persona asociada", "Cotitular o persona apoderada vinculada a un abonado, con fechas de inicio y fin."],
    ["Completitud", "Indica si el expediente tiene todos los documentos obligatorios según su tipo de abonado (RF-14)."],
    ["Tipo pendiente", "Abonado importado de SADA que todavía no tiene tipo (persona física o jurídica)."],
    ["Estado especial", "Variante de una pantalla: sin datos, error de validación, proceso en curso o éxito."],
    ["D-xx", "Identificador de un cuadro de diálogo (confirmación o captura corta) que se abre sobre una pantalla."],
    ["GitHub Pages", "Servicio gratuito de GitHub que publica una página web de solo lectura a partir de un repositorio."],
]

OBJETIVOS = [
    ["P-02", "¿La secretaría y la administradora encuentran el camino para completar las tareas T-01 a T-06 sin ayuda y entienden los mensajes?", "Desechable · horizontal · media", "HTML, CSS y JavaScript en GitHub Pages", "2 días", "Se bota tras la evaluación; las pantallas aprobadas y las fichas guían la construcción en Next.js."],
    ["P-03", "¿Cargar un documento (CU-04) atraviesa pantalla, controlador, base de datos, almacén cifrado y bitácora conservando la fecha original del documento?", "Evolutivo · vertical · media", "Base del sistema LICS v2.5.0 reutilizada (decisión del 04/11/2026): Next.js, Django 5.2.6 con Django REST Framework 3.16.1 y PostgreSQL 17 en Docker Compose", "1 semana (Semanas 12 y 13)", "Se conserva (Incremento 1)"],
    ["P-04", "¿La administradora del Acueducto aprueba el aspecto (color, tipografía, jerarquía) de las pantallas más usadas?", "Desechable · horizontal · alta", "El mismo HTML con un tema de color (PAN-03, PAN-04, PAN-05 y PAN-07)", "2 horas", "Se bota; la paleta aprobada queda en la guía de estilo (sección 5)."],
]

PERFILES = [
    ["Frecuencia de uso", "Diaria, después de la secretaría (ERS 2.3). Más consultas del 1 al 15 de cada mes (B-07).", "Diaria. Es la primera usuaria (B-04) y hará la digitalización progresiva de los 1 015 expedientes."],
    ["Experiencia con computadoras", "Media: usa SADA (facturación móvil) y herramientas de Microsoft; no es personal técnico (Visión 3.2, ERS 2.3).", "Básica: según la Visión, no tiene un buen manejo de la tecnología. Necesita pocos pasos y mensajes que digan cómo corregir (R-08 del DAS)."],
    ["Tareas más frecuentes", "Consultar y actualizar expedientes, revisar la completitud y la bitácora, administrar respaldos y tipos de documento, importar SADA.", "Digitalizar y cargar documentos, buscar y consultar expedientes, registrar abonados y cambios de titular."],
    ["Lo que más le preocupa", "Perder documentos (ya ha pasado) y no tener respaldo; que al cambiar de titular sigan apareciendo varios nombres (B-21); que los datos lleguen a terceros (B-16).", "SUPUESTO: equivocarse al cargar (tipo, fecha o expediente) y no saber cómo corregir; el tiempo que toma digitalizar dentro de la jornada. Se pregunta en la evaluación."],
    ["Qué no debe poder hacer", "Eliminar documentos (no existe esa función, S-04), modificar o borrar la bitácora (RNF-11), cambiar un número de paja (RN-01) ni cambiar la contraseña de la otra cuenta: solo puede asignarle una temporal (RF-20).", "Lo mismo que la Administración: las dos cuentas tienen los mismos permisos (B-15, RN-09). Propuesta por validar: restaurar un respaldo requeriría la autorización de la cuenta de la Administración (sección 11)."],
]

ENTORNO = [
    ["Equipo", "Una sola laptop operativa, en mal estado, con Windows 10 u 11 de 64 bits (S-15, R-01 del DAS). Resolución desconocida: SUPUESTO de 1366 × 768, el mínimo de la ERS (3.4).", "Solo para computadora (decisión del 04/11/2026): diseño base de 1366 × 768, con ancho mínimo de 1280 px y hasta 1920 × 1080. No hay versión para celular. Menú lateral fijo y tablas con desplazamiento horizontal."],
    ["Escáner y archivos", "No hay escáner propio: se digitaliza con fotocopiadoras e impresoras multifuncionales que generan PDF o PNG. Las fotos de celular deben convertirse (S-08, B-09).", "Carga de varios archivos a la vez, validación de PDF o PNG y de 10 MB antes de guardar, y un mensaje que explica cómo convertir un archivo no aceptado."],
    ["Conexión a internet", "Estable («wifi de 30», B-03). Corrige la Visión, que la describe como inestable (Anexo B). SIGEDA funciona sin internet (R-02 del DAS).", "Ninguna pantalla depende de internet, así que no hay estados «sin conexión». OneDrive aparece solo como destino opcional del respaldo (PAN-08)."],
    ["Lugar de trabajo", "Oficina con atención al público, tres escritorios y una laptop compartida; consultas todos los días, más del 1 al 15 de cada mes (B-07). SUPUESTO: hay interrupciones frecuentes.", "Búsqueda rápida en la barra superior de todas las pantallas; aviso antes de cerrar la sesión por inactividad (D-08) y confirmación al salir con datos sin guardar (D-07)."],
    ["Datos personales", "Cédulas, contratos, firmas (Ley 8968)", "Identificación parcialmente oculta en las listas y completa solo dentro del expediente; aviso en la exportación (RN-10); prototipos solo con datos ficticios."],
]

TAREAS = [
    ["T-01", "«Busque el expediente de la paja 0412 y dígame quién es el titular».", "Secretaría", "Varias veces al día (B-07)", "1 minuto o menos, sin ayuda (RNF-01a)", "CU-05, CU-06"],
    ["T-02", "«Cargue el plano escaneado de la paja 0412; el papel tiene fecha 15/03/2005».", "Secretaría", "Muchas veces al día durante la digitalización", "3 minutos o menos, con la fecha original correcta y sin ayuda (RNF-01b)", "CU-04"],
    ["T-03", "«Cargue la solicitud de 2026 como nueva versión de la solicitud de 2005».", "Secretaría", "SUPUESTO: semanal", "3 minutos o menos; la versión de 2005 sigue en el historial", "CU-04 (A1), CU-06"],
    ["T-04", "«Vea qué documentos le faltan al expediente 0412 y cargue uno desde ahí».", "Administración", "SUPUESTO: semanal", "Identifica los 2 faltantes en 1 minuto o menos y llega a la carga sin volver a buscar", "CU-08, CU-04"],
    ["T-05", "«Registre que la paja 0412 ahora es de Esteban Mora Vega».", "Secretaría o Administración", "SUPUESTO: pocas veces al mes", "SUPUESTO: 3 minutos o menos; el titular anterior queda solo en el historial", "CU-07"],
    ["T-06", "«Revise si el respaldo de ayer salió bien y, si no, haga uno ahora».", "Administración", "Semanal (DAS 8.2)", "SUPUESTO: sabe el estado del respaldo en 1 minuto o menos", "CU-11"],
]

INVENTARIO = [
    ["PAN-01", "Inicio de sesión", "PantallaInicioSesion", "CU-01", "RF-01; RNF-09", "Ambas", "2"],
    ["PAN-02", "Menú principal (Inicio)", "— (marco de navegación; ver la pregunta de control)", "—", "RF-16 (aviso de respaldo pendiente al iniciar sesión)", "Ambas", "2"],
    ["PAN-03", "Buscar expediente (pestañas Expedientes y Documentos)", "PantallaBusquedaExpedientes", "CU-05", "RF-10, RF-11", "Ambas", "1 (Sebastián y Alejandro)"],
    ["PAN-04", "Detalle del expediente (documentos, versiones, completitud y visor)", "PantallaExpediente", "CU-06, CU-12; abre D-01 (CU-14) y D-02 (CU-17)", "RF-07, RF-08, RF-11, RF-12, RF-14, RF-17, RF-19, RF-22", "Ambas", "2"],
    ["PAN-05", "Cargar documento", "PantallaCargaDocumento", "CU-04", "RF-05, RF-06, RF-07", "Ambas", "1 (Mariangel y Kendal)"],
    ["PAN-06", "Registrar o modificar abonado y personas asociadas", "PantallaExpediente (modo edición); abre D-04 y D-06", "CU-02, CU-07, CU-15, CU-18", "RF-02, RF-03, RF-13, RF-21", "Ambas", "2"],
    ["PAN-07", "Panel de completitud", "PantallaCompletitud", "CU-08", "RF-14 (y RF-04: tipo pendiente)", "Ambas (sobre todo la Administración)", "4"],
    ["PAN-08", "Respaldo y restauración (con copia en OneDrive, prueba de restauración y cuarentena)", "PantallaRespaldos; abre D-05", "CU-11", "RF-16", "Ambas; restaurar requiere la Administración (propuesta por validar); el Reloj del sistema dispara el automático", "3"],
    ["PAN-09", "Importar datos de SADA", "PantallaImportacion", "CU-03", "RF-04", "Ambas (sobre todo la Administración)", "3"],
    ["PAN-10", "Tipos de documento y grupos de alternativas", "PantallaTiposDocumento", "CU-09", "RF-09", "Ambas", "4"],
    ["PAN-11", "Bitácora", "PantallaBitacora", "CU-10", "RF-15", "Ambas", "4"],
    ["PAN-12", "Exportar documentos", "PantallaExportacion", "CU-13", "RF-18", "Ambas", "4"],
    ["PAN-13", "Historial de versiones de un documento", "PantallaHistorialVersiones", "CU-06 (y CU-04, A1)", "RF-07", "Ambas", "2"],
    ["PAN-14", "Mi cuenta (cambiar contraseña y asignar una temporal)", "PantallaGestionCuenta", "CU-01, CU-16", "RF-01, RF-20", "Ambas", "2"],
    ["D-01 a D-08", "Diálogos: anular documento, editar datos del documento, baja o reactivación, cambiar titular, restaurar, agregar persona asociada, salir sin guardar y sesión por cerrarse", "Operaciones de las clases anfitrionas: PantallaCargaDocumento.solicitarAnulacion() y editarDatos(); PantallaExpediente.solicitarBajaOReactivacion(), solicitarCambioTitular() y agregarPersonaAsociada(); PantallaRespaldos.solicitarRestauracion()", "CU-14, CU-17, CU-12, CU-07, CU-11, CU-15", "RF-19, RF-22, RF-17, RF-13, RF-16, RF-03; RNF-09", "Ambas", "El de su pantalla"],
]

CONTROL = [
    "Ningún RF queda sin pantalla: los 22 aparecen en la sección 10.1. La única parte sin interfaz es el respaldo automático diario de RF-16, que dispara el Reloj del sistema; su resultado se ve en PAN-08, en el aviso de PAN-02 y en la barra superior.",
    "Toda pantalla responde a algún RF. PAN-02 no tiene clase límite en el UML v1.0 porque no captura datos: es el marco de navegación, con el menú lateral, la búsqueda rápida y el aviso de respaldo pendiente que pide RF-16 al iniciar sesión.",
    "PAN-04 y PAN-06 comparten la clase PantallaExpediente, porque en el UML v1.0 esa clase tiene las operaciones registrarAbonado(), agregarPersonaAsociada(), solicitarCambioTitular() y modificarAbonado(). PAN-06 es su modo de edición.",
    "Anular (CU-14) y editar datos de un documento (CU-17) son diálogos (D-01 y D-02) que se abren desde PAN-04 y usan las operaciones solicitarAnulacion() y editarDatos() de PantallaCargaDocumento. Son acciones cortas que no cambian de contexto.",
    "Se agregan dos pantallas al inventario sugerido: PAN-13 (PantallaHistorialVersiones, RF-07) y PAN-14 (PantallaGestionCuenta, RF-01 y RF-20). La v0.1 tenía además PAN-15 (revisar posibles duplicados), que el equipo quitó el 04/11/2026: la base de datos impide repetir una cédula y PAN-06 avisa si la persona ya existe; la fusión queda como mejora futura (Anexo B). Los nombres de clase sugeridos por la plantilla se corrigen según el UML: PantallaBusquedaExpedientes, PantallaCargaDocumento y PantallaCompletitud.",
    "Orden de los incrementos. 1: la rebanada de carga (PAN-05) y la de búsqueda (PAN-03), planeadas en la Semana 12. 2: sesión y cuentas (PAN-01, PAN-14), el expediente completo (PAN-02, PAN-04, PAN-06, PAN-13) y sus diálogos. 3: respaldo (PAN-08), que debe funcionar antes de cargar datos reales, junto con la importación de SADA (PAN-09). 4: tipos de documento (PAN-10), completitud (PAN-07), bitácora (PAN-11) y exportación (PAN-12). Los tipos de documento iniciales se cargan al instalar (Modelo ER 3.6.1), y la bitácora registra desde el Incremento 1 aunque su pantalla de consulta llegue en el 4.",
]

REGLAS = [
    "Desde cualquier pantalla, después de iniciar sesión, se llega a Buscar expediente en un clic: por el menú lateral o con la búsqueda rápida de la barra superior.",
    "Ninguna tarea frecuente (T-01 a T-04) requiere más de 3 pantallas después de la búsqueda. Para cargar un documento se entra desde el expediente (PAN-04) o desde el panel de completitud (PAN-07), con el expediente ya elegido.",
    "Toda acción que anula, da de baja, cambia el titular o restaura pide confirmación en un diálogo que dice qué pasará y qué se conserva (D-01, D-03, D-04 y D-05). Restaurar además se activa solo al escribir la clave, la autorización y la palabra RESTAURAR.",
    "Salir de un formulario con datos escritos pide confirmación (D-07). Ningún dato se pierde sin aviso, tampoco al cerrarse la sesión por inactividad (D-08).",
    "Toda pantalla secundaria muestra la ruta (por ejemplo, «Buscar expediente › Expediente 0412 › Cargar documento») para volver un paso atrás.",
]

RECORRIDOS = [
    ["T-01", "PAN-02 → escribir «0412» en la búsqueda rápida → «Buscar» → PAN-03 (resultados) → «Abrir» → PAN-04 (el titular vigente se ve en el encabezado)", "3 pantallas · 3 acciones"],
    ["T-02", "PAN-03 → «Abrir» → PAN-04 → «Cargar documento» → PAN-05 → «Elegir archivos» → tipo «Plano legible» y fecha 15/03/2005 → «Guardar documentos» → mensaje de éxito → «Ver expediente» → PAN-04", "3 pantallas · 6 acciones"],
    ["T-03", "PAN-04 → «Nueva versión» en la fila del formulario → PAN-05 (opción «nueva versión» ya marcada) → elegir archivo y fecha 10/02/2026 → «Guardar documentos» → PAN-04 → «v2 · ver versiones» → PAN-13", "3 pantallas · 5 acciones"],
    ["T-04", "Menú «Completitud» → PAN-07 → localizar la fila 0412 (o filtrar) → «Cargar lo que falta» → PAN-05 → «Guardar documentos» → PAN-04", "3 pantallas · 4 acciones"],
    ["T-05", "PAN-04 → «Cambiar titular» → PAN-06 → «Cambiar titular…» → D-04 (nuevo titular y fecha) → «Confirmar cambio de titular» → PAN-04", "2 pantallas y 1 diálogo · 4 acciones"],
    ["T-06", "PAN-02 (muestra un aviso si el respaldo falló) o menú «Respaldos» → PAN-08 (último respaldo y estado de cada copia) → «Respaldar ahora» si hace falta", "1 o 2 pantallas · 2 acciones"],
]

ESTILO = [
    ["Colores (fondo, texto, principal, error, éxito)", "Wireframe: escala de grises (texto #1E1E1E sobre blanco, secundario #4D4D4D, principal #2E2E2E) y color solo en los estados, siempre con texto: verde #2F7A45 sobre #E6F2EA (completo, verificado), ámbar #7A5600 sobre #FFF4D6 (aviso, pendiente) y rojo #A61B1B sobre #FBE9E9 (error, falta). Alta fidelidad: fondo #EEF3F6, paneles blancos, texto #14212B y principal #0B5C8A con texto blanco; los mismos colores de estado.", "Todos los pares cumplen 4,5:1 o más (WCAG 2.2): texto 16,7:1; secundario 8,5:1; principal del wireframe 13,6:1; principal azul 7,2:1; rojo 6,4:1; ámbar 6,1:1; verde 4,6:1. Revisado con axe-core 4.10 en todos los estados: sin infracciones. El estado nunca depende solo del color: siempre lleva texto (World Wide Web Consortium, 2023)."],
    ["Tipografía y tamaño mínimo", "Segoe UI (incluida en Windows); Arial como alternativa. Texto de 15 px, títulos de 22 px, mínimo de 12,5 px solo para ayudas y etiquetas.", "No hay que instalar nada (R-06 del DAS). Es legible a 1366 × 768 para una usuaria con manejo básico (R-08)."],
    ["Botón principal y secundario", "Principal: relleno oscuro (azul en alta fidelidad), uno solo por sección, a la derecha («Guardar documentos», «Buscar»). Secundario: borde y fondo blanco («Cancelar»). Peligroso: borde grueso y el verbo exacto («Anular documento», «Restaurar»). Alto mínimo de 38 px.", "La usuaria reconoce la acción principal sin leer todo, y el verbo dice qué pasa (Krug, 2014; heurísticas 2 y 4)."],
    ["Formato de fecha", "dd/mm/aaaa en campos y tablas; fecha y hora como dd/mm/aaaa hh:mm (24 horas). La fecha del documento se propone con la de hoy.", "Usado en la ERS (RF-06, RN-07)."],
    ["Número de paja", "Texto, tal como se registró, en negrita y en la primera columna de las tablas. Se rechaza con espacios; no se convierte a número, para no perder ceros iniciales.", "RN-01: identifica al abonado y es lo que la usuaria usa para buscar (B-20). abonado.numero_paja es texto (Modelo ER v1.1; Anexo C, pregunta 1)."],
    ["Identificaciones (física, jurídica, DIMEX)", "Lista «Tipo de identificación» y número con máscara según el tipo: física 0-0000-0000 (9 dígitos), jurídica 3-000-000000 (10), DIMEX 11 o 12 dígitos, pasaporte con letras y números. En las listas se oculta la parte central (1-••••-0123).", "persona.tipo_identificacion y persona.identificacion (Modelo ER v1.1); la longitud de la jurídica está pendiente (sección 11). Ocultar en las listas reduce la exposición de datos (Ley 8968)."],
    ["Mensajes de error", "Recuadro arriba con el resumen («Hay 3 archivos con problemas. No se guardó ninguno todavía.») y, junto a cada campo, ⚠ + qué pasó con el dato concreto + qué hacer: «Pesa 14,2 MB y el máximo es 10 MB. Escanéelo a menor resolución o divídalo en dos archivos». Nunca códigos de error.", "RNF-02: en español, con la causa y la acción. Heurística 9 (Nielsen, 1994)."],
    ["Confirmación de acciones riesgosas", "Diálogo que nombra el elemento, dice qué pasará y qué se conserva, con el botón peligroso nombrando la acción. Anular pide un motivo obligatorio. Restaurar pide además la clave de cifrado y escribir RESTAURAR.", "RF-16, RF-17, RF-19, RNF-11 y RNF-13. Previene errores (heurística 5). Nada se borra: solo se anula, se cierra o se agrega."],
    ["Términos del sistema", "Abonado: la paja con su expediente. Titular vigente: la persona responsable hoy. Persona asociada: cotitular o apoderada. Expediente: los documentos de un abonado. Documento: tiene una o más versiones. Se dice «anular», nunca «eliminar». Las cuentas se llaman «Secretaría» (usuario secretaria) y «Administración» (usuario administracion).", "Revisión de la ERS v1.1, glosario de la ERS v1.2, Modelo ER v1.1 y revisión del docente (Mcintosh Molina, 2026b)."],
    ["Íconos", "Pocos y siempre con texto: ✓ (completo, verificado), ⚠ (error o aviso) e indicador giratorio (en proceso). No hay íconos solos.", "Recomendado: ícono siempre acompañado de texto. La secretaría tiene un manejo básico de la tecnología (R-08)."],
]

PEND_BOCETO = "PENDIENTE: foto del boceto a mano (la entrega el equipo)."
BOCETO_QA = [["¿Qué decidieron con este boceto?", "PENDIENTE: se completa con los bocetos."],
             ["¿Qué alternativa descartaron y por qué?", "PENDIENTE: se completa con los bocetos."],
             ["¿Qué duda quedó para la evaluación?", "PENDIENTE: se completa con los bocetos."]]

NAVEGABLE = [
    ["Herramienta", "HTML, CSS y JavaScript en un solo archivo (index.html). Las pantallas, los estados, los diálogos y el mapa de navegación salen de la misma fuente. Las capturas y el mapa se generan con scripts (Playwright y Graphviz)."],
    ["Enlace de solo lectura", ENLACE + ". Copia sin conexión: prototipo/index.html en el archivo .zip (abre con doble clic)."],
    ["Pantalla de inicio del recorrido", "PAN-01 Inicio de sesión: entra con cualquier usuario y contraseña. Un «Panel del prototipo» (abajo a la derecha) permite saltar a cualquier pantalla, estado o diálogo y cambiar a la maqueta de alta fidelidad; se cierra solo al elegir un destino. Una franja superior recuerda que los botones no guardan nada y que todos los datos son ficticios."],
    ["Pantallas incluidas", "14 de 14 del inventario, más 8 diálogos; 77 capturas en total (estados incluidos). Uso previsto: computadora."],
]

# ---------------- Fichas ----------------
FICHAS = {
"PAN-03": dict(
  img="PAN-03_buscar-expediente_exito.png",
  elem=[
    ["Número de paja", "Campo de texto", "abonado.numero_paja", "Sin espacios; coincidencia exacta o por el inicio", "No"],
    ["Nombre del titular", "Campo de texto", "persona.nombre del vínculo vigente (vinculo_abonado.rol = TITULAR y fecha_fin nula)", "Coincidencia parcial, sin distinguir mayúsculas ni tildes", "No"],
    ["Identificación", "Campo de texto", "persona.identificacion", "Con o sin guiones (se normaliza)", "No"],
    ["Sector", "Lista", "sector.nombre (abonado.id_sector)", "Valores del catálogo; «Todos» por defecto", "No"],
    ["Incluir abonados de baja", "Casilla", "abonado.estado", "Marcada por defecto: la baja no elimina el expediente (RN-08)", "No"],
    ["Pestaña Documentos: tipo, nombre identificador, fecha desde y hasta", "Lista, texto y dos fechas", "documento.id_tipo_documento, documento.nombre_identificador, version_documento.fecha_documento", "dd/mm/aaaa; «desde» no mayor que «hasta»; solo documento.estado = VIGENTE", "No"],
    ["Lista de resultados", "Tabla", "abonado.numero_paja, persona.nombre, persona.identificacion (parcial), sector.nombre, abonado.tipo_abonado, abonado.estado y completitud (derivada, Q3)", "Orden por número de paja; máximo 50 filas", "—"],
    ["Al menos un criterio", "Regla del formulario", "—", "Si todos los criterios están vacíos, «Buscar» muestra el aviso de escribir uno", "Sí (uno)"],
  ],
  acc=[
    ["Buscar", "Ejecuta la consulta Q1 por la fachada IConsultas (ControladorBusqueda) con los criterios combinados (todos deben cumplirse)", "Resultados en la misma pantalla, con la cantidad y el tiempo"],
    ["Limpiar", "Borra los criterios", "PAN-03 vacía"],
    ["Abrir (fila)", "Abre el expediente", "PAN-04"],
    ["Pestaña Documentos › Filtrar documentos", "Ejecuta la consulta Q4 en todo el archivo (RF-11)", "Lista de documentos; «Ver» abre PAN-04 con el visor"],
    ["Registrar (en el mensaje sin resultados)", "Lleva al registro de un abonado nuevo", "PAN-06"],
  ],
  est=["Al entrar: «Escriba al menos un criterio y presione Buscar». Sin resultados: «No hay expedientes con el número de paja 9999. Revise el número o busque por el nombre del titular. Si el abonado es nuevo, puede registrarlo».",
       "Campo marcado con ⚠: «El número de paja no puede llevar espacios. Escríbalo sin espacios, por ejemplo 0412». Con más de 50 resultados: «Se muestran los primeros 50 de 214 expedientes del sector Bodegas. Agregue el nombre o el número de paja para acotar».",
       "«Buscando en 1 015 expedientes…» con indicador giratorio y filas de relleno; el botón no se puede presionar dos veces.",
       "Tabla con «7 expedientes encontrados para mora en 0,4 s»; los incompletos y los de baja llevan etiquetas de texto."],
  preg=["Los cuatro criterios de RF-10 (número de paja, nombre del titular vigente, identificación y sector), solos o combinados: deben cumplirse todos. La búsqueda rápida de la barra superior acepta paja o nombre. La pestaña «Documentos» cubre RF-11. En el wireframe: panel de criterios y pestañas.",
        "Sí: «perez» encuentra «Pérez», con unaccent y trigramas de PostgreSQL (DAS 7.2, ADR-06). Solo busca al titular vigente: el anterior no aparece (RN-12, B-21). Lo dice la ayuda bajo el campo Nombre.",
        "Paja, titular vigente, identificación (parcial), sector, tipo, estado, completitud y «Abrir», ordenadas por número de paja. Con cero resultados, un mensaje con la causa y la acción. Con más de 50, se muestran 50 y se pide acotar (estado «más de 50», solo con filas del sector elegido).",
        "Con etiquetas de texto: «De baja» (la fila además va en gris) en Estado, y «Incompleto · faltan 2» o «Tipo pendiente» en Completitud. No depende solo del color.",
        "El tiempo desde «Buscar» hasta mostrar la tabla, con los 1 015 abonados y sus documentos cargados, en la laptop o un equipo equivalente: 19 de 20 búsquedas en 3 s o menos (EC-04). El prototipo muestra el tiempo; en el Incremento 1 se mide con un registro de tiempo en la consulta Q1."],
  traz=("RF-10, RF-11", "RN-01, RN-12", "RNF-01, RNF-02, RNF-05", "CU-05, flujo básico (ingresar criterios, ver resultados, abrir); entrada a CU-06")),
"PAN-04": dict(
  img="PAN-04_detalle-del-expediente_exito.png",
  elem=[
    ["Encabezado del abonado", "Texto", "abonado.numero_paja, sector.nombre, abonado.tipo_abonado, abonado.estado", "Solo lectura", "—"],
    ["Personas del expediente", "Tabla", "persona.nombre, persona.identificacion, vinculo_abonado.rol, vinculo_abonado.fecha_inicio", "Solo vínculos vigentes (fecha_fin nula); un único titular (índice único parcial, RN-02)", "—"],
    ["Historial de titulares", "Sección plegable", "vinculo_abonado.fecha_inicio y fecha_fin con rol TITULAR y fecha_fin con valor (Q5)", "Solo lectura", "—"],
    ["Aviso de completitud", "Recuadro", "Derivado (Q3): tipo_documento.obligatoriedad, grupo_alternativas, tipo_documento.es_exigido_a_cotitulares", "Solo documentos vigentes del titular y de los cotitulares vigentes", "—"],
    ["Lista de documentos", "Tabla", "tipo_documento.prioridad, tipo_documento.nombre, documento.nombre_identificador, persona.nombre (documento.id_persona), version_documento.fecha_documento, version_documento.numero_version", "Orden: prioridad, nombre del tipo e id_documento (RN-05, Q2); solo VIGENTE, salvo el filtro", "—"],
    ["Filtros", "Lista, texto, dos fechas y casilla «Mostrar anulados»", "documento.id_tipo_documento, documento.nombre_identificador, version_documento.fecha_documento, documento.estado", "dd/mm/aaaa; «desde» no mayor que «hasta»", "No"],
    ["Visor del documento", "Visor PDF o PNG integrado (PDF.js)", "version_documento.ruta_archivo (se descifra en memoria), formato, tamano_bytes, fecha_carga", "Se muestra en 5 s o menos (RNF-06)", "—"],
    ["Documento anulado", "Fila en gris con etiqueta, motivo y fecha", "documento.estado, documento.motivo_anulacion, documento.fecha_anulacion", "Visible solo con «Mostrar anulados» (RF-19)", "—"],
  ],
  acc=[
    ["Cargar documento", "Abre la carga con el expediente ya elegido", "PAN-05"],
    ["Ver / Nueva versión / v2 · ver versiones (fila)", "Muestra el documento en el visor; abre la carga en modo «nueva versión»; abre el historial", "Visor en PAN-04; PAN-05; PAN-13"],
    ["Editar datos / Anular (fila)", "Corrige el tipo y el nombre identificador (RF-22) o anula con motivo (RF-19); un evento en la bitácora con el valor anterior y el nuevo", "D-02 o D-01 → PAN-04"],
    ["Modificar abonado / Cambiar titular / Agregar o quitar personas", "Abre el modo de edición del expediente", "PAN-06"],
    ["Dar de baja (o Reactivar)", "Cambia abonado.estado y abonado.fecha_baja sin borrar documentos (RF-17)", "D-03 → PAN-04"],
    ["Exportar / Ver qué falta", "Abre la exportación o el detalle de completitud del abonado", "PAN-12 / PAN-07"],
  ],
  est=["«Este expediente todavía no tiene documentos digitalizados. Mientras tanto se consulta en papel. Cargar el primer documento».",
       "«No se encontró el archivo de Plano legible · Plano lote 12 en la laptop. Los datos del documento siguen guardados. Restaure el último respaldo desde Respaldos o avise a la Administración». El Modelo ER (4.1) marca el archivo como no disponible.",
       "Visor con «Abriendo Plano lote 12… (máximo 5 s)».",
       "Después de cargar: «Documento cargado: Certificación de registro de propiedad (versión 1). Ya aparece en el expediente, en el lugar que le toca según su tipo»."],
  preg=["Por tipo_documento.prioridad (1 Plano legible y 2 Formulario de solicitud, confirmados; del 3 en adelante es provisional, Anexo C pregunta 4), luego por el nombre del tipo y luego por id_documento, es decir, el orden de carga. La columna «Prior.» lo hace visible.",
        "La columna «Versión» muestra la vigente (v1, v2). Si hay más de una, el enlace «v2 · ver versiones» abre PAN-13 con todas, sus fechas y quién las cargó. Ninguna se sobrescribe (RN-06).",
        "No por defecto. Con «Mostrar anulados» aparecen en gris con la etiqueta «Anulado», el motivo y la fecha (RF-19). No cuentan para la completitud.",
        "Sí: el aviso usa solo los documentos vigentes del titular vigente y de los cotitulares vigentes (RF-13, RF-14) y dice qué falta y de quién («Copia de cédula del cotitular Esteban Mora Vega»). Los documentos del titular anterior se ven con la etiqueta «titular anterior», pero no cuentan.",
        "Dentro del expediente se muestran completos el nombre y la identificación de sus personas, porque las dos cuentas tienen los mismos permisos (RN-09). Fuera del expediente, en las listas, la identificación va parcial. El contenido solo se ve en el visor; sale de SIGEDA únicamente con «Exportar», que queda en la bitácora."],
  traz=("RF-07, RF-08, RF-11, RF-12, RF-14, RF-17, RF-19, RF-22", "RN-02, RN-05, RN-06, RN-08, RN-12", "RNF-03, RNF-06", "CU-06, flujo básico; CU-04, pasos 1 y 7; CU-12; CU-14; CU-17")),
"PAN-05": dict(
  img="PAN-05_cargar-documento_seleccionado.png",
  elem=[
    ["Expediente", "Texto con enlace «Cambiar de expediente»", "abonado.numero_paja y persona.nombre del titular vigente", "El abonado debe existir (precondición de CU-04)", "Sí"],
    ["¿Qué va a cargar?", "Botones de opción", "Decide si se crea un documento o una version_documento nueva", "Si es nueva versión, hay que elegir el documento", "Sí"],
    ["Documento del que es nueva versión", "Lista", "version_documento.id_documento (numero_version = la siguiente)", "Solo documentos VIGENTES del expediente", "Sí, si es nueva versión"],
    ["Archivos", "Zona de arrastre y selector de varios archivos", "version_documento.nombre_original, formato, tamano_bytes y hash_sha256 (calculado)", "Solo PDF o PNG (RN-11); hasta 10 MB cada uno (RF-05, S-21)", "Sí"],
    ["Tipo de documento", "Lista por archivo", "documento.id_tipo_documento", "Uno del catálogo", "Sí"],
    ["Persona que lo aporta", "Lista por archivo", "documento.id_persona", "Solo personas con vínculo vigente con el abonado (Modelo ER 2.7); se propone el titular vigente", "No"],
    ["Nombre identificador", "Texto por archivo", "documento.nombre_identificador", "Libre (B-22)", "No"],
    ["Fecha del documento", "Fecha por archivo", "version_documento.fecha_documento", "dd/mm/aaaa; se propone la de hoy (RN-07)", "Sí"],
    ["Fecha de carga", "No es un campo: se informa", "version_documento.fecha_carga", "La asigna el sistema y no se puede cambiar (RF-06)", "—"],
  ],
  acc=[
    ["Elegir archivos (o arrastrar)", "Crea una fila por archivo y valida el formato y el tamaño de inmediato", "Filas con ⚠ si algo no sirve"],
    ["Guardar documentos", "ControladorDocumentos.validarArchivo() y cargarDocumento() o cargarNuevaVersion(): documento y version_documento en una transacción, archivo cifrado con AES-256 y un registro en la bitácora por documento", "Mensaje de éxito → «Ver expediente» (PAN-04) o «Cargar otro documento»"],
    ["Cancelar", "Si ya hay archivos elegidos, pregunta antes de salir", "D-07 → PAN-04"],
    ["Quitar (fila)", "Saca ese archivo de la lista", "La misma pantalla"],
  ],
  est=["Sin archivos: «Todavía no ha elegido archivos» y el botón «Guardar documentos» desactivado.",
       "Recuadro «Hay 3 archivos con problemas. No se guardó ninguno todavía» y en cada fila: «Es un archivo JPG. Solo se aceptan PDF o PNG: conviértalo con la fotocopiadora o elija otro archivo», «Pesa 14,2 MB y el máximo es 10 MB. Escanéelo a menor resolución o divídalo en dos archivos» y «Falta el tipo de documento. Elíjalo en la lista».",
       "«Cifrando y guardando el archivo 2 de 2…» con barra de avance; el botón cambia a «Guardando…» desactivado y se pide no cerrar SIGEDA.",
       "«Se cargaron 2 documentos al expediente 0412», con el tipo y la fecha de cada uno y la aclaración de que la carga quedó en la bitácora."],
  preg=["Se llega desde el expediente (PAN-04) o desde el panel de completitud (PAN-07), así que el expediente ya viene elegido y se muestra arriba; «Cambiar de expediente» vuelve a PAN-03. La persona se elige por archivo, en una lista con solo las personas vigentes del expediente y su rol; se propone el titular vigente.",
        "En la columna «Fecha del documento» de cada archivo: se propone la de hoy y se puede cambiar, con la ayuda «Si digitaliza un papel viejo, ponga la fecha que tiene el papel». La fecha de carga no es un campo: se explica que se guarda sola, y luego se ve en el visor y en PAN-13 («Cargado: 04/11/2026 09:12»).",
        "Con la opción explícita «Una nueva versión de un documento que ya está en el expediente» y la lista del documento. El enlace «Nueva versión» de cada fila de PAN-04 abre la pantalla con esa opción ya marcada. El sistema no lo adivina por el nombre del archivo.",
        "Se valida al elegir el archivo, antes de guardar. La fila queda marcada con ⚠, la causa con el dato real y la acción, y no se guarda nada mientras haya errores. El límite de 10 MB viene de RF-05 y S-21; la plantilla lo atribuye a RNF-06, que es el tiempo de visualización (Anexo B).",
        "Un mensaje con lo que se cargó y dos salidas: «Ver expediente» (PAN-04, con el documento en su lugar según la prioridad) o «Cargar otro documento»."],
  traz=("RF-05, RF-06, RF-07 (además RF-13, persona que aporta, y RF-15, bitácora)", "RN-06, RN-07, RN-11", "RNF-01, RNF-02, RNF-03, RNF-10", "CU-04, pasos 1 a 7, A1 y E1")),
"PAN-06": dict(
  img="PAN-06_registrar-o-modificar-abonado-y-personas_modificar.png",
  elem=[
    ["Número de paja", "Campo de texto", "abonado.numero_paja", "Único; no se puede cambiar después (RN-01)", "Sí"],
    ["Sector", "Lista", "abonado.id_sector (sector.nombre)", "Del catálogo; los importados pueden no tenerlo", "Sí al registrar (RF-02)"],
    ["Tipo de abonado", "Botones de opción", "abonado.tipo_abonado", "PERSONA_FISICA o PERSONA_JURIDICA; PENDIENTE solo por importación", "Sí"],
    ["Titular vigente: nombre", "Campo de texto y «Buscar persona ya registrada» (D-06)", "persona.nombre; vinculo_abonado (rol TITULAR, fecha_inicio)", "Texto libre; se puede elegir una persona ya registrada", "Sí"],
    ["Tipo de identificación y número", "Lista y campo con máscara", "persona.tipo_identificacion, persona.identificacion", "Se llenan juntos o ninguno; longitud según el tipo. Únicos (índice único parcial): si la cédula ya existe, aviso «Ya existe una persona con la cédula…» con la opción «Usar esa persona»", "Sí al registrar a mano; no en los importados"],
    ["Personas asociadas", "Tabla editable", "vinculo_abonado.id_persona, rol (COTITULAR o APODERADA), fecha_inicio y fecha_fin", "Sin periodos superpuestos (EXCLUDE); quitar es poner fecha_fin", "No"],
    ["Historial de titulares", "Tabla de solo lectura", "vinculo_abonado con rol TITULAR y fecha_fin con valor", "—", "—"],
    ["Estado", "Texto", "abonado.estado, abonado.fecha_baja", "Se cambia con D-03 desde PAN-04", "—"],
  ],
  acc=[
    ["Guardar (registrar)", "ControladorAbonados: abonado, persona y vínculo TITULAR en una transacción; evento CREACION en la bitácora", "Éxito → «Cargar documentos» (PAN-05) o «Ver expediente» (PAN-04)"],
    ["Guardar (modificar)", "Actualiza sector, tipo y vínculos; un evento MODIFICACION por elemento, con el valor anterior y el nuevo", "PAN-04"],
    ["Cambiar titular…", "D-04: nuevo titular y fecha. Cierra el vínculo anterior y abre el nuevo en una transacción; evento CAMBIO_TITULAR", "PAN-04 con el titular nuevo"],
    ["+ Agregar persona / Buscar persona ya registrada", "D-06: busca por cédula o nombre; si no aparece, registra una persona nueva con rol y fecha de inicio", "D-06 → PAN-06"],
    ["Quitar del expediente", "Cierra el vínculo con la fecha de hoy; los documentos de la persona se quedan", "La misma pantalla"],
    ["Usar esa persona (aviso de cédula existente)", "Toma la persona ya registrada en vez de crear otra", "La misma pantalla"],
  ],
  est=["Formulario vacío «Registrar abonado» con «Aún no hay personas asociadas». Abonado importado: «Abonado importado de SADA el 14/09/2026: faltan el tipo de abonado, el sector y la identificación del titular».",
       "«No se pudo guardar: hay 2 datos por corregir», más «El número de paja 0412 ya está registrado (Ana Lucía Mora Vega). Revise el número o abra ese expediente», «La cédula física tiene 9 dígitos (ejemplo 1-0000-0123) y aquí hay 8». Si la cédula ya está registrada: «Ya existe una persona con la cédula física 1-0000-0123: Ana Lucía Mora Vega, titular de la paja 0412», con «Usar esa persona» o «Revisar el número».",
       "«Guardando abonado, titular y vínculo en una sola operación…».",
       "«Abonado 0533 registrado con su titular vigente. Quedó en la bitácora a nombre de la cuenta secretaria. Ahora puede cargar sus documentos»."],
  preg=["Obligatorios: número de paja, tipo de abonado, sector, y nombre e identificación del titular (RF-02). Opcionales: las personas asociadas. Excepción: los importados de SADA llegan sin tipo, sector ni identificación (Modelo ER: PENDIENTE y columnas opcionales) y se completan aquí.",
        "La lista «Tipo de identificación» cambia la máscara y la ayuda: física 9 dígitos (0-0000-0000), jurídica 10 (3-000-000000, S-02), DIMEX 11 o 12, pasaporte con letras y números sin longitud fija. Se valida al salir del campo. Las longitudes están pendientes de confirmar (sección 11).",
        "En la tabla «Personas asociadas», con su rol (Cotitular o Apoderada) y sus fechas. «+ Agregar persona» abre D-06, que busca primero si ya existe. «Quitar del expediente» no borra: pone fecha_fin con la fecha de hoy, y sus documentos se quedan.",
        "El botón «Cambiar titular…» abre D-04: nuevo titular (existente o nuevo) y fecha. El diálogo explica que el actual pasa al historial con fecha de fin y que sus documentos se conservan. Se cierra un vínculo y se abre otro en una transacción, y el historial se ve en «Historial de titulares». El tipo de abonado no cambia (RF-13).",
        "Con un aviso arriba que dice de dónde viene y qué le falta, y el campo Tipo marcado con «Tipo pendiente: elija uno para que se pueda calcular la completitud». Se llega desde el grupo «Tipo pendiente» de PAN-07."],
  traz=("RF-02, RF-03, RF-13, RF-21 (y RF-04)", "RN-01, RN-02, RN-12", "RNF-02", "CU-02 y CU-07, flujos básicos; CU-15; CU-18")),
"PAN-07": dict(
  img="PAN-07_panel-de-completitud_exito.png",
  elem=[
    ["Indicadores", "Cuatro tarjetas", "Conteos derivados (Q3 y Q8) sobre abonado.estado y abonado.tipo_abonado", "Los de baja no cuentan", "—"],
    ["Avance de la digitalización", "Barra", "Porcentaje de abonados ACTIVOS con expediente completo", "—", "—"],
    ["Filtros", "Cuatro listas y una casilla", "Estado de completitud (derivado), sector.nombre, tipo_documento.nombre del faltante, abonado.tipo_abonado, abonado.estado", "—", "No"],
    ["Lista de incompletos", "Tabla", "abonado.numero_paja, persona.nombre (titular vigente), sector.nombre, abonado.tipo_abonado y tipos faltantes", "Orden por número de paja", "—"],
    ["Faltantes de un grupo de alternativas", "Etiqueta con borde discontinuo", "grupo_alternativas.nombre y sus tipo_documento", "Se cumple con cualquiera de los tipos del grupo (RN-03b)", "—"],
    ["Detalle por persona", "Tabla", "tipo_documento.obligatoriedad, tipo_documento.es_exigido_a_cotitulares, vinculo_abonado.rol", "Solo titular y cotitulares vigentes; solo documento.estado = VIGENTE", "—"],
    ["Tipo pendiente", "Tabla aparte", "abonado.tipo_abonado = PENDIENTE (Q8)", "No se les calcula la completitud (RF-14)", "—"],
  ],
  acc=[
    ["Aplicar filtros", "Recalcula la lista con los filtros elegidos", "La misma pantalla"],
    ["Cargar lo que falta", "Abre la carga con el expediente ya elegido", "PAN-05"],
    ["Abrir", "Abre el expediente", "PAN-04"],
    ["Asignar tipo (tipo pendiente)", "Abre el modo de edición del abonado importado", "PAN-06"],
    ["Ver qué falta (desde PAN-04)", "Muestra el detalle por persona del abonado", "PAN-07, estado de detalle"],
  ],
  est=["«Todavía no hay abonados registrados. Importe el listado de SADA para empezar a medir el avance», con enlace a PAN-09.",
       "No hay datos que escribir, solo filtros. Si un filtro no encuentra nada: «Ningún abonado del sector Pilas tiene pendiente el Contrato de servicio. Cambie el filtro Documento que falta o elija otro sector».",
       "«Calculando la completitud de 1 011 expedientes activos…», con las tarjetas en «—».",
       "Tarjetas (cada una dice «de 1 011 activos»), barra de avance y lista de incompletos con lo que falta."],
  preg=["Primero cuatro tarjetas con números (completos, incompletos, tipo pendiente y de baja) y la barra de avance; luego la lista de incompletos con lo que les falta. Las etiquetas llevan texto, no solo color.",
        "Una sola etiqueta con borde discontinuo: «Uno de: Permiso de construcción vigente o Formulario de construcción y uso del agua» (RN-03b). En el detalle es una fila de grupo, y se cumple con cualquiera de los dos.",
        "Por estado de completitud, sector, documento que falta y tipo de abonado, más una casilla para mostrar los de baja.",
        "Los de tipo pendiente van en una sección aparte con «Asignar tipo» y no se les calcula la completitud (RF-14). Los de baja no cuentan en el avance y se ocultan, salvo que se marque la casilla.",
        "Sí: «Cargar lo que falta» abre PAN-05 con el expediente elegido (T-04), y en el detalle hay un botón «Cargar» por cada faltante."],
  traz=("RF-14 (y RF-04, RF-09)", "RN-03a, RN-03b, RN-04", "RNF-01", "CU-08, flujo básico")),
"PAN-08": dict(
  img="PAN-08_respaldo-y-restauracion_exito.png",
  elem=[
    ["Último respaldo completo", "Texto", "respaldo.fecha_hora con respaldo.estado = COMPLETO (Q9)", "Aviso si pasó más de 1 día (RNF-12)", "—"],
    ["Copias", "Texto", "copia_respaldo.destino (DISCO_EXTERNO, ONEDRIVE), copia_respaldo.estado, copia_respaldo.fecha_hora_verificacion", "COMPLETO si y solo si hay al menos una copia VERIFICADA", "—"],
    ["Próximo respaldo automático", "Texto", "Configuración del Programador de tareas (DAS 5.1)", "—", "—"],
    ["Historial de respaldos", "Tabla", "respaldo.fecha_hora, respaldo.tipo, respaldo.estado, respaldo.tamano_bytes; copia_respaldo por destino", "Retención de 7 diarios y 4 semanales (DAS 8.2)", "—"],
    ["Respaldo por restaurar", "Lista (D-05)", "respaldo.id_respaldo, respaldo.nombre_paquete", "Solo respaldos COMPLETOS", "Sí"],
    ["Clave de cifrado", "Campo de contraseña (D-05)", "— (no se guarda; RNF-13)", "Debe descifrar el paquete", "Sí"],
    ["Autorización de la Administración", "Campo de contraseña (D-05)", "cuenta.hash_contrasena de la cuenta con cuenta.perfil = ADMINISTRADORA (se verifica, no se guarda)", "Propuesta por validar (sección 11)", "Sí, si se aprueba"],
    ["Confirmación", "Texto «RESTAURAR» (D-05)", "—", "Debe coincidir; «Restaurar» queda desactivado hasta completar clave, autorización y RESTAURAR", "Sí"],
    ["Copia en OneDrive", "Carpeta y casilla (estado «onedrive»)", "copia_respaldo.destino = ONEDRIVE", "Solo si se confirma S-10", "No"],
    ["Prueba de restauración", "Fecha, respaldo, computadora, resultado y observaciones (estado «prueba»)", "Sin tabla en el Modelo ER v1.1: se propone en el Anexo B", "Propuesta: cada 3 meses (DAS 8.2)", "Sí, al registrarla"],
    ["Archivos en cuarentena", "Contador y enlace", "registro_bitacora.accion = CUARENTENA", "Archivos sin registro (corrección 2.3 del DAS)", "—"],
  ],
  acc=[
    ["Respaldar ahora", "ControladorRespaldos: respaldo MANUAL, copia y verificación SHA-256 de cada copia; evento RESPALDO en la bitácora", "Mensaje de éxito o de error en la misma pantalla"],
    ["Restaurar un respaldo…", "D-05: respaldo automático previo, restauración de la base y de los documentos, y registro en registro_restauracion; la bitácora no se borra", "PAN-08 con el mensaje de restauración"],
    ["Configurar (OneDrive)", "Guarda la carpeta de OneDrive como segundo destino", "PAN-08"],
    ["Registrar prueba", "Anota el resultado de la prueba de restauración en otra computadora", "PAN-08"],
    ["Ver lista (cuarentena)", "Muestra los archivos sin registro apartados, con fecha y motivo", "PAN-08, estado «cuarentena»"],
  ],
  est=["«Aún no hay ningún respaldo. Conecte el disco externo y presione Respaldar ahora. Después SIGEDA respaldará solo todos los días».",
       "Verificación fallida: «El respaldo de las 10:05 falló: la copia en el disco externo no coincide con el original…». Disco desconectado: «El disco externo no está conectado. El respaldo automático de ayer (03/11/2026, 16:30) quedó pendiente», «Reintentando cada 30 minutos», con el mismo aviso en PAN-02 y en ámbar en la barra superior.",
       "«Respaldando… copiando documentos (45 %)», con barra de avance; se puede seguir trabajando, pero no desconectar el disco.",
       "«Respaldo completo y verificado: 04/11/2026 10:05. La copia en el disco externo coincide con el original». La tarjeta, el historial y la barra superior pasan a esa fecha."],
  preg=["La tarjeta «Último respaldo completo» muestra la fecha, hace cuánto fue y el estado de cada copia. Además, la barra superior de todas las pantallas muestra el último respaldo, y PAN-02 avisa si pasó más de 1 día o si quedó pendiente.",
        "El aviso «El disco externo no está conectado…» en PAN-08 y al iniciar sesión (PAN-02), hasta que se complete (RF-16). Si OneDrive está configurado y su copia se verifica, el respaldo queda COMPLETO con un aviso de que faltó el disco (corrección 2.2 del DAS).",
        "Cada copia se verifica con SHA-256 al copiarla (estado VERIFICADA). La prueba de restauración en otro equipo aparece como «Pendiente (propuesta: cada 3 meses)» para recordarla (DAS 8.2).",
        "D-05 avisa que se reemplazarán todos los abonados y documentos por los de esa fecha y que se perderá lo posterior, que antes se hace un respaldo del estado actual y que la bitácora no se borra: se agrega el registro de la restauración (RNF-11). Pide la clave de cifrado, la autorización de la Administración (propuesta) y escribir RESTAURAR; el botón se activa solo al completar todo.",
        "Propuesta por validar: cualquiera de las dos cuentas inicia la restauración, pero se requiere la contraseña de la Administración, porque es la responsable de los respaldos (DAS 8.2) y la acción reemplaza todo. Es una excepción a RN-09 (mismos permisos), así que se pregunta en la evaluación (sección 11) y se anota en el Anexo B. La restauración queda en la bitácora."],
  traz=("RF-16", "RN-08, RN-09 (excepción propuesta)", "RNF-04, RNF-10, RNF-11, RNF-12, RNF-13", "CU-11")),
}
ESTADOS_LABEL = ["Sin datos / sin resultados", "Error de validación", "Proceso en curso", "Éxito"]

RESTO = [
    ["PAN-01 Inicio de sesión", "PAN-01_inicio-de-sesion_*.png (4)", "Entrar con usuario y contraseña; bloqueo de 5 minutos tras 5 intentos y cambio obligatorio de una contraseña temporal (RF-01, RF-20, RNF-09)."],
    ["PAN-02 Menú principal (Inicio)", "PAN-02_menu-principal-inicio_*.png (2)", "Punto de partida: accesos a buscar, cargar y registrar, avance de la digitalización y aviso de respaldo pendiente (RF-16)."],
    ["PAN-09 Importar datos de SADA", "PAN-09_importar-datos-de-sada_*.png (5)", "Importar el listado de SADA en 4 pasos con resumen de importados, omitidos y rechazados (RF-04)."],
    ["PAN-10 Tipos de documento", "PAN-10_tipos-de-documento_*.png (3)", "Definir prioridad, obligatoriedad, exigencia a cotitulares y grupos de alternativas de cada tipo (RF-09)."],
    ["PAN-11 Bitácora", "PAN-11_bitacora_*.png (3)", "Consultar los registros por cuenta, fechas, paja y acción, con el valor anterior y el nuevo de cada campo (RF-15)."],
    ["PAN-12 Exportar documentos", "PAN-12_exportar-documentos_*.png (3)", "Copiar a una carpeta o imprimir documentos elegidos de un expediente, con aviso de confidencialidad (RF-18, RN-10)."],
    ["PAN-13 Historial de versiones", "PAN-13_historial-de-versiones_*.png (2)", "Ver todas las versiones de un documento con su fecha del documento, fecha de carga y quién la cargó (RF-07)."],
    ["PAN-14 Mi cuenta", "PAN-14_mi-cuenta_*.png (3)", "Cambiar la contraseña propia y asignar una contraseña temporal a la otra cuenta (RF-01, RF-20)."],
    ["D-01 a D-08 Diálogos", "D-01_anular-documento.png … D-08_sesion-por-cerrarse.png", "Confirmaciones y capturas cortas: anular, editar datos, baja o reactivación, cambiar titular, restaurar, agregar persona asociada, salir sin guardar y sesión por cerrarse."],
]

ALTA = ("La maqueta de alta fidelidad (P-04) usa el mismo archivo del prototipo con un tema de color: azul principal #0B5C8A, colores de "
    "estado con texto y una franja superior que dice «Maqueta de alta fidelidad (P-04) · solo muestra el aspecto: no funciona». "
    "Se aplica a todas las pantallas y se capturó en PAN-03, PAN-04, PAN-05 y PAN-07 (archivos ALTA_PAN-xx.png del .zip). "
    "Se mostrará a la administradora al final de la sesión de evaluación, después de las tareas, para que no confunda el aspecto con un sistema terminado. "
    "PENDIENTE: registrar a quién se mostró, qué opinó del aspecto y cómo se le aclaró que todavía no funciona.")

VERTICAL = [
    ["Función (rebanada)", "CU-04 Cargar documento (RF-05, RF-06 y RF-07), plan del Incremento 1 (pareja de Mariangel Arias y Kendal Trejos). Construida completa: carga de uno o varios archivos con tipo, persona que lo aporta (solo personas con vínculo vigente), nombre identificador y fecha del documento; nueva versión de un documento existente; validación del formato por el contenido del archivo (no por la extensión) y del tamaño máximo de 10 MB; cifrado, SHA-256 y bitácora en una sola transacción. Para comprobarla se hicieron además, en versión mínima, el inicio de sesión (PAN-01), el expediente (PAN-04) y el historial de versiones (PAN-13)."],
    ["Versión", "0.1.0 (archivo VERSION del repositorio)."],
    ["Pantalla (PAN-xx)", "PAN-05 Cargar documento (PantallaCargaDocumento), prototipo evolutivo vertical, con los 6 estados del prototipo navegable: inicial, seleccionado, error, cargando, éxito y nueva versión. Ruta: /sigeda/expedientes/<número de paja>/cargar. Corre localmente (localhost) con Docker Compose; no está publicado en internet porque usa la base de datos y el almacén cifrado."],
    ["Clase control y métodos", "ControladorDocumentos (backend/src/apps/documents/controlador.py): validar_archivo(), cargar_documento() y cargar_nueva_version(); las dos últimas son transacciones (@transaction.atomic). La bitácora se registra con bitacora/servicio.registrar(), que cumple el papel de ControladorBitacora.registrar(). Los nombres siguen la convención de Python (snake_case) en lugar de la del UML."],
    ["Interfaz y repositorio", "ControladorDocumentos hace de fachada IDocumentos (no se creó una clase aparte); RepositorioDocumentos (listar_expediente, listar_versiones, obtener_version_vigente) para las consultas (IPersistencia); AlmacenArchivosCifrados (IAlmacenArchivos) con ServicioCifrado (AES-256-GCM). API REST: POST /api/sigeda/documentos/cargar/ y descarga descifrada de cada versión en /api/sigeda/documentos/<id>/versiones/<n>/descargar/."],
    ["Tablas que usa", "Las 14 tablas del Modelo ER v1.1 quedaron creadas (migraciones de Django y script DDL sigeda_v1.1.sql, generado con pg_dump desde la base migrada) con sus llaves primarias simples y compuestas, llaves foráneas, valores únicos, los índices únicos parciales de RN-02 y de la cédula, las 2 restricciones EXCLUDE de vinculo_abonado y los CHECK de reglas (anulación, baja, origen de la bitácora, prioridad, tamaño). PENDIENTE: los CHECK de los dominios de valores (por ejemplo, tipo_abonado, rol, formato, perfil, accion), que hoy solo valida la aplicación. CU-04 escribe en documento, version_documento y registro_bitacora, y lee abonado, persona, vinculo_abonado, tipo_documento y cuenta."],
    ["Lenguaje, base de datos y herramientas", "Python 3.13 con Django 5.2.6 y Django REST Framework 3.16.1; PostgreSQL 17 con las extensiones btree_gist, unaccent y pg_trgm; Next.js 16 y React 19 (TypeScript); Docker Compose; librería cryptography (AESGCM); Playwright y axe-core para las capturas y la accesibilidad. Base: LICS v2.5.0 (Arias Rojas, s.f.), de la que se quitaron los módulos de negocio que no aplican (inventario, ventas, caja, clientes y migración de datos)."],
    ["Repositorio de código (si existe)", "https://github.com/KendalTC/SIGEDA (rama main). La prueba de terminado y las capturas están en docs/evidencia/. El script DDL se entrega junto con este documento (sigeda_v1.1.sql); PENDIENTE subirlo al repositorio, porque el .gitignore heredado de LICS excluye los archivos .sql."],
]

PRUEBAS = [
    ["Conservar la fecha original", "5 PDF ficticios de menos de 10 MB (prueba automática) y 1 PDF por la API, abonado de prueba 0412, fecha del documento 15/03/2005", "5 cargas; fecha_documento = 15/03/2005 en las 5; el SHA-256 del archivo descifrado coincide con el original", "Las 5 versiones quedaron con fecha_documento 15/03/2005 y el SHA-256 correcto. En la base real: id_documento 1, versión 1, fecha 2005-03-15; el archivo descargado y descifrado tiene el mismo SHA-256 que el original y no tiene diferencias.", "Sí"],
    ["Cifrado", "El archivo de la prueba anterior, leído directo del almacén sin pasar por SIGEDA", "0 archivos legibles fuera de SIGEDA (RNF-10)", "El archivo guardado no empieza con %PDF- ni coincide con el original; mide 295 bytes = 267 del original + 12 del nonce + 16 de la etiqueta GCM. Solo AlmacenArchivosCifrados lo recupera.", "Sí"],
    ["Rechazos", "1 archivo .jpg y 1 PDF de 11,0 MB (cualquier tamaño mayor a 10 MB sirve)", "2 rechazos con mensaje de causa y acción; 0 filas nuevas en documento y version_documento", "Respuesta 400 con 2 mensajes: «Es un archivo JPG. Solo se aceptan PDF o PNG: conviértalo con la fotocopiadora o elija otro archivo» y «Pesa 11,0 MB y el máximo es 10 MB. Escanéelo a menor resolución o divídalo en dos archivos». Las filas de documento y version_documento son las mismas antes y después.", "Sí"],
    ["Nueva versión", "Versión 2 del documento de la prueba 1 (Certificación de registro de propiedad), con fecha 10/02/2026", "numero_version = 2 creada; la versión 1 conserva fecha_documento 15/03/2005", "numero_version = 2 con fecha 2026-02-10; la versión 1 sigue con fecha 2005-03-15.", "Sí"],
    ["Bitácora", "Las 2 cargas reales de las pruebas 1 y 4", "1 fila en registro_bitacora (CREACION) por cada carga, a nombre de la cuenta", "2 filas CREACION (id_registro_bitacora 1 y 2), las dos con id_cuenta 1 (secretaria).", "Sí"],
    ["Pruebas automáticas", "make test-sigeda: CU-04 y restricciones del Modelo ER (un solo titular vigente, periodos sin traslape, cédula única, CHECK de anulación, etc.)", "Todas pasan", "40 de 40 pruebas pasaron.", "Sí"],
    ["Accesibilidad", "axe-core con las reglas del prototipo, en PAN-01, PAN-04, PAN-05 (inicial, con archivos y errores, nueva versión) y PAN-13", "0 infracciones, igual que el prototipo navegable", "Primera corrida: 2 críticas (campos de PAN-05 sin etiqueta asociada) y 1 menor (encabezado vacío en PAN-13). Se corrigieron y la segunda corrida dio 0.", "Sí"],
]

APRENDIZAJES = ("Se confirmaron las decisiones del Documento de Arquitectura v1.1 para esta rebanada. ADR-02: el cifrado AES-256-GCM con SHA-256 funciona como se diseñó; el formato del archivo cifrado, que el DAS no definía, quedó como nonce de 12 bytes + contenido cifrado + etiqueta de 16 bytes. ADR-01 y Modelo ER v1.1: Django 5.2 maneja las llaves primarias compuestas (version_documento, vinculo_abonado) junto con los índices únicos parciales y las restricciones EXCLUDE de PostgreSQL 17, así que el modelo se implementó sin cambios. Reutilizar LICS dio hecha la infraestructura (Docker Compose, Nginx, pruebas), pero obligó a quitar sus módulos de negocio y a renombrar «lics». Cambios y hallazgos: la fachada IDocumentos no se creó como clase aparte, porque ControladorDocumentos cumple ese papel (Anexo B); el formato se valida por la firma del archivo y no por la extensión; falta un proceso de reconciliación para el caso raro de que SIGEDA se cierre entre la confirmación en la base y el traslado del archivo desde la cuarentena (Incremento 3); el campo de fecha del navegador muestra el formato según el idioma del navegador (en las capturas, tomadas con un navegador en inglés, aparece mm/dd/aaaa), así que hay que forzar dd/mm/aaaa; y la clave de cifrado vive por ahora en un archivo de configuración fuera del repositorio (SUPUESTO): su custodia física y digital (RNF-13) queda para el despliegue.")

PLAN_SESION = [
    ["Participantes (rol, no nombre completo)", "Administradora del Acueducto (usuaria real). Si está disponible, también la secretaría."],
    ["Fecha, lugar y modalidad", "PENDIENTE: fecha antes del 06/11/2026; oficina del Acueducto; presencial, con el prototipo en una laptop del equipo."],
    ["Quién conduce y quién anota", "PENDIENTE: un integrante conduce con el guion del Anexo C y otro anota tiempos, dudas y comentarios textuales."],
    ["Prototipo usado (P-02, P-03…)", "P-02 (navegable) para las tareas y P-04 (maqueta de alta fidelidad) al final."],
    ["Tareas evaluadas (de la sección 2.3)", "T-01 a T-06, en ese orden, leídas igual a cada participante."],
]
RESULTADOS = [[f"T-0{i}", P, P, P, P] for i in range(1, 7)]
HALLAZGOS = [["H-01", P, "PENDIENTE: se completa con la sesión de evaluación.", P, P, P]]

HEUR = [
    ["1. Visibilidad del estado del sistema", "El último respaldo se ve en la barra superior de todas las pantallas; PAN-05 muestra «Cifrando y guardando el archivo 2 de 2…» con barra de avance; PAN-03 muestra cuántos resultados hay y en cuánto tiempo.", "Cumple"],
    ["2. Relación con el mundo real (palabras de la usuaria)", "Usa «paja», «titular», «expediente» y «cotitular», que son palabras de la administradora. Pero «nombre identificador», «tipo pendiente» y «cuarentena» son términos del equipo (PAN-05, PAN-07, PAN-08): se preguntan en la evaluación.", "Parcial"],
    ["3. Control y libertad (deshacer, cancelar)", "Todos los formularios y diálogos tienen «Cancelar» (los diálogos también se cierran con Esc), y salir con datos pide confirmación (D-07). Pero no se puede deshacer una anulación (D-01): solo se puede volver a cargar el documento.", "Parcial"],
    ["4. Consistencia y estándares", "Un solo botón principal por sección, en la misma posición; fechas dd/mm/aaaa y mensajes con el mismo formato en las 14 pantallas; las migas siempre arriba.", "Cumple"],
    ["5. Prevención de errores", "PAN-05 valida formato y tamaño al elegir el archivo, antes de guardar; PAN-06 avisa si ya existe una persona con esa cédula; «Restaurar» (D-05) se activa solo con la clave, la autorización y la palabra RESTAURAR. No se previene cargar en el expediente equivocado: el expediente se muestra arriba, pero no se confirma.", "Parcial"],
    ["6. Reconocer antes que recordar", "Listas para tipo de documento, persona y sector; la fecha del documento propuesta; el expediente visible arriba en la carga; los faltantes con nombre en PAN-07.", "Cumple"],
    ["7. Flexibilidad y eficiencia de uso", "Búsqueda rápida en la barra superior y carga de varios archivos a la vez (PAN-05). No hay atajos de teclado ni se recuerda el último tipo de documento usado, lo que haría más lenta la digitalización masiva.", "Parcial"],
    ["8. Diseño estético y minimalista", "PAN-04 junta datos del abonado, personas, aviso, filtros, tabla y visor; a 1366 × 768 hay que desplazarse para ver todos los documentos. Las demás pantallas son sobrias.", "Parcial"],
    ["9. Ayudar a reconocer, diagnosticar y recuperarse de errores", "Los mensajes dicen la causa con el dato y qué hacer: «Pesa 14,2 MB y el máximo es 10 MB. Escanéelo a menor resolución o divídalo en dos archivos» (PAN-05); «El número de paja 0412 ya está registrado…» (PAN-06).", "Cumple"],
    ["10. Ayuda y documentación", "Solo hay textos de ayuda bajo los campos y una franja que aclara que el prototipo no guarda nada. No hay ayuda contextual ni una guía breve para la inducción de 30 minutos que exige RNF-01.", "No"],
]

DATOS_PERS = [
    ["Todos los nombres, cédulas y números de paja de los prototipos son ficticios.", "Sí", "Nombres y razones sociales inventados; identificaciones con tomo 0000, que no existe en el Registro Civil, y números de paja inventados. Los sectores son reales, pero no son datos personales."],
    ["Ninguna captura o foto muestra un expediente físico real.", "Sí", "El visor del prototipo muestra un rectángulo de relleno."],
    ["El prototipo vertical usa una base de datos de prueba, no la de la ASADA.", "Sí", "Abonado de prueba 0412, personas con identificaciones de tomo 0000 y PDF ficticios generados para las pruebas (docs/evidencia/prueba_terminado_CU04.md)."],
    ["Se decidió qué datos se ocultan parcialmente en listas (por ejemplo, la identificación).", "Sí", "La identificación se oculta en las listas (1-••••-0123) y se muestra completa dentro del expediente (guía de estilo, sección 5)."],
    ["El enlace del prototipo es de solo lectura.", "Sí", "GitHub Pages solo permite ver la página; solo los colaboradores que agregue el dueño del repositorio pueden cambiarla."],
]

RF_TRAZ = [
    ["RF-01", "PAN-01, PAN-14", "Usuario y contraseña; «Cambiar mi contraseña»", "P-02"],
    ["RF-02", "PAN-06", "Formulario «Registrar abonado» con número de paja único", "P-02"],
    ["RF-03", "PAN-06, D-06, PAN-04", "Tabla «Personas asociadas» con rol y fechas; diálogo «Agregar persona asociada»", "P-02"],
    ["RF-04", "PAN-09, PAN-07", "Importación en 4 pasos con resumen; grupo «Tipo pendiente»", "P-02"],
    ["RF-05", "PAN-05", "Zona de archivos con validación de PDF o PNG y 10 MB", "P-02, P-03"],
    ["RF-06", "PAN-05, PAN-13", "Fecha del documento propuesta y editable; fecha de carga automática", "P-02, P-03"],
    ["RF-07", "PAN-05, PAN-04, PAN-13", "Opción «nueva versión», columna Versión e historial de versiones", "P-02, P-03"],
    ["RF-08", "PAN-04", "Columna «Prior.» y orden automático por prioridad del tipo", "P-02"],
    ["RF-09", "PAN-10", "Tabla de tipos; prioridad, obligatoriedad, grupos y exigencia a cotitulares", "P-02"],
    ["RF-10", "PAN-03 y barra superior", "Criterios combinados y lista de resultados", "P-02"],
    ["RF-11", "PAN-03 (pestaña Documentos), PAN-04", "Filtros por tipo, nombre identificador y rango de fechas", "P-02"],
    ["RF-12", "PAN-04", "Datos del abonado, titular, personas, documentos ordenados y visor", "P-02"],
    ["RF-13", "PAN-06, D-04, PAN-04", "Diálogo «Cambiar titular»; historial de titulares", "P-02"],
    ["RF-14", "PAN-07, PAN-04", "Tarjetas, lista de faltantes y detalle por persona; aviso en el expediente", "P-02, P-04"],
    ["RF-15", "PAN-11", "Filtros por cuenta, fechas, paja y acción; detalle del valor anterior y el nuevo", "P-02"],
    ["RF-16", "PAN-08, D-05, PAN-02 y barra superior", "«Respaldar ahora», «Restaurar un respaldo…», último respaldo y avisos. El respaldo automático no tiene pantalla: lo dispara el Reloj del sistema.", "P-02"],
    ["RF-17", "PAN-04, D-03", "Botón «Dar de baja» o «Reactivar»", "P-02"],
    ["RF-18", "PAN-12", "Selección de documentos, carpeta de destino o impresión", "P-02"],
    ["RF-19", "PAN-04, D-01", "«Anular» con motivo; casilla «Mostrar anulados»", "P-02"],
    ["RF-20", "PAN-14, PAN-01", "«Generar contraseña temporal»; cambio obligatorio al entrar", "P-02"],
    ["RF-21", "PAN-06", "Modo de modificación del abonado y de sus personas", "P-02"],
    ["RF-22", "PAN-04, D-02", "«Editar datos» (tipo y nombre identificador)", "P-02"],
]
RNF_TRAZ = [
    ["RNF-01", "Pocos pasos (T-01 y T-02 en 3 pantallas), expediente ya elegido en la carga y fecha propuesta.", "T-01 en 1 minuto o menos y T-02 en 3 minutos o menos en la evaluación (8.2). PENDIENTE"],
    ["RNF-02", "Todo en español; cada error con la causa y la acción (guía de estilo).", "Estados de error de PAN-03, PAN-05, PAN-06 y PAN-09 (capturas *_error.png)"],
    ["RNF-03", "No se puede editar la fecha de carga ni sobrescribir; la nueva versión es explícita.", "PAN-05, PAN-13; prueba de terminado 7.1: la fecha original y la versión 1 se conservan al cargar la versión 2"],
    ["RNF-04", "Estado de cada copia verificada y recordatorio de la prueba de restauración.", "PAN-08"],
    ["RNF-05", "Muestra el tiempo de la búsqueda y limita la lista a 50 filas.", "PAN-03; medición en el Incremento 1 (búsqueda). PENDIENTE"],
    ["RNF-06", "Visor integrado con el indicador «máximo 5 s».", "PAN-04 (estado cargando); medición PENDIENTE"],
    ["RNF-07", "Fichas con tabla.columna y clases límite; prototipo de un solo archivo, con scripts.", "Secciones 3 y 6; Anexo A"],
    ["RNF-08", "Diseño para computadora a 1366 × 768 en Windows, sin depender de internet.", "Capturas a 1366 × 768 (resolución SUPUESTA)"],
    ["RNF-09", "Bloqueo de 5 minutos tras 5 intentos, mínimo de 8 caracteres y aviso antes de cerrar la sesión a los 15 minutos.", "PAN-01 (error y bloqueada), PAN-14 (error), D-08"],
    ["RNF-10", "Visor sin descarga; la exportación advierte que los archivos salen sin cifrar.", "PAN-12; prueba de terminado 7.1: el archivo del almacén no se puede leer fuera de SIGEDA"],
    ["RNF-11", "La bitácora no tiene botones para editar ni borrar; la restauración advierte que no la borra.", "PAN-11, D-05"],
    ["RNF-12", "Aviso cuando el último respaldo tiene más de 1 día o quedó pendiente.", "PAN-02 (aviso), PAN-08 (pendiente)"],
    ["RNF-13", "La restauración pide la clave desde una de sus dos copias.", "D-05; registro de la prueba de restauración en PAN-08"],
]

PENDIENTES = [
    ["¿Qué resolución de pantalla tiene la laptop?", "Todas", "Diseñar a 1366 × 768 (SUPUESTO) y de forma adaptable."],
    ["¿La cédula jurídica tiene 9 o 10 dígitos? ¿Hay abonados con DIMEX o pasaporte?", "PAN-06", "10 dígitos (S-02); aceptar DIMEX y pasaporte (Modelo ER, Anexo C, preguntas 6 y 15)."],
    ["¿El número de paja tiene ceros iniciales, letras o guiones? ¿Se reutiliza tras una baja?", "PAN-03, PAN-06", "Texto sin espacios y no reutilizable (Modelo ER, Anexo C, pregunta 1)."],
    ["¿En qué orden van los tipos de documento del 3 al 14?", "PAN-04, PAN-10", "El orden provisional del Modelo ER (3.6.1), ajustable en PAN-10."],
    ["¿Prefiere cargar varios archivos a la vez o uno por uno?", "PAN-05", "Varios a la vez, cada uno con su tipo y su fecha (propuesta del DAS; Anexo B)."],
    ["¿Se entiende «nombre identificador»? ¿Qué palabra usaría?", "PAN-04, PAN-05", "Probarlo en la evaluación; alternativa: «Descripción»."],
    ["¿Se debe anotar quién pidió una exportación (Junta Directiva, ARESEP)?", "PAN-12", "Agregar un campo «Solicitado por» (Anexo B)."],
    ["¿Le parece bien el aspecto de la maqueta (colores y tamaño de letra)?", "Todas", "El tema azul propuesto (P-04)."],
    ["¿Solo la Administración debe poder restaurar un respaldo?", "PAN-08, D-05", "Sí: se pide la contraseña de la Administración (propuesta por validar; excepción a RN-09)."],
    ["¿Los abonados de baja cuentan en el total y en el avance de la digitalización?", "PAN-02, PAN-07", "No: el avance se mide sobre los 1 011 activos y los 4 de baja se muestran aparte."],
    ["¿Quién hace la prueba de restauración cada 3 meses, en qué computadora y dónde se guardan las copias de la clave?", "PAN-08", "La Administración, en una computadora distinta a la laptop; la clave en una copia física y una digital (RNF-13)."],
    ["Riesgo aceptado: si las dos cuentas quedan bloqueadas o se olvidan ambas contraseñas, nadie puede entrar desde la aplicación.", "PAN-01, PAN-14", "No se agrega código de recuperación (decisión del equipo, 04/11/2026). Lo resuelve el soporte técnico en el servidor y queda en la bitácora."],
]

CHECK = [
    ["✓", "P-02 a P-04 con pregunta, tipo, herramienta, tiempo y destino (sección 1). P-01 (bocetos en papel) se omitió por indicación del docente."],
    ["✓", "2 perfiles, 5 factores de entorno y 6 tareas con meta medible; algunas metas y frecuencias están marcadas como SUPUESTO."],
    ["✓", "14 pantallas y 8 diálogos, verificados contra la ERS v1.2 y el UML v1.0 (sección 3)."],
    ["✓", "Los 22 RF aparecen en la sección 10.1; el respaldo automático no tiene pantalla y se explica."],
    ["✓", "La figura 1 se genera del mismo archivo del prototipo, y un script verifica que cada flecha exista como enlace."],
    ["✓", "5 reglas (4.1) y el recorrido de las 6 tareas (4.2)."],
    ["✓", "Sección 5, con contrastes WCAG calculados."],
    ["—", "No aplica: el docente indicó omitir los bocetos en papel."],
    ["✓", "Las 14 pantallas están enlazadas y revisadas con axe-core; publicado en https://kendaltc.github.io/sigeda-prototipo/."],
    ["✓", "Fichas 6.1 a 6.6 completas."],
    ["✓", "Sección 7: CU-04 construido sobre la base de LICS, con la prueba de terminado ejecutada (7 de 7 pasaron) y capturas reales."],
    ["✗", "PENDIENTE: sesión con la administradora (sección 8)."],
    ["✗", "PENDIENTE: depende de la sesión de evaluación."],
    ["✓", "4 «Cumple», 5 «Parcial» y 1 «No» (sección 8.4)."],
    ["✓", "Sección 9."],
    ["✓", "Secciones 10.1 y 10.2."],
    ["✓", "Anexos A, B y C; referencias en APA 7. En el Anexo A, el enlace está pendiente."],
    ["✓", ".docx y PDF de la versión 1.0, .zip con capturas y prototipo, enlace del prototipo navegable, repositorio del prototipo vertical y script DDL (sigeda_v1.1.sql)."],
]

REFS_EXTRA = [
    "Arias Alfaro, M., Arias Rojas, A., Alfaro Arias, S., y Trejos Cubero, K. (2026a). Documento de visión del proyecto SIGEDA (versión 1.1) [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Arias Alfaro, M., Arias Rojas, A., Alfaro Arias, S., y Trejos Cubero, K. (2026b). Especificación de requerimientos de software del SIGEDA (versión 1.2) [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Arias Alfaro, M., Arias Rojas, A., Alfaro Arias, S., y Trejos Cubero, K. (2026c). Modelos UML del SIGEDA (versión 1.0) [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Arias Alfaro, M., Arias Rojas, A., Alfaro Arias, S., y Trejos Cubero, K. (2026d). Documento de arquitectura de software del SIGEDA (versión 1.1) [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Arias Alfaro, M., Arias Rojas, A., Alfaro Arias, S., y Trejos Cubero, K. (2026e). Modelo entidad-relación y relacional del SIGEDA (versión 1.1) [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Arias Rojas, A. (s.f.). laboratorio-inyeccion-castro-solis (versión 2.5.0) [Software]. GitHub. https://github.com/aleariasr/laboratorio-inyeccion-castro-solis",
    "Mcintosh Molina, J. (2026a). Retroalimentación: Documento de Arquitectura SIGEDA, versión 1.1 [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
    "Mcintosh Molina, J. (2026b). Revisión del prototipo SIGEDA: hallazgos y recomendaciones [Documento no publicado]. Universidad de Costa Rica, Sede de Occidente.",
]

ANEXO_A = [
    [ENLACE, "Prototipo navegable (enlace de solo lectura)", "HTML"],
    ["Capturas_y_Bocetos_SIGEDA.zip › prototipo/index.html", "Copia sin conexión del prototipo navegable (abre con doble clic)", "HTML"],
    ["Capturas_y_Bocetos_SIGEDA.zip › capturas/", "Capturas de wireframes: 14 pantallas con sus estados, 8 diálogos y 4 de alta fidelidad (77 PNG)", "PNG"],
    ["Capturas_y_Bocetos_SIGEDA.zip › mapa_navegacion/", "Mapa de navegación: versión del documento (Figura 1) y versión detallada con cada flecha del menú lateral; ambas se generan desde pantallas.json", "Graphviz DOT, SVG y PNG"],
    ["Capturas_y_Bocetos_SIGEDA.zip › herramientas/", "Scripts que generan las capturas (capturar.js, Playwright), el mapa (mapa.py y mapa_doc.py) y la revisión de accesibilidad (axe.js, axe-core)", "JavaScript, Python"],
    ["Capturas_y_Bocetos_SIGEDA.zip › prototipo_vertical/sigeda_v1.1.sql", "Script DDL del Modelo ER v1.1 (14 tablas), generado con pg_dump desde la base migrada", "SQL (PostgreSQL 17)"],
    ["Capturas_y_Bocetos_SIGEDA.zip › prototipo_vertical/", "Capturas reales del prototipo vertical y resultado de la prueba de terminado", "PNG, Markdown"],
    ["https://github.com/KendalTC/SIGEDA", "Código del prototipo vertical (CU-04) sobre la base de LICS; evidencia en docs/evidencia/", "Python, TypeScript"],
]

ANEXO_B = [
    ["Modelos UML v1.0 y Documento de Arquitectura v1.1", "Componentes (IDocumentos) y clases de control", "ControladorDocumentos cumple el papel de la fachada IDocumentos (no hay una clase aparte) y las operaciones se escriben en snake_case de Python (validar_archivo, cargar_documento, cargar_nueva_version). Documentar el formato del archivo cifrado: nonce de 12 bytes + contenido + etiqueta de 16 bytes.", "Prototipo vertical (sección 7.2)."],
    ["Modelos UML v1.0", "2.1 Clases candidatas", "Indicar que PAN-02 es un marco de navegación sin clase límite y que PantallaExpediente tiene un modo de consulta (PAN-04) y uno de edición (PAN-06).", "Inventario de pantallas (sección 3)."],
    ["Documento de Arquitectura v1.1", "0.3 Relación con artefactos previos", "Citar los Modelos UML v1.0: la v1.1 todavía no existe (Modelo ER v1.1, Anexo B, fila 18).", "Sección 0.3."],
    ["ERS v1.2", "RF-05 y CU-04", "Permitir elegir varios archivos y cargarlos en una operación, cada uno con su tipo y su fecha (propuesta del Anexo B del DAS).", "PAN-05; riesgo RT-10 (unos 6 090 documentos por digitalizar)."],
    ["ERS v1.2", "RF-05 y S-21", "Dejar claro que el límite de 10 MB es de RF-05 y S-21. La plantilla de prototipos lo atribuye a RNF-06, que es el tiempo de visualización.", "Ficha 6.3."],
    ["ERS v1.2", "RF-03, RF-13 y glosario", "Reemplazar el rol «titular anterior» por un vínculo TITULAR cerrado (vinculo_abonado.fecha_fin con valor). Roles: TITULAR, COTITULAR y APODERADA.", "Modelo ER v1.1; PAN-04 y PAN-06."],
    ["ERS v1.2", "RF-15", "Listar las 12 acciones de la bitácora del Modelo ER v1.1, incluidas RESTABLECIMIENTO_CONTRASENA y CUARENTENA.", "PAN-11 (filtro de acciones)."],
    ["ERS v1.2", "3.4 Interfaces de usuario", "Agregar a la lista de pantallas: importación, exportación y gestión de cuenta.", "Inventario de pantallas."],
    ["Documento de Visión v1.1", "3.3 y 5", "Cambiar «internet inestable» por «estable» (B-03), como ya hace el DAS.", "Entorno de uso (2.2)."],
    ["Modelo ER v1.1", "persona, consulta Q11 y reglas de importación (2.7)", "Quitar persona.id_persona_fusionada_en, la consulta Q11 y la fusión; se anotan como mejora futura. Se conserva el índice único parcial (tipo_identificacion, identificacion). Regla nueva: la importación de SADA crea una persona por abonado y el duplicado se detecta al completar la cédula en PAN-06 («Ya existe una persona con esa cédula», con la opción de usarla).", "Decisión del equipo del 04/11/2026; PAN-06, estado «persona-existente»."],
    ["Modelo ER v1.1", "Tablas de respaldo", "Agregar dónde registrar la prueba de restauración (SUPUESTO: tabla prueba_restauracion con fecha, id_respaldo, computadora, resultado y observaciones).", "PAN-08, estado «prueba»; RNF-04 y DAS 8.2."],
    ["Modelo ER v1.1 y ERS v1.2", "cuenta.perfil y RN-09", "La interfaz llama a las cuentas «Secretaría» y «Administración» (usuarios secretaria y administracion); cuenta.perfil puede conservar SECRETARIA y ADMINISTRADORA. Propuesta por validar: excepción a RN-09 para que restaurar requiera la Administración.", "Revisión del docente (Mcintosh Molina, 2026b); D-05."],
    ["Documento de Arquitectura v1.1", "7.2 Tecnología y 8 Despliegue", "Registrar la decisión del 04/11/2026: construir sobre la base de LICS v2.5.0. Faltantes por cubrir: respaldar también los documentos y cifrar el paquete, restaurar sin borrar la bitácora y desde la aplicación, bloqueo tras intentos fallidos y cierre por inactividad, y cambiar el nombre «lics» en infra, scripts y flujos de GitHub.", "Sección 7; análisis del código de LICS."],
    ["Modelo ER v1.1", "registro_bitacora (EXPORTACION)", "Evaluar guardar quién solicitó la exportación (Junta Directiva o entidad con facultad legal).", "PAN-12; pendiente 7 de la sección 11."],
    ["Plantilla de prototipos", "Sección 3", "Se usan los nombres de clase del UML v1.0: PantallaBusquedaExpedientes, PantallaCargaDocumento y PantallaCompletitud.", "Pregunta de control (sección 3)."],
]

GUION_EXTRA = "Al terminar las tareas, mostrar la maqueta de alta fidelidad (P-04) aclarando: «Así podría verse; todavía no funciona». Preguntar qué le parecen los colores y el tamaño de la letra."
GUION_TAREAS = "Antes de empezar: abrir el prototipo en PAN-01 a 1366 × 768, con el «Panel del prototipo» cerrado. Tareas, en orden: T-01 a T-06 (sección 2.3). Anotar en la tabla 8.2 si la completó sin ayuda, el tiempo, dónde dudó y sus palabras exactas."
