# SIGEDA: contexto del proyecto para Claude Code

> Este archivo va en la raíz del repositorio de SIGEDA. Claude Code lo lee al iniciar cada sesión.
> Si algo de aquí choca con un documento entregado, manda el documento: avisale a Kendal y anotá la diferencia.

## 1. Quiénes somos y qué estamos haciendo

- **Curso:** IF6100 Análisis y Diseño de Sistemas, Universidad de Costa Rica, Sede de Occidente (Recinto de Grecia), Grupo 02, II Ciclo 2026.
- **Docente:** Mag. James Mcintosh Molina.
- **Equipo:** Mariangel Arias Alfaro (C4C688), Alejandro Arias Rojas (C4C759), Sebastián Alfaro Arias (C4C212) y Kendal Trejos Cubero (C4K374). Kendal es quien trabaja con vos.
- **Cliente:** ASADA «Acueducto Bodegas y Pilas» (Costa Rica). Así se escribe el nombre siempre; algunas plantillas del profesor dicen «Pilas y Bodegas» por error.
- **Sistema:** **SIGEDA**, Sistema de Gestión Documental del Acueducto. Digitaliza y organiza los expedientes de los **1 015 abonados**: unos 6 090 documentos por digitalizar.
- **Usuarias:**
  - **Secretaría:** la primera usuaria; manejo básico de la tecnología; digitaliza.
  - **Administración (la administradora):** revisa respaldos, completitud y bitácora.
  - Las dos cuentas tienen los mismos permisos (RN-09). Hay una excepción propuesta y todavía por validar: solo la Administración puede autorizar una restauración.
- **Entorno:**
  - Una sola laptop con Windows 10 u 11 de 64 bits, en mal estado. Resolución desconocida: SUPUESTO 1366 × 768.
  - Se escanea con fotocopiadoras multifuncionales, que generan PDF o PNG.
  - Internet estable, pero SIGEDA funciona sin internet.
  - Respaldo en disco externo; OneDrive solo si se confirma la licencia (S-10).
- **Datos personales:** cédulas, contratos y firmas (Ley 8968). Solo se entregan a quien tenga facultad legal, como ARESEP; a AyA y a la Municipalidad no.

## 2. Reglas de trabajo (obligatorias)

1. **No inventés información.** Si algo no está en los documentos, marcalo como **SUPUESTO** y preguntale a Kendal. No fabriqués resultados de pruebas, de evaluaciones con usuarias ni capturas.
2. **Usá los nombres `tabla.columna` del Modelo ER v1.1** (sección 5 de este archivo) en el código, las migraciones y la documentación. No renombrés tablas ni columnas sin avisar; si un cambio es necesario, anotalo para el Anexo B.
3. **Solo datos ficticios.**
   - Identificaciones con tomo 0000, que no existe en el Registro Civil (por ejemplo 1-0000-0123).
   - Nombres inventados, como los del prototipo: Ana Lucía Mora Vega en la paja 0412, Esteban Mora Vega como cotitular, Rodrigo Mora Castro como titular anterior.
   - Nunca uses datos reales de la ASADA ni de los clientes de LICS.
4. **Idioma:**
   - Hablale a Kendal en español de Costa Rica (voseo).
   - La interfaz le habla a la usuaria de usted («Escriba», «Revise»), como en el prototipo.
   - Fechas dd/mm/aaaa y horas de 24 h.
   - Los mensajes de error dicen la causa, con el dato concreto, y qué hacer (RNF-02). Nunca muestran códigos de error.
5. **Git:**
   - No hagás `commit` ni `push` sin que Kendal lo pida.
   - **Nunca hagás push al repositorio de LICS de Alejandro.**
   - La carpeta de documentos de OneDrive también es un repositorio Git: ahí tampoco hagás commits.
6. **No modifiqués los archivos originales** de la carpeta de documentos (`Enunciados/`, entregables ya presentados). Para generar algo nuevo, trabajá en una copia o en una versión nueva (v0.4, v1.1, etc.).
7. **Referencias en APA 7** en los documentos.
8. **Antes de borrar módulos o hacer cambios grandes** (quitar apps de LICS, cambiar el modelo, tocar `infra/`), proponé el plan y esperá el visto bueno de Kendal.
9. Trabajá por incrementos pequeños y verificables. Cada cambio lleva su prueba (`make test` o la que corresponda).

## 3. Dónde está cada cosa

