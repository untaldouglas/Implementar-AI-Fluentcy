# Alineación Estratégica: Manual × Roadmap × Perfil Director
**Versión:** 1.0 | **Fecha:** 26 junio 2026 | **Autor:** @untaldouglas

---

## 1. Propósito de este documento

Este documento resuelve las tres tensiones detectadas entre los documentos existentes:

| Tensión | Origen | Resolución propuesta |
|---------|--------|---------------------|
| **Herramientas** | Manual habla de Claude, Roadmap de Hermes | Hermes como orquestador universal — Claude como backend disponible |
| **Complejidad** | Manual asume arquitecto avanzado, Roadmap tiene equipo heterogéneo | Mapeo progresivo: cada persona avanza por niveles según su rol |
| **Conexión** | Documentos no se referencian entre sí | Cada fase del Roadmap se ancla explícitamente a un nivel del Manual |

---

## 2. Principio de alineación: "El Director como Arquitecto del Sistema"

Tu perfil SOUL.md define 3 roles operativos. Esta alineación los mapea a responsabilidades específicas dentro del roadmap de AI Fluency:

```
┌─────────────────────────────────────────────────────────────────┐
│  ROL RENACENTISTA                                               │
│  (Scripts, prototipos, debug, Ollama, refactor)                 │
│  → Diseña y construye los agentes que el equipo usará           │
│  → Resuelve la fricción técnica del setup                       │
│  → Nivel objetivo personal: 7-9 (Piloto Automático)             │
├─────────────────────────────────────────────────────────────────┤
│  ROL CONSULTOR                                                  │
│  (Procesos, Lean, Scrum, ITIL, SLA)                             │
│  → Traduce procesos del equipo en Skills/Playbooks              │
│  → Identifica "desperdicios" (muda) automatizables con IA       │
│  → Nivel objetivo para el equipo: 3-5 (Conductor)               │
├─────────────────────────────────────────────────────────────────┤
│  ROL DIRECTOR                                                   │
│  (Gobernanza, presupuesto, auditoría, riesgo)                   │
│  → Define métricas de éxito del piloto                          │
│  → Reporta impacto a Rectoría en términos de Flow               │
│  → Decide inversiones en infraestructura IA                     │
│  → Nivel objetivo institucional: estandarización (Fase 3)       │
└─────────────────────────────────────────────────────────────────┘
```

**Conclusión clave:** No eres un participante más del piloto. Eres el **arquitecto del sistema** que lo hace posible. Tu progresión en niveles (7–9) va por separado de la progresión del equipo (0→5).

---

## 3. Stack tecnológico unificado

El Manual menciona Claude como herramienta. El Roadmap posiciona Hermes. La resolución es una **arquitectura en capas**:

```
┌──────────────────────────────────────────────────────┐
│  CAPA 5: Agentes Especializados (lo que construyen)  │
│  → Hermes Agent + Skills/Playbooks                   │
├──────────────────────────────────────────────────────┤
│  CAPA 4: Orquestación (lo que tú operas)             │
│  → Hermes Agent como cerebro del sistema             │
│  → Cron jobs, multi-agente, delegación               │
├──────────────────────────────────────────────────────┤
│  CAPA 3: Modelos de IA (el motor, intercambiable)    │
│  → Claude (Anthropic) como modelo principal           │
│  → Ollama local como alternativa offline              │
│  → Otros según disponibilidad/costo                   │
├──────────────────────────────────────────────────────┤
│  CAPA 2: Contexto y memoria                          │
│  → Hermes memories, skills, SOUL.md, .claudedoc       │
│  → MCP servers (Slack, Drive, Notion, ERPNext)       │
├──────────────────────────────────────────────────────┤
│  CAPA 1: Infraestructura                             │
│  → Mac M4 + laptop Linux Pop!_OS 24.04               │
│  → Repo GitHub (untaldouglas/mihermes)                │
│  → Servidor interno UJMD (si aplica)                 │
└──────────────────────────────────────────────────────┘
```

**Regla para el equipo:** "Usamos Hermes Agent como interfaz y orquestador. El modelo que hay detrás (Claude, Ollama, etc.) es intercambiable y transparente para el usuario final."

