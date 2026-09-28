# Lecciones y Estándares de Diseño de Fases — Programa AI Fluency (MCA)

**Programa AI Fluency · MCA · UJMD — Dirección de Servicios Informáticos**
**Origen:** análisis post-corrección F2 del 28/09/2026 (Módulo A1) — validado por Douglas.
**Alcance:** obligatorio para el diseño de toda fase nueva (F3 en adelante) y aplicable a la operación remanente de F2.
**Instrumentos donde aterriza:** `01_piloto/cohortes/plantilla_plan_cohorte.md` (pre-flight §0), `00_marco/Protocolo_Evidencia_y_Estado.md` (complemento, no reemplazo).

---

## A. Lecciones observadas (con su evidencia)

| # | Lección | Evidencia del programa |
|---|---|---|
| L-01 | El aprendizaje de una herramienta nueva es un **módulo formal** (documento, rúbrica, ventana, entregable) que precede a toda producción de artefactos — nunca implícito ni diferido. | F2 arrancó sin nivelación en Hermes; la producción de SOUL/skills se trabó y obligó al adendum A1 (28/09). |
| L-02 | Reutilizar material ya probado (curaduría) en lugar de crear desde cero hace las correcciones baratas. Solo es posible si las fases anteriores versionan sus artefactos. | A1 se armó con material F1 en horas: glosario consolidado, plantillas C19–C22, 3 SOUL y 3 skills reales aprobados. |
| L-03 | **Rúbrica antes de compromiso** (§4.5): ningún módulo/compromiso se anuncia sin plantilla-rúbrica publicada y ubicación de entrega. | Nació del fallo C18–C20 (julio, compromisos sin plantilla); el 28/09 el gate frenó el adendum de las guías contra una rúbrica inexistente. |
| L-04 | **Documento canónico primero.** Todo módulo nace con su documento único (contenido + links verificados); la comunicación, las guías y la automatización van después. | El comunicado y el cron del 28/09 se prepararon antes de que existiera `modulo_a1_hermes.html` — el Director no encontraba el contenido del módulo. |
| L-05 | Las ventanas de adopción se calculan contra la **carga operativa real del equipo** (semestre, cierres, incidencias), con margen, no contra el calendario del programa. | Ventana inicial de A1 de 1 semana fue corregida a 2 semanas + semana de cierre (decisión del Director). |
| L-06 | **Links verificados** (HTTP real o API) en todo artefacto de comunicación; se declara explícitamente lo que aún no existe. | Comunicado 28/09 con 9 links probados; la rúbrica inexistente se declaró como pendiente, no se inventó URL. |
| L-07 | La evidencia sin verificación documental periódica se acumula como riesgo silencioso. | Corte D01–D10 vencido el 11/09 y sin verificación a 28/09 — el mayor riesgo de F2 no fue pedagógico sino de control. |
| L-08 | Correcciones y rebaselines se registran con entradas nuevas en el log, sin reescribir historia; el estado se declara honesto ("no recibido", "obsoleto") aunque incomode. | Sesiones 33–36 del 28/09; regla vigente desde Protocolo 17/07. |
| L-09 | Los instrumentos nacen en el repo (versionado) y se publican a Drive/Pages desde ahí — evita evidencia "enterrada" y espejos desincronizados. | Julio: evidencia enterrada en carpetas personales; 28/09: documento → commit → Pages → link, sin fricción. |

## B. Estándares de diseño de fase (obligatorios)

1. **Pre-flight de fase** (§0 de la plantilla de cohorte): 1 sesión de 60 min antes de arrancar, que responde con evidencia las 6 preguntas del checklist.
2. **Módulo de nivelación de herramienta** como fase formal del ciclo, con documento canónico, rúbrica, ventana calculada contra carga operativa y entregable propio que alimenta los entregables de cohorte.
3. **Corte documental quincenal** durante la ejecución: el agente cruza la matriz de evidencia contra las rúbricas y reporta brechas (URL faltante, sin validación) — no se espera al cierre de fase.
4. **Escalamiento de validación:** el cohorte valida con rúbrica y el Director audita por muestreo (no co-firma total) — prerrequisito para escalar a Capa 2. Solo aplica cuando el módulo de nivelación haya producido los artefactos base.
5. **Taxonomía única de identificadores:** M# (módulos) · L# (lecciones) · E# (entregables de cohorte) · C# (compromisos) · D# (decisiones) · R# (recomendaciones). Documentar el ID en la primera aparición.
6. **Inventario de reutilización al inicio:** qué artefactos de fases anteriores se reusan, se adaptan o son nuevos — decidido antes de planificar contenido.
7. **Retrospectiva formal al cierre** con matriz de participación (modelo: `Retrospectiva_Champions_Fase1_2026-08`); sus hallazgos entran a `plantilla_plan_cohorte.md` como "lecciones del cohorte anterior".

## C. Checklist pre-flight de cohorte (copiar a cada plan nuevo)

- [ ] ¿Qué herramienta/skill nuevo introduce esta fase y quién lo enseña?
- [ ] ¿Existe el Módulo de nivelación con documento canónico + rúbrica + ventana?
- [ ] ¿Qué material de fases anteriores se reutiliza / adapta / es nuevo? (inventario)
- [ ] ¿Qué ventana real tiene el equipo (semestre, cierres, feriados, carga)?
- [ ] ¿Qué cortes documentales quincenales se programaron y quién los ejecuta?
- [ ] ¿Quién es dueño de cada instrumento (documento, rúbrica, matriz, comunicado)?

## D. Aplicación inmediata en F2 (operación remanente)

| Acción | Cuándo |
|---|---|
| Rúbrica `_PLANTILLA_A1_` en Drive antes del cron del 29/09 8:00 AM | Facilitadores |
| Primer corte documental quincenal: D01–D10 pendientes + entregas A1 (09/10) | 10/10 |
| Verificación documental previa al cierre F2 (16/10): E1–E8 con URL, fecha, responsable | 12/10–16/10 |
| Retrospectiva F2 → lecciones a `plantilla_plan_cohorte.md` | semana del 19/10 |
| Pre-flight F3 con este checklist antes de su kickoff | antes del 19/10 |

---

*Mantenido por Hermes Agent · creado 28/09/2026 · actualizar en cada retrospectiva de fase.*