### 3.1 Repositorio de código (este)
- Base: **LICS v2.5.0**, de Alejandro Arias Rojas (`github.com/aleariasr/laboratorio-inyeccion-castro-solis`). Alejandro autorizó usarlo para SIGEDA.
- Este repositorio de SIGEDA se crea a partir de esa base. El remoto de LICS se renombra a `lics` (solo lectura) y `origin` apunta al repositorio nuevo de SIGEDA.

### 3.2 Carpeta de documentos del proyecto (OneDrive)
Ruta en Windows:
`C:\Users\tcken\OneDrive - Universidad de Costa Rica\Escritorio\UCR\II CICLO\Analisis y Diseño de Sistemas\1.ProyectoAcueducto`

Desde WSL:
`/mnt/c/Users/tcken/OneDrive - Universidad de Costa Rica/Escritorio/UCR/II CICLO/Analisis y Diseño de Sistemas/1.ProyectoAcueducto`

La ruta tiene espacios y «ñ»: ponela siempre entre comillas. Abrí Claude Code con `--add-dir "<esa ruta>"` para poder leerla.

| Archivo (relativo a `1.ProyectoAcueducto/`) | Qué es | Para qué lo usás |
|---|---|---|
| `Contexto_Completo_Proyecto_SIGEDA.md` | Resumen de todo el proyecto: entrevista, reunión del 21/09, ERS, UML, decisiones | Leelo primero |
| `README.md` | Descripción de la carpeta | Orientación |
| `Documentacion/ENTREVISTA.md`, `ENTREVISTA 21 SEPTIEMBRE.docx`, `Guia_Reunion_Administradora_21set2026_1.docx` | Elicitación con la administradora (respuestas B-01 a B-23) | Fuente de los requisitos |
| `Entregables/Vision_Proyecto.docx` | Documento de Visión v1.1 (25/09/2026) | Alcance; dice «internet inestable», pero es estable (B-03) |
| `Entregables/ERS_Acueducto_Bodegas_Pilas_v1.2.docx/.pdf` | **ERS v1.2** (28/09/2026): RF-01 a RF-22, RN-01 a RN-12, RNF-01 a RNF-13, supuestos S-01 a S-21 | **Qué debe hacer el sistema.** Criterios de aceptación |
| `Entregables/Cambios_ERS_v1.2_SIGEDA.pdf` | Correcciones del profesor a la ERS | Contexto |
| `Entregables/Modelos_UML_Acueducto_Bodegas_Pilas.docx/.pdf` y `Entregables/UML/` | **Modelos UML v1.0**: CU-01 a CU-18, especificación de CU-04, clases, secuencia, componentes, trazabilidad | Clases límite, control y entidad; operaciones |
| `Entregables/Arquitectura/Documento_Arquitectura_SIGEDA_v1.1.pdf` y `Retroalimentacion_Documento_Arquitectura_SIGEDA.docx` | **DAS v1.1** (27/10/2026) y su retroalimentación (29/10/2026) | Capas, ADR-01 a ADR-06, despliegue, respaldo (8.2), escenarios EC-01 a EC-04 |
| `Entregables/Modelo entidad relacion/Modelo_ER_Relacional_SIGEDA_v1.1.docx/.pdf` y `Modelo_Relacional_SIGEDA_v1.1_Contexto.md` | **Modelo ER y Relacional v1.1** (03/11/2026): 14 tablas, CHECK, índices, EXCLUDE, consultas Q1 a Q11 | **Fuente del esquema de la base** |
| `Entregables/Prototipos/Prototipos_Interfaz_SIGEDA_v0.3.docx/.pdf` | **Prototipos de interfaz v0.3** (04/11/2026): inventario PAN-01 a PAN-14, mapa, guía de estilo, fichas con `tabla.columna`, sección 7 (prototipo vertical, PENDIENTE) | **Cómo se ve y se comporta cada pantalla.** Hay que completar la sección 7 |
| `Entregables/Prototipos/prototipo/index.html` | Prototipo navegable (un solo HTML). Abrilo en el navegador: `#/PAN-05?estado=seleccionado`, `?hifi=1` para alta fidelidad | Referencia visual de cada pantalla, estado y mensaje |
| `Entregables/Prototipos/capturas/` (77 PNG) y `pantallas.json` | Capturas de todos los estados y el inventario o mapa en JSON | Referencia de la interfaz |
| `Entregables/Prototipos/herramientas/` | `contenido.py` + `construir.py` (llenan la plantilla y generan el .docx), `pdf_toc.py` (PDF con LibreOffice), `capturar.js`, `axe.js`, `mapa*.py` | Para generar el documento v0.4 con la sección 7 |
| `Entregables/Prototipos/Revisión del prototipo SIGEDA — Hallazgos y recomendaciones.pdf` | Revisión del profesor al prototipo (ya aplicada en la v0.3) | Contexto |
| `Enunciados/` | Plantillas originales del profesor (ERS, UML, DAS, Modelo ER, Prototipos) | **No se modifican** |
| `Prompt_Prototipos_SIGEDA.md` | Prompt original del entregable de prototipos | Contexto |

