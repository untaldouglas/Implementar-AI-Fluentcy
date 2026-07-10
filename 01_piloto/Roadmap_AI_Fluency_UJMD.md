# Roadmap de AI Fluency — Dirección de Informática UJMD
**Versión:** 2.0 | **Fecha:** Junio 2026 | **Framework:** Modelo de Conducción AI (MCA) | **Herramienta:** Hermes Agent (NousResearch) | **Autor:** @untaldouglas

---

## Contexto de partida

| Dimensión | Estado actual |
|---|---|
| Equipo total | 10–25 personas distribuidas en 3 áreas |
| Nivel de AI | Heterogéneo: brecha notable entre miembros avanzados y novatos |
| Objetivo | Uso productivo diario + capacidad de construir soluciones con IA |
| Estrategia | Piloto de 1 mes → escala al equipo completo |
| Framework | Modelo de Conducción AI (MCA) — escala L0–L9, 5 licencias certificables |
| Herramienta central | Hermes Agent (NousResearch, open source) — orquestador universal del programa |

---

## Principio rector

> **"Homogenizar hacia arriba, no hacia el mínimo común."**
> El piloto no busca que todos sepan lo mismo, sino que todos alcancen un umbral funcional desde el cual seguir creciendo de forma autónoma.

---

## Fase 0 — Preparación del terreno *(Semanas -1 a 0)*

**Antes de arrancar el piloto, el Director debe completar:**

### 0.1 Selección de los 3 Agentes Piloto
- Criterio de selección: **no el más avanzado ni el más novato** — elegir la persona de cada área con mayor apertura al cambio y capacidad de transferir conocimiento.
- Rol que asumen: **AI Champion de su área** al finalizar el piloto.

### 0.2 Diagnóstico de Conducción AI (baseline)
Aplicar el cuestionario de diagnóstico MCA (15–20 min) a los Champions para mapear:
- Herramientas de IA que usan actualmente y con qué frecuencia
- Casos de uso donde ya aplican IA (aunque sea informalmente)
- Bloqueos percibidos: técnicos, de confianza, de tiempo
- **Resultado:** nivel L0–L9 estimado → licencia de entrada → itinerario personalizado
- **Instrumento:** `google_form/crear_form_conduccion_ai.gs` → `make create-form`

### 0.3 Setup técnico de Hermes Agent
- Clonar repositorio: `github.com/nousresearch/hermes-agent`
- Definir entorno compartido (local o servidor interno UJMD)
- Configurar SOUL.md inicial por área (`SOUL_plantillas/`) y acceso para los 4 Champions
- Documentar el setup para facilitar la escalada posterior

### 0.4 Definir métricas de éxito del piloto
Antes de iniciar, acordar qué se medirá al final del mes:
- ¿Cuántos casos de uso propios resolvió cada piloto con IA?
- ¿Puede el piloto explicar y enseñar lo aprendido a un colega?
- ¿Se construyó al menos 1 agente funcional por área?

---

## Fase 1 — Piloto "3 Champions" *(Mes 1)*

> **Participantes:** 1 persona por cada una de las 3 áreas.
> **Formato:** Sesiones semanales de 2h + trabajo autónomo guiado entre sesiones.
> **Facilitador:** El Director (tú) + recursos autoguiados.

---

### 🗓 Semana 1 — Fundamentos y nivelación

**Objetivo:** Que los 3 pilotos partan del mismo punto conceptual, sin importar su nivel previo.

| Actividad | Descripción |
|---|---|
| Sesión 1 (2h) | "¿Qué es el Modelo de Conducción AI y por qué importa en TI?" — marco conceptual, diferencia entre usar IA y conducirla |
| Tarea autónoma | Exploración libre: usar cualquier herramienta de IA para resolver un problema real del trabajo diario y documentar el resultado |
| Lectura guiada | Introducción a LLMs, prompting básico, y qué es un agente de IA |
| Onboarding | Revisar `onboarding.html` — entender las 5 licencias y el itinerario personal |
| Hermes Agent | Instalar y ejecutar Hermes Agent siguiendo la guía de setup de Fase 0.3 — primer contacto con la herramienta del programa |

**Entregable de semana:** Cada piloto documenta 3 casos de uso potencial de IA en su área.

