# Prompt: Prototipos de Interfaz de Usuario de SIGEDA (IF6100)

> Copiá todo este archivo como primer mensaje del chat nuevo, con la carpeta `1.ProyectoAcueducto` conectada.

---

## 1. Quién soy y qué necesito

Soy Kendal Trejos Cubero, estudiante de IF6100 Análisis y Diseño de Sistemas (UCR, Sede de Occidente, Recinto de Grecia, Grupo 02, II Ciclo 2026). El docente es el Mag. James Mcintosh Molina.

Mi equipo y yo diseñamos **SIGEDA (Sistema de Gestión Documental del Acueducto)** para la ASADA **Acueducto Bodegas y Pilas**. El sistema digitaliza, organiza y permite consultar los expedientes en papel de sus 1 015 abonados.

**Equipo:**
- Mariangel Arias Alfaro (C4C688)
- Alejandro Arias Rojas (C4C759)
- Sebastián Alfaro Arias (C4C212)
- Kendal Trejos Cubero (C4K374)

**El entregable de ahora** es el de prototipos. Hay que llenar **toda** la plantilla `Enunciados/Plantilla_Prototipos_Interfaz_SIGEDA.docx` y producir lo que pide:

1. El documento en .docx y en PDF.
2. Un prototipo navegable con enlace de solo lectura, o el archivo exportado si la herramienta no permite compartir.
3. Un .zip con las fotos de los bocetos y las capturas PNG de las pantallas.

**Quiero automatizar lo más posible para no hacer mucho trabajo manual.** Pero hay cosas que, por su naturaleza, tienen que ser reales y no se pueden inventar. Están en la sección 6.

Tenés acceso a la carpeta del proyecto. En la sección 3 te explico qué contiene cada archivo, para que lo revisés como contexto.

---

## 2. Reglas de trabajo (importantes)

1. **No inventés información.**
   - Todo dato sale de los entregables de la carpeta o del Proyecto de Claude «Analisis y Diseño de Sistemas», si tenés acceso a él.
   - Si algo no está y es razonable proponerlo, proponelo y **marcalo como SUPUESTO**, en el documento y en tu mensaje.
   - Si algo no está claro o hay que decidirlo, **preguntame antes de seguir**.
2. **Antes de construir nada, analizá y preguntá.**
   - El primer mensaje que me mandés es el análisis de la sección 7. Esperá mi respuesta.
3. **Trabajá por fases con puntos de revisión.** Mostrame cada fase terminada antes de pasar a la siguiente (sección 8).
4. **Nombres de datos:** usá los nombres de tabla y columna del **Modelo ER/Relacional v1.1** (`tabla.columna`). Cuando dos documentos se contradigan, la prioridad es esta:
   1. Modelo ER/Relacional v1.1, para datos y reglas de integridad.
   2. Documento de Arquitectura, para la arquitectura.
   3. Modelos UML v1.0, para casos de uso y clases límite.
   4. ERS v1.2, para requerimientos y reglas de negocio.
   - Toda diferencia que encontrés va al **Anexo B** de la plantilla.
5. **Solo datos ficticios** en prototipos y capturas: nombres, cédulas y números de paja (Ley 8968, sección 10 de la plantilla). Nunca usés datos reales de abonados.
6. **Español de Costa Rica, claro y directo.** Sin relleno. La plantilla tiene texto gris de instrucciones y recuadros ámbar de ejemplo (lecturas de medidor): **ambos se eliminan** en la versión final, igual que todo `[COMPLETAR]`.
7. **No modifiqués los archivos originales** de la carpeta. Trabajá sobre copias.
   - Guardá todo lo nuevo en `Entregables/Prototipos/`, o en la carpeta que te diga.
   - La carpeta es un repositorio Git: no hagás commits salvo que te lo pida.
8. Las referencias van en APA 7, como pide la plantilla.

---

## 3. Mapa de la carpeta `1.ProyectoAcueducto`

### 3.1 Raíz