## 4. Requerimientos (resumen; el texto exacto está en la ERS v1.2)

| RF | Nombre | Lo esencial | Pantallas |
|---|---|---|---|
| RF-01 | Autenticar usuario | Usuario y contraseña; dos cuentas con los mismos permisos; cada una cambia su contraseña | PAN-01, PAN-14 |
| RF-02 | Registrar abonado | Número de paja obligatorio y único, tipo, titular vigente (nombre e identificación), sector y estado | PAN-06 |
| RF-03 | Personas asociadas | Cotitular y persona apoderada con fechas; el titular anterior queda como vínculo TITULAR cerrado | PAN-06, D-06, PAN-04 |
| RF-04 | Importar listado de SADA | Crea un abonado por paja no registrada; resumen de importados, omitidos y rechazados; tipo PENDIENTE | PAN-09, PAN-07 |
| RF-05 | Cargar documento | PDF o PNG, tipo obligatorio, nombre identificador opcional, **máximo 10 MB** (S-21) | PAN-05 |
| RF-06 | Fechas del documento | Fecha del documento (hoy por defecto, reemplazable por la original); fecha y hora de carga automática y no editable | PAN-05, PAN-13 |
| RF-07 | Versiones | Una nueva versión no sobrescribe; la más reciente es la vigente; historial consultable | PAN-05, PAN-04, PAN-13 |
| RF-08 | Orden por prioridad | Expediente ordenado por prioridad del tipo (1 plano, 2 solicitud…) | PAN-04 |
| RF-09 | Tipos de documento | Prioridad, obligatoriedad, grupos de alternativas, exigencia a cotitulares | PAN-10 |
| RF-10 | Buscar expedientes | Por paja, nombre del titular vigente, identificación y sector, combinados | PAN-03 |
| RF-11 | Filtrar documentos | Por tipo, nombre identificador y rango de fechas, en el expediente o en todo el archivo | PAN-03, PAN-04 |
| RF-12 | Consultar expediente | Datos, titular, personas, documentos ordenados y visor | PAN-04 |
| RF-13 | Cambiar titular | Cierra el vínculo anterior y abre el nuevo en una transacción | PAN-06, D-04 |
| RF-14 | Completitud | Obligatorios según el tipo de abonado; solo documentos vigentes del titular y de los cotitulares vigentes | PAN-07, PAN-04 |
| RF-15 | Bitácora | Todo cambio a nombre de quien lo hizo, con el valor anterior y el nuevo; no se edita ni se borra | PAN-11 |
| RF-16 | Respaldo y restauración | Diario, automático y cifrado; manual; restaurar; avisos | PAN-08, D-05, PAN-02 |
| RF-17 | Baja y reactivación | No borra documentos | PAN-04, D-03 |
| RF-18 | Exportar | A carpeta o impresión, con aviso de confidencialidad (RN-10) | PAN-12 |
| RF-19 | Anular documento | Con motivo; no se borra; filtro «Mostrar anulados» | PAN-04, D-01 |
| RF-20 | Contraseña temporal | Una cuenta le asigna una temporal a la otra; cambio obligatorio al entrar | PAN-14, PAN-01 |
| RF-21 | Modificar abonado | Sector, tipo y personas | PAN-06 |
| RF-22 | Editar datos del documento | Tipo y nombre identificador | PAN-04, D-02 |

**No funcionales clave:**
- RNF-01: T-01 (buscar) en 1 minuto o menos; T-02 (cargar) en 3 minutos o menos, sin ayuda.
- RNF-02: todo en español, con causa y acción.
- RNF-03: no se pierden documentos ni cambian sus fechas.
- RNF-04: el respaldo se restaura completo en otro equipo y el SHA-256 coincide.
- RNF-05: búsqueda en 3 s o menos en 19 de 20 casos (EC-04).
- RNF-06: visualización en 5 s o menos.
- RNF-09: seguridad.
  - Bloqueo de 5 minutos tras 5 intentos fallidos.
  - Contraseña de mínimo 8 caracteres.
  - Cierre de sesión a los 15 minutos de inactividad, con aviso previo (D-08).