Esto resuelve la disonancia: el Manual describe capacidades que se logran **usando Hermes como vehículo**, con Claude (u otros) como motor intercambiable.

---

## 4. Mapeo completo: Niveles × Fases × Rol Director

### 4.1 Tabla maestra de alineación

| Nivel Manual | Zona | Fase Roadmap | Quién lo alcanza | Entrega concreta |
|-------------|------|--------------|-------------------|------------------|
| **L0: El Taxi** | Pasajero | Fase 0 (preparación) | Todo el equipo (baseline) | Uso básico de ChatGPT/Claude web |
| **L1: El Chofer** | Pasajero | Fase 1, S1 | Equipo tras S1 | Memoria básica en chat, búsquedas web con IA |
| **L2: El Coche Propio** | Pasajero | Fase 1, S2 | Equipo tras S2 | Hermes instalado, archivo local indexado |
| **L3: Copiloto de Contexto** | Conductor | Fase 1, S3 | Champions + equipo avanzado | Proyectos configurados en Hermes |
| **L4: Copiloto con Manos (MCP)** | Conductor | Fase 2, S7-8 | Champions + equipo en escalamiento | MCP conectando Slack/Drive/ERPNext |
| **L5: Copiloto Entrenado** | Conductor | Fase 2, S9-10 | Equipo completo al finalizar | Skills propios del área operando |
| **L6: Vehículo Autónomo (Cowork)** | Autopilot | Fase 3 (institucionalización) | Champions + tú (Douglas) | Delegación multi-etapa funcionando |
| **L7: Vehículo Autónomo Total** | Autopilot | Fase 3 | Tú (Douglas, rol Renacentista) | Agentes con acceso a terminal |
| **L8: Agentes SDK** | Autopilot | Fase 3+ | Tú (Douglas) | Cron jobs autónomos (ya tienes 3) |
| **L9: Swarm Intelligence** | Autopilot | Visión futura | Tu área como referencia | Multi-agente debatiendo soluciones |

### 4.2 Tu progresión personal (Douglas, Director)

```
SEMANA -1 a 0    → Estás en Nivel 8 (ya tienes cron jobs activos)
                   → Meta: consolidar L8 y experimentar L9
MES 1 (piloto)   → Tú operas en L7-8 mientras llevas al equipo a L0-L2
MES 2-3          → Tú en L8-9, equipo escala a L3-L5
MES 4-6          → Institucionalizas: estándar UJMD-IT = L5 mínimo
```

### 4.3 Progresión del equipo (10-25 personas)

```
Fase 0          → Todos diagnosticados (L0 o L1)
Fase 1 (Mes 1)  → 3 Champions de L0→L3, resto a L1-L2
Fase 2 (Mes 2-3) → Champions L3→L5, resto L2-L4
Fase 3 (Mes 4-6) → Todos L4-L5, Champions L5-L6
```

### 4.4 Nueva fase: Estudiantes universitarios (Mes 7-9)

**Contexto:** La UJMD vincula el trabajo de la Dirección con la formación estudiantil. AI Fluentcy se extiende a estudiantes para potenciar su gestión del aprendizaje.

| Nivel | Aplicación estudiantil | Entregable |
|-------|------------------------|------------|
| L0-L1 | Uso básico de ChatGPT/Claude para resumir lecturas y organizar apuntes | Guías de "primeros pasos" |
| L2-L3 | Agentes con memoria que recuerdan cursos, proyectos, estilos de aprendizaje | SOUL.md estudiantil (por carrera) |
| L4-L5 | MCP conectando Google Classroom, Drive, bibliotecas digitales | Skills para gestión de aprendizaje |
| L6-L9 | Agentes autónomos que organizan cronogramas, generan resúmenes, preparan exámenes | Agentes personalizados por materia |

**Investigación asociada:** Esta fase es el caso de estudio para el protocolo de investigación aplicada (ver `Protocolo_Investigacion_AI_Fluentcy.md`).

---

## 5. Integración con tus herramientas actuales

### 5.1 Cómo tus skills existentes alimentan el Roadmap

