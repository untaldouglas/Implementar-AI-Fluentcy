# Matriz estándar de instrucciones para entregables — Fase 2

## Propósito y alcance

Esta matriz consolida las seis guías personalizadas de 14 días de Fase 2:

- Luis Molina — Infraestructura y Seguridad Informática.
- Jorge López — Sistemas y Operaciones.
- Stephanie Miranda — Desarrollo y Mantenimiento de Sistemas.
- Betty Figueroa — Asistencia a la Dirección y Mesa de Servicio.
- Bryan Gómez — Soporte Técnico y Mesa de Servicio.
- Oscar Alfaro — Desarrollo y documentación técnica.

El estándar aplica a todos los participantes. La personalización se hace únicamente en el **caso real**, el proceso medido, el tipo de documento y el facilitador. No se deben cambiar los requisitos de evidencia, seguridad, validación ni trazabilidad.

## Reglas transversales obligatorias

1. Trabajar únicamente con información autorizada. Anonimizar nombres, correos, identificadores, credenciales, datos personales, incidentes y cualquier información restringida.
2. Registrar el prompt utilizado, la herramienta, la fecha, el resultado obtenido y las modificaciones hechas por la persona participante.
3. La IA propone o redacta; la persona participante verifica, corrige y aprueba el contenido antes de entregarlo.
4. Guardar cada evidencia en la carpeta del participante dentro de `F2_02_Evidencia_Participantes/<Participante>/`.
5. Usar nombres de archivo trazables: `F2_<participante>_D<dd>_<entregable>_<vN>.<ext>`.
6. Compartir el documento con el facilitador como comentarista. El estado **Aprobado** requiere validación del facilitador y co-firma de Douglas.
7. Si una evidencia contiene datos sensibles, conservar solo una versión anonimizada para revisión y registrar dónde queda la versión restringida, sin incluirla en esta carpeta.

## Matriz de entregables diarios

