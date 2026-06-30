# Lección 1: Instalación del Core Agent

> **Tiempo estimado:** 10-15 minutos
> **Nivel:** L2 → L3
> **Objetivo:** Tener `hermes` funcionando en tu terminal

---

## 📋 Prerrequisitos

| Requisito | Detalle |
|---|---|
| Sistema operativo | macOS, Linux, o Windows (incluye WSL) |
| Terminal | Acceso a tu terminal nativa (Terminal.app, PowerShell, o bash) |
| Python | No obligatorio para instalación vía script (el instalador lo gestiona) |
| Internet | Conexión estable para descargar (~50 MB) |

---

## Paso 1: Instalar Hermes Agent

Abre tu terminal y ejecuta **una** de estas opciones:

### Opción A — Instalador oficial (recomendada)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Este script instala automáticamente:
- `uv` (gestor de paquetes Python)
- Python (si no está presente)
- El entorno virtual de Hermes
- El comando `hermes` en tu PATH

### Opción B — vía pip (si ya tienes Python 3.11+)

```bash
pip install hermes-agent
```

---

## Paso 2: Verificar la instalación

Ejecuta el diagnóstico inicial:

```bash
hermes doctor
```

**Resultado esperado:**
```
✓ Python version: 3.11.x
✓ Virtual environment: active
✓ Hermes Agent: installed
⚠ API key: not configured (lo haremos en la Lección 2)
```

> Si `hermes doctor` reporta errores, ejecuta `hermes doctor --fix` para intentar autocorrección.

---

## Paso 3: Primer contacto

Inicia el modo chat interactivo:

```bash
hermes
```

Verás el banner de Hermes y el prompt de chat. Escribe un mensaje de prueba:

```
> Hola, soy [tu nombre] y estoy configurando Hermes Agent para el piloto AI Fluency.
```

El agente responderá (posiblemente con un error de API key — eso es normal en este punto, lo resolvemos en la Lección 2).

Para salir:

```
/quit
```

---

## ✅ Checklist de verificación — Lección 1

- [ ] `hermes` responde en la terminal
- [ ] `hermes doctor` ejecuta sin errores críticos
- [ ] Pude iniciar una sesión de chat (aunque falle por API key)
- [ ] Sé cómo salir con `/quit`

---

## ⚠️ Problemas comunes

| Problema | Solución |
|---|---|
| `command not found: hermes` | Cierra y reabre la terminal. Si persiste, ejecuta `source ~/.bashrc` (Linux) o reinicia Terminal.app (macOS) |
| Error de permisos en macOS | Ejecuta `sudo chown -R $(whoami) ~/.hermes` |
| Python no encontrado | El instalador maneja esto; si usaste pip, instala Python 3.11+ primero |
| Windows: `curl` no existe | Usa WSL o descarga el script manualmente desde https://hermes-agent.nousresearch.com/install.sh |

---

## 📝 Reflexión

Antes de continuar a la Lección 2, anota en tu `learning_record/progreso_champion.md`:

1. ¿Qué sistema operativo usas?
2. ¿`hermes doctor` pasó sin errores?
3. ¿Tuviste algún problema? ¿Cómo lo resolviste?

---

**Siguiente:** [Lección 2 — Configuración del modelo y provider →](../02_configuracion.md)