| Tu skill actual | Aportación al Roadmap AI Fluency |
|----------------|----------------------------------|
| **director-flow-report** | Métricas de éxito cuantitativas: reducir Defect Flow%, mejorar Flow Efficiency con IA |
| **end-of-day** | Documentación automática del avance del piloto en LinkedIn (visibilidad institucional) |
| **SOUL.md (3 roles)** | Modelo de referencia: cada miembro del equipo puede tener su propio SOUL.md adaptado a su rol |
| **Cron jobs activos** | Evidencia viva de Nivel 8 funcionando — demo tangible para el equipo |
| **Repo mihermes** | Infraestructura de distribución: skills, memories, SOUL.md versionados para todo el equipo |

### 5.2 Nuevas herramientas a desarrollar (Rol Renacentista)

Para que el Roadmap funcione, necesitas construir (Fase 0, semanas -1 a 0):

| Artefacto | Propósito | Nivel que habilita |
|-----------|-----------|-------------------|
| **SOUL.md del equipo** | Plantilla adaptada por área (Infra, Desarrollo, Soporte) | L2-L3 para cada miembro |
| **Skills de área** | Playbooks Lean/ITIL específicos por área (ya mencionados en Manual, sección Aplicaciones Sectoriales) | L5 al finalizar Fase 2 |
| **Agente de monitoreo Flow** | Cron job que detecta anomalías en métricas Flow automáticamente | L8, conecta con director-flow-report |
| **Checklist de instalación Hermes** | Script + documento para que cada miembro instale en 30 min | L0→L2 rápido |
| **Cuestionario baseline** | Adaptado del Manual (nivel de AI literacy) | Diagnóstico Fase 0 |

---

## 6. Métricas de éxito integradas

Combinando las métricas cualitativas del Roadmap con las cuantitativas del Manual y tus Flow metrics:

### Métricas por fase

| Fase | Métrica cualitativa (Roadmap) | Métrica cuantitativa (Manual + Flow) | Cómo la mides |
|------|------------------------------|--------------------------------------|---------------|
| **Fase 0** | Champions seleccionados y con baseline | 100% de Champions tienen SOUL.md configurado | Checklist + git log |
| **Fase 1** | 3 agentes funcionales, 3 mini-guías | Reducción ≥20% en tiempo de 1 tarea recurrente por agente | Antes/después medido en Flow Time |
| **Fase 2** | Equipo usando IA en ≥2 tareas reales | Flow Efficiency de Defect sube 10%+ (IA acelera triage) | director-flow-report comparativo |
| **Fase 3** | Catálogo de agentes internos operativo | Flow Distribution — Debt <15% (automatización con IA) | Reporte trimestral a Rectoría |
| **Fase 4** | Estudiantes universitarios usando agentes | Mejora en promedio académico (≥0.3 puntos), autorregulación | Protocolo de investigación (pre-post) |

### Métricas de "Combustible" (del Manual)

| Indicador | Fórmula | Meta Fase 3 |
|-----------|---------|-------------|
| **Tasa de éxito en primer intento** | (respuestas sin iteración) / (total respuestas) | ≥70% (indica buen contexto inyectado) |
| **Tokens por tarea completada** | Promedio de tokens consumidos por resolución | Reducir 30% vs baseline (contexto más eficiente) |
| **Índice de alucinaciones** | Reportes de error por respuestas inventadas | <5% de interacciones totales |

---

## 7. Protocolo de control de datos aplicado al piloto

Alineado con tu SOUL.md ("Protocolo de Control de Tránsito de Datos"):

| Rol | Durante el piloto | Regla de datos |
|-----|-------------------|----------------|
| **Equipo en modo Director/Consultor** | Analizando métricas, reportando a jefes | PROHIBIDO usar datos ficticios para decisiones reales |
| **Equipo en modo Renacentista** | Construyendo agentes, probando código | OBLIGATORIO usar mocks sintéticos (estudiante_ejemplo_1) |
| **Douglas como Arquitecto** | Diseñando la infraestructura | Decide qué datos pueden indexarse localmente vs. qué debe quedar fuera |

---

## 8. Plan de acción inmediato (Próximos 14 días)

Tomando los "3 próximos pasos" del Roadmap y enriqueciéndolos con el Manual:

### Día 1-3: Decisión de stack (resuelve la disonancia de herramientas)