| ID | Momento / propósito | Instrucción estándar precisa | Producto mínimo que se entrega | Evidencia y trazabilidad | Criterio de aceptación | Valida |
|---|---|---|---|---|---|---|
| D1 | Prompt estructurado | Selecciona una tarea real no sensible del puesto. Ejecuta en Gemini: (a) un prompt libre, (b) un prompt con **rol + tarea + contexto + formato + criterio de calidad** y (c) tu propio prompt. Compara los resultados. | Documento con los 3 prompts, sus respuestas y una comparación breve. | Respuesta A, respuesta B, prompt propio, fecha y herramienta. | Se observa diferencia entre A y B; el prompt propio es aplicable al puesto, no contiene datos sensibles y define un resultado verificable. | Facilitador |
| D2 | Productividad con prompts reales | Diseña y ejecuta 3 prompts sobre tareas frecuentes del puesto. Personalízalos con datos ficticios o anonimizados. Elige el mejor resultado y explica por qué. | Google Doc con 3 prompts ejecutados, 3 respuestas y anotación comparativa. | Prompts completos, respuestas, criterio de selección y fecha. | Los 3 prompts corresponden al puesto, producen respuestas utilizables y la comparación identifica fortalezas, límites y ajustes. | Facilitador |
| D3 | Contexto y memoria | Retoma el chat del D2. Añade contexto nuevo, solicita una mejora concreta y verifica si la respuesta cambia de forma pertinente. Pide además un resumen de una instrucción larga. | Registro de la conversación retomada y nota de qué contexto mejoró el resultado. | Captura o enlace al chat, prompt de mejora, respuesta antes/después y nota de aprendizaje. | Se demuestra continuidad de contexto y se distingue entre contexto útil, ambiguo y no autorizado. | Facilitador |
| D4 | Refinamiento iterativo | Toma un borrador del D1–D3 y aplica al menos 3 refinamientos en cadena: estructura, extensión, tono, precisión, formato o audiencia. Conserva la versión inicial y la final. | Documento final refinado más registro de los 3 cambios. | Versión inicial, versión final, prompts de refinamiento y tiempo invertido. | La versión final mejora de manera visible; cada cambio tiene una razón y la persona participante verificó el contenido. | Facilitador |
| D5 | Lectura segura de archivos / L2 | Selecciona un documento real no sensible del área. En Gemini, solicita: (a) resumen en 5 puntos y (b) acciones concretas. Clasifica qué tipo de archivo puede compartirse y cuál no. | Ficha de análisis del documento y resumen generado. | Nombre no sensible del archivo, resumen, acciones, clasificación y justificación de acceso. | El archivo es autorizado; el resumen es fiel; las acciones son distinguibles de los hechos; la clasificación respeta ISO/IEC 27001 y política institucional. | Facilitador |
| D6 | Clasificación de activos de información | Crea una tabla con al menos 6 activos o tipos de información del puesto. Para cada fila registra: activo, uso, propietario, clasificación, riesgo, herramienta permitida y control requerido. | Google Doc con tabla completa de clasificación. | Tabla, fuente/política consultada y fecha de revisión. | Contiene ≥6 filas propias del puesto, clasificación razonada, riesgos identificados y regla clara de qué nunca debe enviarse a una IA externa. | Facilitador |
| D7 | Caso real de Semana 1 | Elige un documento o procedimiento que realmente necesites producir. Redáctalo con Gemini usando rol + tarea + contexto; refínalo al menos 2 veces; revísalo manualmente y registra el proceso. | Documento final del caso real y bitácora de elaboración. | Prompt inicial, refinamientos, versión final, tiempo invertido y desperdicios LEAN observados. | El documento es útil para el puesto, está revisado por la persona, no expone datos sensibles y conserva trazabilidad completa del proceso. | Facilitador |
| D8 | Revisión y decisión de Semana 2 | Presenta D1–D7 al facilitador. Registra acuerdos, correcciones y pendientes. Define con el facilitador un caso real medible para Semana 2. | Nota de revisión y ficha del caso real de Semana 2. | Fecha, participantes, acuerdos, ajustes, responsable y caso elegido. | La revisión tiene decisiones concretas; el caso tiene alcance, resultado esperado, proceso medible y autorización para usar la información. | Facilitador + participante |
| D9 | Marco de operación y control | Elige una práctica del área. Solicita a Gemini una descripción con roles y pasos y conviértela en una matriz RACI según COBIT; cuando aplique, relaciona ITIL, agile/SCRUM o PRINCE2. Evalúa qué aplica a UJMD. | Borrador de práctica, matriz RACI y evaluación de aplicabilidad. | Prompt, respuesta, RACI, supuestos, ajustes realizados y fuentes de marco. | Los roles R/A/C/I no quedan ambiguos; la evaluación separa recomendación de decisión institucional y documenta adaptaciones necesarias. | Facilitador |
| D10 | Línea base y desperdicio LEAN | Identifica 2 procesos repetitivos. Describe pasos, entradas, salidas, responsables, frecuencia y tiempo actual. Marca esperas, reprocesos y tareas manuales. Selecciona 1 proceso para medir. | Plantilla de proceso medido C19/F2 con línea base. | Dos candidatos, desperdicios detectados, proceso elegido, fecha, número de casos y método de medición. | Existen ≥2 candidatos; la línea base es reproducible; el tiempo se mide con una unidad definida y el proceso elegido puede compararse después. | Facilitador |
| D11 | Primer uso de Hermes | Verifica la instalación de Hermes con el facilitador. Ejecuta `hermes chat -q "hola, ¿quién eres?"`. Repite en Hermes un prompt usado en Gemini y compara ambas respuestas. | Registro del primer chat y comparación Gemini vs Hermes. | Captura del chat, comandos, prompt equivalente, respuestas y conclusión. | Se confirma la instalación; la comparación usa la misma tarea y distingue privacidad, contexto, calidad, velocidad y uso recomendado. | Facilitador |
| D12 | Hermes aplicado al caso real | Aplica Hermes al caso real de D8 usando únicamente información autorizada. Solicita una salida concreta y registra cuándo conviene usar Gemini y cuándo Hermes. | Resultado de Hermes y criterio de selección de herramienta. | Prompt, respuesta, archivos consultados sin exponer contenido sensible, decisión Gemini/Hermes y fecha. | La salida es pertinente, la decisión considera seguridad y contexto, y queda claro qué debe revisar una persona antes de usarla. | Facilitador |
| D13 | Mini-proyecto y medición de valor | Define alcance y exclusiones. Desglosa el mini-proyecto en fases, entregables, responsables, tiempos y riesgos. Ejecuta el caso de D10 con IA y mide el tiempo con el mismo método de la línea base. | Plan del mini-proyecto, entregable final y medición antes/después. | Plan, riesgos/mitigaciones, línea base, medición con IA, cálculo del delta y validación del resultado. | Hay alcance claro; todos los entregables tienen responsable; los riesgos tienen mitigación; el delta se calcula con datos comparables y no se atribuye causalidad sin evidencia. | Facilitador + Douglas |
| D14 | Cierre y validación | Escribe la reflexión del ciclo, organiza D1–D13 en Drive, comparte el expediente con el facilitador como comentarista y presenta el caso real y su medición. | Reflexión, expediente completo y acta/registro de validación. | Carpeta ordenada, enlace compartido, comentarios atendidos, aprobación del facilitador y co-firma de Douglas. | No faltan entregables; la reflexión identifica aprendizajes y próximos pasos; el caso es reproducible; la carpeta queda validada. | Facilitador + Douglas |

