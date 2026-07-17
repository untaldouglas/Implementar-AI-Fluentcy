# Conocimiento Colectivo — Piloto Champions

> Nace de la reunión de seguimiento del 10/07 (Sesión 18): en la reunión colaborativa de Champions del 08/07,
> Irvin, Mario y Patrick reportaron avances más allá de lo esperado para S1 — ya conversan de subagentes,
> workflows y llegaron a crear scripts `.sh` propios. Douglas concluyó que ese conocimiento no debe quedarse
> disperso ni solo en la cabeza de cada Champion: se solicitó formalizarlo en 3 artefactos vivos.
>
> **Por qué separado por área no basta:** el valor real apareció cuando los 3 conversaron entre sí, no cuando
> cada uno avanzó solo — todos tenían de referencia común el área de sistemas (los 3 pasaron por ahí), lo que
> les permitió validar y construir conocimiento de forma asociativa. Esta carpeta existe para capturar
> justamente esa capa colectiva, no la individual (que vive en `01_piloto/learning_record/`).

---

## Los 3 artefactos solicitados a los Champions

> Nombre formal (Bloque 5, misma reunión): glosario del dominio **"Uso de Agentes AI" / "AIFluent"**.

| Artefacto | Herramienta oficial (Bloque 5) | Mirror en el repo | Propósito |
|---|---|---|---|
| Glosario del dominio | **Google Sheets** (hoja electrónica) — link pendiente de agregar aquí | [glosario_dominio.md](glosario_dominio.md) | Términos técnicos/AI Fluency que los Champions usan y que un nuevo integrante necesitaría entender |
| Preguntas frecuentes | **Google Docs** (documento) — link pendiente de agregar aquí | [preguntas_frecuentes.md](preguntas_frecuentes.md) | Dudas reales que surgieron y cómo se resolvieron — evita repetir la misma pregunta 3 veces |
| Lista de errores | **Google Docs** (documento) — link pendiente de agregar aquí | [lista_errores.md](lista_errores.md) | Errores/bloqueos encontrados en la práctica (Hermes, scripts, workflows) y su solución o workaround |

**Nota de formato:** el glosario vive en hoja de cálculo (una fila por término); FAQ y lista de errores viven en documento (formato libre/tabla). Los `.md` de esta carpeta son mirror para trazabilidad interna del repo — la fuente de verdad operativa es Google Workspace, siguiendo la metodología de entrega acordada (ver [`01_piloto/learning_record/_dashboard.md`](../learning_record/_dashboard.md) y [`04_herramientas/agendas/2026-07-10_anotaciones_reunion.md`](../../04_herramientas/agendas/2026-07-10_anotaciones_reunion.md)).

---

## Convención de actualización

- Se construyen **colectivamente** — cualquier Champion puede agregar una fila, no solo quien lo descubrió.
- Cadencia sugerida: actualizar en cada reunión colaborativa semanal (miércoles, 2h) — ver `ESTADO_PROYECTO.md` → Cadencia de reuniones.
- No borrar entradas antiguas aunque queden obsoletas; marcarlas como tal. Es memoria del piloto, sirve para el playbook replicable (`02_playbook/`).

---

## Estado

| Artefacto | Entradas al 17/07 |
|---|---|
| Glosario del dominio | 🟢 13 entradas — Patrick (5, filtradas de 10), Mario (3), Irvin (1), Claude Code consolidado (4) |
| Preguntas frecuentes | 🟢 4 entradas — Patrick (1, filtrada de 4), Irvin (1), Claude Code consolidado (2) |
| Lista de errores | 🟢 5 entradas — creado desde cero (no existía) |

**17/07/2026 — Completado por Claude Code por decisión de Douglas.** A diferencia de C19 (evidencia
medida individualmente por cada Champion), C17 es un compromiso de formalización/consolidación de
conocimiento ya disperso en Drive — apropiado para que lo complete el agente con visibilidad
completa del piloto. Se filtró el aporte de Patrick (glosario/FAQ) para quedarse solo con lo que
cumple el criterio de la rúbrica ("caso real de trabajo con Hermes", no término copiado de un
manual); los 5 términos ITIL/COBIT genéricos sin ese anclaje quedaron fuera. Los 3 artefactos ya
viven en `02_Conocimiento_Colectivo` de Drive (ubicación correcta), no en carpetas personales.
**Sigue pendiente:** Irvin y Mario no han aportado por iniciativa propia todavía (lo suyo aquí viene
de minar su evidencia de C19) — la próxima colaborativa semanal debe cerrar esa brecha para que sea
un artefacto verdaderamente construido por los 3, no solo consolidado por el agente.

*Creado: 2026-07-10 · Acordado en la reunión de seguimiento (Sesión 18) tras el reporte positivo de la colaborativa del 08/07 · Piloto AI Fluency UJMD*
