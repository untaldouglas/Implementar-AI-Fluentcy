---
name: aifluent-glosario
description: Gestionar el glosario consolidado del programa AI Fluency.
---

# Gestión del Glosario — AI Fluency UJMD

El agente es el GESTOR OFICIAL del glosario del programa (responsabilidad asignada por Douglas el 19/08/2026). Experto en identificar nuevos términos del dominio de negocio y del programa formativo, describirlos y ejemplificarlos con casos reales.

## Dónde vive el glosario (3 planos, modelo del programa)

1. **Fuente de verdad viva (humanos):** Drive `02_Conocimiento_Colectivo/Glosario del dominio` (Google Doc) + spreadsheet espejo `Glosario_Dominio` (1t07zfQySxfNYeExyKuN8_ETfozN-usDO1vaDA_F9HlA).
2. **Versión consolidada y versionada (git):** `01_piloto/conocimiento_colectivo/Glosario_Consolidado.md` — ESTE es el archivo maestro que se actualiza y commitea. Tiene 3 secciones: A) dominio técnico/operativo (F1) · B) términos del programa formativo · C) términos nuevos de la fase actual.
3. **Publicado/promovido:** NotebookLM del proyecto (fuente de consulta) + referencias en guías personalizadas (Día 1) + índices docs/.

## Formato de cada entrada

`| Término | Definición | Ejemplo de uso real en el programa | Aportado por | Fecha |`

Regla: SOLO entran términos con caso real de uso en el programa (nada teórico sin anclaje). Cada entrada debe responder: ¿dónde se usa este término en AI Fluency?

## Cómo mantenerlo (cada sesión)

1. **Al cerrar sesión** (con `make cierre-sesion` o antes de responder un resumen): revisar si la sesión introdujo términos nuevos (herramientas, decisiones D1–D8, artefactos creados, conceptos MCA, vocabulario de participantes).
2. **Criterio de inclusión:** término usado en el programa (artefacto, decisión, herramienta, guía, correo) — no definiciones genéricas de diccionario.
3. **Actualizar** `01_piloto/conocimiento_colectivo/Glosario_Consolidado.md`: agregar filas a la sección C (términos de la fase) con fecha real; mover a sección A/B cuando la fase cierre y el término sea estable.
4. **Sincronizar espejos:** actualizar el Google Doc/spreadsheet de Drive cuando haya cambios sustantivos (≥3 términos nuevos o cierre de fase).
5. **Commit con el ritual** `make cierre-sesion MSG="Glosario: +N términos (...) ..."`.

## Cómo promoverlo

- **Guías personalizadas:** cada guía (Día 1) referencia el glosario como recurso oficial junto a NotebookLM.
- **NotebookLM:** el glosario es fuente del notebook del proyecto (asistente de consulta).
- **Kickoff/sesiones:** presentar el glosario en el kickoff como vocabulario común del programa; animar a los participantes a proponer términos (ruta: le dicen al agente "agregar término X" o Douglas lo solicita).
- **Comunicaciones:** cuando un correo/agenda use un término nuevo, enlazar la definición.
- **Índices:** mantener el glosario enlazado desde docs/ y referenciado en plan_cohorte.

## Cómo monitorear su impacto

- **Cantidad:** términos totales y por fase (reporte en ESTADO_PROYECTO al cierre de fase).
- **Aportes por persona:** quién aporta términos (métrica de participación — cierra la deuda de C17: en F1 solo 3 Champions aportaron; F2 busca más).
- **Uso real:** términos del glosario que aparecen en evidencias de participantes (evidencia usa el vocabulario del glosario = está integrado).
- **Cobertura de sección C→A/B:** cuántos términos de la fase sobreviven al cierre (los que quedan son los de valor durable).
- **Reporte:** al cierre de cada fase, agregar entrada al ESTADO_PROYECTO con: total términos, nuevos, aportes por persona, top términos usados en evidencia.

## Pitfalls

- NO agregar términos sin ejemplo real del programa (regla de oro — evita glosario decorativo).
- NO reescribir entradas históricas: las secciones A/B son estables; los cambios van en C y luego se promueven.
- NO duplicar: buscar el término en el archivo antes de agregar (usar search_files sobre Glosario_Consolidado.md).
- NO olvidar sincronizar Drive cuando la actualización es sustantiva.
- El archivo maestro es el del REPO (versionado); Drive es espejo para humanos.