| Archivo | Qué contiene | Uso para los prototipos |
|---|---|---|
| `Contexto_Completo_Proyecto_SIGEDA.md` | Resumen del proyecto hasta el 01/10/2026: datos del curso y del equipo, entrevista del 28/08, revisión de la Visión, reunión de validación del 21/09 (respuestas B-01 a B-23), evolución de la ERS y entrega UML. | **Leelo primero.** Da el contexto del negocio. Es anterior al DAS y al Modelo ER. |
| `ENTREVISTA 21 SEPTIEMBRE.docx` | Notas de la reunión de validación con la administradora del 21/09/2026. | Palabras reales de la usuaria (heurística 2 de Nielsen), tareas reales y preocupaciones. |
| `Guia_Reunion_Administradora_21set2026_1.docx` | Guía de preguntas para esa reunión. | Contexto de qué se validó. |
| `Retroalimentacion_Documento_Arquitectura_SIGEDA.docx` | Revisión del docente del DAS v1.1 (29/10/2026): correcciones P1, P2 y P3. | Decisiones de arquitectura que afectan la interfaz: capa de presentación, Facade de búsqueda, bitácora, respaldo. |
| `Revision_Modelo_ER_Relacional_SIGEDA.pdf` | **Se movió** a `Entregables/Modelo entidad relacion/` (sección 3.3). | — |
| `README.md`, `.gitignore` | Archivos del repositorio. | No aplica. |

### 3.2 `Entregables/`: lo que el equipo ya entregó

| Archivo | Qué contiene | Uso para los prototipos |
|---|---|---|
| `Vision_Proyecto.docx` | Documento de Visión v1.0 (fecha 9/1/2026; se cita como v1.1 en documentos posteriores; confirmá la versión conmigo). Incluye: problema, interesados, **perfiles de usuaria** (3.2), **entorno** (3.3: oficina, una sola laptop, internet inestable, respaldo en discos externos), necesidades N-01 a N-05, capacidades, **restricciones** (5) y rangos de calidad. | Secciones 2.1 y 2.2 de la plantilla (perfiles y entorno). |
| `ERS_Acueducto_Bodegas_Pilas_v1.2.docx` / `.pdf` | **ERS v1.2, la vigente.** Contiene: RF-01 a RF-22 (tabla 3.1), RNF-01 a RNF-13 (3.2), reglas RN-01 a RN-12 (3.3), actores y CU-01 a CU-17 (4), matriz de trazabilidad (5), criterios de validación (6), anexos. | **Fuente principal** de qué hace cada pantalla, validaciones, metas medibles y trazabilidad (secciones 3, 7, 11). |
| `ERS_Acueducto_Bodegas_Pilas_V1.1.docx` | ERS anterior. | Solo para historial. **No usar** como fuente. |
| `Cambios_ERS_v1.2_SIGEDA.pdf` | Cambios de la v1.1 a la v1.2 según la revisión del docente. | Contexto de por qué existen RF-19 a RF-22. |
| `Modelos_UML_Acueducto_Bodegas_Pilas.docx` / `.pdf` | **Modelos UML v1.0 (02/10/2026), la versión entregada.** Contiene: actores (1.1), diagrama de CU con CU-18 (1.2), especificación de CU-02, **CU-04** y CU-07 (1.3), **clases candidatas con estereotipo** (2.1), diagrama de clases (2.2), atributos y operaciones (2.3), secuencia de CU-04 (3), componentes (4), trazabilidad (6) y Anexo A de diferencias con la ERS. | Clases límite: **cada una es una pantalla** (inventario, sección 3). Flujos de CU-04 para PAN-05. |
| `Plantilla_Modelos_UML_Acueducto_Pilas_Bodegas.docx` | Borrador anterior de los Modelos UML. | **No usar**: lo reemplaza el archivo anterior. |
| `Diagrama_Casos_de_Uso_SIGEDA.png`, `Diagrama_Clases_SIGEDA.png` | Imágenes sueltas de borradores de los diagramas. | Solo referencia visual. Los diagramas finales están dentro del .docx de UML. |
| `UML/` | Imágenes y tablas sueltas del borrador UML: `Diagrama_Clases_SIGEDA_v2.png`, `Diagrama_Componentes_Sigeda.png`, `Diagrama_Secuencia_Sigeda.png` y las tablas 2.1, 2.3, 3.3 (interacción de CU-04), 4.1 y 6. | Útil si necesitás una tabla en formato editable. En caso de diferencia, manda el .docx final. |

### 3.3 `Entregables/Modelo entidad relacion/`

