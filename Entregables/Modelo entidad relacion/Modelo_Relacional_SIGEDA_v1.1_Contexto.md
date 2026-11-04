# SIGEDA: Modelo ER y Relacional v1.1 (corregido). Contexto para la siguiente etapa

**Estado al 03/11/2026.** El documento *Modelo_ER_Relacional_SIGEDA_v1.1* (53 páginas, docx + pdf) atiende las 19 observaciones de la revisión del docente (Mac858) del 02/11/2026. Este archivo reemplaza la parte de modelo lógico de `claude/Contexto_SIGEDA_Modelo_Relacional.md` y es la fuente para el **script DDL del Avance de Construcción (06/11/2026)**.

- **Motor:** PostgreSQL 17, aprobado por el docente. Se permiten el índice único parcial (RN-02) y EXCLUDE (obs. 7).
- **Equipo:** Mariangel Arias Alfaro, Alejandro Arias Rojas, Sebastián Alfaro Arias, Kendal Trejos Cubero. Docente: Mag. James Mcintosh Molina. IF6100, Grupo 02, II Ciclo 2026.

## Decisiones tomadas con el usuario (03/11/2026)

| Observación | Decisión |
|---|---|
| Obs. 2 (alta): un solo campo por evento | **Opción A.** `registro_modificacion` es el detalle del evento: PK (id_registro_bitacora, campo_modificado), 1..* para MODIFICACION y ANULACION. Es entidad débil, ya no subtipo. |
| Obs. 1 (alta): personas duplicadas | **UQ parcial** (tipo_identificacion, identificacion) cuando no son nulas, más **consulta Q11** de posibles duplicados (mismo nombre normalizado), más **fusión** con `persona.id_persona_fusionada_en` (FK a persona). Nada se borra. |
| Obs. 7: periodos de vínculo | **Se mantiene la PK** (id_abonado, id_persona, fecha_inicio) y se agregan **2 EXCLUDE**. Un error se corrige en la misma fila (evento MODIFICACION). Un vínculo que no debió existir se cierra con fecha_fin = fecha_inicio, que deja un periodo vacío (SUPUESTO). |

## Esquema lógico v1.1: 14 tablas, 14 FK, todas RESTRICT

1. **sector**(**id_sector** PK, nombre UQ)
2. **abonado**(**id_abonado** PK, numero_paja UQ, id_sector FK→sector opc., tipo_abonado CHECK, estado CHECK, fecha_baja opc.)
3. **persona**(**id_persona** PK, nombre, tipo_identificacion CHECK opc., identificacion opc., id_persona_fusionada_en FK→persona opc.)
   - UQ parcial (tipo_identificacion, identificacion) WHERE ambas NOT NULL.
4. **vinculo_abonado**(**id_abonado** PK FK→abonado, **id_persona** PK FK→persona, **fecha_inicio** PK, rol CHECK, fecha_fin opc.)
5. **grupo_alternativas**(**id_grupo_alternativas** PK, nombre UQ, obligatoriedad CHECK)
6. **tipo_documento**(**id_tipo_documento** PK, id_grupo_alternativas FK opc., nombre UQ, prioridad, obligatoriedad CHECK opc., es_exigido_a_cotitulares)
7. **documento**(**id_documento** PK, id_abonado FK, id_tipo_documento FK, id_persona FK opc., nombre_identificador opc., estado CHECK, motivo_anulacion opc., fecha_anulacion opc.)
8. **version_documento**(**id_documento** PK FK, **numero_version** PK, nombre_original, ruta_archivo UQ, formato CHECK, tamano_bytes, fecha_documento, fecha_carga, hash_sha256)
9. **cuenta**(**id_cuenta** PK, usuario UQ, hash_contrasena, perfil CHECK, intentos_fallidos, bloqueada_hasta opc., es_contrasena_temporal)
10. **registro_bitacora**(**id_registro_bitacora** PK, id_cuenta FK opc., id_abonado ref. lógica **sin FK** opc., fecha_hora, accion CHECK (discriminador), elemento_afectado, origen CHECK)
11. **registro_modificacion**(**id_registro_bitacora** PK FK→registro_bitacora, **campo_modificado** PK, valor_anterior opc., valor_nuevo opc.)
12. **registro_restauracion**(**id_registro_bitacora** PK FK→registro_bitacora, nombre_paquete, fecha_respaldo_restaurado)
13. **respaldo**(**id_respaldo** PK, id_cuenta FK opc., fecha_hora, tipo CHECK, estado CHECK (derivado guardado), nombre_paquete UQ opc., hash_sha256 opc., tamano_bytes opc.)
14. **copia_respaldo**(**id_respaldo** PK FK→respaldo, **destino** PK CHECK, estado CHECK, fecha_hora_verificacion opc.)

