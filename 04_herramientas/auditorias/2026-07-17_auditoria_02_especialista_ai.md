# Auditoría #02 — AI Fluency · MCA (lente ITIL / Lean / Especialista en soluciones AI)

| Campo | Valor |
|---|---|
| Fecha de auditoría | 2026-07-17 (día #17 del programa) |
| Auditor | Claude (rutina en la nube `trig_01TubHGS7vnvJQPWu6gTtN8T`, según `_plan_serie_auditorias.md`) |
| Cadencia | Semanal, viernes AM antes del seguimiento de las 14:00 (próxima: ~2026-07-24, auditoría #03 con lente COBIT introductorio) |
| Alcance | Todo lo leído en #01, más: `01_piloto/learning_record/`, `01_piloto/conocimiento_colectivo/`, `01_piloto/SOUL_plantillas/`, `04_herramientas/guia_setup_champions/learning_record/`, agendas del 13–17/07, `Acta_Seleccion_Champions_AI_Fluency.md`, `Licencia_Conduccion_AI.md` |
| Contexto al momento | Fase 1, S2 en curso (día 17), S1 sigue cerrada 3/3 desde el 10/07. C19 confirmado NO RECIBIDO al 16/07. Reunión de seguimiento hoy 14:00 (C18–C20 + mini-reportes S2) |
| Objetivo del auditado | Compartir conocimiento sobre AI usando la metodología MCA (metáfora vehicular, L0–L9, 5 licencias) |
| Lente nuevo de esta iteración | **Especialista en soluciones AI** (arquitectura de agentes, SOUL.md, delegación segura, prácticas de Hermes) — según `_plan_serie_auditorias.md` |

> **Cómo usar este archivo:** continúa la numeración estable de IDs de la auditoría #01 (I1–I8, H1–H8, R1–R10). Los hallazgos nuevos de esta iteración son I9–I11, H9–H10, R11–R17. No se edita ni contradice la auditoría #01 — es memoria. La tabla de seguimiento (sección 8) es la fuente de verdad de estados vigentes.

---

## 1. Veredicto general

**El diseño sigue siendo sólido — los SOUL.md por área son de calidad real y hay evidencia de campo genuina de delegación segura. Pero la corriente de valor sigue invertida (H1 persiste sin cambio) y esta semana apareció una variante más seria del mismo problema: el propio sistema de verificación del programa empezó a marcarse a sí mismo como "completado" sin evidencia real detrás — exactamente el patrón que dio origen a esta serie de auditorías el 10/07 (I1).**

En los 7 días desde la auditoría #01: cero entregables **nuevos** de Champions verificados contra documento real (S1 ya estaba cerrada la semana pasada). C19 —la medición antes/después que iba a cerrar H8— está confirmada como **no recibida** al 16/07. C17 (conocimiento colectivo) sigue con sus 3 artefactos vacíos pese a que el log de `ESTADO_PROYECTO.md` del 14/07 afirmó, en tiempo pasado, que estaría cerrado "antes de la reunión del 17/07". Y se descubrió que `01_piloto/learning_record/*.md` certifica L1–L3 de Hermes (✅✅✅) para los 3 Champions apuntando a un "detalle con evidencia" en `04_herramientas/guia_setup_champions/learning_record/*.md` que está, en los tres casos, vacío o autocontradictorio (I9). El programa no se estancó — se mantuvo activo produciendo agendas, borradores y esquemas del lado del Director — pero el aprendizaje verificable de los Champions sigue en cero desde hace una semana. **Día 17 de 184. Recuperable, con la misma causa raíz de la #01: el sistema sigue optimizado para que el Director produzca artefactos de seguimiento, no para que los Champions produzcan evidencia.**

La reunión de hoy 14:00 ya está diseñada con el criterio correcto ("no se certifica por reporte verbal" — agenda `2026-07-17_seguimiento_c18_c20.md`), lo cual es en sí mismo una fortaleza y una señal de que la lección de la #01 se internalizó a nivel de proceso de reunión, aunque no todavía a nivel de todos los documentos vivos del repo.

---

## 2. Qué mejoró en esta edición (obligatorio desde la #02)

**Mejora metodológica: verificación de segundo nivel — no basta con abrir el documento que afirma "completado", hay que abrir el documento *al que ese documento apunta como evidencia*.**

La auditoría #01 verificaba entregables contra su documento fuente directo (ej. el caso ancla de Irvin en Drive/PDF). Esta auditoría añadió un paso: cuando un documento resumen (`01_piloto/learning_record/*.md`) cita otro archivo como "detalle con evidencia" (`04_herramientas/guia_setup_champions/learning_record/*.md`), se abre también ese segundo archivo — no se asume que el resumen refleja correctamente lo que hay detrás del enlace. Ese paso adicional fue lo que encontró I9, el hallazgo más importante de esta semana: una cadena de referencias donde el nivel superior dice ✅✅✅ y el nivel inferior está vacío. Es la misma regla de oro de la #01 ("evidencia verificable, no intención"), aplicada ahora también a la integridad de las **referencias entre documentos**, no solo a la existencia de un documento.

---

## 3. Fortalezas verificadas (lente especialista en soluciones AI)

1. **Los 3 SOUL.md de área están genuinamente bien diseñados.** Disparadores de contexto claros por comando/palabra clave, nivel AI sugerido por tipo de tarea, Skills esperados con entregable concreto, y — el punto más relevante para este lente — **reglas de aprobación humana explícitas en el punto de mayor riesgo de cada área**: "Ningún merge a main sin revisión" (Desarrollo), "Ningún cambio de infra se ejecuta sin confirmación humana cuando toque producción" (Infraestructura), "Ningún ticket se cierra sin evidencia de resolución" (Soporte). Esto no es boilerplate — es una gobernanza de delegación real, y coincide con el estándar que exigiría cualquier revisión de seguridad de agentes.
2. **Evidencia de campo real de delegación segura**, no solo la regla escrita: Patrick excluyó conscientemente IPs y credenciales de su caso ancla (Día 7, pregunta 2 — nota ya capturada en `learning_record/patrick_orellana.md`); Irvin documentó una limitante real (sin privilegios para crear API Key en ERPNext) en lugar de improvisar un acceso inseguro.
3. **Verificación de outputs demostrada, no solo predicada:** Irvin detectó que Hermes falló una tarea real de ordenamiento de archivos (`dd/mm/aaaa`) y, en su propia reflexión Día 7, reporta que ahora verifica los resultados después de cada tarea — es el comportamiento exacto que su bloqueo de diagnóstico (Confianza/Seguridad) necesitaba desarrollar, y ocurrió en la práctica, no en una sesión de coaching.
4. **La reunión de hoy está diseñada con el criterio correcto.** La agenda `2026-07-17_seguimiento_c18_c20.md` fija explícitamente "no se certifica por reporte verbal" y trae guion de preguntas por Champion orientado a evidencia, no a autorreporte — aplica directamente la lección de la #01.
5. **El patrón de automatización con aprobación humana sigue siendo correcto donde existe** (crons SOD/EOD, auditoría semanal, bloques de calendario, borrador de nudge C19) — el diseño de "borrador, nunca envío automático" se mantiene sin excepciones detectadas.

---

## 4. Actualización de inconsistencias de la auditoría #01 (I1–I8)

| ID | Resumen | Evidencia nueva esta semana | Estado actualizado |
|---|---|---|---|
| I1 | Criterio S1 (3 vs 1 vs 2 casos) | Aclaración quedó escrita en `Roadmap:78` y `ESTADO` (decisión 10/07); sin nueva contradicción detectada | ✅ Cerrado |
| I2 | Fechas límite descuadradas (07 vs 08/07) | C14 cerrado 3/3 desde el 10/07; la tensión de fechas queda como antecedente histórico, sin efecto activo | ✅ Cerrado (mooted por cierre de C14) |
| I3 | Meta L5 en 1 mes vs "un peldaño al mes" | `Acta_Seleccion_Champions_AI_Fluency.md:60,75,90` sigue diciendo **"Meta de progresión: L2 → L5 durante el piloto"** para los 3 Champions, sin corrección. R7 (ajustar a L3/Licencia Básica) no se ejecutó | 🔴 Abierto — sin cambios |
| I4 | Numeración de fases divergente | `Roadmap_AI_Fluency_UJMD.md` sigue con 4 fases (Prep/Piloto/Escalada meses 2-3/Institucionalización meses 4-6); `ESTADO_PROYECTO.md` ya usa 5 (F0-F4, con F2 Expansión, F3 Certificaciones, F4 Institucionalización como fases separadas). No se unificó | 🔴 Abierto — sin cambios |
| I5 | Colisión notación L# (lecciones setup vs niveles MCA) | Confirmado de nuevo al leer `protocolo_verificacion.md` y los 3 archivos de `guia_setup_champions/learning_record/`: encabezados como "Lección 1: Instalación (L2→L3)" siguen mezclando numeración de lección con nivel MCA en el mismo documento | 🔴 Abierto — sin cambios |
| I6 | 3 vs 4 Champions | `ESTADO_PROYECTO.md` → tabla "Equipo y roles" ya separa claramente Director de los 3 Champions (mejora parcial); `Acta_Seleccion_Champions_AI_Fluency.md` y `Roadmap` (título "Piloto 3 Champions") no se tocaron | 🟡 Mitigado parcialmente (solo en ESTADO) |
| I7 | Learning records duplicados | Los 3 registros de `01_piloto/learning_record/` declaran explícitamente al otro directorio como "detalle", estableciendo de facto cuál es resumen y cuál detalle — pero ver I9: esa relación está rota en la práctica | 🟡 Mitigado en forma, roto en contenido (ver I9) |
| I8 | Alineación obsoleta (GSuite) | `Alineacion_Estrategica.md` sección 10 sigue describiendo la integración técnica MCP/OAuth como pendiente ago-oct **sin nota** que distinga esto del esquema de uso manual (C18) ya funcionando. La aclaración vive en `04_herramientas/agendas/2026-07-13_c18_esquema_workspace.md`, no en la Alineación misma (R8 pedía justo eso) | 🟡 Aclarado en documento derivado, no en la fuente |

---

## 5. Inconsistencias nuevas (I9–I11)

| ID | Inconsistencia | Ubicación del conflicto | Impacto | Estado |
|---|---|---|---|---|
| **I9** | **Verificación L1-L3 de Hermes marcada ✅✅✅ sin evidencia real detrás.** `01_piloto/learning_record/{irvin,mario,patrick}.md` (creado 10/07) certifica las 3 lecciones de setup de Hermes como completas para los 3 Champions, remitiendo a `04_herramientas/guia_setup_champions/learning_record/*.md` como "detalle con evidencia". Al abrir esos 3 archivos: Irvin y Mario dicen literalmente **"Estado: ⚪ No iniciado"** con todos los checkboxes de Lección 1–3 vacíos (`⬜`) y sin ningún output pegado; Patrick dice en el encabezado **"✅ Setup completado y validado (02/07/2026)"** pero el cuerpo del mismo archivo tiene exactamente los mismos checkboxes vacíos que los otros dos — contradicción dentro de un único documento. El agregador `dashboard_avance.md` nunca se actualizó desde el 29/06 y sigue en "0/9 lecciones (0%)". | `01_piloto/learning_record/*.md` vs `04_herramientas/guia_setup_champions/learning_record/*.md` vs `dashboard_avance.md` | **El hallazgo más serio de esta semana.** Es el mismo patrón que dio origen a la serie (I1 de la #01: validación verbal vs documento real) — pero esta vez el "reporte verbal" fue reemplazado por un documento que cita otro documento como respaldo sin que ese respaldo exista. Un lector que confíe en el resumen (como haría cualquier stakeholder externo o Rectoría) certificaría algo que la evidencia primaria contradice. | 🔴 Abierto |
| **I10** | **Log de `ESTADO_PROYECTO.md` afirma en tiempo pasado un hito que 2 días después resultó falso.** La entrada del 2026-07-14 dice textualmente: *"Punto 3 verificado y completado: C18 (Workspace), C19 (≥2 procesos medidos), C20 (perfil estándar) cerrados antes de la reunión del 17/07. C19 cierra H8 de auditoría #01."* Dos días después, la entrada del 16/07 en el mismo archivo corrige: *"C19: no hay documentos en la carpeta de Drive al 16/07. Estado corregido a NO RECIBIDO."* | `ESTADO_PROYECTO.md`, log 2026-07-14 vs log 2026-07-16 | El log oficial —la fuente de verdad viva del proyecto— usó lenguaje de hecho consumado ("verificado y completado", "cerrados") para describir una expectativa futura. Alguien que lea solo la entrada del 14/07 (sin llegar a la del 16/07) se lleva una imagen falsa del estado de C19. Mismo riesgo que I9, distinto lugar del repo. | 🔴 Abierto |
| **I11** | **Colisión menor de numeración "Semana".** `Roadmap_AI_Fluency_UJMD.md` usa S1–S4 como semanas *pedagógicas* del piloto (S3 = "Construcción de agentes con Hermes"). `ESTADO_PROYECTO.md` usa "Semana 3 (julio 15–21)" como semana *calendario* para C18–C20 (esquema Workspace, medición de procesos, perfiles de área) — contenido que no corresponde a la S3 pedagógica del Roadmap. Es la misma familia de problema que I5 (colisión de notación), aplicada a "S#" en vez de "L#". | `Roadmap:97-108` vs `ESTADO_PROYECTO.md` tabla "Compromisos Semana 3" | Bajo por ahora (no ha causado una decisión equivocada), pero mismo riesgo de I5 al escalar a Capa 1: alguien nuevo leerá "Semana 3" en dos documentos y entenderá cosas distintas. | 🟡 Abierto — impacto menor |

---

## 6. Hallazgos de fondo nuevos (H9–H10) — lente especialista en soluciones AI

| ID | Hallazgo | Evidencia | Estado |
|---|---|---|---|
| **H9** | **Higiene de perfiles Hermes sin criterio de verificación.** El plan de la serie pregunta explícitamente si "los flujos con Hermes siguen buenas prácticas (perfiles separados...)". Solo Irvin dejó evidencia de haber creado un perfil separado (`Testprofile`, con API de modelos Google) para aislar su práctica. No hay evidencia equivalente para Mario ni Patrick, y ningún checklist de certificación (`protocolo_verificacion.md`, `Licencia_Conduccion_AI.md`) exige perfiles separados como criterio. La buena práctica existe, pero depende de la iniciativa individual del Champion, no del sistema. | `learning_record/irvin_morales.md` (perfil Testprofile) vs ausencia del mismo dato en los registros de Mario/Patrick; `protocolo_verificacion.md` sin este criterio | 🔴 Abierto |
| **H10** | **Vacío de proceso entre "Hermes está bien instalado" y "el resultado de Hermes es correcto".** `protocolo_verificacion.md` define 3 niveles de verificación robustos, pero los 3 cubren exclusivamente la instalación/configuración de Hermes (`hermes doctor`, `hermes chat -q`, `hermes status --all`) — ninguno cubre la verificación de outputs de tareas reales delegadas (el caso ancla, C19, futuros Skills). El único ejemplo de verificación de output real que existe (Irvin y el error de ordenamiento de archivos) fue un hallazgo espontáneo del Champion, no producto de un paso protocolizado. Para un programa cuyo objetivo final es delegación segura a niveles L4+, este vacío crece en importancia cada semana que pasa. | `protocolo_verificacion.md` (alcance limitado a setup) vs `irvin_morales.md` (único caso de verificación de output, no sistematizado) | 🔴 Abierto |

---

## 7. Validación del rumbo (objetivo: compartir conocimiento vía MCA)

- **El vehículo sigue siendo bueno** — nada en esta auditoría cuestiona el diseño de MCA, las licencias o los SOUL.md. Al contrario: la calidad real de los SOUL.md y la evidencia de campo de delegación segura (Fortalezas #1–3) son señales de que, cuando el Champion sí produce evidencia, es evidencia de calidad.
- **El riesgo se mantiene donde la #01 lo identificó — en la ejecución, no en el diseño —, pero con una variante más peligrosa esta semana:** el propio sistema de seguimiento (learning_record + log de ESTADO) empezó a autocertificarse sin respaldo real. Si esto no se corrige, la serie de auditorías pierde parte de su valor: ya no basta con que Douglas confíe en el resumen, porque el resumen mismo puede estar desconectado de la evidencia que dice representar.
- **Oportunidad temporal:** día 17 de 184, exactamente 1 semana desde la #01. El patrón de "0 entregables de Champions verificados en la ventana" se repite igual que hace 7 días — la reunión de hoy es la segunda oportunidad consecutiva de revertirlo con evidencia real, no la primera.

---

## 8. Recomendaciones nuevas (R11–R17)

### Inmediatas (reunión 17/07, 14:00)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R11** | Aplicar hoy mismo, en la reunión, el mismo estándar de "abrir el documento real" a C19/C18/C20/C17/mini-reportes S2 — tal como ya lo prescribe la agenda preparada. No cerrar ningún compromiso por explicación verbal. | H1, I9, I10 | ⬜ |
| **R12** | Ejecutar la ventana de recuperación de C19 (propuesta: lunes 20/07, 12:00) si al cierre de la reunión sigue sin evidencia, y esta vez convertir el recordatorio en una rutina automatizada dirigida a los Champions (cron con aprobación humana), no en un correo manual puntual como el nudge del 14/07 — primera automatización real que sirva a los Champions, cerrando H5 de una vez. | H5, H8 | ⬜ |

### Esta semana (17–24 jul)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R13** | Corregir la cadena rota de `01_piloto/learning_record/` → `guia_setup_champions/learning_record/`: o se pega la evidencia real de L1-L3 en los 3 archivos de detalle, o se declara explícitamente ese directorio como histórico/no vinculante y se elimina la referencia "ver detalle con evidencia" de `01_piloto/learning_record/*.md`. No dejar el puntero roto. | I9 | ⬜ |
| **R14** | Adoptar una convención de lenguaje en el log de `ESTADO_PROYECTO.md`: nunca usar "verificado y completado" para un hito que depende de un evento futuro (ej. una reunión o entrega que aún no ocurrió) — usar "planificado" u "objetivo de la sesión" en su lugar. | I10 | ⬜ |
| **R15** | Agregar un criterio de "perfil separado por rol Hermes" al checklist de certificación L2 en `protocolo_verificacion.md` o `Licencia_Conduccion_AI.md`, usando el caso de Irvin (`Testprofile`) como plantilla replicable para Mario y Patrick. | H9 | ⬜ |

### Estructurales (antes de Fase 2 / antes de auditoría #04 pre-Demo Day)

| ID | Recomendación | Resuelve | Estado |
|---|---|---|---|
| **R16** | Extender `protocolo_verificacion.md` con un 4º nivel: verificación de outputs de tareas reales delegadas (no solo de instalación) — documentar el caso de Irvin como el primer ejemplo del protocolo. | H10 | ⬜ |
| **R17** | Ejecutar de una vez las recomendaciones estructurales pendientes de la #01 que siguen sin tocarse: R7 (ajustar meta L2→L5 a L3 en `Acta_Seleccion_Champions_AI_Fluency.md`), R8 (unificar numeración de fases/semanas — incluye ahora I11), R9 (nombrar co-facilitador rotativo). Ninguna requiere más de 1 sesión de trabajo; llevan 7 días abiertas sin movimiento. | I3, I4, I5, I11, H6 | ⬜ |

---

## 9. Tabla de seguimiento para la próxima auditoría (#03, ~2026-07-24, + lente COBIT EDM01/APO01/MEA01)

> Copiar esta tabla a la auditoría #03 y actualizar estados. Criterio de cierre: evidencia verificable, no intención.

| ID | Resumen corto | Estado 10/07 | Estado 17/07 | Estado 24/07 |
|---|---|---|---|---|
| I1 | Criterio S1 (3 vs 1 vs 2 casos) | 🔴 Abierto | ✅ Cerrado | |
| I2 | Fechas límite descuadradas (07 vs 08/07) | 🔴 Abierto | ✅ Cerrado (mooted) | |
| I3 | Meta L5 en 1 mes vs "un peldaño al mes" | 🔴 Abierto | 🔴 Abierto | |
| I4 | Numeración de fases divergente | 🔴 Abierto | 🔴 Abierto | |
| I5 | Colisión notación L# (lecciones vs niveles) | 🔴 Abierto | 🔴 Abierto | |
| I6 | 3 vs 4 Champions | 🔴 Abierto | 🟡 Mitigado parcial | |
| I7 | Learning records duplicados | 🟡 Mitigado | 🟡 Mitigado (roto en contenido, ver I9) | |
| I8 | Alineación obsoleta (GSuite resuelto) | 🔴 Abierto | 🟡 Aclarado en doc derivado | |
| I9 | learning_record ✅✅✅ sin evidencia detrás (setup Hermes) | — | 🔴 Abierto (nuevo) | |
| I10 | Log ESTADO afirma cierre futuro como completado | — | 🔴 Abierto (nuevo) | |
| I11 | Colisión numeración "Semana" (pedagógica vs calendario) | — | 🟡 Abierto (nuevo, menor) | |
| H1 | Corriente de valor invertida (artefactos > aprendizaje) | 🔴 Abierto | 🔴 Abierto — sin cambio en 7 días | |
| H2 | Feedback semanal insuficiente para L1 | 🔴 Abierto | 🔴 Abierto | |
| H3 | WIP >> capacidad (2h/semana sin bloquear) | 🔴 Abierto | 🟡 Resuelto solo para Douglas (bloques de calendario); Champions sin verificar | |
| H4 | Estándares definidos sin ejecutar (verificación pares) | 🔴 Abierto | 🔴 Abierto — agravado, ver I9 | |
| H5 | Cero automatización hacia Champions | 🔴 Abierto | 🔴 Abierto — nudge C19 fue manual, no recurrente | |
| H6 | Factor bus = 1 | 🔴 Abierto | 🔴 Abierto | |
| H7 | Sin proceso estándar de prórroga/excepción | 🔴 Abierto | 🟡 En vías — ventana de recuperación C19 aplicando el patrón, aún no generalizado como política | |
| H8 | Métricas sin línea base ("antes" no medido) | 🔴 Abierto | 🔴 Abierto — C19 confirmado no recibido | |
| H9 | Higiene de perfiles Hermes sin criterio de verificación | — | 🔴 Abierto (nuevo) | |
| H10 | Sin protocolo de verificación de outputs (solo de setup) | — | 🔴 Abierto (nuevo) | |

**Preguntas guía para la auditoría #03 (+ lente COBIT introductorio EDM01/APO01/MEA01):**

1. ¿C19 se recuperó en la ventana única (20/07) o se dejó vencer una segunda vez sin consecuencia visible? (H8, H7)
2. ¿El log de `ESTADO_PROYECTO.md` dejó de usar lenguaje de "completado" para hitos futuros? (I10, R14)
3. ¿Se corrigió la cadena rota `01_piloto/learning_record` ↔ `guia_setup_champions/learning_record`? (I9, R13)
4. ¿Existe ya al menos 1 automatización real (no borrador manual) dirigida a los Champions? (H5, R12)
5. EDM01 (madurez 0-2): ¿las decisiones de esta semana (ventana de recuperación, ajuste de meta si aplica) quedaron documentadas y comunicadas formalmente a los 3 Champions, o solo vividas en la reunión?
6. APO01 (madurez 0-2): ¿existe ya un dueño explícito y único de "mantener consistentes" Roadmap/Acta/ESTADO, o sigue siendo responsabilidad difusa del Director en cada sesión?
7. MEA01 (madurez 0-2): además de esta serie de auditorías, ¿hay algún mecanismo de monitoreo del desempeño del programa que no dependa de que Douglas o Claude lo ejecuten manualmente?
8. ¿El ratio de la jornada fue más coaching que producción de artefactos del Director? (H1 — pregunta fija de la serie)

---

*Auditoría #02 · 2026-07-17 · Próxima: ~2026-07-24 (+ lente COBIT introductorio) · Serie: `04_herramientas/auditorias/`*