| Archivo | Qué contiene | Uso para los prototipos |
|---|---|---|
| `Modelo_Relacional_SIGEDA_v1.1_Contexto.md` | **Resumen del modelo de datos vigente:** las 14 tablas con columnas, dominios CHECK, reglas que programa la aplicación, volúmenes y pendientes. | **Leelo primero, junto con el contexto de la raíz.** Es la fuente de `tabla.columna` para las fichas de la sección 7. |
| `Modelo_ER_Relacional_SIGEDA_v1.1.docx` / `.pdf` | Modelo ER y Relacional v1.1 (03/11/2026), que atiende las 19 observaciones del docente. Secciones clave: diccionario de datos (3.4), reglas y responsables (2.7), consultas Q1 a Q11 (5), Anexo B (cambios pendientes en otros artefactos), Anexo C (preguntas a la administradora). | Validaciones de cada campo, estados, orden del expediente (RN-05) y datos personales (4.2). |
| `Modelo_ER_Relacional_SIGEDA.pdf` | Versión 1.0 entregada (29/10/2026). | Solo historial. |
| `Revision_Modelo_ER_Relacional_SIGEDA.pdf` | Revisión del docente de la v1.0 (02/11/2026). | Muestra el nivel de detalle que espera el docente. |
| `Fuentes_Diagramas_ER_SIGEDA_v1.1.zip` | Fuentes Graphviz (.dot, .svg, .png) de las figuras del modelo y el script `figs.py`. | Ejemplo de diagramas generados por código. Sirve de idea para el mapa de navegación. |

### 3.4 `Enunciados/`: plantillas del docente

| Archivo | Qué es |
|---|---|
| **`Plantilla_Prototipos_Interfaz_SIGEDA.docx`** | **La plantilla que hay que llenar** (sección 4 de este prompt). |
| `Plantilla_Modelo_ER_Relacional_SIGEDA.docx`, `Plantilla_Documento_Arquitectura_SIGEDA.docx`, `Plantilla_Modelos_UML_Acueducto_Pilas_Bodegas.docx`, `ERS_Plantilla_Acueducto_Pilas_Bodegas.docx` | Plantillas de entregables anteriores. Sirven de referencia de formato. |

### 3.5 `Documentacion/`

| Archivo | Qué contiene |
|---|---|
| `ENTREVISTA.md` | Notas de la entrevista inicial con la administradora: estructura, procesos, archivo físico y necesidades. |
| `Preguntas_ERS_Reunion_Administradora.md` | Preguntas preparadas para la reunión de validación de la ERS. |
| `Documentos_Proyecto_ASADA/` | Guías del curso para la propuesta inicial y `Propuesta_Proyecto_ASADA.docx`. Contexto general; poca relevancia para este entregable. |

### 3.6 Lo que NO está en la carpeta

Si tenés acceso al Proyecto de Claude, revisá ahí estos documentos. Si no, pedímelos.

- **Documento de Arquitectura (DAS):** el equipo entregó la v1.1 (27/10/2026) y el archivo no está en la carpeta. Si tenés el Proyecto, `claude/Documento_Arquitectura_SIGEDA.md` resume las decisiones de la v1.0. Lo esencial para prototipos:
  - **Stack propuesto:** Electron (app de escritorio) + Next.js/React (interfaz) + Django/DRF (API) + PostgreSQL 17, todo local en la laptop (Windows 10/11 de 64 bits, Docker en WSL2), sin servidor.
  - **Arquitectura:** capas límite, control y entidad (BCE) y patrón Facade para la búsqueda.
  - **Escenarios de calidad:** búsqueda en 3 s o menos; documento visible en 5 s o menos.
  - **Seguridad y respaldo:** archivos cifrados con AES-256; respaldo diario a disco externo (OneDrive opcional).
- **DFD de la Semana 9:** almacenes D1 Abonados, D2 Documentos, D3 Bitácora de respaldos. El Modelo ER propone agregar D4 Cuentas y D5 Bitácora.
- **Retroalimentación de los Modelos UML** (07/10/2026).
- **Plan del Incremento 1** (Semana 12, en clase). Lo resumo en la sección 5.3.
- En el Proyecto también están `claude/Modelo_Relacional_SIGEDA_v1.1_Contexto.md` (igual al de la carpeta) y `claude/Contexto_SIGEDA_Modelo_Relacional.md`, que incluye la transcripción de la retroalimentación del DAS.

---