- RNF-10: archivos cifrados, ilegibles fuera de SIGEDA.
- RNF-11: bitácora de solo inserción; la restauración no la borra.
- RNF-12: pérdida máxima de 1 día.
- RNF-13: la clave de cifrado tiene una copia física y otra digital.

**Reglas de negocio clave:**
- RN-01: el número de paja es texto, único, sin espacios, y no se cambia.
- RN-02: un solo titular vigente.
- RN-03a y RN-03b: obligatorios por tipo de abonado y grupos de alternativas.
- RN-05: orden por prioridad, luego nombre del tipo, luego `id_documento`.
- RN-06: versiones sin sobrescribir.
- RN-07: la fecha del documento por defecto es hoy.
- RN-08: la baja no elimina.
- RN-09: mismos permisos para las dos cuentas.
- RN-10: los datos personales solo se entregan a quien tenga facultad legal.
- RN-11: solo PDF o PNG.
- RN-12: el titular anterior no aparece en las búsquedas.

## 5. Modelo de datos (Modelo ER v1.1 con las decisiones del 04/11/2026)

PostgreSQL 17, aprobado por el docente. Hay 14 tablas y todas las llaves foráneas son RESTRICT: sin CASCADE ni borrados.

1. `sector`(**id_sector**, nombre UQ)
2. `abonado`(**id_abonado**, numero_paja UQ, id_sector FK opcional, tipo_abonado CHECK, estado CHECK, fecha_baja opcional)
3. `persona`(**id_persona**, nombre, tipo_identificacion CHECK opcional, identificacion opcional)
   - UQ parcial (tipo_identificacion, identificacion) cuando ambas no son nulas.
   - CHECK: las dos se llenan juntas o ninguna.
   - **Decisión del 04/11/2026:** se quita `id_persona_fusionada_en`, la fusión y la consulta Q11 (quedan como mejora futura).
4. `vinculo_abonado`(**id_abonado, id_persona, fecha_inicio**, rol CHECK, fecha_fin opcional)
   - CHECK fecha_fin >= fecha_inicio.
5. `grupo_alternativas`(**id_grupo_alternativas**, nombre UQ, obligatoriedad CHECK sin NINGUNA)
6. `tipo_documento`(**id_tipo_documento**, id_grupo_alternativas FK opcional, nombre UQ, prioridad > 0, obligatoriedad CHECK opcional, es_exigido_a_cotitulares)
   - CHECK: tiene grupo u obligatoriedad, nunca las dos ni ninguna.
7. `documento`(**id_documento**, id_abonado FK, id_tipo_documento FK, id_persona FK opcional, nombre_identificador opcional, estado CHECK, motivo_anulacion opcional, fecha_anulacion opcional)
8. `version_documento`(**id_documento, numero_version**, nombre_original, ruta_archivo UQ, formato CHECK, tamano_bytes > 0, fecha_documento, fecha_carga, hash_sha256)
9. `cuenta`(**id_cuenta**, usuario UQ, hash_contrasena, perfil CHECK, intentos_fallidos >= 0, bloqueada_hasta opcional, es_contrasena_temporal)
10. `registro_bitacora`(**id_registro_bitacora**, id_cuenta FK opcional, id_abonado como referencia lógica **sin FK**, fecha_hora, accion CHECK, elemento_afectado, origen CHECK)
11. `registro_modificacion`(**id_registro_bitacora, campo_modificado**, valor_anterior, valor_nuevo)
    - Habrá 1 o más filas para MODIFICACION y ANULACION; `campo_modificado` = `tabla.columna`.
12. `registro_restauracion`(**id_registro_bitacora**, nombre_paquete, fecha_respaldo_restaurado)
13. `respaldo`(**id_respaldo**, id_cuenta FK opcional, fecha_hora, tipo CHECK, estado CHECK, nombre_paquete UQ opcional, hash_sha256 opcional, tamano_bytes opcional)
14. `copia_respaldo`(**id_respaldo, destino**, estado CHECK, fecha_hora_verificacion opcional)

**Dominios CHECK:**

