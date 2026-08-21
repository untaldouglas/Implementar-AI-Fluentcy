# Plan de Cohorte F2 — Expansión al equipo (Capa 1: Dirección IT)

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Fecha de creación:** 14/08/2026 · **Sponsor/Instructor:** Douglas A. Galindo (L8)
**Capa:** 1 — Dirección IT · **Cohorte anterior:** F1 (referencia congelada en rama `Fase01`)

> **Arranque condicionado al baseline:** la fecha de inicio y los itinerarios individuales se definen DESPUÉS de analizar las respuestas del Google Form baseline de cada nuevo participante. Este documento registra lo definido al 14/08; los campos `[PENDIENTE — baseline]` se completan al cerrar la Fase 1 del ciclo.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Cohorte | F2 — Expansión al equipo |
| Capa | Capa 1 — Dirección IT |
| Estado | 🟡 EN PLANIFICACIÓN (inicio en los próximos 7 días hábiles — planificación, no ejecución) |
| Instructor | Douglas A. Galindo (L8) |
| Validadores (primer ejercicio) | Champions F1 (Mario, Irvin, Patrick — L4–L5) **validan** · Douglas **co-firma** |

## 2. Participantes (6 nuevos — confirmados por Douglas y coordinadores 14/08)

| # | Nombre | Email | Coordinación/Grupo | Rol | Baseline (19/08) | Meta ciclo |
|---|---|---|---|---|---|---|
| 1 | Luis Molina | lamolinaq@ujmd.edu.sv | Infraestructura (Coordinador) | Participante (coordinador) | L1 · Pasajero 🟤 (score 14/50) | L2 — IA lee archivos del área |
| 2 | Stephanie Miranda | symirandav@ujmd.edu.sv | Desarrollo (Coordinadora) | Participante (coordinadora) | L1 · Pasajero 🟤 (score 14/50) | L2 — IA lee archivos del área |
| 3 | Jorge López | jelopezr@ujmd.edu.sv | Sistemas (Coordinador) | Participante (coordinador) | **L2 · Conductor 🟢 (score 18/50)** | L3 — SOUL.md con contexto fijo |
| 4 | **Bryan Gómez** | begomezch@ujmd.edu.sv | **Sistemas** | Participante (nuevo) | L1 · Pasajero 🟤 (score 14/50) | L2 — IA lee archivos del área |
| 5 | **Betty Figueroa** | bcfigueroac@ujmd.edu.sv | **Sistemas → acompañará a Infraestructura** | Participante (nueva) | L1 · Pasajero 🟤 (score 8/50) | L2 — IA lee archivos del área |
| 6 | **Oscar Alfaro** | ojalfarob@ujmd.edu.sv | **Desarrollo** | Participante (nuevo) | L1 · Pasajero 🟤 (score 11/50) | L2 — IA lee archivos del área |

> **Baseline F2 cerrado 6/6 (análisis 19/08):** respuestas recibidas en tiempo (Luis 14/08 · Betty 17/08 · Stephanie 17/08 · Jorge 17/08 · Bryan 17/08 · Oscar 18/08) y consolidadas en `F2_01_Baseline_RESTRINGIDO/Respuestas_Diagnostico_Conduccion_AI` (Drive). Grupo: promedio 16.2/50 · mínimo L1 · máximo L2 · **5 Pasajeros 🟤 + 1 Conductor 🟢** (Jorge, meta L3 con Licencia Básica). Bloqueos del grupo (de más a menos): Acceso/Permisos (10) · Seguridad/Privacidad (9) · Soporte (8) · Conocimiento técnico (7) · Confianza (5) · Cultura (5) · Tiempo (0). Itinerarios individuales generados en la hoja `ITINERARIOS` del mismo spreadsheet. Implicación de planificación: resolver accesos y reglas de datos (qué SÍ/NO subir a IA) temprano en F2 — son los bloqueos nº 1 y nº 2 del grupo, no tiempo ni cultura.

> **Participantes nuevos confirmados por los coordinadores (14/08):** Bryan Gómez (Sistemas) · Betty Figueroa (Sistemas, acompañará al grupo de Infraestructura) · Oscar Alfaro (Desarrollo). Los 3 coordinadores (Luis, Stephanie, Jorge) completan los 6 participantes.

**Facilitadores/validadores (Champions F1) — grupos asignados (confirmado 19/08):**

| Rol | Nombre | Licencia | Grupo que facilita | Qué valida |
|---|---|---|---|---|
| Facilitador | **Irvin Morales** | 🔵 Profesional (L4–L5) | **Jorge + Bryan** (Sistemas/Operaciones y Soporte) | Sesiones, acompañamiento |
| Facilitador | **Patrick Orellana** | 🔵 Profesional | **Luis + Betty** (Infraestructura/Seguridad y Mesa de Servicio) | Sesiones, acompañamiento |
| Facilitador | **Mario Valencia** | 🔵 Profesional | **Stephanie + Oscar** (Desarrollo/Mantenimiento y Programador Analista) | Sesiones, acompañamiento |
| Validador (con rúbrica) | Mario, Irvin, Patrick | 🔵 Profesional | Cada uno valida la evidencia de su grupo | Evidencia de Básica — Douglas co-firma (solo este primer ejercicio) |
| Instructor | Douglas | 🏆 L8 | Todos | Profesional y superiores |

