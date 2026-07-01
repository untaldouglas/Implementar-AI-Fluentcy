# Acta de Selección de Champions — Piloto AI Fluency
**Dirección de Servicios Informáticos · UJMD**  
**Fecha de emisión:** 26 de junio de 2026  
**Ref:** AI-FLUENCY-2026-001 | Piloto Mes 1

---

## 1. Contexto

En cumplimiento con la **Fase 0.1 del Roadmap AI Fluency UJMD**, y siguiendo el criterio del principio rector — *"homogenizar hacia arriba, no hacia el mínimo común"* — se seleccionan los Champions que liderarán la primera fase del piloto de adopción de IA en la Dirección de Servicios Informáticos.

### Criterios de selección aplicados

| Criterio | Justificación |
|---|---|
| Mayor apertura al cambio | Capacidad demostrada de adoptar nuevas herramientas y metodologías |
| Capacidad de transferir conocimiento | Posición natural como referente en su equipo, no necesariamente experto técnico |
| Representatividad por área | 1 Champion por cada una de las 3 áreas de la Dirección + Director como arquitecto |
| Complementariedad de roles | Cubrir los 3 perfiles SOUL.md del equipo |

### Modelo de referencia

El modelo **Manual de Implementación Estratégica (10 niveles de autonomía vehicular)** establece que los Champions deben avanzar desde L0 a L5 durante el piloto, construyendo 1 agente funcional por área antes del Demo Day.

---

## 2. Champions seleccionados

| # | Nombre | Correo institucional | Rol en UJMD | Área asignada | Rol Piloto | Perfil SOUL |
|---|---|---|---|---|---|---|
| 1 | **Douglas Galindo** | dagalindo@ujmd.edu.sv | Director de Servicios Informáticos | Dirección + Liderazgo transversal | Arquitecto del sistema + Champion líder | Director (SOUL.md existente) |
| 2 | **Irvin Josué Morales Parada** | ijmoralespa@ujmd.edu.sv | *(rol operativo a confirmar)* | **Soporte / Mesa de Servicios** | Champion de área — Soporte | Consultor Lean/ITIL |
| 3 | **Mario Edgardo Valencia Campos** | mevalenciac@ujmd.edu.sv | *(rol operativo a confirmar)* | **Desarrollo** | Champion de área — Desarrollo | Renacentista técnico |
| 4 | **Patrick Eduardo Orellana Amaya** | peorellanaa@ujmd.edu.sv | *(rol operativo a confirmar)* | **Infraestructura** | Champion de área — Infraestructura | Consultor técnico + Renacentista |

---

## 3. Roles y responsabilidades

### 3.1 Douglas Galindo — Arquitecto del sistema + Champion líder

**Responsabilidades:**
- Diseñar y mantener la arquitectura de Hermes Agent (orquestador universal)
- Facilitar las sesiones semanales de 2h durante el piloto
- Garantizar la alineación entre Manual conceptual, Roadmap operativo y ejecución real
- Construir los 3 SOUL.md de área y los artifacts del piloto
- Reportar impacto a Rectoría vía métricas Flow integradas
- Avanzar personalmente a Nivel 8-9 (Piloto Automático)

**Nivel baseline esperado:** Nivel 8 (ya opera cron jobs) — meta L9 durante piloto.

### 3.2 Patrick Eduardo Orellana Amaya — Champion de Infraestructura

**Responsabilidades:**
- Construir agente funcional de infraestructura en Mes 1 (Skill: `infra-triage-incidentes` o similar)
- Aplicar SOUL.md de Infraestructura en todas las sesiones
- Transferir conocimiento al equipo de Infraestructura en Fase 2
- Documentar casos de uso reales del área en repo `mihermes`

**Meta de progresión:** L2 → L5 durante el piloto.

**Skills esperados al finalizar el piloto:**
- `infra-triage-incidentes` — clasificación automática de alertas
- `infra-report-capacidad` — reporte automático de uso de servidores
- `infra-automation-scripts` — generación asistida de scripts operativos

### 3.3 Mario Edgardo Valencia Campos — Champion de Desarrollo

**Responsabilidades:**
- Construir agente funcional de desarrollo en Mes 1 (Skill: `dev-code-review` o `dev-generar-tests`)
- Aplicar SOUL.md de Desarrollo en todas las sesiones
- Transferir conocimiento al equipo de Desarrollo en Fase 2
- Documentar casos de uso reales del área en repo `mihermes`

**Meta de progresión:** L2 → L5 durante el piloto.

**Skills esperados al finalizar el piloto:**
- `dev-code-review` — revisión automática de PRs con checklist de seguridad
- `dev-generar-tests` — suite de pruebas a partir de código existente
- `dev-adr-generator` — decisiones de arquitectura documentadas

### 3.4 Irvin Josué Morales Parada — Champion de Soporte

