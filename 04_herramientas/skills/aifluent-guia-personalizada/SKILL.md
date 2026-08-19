---
name: aifluent-guia-personalizada
description: Generar guías de 14 días por participante AI Fluency.
---

# Guía Personalizada de Aprendizaje — AI Fluency por Fase

Genera una guía de 14 días (HTML autocontenido + Google Doc en Drive) POR PARTICIPANTE, personalizada con su nivel baseline, funciones reales del puesto, facilitador asignado, bloqueos del itinerario y marcos de gestión (ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile). El artefacto se reutiliza y mejora en cada fase: al cerrar la fase, registrar lecciones en este skill.

## Precondiciones (verificar antes de generar)

1. **Baseline cerrado y analizado** (6/6 respuestas en tiempo) → hoja `NIVELES_MCA` con scores por participante.
2. **Itinerarios calculados** → hoja `ITINERARIOS` del spreadsheet de la fase (`F2_01_Baseline_RESTRINGIDO/Respuestas_Diagnostico_Conduccion_AI`).
3. **Funciones reales del puesto CONFIRMADAS por Douglas** — NUNCA usar títulos de documentos de RRHH en Drive sin confirmar (lección 19/08/2026: el documento oficial 008 "Coordinador de Operaciones" NO correspondía al rol real de Luis = Coordinador de Infraestructura y Seguridad Informática). Si hay duda: preguntar, no inventar.
4. **Grupos de facilitación asignados** (Champions F1 como facilitadores R9) — confirmados por Douglas.

## Pasos

### 1. Confirmar puestos y funciones (gate obligatorio)
- Preguntar a Douglas la función real de cada participante si no está documentada (él da la nomenclatura vigente, no RRHH).
- Mapear cada participante a su facilitador (ej. F2: Irvin→Jorge+Bryan · Patrick→Luis+Betty · Mario→Stephanie+Oscar).
- Registrar los grupos en memoria y en `01_piloto/cohortes/F<X>/plan_cohorte.md`.

### 2. Definir la estructura de la guía (14 días, 2 semanas)
- **Semana 1** (herramienta principal = Gemini con cuenta institucional): D1 prompts (rol+tarea+contexto) · D2 3 prompts reales del puesto · D3 contexto/memoria · D4 refinamiento · D5 nivel L2 (IA lee archivos del área) · D6 tabla de clasificación de activos (ISO 27001) · D7 caso real de la semana · D8 revisión con facilitador.
- **Semana 2**: D9 marcos (ITIL/COBIT — según el rol) · D10 LEAN (desperdicios, PDCA, línea base antes/después) · D11 introducción a Hermes (complemento) · D12 Hermes con caso real · D13 PRINCE2/agile (mini-proyecto) + medición delta · D14 entrega, reflexión, validación (facilitador + co-firma Douglas).
- Cada día: concepto clave, práctica, checklist interactivo, alerta de seguridad, bloque de evidencia, navegación día↔día.

### 3. Personalizar por participante
- **Funciones del puesto**: ejercicios anclados a tareas REALES (según la descripción de Douglas, no RRHH).
- **Marcos por rol**:
  - Infraestructura/Seguridad (Luis): ITIL gestión de incidentes/cambios · COBIT RACI · ISO 27001 clasificación de activos · NIST · LEAN PDCA · PRINCE2 (plan de proyecto de seguridad).
  - Sistemas/Operaciones (Jorge): ITIL escalamiento de incidentes · COBIT · ISO 27001 · LEAN · PRINCE2.
  - Desarrollo/Mantenimiento (Stephanie/Oscar): agile/SCRUM (sprints, backlog) · ITIL gestión de cambios · COBIT RACI · SDLC seguro/OWASP · LEAN · PRINCE2.
  - Mesa de Servicio (Betty/Bryan): ITIL service desk (solicitudes, incidentes) · ISO 27001 (datos personales) · LEAN (tiempos de atención).
- **Seguridad de datos transversal**: banner en toda la guía + alerta en CADA día + tabla de clasificación de activos adaptada al área (6+ filas: qué se comparte con IA / qué nunca).
- **Bloqueos del itinerario**: integrar el "bloqueo a trabajar" de la hoja ITINERARIOS (ej. acceso/permisos para Jorge; qué SÍ/NO subir para Betty/Bryan).
- **Herramientas**: Gemini primero (D1–D10), Hermes como complemento (D11–D12), integración (D13).

### 4. Generar los artefactos
1. **HTML autocontenido** en `docs/fase<X>/guia_<nombre>.html` — reutilizar el CSS/estructura de la guía de Luis (docs/fase2/guia_luis_molina.html) como plantilla base; generar el resto con script (patrón: /tmp/generar_guias_f2.py) para consistencia.
2. **Google Docs en Drive** carpeta `F2_03_Sesiones_Material` (o F<X>_03): subir el HTML con mimeType `application/vnd.google-apps.document` (conversión HTML→Doc) — nombre: "Guía 14 Días — <Nombre> (F<X>)".
3. **Índice navegable** `docs/fase<X>/index.html` (replicar estilo fase1) + tarjeta en `docs/index.html` (actualizar estado de la fase en el subtitle).

### 5. Actualizar artefactos del programa (no olvidar)
- `01_piloto/cohortes/F<X>/plan_cohorte.md`: niveles baseline, grupos de facilitación, entregables.
- `ESTADO_PROYECTO.md`: fecha, fase actual, próximo hito, entrada de log con lo completado.
- `README.md`: estado general + árbol con `docs/fase<X>/`.
- `04_herramientas/agendas/agenda_kickoff_f<X>.md`: agregar las guías al material de apoyo y al bloque "Tu itinerario" (el participante recibe SU guía en el kickoff).
- Emails/notificaciones si aplica (borrador Gmail a participantes con sus guías).

### 6. Cerrar con el ritual
`make cierre-sesion MSG="..."` (verifica evidencia Drive → consistencia → commit → push dual repozone + GitHub).

## Mejora continua del skill (al cerrar cada fase)
- Registrar aquí las lecciones aprendidas (ej. F2: usar funciones reales confirmadas, NO títulos RRHH; 14 días en vez de 7; Gemini como herramienta principal).
- Al iniciar una fase nueva, copiar la estructura baseline de la fase anterior (carpeta F<X>_01_Baseline_RESTRINGIDO + spreadsheet) — instrucción de Douglas 19/08.

## Pitfalls
- NO usar títulos de RRHH de Drive como autoridad del puesto — Douglas define la función real (corregido 19/08: Luis).
- NO subir datos sensibles a Drive público: la carpeta baseline es RESTRINGIDA y nunca se publica.
- NO generar guías sin confirmar facilitadores y funciones (gate del paso 1).
- Los .docx de Drive no se exportan como texto vía API (binarios ZIP) — descargar y extraer word/document.xml para leerlos.
