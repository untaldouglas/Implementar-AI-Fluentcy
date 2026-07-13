# S2 · Taller de Prompting Aplicado

> Sesión de hoy **lunes 13/07 · 14:00–15:00** (bloque de calendario recurrente). Arranque de S2 (Productividad personal con IA). Mini-reportes S2 vencen **viernes 17/07**. Insumos: los 3 casos ancla reales de S1 (ver `01_piloto/learning_record/`) + buenas prácticas de prompting.

---

## 0. Objetivo de la sesión

S1 dejó a los 3 Champions con un caso ancla funcional pero con margen de mejora identificado en la revisión. Este taller no enseña prompting desde cero — **toma el prompt real de cada uno y lo lleva un nivel más allá**, usando 5 técnicas que S1 no cubrió explícitamente. La salida de hoy (prompt "antes" vs "después" con tiempo medido) es insumo directo para **C19** (medición tiempo/costo antes-después, vence 17/07).

---

## 1. Repaso rápido (5 min) — el marco de S1

Los 3 ya dominan esto de la guía de 7 días, solo se nombra para anclar lo nuevo encima:

> **Rol** (¿quién es el agente?) + **Tarea** (¿qué debe hacer?) + **Contexto** (¿qué necesita saber?)

Lo de hoy son 5 capas adicionales sobre esa base.

---

## 2. Marco ampliado — 5 técnicas de prompting aplicado (15 min)

| # | Técnica | En qué consiste | Por qué importa para S2 |
|---|---|---|---|
| 1 | **Formato de salida explícito** | Especificar la forma exacta de la respuesta (tabla, 3 pasos numerados, longitud máxima, tono) en vez de dejarlo implícito | Reduce iteraciones de retrabajo — se pide el formato final desde el primer intento |
| 2 | **Restricciones y exclusiones** | Decir explícitamente qué NO debe hacer o qué datos NO debe tocar (ej. "no incluyas IPs ni credenciales", "no inventes cifras que no te di") | Es la práctica que Patrick ya aplicó bien de forma intuitiva (excluir IPs/credenciales) — hoy se formaliza como paso reutilizable por los 3 |
| 3 | **Descomposición de tareas complejas** | Para tareas de varios pasos, pedir primero un plan/lista de riesgos y luego la ejecución, en vez de pedir todo junto | Aplica directo al caso de Mario (refactorización) — separar "qué riesgos tiene este cambio" de "hazme el refactor" |
| 4 | **Iteración dirigida** | Refinar en el mismo hilo con instrucciones puntuales ("hazlo más breve", "usa un ticket real en vez del genérico de la guía") en vez de empezar de cero | Ya lo vieron Día 3 (S1) — hoy se aplica a mejorar prompts que quedaron genéricos |
| 5 | **Verificación humana post-generación** | Revisar línea por línea antes de usar, especialmente en scripts o cuando hay datos que Hermes no tiene de primera mano | Conecta con el hallazgo real de Irvin (Hermes falló un ordenamiento de fechas) y con la inconsistencia real de Patrick (`monitor_servidores_pro.sh`: el encabezado dice "CPU y disco", el cuerpo solo hace `ping`) |

---

## 3. Ejercicio aplicado — por Champion (30 min)

Cada quien trabaja sobre **su propio caso real**, no un ejemplo genérico.

### Irvin (Soporte) — de prompt genérico a prompt propio

- **Punto de partida real:** el prompt de su caso ancla ("Solicito ayuda con mi equipo no enciende") replica el ejemplo de la guía en vez de partir de un ticket propio — a diferencia de su prompt del Día 1, que sí usó un ticket real de AD.
- **Ejercicio:** reescribir el prompt del caso ancla con un ticket real de hoy (anonimizado), aplicando:
  - Técnica 1 (formato): pedir explícitamente la respuesta en 3 pasos + escalamiento, como ya la estructuró.
  - Técnica 2 (restricciones): "no asumas causas que el usuario no reportó".
- **Entrega:** prompt nuevo + respuesta, comparado contra el prompt genérico anterior (tiempo estimado de cada uno).

### Mario (Desarrollo) — descomponer antes de ejecutar

- **Punto de partida real:** caso ancla de refactorización del módulo Graduados/GAO (C#/Java), ~20 min ahorrados estimados.
- **Ejercicio:** tomar un cambio de código pendiente y aplicar Técnica 3 — primero un prompt que pida "lista los riesgos de este cambio antes de proponerlo" y luego, en el mismo hilo (Técnica 4), pedir el refactor ya acotado a esos riesgos.
- **Entrega:** los dos prompts (riesgos → refactor) + tiempo medido de cada paso — insumo directo para C19.

### Patrick (Infraestructura) — verificación línea por línea + restricciones como plantilla

- **Punto de partida real:** `monitor_servidores_pro.sh` tiene una inconsistencia real entre el encabezado (dice verificar CPU y disco) y el cuerpo (solo hace `ping`) — no se revisó línea por línea al generarlo.
- **Ejercicio:**
  - Técnica 5: escribir un prompt que le pida a Hermes auditar el script existente línea por línea contra su propio encabezado/documentación y señalar inconsistencias.
  - Técnica 2: formalizar como plantilla reutilizable la instrucción que ya usa bien de forma intuitiva ("excluye IPs y credenciales reales") para que los otros 2 Champions también la adopten en sus propios prompts.
- **Entrega:** script corregido + la plantilla de restricción de datos sensibles, lista para compartir en conocimiento colectivo (C17).

---

## 4. Cierre (10 min)

1. Cada Champion deja registrado en su carpeta de evidencia S2 (Drive, mismo flujo comentador → Aprobar acordado en Sesión 18): prompt "antes" (S1) vs prompt "después" (hoy), con tiempo estimado de cada uno.
2. Recordar: esta comparación **antes/después con tiempo medido es exactamente lo que pide C19** — ya no hace falta un ejercicio aparte para eso, este taller lo cubre en la práctica.
3. Próxima carga de conocimiento colectivo: miércoles 15/07 — la plantilla de restricciones de Patrick es candidata natural para la lista de errores / FAQ (C17).

---

*Preparado: 2026-07-13 · Sesión S2 (14:00) · Piloto AI Fluency UJMD*
