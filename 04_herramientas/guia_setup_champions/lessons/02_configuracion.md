# Lección 2: Configuración del Modelo y Provider

> **Tiempo estimado:** 15-20 minutos
> **Nivel:** L3 → L4
> **Objetivo:** Conectar Hermes Agent con un modelo LLM (Claude) y configurar el gateway de Telegram

---

## 📋 Prerrequisitos

- Lección 1 completada (`hermes doctor` pasa sin errores críticos)
- Clave API de OpenRouter (proporcionada por Douglas) — o cuenta propia en https://openrouter.ai
- Tu cuenta de Telegram activa

---

## Paso 1: Configurar el asistente de setup

Ejecuta el wizard interactivo:

```bash
hermes setup
```

El asistente te guiará por las secciones de configuración. Selecciona:

1. **Model section:**
   - Provider: `openrouter`
   - Model: `meta-llama/llama-3.3-70b-instruct:free` (gratuito, recomendado para iniciar)
   - API Key: pega la clave de OpenRouter que te proporcionó Douglas

   > **Alternativas gratuitas reconocidas:**
   > - Groq: provider `groq`, modelos ultra-rápidos (Llama 3, Gemma)
   > - Ollama: provider `ollama`, completamente local (sin costo, sin internet)
   > - NVIDIA NIM: provider `openai` con base URL de NVIDIA, créditos gratuitos

2. **Terminal section:**
   - Backend: `local` (mantén el valor por defecto)
   - Working directory: tu directorio de trabajo

3. **Tools section:**
   - Habilita: `web`, `terminal`, `file`, `skills`
   - Deja deshabilitados por ahora: `browser`, `image_gen`, `video`

---

## Paso 2: Alternativa rápida — configuración manual

Si prefieres no usar el wizard, puedes configurar directamente:

```bash
# Seleccionar modelo y provider
hermes model
```

Esto abre un menú interactivo. Navega con las flechas:
- Provider → `openrouter`
- Model → `meta-llama/llama-3.3-70b-instruct:free`

Para guardar la API key, edita el archivo `.env`:

```bash
hermes config env-path    # te muestra dónde está el archivo .env
```

Añade esta línea al `.env`:

```
OPENROUTER_API_KEY=sk-or-XXXXX-tu-clave-aqui
```

> **⚠️ IMPORTANTE:** Nunca compartas tu API key por correo, chat, ni screenshots. Si necesitas transmitirla, usa canales seguros.

---

## Paso 3: Verificar que el modelo responde

Haz una consulta de prueba:

```bash
hermes chat -q "¿Cuál es la capital de El Salvador?"
```

**Resultado esperado:** El agente responde "San Salvador" en pocos segundos.

Si responde correctamente, **el modelo está configurado.** ✅

> **¿Sin créditos aún?** Usa Groq como fallback inmediato — es gratuito y ultra-rápido: ejecuta `hermes model`, selecciona provider `groq` y elige `llama-3.3-70b-versatile`.

---

## Paso 4: Configurar el gateway de Telegram (opcional para Sesión 0, pero recomendado)

El gateway te permite interactuar con Hermes desde Telegram, igual que lo hace Douglas.

```bash
hermes gateway setup
```

Selecciona `telegram` y sigue las instrucciones:
1. Crea un bot en Telegram hablando con `@BotFather`
2. Copia el token del bot
3. Pégalo cuando el setup lo solicite

Inicia el gateway:

```bash
hermes gateway start
```

Verifica el estado:

```bash
hermes gateway status
```

**Resultado esperado:** `telegram: connected ✓`

> **Nota:** Si prefieres esperar a la Sesión 0 para configurar Telegram, puedes saltar este paso. Es opcional para el setup inicial pero muy recomendado para uso diario.

---

## ✅ Checklist de verificación — Lección 2

- [ ] `hermes setup` completado (o configuración manual)
- [ ] `hermes chat -q "..."` responde correctamente
- [ ] API key guardada en `.env` (no en config.yaml)
- [ ] (Opcional) Gateway de Telegram conectado

---

## ⚠️ Problemas comunes

| Problema | Solución |
|---|---|
| `401 Unauthorized` al consultar | La API key es incorrecta o está vencida. Verifica en `.env` |
| `model not found` | Ejecuta `hermes model` y selecciona un modelo de OpenRouter (ej: `meta-llama/llama-3.3-70b-instruct:free`) |
| Gateway no conecta | Verifica el token del bot con `@BotFather`. Revisa logs: `hermes gateway status` |
| Respuesta muy lenta | Es normal en la primera consulta. Las siguientes usan cache |

---

## 📝 Reflexión

Registra en tu `learning_record/progreso_champion.md`:

1. ¿Qué modelo configuraste?
2. ¿La consulta de prueba funcionó?
3. ¿Configuraste el gateway de Telegram? ¿Funcionó?
4. ¿Qué dudas te quedaron?

---

**Siguiente:** [Lección 3 — Verificación y pruebas finales →](../03_verificacion.md)