| Columna | Valores |
|---|---|
| `abonado.tipo_abonado` | PERSONA_FISICA, PERSONA_JURIDICA, PENDIENTE |
| `abonado.estado` | ACTIVO, DE_BAJA (DE_BAJA ⇔ fecha_baja no nula) |
| `persona.tipo_identificacion` | CEDULA_FISICA, CEDULA_JURIDICA, DIMEX, PASAPORTE |
| `vinculo_abonado.rol` | TITULAR, COTITULAR, APODERADA |
| `grupo_alternativas.obligatoriedad` | PERSONA_FISICA, PERSONA_JURIDICA, AMBAS |
| `tipo_documento.obligatoriedad` | PERSONA_FISICA, PERSONA_JURIDICA, AMBAS, NINGUNA |
| `documento.estado` | VIGENTE, ANULADO (ANULADO ⇔ motivo y fecha no nulos) |
| `version_documento.formato` | PDF, PNG |
| `cuenta.perfil` | SECRETARIA, ADMINISTRADORA. En la interfaz se muestran como «Secretaría» y «Administración»; los usuarios son `secretaria` y `administracion` |
| `registro_bitacora.origen` | USUARIA, SISTEMA (USUARIA ⇔ id_cuenta no nulo) |
| `registro_bitacora.accion` | CREACION, MODIFICACION, ANULACION, CAMBIO_TITULAR, BAJA, REACTIVACION, IMPORTACION, EXPORTACION, RESPALDO, RESTAURACION, RESTABLECIMIENTO_CONTRASENA, CUARENTENA |
| `respaldo.tipo` | AUTOMATICO, MANUAL |
| `respaldo.estado` | COMPLETO, PENDIENTE, FALLIDO (COMPLETO ⇔ existe una copia VERIFICADA) |
| `copia_respaldo.destino` | DISCO_EXTERNO, ONEDRIVE |
| `copia_respaldo.estado` | PENDIENTE, VERIFICADA, FALLIDA |

**Índices y restricciones en `vinculo_abonado`** (requieren `CREATE EXTENSION btree_gist`; también se usan `unaccent` y `pg_trgm` para la búsqueda, ADR-06):
- UNIQUE (id_abonado) WHERE rol = 'TITULAR' AND fecha_fin IS NULL. Es RN-02.
- UNIQUE (id_abonado, id_persona) WHERE fecha_fin IS NULL.
- EXCLUDE USING gist (id_abonado WITH =, id_persona WITH =, daterange(fecha_inicio, fecha_fin, '[)') WITH &&).
- EXCLUDE USING gist (id_abonado WITH =, daterange(fecha_inicio, fecha_fin, '[)') WITH &&) WHERE (rol = 'TITULAR').

**Reglas que programa la aplicación:**
- **Alta de abonado:** abonado + persona + vínculo TITULAR en una sola transacción.
- **Cambio de titular:** cerrar el vínculo anterior y abrir el nuevo en la misma transacción.
- **Carga (CU-04):** documento + version_documento (numero_version = 1) + bitácora en una transacción. La persona debe tener un vínculo vigente con el abonado.
- **Nueva versión:** numero_version = máximo + 1; la anterior se conserva.
- **Importación de SADA:** crea una persona por abonado y no une nombres. El duplicado se detecta cuando alguien completa la cédula (aviso «Ya existe una persona con esa cédula» con la opción de usarla).
- **Bitácora:** un evento por elemento afectado. La bitácora es de solo inserción: el usuario de base de datos de la aplicación solo tiene INSERT y SELECT sobre ella (ADR-05).
- **Grupo de alternativas:** 2 o más tipos.

**Catálogos iniciales.** Los saca del prototipo; la prioridad del 3 en adelante es provisional.
- **Sectores:** Bodegas, Pilas, Calle Cerro, Calle Central y Trapiche. SUPUESTO: confirmar la lista completa.
- **Tipos de documento:**
  1. Plano legible (Ambas)
  2. Formulario de solicitud (Ambas)
  3. Copia de cédula (Persona física, exigido a cotitulares)
  4. Certificación de registro de propiedad (Persona física)
  5. Contrato de servicio (Ambas)
  6. Cédula jurídica (Persona jurídica)
  7. Personería jurídica vigente (Persona jurídica)
  8. Cédula de la persona apoderada (Persona jurídica)
  9. Permiso de construcción vigente: grupo «Permiso o formulario», Persona jurídica
  10. Formulario de construcción y uso del agua: mismo grupo
  11. Boletas de trabajo (Ninguna)
  12. Recibos por cobros especiales (Ninguna)
  13. Conexiones ilegales (Ninguna)
  14. Fotos del inmueble (Ninguna)

## 6. Arquitectura (DAS v1.1) y decisión de tecnología

- **Estilo:** capas.
  - Presentación (Next.js).
  - Lógica de negocio (controladores y fachadas `IDocumentos`, `IConsultas`, `IBitacora`).
  - Datos y servicios (repositorios `IPersistencia`, `AlmacenArchivosCifrados` sobre `IAlmacenArchivos`, `ServicioCifrado`, Programador de tareas).
  - Aplicación web local en la misma laptop, presentada como aplicación de escritorio.
