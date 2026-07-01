# Lección 3: Verificación y Pruebas Finales

> **Tiempo estimado:** 10 minutos
> **Nivel:** L4 → L5
> **Objetivo:** Confirmar que Hermes Agent está 100% funcional y listo para Sesión 0

---

## 📋 Prerrequisitos

- Lección 1 completada (instalación)
- Lección 2 completada (modelo configurado y respondiendo)
- `hermes chat -q` responde correctamente

---

## Paso 1: Diagnóstico completo

Ejecuta el doctor con autocorrección:

```bash
hermes doctor --fix
```

**Resultado esperado:**

```
✓ Python version: 3.11.x
✓ Virtual environment: active
✓ Hermes Agent: installed
✓ API key: configured (openrouter)
✓ Model: meta-llama/llama-3.3-70b-instruct:free
✓ Terminal: local backend
✓ Tools: web, terminal, file, skills
```

> Cualquier línea con `✗` o `⚠` debe resolverse antes de Sesión 0. Contacta a Douglas si no puedes resolverla.

---

## Paso 2: Prueba de herramientas (toolsets)

Hermes no es solo chat — puede ejecutar acciones. Vamos a probar 3 toolsets clave:

### Prueba A — Web search

```bash
hermes chat -q "Busca en la web: Universidad Dr. José Matías Delgado El Salvador"
```

Verifica que el agente use la herramienta `web_search` y devuelva información real sobre la UJMD.

### Prueba B — File operations

```bash
hermes chat -q "Crea un archivo llamado prueba_champion.txt en mi directorio home con el texto: Setup de Hermes Agent completado por [tu nombre]"
```

Verifica que el archivo fue creado:

```bash
cat ~/prueba_champion.txt
```

### Prueba C — Skills

Lista los skills disponibles:

```bash
hermes skills list
```

Deberías ver una lista de skills categorizados. Carga uno para probar:

```bash
hermes chat -s hermes-agent -q "¿Qué puedes hacer según tu documentación?"
```

---

## Paso 3: Verificar estado global

Ejecuta el status completo:

```bash
hermes status --all
```

Esto muestra el estado de todos los componentes. Copia y guarda este output — lo vas a compartir con Douglas como evidencia de setup completado.

---

## Paso 4: Limpiar archivos de prueba

```bash
rm ~/prueba_champion.txt
```

---

## ✅ Checklist final — Listo para Sesión 0

| # | Verificación | Comando | ¿Pasa? |
|---|---|---|---|
| 1 | Hermes instalado | `hermes doctor` | ⬜ |
| 2 | Modelo configurado | `hermes chat -q "Hola"` | ⬜ |
| 3 | Web search funcional | `hermes chat -q "busca..."` | ⬜ |
| 4 | File operations | `hermes chat -q "crea archivo..."` | ⬜ |
| 5 | Skills accesibles | `hermes skills list` | ⬜ |
| 6 | Gateway Telegram (opcional) | `hermes gateway status` | ⬜ |
| 7 | Status global | `hermes status --all` | ⬜ |

**Si todos los ítems están ✅, estás listo para Sesión 0.**

---

## 📤 Entrega final

Envía a Douglas antes del 30/06 23:59:

1. El output de `hermes status --all`
2. Tu `learning_record/progreso_champion.md` completado
3. Cualquier duda o bloqueo que hayas tenido

**Canal:** Correo a dagalindo@ujmd.edu.sv o mensaje directo en Teams

---

## 🎯 Nivel alcanzado

Al completar esta lección, has alcanzado **Nivel L5** en el modelo de autonomía:

| Nivel | Descripción | Estado |
|---|---|---|
| L0 | Sin conocimiento de IA | ⬜ |
| L1 | Conoce conceptos básicos | ⬜ |
| L2 | Usa herramientas de IA básicas | ✅ (baseline) |
| L3 | Instala y configura herramientas | ✅ |
| L4 | Configura providers y modelos | ✅ |
| L5 | **Verifica y opera independientemente** | ✅ |

**Meta del piloto:** L5 alcanzado. Próximo objetivo durante el piloto: construir un agente funcional para tu área.

---

**← Anterior:** [Lección 2 — Configuración del modelo](../02_configuracion.md)
**🏠 Inicio:** [Misión](../mission.md)
