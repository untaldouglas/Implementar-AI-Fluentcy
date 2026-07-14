# C18 — Esquema operativo de integración a Google Workspace

> Preparado para la reunión de seguimiento del **viernes 17/07**. Acordado en Sesión 18 (10/07, Bloque 5): Patrick (Infraestructura) indica cómo y cuándo los Champions tienen acceso; Douglas comparte ejemplos de uso. Ver `ESTADO_PROYECTO.md` (C18) y las notas de la reunión en [`2026-07-10_anotaciones_reunion.md`](2026-07-10_anotaciones_reunion.md).

---

## 0. Alcance — qué es y qué NO es C18

Importante no confundir dos cosas distintas (esta confusión es el hallazgo I8 de la auditoría #01):

| | **C18 (esto)** | Integración técnica GSuite (`00_marco/Alineacion_Estrategica.md`, sección 10) |
|---|---|---|
| Qué es | Formalizar el **uso manual** que ya está funcionando: Champions usando sus cuentas `@ujmd.edu.sv` para compartir/aprobar documentos en Drive, bloques de Calendar, correo | **MCP server + OAuth 2.0 + service account** para que **Hermes Agent lea/escriba** directamente en Gmail/Calendar/Drive/Meet a nombre del usuario |
| Estado | Ya funciona de facto (canal de entrega de evidencia desde el 10/07) — falta documentarlo como esquema | 🔴 Sin arrancar — planificado agosto-octubre 2026 |
| Habilita | L1-L3 (Zona Pasajero/Conductor) — evidencia trazable, colaboración básica | L4-L5 (Copiloto) — el agente opera Workspace en nombre del Champion |
| Responsable | Patrick define el esquema; Douglas aporta ejemplos | Infraestructura + Douglas, con GCP de por medio |

**C18 no depende de la integración técnica.** Es el escalón anterior: ordenar cómo se usa lo que ya existe (cuentas institucionales + Drive compartido) antes de automatizarlo.

---

## 1. Ejemplos de uso (aporte de Douglas)

Casos ya validados en el piloto que sirven de base para el esquema:

1. **Canal de entrega de evidencia (Drive)** — decidido en Sesión 18 (10/07): el Champion comparte el documento como **comentador** mientras está en borrador; cuando está listo para validación, lo pasa a **Aprobar**. Sin PDF. Nombres propios de archivo (ver modelo de Patrick: `EvidenciaS1_CasoAncla_VerificacionDiariaInfraestructura`).
2. **Carpeta compartida del piloto** — `https://drive.google.com/drive/folders/1eNbWpOmgatmQjOM5KZj6FNoA2CGR1kEj` como raíz; cada Champion con subcarpeta propia (evidencia S1/S2, conocimiento colectivo).
3. **Conocimiento colectivo (C17)** — glosario en **hoja electrónica** compartida (edición conjunta los 3), FAQ y lista de errores en **documento** compartido — construcción colaborativa, no un dueño único.
4. **Calendar** — bloques recurrentes Lun/Mar 14:00-15:00 ya creados para Douglas; mismo patrón replicable para que cada Champion bloquee su tiempo de práctica semanal.
5. **ESTADO_PROYECTO en Drive** — copia espejo del estado vivo del proyecto para lectura/edición desde móvil (ya en uso por Douglas, podría extenderse a Patrick para que actualice su parte de C18 directamente ahí).

Estos 5 casos ya prueban que **no hace falta OAuth ni MCP server** para operar — solo cuentas institucionales + convenciones claras de carpetas/permisos. Ese es justamente el vacío que C18 debe cerrar: las convenciones existen implícitamente (en la cabeza de Douglas) pero no están escritas como esquema.

---

## 2. Plantilla para que Patrick complete (esquema operativo de acceso)

> Patrick: no hace falta prosa — llenar la tabla y las 4 preguntas alcanza para el viernes.

### 2.1 Estructura de carpetas y permisos

| Carpeta/recurso | Quién tiene acceso | Nivel de permiso | Convención de nombres |
|---|---|---|---|
| Carpeta raíz del piloto | | | |
| Subcarpeta por Champion | | | |
| Conocimiento colectivo (glosario/FAQ/errores) | | | |
| _(agregar filas según haga falta)_ | | | |

### 2.2 Preguntas a responder

1. **¿Cómo se le da acceso a un Champion nuevo?** (paso a paso: quién comparte, con qué cuenta, qué permiso)
2. **¿Qué pasa si alguien sale del piloto?** (revocación de acceso — hoy no hay proceso definido)
3. **¿Hay algo que NO debería vivir en Drive compartido?** (dato sensible, credenciales, información de producción — enlaza con la regla de datos sintéticos de los SOUL.md)
4. **¿Qué necesita Infraestructura de Douglas para que esto funcione sin fricción?** (ej. permisos de admin en la carpeta raíz, plantilla de estructura de subcarpetas, etc.)

---

## 3. Cómo se usa este documento

- Douglas comparte la sección 1 con Patrick antes del miércoles 15/07 (colaborativa), para que tenga tiempo de completar la sección 2.
- Patrick trae la sección 2 completa a la reunión de seguimiento del **viernes 17/07** — ahí se cierra C18.
- Al cerrar, actualizar `ESTADO_PROYECTO.md` (tabla de compromisos C18) y, si aplica, la fila de I8 en la próxima auditoría (#02, 17/07 AM).

---

*Preparado: 2026-07-13 · Compromiso C18 · Piloto AI Fluency UJMD*
