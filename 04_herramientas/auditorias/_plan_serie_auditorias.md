# Plan de la Serie de Auditorías — AI Fluency · MCA

> Definido el 2026-07-10 (cierre de jornada) por solicitud de Douglas, tras el valor demostrado por la
> auditoría #01. **Este archivo es el plan vivo de la serie** — se actualiza al planificar cada iteración.
> Los archivos de auditoría (`2026-XX-XX_auditoria_NN_*.md`) son memoria histórica y no se editan.

---

## Cadencia y reglas

| Regla | Valor |
|---|---|
| Frecuencia | **Semanal** (antes era ~10 días) |
| Día sugerido | Viernes por la mañana, **antes** de la reunión de seguimiento de las 14:00 — para que los hallazgos alimenten la reunión, no lleguen tarde |
| Próxima | **Auditoría #02 — viernes 2026-07-17** |
| Trazabilidad | IDs estables (I# inconsistencias, H# hallazgos, R# recomendaciones) que continúan la numeración de la serie; copiar la tabla de seguimiento de la auditoría anterior y actualizar estados |
| Criterio de cierre | Evidencia verificable, no intención (regla de oro validada el 10/07 con el caso de la validación verbal vs. documento real) |
| Mejora continua | Cada iteración incorpora al menos una mejora metodológica respecto a la anterior (sección "Qué mejoró en esta edición" obligatoria desde la #02) |

## Evolución de criterios por iteración

La serie madura acumulativamente — cada lente se suma, no reemplaza:

| # | Fecha | Lentes | Qué se agrega |
|---|---|---|---|
| 01 | 2026-07-10 ✅ | ITIL + Lean | Línea base: 8 I#, 8 H#, 10 R#, tabla de seguimiento |
| 02 | 2026-07-17 | + **Especialista en soluciones AI** | Criterios de arquitectura de agentes: ¿los SOUL.md están bien diseñados? ¿la delegación es segura (datos excluidos, aprobación humana)? ¿los flujos con Hermes siguen buenas prácticas (perfiles separados, trazabilidad de prompts, verificación de outputs)? ¿la automatización sirve a los Champions o solo al Director (seguimiento de H5)? |
| 03 | 2026-07-24 | + **COBIT (introducción)** | Primeros objetivos de gobierno: EDM01 (marco de gobierno — ¿decisiones documentadas y comunicadas?), APO01 (marco de gestión) y MEA01 (monitoreo del desempeño — ¿las métricas de la Alineación se están midiendo?). Solo evaluar madurez nivel 0-2, sin burocratizar el piloto |
| 04 | 2026-07-31 | Consolidación pre-Demo Day | Auditoría de cierre de Fase 1: ¿el Demo Day presenta evidencia medible o anécdotas? Verificación completa de la tabla de seguimiento acumulada. Insumo directo para el reporte a Rectoría |
| 05+ | agosto (F2) | + COBIT progresivo (APO07 gestión del talento, BAI08 gestión del conocimiento) | Al escalar a Capa 1 (Dirección IT completa), el lente de gestión del conocimiento (BAI08) evalúa si glosario/FAQ/errores escalan al equipo completo |

## Preguntas fijas de toda auditoría (además de las específicas)

1. ¿Cuántos entregables fueron **verificados contra documento real** (no validación verbal) desde la anterior?
2. ¿El ratio de la semana fue más coaching/aprendizaje que producción de artefactos? (H1)
3. ¿Qué recomendación de la auditoría anterior NO se ejecutó, y por qué?
4. ¿Apareció alguna nueva inconsistencia documental entre marco, estado vivo y docs publicados?

## Vínculo con los marcos

- **ITIL**: mejora continua (CSI), gestión de niveles de servicio (expectativas Champions-Director), start where you are.
- **Lean**: eliminación de muda (sobreproducción de artefactos), flujo de la corriente de valor (aprendizaje), heijunka (WIP vs. capacidad de 2h/semana).
- **COBIT** (progresivo): gobierno de la información y el conocimiento — pertinente porque el programa aspira a institucionalizarse (F4) y a publicarse como investigación; ambos exigen gobernanza demostrable.
- **Especialista AI**: el diferenciador — ningún marco clásico evalúa si un SOUL.md está bien diseñado o si la delegación a agentes es segura. Este lente es el aporte original de la serie y candidato a sección del playbook replicable.

---

*Serie: `04_herramientas/auditorias/` · Plan creado 2026-07-10 · Actualizar este archivo al planificar cada iteración*