**Orden de creación en el DDL:**
1. sector
2. abonado
3. persona
4. vinculo_abonado
5. grupo_alternativas
6. tipo_documento
7. documento
8. version_documento
9. cuenta
10. registro_bitacora
11. registro_modificacion
12. registro_restauracion
13. respaldo
14. copia_respaldo

## Dominios CHECK

| Columna | Valores |
|---|---|
| abonado.tipo_abonado | PERSONA_FISICA, PERSONA_JURIDICA, PENDIENTE |
| abonado.estado | ACTIVO, DE_BAJA (DE_BAJA ⇔ fecha_baja no nula) |
| persona.tipo_identificacion | CEDULA_FISICA, CEDULA_JURIDICA, **DIMEX, PASAPORTE** (obs. 13) |
| vinculo_abonado.rol | TITULAR, COTITULAR, APODERADA |
| grupo_alternativas.obligatoriedad | PERSONA_FISICA, PERSONA_JURIDICA, AMBAS (**sin NINGUNA**, obs. 12) |
| tipo_documento.obligatoriedad | PERSONA_FISICA, PERSONA_JURIDICA, AMBAS, NINGUNA |
| documento.estado | VIGENTE, ANULADO (ANULADO ⇔ motivo y fecha no nulos) |
| version_documento.formato | PDF, PNG |
| cuenta.perfil | SECRETARIA, ADMINISTRADORA |
| registro_bitacora.origen | USUARIA, SISTEMA (USUARIA ⇔ id_cuenta no nulo) |
| registro_bitacora.accion | CREACION, MODIFICACION, ANULACION, CAMBIO_TITULAR, BAJA, REACTIVACION, IMPORTACION, EXPORTACION, RESPALDO, RESTAURACION, RESTABLECIMIENTO_CONTRASENA, CUARENTENA |
| respaldo.tipo | AUTOMATICO, MANUAL |
| respaldo.estado | COMPLETO, PENDIENTE, FALLIDO |
| copia_respaldo.destino | DISCO_EXTERNO, ONEDRIVE (como máximo 2 copias por respaldo) |
| copia_respaldo.estado | PENDIENTE, VERIFICADA, FALLIDA |

**Otros CHECK:**
- tipo_documento: tiene grupo u obligatoriedad, nunca ambos ni ninguno.
- persona: tipo e identificación se llenan juntos o ninguno; id_persona_fusionada_en <> id_persona.
- vinculo_abonado: fecha_fin >= fecha_inicio.
- prioridad > 0; tamano_bytes > 0; intentos_fallidos >= 0.

## Índices únicos parciales y EXCLUDE (vinculo_abonado)

- UNIQUE (id_abonado) WHERE rol = 'TITULAR' AND fecha_fin IS NULL. Corresponde a RN-02: como máximo un titular vigente.
- UNIQUE (id_abonado, id_persona) WHERE fecha_fin IS NULL.
- EXCLUDE USING gist (id_abonado WITH =, id_persona WITH =, daterange(fecha_inicio, fecha_fin, '[)') WITH &&). Impide periodos superpuestos de la misma pareja.
- EXCLUDE USING gist (id_abonado WITH =, daterange(fecha_inicio, fecha_fin, '[)') WITH &&) WHERE (rol = 'TITULAR'). Impide titulares superpuestos.
- Requiere `CREATE EXTENSION btree_gist;`. El rango es semiabierto: un titular puede terminar el mismo día en que empieza el siguiente.

## Reglas que programa la aplicación (sección 2.7)

- **Alta de abonado** (CU-02 e importación CU-03): abonado + persona + vínculo TITULAR en **una transacción**, porque todo abonado tiene exactamente un titular vigente.
- **Cambio de titular** (CU-07): se cierra el anterior y se abre el nuevo en la misma transacción.
- **Carga de documento** (CU-04): documento + version_documento(numero_version = 1) en una transacción. Además se valida que la persona tenga un vínculo vigente con el abonado.
- **Importación de SADA:** se busca por nombre normalizado y **no se une automáticamente**. La consulta Q11 lista los posibles duplicados y la fusión la decide la administradora en CU-15/CU-18.
- **Fusión** (una transacción):
  1. Se mueven los vínculos y documentos de la persona duplicada a la que queda. Si ambas tienen un vínculo vigente con el mismo abonado, se conserva uno y se cierra el otro.
  2. La duplicada guarda id_persona_fusionada_en.
  3. Se registra un evento MODIFICACION por cada elemento cambiado.
  4. La persona fusionada no recibe nada nuevo y no aparece en las búsquedas.
