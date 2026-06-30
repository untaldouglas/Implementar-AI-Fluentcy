# Protocolo de Verificación — Aprendizaje Champions

> **Cómo verificar que el aprendizaje propuesto por `teach` fue real, no autoreporte.**

---

## Principio del skill `teach`

> *"Success is verified when the learner has demonstrated functional ability on the topic, as tracked and documented in the learning_record."*

No basta con que el Champion diga "ya lo hice". Se debe **demostrar capacidad funcional** con evidencia auditable.

---

## 3 Niveles de Verificación

### Nivel 1 — Autoverificación (Champion ejecuta solo)

Cada lección tiene un checklist con comandos que el Champion debe ejecutar en su terminal. El output real se pega en el learning record.

| Lección | Comando de verificación | Evidencia requerida |
|---|---|---|
| L1: Instalación | `hermes doctor` | Output completo pegado en learning_record |
| L2: Configuración | `hermes chat -q "¿Capital de El Salvador?"` | Respuesta del agente pegada |
| L3: Verificación | `hermes status --all` | Output completo pegado |

### Nivel 2 — Verificación por pares (Champion → Champion)

Durante la Sesión 0, cada Champion verifica a otro:

| Quién verifica | A quién | Qué revisa |
|---|---|---|
| Patrick → Mario | Mario | `hermes doctor` en terminal de Mario |
| Mario → Irvin | Irvin | `hermes chat -q` responde correctamente |
| Irvin → Patrick | Patrick | `hermes skills list` muestra skills cargados |

### Nivel 3 — Verificación por Director (Douglas)

Douglas revisa los 3 learning records antes de certificar L5:

- [ ] Output de `hermes status --all` pegado en cada record
- [ ] Reflexión final completada (¿qué aprendiste?, ¿qué fue difícil?)
- [ ] Nivel autorreportado coincide con evidencia
- [ ] Sin bloqueos sin resolver

---

## Criterios de Aprobación por Nivel

| Nivel | Criterio | Cómo se mide |
|---|---|---|
| L2 → L3 | `hermes` responde en terminal | `which hermes` devuelve ruta |
| L3 → L4 | Modelo responde correctamente | `hermes chat -q` devuelve respuesta coherente |
| L4 → L5 | Tools funcionan | web_search + file + skills probados |
| L5 (certificación) | Douglas firma el record | Revisión + aprobación manual |

---

*Piloto AI Fluency UJMD · Fase 0 · Junio 2026*
