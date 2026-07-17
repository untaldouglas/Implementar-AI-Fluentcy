# Matriz de Entregables por Nivel — MCA · Hermes Agent

> ⚠️ **PROPUESTA v0.1 (17/07/2026) — EN REVISIÓN DE DOUGLAS, NO VINCULANTE AÚN.**
> Al aprobarse: se convierte en el catálogo canónico de entregables por nivel, cada compromiso nuevo la cita (regla Protocolo §4.5), y las plantillas "por crear" se generan antes de anunciar el nivel correspondiente.

**Herramienta central:** Hermes Agent (NousResearch). Cada nivel usa la capacidad de Hermes que le corresponde según el mapeo del `Manual_Implementacion_Estrategica.md`.
**Ubicación de todas las entregas:** carpeta única de Drive → `01_Evidencia_Champions/` (estructura del 17/07), salvo lo versionado en Git (SOUL.md, SKILL.md).
**Alcance del piloto (F1):** hasta **L3 / Licencia Básica** (decisión R7/I3). L4+ es Fase 2 en adelante — sus filas existen para planificar, no para exigir hoy.

---

## 🟤 Permiso de Aprendizaje (L0–L1) — "Conoce la IA, la usa con asistencia"

| Nivel | Objetivo de aprendizaje | Entregable verificable | Plantilla | Descripción e instrucciones |
|---|---|---|---|---|
| **L0 — El Taxi** (chat básico) | Formular prompts efectivos con el marco Rol-Tarea-Contexto; entender qué es un LLM y sus límites | 1 ejercicio prompt A/B documentado (mismo problema, prompt débil vs estructurado, comparación de resultados) | ✅ Cubierto por la guía S1 (Día 1) — no requiere plantilla propia | Se hace durante la guía de 7 días. Evidencia en `S1_Fundamentos/<Nombre>/`. Verificado para los 3 Champions (S1 cerrada 3/3) |
| **L1 — El Chofer** (memoria + web) | Usar memoria y búsqueda web de Hermes; **verificar los resultados** antes de usarlos (hábito base de delegación segura) | 1 caso de uso real con verificación documentada del output (qué se revisó, qué falló, qué se corrigió) | ✅ Cubierto por guía S1 (caso ancla Día 6 + reflexión Día 7) | Evidencia en `S1_Fundamentos/<Nombre>/`. Caso fundacional del programa: Irvin y el ordenamiento dd/mm/aaaa (protocolo Nivel 4) |

**Criterio de licencia** (`Licencia_Conduccion_AI.md`): baseline completado + 1 sesión guiada registrada + distingue L0–L3. **Estado piloto: los 3 Champions lo superaron.**

---

## 🟢 Licencia Básica (L2–L3) — "Conduce solo en rutas conocidas" ← **META DEL PILOTO**

| Nivel | Objetivo de aprendizaje | Entregable verificable | Plantilla | Descripción e instrucciones |
|---|---|---|---|---|
| **L2 — El Coche Propio** (Hermes local + SOUL.md) | Operar Hermes instalado localmente con perfil separado de práctica y SOUL.md personalizado del área; medir el impacto de delegar tareas reales | (a) Setup verificado — Lecciones 1-3 con outputs (`hermes doctor` / `chat -q` / `status --all`); (b) **perfil Hermes separado** (criterio R15); (c) **2 procesos medidos antes/después** (= C19); (d) mini-reporte de prompting (= S2) | ✅ `_PLANTILLA_C19_Proceso_Medido` · ✅ `_PLANTILLA_S2_MiniReporte` · Setup: checklist de `protocolo_verificacion.md` | C19: una copia de la plantilla POR PROCESO → `C19_medicion_antes_despues/<Nombre>/`, nombre `AIFluency_<Nombre>_C19_<Proceso>`. S2: copia → subcarpeta del Champion, `AIFluency_<Nombre>_S2_MiniReporte`. Perfil separado: modelo replicable = `Testprofile` de Irvin |
| **L3 — El Copiloto de Contexto** (proyectos / contexto persistente) | Eliminar la re-explicación: construir un contenedor de conocimiento fijo (SOUL.md maduro + memorias/archivos de contexto del área) que Hermes carga en cada sesión | (a) SOUL.md del área activo y versionado (base: perfil estándar = C20); (b) 1 tarea recurrente ejecutada con el contexto persistente, midiendo el ahorro de re-explicación vs. sesión "fría" | ✅ `_PLANTILLA_C20_Perfil_de_Area` (insumo del SOUL.md) · 🔲 **Por crear:** `_PLANTILLA_L3_Contexto_Persistente` (comparativa sesión fría vs. con contexto) | C20: copia → `C20_perfiles_area/`, nombre `AIFluency_<Nombre>_C20_Perfil<Area>`. SOUL.md: se versiona en Git (repo del área / `01_piloto/SOUL_plantillas/` como referencia), no en Drive. La medición fría-vs-contexto va en Drive |

**Criterio de licencia:** 2 casos de uso documentados + uso autónomo en tareas rutinarias + conoce ≥2 herramientas. **C19 conforme = criterio (a) cumplido → firma de actas.**

---

## 🔵 Licencia Profesional (L4–L5) — "Configura el vehículo para su trayecto" — *Fase 2*