- **ADR:**
  - **ADR-01, tecnología:** Electron + Next.js + Django/DRF + PostgreSQL 17 + Nginx (solo 127.0.0.1) + Docker Compose en WSL2, con instalador sin conexión.
  - **ADR-02, documentos:** cifrados con AES-256-GCM en un volumen; los metadatos, la ruta y el SHA-256 van en PostgreSQL.
  - **ADR-03, respaldo:** diario y completo (base + almacén), verificado con SHA-256, cifrado y copiado al disco USB (y a OneDrive si se confirma S-10). Se conservan 7 diarios y 4 semanales. El temporizador de systemd hace de Reloj del sistema.
  - **ADR-04, importación de SADA:** `IFuenteImportacion.leerFilas(ruta)` con openpyxl o csv.
  - **ADR-05, cuentas y seguridad:** dos cuentas, un rol, PBKDF2, bloqueo de 5 minutos tras 5 intentos, inactividad de 15 minutos, bitácora de solo inserción.
  - **ADR-06, búsqueda:** índices B-tree + pg_trgm/unaccent.
- **Decisión del 04/11/2026: reutilizar LICS v2.5.0** como base. Trae:
  - Python 3.13, Django 5.2.6, DRF 3.16.1, psycopg 3, gunicorn, openpyxl y reportlab.
  - Next.js 16.2 + React 19.2 en modo standalone.
  - PostgreSQL 17, Nginx y Docker Compose (`infra/docker/compose.yml`, `compose.prod.yml`).
  - systemd (servicio, temporizador de respaldo y vigilante).
  - En Windows: Electron (^31, desactualizado), WSL2 + Docker Engine, imagen dorada, instalador NSIS, tareas programadas y un ejecutor de GitHub Actions self-hosted.
  - Apps de Django: `accounts`, `core`, `configuration`, `documents`, `health`. Las de negocio de LICS (`inventory`, `sales`, `cash`, `customers`, `legacy_migration`) **no aplican a SIGEDA**.
  - Documentación de LICS en `docs/`: architecture, backup-restore, security, deployment, etc.
- **Faltantes de LICS frente a SIGEDA.** Hay que construirlos:
  1. `scripts/backup.sh` respalda solo la base (pg_dump): no incluye los documentos (volumen `backend_media`), no cifra y deja el respaldo dentro de la distribución local.
  2. `scripts/restore.sh` reemplaza toda la base, **bitácora incluida**, y solo corre desde la terminal (pide escribir `RESTORE lics`). SIGEDA restaura desde la aplicación (D-05), sin borrar la bitácora, con respaldo previo automático y registro en `registro_restauracion`.
  3. No tiene bloqueo tras intentos fallidos ni cierre por inactividad.
  4. «lics» aparece unas 455 veces en 52 archivos de `infra/`, `scripts/` y `.github`: hay que renombrarlo a «sigeda».
  5. `package.json` dice «UNLICENSED» con autor «Castro Solis»: hay que ajustar el nombre, el autor y la licencia, dándole crédito a Alejandro.
  6. Cifrado AES-256-GCM de documentos y manejo de la clave (RNF-13). La clave nunca va en el repositorio. SUPUESTO: archivo o variable fuera del repositorio, más la copia física.
- **Despliegue:** sigue abierto (laptop local o máquina virtual Linux en Azure). El código no depende de esa decisión: no la bloqueés.

## 7. Interfaz (Prototipos v0.3)

- **Pantallas:** PAN-01 a PAN-14.
  - PAN-01 inicio de sesión, PAN-02 inicio, PAN-03 buscar, PAN-04 expediente, PAN-05 cargar documento, PAN-06 abonado y personas, PAN-07 completitud.
  - PAN-08 respaldos, PAN-09 importar SADA, PAN-10 tipos de documento, PAN-11 bitácora, PAN-12 exportar, PAN-13 versiones, PAN-14 mi cuenta.
- **Diálogos:** D-01 anular, D-02 editar datos, D-03 baja o reactivación, D-04 cambiar titular, D-05 restaurar, D-06 agregar persona asociada, D-07 salir sin guardar, D-08 sesión por cerrarse.
- **Guía de estilo:**
  - Segoe UI, texto de 15 px, títulos de 22 px.
  - Un solo botón principal por sección. Los botones peligrosos llevan borde rojo y el verbo exacto.
  - Color principal #0B5C8A. Estados: verde #2F7A45 sobre #E6F2EA, ámbar #7A5600 sobre #FFF4D6, rojo #A61B1B sobre #FBE9E9, siempre con texto.
  - Contraste mínimo de 4,5:1 (WCAG 2.2).
  - La identificación se oculta parcialmente en las listas (1-••••-0123).
  - Se dice «anular», nunca «eliminar».