## 3. Entregables del cohorte (definidos por Douglas 14/08)

| # | Entregable | Evidencia de cumplimiento |
|---|---|---|
| E1 | 6 personas nuevas con conocimiento validado para nivel L6 | Rúbrica/evidencia por participante (modelo F1: evidencia real, no verbal) |
| E2 | Profiles, Skills y SOULs por puesto de trabajo de las coordinaciones, creados y gestionados en **Git repository local** | Repo del equipo con `profiles/`, `skills/`, `souls/` por coordinación (consolida R20 de F1) |
| E3 | Herramienta definida para memoria externa a Hermes | Decisión documentada (ADR) + herramienta operativa |
| E4 | Proceso de gestión de Skills externos dentro de la operación | Flujo definido y documentado (ingreso/actualización/calidad) |
| E5 | Al menos 1 MCP funcional para integrar soluciones corporativas (se sugiere 1 MCP por servicio) | MCP operativo conectado a un servicio corporativo |
| E6 | Solución gateway de AI services funcionando (https://github.com/maximhq/bifrost) como punto de consumo de LLM credits | Bifrost operativo y consumiendo créditos |
| E7 | Presupuesto autorizado para consumo administrado de LLM credits — $200 mensuales presupuestados (validar) | Autorización/captura del presupuesto |
| E8 | Métricas de impacto en valor de negocio al usar productos creados en el programa | Informe de métricas + actualizaciones sugeridas ANTES de modificar/crear contenido |

## 4. Cronograma del ciclo

| Fase | Actividad | Ventana | Estado |
|---|---|---|---|
| F0 | Planificación del cohorte (este documento) | 14–18/08 | 🟡 |
| F1 | Selección + diagnóstico baseline (Google Form) — **límite martes 18/08 17:00** + análisis de respuestas → itinerarios | 18–20/08 | 🟡 |
| F2 | **Kickoff F2: viernes 21/08, 14:00–15:15, CC 2 de la Dirección de Informática** (agenda se hará llegar posteriormente) + Setup: instalación Hermes, SOUL por área, repo del equipo creado desde el día 1 (E2) | 21/08 → | ⬜ |
| F3 | Sesiones semanales (cadencia F1: mié 2–4 PM + vie 2–3 PM) | ~8–10 semanas | ⬜ |
| F4 | Verificación continua (Drive Approvals + auditorías de medio ciclo) | Paralela a F3 | ⬜ |
| F5 | Evaluación + cierre (Demo Day F2, actas, sellos) | [PENDIENTE] | ⬜ |
| F6 | Post-cierre: métricas de salida (post-baseline) + métricas de valor (E8) + retrospectiva | Tras F5 | ⬜ |

## 5. Validación (primer ejercicio de transición)

| Criterio | Quién valida | Cómo |
|---|---|---|
| 🟤 Permiso | Facilitador (Champion F1) | Baseline + sesión guiada |
| 🟢 Básica | **Champion F1 valida + Douglas co-firma** | Drive Approvals sobre 2 casos medidos |
| 🔵 Profesional | Instructor (Douglas) | SOUL + Skill + 3 casos + flujo |
| 🟣 Avanzada | Instructor + revisión de repo | Automatización + repo compartido + métricas |

> **Nota:** los 6 participantes nuevos arrancan con meta de conocimiento validado nivel L6 (E1) — la progresión de licencias se asigna según baseline individual. Revisión del esquema de validación al cierre de F2.

## 6. Presupuesto y recursos

| Recurso | Monto / Detalle | Estado |
|---|---|---|
| LLM credits | $200/mes presupuestados | 🟡 VALIDAR (E7) |
| Gateway AI services | Bifrost (maximhq/bifrost) | ⬜ (E6) |
| Memoria externa | [PENDIENTE — evaluar opciones] | ⬜ (E3) |
| MCP corporativo | [PENDIENTE — definir primer servicio] | ⬜ (E5) |

## 7. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Carga operativa de Douglas (inicio de clases 2-2026) retrasa sesiones | Media | Medio | Co-facilitación rotativa de Champions F1 (R9) desde la primera sesión |
| 6 participantes con niveles baseline dispares | Alta | Medio | Itinerarios individuales según análisis del baseline (no ruta única) |
| Validación centralizada → cuello de botella | Media | Alto | Champions F1 validan Básica con rúbrica; Douglas co-firma (esquema transitorio) |
| Costos LLM sin control | Media | Alto | Gateway Bifrost (E6) + presupuesto E7 medido desde el día 1 |

## 8. Lecciones del cohorte anterior (F1 — retrospectiva)

> **Consolidado 18/08/2026** a partir de la matriz de evaluación F1 (3/3 Champions: Mario 14/08, Irvin 14/08, Patrick 17/08). Fuente: Google Sheets `1eABdRc9XaySjjjniA4slSbYEXHMpx2bVZ0adXR7YoNM`, hoja `Evaluación Fase 1`. Resultados: utilidad profesional 4.7/5 · recomendación 3/3 Sí · acompañamiento 4/5 · carga de trabajo 3.3/5 · ~35 h/mes por persona. Estas lecciones se aplican al diseñar sesiones de F2.

| # | Lección de F1 | Evidencia (quién lo dijo) | Aplicación a F2 |
|---|---|---|---|
| L1 | Grabar sesiones con calidad desde el inicio, como material asíncrono de referencia ("es muy beneficioso ver cómo se hacen las cosas que solo leerlo"; "mejorar las grabaciones al inicio, ya después mejoró") | Mario, Patrick | Grabar desde el kickoff con calidad; repositorio de material asíncrono por sesión |
| L2 | Cadencia de entregas quincenal con revisiones intermedias obligatorias, no semanal ("más margen para profundizar en la calidad del trabajo sin la presión de cerrar un entregable final cada pocos días") | Irvin | Entregas quincenales + revisión intermedia obligatoria (insumo para D2) |
| L3 | Setup estandarizado y guiado por el instructor, con checklist de verificación ("que todos sigan y hablen el mismo idioma y no cada quien lo instala a su forma y al final a unos funciona bien y a otros no") | Patrick | Sesión de instalación guiada + verificación de funcionamiento común para los 6 |
| L4 | Material de apoyo y documental claro, con dudas resueltas durante el taller práctico | Irvin | Publicar material documental antes de cada taller; tiempo de dudas en sesión |
| L5 | Planificar cada sesión con duración estimada y apoyo visual ("calcular los tiempos de estudios... qué temas se pueden abordar en cada sesión") | Mario | Agenda de sesión con tiempos y visuales |
| L6 | Mantener el estándar de entregas de mediados de F1 (plantillas-rúbricas) y las actividades aplicadas al trabajo real; las más valoradas fueron C20 (perfil de área) y C21 (skill propio) | Mario, Irvin | Preservar el modelo de evidencia real con rúbrica en F2 |
| L7 | La discusión colectiva entre pares con puntos de vista distintos es un activo de aprendizaje | Patrick | Mantener espacios de discusión grupal en las sesiones |
| L8 | Carga de trabajo reportada ~30–40 h/mes y valorada 3.3/5: no duplicar la carga al duplicar la población | Los 3 | Ajustar cadencia (L2) y expectativas explícitas de dedicación |

## 9. Acuerdos del kickoff F2 (21/08/2026)

> **Reunión ejecutada:** viernes 21/08, 14:00–15:15, CC 2 · acta AI-FLUENCY-2026-002 firmada · reglas de evidencia y datos claras · herramientas informadas (Gemini primeras actividades, Hermes Agent herramienta de trabajo, NotebookLM asistente).

| # | Acuerdo/compromiso | Detalle | Fecha límite | Estado |
|---|---|---|---|---|
| K1 | **Informar días y hora de reuniones por grupo** | Cada grupo (facilitador + sus 2 participantes) informa POR ESCRITO los días y horas de sus reuniones de grupo: Irvin→Jorge+Bryan · Patrick→Luis+Betty · Mario→Stephanie+Oscar | **3 días hábiles: miércoles 26/08/2026** | ⏳ Pendiente |
| K2 | **Uso de recursos de referencia** | Los participantes usarán los recursos de referencia entregados (guías personalizadas 14 días, itinerarios, plan de cohorte, glosario, NotebookLM, materiales Drive) | Continuo | ✅ Aceptado en kickoff |
| K3 | **Dedicación semanal mínima** | Disposición de participar al menos **4 horas semanales estimadas** por participante | Continuo | ✅ Aceptado en kickoff |
| K4 | **Reglas del juego** | Reglas de evidencia real (no verbal) y de datos (qué SÍ/NO subir a la IA) quedaron claras en el kickoff | Continuo | ✅ Comunicadas |
| K5 | **Herramientas informadas** | Gemini (primeras actividades), Hermes Agent (herramienta de trabajo), NotebookLM (asistente de consulta) comunicadas a los 6 | Continuo | ✅ Comunicadas |

**Próximo hito:** recibir K1 (días/horas de reuniones por grupo) → consolidar cronograma definitivo (insumo para D2) → agendar setup guiado de Hermes → primera sesión semanal.

---



*Aprobado por Sponsor: _______________  Fecha: ______________*
