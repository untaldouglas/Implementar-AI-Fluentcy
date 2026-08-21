# Glosario Consolidado — AI Fluency UJMD

**Programa AI Fluency · Modelo de Conducción AI (MCA) · Dirección de Servicios Informáticos**
**Gestor del glosario:** Hermes Agent (responsabilidad asignada por Douglas, 19/08/2026)
**Actualización:** se agregan términos en cada cierre de sesión y al adoptar nuevas herramientas/decisiones. Este archivo es la versión consolidada y versionada (git); el espejo vivo está en Drive `02_Conocimiento_Colectivo/Glosario del dominio` (fuente de verdad para humanos).

> **Formato de cada entrada:** Término | Definición | Ejemplo de uso real en el programa | Aportado por | Fecha.
> **Política:** solo entran términos con caso real de uso en el programa (no definiciones teóricas sin anclaje). Se referencia desde las guías personalizadas, el NotebookLM y las comunicaciones.

---

## A. Términos del dominio técnico y operativo (consolidados 17/07/2026)

| Término | Definición | Ejemplo de uso real | Aportado por | Fecha |
|---|---|---|---|---|
| Hardening | Endurecimiento de seguridad: reducir la superficie de ataque de un sistema eliminando servicios innecesarios o configurando políticas de acceso estrictas. | Aplicado por Patrick al delegar tareas de infraestructura a Hermes, excluyendo IPs y credenciales de los prompts (delegación segura, verificada 10/07). | Patrick | 17/07/2026 |
| LDAP | Protocolo para acceder y mantener servicios de directorio (ej. Active Directory). | Usado en el skill `ad-reporting` de Patrick para automatizar reportes de altas/bajas en Active Directory con PowerShell + LDAPFilter. | Patrick | 17/07/2026 |
| OAuth | Estándar abierto para delegar acceso a recursos sin exponer las credenciales del usuario. | Relevante en el skill `google-workspace-reporting` de Patrick, que orquesta reportes de auditoría sin exponer contraseñas. | Patrick | 17/07/2026 |
| Principio de Menor Privilegio | Un usuario o proceso solo debe tener los permisos mínimos necesarios para su tarea. | Criterio que Patrick aplica al decidir qué datos excluir de un prompt antes de delegarlo a Hermes (SOUL.md, Administrador Senior de Infraestructura). | Patrick | 17/07/2026 |
| Segregación de Funciones | Control interno que divide responsabilidades para evitar que una sola persona controle totalmente una operación crítica. | Aplica al esquema de permisos de Drive: ningún Champion usa su carpeta personal como fuente de evidencia oficial. | Patrick | 17/07/2026 |
| Subagente | Instancia de un agente AI con un rol acotado que se invoca dentro de una tarea mayor, en vez de resolver todo en una sola conversación. | `verificar_evidencia_drive.py` se ejecutó como puente automatizado para detectar evidencia de Champions enterrada en carpetas personales (17/07). | Claude Code (consolidado) | 17/07/2026 |
| Skill (SKILL.md) | Procedimiento reutilizable de un agente AI, documentado y versionado: trigger, procedimiento, pitfalls, verificación. | Los 8 skills custom auditados por Patrick (`ad-reporting`, `google-workspace-reporting`, etc.) y los 3 skills de F1 versionados en el repo del equipo. | Patrick | 16/07/2026 |
| Iterative Refinement | Técnica de prompting: pedir un primer análisis y luego refinar iterativamente hasta obtener el resultado deseado. | Usada por Mario para refactorizar el método de capitalización de un sistema legacy con C# y validar cada iteración. | Mario | 17/07/2026 |
| Chain of Thought | Técnica de prompting que pide al agente desglosar su razonamiento paso a paso antes de responder. | Usada por Mario para generar la suite de pruebas NUnit del módulo refactorizado (cada caso de prueba con su razonamiento). | Mario | 17/07/2026 |
| Few-Shot | Técnica de prompting que incluye ejemplos previos en el prompt para que el agente replique el patrón. | Aplicada por Mario junto con Chain of Thought al construir los casos de prueba del módulo legacy. | Mario | 17/07/2026 |
| Delegación segura | Criterio para decidir qué partes de una tarea son seguras para delegar a la IA y cuáles no (datos sensibles, decisiones). | Irvin identificó que su prompt de instalación remota no evaluaba riesgos; ajustó su delegación para no exponer credenciales. | Irvin | 17/07/2026 |
| Learning Record | Registro individual (no colectivo) del avance de cada Champion; vive en `01_piloto/learning_record/`. | Se diferencia de la carpeta colectiva de conocimiento: uno es avance personal, el otro es conocimiento del equipo. | Claude Code (consolidado) | 17/07/2026 |
| gdai / conector Drive | Vía de acceso a la carpeta única de Drive del programa, ya autenticada para el agente. | Usado para verificar en vivo, el 17/07, el contenido real de la carpeta de evidencia de los Champions. | Claude Code (consolidado) | 17/07/2026 |