## 4. La plantilla `Plantilla_Prototipos_Interfaz_SIGEDA.docx`

Leela completa. Esta es la estructura y lo que exige cada sección:

| Sección | Qué pide | Observaciones para SIGEDA |
|---|---|---|
| Portada | Integrantes, herramienta de prototipado con enlace de solo lectura, versión y fecha (la fija el profesor). | La plantilla dice «Acueducto de **Pilas y Bodegas**». En todos los entregables usamos «Acueducto **Bodegas y Pilas**»: **preguntame cuál dejar.** |
| 0 Introducción | Propósito; alcance con los cuatro niveles; relación con artefactos (versión de cada insumo); definiciones. | Los cuatro niveles son: bocetos en papel, navegable, vertical del Incremento 1 y alta fidelidad (este último opcional). La plantilla pide «Modelos UML v1.1», pero **esa versión no existe**: usamos la v1.0 (Anexo B, fila 18 del Modelo ER). |
| 1 Objetivos | P-01 a P-04: pregunta, tipo, herramienta, tiempo máximo y destino final. | — |
| 2 Usuarias y contexto | 2.1 perfiles de administradora y secretaria; 2.2 entorno; 2.3 de 5 a 8 tareas con meta medible. | Las metas pueden salir de RNF-01: buscar un expediente en 1 minuto o menos y cargar un documento en 3 minutos o menos, tras una inducción de 30 minutos. También de RNF-05 (búsqueda en 3 s o menos) y RNF-06 (visualización en 5 s o menos). |
| 3 Inventario | PAN-01 a PAN-12 con clase límite, CU, RF, actor e incremento, más la pregunta de control. | Ver «Discrepancias», sección 5.2. |
| 4 Mapa de navegación | Figura más 4.1 reglas y 4.2 recorrido de tareas. | Puede generarse con Mermaid, Graphviz o la herramienta elegida. |
| 5 Guía de estilo | Colores (contraste WCAG 4.5:1), tipografía, botones, fecha dd/mm/aaaa, número de paja, identificaciones, mensajes de error (qué pasó + qué hacer), confirmaciones y términos. | RNF-02: todo en español, y cada error indica causa y acción. |
| 6 Bocetos | Fotos de bocetos a mano de PAN-03, PAN-04 y PAN-07, **con dos alternativas para al menos una**, más tres preguntas por boceto. | **Los dibujamos nosotros** (sección 6). |
| 7 Navegable | Wireframes grises de **todas** las pantallas, enlazados. Seis fichas completas: 7.1 PAN-03, 7.2 PAN-04, 7.3 PAN-05, 7.4 PAN-06, 7.5 PAN-07, 7.6 PAN-08. Cada ficha lleva captura, elementos con `tabla.columna`, acciones, estados, preguntas de diseño y trazabilidad. 7.7 lleva el resto de pantallas y 7.8 la alta fidelidad (opcional). | **La parte más pesada; automatizala.** |
| 8 Vertical (Incremento 1) | Plan del Incremento 1 actualizado con lo construido, capturas funcionando, prueba de terminado y aprendizajes. | Ver sección 5.3. |
| 9 Evaluación | Plan de sesión, resultados por tarea, hallazgos con severidad de Nielsen y autoevaluación con las 10 heurísticas. | **Los resultados tienen que ser reales** (sección 6). |
| 10 Datos personales | Lista de verificación de Ley 8968. | — |
| 11 Trazabilidad | RF → pantalla y RNF → evidencia. | Los 22 RF tienen que aparecer. |
| 12 Pendientes | Preguntas para la administradora. | Pueden reutilizar las del Anexo C del Modelo ER. |
| 13 Lista de verificación | 18 criterios: **es la misma lista que usa el docente para revisar.** | — |
| 14 Referencias y Anexos A, B y C | Archivos y enlaces; cambios a artefactos anteriores; guion de evaluación. | — |

---

## 5. Datos clave que ya revisé (verificalos vos también)

### 5.1 Clases límite del UML v1.0 (las pantallas)

