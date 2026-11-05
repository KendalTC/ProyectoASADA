# Prueba de terminado — CU-04 Cargar documento

Ejecutada de verdad el 04/11/2026 contra el stack real (Docker Compose:
PostgreSQL 17 + Django 5.2.6 + Next.js 16, sin mocks), con el abonado
de prueba 0412 (Ana Lucía Mora Vega, titular; Esteban Mora Vega,
cotitular; Rodrigo Mora Castro, titular anterior) y la cuenta
`secretaria`. Resultados reales, no inventados (CLAUDE.md, regla 1).

Dos formas de evidencia, ambas reales:

1. **Suite automática** (`apps.documents.tests_sigeda.CargaDeDocumentoCU04Tests`,
   repetible con `make test-sigeda`): 15 pruebas, cubren exactamente
   las 5 filas de esta tabla más las reglas de negocio adicionales.
   **Resultado: 40/40 pruebas pasaron** (15 de CU-04 + 25 de las demás
   restricciones del Modelo ER tocadas en esta sesión). La suite
   completa de LICS + SIGEDA: **908/908 pruebas pasaron** (868 de LICS
   sin romperse + 40 nuevas), corrida con `make test`.
2. **Verificación manual contra la base de desarrollo real**, vía
   `curl` a la API y `psql` directo a Postgres — para confirmar que lo
   que corre en contenedores reales (no solo en la base de pruebas
   aislada de Django) se comporta igual. Capturas reales del navegador
   en `docs/evidencia/capturas/` (tomadas con Playwright contra la app
   ya levantada, sin datos inventados).

## 1. Conservar la fecha original

**Datos:** PDF ficticio (`certificacion_registro.pdf`, cabecera `%PDF-`
real, 267 bytes), abonado 0412, fecha del documento 15/03/2005.

**Esperado:** fecha_documento = 15/03/2005; el SHA-256 del archivo
descifrado coincide con el original.

**Resultado obtenido:**
- Automatizado: `test_conserva_fecha_original_en_5_cargas` sube 5
  archivos distintos con fecha 15/03/2005 y verifica que las 5 filas
  de `version_documento` tengan esa fecha y el `hash_sha256` correcto. **Pasó.**
- Manual: cargado vía `POST /api/sigeda/documentos/cargar/`. Fila real
  en `version_documento`:
  ```
  id_documento=1 numero_version=1 fecha_documento=2005-03-15
  hash_sha256=bd24f1c80bf2a2019e38cace057b377d1ac143d039a80aada2e6c67fc46103ed
  ```
  Descargado vía `GET /api/sigeda/documentos/1/versiones/1/descargar/`
  y comparado con `sha256sum`: **hash idéntico al original**, `diff`
  sin diferencias.

**¿Pasó?** Sí.

## 2. Cifrado

**Datos:** el archivo cargado en la prueba 1, leído directamente del
volumen de almacenamiento (sin pasar por SIGEDA).

**Esperado:** 0 archivos legibles fuera de SIGEDA (RNF-10).

**Resultado obtenido:**
- Automatizado: `test_archivos_en_el_almacen_quedan_cifrados` confirma
  que el archivo en disco no empieza con `%PDF-` y no es igual al
  contenido original; y que `AlmacenArchivosCifrados.leer_archivo()`
  sí recupera el original. **Pasó.**
- Manual: `od -c` sobre el archivo real en
  `/app/almacen_cifrado/documentos/de39f22fd6b84d99aefdce9ca8440243.bin`
  muestra bytes sin ningún patrón reconocible (no `%PDF-`, no texto).
  Tamaño en disco: 295 bytes = 267 (original) + 12 (nonce) + 16 (tag
  GCM) — exacto. AES-256-GCM vía `cryptography.hazmat...AESGCM`, clave
  de 32 bytes fuera del repositorio (`infra/docker/.env`, gitignored).

**¿Pasó?** Sí.

## 3. Rechazos

**Datos:** 1 archivo `.jpg` (cabecera JPEG real) y 1 PDF de más de
10 MB (cabecera `%PDF-` real + relleno; se usó 11,0 MB, por encima del
límite de 10 MB del enunciado original de "14 MB" pero con el mismo
efecto de prueba).

**Esperado:** 2 rechazos con mensaje de causa y acción; 0 filas nuevas
en `documento` y `version_documento`.

**Resultado obtenido:**
- Automatizado: `test_rechaza_jpg_y_no_guarda_nada`,
  `test_rechaza_archivo_de_mas_de_10mb_y_no_guarda_nada` y
  `test_lote_con_un_archivo_invalido_no_guarda_ninguno` (vía API
  completa, con `APIClient`). **Pasaron los 3.**
- Manual: `POST /api/sigeda/documentos/cargar/` con los 2 archivos
  devolvió `400` y:
  ```json
  {"detail":"Hay 2 archivo(s) con problemas. No se guardó ninguno todavía.",
   "errores":[
     {"indice":0,"archivo":"foto.jpg","errores":{"archivo":"Es un archivo JPG. Solo se aceptan PDF o PNG: conviértalo con la fotocopiadora o elija otro archivo."}},
     {"indice":1,"archivo":"plano_grande.pdf","errores":{"archivo":"Pesa 11,0 MB y el máximo es 10 MB. Escanéelo a menor resolución o divídalo en dos archivos."}}]}
  ```
  Conteo de `documento`/`version_documento` antes y después del
  intento: **idéntico** (sin filas nuevas).

**¿Pasó?** Sí.

## 4. Nueva versión

**Datos:** nueva versión del documento 1 (el de la prueba 1), con
fecha 10/02/2026.

**Esperado:** `numero_version` = 2; la versión 1 conserva
`fecha_documento` 15/03/2005.

