# 🚗 Propuesta de Prompts para Onboarding de Champions
## AI Fluency — Modelo de Conducción AI · Fase 1, Semana 1
### Basado en: *Hermes Agent Daily Assistant Prompt Pack*

---

## 📊 Diagnóstico: ¿Qué prompts ya tiene Douglas vs. qué falta para los Champions?

| Prompt del Pack | Douglas ya lo tiene | ¿Aplica a Champions L1→L3? |
|---|---|---|
| 1. Entrevista de descubrimiento | ✅ (Morning Command Center) | 🔴 **SÍ — es el punto de partida** |
| 2. Mapa de delegación | ✅ (Governance Review implícito) | 🟡 Sí, pero simplificado |
| 3. Elegir 3 workflows | ❌ | 🟢 **SÍ — ideal para esta semana** |
| 4. Check-in diario | ✅ (Cron 6:30 AM) | ❌ No aplica (son L1, no directores) |
| 5. Convertir en skill | ✅ (`/learn` + `skill_manage`) | 🟡 Futuro (cuando lleguen a L5) |
| 6. Convertir en cron job | ✅ (10 cron jobs activos) | 🟡 Futuro (cuando lleguen a L6) |
| 7. Regla de seguridad | ✅ (memoria del sistema) | 🔴 **SÍ — fundamental desde día 1** |
| 8. Revisión semanal | ❌ | 🟡 Futuro (cuando tengan workflows) |

---

## 🎯 Propuesta: 3 prompts para la Semana 1 (adaptados a L1)

### Prompt 1 — Entrevista de descubrimiento *(Día 3-4 de la guía)*

Este es el equivalente al Prompt 1 del Pack, adaptado para Champions que recién instalaron Hermes:

```
Quiero que me entrevistes para descubrir cómo podés ayudarme en mi área
de [Soporte | Desarrollo | Infraestructura] en la UJMD.

Haceme una pregunta a la vez sobre:
- Mis tareas repetitivas del día a día
- Las decisiones que tomo con frecuencia
- Lo que más tiempo me consume
- Las interrupciones constantes que recibo
- Las cosas que postpono porque no me da tiempo
- La información que siempre tengo que buscar

Después de cada respuesta, identificá posibles tareas donde Hermes podría
ayudarme.

Al final, dame:
1. Las 5 tareas principales donde podrías ayudarme YA
2. Las 2 más fáciles de implementar esta semana
3. Qué necesitarías de mí para cada una (archivos, permisos, contexto)
```

**Objetivo:** Que cada Champion descubra su propio "Hermes use case", anclado en su realidad diaria.

---

### Prompt 2 — Mapa de delegación simplificado *(Día 5-6 de la guía)*

Adaptación del Prompt 2 del Pack, con solo 2 categorías para no abrumar:

```
Con base en lo que te conté de mi trabajo en [área], armame un mapa simple
de delegación con solo dos categorías:

1. ✅ Tareas que podés hacer vos solo sin mí (investigar, resumir, generar
   borradores, buscar información técnica, comparar opciones)

2. 🛑 Tareas donde solo preparás o sugerís, pero YO decido y ejecuto
   (cambiar configuraciones, responder a usuarios, modificar código en
   producción, tocar servidores)

Para cada tarea explicame:
- Por qué está en esa categoría
- Qué necesitás de mí para hacerla bien
- Cuál sería el primer caso concreto que probamos juntos
```

**Objetivo:** Enseñar el concepto de "delegación segura" desde el día 1. Esto ataca directamente los 3 bloqueos:
- Irvin (Confianza): ver tareas "seguras" genera confianza gradual
- Mario (Permisos): identifica qué necesita acceso y qué no
- Patrick (Delegación): su bloqueo principal, abordado explícitamente

---

### Prompt 3 — Regla de seguridad personal *(Día 4, junto con SOUL.md)*

Adaptación del Prompt 7 del Pack:

```
De ahora en adelante, para CUALQUIER tarea que hagamos juntos, aplicá
esta regla de seguridad:

✅ PODÉS: investigar, resumir, comparar, preparar borradores, buscar
   documentación técnica, generar scripts para que yo revise, sugerir
   soluciones, organizar información.

🛑 NO PODÉS sin mi aprobación explícita: ejecutar comandos en servidores
   de la UJMD, modificar archivos de configuración reales, responder a
   usuarios o tickets, cambiar código en producción, acceder a bases de
   datos, exponer IPs o contraseñas.

Antes de cualquier acción que toque sistemas reales, mostrame:
1. Qué vas a hacer
2. Por qué lo recomendás
3. El comando o archivo exacto
4. El riesgo
5. Preguntame: "¿Apruebo?"

Esperá mi "sí" antes de actuar.
```

**Objetivo:** Cada Champion internaliza que Hermes es un copiloto, no un piloto automático. Esto construye el músculo de "delegación segura" que es la base de TODO el programa.

---

## 📅 Secuencia propuesta: integrar al itinerario de 7 días

| Día de la guía | Actividad original | Prompt nuevo que se integra |
|---|---|---|
| Día 1 | Lección 1 — Instalación | *(sin cambios — es puro setup técnico)* |
| Día 2 | Lección 1 — Práctica | *(sin cambios — practicar comandos básicos)* |
| **Día 3** | Lección 2 — Configuración | **🆕 Prompt 1: Entrevista de descubrimiento** |
| **Día 4** | Lección 2 — Continuación + SOUL.md | **🆕 Prompt 3: Regla de seguridad personal** |
| **Día 5** | Caso Ancla (parte 1) | **🆕 Prompt 2: Mapa de delegación simplificado** |
| Día 6 | Caso Ancla (parte 2) | Aplicar el mapa a un caso real del área |
| Día 7 | Cierre y reflexión | Evaluar: ¿qué aprendí sobre delegar? |

---

## 🔮 Próximos pasos (Semanas 2-4)

| Prompt del Pack | Cuándo introducirlo | A quién |
|---|---|---|
| Prompt 4 (Check-in diario) | Semana 3 — cuando ya tengan 2+ workflows | Los 3 |
| Prompt 5 (Convertir en skill) | Semana 4 — cuando un workflow se repita 3+ veces | Mario (Desarrollo) primero |
| Prompt 6 (Cron job) | Fase 2 (agosto) — L5+ | El que llegue a Piloto Automático |
| Prompt 8 (Revisión semanal) | Semana 2 en adelante | Douglas + Champions en reunión de seguimiento |

---

## ⚡ Quick Win: lo que cada Champion puede hacer HOY mismo

| Champion | Prompt a usar HOY | Resultado esperado |
|---|---|---|
| **Irvin** | Prompt 1 (Entrevista) | Descubrir 2-3 tareas de Soporte que Hermes puede agilizar (ej: "generame una plantilla de respuesta para tickets de contraseña") |
| **Mario** | Prompt 1 (Entrevista) | Descubrir 2-3 tareas de Desarrollo (ej: "explicame este código legacy de REAC") |
| **Patrick** | Prompt 1 + Prompt 3 (Seguridad) | Descubrir casos de Infraestructura + definir qué NUNCA compartir con Hermes |

---

## 📊 Cómo medir si los prompts funcionan

| Indicador | Línea base (hoy) | Meta (fin de Semana 1) |
|---|---|---|
| Champions que completaron Prompt 1 | 0 de 3 | 3 de 3 |
| Champions con mapa de delegación | 0 de 3 | 3 de 3 |
| Tareas concretas delegadas a Hermes | 0 | ≥2 por Champion |
| Evidencia pegada en learning_record | 0% | 100% (Días 1-7) |

---

*Propuesta generada por Hermes Agent · Morning Command Center · 2026-07-03*
*Fuente: Hermes Agent Daily Assistant Prompt Pack + AI Fluency MCA Playbook*