| Nivel | Objetivo de aprendizaje | Entregable verificable | Plantilla | Descripción e instrucciones |
|---|---|---|---|---|
| **L4 — El Copiloto con Manos** (MCP) | Conectar Hermes a las herramientas del área (Workspace, sistemas internos) con validación humana obligatoria en toda escritura | 1 integración MCP funcionando + documento de reglas de aprobación humana (qué acciones exigen confirmación y por qué) | 🔲 **Por crear:** `_PLANTILLA_L4_Integracion_MCP` (integración, alcance, reglas humano-en-el-bucle, datos excluidos) | Depende de la integración técnica Workspace (ago–oct, `Alineacion_Estrategica.md` §10). La regla de aprobación humana del SOUL.md del área es prerrequisito |
| **L5 — El Copiloto Entrenado** (Skills) | Convertir procedimientos recurrentes del área en Skills ejecutables: `SKILL.md` con trigger, procedimiento, pitfalls y verificación | 1 SKILL.md versionado en Git + demo grabada o transcrita de Hermes ejecutándolo + 3er caso de uso con resultado medible | 🔲 **Por crear:** `_PLANTILLA_L5_Skill` (base: `04_herramientas/Instructivo_Skills_Claude.md` + formato SKILL.md del Manual) | El SKILL.md vive en Git (repositorio del equipo); la demo y la medición en Drive. Candidatos ya identificados en las actas: verificación de respuestas (Irvin), checklist de refactor (Mario), monitoreo formalizado (Patrick) |

**Criterio de licencia:** SOUL.md activo + 1 Skill en Git + 3 casos (1 medible) + explica su flujo a otra persona.

---

## 🟣 Licencia Avanzada (L6–L7) — "Piloto automático con supervisión" — *Fase 2/3*

| Nivel | Objetivo de aprendizaje | Entregable verificable | Plantilla | Descripción e instrucciones |
|---|---|---|---|---|
| **L6 — Vehículo Autónomo de Tareas** (delegación asíncrona) | Delegar objetivos multietapa (`delegate_task` / background con `notify_on_complete`) y verificar outputs con el protocolo Nivel 4 | 1 tarea multietapa delegada de punta a punta + registro de verificación de outputs (criterio previo, revisión, prueba independiente, fallas) | 🔲 **Por crear:** `_PLANTILLA_L6_Delegacion_Asincrona` (reusa las 4 secciones del protocolo Nivel 4) | La verificación de outputs deja de ser opcional: sin registro Nivel 4, la delegación no certifica |
| **L7 — Vehículo Autónomo Total** (terminal + navegador) | Ejecutar flujos técnicos completos con los toolsets `terminal`/`browser` de Hermes, con límites de seguridad explícitos | 1 flujo técnico end-to-end documentado + declaración de límites (qué NO puede tocar: producción, credenciales) | 🔲 **Por crear:** `_PLANTILLA_L7_Flujo_Autonomo` | Prerrequisito: límites de delegación del perfil C20 del área aplicados en la práctica |

**Criterio de licencia:** 1 automatización activa + Skills en repo compartido + métricas de impacto + mentor en ≥1 sesión grupal.

---

## 🏆 Instructor de Conducción (L8–L9) — "Enseña a otros a tomar el volante" — *Fase 3+*

| Nivel | Objetivo de aprendizaje | Entregable verificable | Plantilla | Descripción e instrucciones |
|---|---|---|---|---|
| **L8 — El Servicio de Uber** (cron jobs) | Operar automatizaciones recurrentes (`cron_job` de Hermes) que trabajan sin comando de inicio, con aprobación humana en las salidas | 1 rutina cron activa ≥2 semanas + métricas de su impacto (tiempo/volumen) + runbook de mantenimiento | 🔲 **Por crear:** `_PLANTILLA_L8_Rutina_Automatizada` | Modelo de referencia: las rutinas del programa (SOD/EOD, auditoría semanal) — patrón "borrador, nunca envío automático" |
| **L9 — La Flota Logística** (multi-agente) | Diseñar orquestación multi-agente (patrón orchestrator/leaf, `max_spawn_depth`) con seguridad Shift-Left: permisos auditados en diseño | Diseño de flota documentado + auditoría de permisos previa + **haber certificado a ≥2 personas** (actas firmadas como Instructor) | 🔲 **Por crear:** `_PLANTILLA_L9_Flota` + acta de certificación (ya existe: plantilla en `Licencia_Conduccion_AI.md` §5) | La certificación de otros es el entregable central: el nivel se demuestra enseñando, no solo operando |

**Criterio de licencia:** ≥2 certificados + ≥3 automatizaciones en producción + 1 Skill institucional + métricas automatizadas del área.

---

## Reglas de mantenimiento de esta matriz (al aprobarse)

1. Es la **fuente canónica del catálogo de entregables por nivel** (se agrega al mapa del Protocolo §3). Los compromisos (C#) citan filas de esta matriz; no inventan entregables nuevos sin agregarlos aquí primero.
2. Cada plantilla "🔲 por crear" se publica en Drive **antes** de anunciar el compromiso que la use (Protocolo §4.5).
3. Toda actualización se registra en el log de `ESTADO_PROYECTO.md`.

---

*Propuesta generada el 17/07/2026 a partir de: `Licencia_Conduccion_AI.md` (criterios por licencia), `Manual_Implementacion_Estrategica.md` (capacidades Hermes por nivel), plantillas-rúbrica del 17/07 y protocolo de verificación ampliado (Nivel 4).*
