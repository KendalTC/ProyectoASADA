# Contexto completo del proyecto — SIGEDA (Acueducto Bodegas y Pilas)

Documento de contexto generado para retomar el trabajo en un chat nuevo sin perder el hilo. Resume todo lo trabajado en esta conversación: entrevista, revisión del Documento de Visión, reunión de validación, evolución del ERS con las correcciones del profesor, y los diagramas UML entregados. Todos los documentos mencionados están guardados en el Proyecto de Claude **"Analisis y Diseño de Sistemas"** (carpeta `claude/` para los generados en esta conversación) y/o fueron entregados como archivos descargables en el chat.

## 1. Datos del proyecto

- **Curso:** IF6100 — Análisis y Diseño de Sistemas, II Ciclo 2026, Grupo 02. Universidad de Costa Rica, Sede de Occidente, Recinto de Grecia, Carrera de Informática Empresarial.
- **Profesor:** Mag. James Mc Intosh Molina.
- **Equipo:** Mariangel Arias Alfaro (C4C688), Alejandro Arias Rojas (C4C759), Sebastián Alfaro Arias (C4C212), Kendal Trejos Cubero (C4K374) — este último es el usuario de esta conversación (tckendall7@gmail.com).
- **Organización analizada:** ASADA Acueducto Bodegas y Pilas (Asociación Administradora de Sistemas de Acueductos y Alcantarillados Comunales). Cobertura: Bodegas, Pilas, Calle Cerro, Calle Central, Trapiche (y "Tacares norte", dato pendiente de confirmar con la ASADA — ver sección 3).
- **Sistema propuesto:** **SIGEDA** (Sistema de Gestión Documental del Acueducto). Digitaliza, organiza y permite consultar los expedientes de los 1,015 abonados, sustituyendo el archivo físico actual. **No cubre** facturación (queda en SADA), mantenimiento/averías ni conexiones nuevas.
- **Ruta de entregables del curso (según se ha trabajado):** Documento de Visión → ERS (Especificación de Requerimientos de Software) → Modelos UML (casos de uso, clases, secuencia, componentes) → Modelo de Diseño (semana 11, aún no iniciado).

## 2. Entrevista de elicitación inicial (28/08/2026)

Entrevistada: la administradora del Acueducto, 4 años en el puesto. Notas guardadas en `claude/Notas_Entrevista_Asada_Bodegas_y_Pilas.md`.

Hechos clave levantados:
- Fundada el 1/7/1998 (antes comité de la Asociación de Desarrollo). 1,015 abonados, ~3-4 personas por casa.
- Estructura: Asamblea → Junta Directiva (presidente/vicepresidente) → Administración → Cobros; abogado y contador externos; fontanero jefe + ayudante. Junta se reúne 1er y 3er martes de cada mes.
- Facturación con app móvil "SADA" (lee medidores, calcula monto, genera recibo); cobro en efectivo, tarjeta o depósito (no SINPE).
- Mantenimiento: reportes por 5 canales distintos que convergen en el fontanero (24/7); sin registro formal de reparaciones.
- Conexiones nuevas: formulario → Junta Directiva → administración → trámite municipal → obra; depende del ciclo de reuniones de junta.
- **Archivo físico** (foco del proyecto): archivera por sector/apellido, sin estándar; documentos perdidos documentados; sin respaldo (a diferencia de los archivos digitales del acueducto, que sí se respaldan en discos externos). Infraestructura pobre: 1 laptop en mal estado, wifi presente pero descrita como inestable en esta entrevista (dato que se corrigió después, ver sección 4).
- Necesidades expresadas: buscar por nombre/cédula, buscar por fecha, conservar fecha original al modificar, orden cronológico no editable (dicho con incertidumbre).
- Presupuesto: sin presupuesto fijo, pagan Microsoft y antivirus, prefieren pago anual, cifra aproximada mencionada ~US$200 (periodicidad no aclarada en ese momento).

**5 problemas identificados** (candidatos para la propuesta): archivo físico desorganizado y sin respaldo; canales de avería dispersos dependientes de una sola persona; sin trazabilidad de mantenimiento; conexiones nuevas atadas al calendario de junta; sin pago digital moderno. El equipo decidió enfocar todo el proyecto en el **primero** (archivo documental).

