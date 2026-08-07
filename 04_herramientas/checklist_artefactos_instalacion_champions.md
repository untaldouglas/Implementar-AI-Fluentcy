# Checklist de Verificación — Artefactos en la Instalación de Hermes de cada Champion

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Versión:** 1.0 · **Fecha:** 07/08/2026
**Uso:** verificar que cada estación de Champion contiene los artefactos que sus entregables del programa declaran. Se ejecuta **en la estación del Champion** (con él presente, en su sesión), o por pares (Champion → Champion), o por el Director en sesión de auditoría.

> **Regla del programa:** la evidencia se verifica contra el artefacto real, no contra lo que el Champion dice. Si el artefacto no existe en la instalación, el entregable asociado se marca **pendiente de materializar**, sin importar el estado declarado en Drive.

---

## 1. Verificación base de la instalación (aplica a los 3 Champions)

| # | Artefacto | Comando de verificación | Estado esperado | Entregable asociado |
|---|---|---|---|---|
| 1.1 | Hermes instalado y accesible | `which hermes` | Devuelve ruta (p.ej. `~/.local/bin/hermes`) | C11 — Setup |
| 1.2 | Diagnóstico de salud sin errores | `hermes doctor` | Sin errores bloqueantes (deps, credenciales, config) | C11 — Lección 1 |
| 1.3 | Modelo configurado y responde | `hermes chat -q "¿Capital de El Salvador?"` | Respuesta coherente del agente | C11 — Lección 2 |
| 1.4 | Estado general de la instalación | `hermes status --all` | Output completo sin fallas | C11 — Lección 3 |
| 1.5 | Gateway/mensajería (si aplica) | `hermes gateway status` | Conectado o intencionalmente desactivado (registrar cuál) | C11 |
| 1.6 | Perfil separado de práctica (L2) | `hermes` — perfil/config de práctica distinto del de trabajo | Existe perfil de experimentación con modelo documentado (referencia: `Testprofile` de Irvin) | Auditoría #02 — R15/H9 |

**Verificación por pares (Sesión 0, referencial):** Patrick → Mario (`hermes doctor`), Mario → Irvin (`hermes chat -q`), Irvin → Patrick (`hermes skills list`).

---

## 2. Artefactos de Skills (C21 — por Champion)

> Cada Champion debe tener **su Skill propio instalado** en su Hermes. El Skill vive en `~/.hermes/skills/<nombre>/SKILL.md` y debe coincidir (nombre + contenido) con el versionado en su repositorio Git.

| # | Artefacto | Comando de verificación | Estado esperado |
|---|---|---|---|
| 2.1 | Skill listado | `hermes skills list` | El Skill del Champion aparece en la lista |
| 2.2 | SKILL.md existe en disco | `ls ~/.hermes/skills/<skill>/SKILL.md` | Archivo presente |
| 2.3 | Frontmatter válido | `head -5 ~/.hermes/skills/<skill>/SKILL.md` | `name` y `description` definidos |
| 2.4 | El Skill carga sin error | `hermes skills list` (o `skill_view`) sobre el Skill | Sin errores de carga |
| 2.5 | Coincide con el repo Git | Comparar el SKILL.md local con el del repositorio (commit declarado en C21) | Contenido idéntico o versión posterior documentada |

### Por Champion (C21):

| Champion | Skill esperado | Repo / commit declarado |
|---|---|---|
| Mario Valencia | `refactor-csharp-4` | github.com/mariovalencia/AIFluent · `e09c9f2e` |
| Patrick Orellana | `custom-netmon-dashboard` | github.com/peorellanaa/repo001 · `903a34e` |
| Irvin Morales | `diagnostico-baterias-laptops` | repo Git local · `76403e5` + `2cc18f4` |

---

## 3. Artefactos de SOUL (C20 + C22)

> El SOUL.md propio convierte el perfil de área (C20) en configuración de agente activa (C22). Debe existir en la instalación y ser el que el agente usa.

