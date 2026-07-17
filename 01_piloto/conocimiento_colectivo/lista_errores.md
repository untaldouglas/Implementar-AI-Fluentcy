# Lista de Errores — Piloto Champions

> Errores/bloqueos encontrados en la práctica (Hermes, scripts, workflows, subagentes) y su
> solución o workaround. Ver convención de actualización en [_dashboard.md](_dashboard.md).
>
> **Creado el 17/07/2026 por Claude Code** (decisión de Douglas) — este artefacto no existía
> hasta hoy. Mirror en
> [Drive: Lista_de_Errores](https://docs.google.com/document/d/1NvZaDAuhY_itCQE0minAFXzIzoatg-RecphSLd1rkQ8/edit) (fuente de verdad).

| Error/síntoma | Causa | Solución/workaround | Agregado por | Fecha |
|---|---|---|---|---|
| El encabezado de un script no coincide con lo que el cuerpo realmente ejecuta (`monitor_servidores_pro.sh` de Patrick documenta CPU/disco, el cuerpo solo hace ping). | El script se fue ampliando/documentando por partes sin revisar línea a línea contra el encabezado original. | Detectado en la revisión del Acta de Licencia Básica (17/07); pendiente que Patrick lo corrija antes de formalizarlo como Skill. | Claude Code / Douglas | 17/07/2026 |
| Evidencia real de Champions quedó invisible para la verificación de compromisos (Patrick e Irvin subieron material de C17/C19 a sus carpetas personales de S2). | No existía una regla explícita ni plantilla que indicara la ubicación exacta antes de anunciar el compromiso. | Se construyó un puente automatizado (`verificar_evidencia_drive.py`) que escanea carpetas personales antes de dar un compromiso por "no recibido"; se publicaron plantillas-rúbrica con ubicación exacta. | Claude Code | 17/07/2026 |
| Confusión sobre cuál era la carpeta única de Drive del proyecto. | Dos cuentas de Google conectadas al mismo tiempo generaron ambigüedad sobre cuál era "la" carpeta oficial. | Se fijó una única carpeta y un único conector (gdai / cuenta dagalindo@ujmd.edu.sv); se eliminó la conexión duplicada. | Claude Code | 17/07/2026 |
| Un prompt de automatización no evaluaba el riesgo de incluir datos identificables del entorno (IP y nombre de equipo en el prompt de instalación remota de Irvin). | El enfoque de esa ronda de C19 estaba en medir tiempo, no en evaluar el riesgo del dato incluido. | Irvin lo declaró como "punto de mejora" en vez de ignorarlo; queda pendiente para C18 definir qué campos nunca deben ir en texto plano en un prompt. | Irvin | 17/07/2026 |
| Compromisos (C#) anunciados sin plantilla-rúbrica clara generaron evidencia sin estructura. | La instrucción quedaba abierta a interpretación de cada Champion. | `check_consistencia.sh` (chequeo 6) ahora bloquea que se anuncie un compromiso sin su plantilla-rúbrica y ubicación exacta ya publicadas. | Claude Code | 17/07/2026 |