**Responsabilidades:**
- Construir agente funcional de soporte en Mes 1 (Skill: `soporte-triage-tickets` o `soporte-faq-generator`)
- Aplicar SOUL.md de Soporte en todas las sesiones
- Transferir conocimiento al equipo de Soporte en Fase 2
- Documentar casos de uso reales del área en repo `mihermes`

**Meta de progresión:** L2 → L5 durante el piloto.

**Skills esperados al finalizar el piloto:**
- `soporte-triage-tickets` — clasificación ITIL + prioridad + routing
- `soporte-faq-generator` — artículos de base de conocimiento
- `soporte-reporte-mensual` — métricas Flow + ITIL automáticas

---

## 4. Mecánica de trabajo del piloto

| Elemento | Detalle |
|---|---|
| **Duración del piloto** | Mes 1 (4 semanas) |
| **Sesiones** | Semanales de 2h, facilitadas por Douglas |
| **Herramienta central** | Hermes Agent (NousResearch) — instalado localmente + vía servidor interno UJMD |
| **Backends de modelo** | OpenRouter (principal) + Groq / Ollama / NVIDIA (alternativas gratuitas) — intercambiables |
| **Repositorio** | `untaldouglas/mihermes` — skills versionados por área |
| **Comunicación** | Canal dedicado (Teams/Slack) + reunión semanal sincrónica |
| **Entregables por Champion** | 1 agente funcional (Skill completo) + 1 mini-guía de integración IA |

---

## 5. Calendario de sesiones

| Semana | Fecha (estimada) | Tema | Facilitador |
|---|---|---|---|
| S0 | Por confirmar | Aplicación cuestionario baseline + setup | Douglas |
| S1 | Por confirmar | Fundamentos y nivelación | Douglas |
| S2 | Por confirmar | Productividad personal con IA | Douglas + Champions |
| S3 | Por confirmar | Construcción de agentes con Hermes | Douglas + Champions |
| S4 | Por confirmar | **Demo Day** + lecciones aprendidas | Douglas |

> **Nota:** Las fechas exactas se definirán en coordinación con los 3 Champions tras la aplicación del cuestionario baseline (Fase 0.2).

---

## 6. Compromisos formales

Cada Champion, al firmar/confirmar este acta, se compromete a:

1. **Dedicación:** Mínimo 2h/semana en el piloto más el trabajo autónomo entre sesiones
2. **Entregables:** Completar el agente funcional del área asignada antes del Demo Day
3. **Transferencia:** Liderar la presentación de resultados a su área en Fase 2
4. **Documentación:** Mantener en el repo todos los artifacts generados (Skills, SOUL.md, guías)
5. **Confidencialidad:** Respetar el protocolo de control de datos (mocks sintéticos, no subir datos sensibles a la nube)

El Director (Douglas) se compromete a:
- Facilitar las 4 sesiones del piloto
- Proveer la infraestructura (Hermes Agent, acceso a API keys de OpenRouter/Groq, documentación)
- Apoyar a los Champions con problemas técnicos fuera de sesión
- Reportar impacto institucional a Rectoría

---

## 7. Relación con otros artifacts del proyecto

| Artifact | Rol en este acta |
|---|---|
| Roadmap AI Fluency UJMD | Este acta cumple Fase 0.1 (selección de Champions) |
| Manual de Implementación Estratégica (actualizado) | Marco conceptual; los niveles L0-L9 se mapean a la progresión de cada Champion |
| Alineación Estratégica | Documento puente que integra este acta con manual y roadmap |
| Cuestionario Baseline AI Literacy | Instrumento a aplicar en S0 (siguiente paso tras este acta) |
| SOUL.md plantillas (3 archivos) | Base de trabajo para cada Champion de área |

---

## 8. Próximos pasos

1. ✅ **Acta de selección emitida** (este documento)
2. 🔲 **Confirmación formal** de los 3 Champions de área (respuesta por correo)
3. 🔲 **Agendar S0** para aplicación del cuestionario baseline
4. 🔲 **Setup técnico** de Hermes Agent para los 3 Champions
5. 🔲 **Kick-off del piloto** tras confirmar S0

---

## 9. Firma digital

**Elaborado por:**  
Douglas Galindo  
Director de Servicios Informáticos  
Universidad Dr. José Matías Delgado  
26 de junio de 2026

**Champions confirmados:**
- Douglas Galindo (Arquitecto del sistema + Champion líder)
- Irvin Josué Morales Parada (Champion de Soporte)
- Mario Edgardo Valencia Campos (Champion de Desarrollo)
- Patrick Eduardo Orellana Amaya (Champion de Infraestructura)

---

*Este documento forma parte del proyecto AI Fluency UJMD, Fase 0 — Preparación. El proyecto completo tiene horizonte 6 meses (Fases 0-3) y utiliza Hermes Agent como orquestador universal, con el marco conceptual del modelo de 10 niveles de autonomía vehicular como referencia pedagógica.*