> **Aclaración 10/07/2026 (resuelve I1 de la auditoría #01):** el entregable obligatorio y verificable de S1 es **1 caso ancla completo + reflexión final (Día 7)**, tal como comunican las guías operativas (`docs/guia_*.html`). Los 3 casos de esta fila son la meta acumulada de **S1 + S2** (los otros 2 se completan/identifican en S2, ver entregable de Semana 2 abajo), no un requisito de cierre de S1 por sí solo. Ver `ESTADO_PROYECTO.md` → C14.

---

### 🗓 Semana 2 — Productividad personal con IA

**Objetivo:** Cada piloto integra IA en al menos 2 tareas reales de su trabajo semanal.

| Actividad | Descripción |
|---|---|
| Sesión 2 (2h) | Taller práctico: prompting efectivo, uso de Claude/ChatGPT/Copilot para tareas técnicas — documentación, análisis, drafting, debugging |
| Trabajo guiado | Aplicar IA a los 3 casos de uso identificados en S1 |
| Hermes Agent | Ejecutar los ejemplos del repositorio, entender la arquitectura del agente |
| Retrospectiva corta | Cada piloto comparte: ¿qué funcionó?, ¿qué no?, ¿qué sorprendió? |

**Entregable de semana:** Mini-reporte por piloto: "Cómo usé IA esta semana y qué impacto tuvo."

---

### 🗓 Semana 3 — Construcción de agentes con Hermes

**Objetivo:** Cada piloto construye un agente simple orientado a un problema real de su área.

| Actividad | Descripción |
|---|---|
| Sesión 3 (2h) | Workshop: Anatomía de un agente — tools, memory, reasoning. Cómo diseñar el "trabajo" de un agente antes de construirlo |
| Proyecto guiado | Cada piloto diseña y comienza a construir su agente de área con Hermes Agent |
| Ejemplos sugeridos por área | Infraestructura: agente de monitoreo / alertas; Desarrollo: agente de revisión de código o tests; Soporte: agente de triage de tickets o FAQ inteligente |
| Checkpoint | Revisión con el Instructor: ¿el agente resuelve un problema real? ¿es viable en 1 semana? |

**Entregable de semana:** Agente en estado funcional mínimo (aunque sea básico).

---

### 🗓 Semana 4 — Demo Day y lecciones aprendidas

**Objetivo:** Validar resultados, documentar aprendizajes y preparar la escalada al equipo completo.

| Actividad | Descripción |
|---|---|
| Demo Day (2h) | Cada piloto presenta su agente al Director y (si es posible) a su área. Énfasis en: problema que resuelve, cómo funciona, limitaciones |
| Retrospectiva del piloto | ¿Qué aprendimos sobre el proceso de aprendizaje? ¿Qué cambiaríamos para la escalada? |
| Entrevista de salida | Cuestionario de cierre para comparar con el baseline de Semana -1 |
| Plan de transferencia | Cada piloto diseña cómo presentará lo aprendido a su área en la Fase 2 |

**Entregables finales del piloto:**
- 3 agentes funcionales (1 por área)
- 3 mini-guías de "cómo integré IA en mi trabajo" (para usar en la escalada)
- Informe de lecciones aprendidas del piloto

---

## Fase 2 — Escalada al equipo completo *(Meses 2–3)*

> Los 3 Champions lideran la transferencia a sus áreas, con soporte del Director.

### Estructura de escalada

| Semana | Actividad |
|---|---|
| 5–6 | Champions presentan Demo Day a sus respectivas áreas. El equipo completo hace el diagnóstico baseline. |
| 7–8 | Sesiones de nivelación por área (adaptadas según el perfil del grupo). Los Champions facilitan, el Director respalda. |
| 9–10 | Cada miembro del equipo identifica y trabaja su propio caso de uso con IA. |
| 11–12 | Sesión plenaria: todos comparten sus casos de uso. Se define el catálogo inicial de "soluciones de IA de la Dirección de Informática." |

### Herramientas de soporte para la escalada
- **Repositorio interno de prompts** (compartido por el equipo, mantenido por Champions)
- **Canal dedicado** (Teams/Slack) para compartir hallazgos, errores y logros con IA
- **Biblioteca de agentes** basada en los desarrollados en el piloto

---

## Fase 3 — Institucionalización *(Meses 4–6)*

**De la adopción individual a la capacidad institucional.**

| Iniciativa | Descripción |
|---|---|
| Licencia de Conducción AI obligatoria | Nivel mínimo 🟢 Licencia Básica para todos los miembros del equipo — evaluado con el diagnóstico MCA |
| Catálogo de agentes internos | Inventario de agentes construidos, su propietario, estado y roadmap de mejora |
| Ciclo de mejora continua | Reunión mensual de 1h: "IA en la Dirección" — novedades, nuevos casos de uso, mejoras a agentes existentes |
| Expansión a otras áreas UJMD | Los Champions de la Dirección pueden replicar el modelo hacia otras unidades de la universidad |

---

## Resumen visual del roadmap

```
SEMANA -1 a 0   │  Selección de Champions + Diagnóstico MCA + Setup técnico
─────────────────┼──────────────────────────────────────────────────────────
MES 1 - PILOTO  │  S1: Fundamentos MCA   S2: Productividad personal
(4 Champions)   │  S3: Construcción IA   S4: Demo Day + Licencias iniciales
─────────────────┼──────────────────────────────────────────────────────────
MESES 2-3       │  Escalada al equipo completo
(Equipo)        │  Champions certifican a sus áreas (🟤→🟢→🔵)
─────────────────┼──────────────────────────────────────────────────────────
MESES 4-6       │  Institucionalización
(Dirección)     │  🏆 Primer Instructor interno + Catálogo + Ciclo mensual
```

---

## Riesgos y mitigaciones

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Brecha técnica bloquea a novatos | Media | Empezar con herramientas no-code la primera semana; agentes en S3+ |
| Champions no tienen tiempo para facilitar la escalada | Alta | Acordar dedicación explícita (2h/semana) antes del piloto |
| El equipo vuelve a sus hábitos sin IA después del piloto | Media | Sistema de licencias + canal activo + reunión mensual obligatoria |
| Herramienta de IA elegida tiene curva de aprendizaje alta | Media | El diagnóstico MCA identifica esto en Fase 0; se adapta el itinerario |

---

## Próximos 3 pasos concretos

1. **Esta semana:** Confirmar los 4 Champions (uno por área + Director como Instructor)
2. **Esta semana:** Crear y distribuir el Google Form de diagnóstico (`make create-form`)
3. **Semana que viene:** Revisar resultados del diagnóstico MCA y agendar la Sesión 1

---

*Roadmap del Modelo de Conducción AI — @untaldouglas · Dirección de Informática UJMD · v2.0*  
*Herramienta de implementación: [Hermes Agent (NousResearch)](https://github.com/nousresearch/hermes-agent)*
