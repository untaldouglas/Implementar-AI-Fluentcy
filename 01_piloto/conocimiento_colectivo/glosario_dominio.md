# Glosario del Dominio — Piloto Champions

> Términos técnicos y de AI Fluency que los Champions usan en su día a día. Ver convención de
> actualización en [_dashboard.md](_dashboard.md).
>
> **Consolidado el 17/07/2026 por Claude Code** (decisión de Douglas: C17 es un compromiso de
> formalización/consolidación de conocimiento ya disperso, no de medición individual como C19,
> por lo que es apropiado que se complete así). Fuente: aporte real de Patrick (glosario de
> 10 términos, filtrado — se excluyeron 5 términos genéricos de ITIL/COBIT sin caso real de uso
> de Hermes: COBIT, Continuidad del Servicio, ITILv3, SLA, SOP) + términos reales extraídos de
> los casos C19 de Mario e Irvin + vocabulario operativo del propio piloto. Mirror en
> [Drive: Glosario_Dominio](https://docs.google.com/spreadsheets/d/1t07zfQySxfNYeExyKuN8_ETfozN-usDO1vaDA_F9HlA/edit) (fuente de verdad).

| Término | Definición (en palabras del Champion) | Ejemplo/contexto de uso | Agregado por | Fecha |
|---|---|---|---|---|
| Hardening | Endurecimiento de seguridad: reducir la superficie de ataque de un sistema eliminando servicios innecesarios o configurando políticas de acceso estrictas. | Aplicado por Patrick al delegar tareas de infraestructura a Hermes, excluyendo IPs y credenciales de los prompts (delegación segura, verificada 10/07). | Patrick | 17/07/2026 |
| LDAP | Protocolo para acceder y mantener servicios de directorio (ej. Active Directory). | Usado en el skill `ad-reporting` de Patrick para automatizar reportes de altas/bajas en Active Directory con PowerShell + LDAPFilter. | Patrick | 17/07/2026 |
| OAuth | Estándar abierto para delegar acceso a recursos sin exponer las credenciales del usuario. | Relevante en el skill `google-workspace-reporting` de Patrick, que orquesta reportes de auditoría sin exponer contraseñas. | Patrick | 17/07/2026 |
| Principio de Menor Privilegio | Un usuario o proceso solo debe tener los permisos mínimos necesarios para su tarea. | Criterio que Patrick aplica al decidir qué datos excluir de un prompt antes de delegarlo a Hermes (SOUL.md, Administrador Senior de Infraestructura). | Patrick | 17/07/2026 |
| Segregación de Funciones | Control interno que divide responsabilidades para evitar que una sola persona controle totalmente una operación crítica. | Aplica al esquema de permisos de Drive: ningún Champion usa su carpeta personal como fuente de evidencia oficial. | Patrick | 17/07/2026 |
| Subagente | Instancia de un agente AI con un rol acotado que se invoca dentro de una tarea mayor, en vez de resolver todo en una sola conversación. | `verificar_evidencia_drive.py` se ejecutó como puente automatizado para detectar evidencia de Champions enterrada en carpetas personales (17/07). | Claude Code (consolidado) | 17/07/2026 |
| Skill (SKILL.md) | Procedimiento reutilizable de un agente AI, documentado y versionado: trigger, procedimiento, pitfalls, verificación. | Los 8 skills custom auditados por Patrick (`ad-reporting`, `google-workspace-reporting`, `kanban-orchestrator`, etc.); pendiente formalizar 3 como SKILL.md real para Licencia Profesional. | Patrick | 16/07/2026 |
| Iterative Refinement | Técnica de prompting: pedir un primer análisis y luego refinar/refactorizar sobre ese análisis en una segunda pasada. | Usada por Mario para refactorizar el método de capitalización del módulo de Graduados: 45 min manual → 15 min con Hermes. | Mario | 17/07/2026 |
| Chain of Thought | Técnica de prompting que pide al agente desglosar su razonamiento paso a paso antes del resultado final. | Usada por Mario para generar la suite de pruebas NUnit del módulo de Graduados y las consultas SQL del tablero de Metabase. | Mario | 17/07/2026 |
| Few-Shot | Técnica de prompting que incluye ejemplos previos en el prompt para guiar el formato o criterio de la respuesta del agente. | Aplicada por Mario junto con Chain of Thought al construir las consultas SQL del tablero de autoevaluación en Metabase. | Mario | 17/07/2026 |
| Delegación segura | Criterio para decidir qué partes de una tarea son seguras para entregar a un agente AI sin exponer datos sensibles o de producción. | Irvin identificó que su prompt de instalación remota no evalúa el riesgo de incluir IPs/nombres de equipo — lo declaró como "punto de mejora" en vez de ignorarlo. | Irvin | 17/07/2026 |
| Learning Record | Registro individual (no colectivo) del avance de cada Champion: evidencia, autorreporte de nivel MCA, reflexiones. | Vive en `01_piloto/learning_record/`; se diferencia de esta carpeta (`02_Conocimiento_Colectivo`), que es la capa asociativa entre los 3 Champions. | Claude Code (consolidado) | 17/07/2026 |
| gdai / conector Drive | Vía de acceso a la carpeta única de Drive del piloto, ya autenticada, para leer/escribir evidencia sin depender de credenciales manuales. | Usado para verificar en vivo, el 17/07, el contenido real de las carpetas personales de Patrick e Irvin antes de la reunión de seguimiento. | Claude Code (consolidado) | 17/07/2026 |

**Pendiente:** Irvin y Mario aún no han aportado términos por iniciativa propia (solo se extrajeron de su evidencia de C19). Se espera que amplíen esta tabla directamente en la próxima colaborativa semanal.
