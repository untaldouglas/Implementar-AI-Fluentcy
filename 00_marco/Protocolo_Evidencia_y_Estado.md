# Protocolo de Evidencia y Estado — Sistema de Operación Coherente
**Versión:** 1.0 | **Fecha:** 17 julio 2026 | **Origen:** consultoría de consistencia tras auditoría #02 (resuelve I9, I10, I11, R13, R14; previene recurrencia de I1)

---

## 1. Diagnóstico: por qué pasó lo que pasó

Las auditorías #01 y #02 encontraron el mismo patrón tres veces en distintos lugares:

| Incidente | Dónde | Qué pasó |
|---|---|---|
| I1 (aud. #01) | Reunión → learning_record | Se certificó S1 por reporte verbal; el documento real no coincidía |
| I9 (aud. #02) | learning_record → guia_setup | Un resumen marca ✅✅✅ citando un "detalle con evidencia" que está vacío |
| I10 (aud. #02) | Log de ESTADO_PROYECTO | Se registró como "verificado y completado" un hito futuro que luego no ocurrió |

**Causa raíz:** no es (solo) la doble ubicación GitHub/Drive. Es que **cada hecho del proyecto vive en varios documentos a la vez, sin que ninguno esté declarado como fuente única, y los estados se escriben en el momento del compromiso o del reporte — no en el momento de la verificación.** La dualidad GitHub/Drive es la instancia más visible del problema (la evidencia vive en Drive, el estado en Git, y nada los conecta obligatoriamente), pero I9 ocurrió íntegramente dentro del repo e I10 dentro de un solo archivo. Mientras un hecho tenga N copias mantenidas a mano por un solo operador (factor bus = 1, H6), la divergencia no es un riesgo: es una certeza estadística.

**Agravante detectado el 17/07:** existen **dos carpetas de Drive del proyecto en cuentas distintas** — `1eNbWpOmgatmQjOM5KZj6FNoA2CGR1kEj` (registrada en ESTADO, accesible vía token Hermes) y `1QDKBHqX-cimWgiEiIBDRQNE161FNWT1M` (propiedad de douglasag@gmail.com, accesible vía conector claude.ai, contiene el ESTADO_PROYECTO en Docs y los artefactos del programa). Ambas contienen artefactos reales del proyecto. Esto es literalmente la causa raíz en acción: dos "fuentes canónicas" de evidencia que ninguna herramienta ve completas a la vez.

---

## 2. Principio único

> **Un hecho → una fuente canónica → las demás copias son renders que se actualizan desde ella, nunca al revés, y siempre en la misma sesión.**
>
> **Un estado "✅ Verificado" sin enlace a evidencia es inválido por definición.**

---

## 3. Mapa de fuentes canónicas

| Tipo de hecho | Fuente canónica (única) | Renders permitidos (se actualizan DESDE la fuente, misma sesión) |
|---|---|---|
| Estado de compromisos (C#) | Tabla de compromisos de `ESTADO_PROYECTO.md` | `Dashboard_Jornada.html` (ambas copias), Docs de ESTADO en Drive |
| Evidencia de Champions | **Google Drive — carpeta única del proyecto** (ver §7) | Espejo local en `01_piloto/evidencia_piloto/` (solo archivo, no fuente) |
| Veredicto de verificación por Champion | `01_piloto/learning_record/<champion>.md` | `learning_record/_dashboard.md` |
| Definiciones del marco (niveles, licencias, criterios) | `00_marco/Licencia_Conduccion_AI.md` y `Manual_Implementacion_Estrategica.md` | Roadmap, guías, actas — citan, no redefinen |
| Calendario de fases | Tabla F0–F4 de `ESTADO_PROYECTO.md` | Roadmap (con nota de mapeo, no numeración propia) |
| Historia del proyecto | Log de `ESTADO_PROYECTO.md` (append-only) | Blog, dashboards |

**Regla de referencias:** un documento solo puede citar a otro como "evidencia" o "detalle" si ese destino existe y está lleno. Si el destino se archiva o queda obsoleto, la referencia se corrige en el mismo commit que lo archiva. Puntero roto = hallazgo de auditoría automático.

---

## 4. Máquina de estados de un compromiso

```
⚪ DEFINIDO ──→ 🟡 EN CURSO ──→ 📥 ENTREGADO ──→ ✅ VERIFICADO
                    │                (existe en Drive,   (Douglas abrió el documento real,
                    │                 sin revisar)        cumple el criterio, y registró
                    ↓                                     el enlace + fecha + "Aprobar" en Drive)
                🔴 VENCIDO ──→ ventana de recuperación única (fecha fija) ──→ 📥 o queda 🔴
```

Reglas no negociables:

1. **✅ requiere tres campos juntos:** enlace/ubicación de la evidencia + fecha de verificación + quién verificó. Sin los tres, el estado máximo posible es 📥.
2. **Nada salta de 🟡 a ✅.** El paso por 📥 (documento existente en Drive) es obligatorio — esto es lo que I1 e I9 se saltaron.
3. **La verificación se registra en la misma sesión en que ocurre**, en la fuente canónica primero, renders después. No se deja "para el cierre de jornada".
4. **El reporte verbal nunca cambia un estado.** Puede motivar abrir el documento — nada más (regla de la agenda del 17/07, ahora política permanente).
5. **Todo compromiso nuevo que exija evidencia de Champions nace equipado** (regla del 17/07): antes de anunciarlo deben existir (a) su **plantilla-rúbrica** en Drive (prefijo `_PLANTILLA_`, en la carpeta del entregable: instrucciones de copia/renombre, campos del criterio de aceptación, rúbrica de autoevaluación y bloque de veredicto del Director) y (b) la **ubicación exacta de entrega** declarada en la matriz de compromisos de `ESTADO_PROYECTO.md`. Sin plantilla y ubicación, el compromiso no se anuncia — un criterio que solo vive en la cabeza del Director o en una agenda es el patrón I1/I9 esperando repetirse.

---

## 5. Regla de lenguaje del log (resuelve I10 / R14)

En el log de `ESTADO_PROYECTO.md`:

- **Tiempo pasado + "verificado/completado/cerrado"**: solo para hechos ya ocurridos y verificados con evidencia al momento de escribir la entrada.
- **Hitos futuros**: siempre "objetivo:", "planificado:", "compromiso de que...". Nunca "quedaron cerrados" para algo que depende de una reunión o entrega que aún no sucede.
- **Correcciones**: se corrige con una entrada nueva que cite a la anterior (como se hizo el 16/07 con C19) — las entradas históricas no se reescriben.

---

## 6. Convenciones de notación (resuelve I5, I11, y parte de I4)

| Símbolo | Significa ÚNICAMENTE | Nunca usarlo para |
|---|---|---|
| `L0`–`L9` | Niveles MCA | Lecciones de setup (escribir "Lección 1/2/3" con palabra completa) |
| `S1`–`S4` | Semanas pedagógicas del piloto (Roadmap: Fundamentos / Productividad / Agentes / Demo Day) | Semanas calendario (escribir el rango de fechas: "semana del 15–21/07") |
| `F0`–`F4` | Fases del programa según la tabla canónica de `ESTADO_PROYECTO.md` | — (el Roadmap mapea sus fases a estas, no mantiene numeración propia) |
| `C1`, `C2`… | Compromisos de la matriz de `ESTADO_PROYECTO.md` | — |
| `I#`, `H#`, `R#` | IDs de la serie de auditorías (numeración continua entre ediciones) | — |

---

## 7. GitHub ↔ Google Drive: qué vive dónde

| | GitHub (repo + Pages) | Google Drive |
|---|---|---|
| **Es la fuente de** | Estado, criterios, marco, historia, dashboards | Evidencia de Champions (documentos de trabajo, con flujo comentador→Aprobar) |
| **Nunca contiene** | Datos de participantes llenados, respuestas baseline, PII (`.gitignore`) | El estado oficial del proyecto (el Docs de ESTADO es render de lectura móvil, no fuente) |
| **Conexión obligatoria** | Todo ✅ en el repo enlaza la evidencia de Drive (URL o nombre exacto + carpeta) | Todo documento aprobado en Drive queda citado en el learning record correspondiente |

**✅ DECISIÓN TOMADA (17/07/2026, mediodía):** la carpeta canónica única es `1eNbWpOmgatmQjOM5KZj6FNoA2CGR1kEj` ("AIFluent Junio 2026"). Estructura creada el mismo día: `00_Gobernanza` (Actas_Licencias, Bitacoras_Reuniones) · `01_Evidencia_Champions` (S1/S2 por Champion, `C19_medicion_antes_despues/`, `C20_perfiles_area/`) · `02_Conocimiento_Colectivo` · `03_Material_Programa` · `04_Diagnostico_RESTRINGIDO` — con un README de reglas de uso en la raíz. La carpeta `1QDKBHqX…` (douglasag@gmail.com) queda **obsoleta**: su contenido útil (ESTADO en Docs, actas de licencia) fue recreado en la canónica, y **la conexión de claude.ai con douglasag@gmail.com se elimina** — no debe volver a usarse para el proyecto (ejecutado y verificado 17/07: sin acceso a la carpeta B ni a sus archivos). Acceso agéntico a Drive: vía `gdai`/`google_api.py` (token Hermes, cae por defecto en la carpeta canónica) o vía el conector de claude.ai, que desde el 17/07 autentica como **dagalindo@ujmd.edu.sv**.

---

## 8. Ritual de sincronización (cierre de cada sesión de trabajo)

1. ¿Cambió algún estado de compromiso? → actualizar la tabla de `ESTADO_PROYECTO.md` (fuente) con evidencia enlazada.
2. → actualizar `Dashboard_Jornada.html` en `04_herramientas/` y copiar a `docs/` (deben quedar idénticos).
3. → si hay veredicto por Champion, actualizar su `learning_record/<champion>.md` + `_dashboard.md`.
4. Añadir entrada al log (respetando §5).
5. Ejecutar `bash 04_herramientas/check_consistencia.sh` — debe pasar en verde antes del commit.
6. Commit + push (el push publica los renders en Pages).

---

## 9. Prevención automatizada

`04_herramientas/check_consistencia.sh` verifica en cada cierre (y puede sumarse a la rutina de auditoría semanal):

1. Las dos copias de `Dashboard_Jornada.html` son idénticas.
2. No hay referencias a la carpeta de Drive no canónica en documentos vivos.
3. No reaparece la frase-puntero "detalle con evidencia" hacia archivos archivados (patrón I9).
4. El log no introduce "verificado y completado" en entradas nuevas que mencionen fechas futuras (patrón I10, chequeo advisory).

Lo que el script no puede ver (contenido de Drive), lo cubre la auditoría semanal con la regla de **verificación de segundo nivel** instaurada en la #02: abrir también el documento al que apunta el documento.

---

*Documento vivo. Cambios a este protocolo se registran en el log de `ESTADO_PROYECTO.md`.*
