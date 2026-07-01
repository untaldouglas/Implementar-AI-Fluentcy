# Glosario — Términos Clave de Hermes Agent

> Referencia rápida para Champions. Mantén este glosario a mano durante el piloto.

---

## Términos esenciales

| Término | Definición |
|---|---|
| **Agent** | El asistente de IA que ejecuta tareas usando herramientas. En nuestro caso, Hermes Agent. |
| **Provider** | El servicio que provee el modelo de IA. Proveedor principal: OpenRouter. Alternativos: Groq, Ollama, NVIDIA. |
| **Model** | El modelo de lenguaje específico. Ej: `meta-llama/llama-3.3-70b-instruct:free` (OpenRouter), `llama-3.3-70b-versatile` (Groq). |
| **Toolset** | Conjunto de herramientas que el agente puede usar: `web`, `terminal`, `file`, `skills`, etc. |
| **Skill** | Procedimiento reusable guardado como documento Markdown. Carga conocimiento especializado al agente. |
| **Gateway** | Servicio que conecta Hermes con plataformas de mensajería (Telegram, Discord, Slack, etc.). |
| **Profile** | Instancia independiente de Hermes con su propia config, skills, memoria y sesiones. |
| **Session** | Una conversación con Hermes. Se puede resumir, exportar y reanudar. |
| **SOUL.md** | Archivo de identidad del agente. Define quién es y cómo se comporta. |
| **CLI** | Command Line Interface — la terminal donde escribes comandos `hermes ...`. |
| **TUI** | Text User Interface — la interfaz visual en terminal (modo interactivo). |

## Comandos clave

| Término | Qué significa |
|---|---|
| `hermes` | Inicia chat interactivo |
| `hermes chat -q "..."` | Consulta única (non-interactive) |
| `hermes setup` | Asistente de configuración |
| `hermes doctor` | Diagnóstico del sistema |
| `hermes model` | Seleccionar modelo/provider |
| `hermes tools` | Habilitar/deshabilitar toolsets |
| `hermes skills list` | Listar skills instalados |
| `hermes gateway start` | Iniciar gateway de mensajería |
| `hermes status --all` | Estado global de todos los componentes |
| `/skill <nombre>` | Cargar un skill en la sesión actual |
| `/reset` | Iniciar nueva sesión limpia |
| `/quit` | Salir del chat |

## Conceptos del piloto AI Fluency

| Término | Definición |
|---|---|
| **Champion** | Miembro del equipo seleccionado para liderar la adopción de IA en su área. |
| **Nivel L0-L9** | Escala de autonomía con IA. L0=sin conocimiento, L9=operación autónoma con cron jobs. |
| **Sesión 0** | Kick-off del piloto. Aplicación del diagnóstico baseline + setup técnico. |
| **Demo Day** | Sesión final donde cada Champion presenta su agente funcional. |
| **SOUL.md de área** | Plantilla de identidad para cada Champion (Infraestructura, Desarrollo, Soporte). |
| **Roadmap** | Documento que define las fases y hitos del proyecto AI Fluency UJMD. |

---

*Actualizado: 29/06/2026 · Piloto AI Fluency UJMD*