| # | Artefacto | Comando de verificación | Estado esperado | Champion |
|---|---|---|---|---|
| 3.1 | SOUL.md propio presente | `ls ~/.hermes/` (o ruta declarada por el Champion) | Archivo SOUL.md propio existe | Patrick ✅ (verificado 10/07) · Mario e Irvin pendientes (C22, vence 14/08) |
| 3.2 | Coherente con su perfil C20 | Comparar contenido del SOUL con el perfil de área aprobado (C20 en Drive) | El SOUL refleja el perfil real del área | Los 3 |
| 3.3 | Activación probada | 1 interacción real documentada con el SOUL activo (sección 3 de la plantilla C22) | Evidencia de la interacción en el documento C22 | Mario e Irvin (C22) |

---

## 4. Evidencia local de entregables (espejos del programa)

> El repositorio del programa mantiene espejos locales de la evidencia de Champions en `01_piloto/evidencia_piloto/<champion>/`. La instalación del Champion debe poder referenciar su propia evidencia.

| # | Artefacto | Ubicación esperada | Entregable asociado |
|---|---|---|---|
| 4.1 | Evidencia S1 (caso ancla) | Drive (fuente de verdad) · espejo en `01_piloto/evidencia_piloto/<champion>/` | C14 — S1 |
| 4.2 | Mini-reporte S2 | Drive (`02_Conocimiento_Colectivo/` adyacente o carpeta de evidencia) | C15 — S2 |
| 4.3 | Procesos medidos C19 (2 por Champion) | Drive `01_Evidencia_Champions/C19_medicion_antes_despues/<champion>/` | C19 |
| 4.4 | Perfil de área C20 | Drive `01_Evidencia_Champions/C20_perfiles_area/` | C20 |
| 4.5 | Skill C21 (plantilla + SKILL.md) | Drive `01_Evidencia_Champions/C21_skill_propio/<champion>/` | C21 |
| 4.6 | SOUL C22 (plantilla + SOUL.md) | Drive `01_Evidencia_Champions/C22_soul_propio/<champion>/` | C22 (Mario e Irvin) |

> Nota: los artefactos 4.x se verifican contra Drive (fuente de verdad). La instalación local se revisa para 2.x (Skills) y 3.x (SOUL), que son los que el agente realmente ejecuta.

---

## 5. Resultado de la verificación (rellenar por Champion)

| Campo | Valor |
|---|---|
| Champion | |
| Fecha de verificación | |
| Verificado por | (Champion · par · Douglas) |
| 1. Instalación base | ✅ / ⬜ (detalle: ) |
| 2. Skill C21 instalado y versionado | ✅ / ⬜ |
| 3. SOUL propio activo | ✅ / ⬜ |
| 4. Evidencia en Drive al día | ✅ / ⬜ |
| Veredicto | ✅ Conforme · 🟡 Con ajustes (lista) · 🔴 No conforme |
| Observaciones / pendientes | |

---

## 6. Notas operativas

- **Fuente de verdad:** los artefactos 4.x (evidencia) se validan en Google Drive con la funcionalidad "Aprobar" — el checklist local complementa, no reemplaza, esa validación.
- **Frecuencia sugerida:** después de cada cierre de compromiso (p.ej., al verificar C22 el 14/08) y en la auditoría de cierre de F1.
- **Registrar el output real:** pegar el output de los comandos 1.x–2.x en el learning record del Champion (formato del `protocolo_verificacion.md`), no describirlo.
- **Herramientas del agente (L4–L5, futuro):** cuando los Champions avancen a Licencia Profesional/Avanzada, agregar verificación de herramientas activas (`hermes tools`), automatizaciones (`hermes cron list` / cron jobs) y Skills en repositorio compartido del equipo.

---

*Documento vivo — se actualiza con cada ciclo de certificación. Base: `04_herramientas/guia_setup_champions/` (lecciones 01–03), `protocolo_verificacion.md` (Niveles 1–4), compromisos C11/C14–C22 del programa.*