| Clase límite | Casos de uso | Qué muestra o captura |
|---|---|---|
| PantallaInicioSesion | CU-01 | Usuario y contraseña; bloqueo tras 5 intentos. |
| PantallaGestionCuenta | CU-01, CU-16 | Cambio de contraseña propia y contraseña temporal para la otra usuaria. |
| PantallaBusquedaExpedientes | CU-05 | Criterios de búsqueda y resultados. |
| PantallaExpediente | CU-06, CU-02, CU-07, CU-12, CU-15, CU-18 | Datos del abonado, titular, personas y documentos; punto de entrada de muchas acciones. |
| PantallaCargaDocumento | CU-04, CU-14, CU-17 | Carga; también anular y editar datos de un documento. |
| PantallaHistorialVersiones | CU-04, CU-06 | Versiones de un documento. |
| PantallaCompletitud | CU-08 | Panel de completitud. |
| PantallaTiposDocumento | CU-09 | Tipos de documento y grupos de alternativas. |
| PantallaBitacora | CU-10 | Registros de la bitácora. |
| PantallaRespaldos | CU-11 | Último respaldo y avisos. |
| PantallaImportacion | CU-03 | Importación de SADA. |
| PantallaExportacion | CU-13 | Selección de documentos para exportar. |

Los controladores son: ControladorAutenticacion, ControladorAbonados, ControladorImportacion, ControladorDocumentos, ControladorBusqueda, ControladorCompletitud, ControladorTiposDocumento, ControladorBitacora, ControladorRespaldos y ControladorExportacion.

### 5.2 Discrepancias que tenés que resolver o consultarme

1. **Nombres de clase en la plantilla:** la plantilla sugiere «PantallaBusqueda», «PantallaCarga» y «PanelCompletitud» (dice que son pistas para verificar). Los nombres reales son **PantallaBusquedaExpedientes, PantallaCargaDocumento y PantallaCompletitud**.
2. **Pantallas que faltan en el inventario de la plantilla:**
   - **PantallaGestionCuenta** (CU-01, CU-16, RF-01, RF-20).
   - **PantallaHistorialVersiones** (RF-07).
   - **PAN-02 Menú principal** no tiene clase límite en el UML: se explica en la pregunta de control.
   - Decidí con argumentos si anular (CU-14) y editar datos de documento (CU-17) son pantallas o diálogos aparte.
3. **Casos de uso:** la ERS v1.2 tiene CU-01 a CU-17. El UML agregó **CU-18 Registrar personas asociadas** («include» de CU-02, CU-07 y CU-15).
4. **Roles de persona:**
   - La ERS (RF-03, RF-13) usa el rol «titular anterior».
   - El **Modelo ER v1.1** lo cambió: los roles son **TITULAR, COTITULAR y APODERADA**, y el titular anterior es un **vínculo cerrado** (`vinculo_abonado.fecha_fin` con valor).
   - Las pantallas siguen el Modelo ER: el historial de titulares se muestra con fechas.
5. **Cambios del Modelo ER v1.1 que impactan la interfaz:**
   - **Identificaciones:** CEDULA_FISICA, CEDULA_JURIDICA, **DIMEX, PASAPORTE**. La plantilla ya pregunta por esto en PAN-06.
   - **Fusión de personas duplicadas:** consulta Q11 de posibles duplicados por nombre tras importar SADA, más fusión con `persona.id_persona_fusionada_en`. Decidí si es una pantalla nueva o parte de PAN-06.
   - **Anulación:** queda en la bitácora con 3 campos (estado, motivo y fecha).
   - **Orden del expediente:** prioridad del tipo, luego nombre del tipo, luego `id_documento`.
   - **Respaldo:** estado COMPLETO si y solo si hay una copia VERIFICADA. Hay como máximo 2 copias: DISCO_EXTERNO y ONEDRIVE.
   - **Abonado importado:** tiene `tipo_abonado = PENDIENTE` y no tiene sector.
6. **Tamaño máximo:** la plantilla dice «10 MB, RNF-06». En la ERS, el límite de 10 MB está en **RF-05 / S-21**. **RNF-06** es el tiempo de visualización (5 s o menos).
7. **Seguridad (RNF-09):** contraseña de mínimo 8 caracteres; bloqueo de 5 minutos tras 5 intentos; sesión cerrada tras 15 minutos de inactividad. Afecta PAN-01 y los estados especiales.
8. **Equipo (RNF-08):** Windows 10/11 de 64 bits, sin servidor. **No conocemos la resolución de pantalla de la laptop**: marcalo como SUPUESTO o preguntame.
9. **Stack del Incremento 1:**
   - El DAS propone Electron + Next.js + Django + PostgreSQL 17, y el docente aprobó PostgreSQL 17.
   - En una actividad de clase, los contratos entre parejas se escribieron con **Java + MySQL** y una tabla `expediente`.
   - **Preguntame qué se usó realmente** antes de llenar la sección 8.