- **Uso previsto:** solo computadora; ancho mínimo de 1280 px; diseño base de 1366 × 768.
- **Accesibilidad:** `label for` en cada campo, `<dialog>` nativo, landmarks. Revisá con axe-core: el prototipo tiene 0 infracciones y la aplicación debe mantenerlo.
- El código de LICS tiene su propio sistema de diseño (`docs/frontend-design-system.md`, `frontend/src/components`). Reutilizá los componentes, pero ajustá el aspecto a la guía de SIGEDA.

## 8. Lo que hay que construir primero: prototipo vertical (Incremento 1)

**Entrega: Avance de Construcción, viernes 06/11/2026.** Para esa fecha se presentan el **script DDL** del modelo v1.1 y la **rebanada vertical de CU-04 Cargar documento**. Esa rebanada le toca a la pareja de Mariangel y Kendal. En clase se había usado Java + MySQL con una tabla `expediente`, pero el docente aprobó PostgreSQL 17 y el modelo usa `abonado`: alineá todo con el modelo v1.1.

**Ficha del prototipo vertical** (sección 7 del documento de Prototipos v0.3):

| Campo | Valor |
|---|---|
| Función | CU-04 Cargar documento (RF-05, RF-06, RF-07) |
| Versión | 0.1.0 |
| Pantalla | PAN-05 Cargar documento (PantallaCargaDocumento): prototipo evolutivo vertical de fidelidad media |
| Clase control | `ControladorDocumentos.cargarDocumento()`, `cargarNuevaVersion()` y `validarArchivo()`. Además `VersionDocumento`/`agregarVersion()`, `Abonado.agregarDocumento()` y `ControladorBitacora.registrar()` |
| Interfaz y repositorio | Fachada `IDocumentos`; `RepositorioDocumentos` (`IPersistencia`); `AlmacenArchivosCifrados` (`IAlmacenArchivos`); `IBitacora` |
| Tablas, en orden de llaves foráneas | abonado, persona, vinculo_abonado, grupo_alternativas, tipo_documento, documento, version_documento, cuenta, registro_bitacora (+ sector) |

**Comportamiento esperado** (ver capturas `PAN-05_*` y la ficha 6.3 del documento):
- Se entra con el expediente ya elegido (desde PAN-04 o PAN-07).
- Se pueden elegir varios archivos a la vez; cada uno lleva su tipo (obligatorio), la persona que lo aporta (solo personas con vínculo vigente; se propone el titular), el nombre identificador (opcional) y la fecha del documento (hoy por defecto, editable, dd/mm/aaaa).
- Opción explícita de «nueva versión de un documento existente».
- **Validación antes de guardar:**
  - Solo PDF o PNG, revisando el contenido real del archivo y no solo la extensión.
  - Máximo 10 MB.
  - Tipo obligatorio.
- Los mensajes son los del prototipo, por ejemplo: «Es un archivo JPG. Solo se aceptan PDF o PNG: conviértalo con la fotocopiadora o elija otro archivo» o «Pesa 14,2 MB y el máximo es 10 MB…».
- Mientras haya errores no se guarda nada.
- **Al guardar, en una sola transacción:**
  - Se crean `documento` y `version_documento`.
  - Se calcula el SHA-256 y se cifra el archivo con AES-256-GCM en el almacén.
  - Se agrega un evento CREACION en `registro_bitacora` por documento, a nombre de la cuenta.
  - `fecha_carga` la asigna el sistema y no se puede editar.
- **Mensaje de éxito**, con dos salidas: «Ver expediente» o «Cargar otro documento».
- Para verificar, como mínimo: listado del expediente ordenado por RN-05 y visor del documento descifrado en memoria (parte de PAN-04).

**Prueba de terminado.** Hay que ejecutarla de verdad y anotar los resultados reales. No los inventés.

| Prueba | Datos | Resultado esperado |
|---|---|---|
| Conservar la fecha original | 5 PDF ficticios de menos de 10 MB, abonado de prueba 0412, fecha 15/03/2005 | 5 cargas; fecha_documento = 15/03/2005 en las 5; el SHA-256 del archivo descifrado coincide con el original |
| Cifrado | Los 5 archivos copiados del almacén y abiertos con otro programa | 0 archivos legibles fuera de SIGEDA (RNF-10) |
| Rechazos | 1 archivo .jpg y 1 PDF de 14 MB | 2 rechazos con causa y acción; 0 filas nuevas en documento y version_documento |
| Nueva versión | Versión 2 del formulario, con fecha 10/02/2026 | numero_version = 2; la versión 1 conserva fecha_documento 15/03/2005 |
| Bitácora | Las cargas anteriores | 1 fila CREACION en registro_bitacora por carga, a nombre de la cuenta |

