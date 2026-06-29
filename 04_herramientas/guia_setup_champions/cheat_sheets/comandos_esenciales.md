# Cheat Sheet — Comandos Esenciales de Hermes Agent

> Referencia rápida. Imprime o ten abierta esta hoja durante el setup.

---

## 🚀 Setup inicial (una sola vez)

```bash
# Instalar Hermes Agent
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Verificar instalación
hermes doctor

# Configurar modelo y provider (interactivo)
hermes setup

# O seleccionar modelo directamente
hermes model

# Ver config actual
hermes config
```

## 💬 Chat

```bash
# Chat interactivo
hermes

# Consulta única
hermes chat -q "tu pregunta aquí"

# Con un skill cargado
hermes chat -s hermes-agent -q "¿qué puedes hacer?"

# Con toolsets específicos
hermes chat -t web,terminal -q "busca X y crea un archivo"
```

## 🔧 Configuración

```bash
# Ver config completa
hermes config

# Editar config.yaml
hermes config edit

# Setear un valor
hermes config set section.key value

# Ver ruta del .env
hermes config env-path

# Verificar estado
hermes status --all
```

## 🛠 Tools y Skills

```bash
# Listar toolsets
hermes tools list

# Habilitar/deshabilitar (interactivo)
hermes tools

# Listar skills instalados
hermes skills list

# Buscar skills
hermes skills search "keyword"

# Inspeccionar sin instalar
hermes skills inspect ID
```

## 📱 Gateway (Telegram)

```bash
# Setup
hermes gateway setup

# Iniciar
hermes gateway start

# Estado
hermes gateway status

# Reiniciar
hermes gateway restart

# Detener
hermes gateway stop
```

## 📅 Cron Jobs

```bash
# Listar
hermes cron list

# Crear
hermes cron create "0 9 * * 1-5"

# Pausar/reanudar
hermes cron pause ID
hermes cron resume ID
```

## 💻 Sesiones

```bash
# Listar sesiones recientes
hermes sessions list

# Reanudar última sesión
hermes --continue

# Reanudar por ID
hermes --resume SESSION_ID
```

## ⌨️ Comandos dentro del chat (slash commands)

| Comando | Acción |
|---|---|
| `/help` | Ver todos los comandos |
| `/new` | Nueva sesión limpia |
| `/model` | Cambiar modelo |
| `/tools` | Gestionar herramientas |
| `/skill <nombre>` | Cargar un skill |
| `/skills` | Buscar/installar skills |
| `/status` | Info de la sesión |
| `/usage` | Uso de tokens |
| `/quit` | Salir |

---

## 🆘 Emergency

```bash
# Algo no funciona
hermes doctor --fix

# Reset completo de config
hermes setup

# Logs del gateway
# Ver en: ~/.hermes/logs/gateway.log

# Contactar a Douglas
# Email: dagalindo@ujmd.edu.sv
# Teams: Douglas Galindo
```

---

*Piloto AI Fluency UJMD · Fase 0 · Junio 2026*