Vacíos que quedaron pendientes de esa entrevista (algunos se resolvieron después en la reunión de validación, columna B- del ERS): qué es exactamente SADA, composición exacta del personal ("8 y 4"), contenido exacto de cada expediente, periodicidad del presupuesto, reportes que pide la junta.

## 3. Revisión del Documento de Visión (`claude/Revision_Documento_Vision_Bodegas_y_Pilas.md`)

Se revisó el primer borrador del Documento de Visión (basado en la plantilla oficial `1er_Artefacto_Documento_Vision_Proyecto.docx`) contra la entrevista. Hallazgos principales:

1. **Crítico:** las secciones 7 (Prioridades del proyecto) y 8 (Otros requerimientos del producto) tenían aún el texto de ejemplo de la plantilla sin completar. Se propuso una redacción concreta para ambas (cronograma/características/calidad/recursos como restricciones o metas; estándares de datos personales, requerimientos de hardware/software, mantenibilidad post-curso).
2. **Inconsistencia interna:** la sección 3.3 decía "internet estable" y la sección 5 decía "inestable" — se recomendó unificar con la versión de la entrevista (inestable) y valorar si SIGEDA necesita funcionar offline.
3. **Datos a verificar con la ASADA:** existencia real de un rol "Secretaria del Acueducto" (no mencionado en el organigrama de la entrevista); la cifra de "4 personas" en oficina (vs. "8 en planta + 4 posibles" de la entrevista); la ubicación "Tacares norte" (no mencionada explícitamente en la entrevista); la fecha ambigua "9/1/2026" (se recomendó escribirla en palabras).
4. Detalles menores: fila de "[Agregar término propio]" sin completar en el glosario; nota "(Preguntar: ...)" dejada dentro de una tabla de necesidades en vez de fuera como supuesto; falta de declarar el presupuesto como restricción.

El equipo corrigió estos puntos (ver `Vision_new.md`/`.docx` en el espacio de trabajo): la versión corregida sí unifica "internet inestable" en 3.3 y 5, sí desarrolla las secciones 7 y 8, y usa fecha en palabras. Estos ajustes son la base de la versión 1.1 del Documento de Visión referenciada en el ERS.

## 4. Reunión de validación con la administradora (21/09/2026)

Se preparó `claude/Preguntas_ERS_Reunion_Administradora.md` (guía de preguntas organizadas en 6 bloques: A. Contenido/estructura del expediente, B. Roles/usuarios/permisos, C. Reglas de negocio sobre documentos, D. Digitalización, E. Reportes/indicadores, F. Confirmaciones puntuales de la Visión) y una guía formal (`Guia_Reunion_Administradora_21set2026.docx/.pdf`) para llevar a la reunión.

Las respuestas quedaron documentadas como el **Anexo B (B-01 a B-23)** del ERS v1.2 (ver íntegro en `claude/ERS_Borrador_SIGEDA.md`, sección 7). Puntos más importantes que salieron de esa reunión y que cambiaron el rumbo del proyecto:

- **Conectividad corregida:** el wifi en realidad es estable ("wifi de 30", sin problemas recientes) — contradice lo registrado en la entrevista original; se documentó como corrección explícita (B-03).
- **Documentos obligatorios del expediente, por fin definidos** (B-05): persona física → formulario, cédula, certificación de propiedad, plano legible, contrato; si hay varios derechohabientes o usufructo compartido, cada uno es persona asociada y debe aportar los mismos documentos. Persona jurídica → formulario, personería jurídica, cédula de la persona apoderada, cédula jurídica, contrato, y **al menos uno** de {permiso de construcción vigente, formulario que explique cuándo se construyó y para qué se usa el agua} (grupo de alternativas); fotos del inmueble son complementarias, no obligatorias.
- **Identificación:** solo por nombre y número de paja, no por cédula (B-20). Un abonado puede tener varias personas asociadas a lo largo del tiempo (ej. si el titular fallece) pero es un solo abonado (B-06).
- **Cambio de titular:** la administradora pidió explícitamente que al cambiar de titular no sigan apareciendo varios nombres — solo el vigente en pantallas/búsquedas, historial conservado aparte (B-21).
- **Orden de documentos:** por prioridad de tipo (plano 1, solicitud 2...), no alfabético ni cronológico (B-18) — esto corrigió lo que la entrevista original había sugerido.
- **Versiones:** se conservan todas, nunca se sobrescriben (B-19).
- **Conservación:** 10 años mínimo; dar de baja a un abonado no borra sus documentos; al eliminarse la "prevista" (conexión física, fuera de alcance) el archivo se queda para siempre (B-14).
- **Seguridad/acceso:** dos perfiles (secretaría, administradora) con contraseñas distintas pero **los mismos permisos**; todo cambio queda a nombre de quien lo hizo (B-15). Datos de personas no se entregan a terceros salvo entidad con facultad legal como ARESEP (AyA y la Municipalidad no supervisan ni piden nada) (B-13, B-16). Junta Directiva no usa el sistema directamente, pide información en físico a la administración (B-17).
- **Panel de Estado de Completitud:** validado y bien recibido; además pidió poder nombrar cada documento al subirlo y filtrar por ese nombre (B-22).
- **Formato de cédula:** física 9 dígitos; jurídica anotada como 9 dígitos en la reunión, aunque el equipo asumió en el ERS el formato oficial de 10 dígitos como referencia (S-02) (B-23).

