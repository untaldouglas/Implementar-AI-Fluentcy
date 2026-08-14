# Guía del Validador — AI Fluency (MCA)

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Versión:** 1.0 · **Fecha:** 14/08/2026 · **Uso:** validadores de evidencia del programa (Champions F1 como validadores junior en F2 + Instructor)
**Esquema transitorio F2:** el Champion F1 valida (con rúbrica) y el Director **co-firma**. Se revisa al cierre de F2.

---

## 1. Principios del validador

1. **Se valida el artefacto, no la persona.** Si el archivo no existe o no está completo, el entregable está pendiente — sin importar lo que el participante diga.
2. **Aprobación nativa de Drive** ("Aprobar") es el único sello válido. Nada de "lo vi y me pareció bien" en el chat.
3. **Consistencia:** aplicar SIEMPRE la misma rúbrica (misma plantilla, mismos criterios) para todos los participantes.
4. **Traza:** todo veredicto queda registrado en el learning record del participante (fecha, versión, veredicto, observaciones).

## 2. Rúbricas por licencia

### 🟢 Básica (L2–L3) — valida Champion F1 (co-firma Director)
| Criterio | Conforme si… |
|---|---|
| 2 casos de uso reales documentados | Cada caso: problema concreto → proceso → resultado |
| Medición completa | Tiempo/costo ANTES y DESPUÉS con la plantilla C19 (no basta "me ahorró tiempo") |
| Uso autónomo | El participante explica cómo resolvió (no es un taller donde le dieron la respuesta) |
| ≥2 herramientas conocidas | Menciona y diferencia al menos 2 herramientas de IA |

### 🔵 Profesional (L4–L5) — valida Instructor
| Criterio | Conforme si… |
|---|---|
| SOUL.md propio configurado y activo | Existe en la instalación + derivado de su perfil de área + ≥1 interacción real documentada |
| 1 Skill versionado en Git | SKILL.md con trigger/procedimiento/pitfalls/verificación + probado 3 veces + repo Git |
| 3 casos de uso, ≥1 medible | Los 2 de Básica + 1 más (cualquiera con resultado medible) |
| Explica su flujo | En sesión (Demo Day): proceso real, cómo verifica, qué NO delegaría |

### 🟣 Avanzada (L6–L7) — valida Instructor + revisión de repo
| Criterio | Conforme si… |
|---|---|
| 1 automatización activa | Cron job / background agent / pipeline verificado en la estación |
| Skills en repo compartido del equipo | `01_piloto/cohortes/<fase>/…` o repo del equipo — no repos personales |
| Métricas de impacto | Tiempo/calidad/volumen documentados |
| 1 mentoría grupal | Participó facilitando ≥1 sesión |

## 3. Procedimiento de validación (paso a paso)

1. **Recibe la solicitud:** el participante comparte el documento como **comentador** en Drive.
2. **Revisa contra la rúbrica** (tabla de la sección 2) — una fila por criterio.
3. **Verifica la instalación si aplica** (Skills/SOUL): checklist de artefactos (`04_herramientas/checklist_artefactos_instalacion_champions.md`).
4. **Aprueba en Drive** con la funcionalidad "Aprobar".
5. **Registra** en el learning record: fecha, versión, veredicto (Conforme / Con ajustes / No conforme), observaciones de coaching.
6. **Co-firma el Director** (esquema transitorio F2) en el acta/registro.

## 4. Veredictos posibles

| Veredicto | Cuándo | Acción |
|---|---|---|
| ✅ Conforme | Cumple todos los criterios de la rúbrica | Aprobación + registro |
| 🟡 Con ajustes | Cumple con observaciones menores | Especificar los ajustes; nueva versión; revalidar |
| 🔴 No conforme / pendiente de materializar | El artefacto no existe o no cumple el criterio esencial | Registrar sin aprobar; plan de recuperación con fecha |

## 5. Errores históricos que NO repetir (aprendidos en F1)

- ❌ Validar por conversación ("me dijo que lo hizo") → ✅ verificar contra el documento real en Drive.
- ❌ Aprobar "avance" como cierre (mini-reporte ≠ medición C19 completa) → ✅ cada compromiso tiene su criterio propio.
- ❌ Evidencia en carpetas personales → ✅ carpeta canónica de entrega.
- ❌ Aceptar un "caso de uso" genérico sin medición → ✅ la plantilla exige antes/después.
- ❌ Ignorar el filtro de datos sensibles → ✅ el participante declara qué datos excluyó.

## 6. Tu rol en el Demo Day

- Verificas la demostración en vivo contra la rúbrica de "explica su flujo" (criterio R21 de la Profesional).
- Marca la rúbrica de la agenda (casillas por criterio) y firma como validador.
- El Director consolida el veredicto final.

---

*Guía viva — se actualiza con cada cohorte. Rúbricas normativas: `00_marco/Licencia_Conduccion_AI.md`.*