- **Discriminador de la bitácora:**
  - MODIFICACION o ANULACION ⇔ 1..* filas en registro_modificacion.
  - RESTAURACION ⇔ exactamente 1 fila en registro_restauracion.
  - Las demás acciones no tienen ninguna de las dos.
  - Se puede reforzar con un disparador diferido.
- **Un evento por elemento afectado** y una fila de detalle por campo (campo_modificado = `tabla.columna`). Una ANULACION genera 1 evento con 3 filas: estado, motivo_anulacion y fecha_anulacion.
- **respaldo.estado:** COMPLETO ⇔ existe una copia VERIFICADA. Se actualiza en la misma transacción que la copia. Es la tercera desnormalización declarada.
- **Grupo de alternativas:** debe tener 2 o más tipos (CU-09).
- **Orden del expediente** (RN-05): prioridad, luego nombre del tipo, luego id_documento.
- **Bitácora de solo inserción:** el usuario de BD de la aplicación solo tiene INSERT y SELECT (ADR-05).
- **Sin CASCADE ni borrados.**

## Desnormalizaciones declaradas (3)

1. El motivo y la fecha de anulación se repiten en el detalle de la bitácora.
2. nombre_paquete se repite en registro_restauracion.
3. respaldo.estado es un derivado que se guarda.

## Volúmenes (5.1, SUPUESTOS)

| Tabla | Al instalar | Al terminar la digitalización | A 5 años |
|---|---|---|---|
| abonado | 1 015 | 1 015 | 1 015 |
| persona | ~1 015 | ~1 220 | ~1 830 |
| documento | 0 | 6 090 | ≤9 135 |
| version_documento | 0 | 6 090 | ≤12 000 |
| registro_bitacora | <10 | ~7 100 | ~22 100 (7 105 + 3 000/año × 5) |
| registro_modificacion | 0 | ~1 070 | ~3 320 (10 % de eventos × 1,5 campos) |
| respaldo | 0 | 1 por día | ~1 830 |
| copia_respaldo | 0 | 1 o 2 por respaldo | ~1 830 a ~3 660 |

## Consultas de verificación

- Q1: búsqueda (excluye personas fusionadas).
- Q2: expediente ordenado.
- Q3: completitud.
- Q4: filtro de documentos.
- Q5: historial de titulares.
- Q6: versiones.
- Q7: bitácora con su detalle.
- Q8: abonados con tipo PENDIENTE.
- Q9: último respaldo.
- Q10: documentos por persona.
- **Q11: posibles duplicados de persona** (nueva).

## Pendientes

- **Obs. 8 (Anexo B como lista de cambios aceptada).** Actualizar los otros artefactos:
  - **Modelos UML v1.1:** Persona con UQ y fusión; RegistroModificacion como composición 1..*; DIMEX/PASAPORTE; Grupo 2..* sin NINGUNA; regla EXCLUDE.
  - **DAS v1.2:** corregir la cita UML (v1.0 hasta que exista la v1.1) y la sección 9.
  - **DFD:** agregar D4 Cuentas y D5 Bitácora.
  - **ERS:** acciones de RF-15.
  - **Fecha de entrega: por acordar con el docente.**
- **Anexo C:** 16 preguntas para la administradora. Las nuevas son la 15 (DIMEX/pasaporte) y la 16 (revisión de duplicados). La 1 cubre la paja reutilizada: si se confirma, la UQ de numero_paja pasa a ser parcial solo para ACTIVO.
- **Avance de Construcción (06/11):** script DDL con todo lo anterior, más el prototipo de la rebanada CU-04 (Sala 2: Mariangel y Kendall).
- **Conflicto previo:** en clase se usaron Java + MySQL y la tabla `expediente`. El docente aprobó PostgreSQL 17 y el modelo usa `abonado` con PK sustituta id_abonado y numero_paja UQ. Falta alinear los contratos de las parejas con el modelo.

## Archivos

- Modelo_ER_Relacional_SIGEDA_v1.1.docx / .pdf (53 pp.), con el Anexo D, que mapea las 19 observaciones a las secciones corregidas.
- Fuentes_Diagramas_ER_SIGEDA_v1.1.zip: .dot, .svg y .png de las 8 figuras y 7 leyendas, más figs.py.
