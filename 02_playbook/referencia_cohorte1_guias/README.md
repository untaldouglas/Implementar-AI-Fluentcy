# Guías de Semana 1 — Cohorte 1 (Champions, julio 2026) · Archivo de referencia

> Copias congeladas el **2026-07-10** (día de cierre de S1) de las guías personalizadas de 7 días usadas
> con la primera cohorte del piloto AI Fluency. **Propósito: servir de plantilla y referencia para
> diseñar las guías de futuros grupos en formación** (Capa 1: Dirección IT completa, y siguientes).
> Las versiones vivas siguen publicadas en `docs/` (GitHub Pages) con su banner de estado.

## Qué contiene

| Archivo | Para quién fue | Caso ancla | Resultado S1 |
|---|---|---|---|
| `guia_setup_champions.html` | Los 3 Champions (común) | Setup de Hermes Agent (3 lecciones) | Ejecutado pre-Sesión 0 |
| `guia_mario_valencia.html` | Desarrollo (L1, Pasajero) | Pair programming / refactor de código legado | ✅ Verificada con documento real (10/07) |
| `guia_patrick_orellana.html` | Infraestructura (L1, Pasajero) | Scripts de monitoreo y verificación de respaldos | ✅ Verificada con documento real (10/07) |
| `guia_irvin_morales.html` | Soporte (L1, Pasajero) | Banco de respuestas rápidas para tickets | 🟡 En cierre al momento del archivo |

## Qué funcionó (mantener en futuras cohortes)

1. **Personalización real por área y por perfil baseline** — cada guía usa el caso ancla del diagnóstico del propio participante, no ejemplos genéricos. Los 3 llegaron más lejos de lo esperado (subagentes, workflows, scripts propios en la primera semana).
2. **Estructura de 7 días con entregable obligatorio claro** — Día 6 (plantilla de caso de uso) + Día 7 (reflexión de 4 preguntas) resultó el criterio verificable correcto.
3. **Comparación Prompt A vs. Prompt B del Día 1** — los participantes la citaron y replicaron por su cuenta.
4. **Exclusión explícita de datos sensibles** — la pregunta del Día 7 "¿qué datos excluiste por seguridad?" produjo respuestas genuinas (IPs, credenciales), evidencia de que la delegación segura se interiorizó.

## Qué corregir en la próxima cohorte (lecciones del 10/07)

1. **Canal de entrega desde el día 1: Google Drive** con compartir-para-aprobación (comentador → "Aprobar"), nunca correo/Teams. La cohorte 1 arrancó con correo/Teams y hubo que migrar a mitad de camino. El bloque "Cómo enviar" de estas copias ya refleja el método correcto.
2. **Nombres propios para los artefactos** — exigirlos en la guía misma con el ejemplo de convención (`AIFluency_<Nombre>_EvidenciaS1_CasoAncla_<Tema>`).
3. **Criterio único de entregable** — publicar desde el inicio que S1 = 1 caso ancla + reflexión (la cohorte 1 sufrió la inconsistencia "3 casos vs. 1 ancla", resuelta como I1 de la auditoría #01).
4. **Corregir la colisión de notación L#** (I5 de la auditoría #01): las lecciones de setup usan L1/L2/L3 que chocan con los niveles MCA — renombrar a "Lección 1/2/3" antes de reutilizar.
5. **Verificación contra documento real, no validación verbal** — el cierre de la cohorte 1 demostró que son cosas distintas; construir el checklist de verificación del facilitador dentro de la propia guía.
6. **Feedback más frecuente que semanal para perfiles L1** (H2 de la auditoría): incorporar micro-check-ins asíncronos 3×/semana a la guía desde el diseño.

---

*Archivado: 2026-07-10 · Cohorte 1: Irvin Morales (Soporte), Mario Valencia (Desarrollo), Patrick Orellana (Infraestructura) · Programa AI Fluency / MCA · UJMD-DSI*
