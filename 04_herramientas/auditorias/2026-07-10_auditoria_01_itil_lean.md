# Auditoría #01 — AI Fluency · MCA (lente ITIL / Lean)

| Campo | Valor |
|---|---|
| Fecha de auditoría | 2026-07-10 (día #10 del programa) |
| Auditor | Claude (análisis solicitado por Douglas A. Galindo) |
| Cadencia prevista | Cada ~10 días (próxima: ~2026-07-20) |
| Alcance | Marco conceptual (`00_marco/`), piloto (`01_piloto/`), herramientas (`04_herramientas/`), estado vivo (`ESTADO_PROYECTO.md`) |
| Contexto al momento | Fase 1 estancada: S1 vencida sin verificar, S2 sin arrancar, progreso ~19%, reunión crítica hoy 14:00 |
| Objetivo del auditado | Compartir conocimiento sobre AI usando la metodología MCA (metáfora vehicular, L0–L9, 5 licencias) |

> **Cómo usar este archivo:** cada hallazgo tiene un ID estable (I# = inconsistencia, H# = hallazgo de fondo, R# = recomendación). En la próxima auditoría, copiar la tabla de seguimiento final, actualizar estados y registrar hallazgos nuevos en un archivo nuevo (`2026-07-XX_auditoria_02_*.md`). No editar hallazgos históricos — son la memoria.

---

## 1. Veredicto general

**La metodología es sólida y el rumbo es correcto. El riesgo no está en el diseño — está en la ejecución, con una causa raíz identificable: el sistema está optimizado para producir artefactos del programa, no para producir aprendizaje en los Champions.**

En 10 días el programa generó blog, infográficos, deck, one-pager para Rectoría, playbook, protocolo de investigación, dashboards, crons y ~16 sesiones de trabajo del Director — y cero entregables verificados de los Champions. En términos Lean: sobreproducción (*muda*) en la corriente de soporte mientras la corriente de valor (el aprendizaje) está detenida. **Recuperable: día 10 de 184.**

---

## 2. Fortalezas verificadas

1. **Diagnóstico antes de intervenir** — baseline aplicado, niveles calculados, itinerarios personalizados (ITIL: *start where you are*).
2. **Gestión visual y transparencia** — `ESTADO_PROYECTO.md` como fuente única viva, dashboards, log fechado. El proyecto detectó su propio estancamiento en 3 días.
3. **Piloto de lote pequeño** — 3 Champions, 1 por área, seleccionados por apertura al cambio, no por nivel técnico.
4. **Postura de seguridad madura** — `.gitignore` intencional, datos sintéticos en desarrollo, aprobación humana en acciones externas (Prompt 7 del onboarding).
5. **El Director modela el destino** — crons SOD/EOD como evidencia viva de L8.
6. **Sistema de certificación replicable y agnóstico de herramienta** — la sección "cómo replicar" de `Licencia_Conduccion_AI.md` es el artefacto que hace transferible el conocimiento.

---

## 3. Inconsistencias documentales (I#)

| ID | Inconsistencia | Ubicación del conflicto | Impacto | Estado |
|---|---|---|---|---|
| **I1** | **Entregable S1: 3 números distintos.** Roadmap pide 3 casos de uso; guías enviadas a Champions piden 1 caso ancla; Licencia Básica pide 2 casos. | `Roadmap:76` vs `docs/guia_*.html` (Día 6) vs `Licencia:43` | Se estaba por verificar incumplimiento contra un criterio nunca comunicado. La más urgente. | 🔴 Abierto (decisión en reunión 10/07) |
| **I2** | **Fechas límite descuadradas.** C14 registrado vencido el 07/07; las guías dicen "enviar antes del 8 de julio". | `ESTADO_PROYECTO.md` vs guías (Entrega Final) | El "atraso de 3 días" es de 2 según lo comunicado. Erosiona confianza si un Champion lo señala. | 🔴 Abierto |
| **I3** | **Meta de nivel del piloto contradictoria.** Acta: "L2→L5 en el piloto"; dashboard: "Champions certificados L3" al 31/07; baseline real: L1. El propio Manual dice "escale un peldaño al mes" — el piloto pide 4 peldaños en 1 mes. | `Acta:60` vs Dashboard vs `Manual:94` | **La contradicción interna más seria del marco.** El documento fundacional predice que la meta del piloto es 4× demasiado ambiciosa. | 🔴 Abierto |
| **I4** | **Numeración de fases divergente.** ESTADO: F3=Certificaciones (oct), F4=Institucionalización (nov-dic). Roadmap: Fase 3=Institucionalización (meses 4-6). Alineación: "Fase 4 (Estudiantes)" con impacto en agosto. | `ESTADO_PROYECTO.md` vs `Roadmap:148` vs `Alineacion:120` | "Fase 3" significa tres cosas distintas según el documento. Problema al replicar/publicar. | 🔴 Abierto |
| **I5** | **Colisión de notación "L#".** Lecciones de setup usan L1/L2/L3 (Instalación/Configuración/Verificación) y a la vez "Lección 1 (L2→L3)" refiriéndose a niveles MCA. | `guia_setup_champions/learning_record/*`, `protocolo_verificacion.md` | Confusión garantizada al escalar a gente nueva. | 🔴 Abierto |
| **I6** | **"3 Champions" vs "4 Champions".** Roadmap titula "Piloto 3 Champions"; Acta y resumen visual dicen 4 (incluye al Director). | `Roadmap:56` vs Acta | El playbook replicable debe decidir: ¿el Director es Champion o Instructor? (Sugerencia: Instructor.) | 🔴 Abierto |
| **I7** | **Dos ubicaciones de learning records.** `04_herramientas/guia_setup_champions/learning_record/` (nunca llenado) y `01_piloto/learning_record/` (creado 10/07, enlazado al primero). | Ambos directorios | Definir canónico y congelar el otro — doble actualización es *muda*. | 🟡 Mitigado (enlazados), falta declarar canónico |
| **I8** | **`Alineacion_Estrategica.md` obsoleto desde hoy.** Sección 10 planifica integración Google Workspace para ago-oct; hoy se marcó como resuelta. | `Alineacion:276-310` | Se adelantó 2 meses un prerrequisito de investigación ("sin GSuite no se miden capacidades L4+") — buena noticia sin capitalizar. | 🔴 Abierto |

---

## 4. Hallazgos de fondo (H#)

### Lente Lean

| ID | Hallazgo | Evidencia | Estado |
|---|---|---|---|
| **H1** | **Corriente de valor invertida.** Abundante material *push* (guías, prompts, decks) sin señal de *pull* verificada: no hay telemetría ni acuse de que los Champions abrieran sus guías. El silencio de 3 días es la señal de pull más honesta — y dice "débil". | 0 entregables verificados vs ~16 sesiones de producción del Director | 🔴 Abierto |
| **H2** | **Ciclo de feedback demasiado largo para novatos.** Perfiles L1 zona Pasajero, con bloqueos diagnosticados de *confianza* y *conocimiento técnico*, recibieron 7 días de trabajo autónomo entre sesiones. Cadencia semanal es correcta para L4+, no para L1. | Baseline (bloqueos por Champion) + estancamiento S1 | 🔴 Abierto |
| **H3** | **Demanda vs capacidad sin balancear (heijunka).** 6 fases + protocolo de investigación Q1/Scopus + integración GCP + blog + marca + playbook, sobre capacidad declarada de 2h/semana que ni siquiera están bloqueadas en calendario. WIP excede capacidad por un orden de magnitud. | Bloqueo activo "Douglas saturado" (10 días abierto) | 🔴 Abierto |
| **H4** | **Trabajo estándar existe pero no se ejecuta.** `protocolo_verificacion.md` define 3 niveles de verificación — pares nunca usado tras Sesión 0. `dashboard_avance.md` congelado en "0/9 lecciones, actualizado 29/06". | Archivos citados | 🔴 Abierto |
| **H5** | **5 porqués del estancamiento → ironía estructural.** El programa que enseña delegación asíncrona (L6-L8) gestiona a sus alumnos 100% síncronamente, dependiente de la atención personal del Director. Los crons trabajan para Douglas, ninguno toca a los Champions (recordatorios, nudges, recolección de evidencia). | Crons existentes: SOD/EOD/backup — todos internos | 🔴 Abierto |

### Lente ITIL

| ID | Hallazgo | Evidencia | Estado |
|---|---|---|---|
| **H6** | **Factor bus = 1.** Douglas es director, arquitecto, facilitador, instructor, verificador y documentador. El programa se detuvo exactamente los días que él se saturó — acoplamiento estructural, no coincidencia. Además su propia Licencia de Instructor exige "haber certificado a ≥2 personas": los co-facilitadores son requisito del sistema, no solo resiliencia. | Estancamiento 08-09/07 correlacionado con saturación | 🔴 Abierto |
| **H7** | **Sin gestión de expectativas formalizada (SLM).** El "contrato" con Champions (guía + fecha del correo) y el registro interno (C14) divergieron sin detección hasta el día 10. No hay proceso estándar de excepción: ¿qué pasa cuando un entregable se atrasa? Se improvisó en la reunión. | I1 + I2 | 🔴 Abierto |
| **H8** | **Métricas definidas, cero instrumentadas.** La Alineación define métricas excelentes (reducción ≥20% de tiempo, éxito al primer intento ≥70%, Flow Efficiency) pero **nadie midió el "antes"**. Sin línea base de tiempos, el Demo Day presenta anécdotas y el protocolo de investigación (pre-post) pierde su "pre". | `Alineacion:161-182` sin mecanismo de captura | 🔴 Abierto — urgente y barato de arreglar |

---

## 5. Validación del rumbo (objetivo: compartir conocimiento vía MCA)

- **El vehículo es bueno.** La metáfora vehicular + licencias es memorable, progresiva, agnóstica de herramienta y replicable — calidad de framework publicable.
- **"Compartir conocimiento" se evidencia cuando otros lo reciben y re-transmiten**, no cuando se documenta. La métrica del objetivo personal no es el número de artefactos — es el momento en que Irvin, Mario o Patrick le enseñan algo a un tercero (teach-back, Fase 2). Todo lo que acelere ese momento sirve al objetivo; el resto puede esperar.
- **Oportunidad temporal:** día 10 de 184, un entregable atrasado ~1 semana. A tiempo, con condición: resetear criterios y cadencia, no solo fechas.

---

## 6. Recomendaciones (R#)

### Inmediatas (reunión 10/07)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R1** | Armonizar criterio S1 a favor de lo comunicado: S1 = 1 caso ancla + reflexión; los 3 casos del Roadmap pasan a meta acumulada S1+S2. Redefinir C14 así. | I1, I2, H7 | ⬜ |
| **R2** | Co-crear la recuperación con los Champions, no presentarla. Preguntar "¿qué les estorbó?" antes de proponer. | H1, H2 | ⬜ |
| **R3** | Decidir buffer del Demo Day explícitamente: moverlo a ~07/08 o recortar S3 (de "agente funcional" a "1 Skill documentado"). | I3, H3 | ⬜ |

### Esta semana (11–17 jul)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R4** | Instrumentar el "antes" ya: cada Champion cronometra 1 tarea recurrente (la de su caso ancla) esta semana. ~15 min de esfuerzo; salva el reporte a Rectoría y el "pre" de la investigación. | H8 | ⬜ |
| **R5** | Micro-check-in asíncrono 3×/semana por Teams (1 línea: hice / me bloqueó). Automatizar el recordatorio con cron de Hermes + aprobación humana — convierte el cuello de botella en demo viva de L8. | H2, H5 | ⬜ |
| **R6** | Limitar WIP formalmente: congelar hasta después del Demo Day el protocolo de investigación, blog por jornada y expansiones. Declararlo en `ESTADO_PROYECTO.md` como decisión. Bloquear las 2h/semana en calendario. | H3 | ⬜ |

### Estructurales (antes de Fase 2)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R7** | Ajustar meta del piloto a L3 / Licencia Básica al 31/07 (L5 como meta de fin de Fase 2) — obedece la regla "un peldaño al mes" del propio Manual. | I3 | ⬜ |
| **R8** | Unificar numeración de fases (ESTADO como calendario canónico), renombrar lecciones para eliminar colisión L#, actualizar Alineación con GSuite resuelto. | I4, I5, I8 | ⬜ |
| **R9** | Nombrar co-facilitador rotativo (un Champion "copiloto" por semana). Reduce factor bus y construye el pipeline de Instructores que el sistema de certificación exige. | H6 | ⬜ |
| **R10** | Declarar `01_piloto/learning_record/` como ubicación canónica y congelar `guia_setup_champions/learning_record/` (solo lectura histórica). Decidir si el Director cuenta como Champion o Instructor en todos los docs. | I7, I6 | ⬜ |

---

## 7. Tabla de seguimiento para la próxima auditoría (~20/07)

> Copiar esta tabla a la auditoría #02 y actualizar estados. Criterio de cierre: evidencia verificable, no intención.

| ID | Resumen corto | Estado 10/07 | Estado 20/07 |
|---|---|---|---|
| I1 | Criterio S1 (3 vs 1 vs 2 casos) | 🔴 Abierto | |
| I2 | Fechas límite descuadradas (07 vs 08/07) | 🔴 Abierto | |
| I3 | Meta L5 en 1 mes vs "un peldaño al mes" | 🔴 Abierto | |
| I4 | Numeración de fases divergente | 🔴 Abierto | |
| I5 | Colisión notación L# (lecciones vs niveles) | 🔴 Abierto | |
| I6 | 3 vs 4 Champions | 🔴 Abierto | |
| I7 | Learning records duplicados | 🟡 Mitigado | |
| I8 | Alineación obsoleta (GSuite resuelto) | 🔴 Abierto | |
| H1 | Corriente de valor invertida (artefactos > aprendizaje) | 🔴 Abierto | |
| H2 | Feedback semanal insuficiente para L1 | 🔴 Abierto | |
| H3 | WIP >> capacidad (2h/semana sin bloquear) | 🔴 Abierto | |
| H4 | Estándares definidos sin ejecutar (verificación pares) | 🔴 Abierto | |
| H5 | Cero automatización hacia Champions | 🔴 Abierto | |
| H6 | Factor bus = 1 | 🔴 Abierto | |
| H7 | Sin proceso estándar de prórroga/excepción | 🔴 Abierto | |
| H8 | Métricas sin línea base ("antes" no medido) | 🔴 Abierto | |

**Preguntas guía para la auditoría #02:**
1. ¿Cuántos entregables de Champions fueron **verificados** (no autoreportados) desde el 10/07?
2. ¿Se midió el "antes" de al menos 1 tarea por Champion? (H8)
3. ¿Existe al menos 1 flujo automatizado dirigido a Champions? (H5)
4. ¿Las 2h/semana están bloqueadas en calendario y se respetaron? (H3)
5. ¿La decisión Demo Day (buffer o recorte) se tomó y se comunicó? (R3)
6. ¿El ratio de la jornada fue más coaching que producción de artefactos? (H1)

---

*Auditoría #01 · 2026-07-10 · Próxima: ~2026-07-20 · Serie: `04_herramientas/auditorias/`*
