# S3 · Construcción de Skill Propio — Guía para Champions

> **Ventana real de trabajo: lunes 27, martes 28 y miércoles 29 de julio.** No hay jornada el jueves 30 ni el viernes 31 (vacaciones nacionales) — por eso S3 se comprime de 5 días a 3. **Fecha límite de entrega: miércoles 29/07, antes del cierre del día (17:00).**
>
> Compromiso: **C21 — Construcción de Skill propio**. Entrega vía Drive con plantilla-rúbrica (ver Sección 5).

---

## 0. Por qué esto importa (y por qué no se puede alargar)

S1 (fundamentos) y S2 (productividad personal) ya están cerrados 3/3. S3 es la última pieza de evidencia que falta antes de Demo Day: un **Skill propio**, real, versionado en el repositorio del equipo. Es también el requisito que falta para subir de Licencia Básica 🟢 a **Licencia Profesional 🔵** (`00_marco/Licencia_Conduccion_AI.md`, sección 3): SOUL.md activo (ya lo tienen) + 1 Skill creado y versionado en Git + 3 casos de uso documentados (ya tienen 2 vía C19, este trabajo cuenta como el 3º si documentan tiempo).

Con la ventana reducida a 3 días, no hay margen para explorar ideas nuevas: **cada quien construye el Skill sobre un problema que ya vive en su evidencia real**, no uno inventado para la entrega.

---

## 1. ¿Qué es un Skill? (versión corta, aplicada)

Un Skill es una instrucción reutilizable que le da a Hermes (o a Claude Code) el procedimiento exacto de una tarea que se repite en tu trabajo, para no explicarla desde cero cada vez. Es un archivo `SKILL.md` con:

- **Frontmatter** (metadatos): `name`, `description`, `tags`
- **Cuerpo**: trigger (cuándo se activa), procedimiento paso a paso, pitfalls conocidos (qué suele salir mal), y cómo verificar el resultado

Referencia técnica ya existente en el repo: `04_herramientas/Instructivo_Skills_Claude.md` (es el Skill que usa el propio programa — úsenlo como ejemplo de formato, no como plantilla a copiar literal).

Del manual (`00_marco/Manual_Implementacion_Estrategica.md`, Nivel 5): *"Ejecute el flujo tres veces, refinando el Skill hasta que el error sea cero. Versione el Skill en el repositorio del equipo."* — ese es el criterio de terminado, no una entrega en el primer intento.

---

## 2. Punto de partida por Champion (no partan de cero)

Cada quien ya tiene, en su propia evidencia de C19/S2, la tarea repetitiva candidata. La entrega es más rápida si formalizan eso, no si buscan un caso nuevo.

### Irvin (Soporte)
- **Candidato natural:** diagnóstico y respuesta estructurada de tickets — ya lo trabajaste en el taller S2 (formato de 3 pasos + escalamiento) y es el patrón que se repite en Instalación de Software Remoto.
- **Qué resuelve:** que cada ticket nuevo se responda con la misma estructura (pasos + escalamiento + qué excluir de datos sensibles) sin reescribir el prompt cada vez.

### Mario (Desarrollo)
- **Candidato natural:** "listar riesgos antes de proponer el cambio" (Técnica 3 del taller S2), aplicado ya en tu refactorización del módulo Graduados, o la generación del tablero de autoevaluación (C19 Metabase).
- **Qué resuelve:** que cualquier cambio de código pase primero por un paso de riesgos documentado antes de ejecutar el refactor, de forma repetible.

### Patrick (Infraestructura)
- **Candidato natural:** auditoría de un script contra su propio encabezado/documentación (Técnica 5 del taller S2) — nace directo del hallazgo real en `monitor_servidores_pro.sh` (el encabezado decía CPU/disco, el cuerpo solo hacía ping).
- **Qué resuelve:** que antes de dar por bueno un script se verifique automáticamente que el cuerpo cumple lo que el encabezado promete.

Si alguno tiene un candidato distinto y más relevante para su semana real de trabajo, adelante — el único requisito no negociable es que sea **real, de su área, y que lo use él o su equipo** (mismo criterio que ya aplicó en la rúbrica de C19).

---

## 3. Plan de 3 días (compresión obligatoria)

| Día | Tarea | Entregable del día |
|---|---|---|
| **Lunes 27/07** | Elegir el proceso real + escribir el `SKILL.md` (frontmatter + procedimiento + pitfalls + verificación) | Primer borrador del `SKILL.md`, aunque tenga errores |
| **Martes 28/07** | Ejecutar el Skill **3 veces** sobre casos reales, corrigiendo el `SKILL.md` después de cada corrida hasta que la 3ª salga sin error | `SKILL.md` refinado + registro de qué falló en cada intento |
| **Miércoles 29/07** | Versionar el Skill en el repositorio del equipo + llenar la plantilla-rúbrica + compartir con Douglas como comentador | Entrega final en Drive antes de las 17:00 |

No hay jornada de holgura después del miércoles — si el lunes se atrasa, la entrega completa está en riesgo. Avisar a Douglas el mismo lunes si hay bloqueo, no el miércoles.

---

## 4. Cómo construir el Skill (paso a paso técnico)

1. Identifica el trigger: ¿qué frase o situación debería activar este Skill automáticamente?
2. Escribe el `SKILL.md`:
   ```
   ---
   name: <nombre-en-kebab-case>
   description: <una línea: qué hace y cuándo usarlo>
   tags: [<área>, <tipo-de-tarea>]
   ---

   ## Cuándo usarlo
   <trigger / frases de activación>

   ## Procedimiento
   <pasos concretos, en orden>

   ## Pitfalls conocidos
   <qué suele salir mal y cómo evitarlo — usa tus propios hallazgos reales, ej. el de monitor_servidores_pro.sh>

   ## Verificación
   <cómo confirmas que el resultado es correcto antes de darlo por bueno>
   ```
3. Pruébalo 3 veces con casos reales (no inventados). Anota qué corregiste entre intento 1→2 y 2→3.
4. Cuando el 3er intento salga sin error, el Skill está listo para versionar.
5. Guárdalo en tu carpeta de Skills del repositorio del equipo (coordinar con Douglas la ruta exacta si no la tienes) y confirma que quedó en Git (commit visible).

---

## 5. Entrega y validación

- **Plantilla-rúbrica:** `_PLANTILLA_C21_Skill_Propio`, en Drive: `01_Evidencia_Champions/C21_skill_propio/`
- **Flujo:** hacer una copia → renombrar `AIFluency_<TuNombre>_C21_Skill<NombreCorto>` → llenar todas las secciones → compartir con Douglas como **comentador** → cuando esté listo, pasar a **"Aprobar"**. Nada de PDF (mismo flujo de C18/C19/C20).
- **Fecha límite:** miércoles 29/07, 17:00. Sin prórroga disponible esta semana por el calendario de vacaciones.

---

*Preparado: 2026-07-24 · Compromiso C21 (S3) · Piloto AI Fluency UJMD*