**Resultado obtenido:**
- Automatizado: `test_nueva_version_no_sobrescribe_la_anterior`. **Pasó.**
- Manual: `POST .../cargar/` con `es_nueva_version: true,
  id_documento: 1` devolvió `numero_version: 2`. Filas reales en
  `version_documento`:
  ```
  id_documento=1 numero_version=1 fecha_documento=2005-03-15
  id_documento=1 numero_version=2 fecha_documento=2026-02-10
  ```

**¿Pasó?** Sí.

## 5. Bitácora

**Datos:** las 2 cargas reales de las pruebas 1 y 4.

**Esperado:** 1 fila `CREACION` en `registro_bitacora` por carga, a
nombre de la cuenta.

**Resultado obtenido:**
- Automatizado: `test_una_fila_creacion_por_carga_a_nombre_de_la_cuenta`. **Pasó.**
- Manual, filas reales en `registro_bitacora`:
  ```
  id_registro_bitacora=1 id_cuenta=1 accion=CREACION elemento_afectado=documento.id_documento=1
  id_registro_bitacora=2 id_cuenta=1 accion=CREACION elemento_afectado=documento.id_documento=1
  ```
  `id_cuenta=1` corresponde a `secretaria`, la cuenta que hizo ambas
  cargas.

**¿Pasó?** Sí.

## Capturas reales

En `docs/evidencia/capturas/` (navegador real, Playwright, contra la
app levantada con `docker compose`, sin datos inventados):

| Archivo | Qué muestra |
|---|---|
| `01_login_inicial.png` | PAN-01-ish: pantalla de inicio de sesión de SIGEDA, con el color de marca #0B5C8A. |
| `02_expediente.png` | PAN-04 mínimo: expediente 0412 recién entrado, con Ana Lucía (titular) y Esteban (cotitular). |
| `03_pan05_inicial.png` | PAN-05, estado inicial: "Todavía no ha elegido archivos". |
| `04_pan05_seleccionado.png` | PAN-05, estado seleccionado: 2 archivos elegidos, uno válido y uno con cédula de Esteban. |
| `05_pan05_error.png` | PAN-05, estado error: un `.jpg` y un PDF de 11 MB, cada uno con su mensaje en rojo, igual al prototipo. |
| `06_pan05_datos_completos.png` | PAN-05 con el archivo válido con tipo, persona y fecha completos, listo para guardar. |
| `07_pan05_cargando.png` / `08_pan05_exito.png` | Resultado del guardado: mensaje de éxito con "Ver expediente" / "Cargar otro documento". |
| `09_pan04_con_documento.png` | Expediente con los 2 documentos cargados (incluida la versión v2 de la prueba 4). |

## Accesibilidad (axe-core)

Corrido contra las 5 pantallas/estados nuevos de SIGEDA (PAN-01 login,
PAN-04 expediente, PAN-05 inicial, PAN-05 con archivos seleccionados y
con error, PAN-05 modo "nueva versión", PAN-13 versiones), con las
mismas reglas que usa el prototipo (`wcag2a`, `wcag2aa`, `wcag21aa`,
`wcag22aa`, `best-practice`):

- Primera corrida: 2 infracciones **críticas** (`label`, `select-name`)
  en los campos de cada fila de PAN-05 (tipo de documento, persona,
  nombre identificador, fecha) — las etiquetas no estaban asociadas
  con `htmlFor`/`id` a su campo. Corregido.
- Una infracción **menor** (`empty-table-header`) en PAN-13: la
  columna de acciones no tenía texto para lectores de pantalla.
  Corregido con un `sr-only`.
- Tras los 2 arreglos: **0 infracciones en las 5 pantallas/estados**,
  igual que el estándar del prototipo (`Prototipos_Interfaz_SIGEDA_v0.3`,
  sección 3).

## Qué se aprendió (confirmaciones y cambios sobre el DAS v1.1)

- **Confirmado:** AES-256-GCM con `cryptography.hazmat.primitives.ciphers.aead.AESGCM`
  funciona bien para este volumen (267 bytes a pruebas de hasta 11 MB);
  el patrón nonce(12)+ciphertext+tag(16) concatenado en un solo
  archivo es simple y suficiente — el DAS no especificaba el formato
  interno, quedó resuelto acá.
- **Confirmado:** Django 5.2 `CompositePrimaryKey` funciona de
  verdad con `ExclusionConstraint` y `UniqueConstraint(condition=...)`
  sobre PostgreSQL 17 — migró, aplicó y los EXCLUDE rechazan
  solapamientos de verdad (ver pruebas de `apps.abonados.tests`).
- **Cambio de alcance respecto al plan original:** no se removieron
  las apps de negocio de LICS (`inventory`, `sales`, `cash`,
  `customers`, `legacy_migration`) en este incremento — SIGEDA se
  construyó como apps nuevas y aditivas (`abonados`, `bitacora`,
  `respaldos`, más adiciones a `accounts`, `configuration`,
  `documents`) para no arriesgar la base bajo presión de tiempo. Esa
  limpieza queda para el siguiente incremento.
- **Limitación conocida, documentada, no oculta:** la "cuarentena" de
  archivos huérfanos usa `transaction.on_commit` para mover el archivo
  de `cuarentena/` a `documentos/` solo después de que la fila de base
  de datos se confirme; no hay todavía un trabajo de reconciliación
  automática para el caso (raro) de que el proceso muera justo entre
  el commit y ese movimiento.
- **SUPUESTO:** la clave de cifrado AES-256 vive en
  `infra/docker/.env` (fuera de Git) solo para este incremento de
  desarrollo. La entrega como secreto de Docker y su custodia física +
  digital (RNF-13) son trabajo de despliegue real, pendiente para el
  Incremento 3.