- [ ] Decidir y documentar: **Hermes Agent como orquestador, Claude como modelo principal vía API, Ollama para fallback local**
- [ ] Actualizar el Manual para que refleje esta arquitectura (Claude como backend, no como plataforma)
- [ ] Verificar que Hermes tenga acceso a Claude API para el equipo

### Día 4-7: Setup personal (Rol Renacentista)

- [ ] Construir plantilla de SOUL.md para el equipo (3 versiones: Infra, Desarrollo, Soporte)
- [ ] Crear checklist de instalación de Hermes (script + documento)
- [ ] Configurar 1 MCP server de ejemplo (ej: Google Drive) para demostrar Nivel 4
- [ ] Documentar tu configuración actual como "evidencia viva" de Nivel 8

### Día 8-10: Preparación del piloto

- [ ] Finalizar cuestionario baseline de AI literacy (adaptado del Manual)
- [ ] Identificar a los 3 Champions usando criterio del Roadmap (apertura al cambio, no nivel técnico)
- [ ] Agendar Sesión 1 de la Fase 1

### Día 11-14: Integración con tu flujo Director

- [ ] Configurar 1 cron job adicional: recordatorio semanal de avance del piloto
- [ ] Crear carpeta en repo `ai_fluency_piloto/` con esta alineación como documento maestro
- [ ] Redactar post de LinkedIn anunciando la iniciativa (rol Director, visibilidad institucional)

---

## 9. Resumen visual de la alineación completa

```
                    ┌─────────────────────────────┐
                    │  DOUGLAS (Arquitecto)        │
                    │  Nivel personal: L7-9        │
                    │  Rol: Renacentista+Director  │
                    └──────────────┬──────────────┘
                                   │ diseña y orquesta
                    ┌──────────────▼──────────────┐
                    │  3 CHAMPIONS (Mes 1)         │
                    │  Nivel target: L3→L5         │
                    │  Rol: Consultor (Lean/ITIL)  │
                    └──────────────┬──────────────┘
                                   │ facilitan y transfieren
                    ┌──────────────▼──────────────┐
                    │  EQUIPO (Mes 2-3)            │
                    │  Nivel target: L2→L5         │
                    │  Rol: usuario productivo     │
                    └──────────────┬──────────────┘
                                   │ institucionalización
                    ┌──────────────▼──────────────┐
                    │  INSTITUCIONALIZACIÓN (Mes 4-6)│
                    │  Estándar UJMD-IT: L5 mínimo │
                    │  Métricas Flow + AI KPIs     │
                    └──────────────┬──────────────┘
                                   │ expansión educativa
                    ┌──────────────▼──────────────┐
                    │  ESTUDIANTES UJMD (Mes 7-9)   │
                    │  Nivel target: L0→L3         │
                    │  Rol: aprendizaje asistido   │
                    │  + Investigación aplicada    │
                    └─────────────────────────────┘

STACK TECNOLÓGICO:
┌─────────────────────────────────────────────────┐
│  Hermes Agent (orquestador universal)            │
│  + Claude API (motor, interchangeable)           │
│  + Ollama local (fallback offline)               │
│  + MCP servers (Slack, Drive, ERPNext, Notion)   │
│  + Google Workspace UJMD (AGOSTO 2026) ← NUEVO   │
│  + Skills/Playbooks (memoria procedural)         │
│  + Repo mihermes (distribución versionada)       │
└─────────────────────────────────────────────────┘
```

---

## 10. Tarea técnica prioritaria: Integración Google Workspace UJMD

> **Nota de estado (17/07/2026 — resuelve I8 de la serie de auditorías):** esta sección describe la **integración técnica** (MCP server, service account, OAuth), planificada para agosto–octubre 2026 y aún **pendiente**. No confundir con el **esquema de uso manual** de Google Workspace, que ya opera en el piloto desde julio (C18 — ver `04_herramientas/agendas/2026-07-13_c18_esquema_workspace.md`): Drive como canal oficial de evidencia (decisión 10/07), Calendar para bloques y reuniones, Gmail con borradores de aprobación humana.

**Objetivo:** Conectar el dominio institucional `ujmd.edu.sv` (Google Workspace) con Hermes Agent para habilitar capacidades L3-L5 full-stack.