## 5. Evolución del ERS (Especificación de Requerimientos de Software)

Archivo canónico: `claude/ERS_Borrador_SIGEDA.md` (= contenido de `ERS_v1.2_SIGEDA.docx`/`.pdf`, entregados como `ERS_Acueducto_Bodegas_Pilas_v1.2.docx/.pdf`).

**v1.0 (18/09/2026):** versión inicial para revisión del profesor, construida a partir de la Visión 1.1 y de lo que ya se podía llenar sin nueva reunión (propósito, alcance, perspectiva, funciones principales, restricciones, gran parte de los RNF). Se identificó que el ejemplo de la plantilla (RF-01 "registrar lectura de medidor", sobre facturación) estaba fuera de alcance y debía sustituirse por requerimientos propios de gestión documental — advertencia incluida en `Preguntas_ERS_Reunion_Administradora.md`.

**v1.1 (23/09/2026):** completa todas las secciones con las respuestas de la reunión del 21/09/2026: RF-01 a RF-18, RNF-01 a RNF-11, reglas de negocio RN-01 a RN-12, interfaces externas, actores, 14 casos de uso preliminares (CU-01 a CU-14 en ese momento), matriz de trazabilidad, validación de 8 criterios de calidad y los dos anexos (A: entrevista, B: reunión de validación).

**v1.2 (28/09/2026):** incorpora las **correcciones de prioridad 1** que el profesor señaló al revisar la v1.1 (documento de revisión referenciado como «Cambios para la ERS v1.2 de SIGEDA»):
- Se agregan **RF-19 a RF-22**: anular documento (CU-14, separado de la baja/reactivación que pasó a ser CU-12), restablecer contraseña (CU-16), modificar abonado y personas asociadas (CU-15), editar datos de documento (CU-17).
- Se agregan **RNF-12** (pérdida máxima tolerable: 1 día) y **RNF-13** (custodia de la clave de cifrado fuera de la laptop).
- Se separa RF-17/CU-12 (baja y reactivación) de RF-19/CU-14 (anulación de documento), que antes estaban mezclados.
- Se dividió **RN-03 en RN-03a y RN-03b** (documentos obligatorios por tipo de abonado) con sus grupos de alternativas.
- Se corrigieron RF-04, RF-09, RF-13 y RF-14 para evaluar la completitud del expediente contra el **titular vigente** y el **tipo de abonado**, no de forma genérica.
- Se ajustó RF-16 a respaldo **diario** (antes semanal) y a manejar la desconexión del disco externo sin afectar la bitácora (RNF-10/RNF-11).
- Correcciones de forma: apellido del profesor corregido (Mc Intosh), unificación de "abonado" vs. "titular", términos agregados al glosario, cita a IEEE Std 830 / ISO IEC IEEE 29148, corrección de la prueba de RF-14 en la sección 6.1.

**Quedan pendientes las correcciones de prioridad 2 y 3** del documento de revisión del profesor — **no abordadas todavía en la v1.2**. Esto es lo primero a retomar si se continúa trabajando el ERS.

