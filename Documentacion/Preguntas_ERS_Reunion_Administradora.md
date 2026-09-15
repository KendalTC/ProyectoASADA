# Preguntas y dudas para la reunión con la administradora — ERS de SIGEDA

**Contexto:** el archivo `ERS_Acueducto_Bodegas_Pilas.docx` que subiste es la plantilla del curso prácticamente en blanco (todas las secciones están marcadas `[COMPLETAR]`, incluyendo la fila de ejemplo RF-01 sobre "registrar lectura de medidor", que es solo el ejemplo genérico de la plantilla). Así que este documento no es todavía una revisión de contenido propio, sino un mapa de qué información les falta reunir antes de poder llenarlo con datos reales de Bodegas y Pilas — que es justo lo que pediste.

Un aviso antes de las preguntas: el ejemplo RF-01 de la plantilla ("registrar lectura de medidor") es sobre facturación, un proceso que el Documento de Visión excluyó explícitamente del alcance de SIGEDA (sección 1.2: "No cubre... facturación, mantenimiento/reportes de averías o gestión de conexiones nuevas"). No editen ese ejemplo — bórrenlo y escriban requerimientos propios de gestión documental, o el ERS quedaría inconsistente con la Visión.

## Lo que ya se puede llenar sin nueva reunión

Varias secciones del ERS se pueden completar directamente adaptando el Documento de Visión y las notas de la entrevista del 2 de septiembre, sin necesitar más información de la administradora: 1.1 Propósito, 1.2 Alcance del producto, 2.1 Perspectiva del producto, 2.2 Funciones principales (a partir de las tres capacidades de la sección 4.2 de la Visión), 2.4 Restricciones, y buena parte de 3.2 Requerimientos no funcionales (usabilidad, confiabilidad, desempeño y soportabilidad ya están descritos en la sección 6 de la Visión, solo falta convertirlos en criterios de aceptación verificables). Vale la pena resolver eso primero para que la reunión se enfoque solo en lo que realmente hace falta.

## Preguntas para la reunión, organizadas por tema

### A. Contenido y estructura del expediente
*(bloquea: 1.3 Definiciones, 3.1 Requerimientos funcionales, 3.3 Reglas de negocio, el "Panel de Estado de Completitud" de la Visión)*

- ¿Cuáles documentos son obligatorios para considerar un expediente "completo"? Esta pregunta ya había quedado pendiente desde la entrevista original y es la que más bloquea el ERS: sin esta lista no se puede definir ni el requerimiento de carga de documentos ni la regla de completitud del panel de estado.
- ¿Existen documentos que varíen según el tipo de abonado (por ejemplo, residencial vs. comercial), o la estructura del expediente es igual para los 1,015?
- ¿Usan internamente algún número o código de abonado (por ejemplo, el que asigna el sistema SADA de facturación), o hoy identifican a cada persona solo por nombre y cédula? Esto afecta si SIGEDA debe buscar/filtrar también por ese número para que se pueda cruzar con la información de facturación más adelante.

### B. Roles, usuarios y permisos
*(bloquea: 2.3 Características de los usuarios, 4.1 Actores, 3.2.5 Seguridad, 3.3 Reglas de negocio)*

- ¿Existe en la práctica un puesto de "secretaria" distinto al de "cobros" que aparece en el organigrama de la entrevista? Si existe, ¿qué debería poder hacer en el sistema frente a lo que puede hacer la administradora (ver también todo, o solo cargar/consultar)?
- ¿La junta directiva necesita consultar expedientes directamente en el sistema, o siempre lo solicita a través de la administradora? Esto define si la junta es un actor del sistema o solo un interesado.
- ¿Debería el sistema tener un usuario y contraseña por persona, o basta con un solo acceso compartido en la computadora de la oficina?
- Retomar la duda que quedó abierta desde la entrevista: los "8 en planta" — ¿quiénes son exactamente y cuáles de ellos usarían este sistema en particular (más allá de la administradora)?

### C. Reglas de negocio sobre el manejo de los documentos
*(bloquea: 3.3 Reglas de negocio, el atributo de Confiabilidad de la Visión)*

- La administradora mencionó, sin estar segura, que el orden de guardado debería ser cronológico y no editable manualmente por ella — ¿se puede confirmar esta regla directamente con ella?
- Si se sube una versión nueva de un documento (por ejemplo, un contrato actualizado), ¿debe reemplazar al anterior, guardarse como una versión adicional conservando el historial completo, o no debería poder modificarse una vez cargado?
- ¿Qué pasa con el expediente de un abonado que se da de baja del servicio? ¿Se conserva indefinidamente, se archiva aparte, o se elimina después de cierto tiempo?

### D. Digitalización de los expedientes existentes
*(bloquea: 2.5 Supuestos y dependencias, requerimientos funcionales de carga/migración, la restricción de la Visión sobre digitación progresiva)*

- ¿Cuentan con un escáner en la oficina, o la digitalización se haría con fotografías de celular? Esto no quedó registrado en la entrevista y cambia bastante el diseño de la función de carga de documentos.
- ¿En qué formato preferirían conservar los documentos (PDF, imagen, ambos)?
- ¿Hay alguna meta o plazo interno de la ASADA para terminar de digitalizar los 1,015 expedientes, o queda completamente a su ritmo?

### E. Reportes e indicadores

- Retomar otra pregunta pendiente de la entrevista: ¿la junta directiva pide regularmente algún reporte o indicador relacionado con los abonados o sus expedientes que hoy sea difícil de generar? Si existe, sería un requerimiento funcional más a documentar en 3.1.

### F. Confirmaciones puntuales que quedaron abiertas desde el Documento de Visión

- Confirmar si "Tacares norte" es correcto como parte de la ubicación/cobertura del Acueducto.
- Confirmar el presupuesto real disponible (~$200 mencionado en la entrevista, sin quedar claro si es mensual, anual o un techo único), ya que condiciona si el sistema puede apoyarse en alguna herramienta con costo (hosting, licencia) o debe ser gratuito.
- Confirmar si la ASADA tiene alguna política interna sobre el manejo de cédulas y datos personales de los abonados, o si esperan que el equipo proponga una como parte del proyecto.

## Sugerencia de orden para la reunión

Si el tiempo con la administradora es limitado, los temas A, B y C son los que más bloquean el contenido central del ERS (sección 3, la más importante según la propia plantilla) y conviene cubrirlos primero. D y E son necesarios pero más rápidos de resolver. F son confirmaciones puntuales que también podrían resolverse por correo o WhatsApp si no alcanza el tiempo en la reunión, tal como ya sugería la validación de la entrevista original.