**Evidencia que hay que producir para el documento:**
- Capturas reales de la aplicación funcionando (pantalla y resultado en la base de datos).
- Resultados de cada prueba.
- Qué se aprendió: decisiones del DAS confirmadas o cambiadas.
- Enlace del repositorio.

Con eso se genera **Prototipos_Interfaz_SIGEDA_v0.4** con los scripts de `herramientas/`: se editan las listas `VERTICAL`, `PRUEBAS` y `ANEXO_A` en `contenido.py` y se reemplazan los marcadores de la sección 7 en `construir.py`. Notas:
- `construir.py` necesita `Enunciados/Plantilla_Prototipos_Interfaz_SIGEDA.docx`, la carpeta de capturas y el mapa rotado 90°, que se saca de `mapa_navegacion/Mapa_Navegacion_SIGEDA_documento.png`.
- `pdf_toc.py` necesita LibreOffice y tiene una ruta de importación de otro entorno que hay que ajustar.

## 9. Después: construcción del sistema por incrementos

Este es el orden definido en la sección 3 del documento de Prototipos:
1. **Incremento 1:** carga (PAN-05) y búsqueda (PAN-03, consulta Q1; RNF-05 medido). La bitácora registra desde aquí, aunque su pantalla llegue en el incremento 4.
2. **Incremento 2:** sesión y cuentas (PAN-01, PAN-14, RNF-09, contraseña temporal) y el expediente completo (PAN-02, PAN-04, PAN-06, PAN-13), con sus diálogos D-01 a D-04, D-06, D-07 y D-08.
3. **Incremento 3:** respaldo y restauración (PAN-08, D-05; faltantes 1 y 2 de LICS) e importación de SADA (PAN-09). El respaldo tiene que funcionar antes de cargar datos reales.
4. **Incremento 4:** tipos de documento (PAN-10), completitud (PAN-07), bitácora (PAN-11) y exportación (PAN-12).

**Pendientes con la administradora** (sección 11 del documento de Prototipos). Mientras no se resuelvan, usá la propuesta y marcala como SUPUESTO:
- ¿Solo la Administración restaura?
- ¿Los abonados de baja cuentan en el total?
- ¿Quién hace la prueba de restauración trimestral y dónde se guarda la clave?
- ¿Cédula jurídica de 9 o 10 dígitos? (Se asumen 10.)
- ¿El número de paja tiene ceros iniciales o se reutiliza?
- Orden de los tipos de documento del 3 al 14.
- Resolución de la laptop.

Además hay un riesgo aceptado: si se bloquean las dos cuentas, lo resuelve el soporte técnico en el servidor. No hay código de recuperación.

**Cambios ya acordados para otros artefactos** (Anexo B del documento de Prototipos):
- Modelo ER: quitar la fusión y Q11; tabla propuesta `prueba_restauracion` (SUPUESTO).
- ERS: excepción a RN-09 para restaurar.
- DAS: decisión de usar LICS.
- UML v1.1: pendiente.

## 10. Cómo trabajar en este repositorio

- **Comandos de LICS** (revisá el `Makefile`): `make up`, `make down`, `make migrate`, `make makemigrations`, `make test`, `make shell`, `make db`, `make logs`.
- **Migraciones:** definí las restricciones de PostgreSQL con `django.contrib.postgres`: `ExclusionConstraint`, `UniqueConstraint(condition=…)`, `CheckConstraint` y las extensiones (`BtreeGistExtension`, `UnaccentExtension`, `TrigramExtension`). Así el DDL sale de las migraciones.
- **Script DDL para la entrega:** generalo desde la base migrada, por ejemplo con `pg_dump --schema-only` o `sqlmigrate`, y guardalo como `db/ddl/sigeda_v1.1.sql`, con un encabezado que cite el Modelo ER v1.1.
- **Nombres de tablas:** en los modelos de Django usá `db_table` para que coincidan exactamente con el Modelo ER (`abonado`, `version_documento`…), sin el prefijo de la app.
- **Pruebas:** cada regla de negocio lleva una prueba automática. La prueba de terminado de la sección 8 debe poder repetirse con un comando.
- **Secretos:** nada de claves en el repositorio; usá `.env.example`.