## B. Términos del programa formativo (consolidados 14/08/2026, plantilla E8)

| Término | Qué es | Ejemplo de uso en el programa |
|---|---|---|
| MCA (Modelo de Conducción AI) | Marco del programa: la IA se aprende como conducir, en niveles progresivos L0–L9 con licencias que certifican competencia demostrada. | Todo el programa se rige por este marco; los itinerarios de F2 se calculan con él. |
| Niveles L0–L9 | Escala de competencia: de chat básico (L0, "Taxi") a orquestación multiagente (L9, "Flota Logística"). | El baseline asigna a cada participante su nivel de partida (F2: 5 en L1, 1 en L2). |
| Licencia | Certificación por nivel de competencia, con evidencia real y no verbal: Permiso 🟤 · Básica 🟢 · Profesional 🔵 · Avanzada 🟣. | F1 cerró con Licencia Profesional 🔵 3/3 firmada el 13/08. |
| Champion F1 | Participante del piloto ya certificado (Mario, Irvin, Patrick). En F2 actúan como facilitadores y validadores de evidencia. | Mario facilita a Stephanie y Oscar; Irvin a Jorge y Bryan; Patrick a Luis y Betty. |
| Coordinación | Área de la Dirección a la que pertenece cada participante: Infraestructura · Desarrollo · Sistemas. | Los KPIs E8 se eligen por coordinación (uno por área). |
| Baseline | Diagnóstico inicial (Google Form) que mide el nivel de partida de cada participante antes del kickoff. | F2: 6/6 respuestas recibidas 14–18/08, analizadas el 19/08. |
| Itinerario | Ruta de aprendizaje individual definida según el resultado del baseline (no hay ruta única). | Hoja `ITINERARIOS` del spreadsheet de la fase; base de las guías de 14 días. |
| Hermes Agent | Orquestador de IA del programa (Nous Research): la herramienta que cada participante configura y usa en su trabajo real. | Se instala y verifica en el setup guiado del kickoff F2 (lección L3 de F1). |
| SOUL.md | Archivo de configuración del agente por puesto/área: disparadores de rol, reglas de manejo de datos y skills esperadas. | Plantillas por área en `01_piloto/SOUL_plantillas/`; entregable E2 de F2. |
| MCP | Protocolo que conecta al agente con sistemas corporativos (ERPNext, Google Workspace, AD…) para operar sobre datos reales (entregable E5). | El programa ya usa MCPs de ERPNext y Google Workspace; E5 busca el primer MCP corporativo funcional. |
| Gateway Bifrost | Punto único de consumo de LLM credits (E6): permite medir cuánto consume cada persona y controlar el presupuesto (E7, $200/mes). | Pendiente de instalar en F2 (decisión D6 en la reunión de planificación). |
| LLM credits | Unidades de consumo de los modelos de IA; se presupuestan y se miden con el gateway. | Presupuesto E7: $200/mes para el cohorte F2. |
| Evidencia real | Entregable verificable (documento, captura, medición, commit). Regla del programa: lo verbal no cuenta. | Los 22 compromisos C1–C22 de F1 se cerraron con evidencia aprobada en Drive. |
| Rúbrica | Criterios de validación contra los que se revisa la evidencia. | Los Champions F1 validan la evidencia de F2 con rúbrica; Douglas co-firma (esquema transitorio). |
| Drive Approvals | Flujo de aprobación en Google Drive: el Champion F1 valida con rúbrica y Douglas co-firma. | Flujo estándar de validación de evidencia del programa (F1: C14–C22). |
| KPI | Indicador de valor de negocio elegido por coordinación (E8): mide el impacto real del uso de IA en la operación. | Candidatos F2: altas/bajas AD (Infraestructura), refactor legacy (Desarrollo), tickets ERPNext (Sistemas). |
| Línea base | Medición ANTES de usar IA (proceso actual). El DESPUÉS se compara contra ella para calcular el delta. | Se mide en la semana 1–2 de F2; cada plantilla E8 tiene su sección ANTES. |
| Delta | Diferencia entre el después y el antes (ej.: −1.2 h = −28%): el número que se presenta en el Demo Day F2. | Meta sugerida de F2: −30% vs línea base por coordinación. |
| C19 (F1) | Plantilla del piloto para medir un proceso antes/después con evidencia: la metodología base de la plantilla KPI E8. | F1: 6 procesos medidos con esta metodología; se replica en F2 vía E8. |
| E1–E8 | Entregables del cohorte F2 (ver plan de cohorte). E8 = métricas de valor de negocio. | Cada entregable tiene responsable y evidencia de cumplimiento definidos (plan_cohorte §3). |
| Demo Day F2 | Evento de cierre donde cada coordinación presenta sus KPIs y deltas ante la Dirección. | Cierre de la ventana F2 (2026-08 a 2026-09). |
| ERPNext | Sistema de gestión de Issues/Tasks de la DSI: fuente de datos típica de los KPIs de Sistemas. | KPI candidato de Jorge: tiempo de resolución de ticket ERPNext. |
| AD (Active Directory) | Directorio de cuentas corporativas: fuente de datos típica de los KPIs de Infraestructura. | KPI candidato de Luis: tiempo de alta/baja de cuentas AD. |
| Uptime | Porcentaje de tiempo en que un servicio está disponible: KPI típico de Infraestructura. | Alternativa del catálogo E8 para la coordinación de Infraestructura. |

