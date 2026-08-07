# Guía Rápida: Qué Aprender y Qué Entregar por Licencia y Nivel

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Versión:** 1.0 · **Fecha:** 07/08/2026 · **Autor:** Douglas A. Galindo

> **Para quién:** facilitadores del programa (quienes acompañan a los Champions) y personas interesadas en participar (futuras capas: Dirección IT, Universidad, Comunidad).
> **Qué es:** versión simplificada de `00_marco/Licencia_Conduccion_AI.md` — qué se aprende en cada licencia, qué evidencia se entrega y con qué plantilla. El marco normativo completo está en los documentos fuente; esta guía es para explicar rápido.
> **Regla de oro:** ninguna licencia se otorga por lo que alguien *dice* que sabe — se otorga con **evidencia real entregada en Drive y aprobada con la funcionalidad "Aprobar"** (nada de PDF, nada verbal).

---

## 1. El mapa en una tabla

| Licencia | Niveles MCA | Analogía | Qué se aprende (esencial) | Evidencia que se entrega | Quién valida |
|---|---|---|---|---|---|
| 🟤 **Permiso de Aprendizaje** | L0–L1 | Taxi · Chofer | Qué es la IA, uso guiado, diferencia entre niveles | Diagnóstico baseline + 1 sesión de uso guiado registrada | Licencia Profesional o superior |
| 🟢 **Licencia Básica** | L2–L3 | Coche Propio · Copiloto de Contexto | Usar IA de forma autónoma en tareas rutinarias de su área; conocer ≥2 herramientas | **2 casos de uso reales documentados** (problema → proceso → resultado) | Licencia Avanzada o Instructor |
| 🔵 **Licencia Profesional** | L4–L5 | Copiloto con Manos (MCP) · Copiloto Entrenado (Skills) | Configurar su propio agente (SOUL), crear Skills, explicar su flujo de trabajo | **SOUL.md propio activo** + **1 Skill versionado en Git** + **3 casos de uso** (≥1 con resultado medible) | Instructor de Conducción |
| 🟣 **Licencia Avanzada** | L6–L7 | Vehículo Autónomo de Tareas · Autónomo Total | Delegar tareas completas, operar terminal/navegador de forma autónoma | **1 automatización activa** (cron/agente/pipeline) + Skills en repo compartido + **métricas de impacto** + 1 mentoría grupal | Instructor + revisión de repositorio |
| 🏆 **Instructor de Conducción** | L8–L9 | Servicio de Uber (cron) · Flota Logística (swarm) | Programar agentes, orquestar multi-agentes, enseñar a otros | **≥2 personas certificadas por él** (acta firmada) + **≥3 automatizaciones en producción** + 1 Skill institucional + métricas automatizadas | Par Instructor / comité |

---

## 2. Ficha por licencia

### 🟤 Permiso de Aprendizaje (L0–L1)
- **Analogías:** L0 El Taxi (chat básico, sin memoria) → L1 El Chofer (memoria + web).
- **Qué aprender:** qué puede y qué no puede hacer la IA; usar un chat con acompañamiento; entender los niveles L0–L3 para ubicarse.
- **Evidencia mínima:** cuestionario baseline completado (score documentado) + 1 sesión de uso guiado registrada.
- **Ejemplo del piloto UJMD:** los 3 Champions arrancaron aquí (diagnóstico Google Form del 01/07).

### 🟢 Licencia Básica (L2–L3)
- **Analogías:** L2 El Coche Propio (indexación local) → L3 El Copiloto de Contexto (proyectos/conocimiento persistente).
- **Qué aprender:** resolver tareas reales de su área con IA de forma autónoma; comparar ≥2 herramientas; medir su propio trabajo (antes/después).
- **Evidencia (2 casos de uso reales):** cada caso con problema concreto, proceso, resultado y **tiempo/costo medido antes y después**.
- **Plantilla:** `_PLANTILLA_C19_Proceso_Medido` (una copia POR proceso) → `01_Evidencia_Champions/C19_medicion_antes_despues/<Nombre>/`.
- **Ejemplo del piloto:** Mario midió refactor de código y tablero Metabase; Patrick, altas/bajas AD y reportería; Irvin, instalación remota y diagnóstico de pantalla.
- **Cierre formal:** acta de certificación firmada por el Instructor (`00_Gobernanza/Actas_Licencias/`).

