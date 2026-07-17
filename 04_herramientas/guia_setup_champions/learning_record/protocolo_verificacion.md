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

## Nivel 4 — Verificación de outputs de tareas delegadas (agregado 17/07/2026 — R16/H10, auditoría #02)

Los Niveles 1–3 verifican que **Hermes está bien instalado**. Este nivel verifica que **el resultado de una tarea real delegada a Hermes es correcto** — el vacío que existía entre "la herramienta funciona" y "el trabajo está bien hecho".

Para cada tarea real delegada (caso ancla, procesos C19, futuros Skills), el Champion documenta:

| Paso | Qué se verifica | Evidencia requerida |
|---|---|---|
| 1. Criterio previo | Antes de delegar, definir qué haría que el resultado sea "correcto" (1–2 líneas) | Criterio escrito en el documento del caso |
| 2. Revisión línea a línea | El output se lee completo — encabezados/comentarios contrastados contra lo que el código o texto realmente hace | Nota de revisión ("revisado, consistente" o discrepancia encontrada) |
| 3. Prueba independiente | Al menos 1 verificación que NO dependa de Hermes (ejecutar el script, contrastar un dato, probar el resultado) | Resultado de la prueba documentado |
| 4. Registro de fallas | Si Hermes falló o alucinó, se documenta la falla y el ajuste — las fallas documentadas valen tanto como los aciertos | Descripción de la falla + corrección |

**Primer ejemplo del protocolo (caso fundacional):** Irvin Morales delegó a Hermes ordenar archivos por fecha `dd/mm/aaaa`, verificó el resultado y detectó que la tarea NO se cumplió correctamente — y adoptó el hábito de verificar cada resultado (reflexión Día 7, S1). Ese comportamiento es exactamente lo que este nivel protocoliza.

**Contraejemplo documentado:** `monitor_servidores_pro.sh` (Patrick, S1) — el encabezado documenta verificación de CPU/disco pero el cuerpo solo hace `ping`. El paso 2 de este protocolo existe para atrapar exactamente eso.

---

## Criterio adicional de certificación L2: perfil Hermes separado (agregado 17/07/2026 — R15/H9, auditoría #02)

Para certificar L2 (Coche Propio), el Champion debe evidenciar un **perfil Hermes separado** para práctica/experimentación, distinto del perfil de trabajo, con su configuración de modelo documentada.

**Plantilla replicable:** el perfil `Testprofile` de Irvin Morales (API de modelos Google, aislado de su flujo de tickets real). Mario y Patrick deben crear el equivalente en su área — pendiente al 17/07.

---

*Piloto AI Fluency UJMD · Fase 0 · Junio 2026 · Ampliado 17/07/2026 (auditoría #02: Nivel 4 + criterio de perfiles)*