**Servicios a integrar:**
1. **Gmail** — Lectura/escritura de correos con validación humana
2. **Calendar** — Gestión de eventos, recordatorios automáticos
3. **Drive** — Indexación y lectura de documentos compartidos
4. **Meet** — Integración con agenda de reuniones
5. **Contactos** — Búsqueda y autocompletado

**Componentes técnicos:**
- **MCP server para Google Workspace** (API oficial de Google)
- **Service account** en Google Cloud Platform para el dominio UJMD
- **OAuth 2.0** con restricción al dominio `ujmd.edu.sv`
- **Políticas de permisos** por rol (Champions vs. equipo vs. estudiantes)

**Cronograma:**
- **Agosto 2026:** Arquitectura + service account GCP
- **Septiembre 2026:** MCP server piloto + primeras 3 integraciones (Gmail, Calendar, Drive)
- **Octubre 2026:** Despliegue a Champions + SOUL.md actualizado

**Riesgos:**
- Seguridad: el service account debe tener **principio de mínimo privilegio**
- Cumplimiento: revisar con legal UJMD el tratamiento de datos
- Dependencia: plan B si Google cambia API o precios

**Entregables:**
1. Documento de arquitectura de integración (`integracion_google_workspace.md`)
2. Service account configurado en GCP
3. 3-5 MCP skills básicos funcionando
4. SOUL.md con configuración de Google Workspace
5. Guía de setup para nuevos miembros

**Vinculación con investigación:** Esta integración es **insumo metodológico** para el protocolo de investigación aplicada (ver `Protocolo_Investigacion_AI_Fluentcy.md`). Sin Google Workspace, no se pueden medir las capacidades L4+ del modelo Gorsht en contexto real.

---

## 11. Dimensión de investigación aplicada

**Documento base:** `Protocolo_Investigacion_AI_Fluentcy.md`

**Objetivo:** Convertir el piloto en un estudio longitudinal publicable en revistas internacionales indexadas (Scopus, WoS).

**Líneas de investigación:**
1. **AI Fluentcy en equipos técnicos** — Progresión L0-L9 y correlación con métricas operativas
2. **AI Fluentcy en estudiantes** — Impacto en gestión del aprendizaje y rendimiento académico
3. **Métricas Flow + IA** — Relacionar adopción de agentes con mejora en Flow Efficiency

**Revistas objetivo:**
- **Tier 1 (Q1):** Computers & Education (Elsevier), The Internet and Higher Education
- **Tier 2 (Q2):** Education and Information Technologies (Springer)
- **Tier 3 (regionales):** RIES, RELATEC, EKS (Scopus)

**Hitos de investigación:**
- **Jul 2026:** Protocolo final + revisión de literatura
- **Ago 2026:** Aprobación comité de ética UJMD + pre-test Champions
- **Sep 2026:** Integración Google Workspace (necesaria para medición)
- **Mar 2027:** Post-test equipo + redacción primer manuscrito
- **Jun 2027:** Envío de manuscrito a revista Q1/Q2

**Contribuciones esperadas:**
- Primer estudio longitudinal del modelo Gorsht en LATAM
- Instrumento validado de AI Literacy técnica
- Evidencia empírica de IA en TI universitario latinoamericano
- Modelo replicable para otras universidades de la región

---

## 12. Conclusión: El efecto compuesto aplicado a tu rol

Tu ventaja como Director no es que sepas más IA que tu equipo — es que **diseñas la arquitectura del sistema** que permite que el equipo lo use productivamente. Esta alineación convierte:

- **El Manual** (conceptual, individual, Claude-céntrico) → en un marco de referencia para la progresión de niveles
- **El Roadmap** (operativo, de equipo, Hermes-céntrico) → en el plan de ejecución con fechas y entregables
- **Tu perfil** (Director/Consultor/Renacentista) → en el engine que hace posible ambos

**La progresión no es lineal, es exponencial** — y tú ya estás varios peldaños arriba del equipo. Tu misión inmediata no es subir tú más rápido, sino **construir los peldaños** para que los demás suban.

---

*Documento generado como puente entre el Manual de Implementación Estratégica y el Roadmap de AI Fluency UJMD, personalizado para el perfil institucional de Douglas Galindo, Director de Servicios Informáticos de la UJMD.*