### 🔵 Licencia Profesional (L4–L5)
- **Analogías:** L4 El Copiloto con Manos (MCP: la IA ejecuta acciones en sus sistemas) → L5 El Copiloto Entrenado (Skills: un SOP ejecutable, no un documento).
- **Qué aprender:** configurar su agente para que trabaje como *ellos* (SOUL.md propio), crear Skills reutilizables y versionados, y explicar su flujo a otra persona.
- **Evidencia (4 piezas):**
  1. **SOUL.md propio** configurado y activo — perfil del área convertido en configuración de agente (disparadores de rol, protocolo de datos, skills). Plantilla: `_PLANTILLA_C22_SOUL_Propio` → `01_Evidencia_Champions/C22_soul_propio/`.
  2. **1 Skill creado, documentado y versionado en Git** (SKILL.md con trigger, procedimiento, pitfalls, verificación; probado 3 veces hasta error cero). Plantilla: `_PLANTILLA_C21_Skill_Propio` → `01_Evidencia_Champions/C21_skill_propio/`.
  3. **3 casos de uso documentados**, al menos 1 con resultado medible (los 2 de Básica + 1 más).
  4. **Explicar su flujo de trabajo con IA** a otra persona (se evalúa en sesión).
- **Ejemplo del piloto:** los 3 Champions entregaron su Skill C21 (refactor C# 4.0, monitoreo de red, diagnóstico de baterías); Patrick ya tiene SOUL propio; Mario e Irvin están cerrando el suyo (C22).

### 🟣 Licencia Avanzada (L6–L7)
- **Analogías:** L6 Vehículo Autónomo de Tareas (delegación asíncrona) → L7 Autónomo Total (terminal + navegador).
- **Qué aprender:** delegar objetivos completos a agentes, automatizar flujos técnicos, medir impacto (tiempo/calidad/volumen).
- **Evidencia:** 1 automatización activa (cron job, agente en background o pipeline) + Skills versionados en **repositorio compartido del equipo** + métricas de impacto documentadas + participar como mentor en ≥1 sesión grupal.
- **Nota:** es aquí donde los Skills personales de C21 deben consolidarse en el repo del equipo.

### 🏆 Instructor de Conducción (L8–L9)
- **Analogías:** L8 El Servicio de Uber (cron jobs que trabajan solos) → L9 La Flota Logística (multi-agentes coordinados).
- **Qué aprender:** diseñar automatizaciones permanentes, orquestar agentes especializados, y **certificar a otros**.
- **Evidencia:** ≥2 personas certificadas por él (acta firmada) + ≥3 automatizaciones/agentes en producción + 1 Skill institucional usado por otros + métricas de su área reportadas de forma regular y automatizada.
- **Ejemplo del piloto:** Douglas (L8) es el Instructor fundador del programa.

---

## 3. Los 5 pasos de la certificación (para cualquier licencia)

1. **Autodiagnóstico** — cuestionario baseline → nivel estimado.
2. **Práctica** — evidencia en Drive (casos, skills, SOUL) con plantilla-rúbrica.
3. **Solicitud** — el Champion comparte el documento como **comentador**.
4. **Validación** — el Instructor revisa y aprueba con la funcionalidad **"Aprobar"** de Google Drive (evidencia real, no verbal).
5. **Registro** — acta firmada + tabla de conductores certificados en `00_marco/Licencia_Conduccion_AI.md`.

**Renovación:** anual, o cuando cambia el nivel de responsabilidad del rol.

---

## 4. Glosario mínimo (para interesados)

| Término | Qué es |
|---|---|
| **MCA** | Modelo de Conducción AI: escala L0–L9 que describe la progresión de conducción de IA (de pasajero a instructor). |
| **Champion** | Participante del piloto (uno por área) que aprende y certifica en niveles. |
| **SOUL.md** | Archivo de configuración del agente: cómo se comporta la IA de cada persona/área (qué activa cada rol, qué datos no toca). |
| **Skill (SKILL.md)** | Habilidad reutilizable del agente: procedimiento probado, versionado en Git. Un SOP ejecutable. |
| **Cron job / agente** | Automatización que ejecuta tareas sin intervención (reportes, monitoreos, recordatorios). |
| **Drive Approvals** | Funcionalidad "Aprobar" de Google Drive: la forma oficial de validar evidencia en el programa. |

---

## 5. Cómo se conecta con las capas de expansión

| Capa | Audiencia | Licencia objetivo inicial |
|---|---|---|
| Capa 0 — Piloto (hecha ✅) | 3 Champions (Desarrollo, Soporte, Infraestructura) | 🟢 Básica lograda 3/3 · 🔵 Profesional en curso |
| Capa 1 — Dirección IT | Equipo directivo | 🟢 Básica (casos de uso reales de su gestión) |
| Capa 2 — Universidad | Docentes y personal administrativo | 🟤 Permiso → 🟢 Básica |
| Capa 3 — Comunidad | Estudiantes | 🟤 Permiso (alfabetización) |

---

*Documento vivo — se actualiza con cada ciclo de certificación. Fuente normativa: `00_marco/Licencia_Conduccion_AI.md` y `00_marco/Manual_Implementacion_Estrategica.md`.*