### 5.3 Plan del Incremento 1 (Semana 12, Sala 2: Mariangel y Kendal)

Base para la sección 8:

- **Rebanada:** CU-04 Cargar documento PDF. **Versión:** 0.1.0.
- **Tablas, en orden de llaves foráneas:**
  1. abonado
  2. persona
  3. vinculo_abonado
  4. grupo_alternativas
  5. tipo_documento
  6. documento
  7. version_documento
  8. cuenta
  9. registro_bitacora
- **Control:** `ControladorDocumentos.cargarDocumento`, `cargarNuevaVersion` y `validarArchivo`; se crea VersionDocumento; `agregarVersion`; `Abonado.agregarDocumento`; `ControladorBitacora.registrar`.
- **Pantalla:** PantallaCargaDocumento (prototipo evolutivo vertical de fidelidad media).
- **Prueba de terminado planeada:**
  - 5 de 5 cargas conservan `fecha_documento` 15/03/2005 intacta y su SHA-256 coincide.
  - 0 archivos legibles fuera de SIGEDA.
  - 2 rechazos (formato y tamaño) dejan 0 filas creadas.
  - La versión 2 conserva la fecha de 2005.
  - Cada carga deja 1 fila en la bitácora.
- **Riesgo principal:** perder la fecha original del documento. Se mitiga con dos columnas separadas, `fecha_documento` y `fecha_carga`.
- **Reparto propuesto:** Kendal hace DDL, entidades y repositorios; Mariangel hace controladores, pantalla y datos de prueba.
- **La otra pareja** (Sebastián y Alejandro) hace Buscar expediente (RF-10).
- **El Avance de Construcción es el 06/11/2026.**
- **Lo que realmente se construyó** (repositorio, capturas, resultados) **te lo paso yo**. No lo supongás.

---

## 6. Lo que NO se puede automatizar ni inventar

Preparás todo lo que facilite estas partes, pero **no fabriqués resultados**:

1. **Bocetos en papel (sección 6).** Tienen que ser fotos de bocetos a mano.
   - Vos me das una guía de qué dibujar en cada pantalla, incluidas las dos alternativas de una de ellas. Si sirve, también hojas imprimibles con el marco de la pantalla.
   - Yo te paso las fotos y vos las insertás y redactás las respuestas que te dicte.
2. **Evaluación con usuarias (sección 9).** Los tiempos, los errores, los comentarios textuales y los hallazgos salen de una sesión real con la administradora o la secretaria. Si no se puede, se hace con una persona ajena que hace el papel, y así se declara.
   - Vos preparás el kit: guion del Anexo C adaptado, tareas, una hoja de registro imprimible o un formulario y el plan 9.1.
   - Mientras no haya sesión, esas celdas quedan marcadas como pendientes, nunca llenas con datos supuestos.
   - Las heurísticas (9.4) sí podés autoevaluarlas, pero de forma creíble y sin marcar «Cumple» en todo.
3. **Prototipo vertical (sección 8).** Capturas y resultados de lo que el equipo construyó de verdad.

---

## 7. Tu primera respuesta: análisis y propuestas (esperá mi decisión)

Antes de construir, mandame:

### 7.1 Resumen de lo que entendiste

En pocas líneas: qué se entrega, qué fuentes vas a usar y qué falta.

### 7.2 Opciones de herramienta para el prototipo navegable

**Analizá entre 4 y 6 opciones** y presentámelas en una tabla comparativa. Mi idea inicial es **HTML**, pero no sé si funciona para lo que pide el docente: decime con honestidad si conviene.