## C. Términos nuevos de F2 (agregados 19/08/2026)

| Término | Definición | Ejemplo de uso real | Aportado por | Fecha |
|---|---|---|---|---|
| Guía personalizada (14 días) | Artefacto de aprendizaje individual por participante, generado con metodología Teach: 14 días estructurados en 2 semanas con ejercicios anclados a las funciones reales del puesto. | 6 guías generadas el 19/08 en `docs/fase2/` (Luis, Jorge, Stephanie, Betty, Bryan, Oscar) + copias en Drive F2_03. | Hermes Agent (gestor) | 19/08/2026 |
| Facilitador (R9) | Champion F1 que acompaña a un grupo de participantes de la fase nueva: co-facilita sesiones y valida evidencia. | F2: Irvin→Jorge+Bryan · Patrick→Luis+Betty · Mario→Stephanie+Oscar. | Douglas | 19/08/2026 |
| Gemini + Workspace | Solución de las primeras actividades de aprendizaje (decisión 19/08, matizada el mismo día): la universidad ya la tiene en su contrato Workspace for Education; sustituye a Claude/Copilot para esa etapa. | Las guías F2 practican primero con Gemini (D1–D10); desde D11 se introduce Hermes Agent como herramienta de trabajo. | Douglas | 19/08/2026 |
| Hermes Agent (herramienta de trabajo) | Herramienta de trabajo del programa: gestiona los recursos de IA que se usen y definan en el proyecto (memory, tools, skills, profiles), permitiendo portabilidad estandarizada del conocimiento entre fases, perfiles y equipos. | Las guías F2 lo introducen en D11–D12 y se usa como herramienta de trabajo durante todo el programa. | Douglas | 19/08/2026 |
| NotebookLM | Asistente de consulta y aprendizaje del proyecto (Google): responde preguntas sobre el programa y las herramientas con base en las fuentes del proyecto. | Se promueve desde el kickoff F2 y se enlaza en el Día 1 de cada guía: notebook.google.com/notebook/47737000-b53d-42ad-93aa-1cc1ba0c9560 | Douglas | 19/08/2026 |
| Clasificación de activos (ISO 27001) | Tabla por participante que clasifica la información de su área (Interno/Confidencial/Restringido) y decide qué se comparte con la IA y qué nunca. | Ejercicio del Día 6 de todas las guías F2; control A.5.9/A.5.12 de ISO 27001. | Hermes Agent (gestor) | 19/08/2026 |
| Acta de selección de participantes | Documento formal (ref AI-FLUENCY-2026-002) que oficializa la incorporación de los participantes de la fase; se firma en el kickoff. | Creada el 19/08; firma en el kickoff 21/08 con Champions F1 como testigos. | Douglas | 19/08/2026 |

---

*Glosario consolidado · Piloto AI Fluency UJMD · Gestor: Hermes Agent (desde 19/08/2026) · Fuentes: spreadsheet Drive `Glosario_Dominio` (17/07) + plantilla E8 (14/08) + sesión 19/08*
