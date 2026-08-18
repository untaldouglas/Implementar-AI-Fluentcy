# _PLANTILLA — KPI de Valor por Coordinación (E8)

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Entregable:** E8 — Métricas de impacto en valor de negocio · **Decisión:** D7
**Uso:** copia pre-llenada para la coordinación **Desarrollo**. Confirmar KPI y responsables en D7 (reunión de planificación F2) y actualizar en cada medición.
**Regla E8 (del plan de cohorte):** el informe de métricas + actualizaciones sugeridas se presenta ANTES de modificar o crear contenido nuevo.

> **Principio del artículo de Naidoo (Wits, 08/2026):** las métricas del piloto engañan ("las demostraciones son impresionantes, los ejecutivos quedan tranquilos"). Lo que justifica escalar es el valor de negocio medido con datos reales, antes y después — no entregables completados. Esta plantilla convierte eso en un número.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Coordinación | **Desarrollo** |
| Responsable de medir | Stephanie Miranda (symirandav@ujmd.edu.sv) |
| Participante(s) vinculado(s) | Stephanie Miranda (coordinadora) · Oscar Alfaro (Desarrollo) |
| Fecha de creación | 2026-08-18 (copia pre-llenada para D7) |
| Fecha de línea base (medición ANTES) | [PENDIENTE — semana 1–2 de F2] |
| Fecha de medición DESPUÉS | [PENDIENTE — cierre F2 / Demo Day] |
| Estado | 🟡 línea base por medir |

---

## 2. KPI elegido

| Campo | Valor |
|---|---|
| KPI | Horas de refactor de código legacy (por entregable) *(candidato sugerido — confirmar en D7)* |
| Definición operativa (qué se cuenta exactamente) | Horas-persona invertidas en refactorizar un entregable de código legacy (misma tarea de F1: `refactor-csharp-4`) |
| Unidad | horas/entregable |
| Fórmula | suma(horas invertidas en refactor) / nº de entregables |
| Fuente de datos | Git (commits) + registro de horas |
| Meta del ciclo F2 | −30% vs. línea base |

---

## 3. Medición ANTES (línea base — proceso actual, sin Hermes)

> Regla: mínimo 5 muestras o 2 semanas de datos reales, lo que ocurra primero. Evidencia real, no estimaciones verbales.

| # | Muestra | Fecha | Valor medido | Evidencia (link Drive / captura) |
|---|---|---|---|---|
| 1 | [describir caso] | [fecha] | [valor] | [link] |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Línea base calculada:** [valor promedio] · [fecha] · Medido por [nombre]

---

## 4. Medición DESPUÉS (con Hermes / productos del programa)

| # | Muestra | Fecha | Valor medido | Evidencia (link Drive / captura) |
|---|---|---|---|---|
| 1 | [describir caso] | [fecha] | [valor] | [link] |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

---

## 5. Resultado y valor de negocio

| Campo | Valor |
|---|---|
| Valor DESPUÉS (promedio) | [valor] |
| Delta vs. línea base | [valor absoluto y % — ej.: −1.2 h (−28%)] |
| ¿Cumple la meta del ciclo? | [✅ / ❌ / parcial] |
| Tiempo invertido en medir | [horas — costo de la medición] |
| Valor monetario aproximado (si aplica) | [ej.: horas recuperadas × costo/hora] |
| Actualización sugerida (E8) | [qué cambiar/crear en el contenido, producto o proceso con este dato — se presenta ANTES de ejecutar] |

**Veredicto del validador (Champion F1) con rúbrica:** [Conforme / No conforme] · [nombre] · [fecha]
**Co-firma Douglas:** [✅ / pendiente] · [fecha]

---

## 6. Catálogo de KPIs candidatos por coordinación (elegir 1 para el ciclo)

> La agenda de planificación F2 sugiere: "tiempo de ticket · horas de refactor · disponibilidad · altas/bajas AD". Ampliado aquí por coordinación. La línea base se mide SIEMPRE con la plantilla de proceso medido (C19 de F1: `_PLANTILLA_C19_Proceso_Medido`).

| Coordinación | KPI candidato | Unidad | Fuente de datos típica |
|---|---|---|---|
| Infraestructura | Tiempo de alta/baja de cuentas AD | minutos/caso | AD · registro manual |
| Infraestructura | Disponibilidad de servicios críticos | % uptime | monitoreo (ej.: dashboard de Patrick) |
| Infraestructura | Tiempo de diagnóstico/atención de incidentes de red/servidores | horas/incidente | mesa de ayuda · bitácora |
| Desarrollo | Horas de refactor de código legacy (por entregable) | horas | Git · estimación + registro |
| Desarrollo | Tiempo de generación de reportes (ej.: reportería mensual Workspace) | minutos/reporte | Google Workspace |
| Desarrollo | Tiempo de despliegue / preparación de ambientes | horas | CI/CD · registro |
| Sistemas | Tiempo de resolución de ticket (apertura → cierre) | horas/ticket | ERPNext (mesa de ayuda) |
| Sistemas | Tiempo de preparación de reportería para la Dirección | horas/reporte | ERPNext · Sheets |
| Sistemas | % de tickets con documentación completa al cierre | % | ERPNext · registro |
| Cualquier | Tiempo total medido con C19 (proceso completo sistematizado con Hermes) | horas/proceso | plantilla C19 de F1 |