**Criterios para comparar** (salen de la plantilla):
1. Cuánto trabajo manual me ahorra. Prioridad: automatización hecha por vos.
2. Si cumple «wireframes en gris, fidelidad media, todas las pantallas enlazadas y navegables con clics».
3. Si da un **enlace de solo lectura** compartible con el docente, o un archivo exportable aceptable.
4. Si se pueden generar **capturas PNG** de cada pantalla de forma automática (por ejemplo, Playwright sobre HTML).
5. Si el **mapa de navegación** (sección 4) se puede generar desde la misma fuente.
6. Costo: gratis o con licencia de estudiante.
7. Curva de aprendizaje para el equipo y facilidad para hacer cambios después de la evaluación (sección 9.3).
8. Qué tan bien se ve como entregable académico y si el docente lo acepta. La plantilla menciona Figma, Penpot, draw.io y PowerPoint como ejemplos.
9. Si sirve de puente hacia la implementación real (Next.js/React del DAS) sin confundir lo desechable con lo evolutivo.

**Opciones mínimas por evaluar:**
- HTML/CSS/JS de un solo archivo o varios archivos, generado por vos y publicado en GitHub Pages, Netlify o un enlace de artifact de Claude si está disponible.
- Figma, a mano o con algún flujo automatizable.
- Penpot.
- draw.io (diagrams.net) con páginas enlazadas.
- PowerPoint o Google Slides con hipervínculos.
- Cualquier otra que consideres mejor; por ejemplo, un tipo de artefacto de diseño de Claude si tu entorno lo ofrece.

Para cada opción decime cómo se cubre la **maqueta de alta fidelidad opcional (7.8)** y si recomendás hacerla.

**Cerrá con tu recomendación** y por qué. Esperá que yo elija.

### 7.3 Preguntas

Las que necesités, numeradas y cortas. Incluí al menos:
- El nombre del acueducto en la portada (5.2 y sección 4).
- La versión de la Visión.
- El stack real del Incremento 1.
- La resolución de la laptop, si no la encontrás.
- Si se hace la maqueta de alta fidelidad opcional.

---

## 8. Plan de trabajo después de mi elección (por fases, con revisión)

1. **Fase A: diseño de la interfaz (secciones 0 a 5).**
   - Objetivos P-01 a P-04, perfiles, entorno y tareas T-01 a T-0x con meta medible.
   - Inventario completo con pregunta de control, mapa de navegación con sus reglas y recorridos, y guía de estilo.
   - → Me lo mostrás.
2. **Fase B: kit de bocetos (sección 6).** Guía de qué dibujar y hojas imprimibles. → Yo dibujo y te paso fotos.
3. **Fase C: prototipo navegable (sección 7).**
   - Todas las pantallas con datos ficticios, enlazadas, en gris.
   - Capturas PNG automáticas.
   - Seis fichas completas, con `tabla.columna` del Modelo ER v1.1, acciones, estados, preguntas de diseño respondidas y trazabilidad.
   - 7.7 con el resto de pantallas.
   - → Me lo mostrás con el enlace.
4. **Fase D: kit de evaluación (sección 9 y Anexo C)** y autoevaluación heurística. → Yo hago la sesión y te paso los resultados.
5. **Fase E: llenar la plantilla.**
   - Edición directa del .docx de la plantilla, conservando su formato y estilos: se borra el texto gris y los ejemplos ámbar, se actualiza la tabla de contenido y no queda ningún `[COMPLETAR]`.
   - Secciones 8, 10, 11, 12, 13, referencias y anexos.
   - Exportar a PDF y armar el .zip de capturas y fotos.
6. **Fase F: verificación final.**
   - Revisá la lista de la sección 13 de la plantilla punto por punto, porque es la que usa el docente.
   - Confirmá que los 22 RF aparecen en la sección 11.1.
   - Confirmá que los nombres coinciden con el Modelo ER v1.1.
   - Revisá visualmente el PDF.
   - Reportame lo que quedó pendiente.

**Estructura sugerida de salida en `Entregables/Prototipos/`:**
- `Prototipos_Interfaz_SIGEDA_v1.0.docx` y `.pdf`
- `prototipo/`: fuente del navegable.
- `capturas/`: PNG por pantalla.
- `bocetos/`: fotos.
- `mapa_navegacion/`: fuente y PNG.
- `Capturas_y_Bocetos_SIGEDA.zip`

---

**Empezá leyendo** estos archivos, en este orden:
1. `Contexto_Completo_Proyecto_SIGEDA.md`
2. `Entregables/Modelo entidad relacion/Modelo_Relacional_SIGEDA_v1.1_Contexto.md`
3. La plantilla
4. La ERS v1.2
5. Los Modelos UML v1.0
6. La Visión
7. La retroalimentación del DAS

Después mandame el análisis de la sección 7.
