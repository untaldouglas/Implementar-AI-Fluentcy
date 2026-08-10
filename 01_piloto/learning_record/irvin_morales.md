# Learning Record — Irvin Josué Morales Parada (Soporte)

## Datos base

| Campo | Valor |
|---|---|
| Nombre | Irvin Josué Morales Parada |
| Correo | ijmoralespa@ujmd.edu.sv |
| Área | Soporte / Mesa de Servicios |
| Nivel baseline | L1 (diagnóstico Google Form, 01/07/2026 · script `calcular_nivel_mca.gs`) |
| Zona | Pasajero |
| Bloqueo detectado en diagnóstico | Confianza/Seguridad |
| Fecha de setup Hermes | 2026-07-02 (C11, Sesión 14 — las 3 estaciones operando) |
| Versión Hermes | _(no archivada — ver nota de verificación abajo)_ |

---

## Lecciones 1–3 (Instalación / Configuración / Verificación)

> **Base real de la verificación (corregido 17/07/2026 — I9/R13, auditoría #02):** el setup funcional quedó verificado el 02/07 (C11: las 3 estaciones operando) y confirmado en la práctica por la evidencia S1 producida con Hermes. Los outputs formales de `hermes doctor`/`hermes status --all` **no fueron archivados**: los formularios de `04_herramientas/guia_setup_champions/learning_record/` quedaron vacíos y están declarados ARCHIVO HISTÓRICO no vinculante. Esta tabla certifica capacidad funcional demostrada, no formulario llenado.

| Lección | Estado | Fecha |
|---|---|---|
| Lección 1: Instalación | ✅ | 2026-07-10 |
| Lección 2: Configuración | ✅ | 2026-07-10 |
| Lección 3: Verificación | ✅ | 2026-07-10 |

---

## Evidencia S1 — Casos de uso

> Entregable original (Roadmap): 3 casos de uso documentados. Guía operativa enviada al Champion (`docs/guia_irvin_morales.html`, Día 6) pedía 1 caso de uso "ancla" completo + reflexión final (Día 7) — criterio RESUELTO el 10/07 (I1, auditoría #01): S1 = 1 caso ancla + reflexión; los 3 casos del Roadmap son meta acumulada S1+S2.

| # | Título del caso de uso | Dónde vive la evidencia | Fecha de entrega | Veredicto verificación | Notas |
|---|---|---|---|---|---|
| 1 (ancla, obligatorio) | **"EQUIPO NO ENCIENDE — Mesa de Servicios UJMD"** (respuesta guiada al usuario con Hermes + OpenRouter/Groq; plantilla Día 6 completa) | ☑ Google Drive (`Sesion practica de los prompt de la guia version 2`) · espejo local en `01_piloto/evidencia_piloto/irvin_morales/` (PDF, 9 págs.) | 2026-07-10 (noche, segunda entrega) | ✅ **Verificado** (documento real revisado, 10/07 noche) | El documento nuevo incluye además práctica Días 1–5 (Prompt A/B, ticket AD real anonimizado, modo interactivo, SOUL, banco de respuestas), perfil `Testprofile` creado y la limitante documentada de API Key en ERPNext |
| 2 (si aplica) | _(no especificado en la reunión)_ | | | | |
| 3 (si aplica) | _(no especificado en la reunión)_ | | | | |

**Reflexión final (Día 7) recibida:** ✅ Sí — 4 preguntas contestadas con sustancia (ver revisión de la noche abajo). Autorreporta **L1** con justificación honesta ("semana de familiarización y bases").
**C14 — resultado de verificación para este Champion:** ✅ **Verificado** (10/07 noche) — segunda entrega revisada contra documento real; cumple el criterio S1 (1 caso ancla + reflexión). El histórico de la reversión de la tarde se conserva abajo.

### Revisión 2026-07-10 (tarde) — documento real vs. lo validado verbalmente

En la reunión de las 14:00 se validó verbalmente que los 3 Champions cerraron S1 al 100%. Al revisar el documento de Irvin en Drive (`AIFluency_Irvin_Practica_Dia1-2_NotasPerfilesHermesDIT.docx`), su contenido real es: práctica de Día 1 (Prompt A vs B, ticket real anonimizado) y Día 2 (2 prompts), más notas de preparación para una reunión de seguimiento con DIT sobre perfiles de Hermes. **No incluye la plantilla de caso de uso del Día 6 ni la reflexión del Día 7**, a diferencia de Mario y Patrick, que sí entregaron el paquete completo.

**Acción tomada:** correo enviado a Irvin (ver `04_herramientas/agendas/2026-07-10_email_irvin_completar_evidencia.md`) pidiendo completar el mismo documento en Drive con el caso ancla y la reflexión, usando el flujo acordado hoy (comentador → Aprobar). Douglas además conversó personalmente con él sobre el caso el mismo día. Queda pendiente que Irvin actualice el documento en Drive.

**Veredicto actualizado:** ⚠️ Pendiente — C14 no cierra para Irvin hasta que complete el documento.

### Revisión 2026-07-10 (noche) — segunda entrega verificada ✅

Irvin entregó un documento nuevo en Drive (`Sesion practica de los prompt de la guia version 2`), revisado contra el documento real (espejo local PDF, 9 páginas). **Cumple el criterio S1:**

- **Caso ancla (Día 6):** ✅ plantilla presente y llena — Título ("EQUIPO NO ENCIENDE — Mesa de Servicios UJMD"), problema manual (~15 min), herramienta (Hermes + OpenRouter/Groq), prompt principal, resultado completo (respuesta profesional de 3 pasos + escalamiento) y ajustes ("bien redactado, no apliqué cambios").
- **Reflexión (Día 7):** ✅ las 4 preguntas contestadas. Destaca la #2: detectó que Hermes no cumplió una tarea de ordenamiento de archivos (`dd/mm/aaaa`) y ahora **verifica los datos después de cada tarea** — exactamente el hábito que su bloqueo de diagnóstico (Confianza/Seguridad) necesitaba desarrollar. En #3 muestra criterio de riesgo: empieza S2 por gestión de canales de comunicación y pospone deliberadamente centros de cómputo/equipos en producción por variables de seguridad y privacidad.
- **Extra:** práctica Días 3–5 (modo interactivo, SOUL, banco de respuestas), perfil `Testprofile` con API de modelos Google, y limitante documentada: sin privilegios para crear API Key en ERPNext ni acceso a un MCP de esa plataforma (insumo útil para C18/C19).

**Observaciones no bloqueantes (coaching para S2):**

1. Dos campos de la plantilla quedaron sin personalizar: "Tiempo ahorrado estimado" conserva el texto de ejemplo (`ej: 15 min × 5 = 75 min`) y "¿Lo usaré de nuevo?" quedó sin marcar.
2. El prompt principal del caso ancla ("Solicito ayuda con mi equipo no enciende") es más básico que lo que él mismo demostró el Día 1 con su prompt estructurado del ticket de contraseña AD; el escenario replica el ejemplo de la guía en lugar de un ticket propio.
3. Metodología de entrega (Bloque 5, 10/07): el nombre del documento es mejorable y la entrega fue un documento nuevo en vez de completar el mismo con flujo comentador → "Aprobar" en Drive. Reforzar el flujo acordado a partir de S2.

**Veredicto final:** ✅ **S1 cerrada para Irvin** — C14 cierra 3/3 para el piloto.

---

## Mini-reporte S2 (Productividad personal con IA)

| Campo | Valor |
|---|---|
| Fecha de entrega | 2026-07-22 (vence 17/07 — entregado en prórroga corta) |
| Dónde vive | Drive (`AIFluency_Irvin_S2_MiniReporte`, `02_Conocimiento_Colectivo/` adyacente) |
| Recibido | ✅ — versión 1 con aprobación nativa completa de Drive (22/07 23:27) |
| Veredicto | ✅ **Verificado** 24/07 ~14:59 — aprobación nativa en Versión 1; versión actual difiere por comentarios posteriores pero no invalida (regla confirmada con Douglas 24/07, mismo patrón aplicado a 3 docs de Mario) |
| C15/S2 — resultado para Irvin | ✅ **Cierra 3/3** (Mario ✅ · Irvin ✅ · Patrick ✅) |

## C19 — Procesos medidos (2 procesos)

| # | Proceso | Dónde vive | Veredicto |
|---|---|---|---|
| 1 | Instalación de Software Remoto (Mesa de Servicios) | Drive (`AIFluency_Irvin_C19_InstalaciónSoftwareRemoto`) · carpeta canónica `01_Evidencia_Champions/C19_medicion_antes_despues/Irvin/` | ✅ Aprobado 24/07 |
| 2 | _(2º proceso)_ entregado y validado 27/07 por Douglas | Drive | ✅ Aprobado 27/07 — **C19 cierra 3/3** |

## C20 — Perfil de área Soporte

| Campo | Valor |
|---|---|
| Dónde vive | Drive (`AIFluency_Irvin_C20_PerfilSoporte`) · carpeta canónica `01_Evidencia_Champions/C20_perfiles_area/` |
| Veredicto | ✅ **Aprobado 27/07** por Douglas. **C20 cierra 3/3.** |
| Insumo habilita | Estandarizar `01_piloto/SOUL_plantillas/SOUL_Soporte.md` y la sección Soporte del playbook (`02_playbook/`) |

## C21 — Skill propio (S3, versionado en Git)

| Campo | Valor |
|---|---|
| Dónde vive | Drive (`AIFluency_IrvinMorales_C21_SkillDiagnosticoBaterias.md` + `SKILL.md`) · carpeta canónica `01_Evidencia_Champions/C21_skill_propio/Irvin/` |
| Skill | `diagnostico-baterias-laptops` — diagnóstico remoto de baterías de laptops administrativas vía WinRM (`powercfg /batteryreport`), fórmula de salud documentada y clasificación ≥80/60–79/40–59/<40 |
| Entregado | 2026-07-31 |
| Versionado | Repo Git local de evidencia · commits `76403e5` (skill creado) + `2cc18f4` (rúbrica actualizada) |
| Veredicto | ✅ **Aprobado 07/08** por Douglas (Drive Approvals) — **C21 cierra 3/3 y Fase 1 completa** |

## C22 — SOUL.md propio (C20 → configuración de agente)

| Campo | Valor |
|---|---|
| Dónde vive | Drive (`01_Evidencia_Champions/C22_soul_propio/`) · plantilla `_PLANTILLA_C22_SOUL_Propio` |
| SOUL entregado | SOUL de Soporte — derivado de su C20 (perfil Soporte) |
| Entregado | 2026-08-07 |
| Veredicto | ✅ **Aprobado 07/08** por Douglas (Drive Approvals) — **C22 cierra 3/3** · con C21/C19/S1, **todos los criterios de Licencia Profesional cumplidos** (pendiente veredicto formal) |

## Verificación Director

| Criterio | Estado |
|---|---|
| Evidencia S1 revisada | ✅ (revisión de documento real: tarde 1ª versión incompleta, noche 2ª versión completa — 10/07) |
| Nivel autorreportado coincide con evidencia | ✅ — autorreporta L1 con justificación; consistente con la evidencia (Mario y Patrick autorreportaron L1.5) |
| Sin bloqueos abiertos | ✅ — documento completado; queda solo coaching de metodología de entrega para S2 |
| C15/S2 (mini-reporte) | ✅ — aprobado por Douglas en Drive (24/07 ~14:59) |
| C19 (2 procesos medidos) | ✅ 2/2 — aprobado 24/07 (1º) y 27/07 (2º) |
| C20 (perfil de área Soporte) | ✅ — aprobado por Douglas (27/07) |
| C21 (Skill propio versionado) | ✅ — aprobado por Douglas en Drive (07/08) |
| C22 (SOUL.md propio activo) | ✅ — aprobado por Douglas en Drive (07/08) |

**Firma Douglas:** ✅ 2026-07-10 (noche) — S1 resuelto tras revisión asistida del documento real
**Fecha de última revisión:** 2026-08-07 — C15–C22 cerrados · criterios de Licencia Profesional cumplidos (pendiente veredicto formal)

*Creado: 2026-07-10 · Compromiso C16 · Actualizado 2026-08-07 con cierre C21 (Fase 1 completa) · Piloto AI Fluency UJMD*