El ERS v1.2 final tiene 22 RF, 13 RNF, 12 RN, 17 casos de uso preliminares (CU-01 a CU-17), matriz de trazabilidad completa contra las 5 necesidades N-01 a N-05 de la Visión, validación contra 8 criterios de calidad (correcto, no ambiguo, completo, consistente, verificable, factible, trazable, priorizado) para cada requerimiento, y los anexos A y B con las notas íntegras de la entrevista y la reunión de validación transcritas.

**Supuestos clave documentados (sección 2.5, S-01 a S-21)** que conviene tener presentes: número de paja como identificador único (S-01); formato de cédulas (S-02); comportamiento del cambio de titular propuesto por el equipo (S-03); no eliminación de documentos nunca (S-04); formato de exportación de SADA (S-05); contrato obligatorio para ambos tipos (S-06); expedientes no digitalizados se consultan en papel (S-07); digitalización con fotocopiadora/impresora, celular debe convertirse (S-08); una sola sesión a la vez (S-09); respaldo diario en disco externo, OneDrive no confirmado (S-10); sistema a la medida, no carpeta compartida (S-11); US$200 solo para costos únicos (S-12); Ley 8968 como referencia, aplicación formal no determinada (S-13); composición del personal no cambia el diseño (S-14); Windows 10/11 64 bits (S-15); ~20 páginas por expediente / ~20,000 páginas totales (S-16); frecuencia de respaldo diaria decidida por el equipo (S-17); Junta Directiva no requiere reportes de SIGEDA (S-18); disponibilidad continua de la laptop y ~1015 abonados (S-19); custodia de la clave de cifrado decidida por el equipo (S-20); tamaño máximo de 10 MB por documento (S-21).

## 6. Modelos UML (trabajo más reciente, ya entregado)

Construidos a partir de los 17 casos de uso y las clases implícitas en el ERS v1.2, siguiendo la plantilla del curso para "Modelos UML" (referencia local: `UML_Plantilla_new.md`, que es la plantilla en blanco del profesor con las 4 secciones esperadas: casos de uso, clases, secuencia, componentes).

**Entregados y guardados en `claude/Diagramas_UML_SIGEDA.md` (resumen) y como archivos descargables:**

1. **Diagrama de Casos de Uso** (`Diagrama_Casos_de_Uso_SIGEDA.png/.puml`): actor general "Usuario del Acueducto" especializado en "Secretaría" y "Administradora" (generalización, ambas con los mismos permisos según el ERS); actor secundario "Reloj del sistema" (dispara CU-11). 17 casos de uso. Relaciones «include»: CU-02 y CU-07 incluyen "Registrar personas asociadas" (RF-03). Relación «extend»: CU-16 (Restablecer contraseña) extiende a CU-01, con punto de extensión "credenciales rechazadas o cuenta bloqueada" (RNF-09).

2. **Diagrama de Clases** (`Diagrama_Clases_SIGEDA.png/.puml`): clasificado en estereotipos de análisis — **Límite** (10 pantallas), **Control** (10 controladores, uno por cada agrupación funcional: autenticación, abonados, importación, documentos, búsqueda, completitud, tipos de documento, bitácora, respaldos, exportación) y **Entidad** (9 clases: Abonado, Persona, Documento, VersionDocumento, TipoDocumento, GrupoDeAlternativas, RegistroBitacora, Respaldo, Cuenta). Relación de composición verificada visualmente: Documento *-- VersionDocumento ("versiones"). Los nombres de operaciones de los controladores se hicieron corresponder uno a uno con los RF/CU del ERS (por ejemplo, ControladorDocumentos.cargarDocumento()/anularDocumento()/editarDatosDocumento() ↔ CU-04/CU-14/CU-17).

3. **Ejemplo resuelto de clases** (`Muestra_Diagrama_Clases.png/.puml`): una versión simplificada centrada solo en CU-04 (Cargar documento) — PantallaCargaDocumento, ControladorDocumentos, Documento, VersionDocumento, TipoDocumento — construida como analogía al "CU-01 ejemplo resuelto" que trae la plantilla del curso, para servir de guía de formato/notación.

**Verificación hecha antes de entregar:** se revisaron los tres `.puml` fuente para confirmar consistencia de nombres entre el diagrama de casos de uso y el de clases, y se generó un recorte (`crop_composition.png`) para confirmar visualmente que el símbolo de composición (rombo relleno) se renderizaba correctamente en Documento *-- VersionDocumento.