---

## 7. Quién mide y con qué frecuencia (se acuerda en D7)

| Campo | Acuerdo |
|---|---|
| Quién mide la línea base | [se acuerda en D7] |
| Quién mide el después | [se acuerda en D7] |
| Frecuencia de medición | [se acuerda en D7] |
| Dónde se registra | [tablero del programa · este archivo · informe E8] |
| Cuándo se revisa con Douglas | [PENDIENTE — definido en D2] |
| Cuándo se presenta ante la Dirección | [Demo Day F2 — fecha PENDIENTE] |

---

## 8. Checklist de cierre del ciclo

- [ ] Línea base medida con evidencia real (≥5 muestras o 2 semanas)
- [ ] Medición después completada con misma metodología
- [ ] Delta calculado y documentado (sección 5)
- [ ] Actualización sugerida presentada ANTES de modificar/crear contenido (regla E8)
- [ ] Validado por Champion F1 con rúbrica
- [ ] Co-firmado por Douglas
- [ ] Registrado en el informe de métricas E8 (entregable del cohorte)

---

## 9. Glosario del programa (para participantes F2)

> Describe lo que se está implementando. Leer antes de llenar esta plantilla; en la reunión de planificación se resuelven dudas.

| Término | Qué es |
|---|---|
| **MCA (Modelo de Conducción AI)** | Marco del programa: la IA se aprende como conducir, en niveles progresivos L0–L9 con licencias que certifican competencia demostrada. |
| **Niveles L0–L9** | Escala de competencia: de chat básico (L0, "Taxi") a orquestación multiagente (L9, "Flota Logística"). |
| **Licencia** | Certificación por nivel de competencia, con evidencia real y no verbal: Permiso 🟤 · Básica 🟢 · Profesional 🔵 · Avanzada 🟣. |
| **Champion F1** | Participante del piloto ya certificado (Mario, Irvin, Patrick). En F2 actúan como facilitadores y validadores de evidencia. |
| **Coordinación** | Área de la Dirección a la que pertenece cada participante: Infraestructura · Desarrollo · Sistemas. |
| **Baseline** | Diagnóstico inicial (Google Form) que mide el nivel de partida de cada participante antes del kickoff. |
| **Itinerario** | Ruta de aprendizaje individual definida según el resultado del baseline (no hay ruta única). |
| **Hermes Agent** | Orquestador de IA del programa (Nous Research): la herramienta que cada participante configura y usa en su trabajo real. |
| **SOUL.md** | Archivo de configuración del agente por puesto/área: disparadores de rol, reglas de manejo de datos y skills esperadas. |
| **Skill** | Procedimiento probado y versionado en Git que el agente ejecuta (ej.: `refactor-csharp-4`, `custom-netmon-dashboard`, `diagnostico-baterias-laptops`). |
| **MCP** | Protocolo que conecta al agente con sistemas corporativos (ERPNext, Google Workspace, AD…) para operar sobre datos reales (entregable E5). |
| **Gateway Bifrost** | Punto único de consumo de LLM credits (E6): permite medir cuánto consume cada persona y controlar el presupuesto (E7, $200/mes). |
| **LLM credits** | Unidades de consumo de los modelos de IA; se presupuestan y se miden con el gateway. |
| **Evidencia real** | Entregable verificable (documento, captura, medición, commit). Regla del programa: lo verbal no cuenta. |
| **Rúbrica** | Criterios de validación contra los que se revisa la evidencia. |
| **Drive Approvals** | Flujo de aprobación en Google Drive: el Champion F1 valida con rúbrica y Douglas co-firma. |
| **KPI** | Indicador de valor de negocio elegido por coordinación (E8): mide el impacto real del uso de IA en la operación. |
| **Línea base** | Medición ANTES de usar IA (proceso actual). El DESPUÉS se compara contra ella para calcular el delta. |
| **Delta** | Diferencia entre el después y el antes (ej.: −1.2 h = −28%): el número que se presenta en el Demo Day F2. |
| **C19 (F1)** | Plantilla del piloto para medir un proceso antes/después con evidencia: la metodología base de esta plantilla KPI. |
| **E1–E8** | Entregables del cohorte F2 (ver plan de cohorte). E8 = métricas de valor de negocio, que este documento materializa. |
| **Demo Day F2** | Evento de cierre donde cada coordinación presenta sus KPIs y deltas ante la Dirección. |
| **ERPNext** | Sistema de gestión de Issues/Tasks de la DSI: fuente de datos típica de los KPIs de Sistemas. |
| **AD (Active Directory)** | Directorio de cuentas corporativas: fuente de datos típica de los KPIs de Infraestructura. |
| **Uptime** | Porcentaje de tiempo en que un servicio está disponible: KPI típico de Infraestructura. |

---

*Plantilla E8 · Piloto AI Fluency UJMD · Sesión 26 (14/08/2026) · una copia por coordinación*
