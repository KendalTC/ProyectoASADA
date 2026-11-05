Hola. Vamos a construir SIGEDA, el sistema de gestión documental de la ASADA Acueducto Bodegas y Pilas, para el curso IF6100 de la UCR. Todo el contexto del proyecto está en `CLAUDE.md`, en la raíz de este repositorio: leelo completo antes de hacer cualquier cosa y seguí sus reglas.

Este repositorio parte del código de LICS v2.5.0 (autor: Alejandro Arias Rojas, integrante del equipo, quien autorizó usarlo). Los documentos del proyecto están en la carpeta que agregué con `--add-dir` (sección 3.2 de `CLAUDE.md`).

## Objetivo de esta sesión

Dejar listo el **prototipo vertical de CU-04 Cargar documento** y el **script DDL del Modelo ER v1.1** para el Avance de Construcción del viernes 06/11/2026. Después vamos a seguir con la construcción del sistema por incrementos (sección 9 de `CLAUDE.md`).

## Pasos

### Fase 0: entender (sin cambiar nada)
1. Leé, en este orden:
   1. `CLAUDE.md`.
   2. `Contexto_Completo_Proyecto_SIGEDA.md`.
   3. `Entregables/Modelo entidad relacion/Modelo_Relacional_SIGEDA_v1.1_Contexto.md`.
   4. La ficha de PAN-05 (sección 6.3) y la sección 7 de `Entregables/Prototipos/Prototipos_Interfaz_SIGEDA_v0.3.pdf`.
   5. La especificación de CU-04 en los Modelos UML.
   6. RF-05 a RF-07 y RNF-03, RNF-10 y RNF-11 en la ERS v1.2.
   7. Las secciones 5, 7 y 8 del DAS v1.1.
2. Mirá las capturas `Entregables/Prototipos/capturas/PAN-05_*.png`, `PAN-04_*.png` y `PAN-13_*.png`.
3. Recorré el repositorio de LICS:
   - `README.md`
   - `docs/architecture.md`, `docs/backup-restore.md`, `docs/security.md`, `docs/development.md`, `docs/data-model.md`
   - `Makefile`
   - `infra/docker/`
   - `backend/src/config/` y `backend/src/apps/{accounts,core,documents,configuration,health}`
   - `frontend/src/` (sobre todo `components/` y `lib/api`)
4. Devolveme un resumen corto con tres cosas:
   - Qué de LICS se reutiliza tal cual, qué se adapta y qué se quita.
   - Cómo vas a representar el Modelo ER v1.1 en Django (apps, `db_table`, restricciones).
   - Cómo vas a cifrar y guardar los archivos.

   Agregá todas las preguntas que tengás. **Esperá mi visto bueno antes de la fase 1.**

### Fase 1: preparar la base de SIGEDA
5. Proponé y, cuando yo apruebe, aplicá:
   - Quitar las apps de negocio de LICS que no aplican (`inventory`, `sales`, `cash`, `customers`, `legacy_migration`), con sus rutas y pantallas.
   - Renombrar «lics» → «sigeda» en el proyecto, compose, scripts e infra. Hacelo con cuidado y revisá que todo siga levantando.
   - Ajustar el nombre, el autor y la licencia en `package.json`, el README y `VERSION` (0.1.0), dándole crédito a LICS y a Alejandro.
6. Verificá que `make up`, `make migrate` y `make test` funcionen.

### Fase 2: modelo de datos y DDL
7. Creá los modelos de Django del Modelo ER v1.1, con todas sus restricciones: CHECK, UQ parciales, EXCLUDE y extensiones `btree_gist`, `unaccent` y `pg_trgm`.
   - No incluyas `persona.id_persona_fusionada_en`.
   - La bitácora es de solo inserción: el usuario de base de datos de la aplicación solo tiene INSERT y SELECT sobre ella.
8. Agregá la carga inicial de los catálogos: sectores, los 14 tipos de documento y el grupo «Permiso o formulario».
9. Agregá datos de prueba ficticios: abonado 0412, Ana Lucía Mora Vega como titular y Esteban Mora Vega como cotitular, más las cuentas `secretaria` y `administracion`.
10. Agregá pruebas automáticas para cada restricción: un solo titular vigente, sin periodos superpuestos, cédula única, CHECK de anulación, etc.
11. Generá `db/ddl/sigeda_v1.1.sql` desde la base migrada y revisá que corresponda tabla por tabla con el Modelo ER v1.1.

### Fase 3: rebanada vertical de CU-04
12. Backend:
    - `ControladorDocumentos` con `validarArchivo()`, `cargarDocumento()` y `cargarNuevaVersion()`.
    - La fachada `IDocumentos`, `RepositorioDocumentos`, `AlmacenArchivosCifrados` (AES-256-GCM con la clave fuera del repositorio), SHA-256 e `IBitacora`.
    - Todo en una transacción. Si algo falla, no quedan archivos huérfanos; si alguno queda, va a cuarentena.
13. API REST:
    - Carga de varios archivos con sus datos.
    - Listado del expediente en el orden de RN-05.
    - Descarga del documento descifrado para el visor.
14. Frontend:
    - PAN-05 según el prototipo: estados inicial, seleccionado, error, cargando, éxito y versión.
    - Una vista mínima del expediente (PAN-04) para comprobar el orden y ver el documento.
    - Mensajes y etiquetas iguales a los del prototipo.
    - Revisá la accesibilidad con axe-core.
15. Prueba de terminado (sección 8 de `CLAUDE.md`): automatizala, ejecutala y guardá los resultados **reales** en `docs/evidencia/prueba_terminado_CU04.md`. Si algo falla, decímelo; no lo maquillés.
16. Capturas reales de PAN-05 y PAN-04 funcionando, y de las filas en la base de datos, guardadas en `docs/evidencia/`.

### Fase 4: documento
17. Prepará los cambios para la sección 7 del documento de Prototipos, que va a ser la versión v0.4:
    - Ficha del prototipo vertical (VERTICAL).
    - Resultados de la prueba (PRUEBAS).
    - Qué aprendimos.
    - Enlace del repositorio (Anexo A).
    - Usá los scripts de `Entregables/Prototipos/herramientas/`.
    - Generá el .docx y el PDF como archivos nuevos (`..._v0.4`), sin tocar la v0.3.
18. Dame la lista de lo que quedó PENDIENTE y de lo que hay que anotar en el Anexo B.

Recordá: no inventés datos ni resultados, marcá los SUPUESTOS, no hagás commits ni push sin que te lo pida y nunca hagás push al repositorio de LICS.
