# Rituales de Jornada — AI Fluency UJMD
**Archivo fuente de verdad para los rituales de inicio y cierre de sesión de trabajo**
Versión: 1.0 · Creado: 2026-06-29 · Skill: `jornada-ritual`

---

## Archivos de estado que Claude DEBE leer en cada ritual

| Archivo | Propósito |
|---|---|
| `ESTADO_PROYECTO.md` | Fase actual, compromisos, bloqueos, acción #1 definida |
| `04_herramientas/Dashboard_Jornada.html` | Compromisos, bloqueos y log visual del proyecto |

---

## 🌅 RITUAL: Inicio de Jornada

**Frases trigger:** "inicio de jornada", "inicio del día", "empezamos", "qué hago hoy"

### Secuencia obligatoria

1. **Leer `ESTADO_PROYECTO.md`** — extraer: fase actual, última sesión registrada, acción #1 definida ayer, bloqueos activos
2. **Calcular contexto del programa** — día/semana del piloto, días al próximo hito crítico
3. **Identificar compromisos urgentes** — los que vencen hoy o mañana, ordenados por fecha límite
4. **Reportar bloqueos activos** — con el fix disponible si existe en el archivo de estado
5. **Presentar TOP 3 acciones del día** — ordenadas: primero por impacto en el programa, luego por urgencia

### Formato de salida (usar siempre este formato exacto)

```
📅 HOY · [fecha] · Día [N] de F[X] — [nombre de la fase]
⏰ Próximo hito: [descripción] en [N] días

🎯 TOP 3 acciones de hoy:
1. [nombre acción] (~[tiempo]) — [razón concreta: qué desbloquea o qué hito avanza]
2. [nombre acción] (~[tiempo]) — [razón]
3. [nombre acción] (~[tiempo]) — [razón]

⚠️ Bloqueos activos: [N]
[lista de bloqueos con fix si existe]

📋 Compromisos que vencen hoy o mañana:
[lista o "Ninguno urgente"]
```

### Reglas del ritual de inicio

- No preguntar nada antes de presentar el resumen. Hacerlo directamente.
- Si hay una acción #1 definida explícitamente en `ESTADO_PROYECTO.md`, esa va siempre como #1.
- Si no hay contexto suficiente (primer uso del día), inferir desde el estado del proyecto.
- Máximo 3 acciones. No más. Prioridad sobre exhaustividad.

---

## 🌙 RITUAL: Fin de Jornada

**Frases trigger:** "fin de jornada", "cierre de jornada", "cerramos", "terminar el día"

### Secuencia obligatoria

1. **Leer `ESTADO_PROYECTO.md`** para conocer el estado de inicio de la sesión
2. **Preguntar qué se completó** — solo si el usuario no lo indicó ya en la conversación:
   *"¿Qué completaste hoy y qué quedó pendiente o surgió nuevo?"*
3. **Actualizar `ESTADO_PROYECTO.md`**:
   - Marcar compromisos completados con ✅ y fecha
   - Agregar nuevos compromisos si surgieron
   - Actualizar bloqueos (remover resueltos, agregar nuevos)
   - Definir acción #1 para mañana
   - Registrar número y nombre de sesión
4. **Actualizar `Dashboard_Jornada.html`**:
   - Compromisos: cambiar estado visual (colores y badges)
   - Bloqueos: agregar o remover según corresponda
   - Decisiones: agregar las tomadas hoy si las hubo
   - Log: agregar entrada EOD con fecha y resumen
5. **Definir y declarar la acción #1 para mañana** — la de mayor valor según fase y estado actual
6. **Preguntar si se genera post de blog** — solo si hubo avance técnico o de programa significativo:
   *"¿Genero el blog post de hoy (HTML + LinkedIn)?"*

### Formato de salida al cierre

```
✅ Jornada cerrada — [fecha]

Completado hoy:
· [item 1]
· [item 2]

Pendiente / nuevo:
· [item 1]

🔒 Compromisos actualizados: [lista de cambios de estado]
⚠️ Bloqueos: [resueltos / nuevos]

🎯 Acción #1 mañana: [descripción clara] (~[tiempo])
   Por qué: [razón concreta]
```

### Reglas del ritual de cierre

- Actualizar SIEMPRE ambos archivos (ESTADO_PROYECTO.md y Dashboard_Jornada.html). No omitir ninguno.
- Si el usuario ya dijo qué completó durante la conversación, no preguntar de nuevo. Inferirlo.
- El post de blog es opcional — preguntar, no asumir.
- La acción #1 de mañana debe ser la de mayor valor, no la más fácil.
- Registrar siempre en el log del dashboard aunque el avance haya sido pequeño.

---

## Comportamiento común a ambos rituales

- **Leer antes de actuar.** Nunca responder desde memoria sin leer primero `ESTADO_PROYECTO.md`.
- **Ser directo.** Sin preámbulos, sin "voy a..." antes de hacerlo. Hacerlo y mostrar el resultado.
- **Actualizar en caliente.** Los archivos de estado deben quedar actualizados al terminar el ritual, no después.
- **No inventar compromisos.** Solo registrar lo que el usuario confirme explícitamente.

---

## Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-06-29 | Versión inicial — rituales de inicio y cierre definidos y validados |