**Pendiente según la plantilla del curso (sección 3 y 4 de `UML_Plantilla_new.md`), aún NO elaborado:**
- Diagrama de secuencia (mínimo 1 caso de uso crítico) con su descripción textual paso a paso.
- Diagrama de componentes de la arquitectura propuesta, con interfaces provistas/requeridas y justificación de la organización en capas.
- Especificación textual completa (tabla ID/Actor/Flujo básico/alternativo/excepción/Postcondiciones) para al menos 3 casos de uso — el ERS solo tiene la tabla resumen de CU, no las fichas completas que pide la sección 1.3 de la plantilla UML.
- Matriz de trazabilidad específica del entregable UML (RF ↔ CU ↔ Clases ↔ Diagrama de secuencia), distinta de la matriz de trazabilidad del ERS.

## 7. Archivos de referencia del curso (subidos por el usuario, sin modificar por Claude)

Guías y plantillas oficiales del profesor, usadas como fuente de estructura pero no editadas en este chat: `1_Guía_Propuesta_Proyecto_ASADA_Plantilla.docx`, `2_Guia_Docente_Propuesta_Proyecto.docx`, `3_Guia_Estudiantes_Elicitacion_ASADA.docx`, `4_Checklist_Propuesta_Proyecto.docx`, `5_RESUMEN_Propuesta_Proyecto_ASADA.docx`, `6_Referencia_Rapida_Profesor.docx`, `Propuesta_Proyecto_ASADA.docx`, `1er_Artefacto_Documento_Vision_Proyecto.docx`, `Actividad_Roleplay_Elicitacion_ASADA.docx`, materiales de sesión (`IF6100_Sesion01_*.html`, `Semana3_IF6100.html`, `canvas_semana2_IF6100.html`, `IF6100_ClaseVirtual_SodaLaEsquina.html`), y los PDF `IF6100_Analisis_Diseno_De_Sistemas_II_2026.pdf`, `IF6100_Actividad_Requerimiento_a_Ciegas.pdf`, `Plantilla_Ishikawa_Semana3.pdf`.

## 8. Estado actual y próximos pasos sugeridos

**Ya entregado y guardado:**
- Notas de entrevista, revisión de la Visión, preguntas para la reunión, guía de reunión.
- ERS v1.2 completo (.md/.docx/.pdf) con correcciones de prioridad 1 del profesor aplicadas.
- 3 diagramas UML (casos de uso, clases, ejemplo resuelto de clases), verificados consistentes entre sí y con el ERS.

**Pendiente, en orden sugerido de retomar:**
1. Aplicar al ERS las **correcciones de prioridad 2 y 3** del profesor que quedaron fuera de la v1.2 (revisar el documento de revisión del profesor para identificarlas puntualmente; no quedó el detalle línea por línea en el contexto recuperado, solo la mención de que existen y no se abordaron).
2. Completar la **especificación textual de al menos 3 casos de uso** en el formato de la plantilla UML (ID, actor, flujo básico/alternativo/excepción, pre/postcondiciones) — el ejemplo ya resuelto en la plantilla es CU-01 de la plantilla genérica; para SIGEDA convendría desarrollar, por ejemplo, CU-04 (Cargar documento), CU-05 (Buscar expediente) y CU-07 (Cambiar titular) u otros que el equipo considere críticos.
3. Construir el **diagrama de secuencia** para el caso de uso crítico elegido (candidato natural: CU-04 Cargar documento, que ya tiene el ejemplo de clases simplificado).
4. Construir el **diagrama de componentes** con la arquitectura en capas (presentación/negocio/datos) y sus interfaces.
5. Completar la matriz de trazabilidad y el checklist de autoevaluación del entregable UML (`UML_Plantilla_new.md`, secciones 6 y 7).
6. Verificar y cerrar los datos que la revisión de la Visión dejó como pendientes de confirmar con la ASADA (rol de "Secretaría" — parcialmente resuelto en la reunión de validación B-04, que sí la valida como primera usuaria; "Tacares norte"; periodicidad exacta del presupuesto de ~US$200).

---
*Documento generado el 30/09/2026 a partir de los archivos guardados en el Proyecto "Analisis y Diseño de Sistemas" y en el espacio de trabajo de la sesión. Úsalo para dar contexto a un chat nuevo: basta con adjuntarlo o pegarlo al inicio de la conversación.*