## Personalización controlada por puesto

| Participante / área | Caso real sugerido por la guía | Variación permitida en D9–D13 |
|---|---|---|
| Luis / Infraestructura y Seguridad | Política o procedimiento de seguridad; caso de infraestructura. | Priorizar clasificación, controles ISO 27001, ITIL/COBIT, permisos, continuidad y riesgo operativo. |
| Jorge / Sistemas y Operaciones | Procedimiento de soporte o gestión; caso de sistemas y operaciones. | Priorizar operación, incidentes/solicitudes, RACI, continuidad y mejora del flujo de atención. |
| Stephanie / Desarrollo y Mantenimiento | Documento de coordinación de desarrollo; caso de desarrollo. | Priorizar agile/SCRUM, cambios ITIL, COBIT, gestión de riesgos y entregas incrementales. |
| Betty / Mesa de Servicio | Guía, plantilla de atención o procedimiento de mesa de servicio. | Priorizar atención, conocimiento, clasificación de datos, respuestas a usuarios y tiempos de servicio. |
| Bryan / Soporte Técnico | Guía o procedimiento de soporte; caso de soporte. | Priorizar incidentes, solicitudes, diagnóstico, escalamiento, base de conocimiento y tiempos de resolución. |
| Oscar / Desarrollo | Documentación técnica o minuta; caso de desarrollo. | Priorizar requisitos, cambios, documentación técnica, sprint/agile, riesgos y trazabilidad. |

## Alineación con los entregables de cohorte E1–E8

| Entregable de cohorte | Evidencia que lo soporta en esta matriz | Estándar de cumplimiento |
|---|---|---|
| E1 — Conocimiento validado | D1–D14, especialmente D6, D7, D9, D10, D13 y D14 | Evidencia real, revisión humana, validación del facilitador y co-firma de Douglas; no basta una explicación verbal. |
| E2 — Profiles, Skills y SOULs | D7, D9, D12 y D13 | Convertir aprendizajes y procedimientos validados en artefactos versionados del área, sin copiar datos sensibles. |
| E3 — Memoria externa a Hermes | D3, D11, D12 y D14 | Registrar qué contexto se conserva, dónde, con qué permisos y cuándo se debe excluir o eliminar. |
| E4 — Gestión de Skills externos | D9, D12, D13 y D14 | Documentar fuente, revisión, adaptación, propietario, versión y criterio de retiro de cada Skill utilizado. |
| E5 — MCP funcional | D9, D12 y D13 | Definir caso de uso, sistema objetivo, permisos mínimos, riesgo, prueba de funcionamiento y responsable operativo. |
| E6 — Gateway Bifrost | D11–D13 | Registrar herramienta/modelo utilizado, costo o consumo cuando esté disponible, control de acceso y resultado de la prueba. |
| E7 — Presupuesto LLM | D10–D13 | Relacionar volumen de uso, tiempo, herramienta y costo estimado con el beneficio observado; separar dato medido de supuesto. |
| E8 — Valor de negocio | D10, D13 y D14 | Reportar línea base, resultado con IA, delta, calidad, riesgos, decisión de adopción y siguiente medición. |

## Criterio de estado

Cada entregable se registra con uno de estos estados:

- **Pendiente:** aún no existe evidencia.
- **En revisión:** la evidencia existe, pero el facilitador solicitó ajustes.
- **Validado:** cumple los criterios y está aprobado por el facilitador.
- **Cofirmado:** además de estar validado, cuenta con la co-firma de Douglas cuando corresponde.

La matriz es el estándar común. Las guías individuales siguen siendo la fuente de ejemplos y contexto específico del puesto.
