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

## 2. Participantes (6 nuevos — definidos por Douglas 14/08)

| # | Nombre | Coordinación | Rol | Baseline | Meta |
|---|---|---|---|---|---|
| 1 | Luis Molina | Infraestructura | Participante (coordinador) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |
| 2 | Stephanie Miranda | Desarrollo | Participante (coordinadora) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |
| 3 | Jorge Siguenza | Sistemas | Participante (coordinador) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |
| 4 | Betty | Sistemas | Participante (nueva) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |
| 5 | [Por confirmar] | Sistemas | Participante (nueva) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |
| 6 | [Por confirmar] | Desarrollo | Participante (nueva) | [PENDIENTE — baseline] | [PENDIENTE — baseline] |

**Facilitadores/validadores (Champions F1):**

| Rol | Nombre | Licencia | Qué valida |
|---|---|---|---|
| Facilitador + co-facilitación rotativa (R9) | Mario, Irvin, Patrick | 🔵 Profesional (L4–L5) | Sesiones, acompañamiento |
| Validador (con rúbrica) | Mario, Irvin, Patrick | 🔵 Profesional | Evidencia de Básica — Douglas co-firma (solo este primer ejercicio) |
| Instructor | Douglas | 🏆 L8 | Profesional y superiores |

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
| F0 | Planificación del cohorte (este documento) | Próximos 7 días hábiles | 🟡 |
| F1 | Selección + diagnóstico baseline (Google Form) + análisis de respuestas → itinerarios | Tras F0 | ⬜ |
| F2 | Setup: instalación Hermes, SOUL por área, **repo del equipo creado desde el día 1** (E2) | Tras F1 | ⬜ |
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

> Pendiente: consolidar la matriz de retrospectiva de F1 (vence 14/08 17:00) y copiar aquí sus lecciones ANTES de diseñar sesiones de F2.

- [Se completará con la retrospectiva de F1]
- [Se completará con la retrospectiva de F1]

---

*Aprobado por Sponsor: _______________  Fecha: ______________*
