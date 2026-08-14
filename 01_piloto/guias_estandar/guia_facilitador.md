# Guía del Facilitador — AI Fluency (MCA)

**Programa AI Fluency · Modelo de Conducción AI (MCA) · UJMD — Dirección de Servicios Informáticos**
**Versión:** 1.0 · **Fecha:** 14/08/2026 · **Uso:** facilitadores del programa (Champions de cohortes anteriores que acompañan a participantes nuevos)
**Para quién:** Mario, Irvin y Patrick en F2, y los facilitadores de cohortes futuros.

---

## 1. Rol del facilitador

El facilitador es un **Champion certificado (L4+)** que acompaña a los participantes de un cohorte nuevo. NO es el que sabe más: es el que **ya recorrió el camino** y evita que los demás tropiecen donde él tropezó.

| Hace | No hace |
|---|---|
| Acompaña sesiones semanales (cadencia del programa) | No valida por sí solo la Profesional (eso es del Instructor) |
| Revisa evidencia de Básica con rúbrica (esquema F2: Champion valida + Director co-firma) | No acepta evidencia verbal: siempre documento real en Drive |
| Co-facilita por rotación semanal (R9): Irvin → Mario → Patrick | No reemplaza la decisión del Director |
| Comparte sus pitfalls y errores reales (normaliza fallar) | No inventa resultados ni "arregla" evidencia del participante |
| Mantiene el learning record del participante al día | No escribe la evidencia POR el participante |

## 2. Cadencia y formato

- **Cadencia estándar (heredada de F1):** miércoles 2:00–4:00 PM (colaborativa) + viernes 2:00–3:00 PM (seguimiento individual).
- **Sesiones:** agenda antes (en `04_herramientas/agendas/`), compromisos con plantilla-rúbrica después.
- **Registro:** cada sesión deja traza en el learning record del participante y en el dashboard de jornada.

## 3. El ciclo de cohorte (las 7 fases — ver guía_facilitador sección "fases" o plan_cohorte.md)

```
F0 Planificación → F1 Selección+baseline → F2 Setup → F3 Sesiones semanales →
F4 Verificación continua → F5 Evaluación+cierre (Demo Day) → F6 Post-cierre
```

**Dónde interviene el facilitador:** F1 (acompaña el baseline), F2 (setup técnico), F3 (sesiones), F4 (valida Básica con rúbrica), F5 (apoya el Demo Day), F6 (retrospectiva).

## 4. Verificación de instalación (chequeo rápido en la estación del participante)

```bash
which hermes          # instalado
hermes doctor         # sin errores bloqueantes
hermes chat -q "Hola" # responde
hermes status --all   # estado completo
hermes skills list    # skills instalados
```

Si algo falla, aplicar `04_herramientas/checklist_artefactos_instalacion_champions.md` (generalizado por cohorte).

## 5. Cómo validar evidencia de Básica (rúbrica resumida)

1. El participante comparte el documento como **comentador** en Drive.
2. Verificas que el documento es **real** (artefacto, no narrativa) y que la medición antes/después está completa.
3. Apruebas con la funcionalidad **"Aprobar"** de Drive.
4. Registras el veredicto en el learning record del participante.
5. El Director **co-firma** (esquema transitorio F2 — se revisa al cierre).

> Regla de oro: si el artefacto no existe en la instalación/Drive, el entregable está **pendiente de materializar** — sin importar lo que el participante diga.

## 6. Pitfalls del facilitador (aprendidos en F1)

- **No confundir "avance" con "cierre":** un mini-reporte conforme no cierra C19 (exige la medición completa con plantilla).
- **No aceptar material "enterrado":** la evidencia vive en la carpeta canónica de entrega (C19_medicion_antes_despues/<nombre>/), no en carpetas personales.
- **No validar verbal:** el Demo Day de F1 demostró que verificar contra documento real ≠ validación verbal. Siempre contra el artefacto.
- **Sé honesto con las limitaciones:** el participante debe declarar qué NO delegaría y por qué (criterio de la Profesional).
- **Anota qué datos excluyó el participante por seguridad** — es evidencia de que la delegación segura se interiorizó.

## 7. Al cierre del cohorte (tu contribución)

- Participa en el Demo Day como apoyo técnico de tu área.
- Aporta a la retrospectiva: qué funcionó y qué cambiarías (se consolida en la sección 8 del plan del siguiente cohorte).
- Co-facilitas el próximo ciclo (rotación).

---

*Guía viva — se actualiza con cada cohorte. Marco normativo: `00_marco/Licencia_Conduccion_AI.md`.*
