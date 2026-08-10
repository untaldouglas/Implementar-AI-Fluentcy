# AI Fluency Program — UJMD
**Dirección de Servicios Informáticos · @untaldouglas**  
Framework: Modelo de Conducción AI (MCA) · Herramienta: [Hermes Agent](https://github.com/nousresearch/hermes-agent)

> **Estado (07/08/2026):** Fase 1 (Piloto Champions) ✅ CERRADA 3/3 — C14–C22 completados con evidencia aprobada en Drive · Licencia Básica 3/3 activada · Licencia Profesional a veredicto. Ver `ESTADO_PROYECTO.md` (fuente de verdad viva).

---

## Estructura del repositorio

```
ai-fluency-ujmd/
│
├── 00_marco/               ← Framework conceptual (leer primero)
│   ├── Manual_Implementacion_Estrategica.md   # MCA: L0–L9, 5 licencias
│   ├── Alineacion_Estrategica.md              # Puente manual ↔ roadmap
│   ├── Licencia_Conduccion_AI.md              # Sistema de certificación
│   ├── Protocolo_Investigacion.md             # Protocolo de investigación
│   └── Guia_Aprendizaje_y_Evidencia_por_Licencia.md  # ★ Guía rápida por licencia/nivel (facilitadores e interesados)
│
├── 01_piloto/              ← Capa 0: Los 3 Champions (Fase 1 completada)
│   ├── Roadmap_AI_Fluency_UJMD.md             # Roadmap operativo v2.0
│   ├── Acta_Seleccion_Champions_AI_Fluency.md # Selección formal + roles
│   ├── learning_record/                       # ★ Registros individuales + dashboard (C16)
│   │   ├── irvin_morales.md · mario_valencia.md · patrick_orellana.md
│   │   └── _dashboard.md
│   ├── conocimiento_colectivo/                # ★ Glosario, FAQ, errores (C17)
│   ├── SOUL_plantillas/                       # Configs por área para Hermes
│   │   ├── SOUL_Soporte.md
│   │   ├── SOUL_Desarrollo.md
│   │   └── SOUL_Infraestructura.md
│   ├── evidencia_piloto/                      # ★ Espejo local de evidencia S1
│   └── google_form/                           # Automatización del diagnóstico
│       ├── crear_form_conduccion_ai.gs        # → make create-form
│       ├── consolidador_appsscript.gs
│       ├── calcular_nivel_mca.gs              # ★ Calcula nivel L0-L9 + itinerario
│       ├── Plantilla_AI_Literacy_Baseline.csv
│       └── Guia_GoogleForm_AI_Literacy.md
│
├── 02_playbook/            ← Documento maestro replicable y escalable
│   └── AI_Fluency_Playbook_UJMD.docx          # Guía completa Capas 0–3
│
├── 03_comunicacion/        ← Materiales de difusión y stakeholders
│   ├── OnePager_Rectoria.html / OnePager_Rectoria_F1.html   # Resumen ejecutivo (F1 = resultados)
│   ├── ResearchBrief_AIFluency.html / ResearchBrief_AIFluency_F1.html  # Brief de investigación (F1 = resultados)
│   ├── Email_Coordinadores_Resultados_F1.html # ★ Resultados F1 para coordinadores de área
│   ├── Presentacion_AIFluency_Deck.html       # Deck de presentación
│   ├── Infografico_AIFluency_UJMD.html        # Infográfico del programa
│   ├── Email_Invitacion_Champions.html        # Correos a champions
│   └── brand/                                 # Identidad visual
│
├── 04_herramientas/        ← Dashboards y herramientas operativas
│   ├── Dashboard_Jornada.html                 # Dashboard inicio/fin jornada
│   ├── checklist_artefactos_instalacion_champions.md  # ★ Checklist de verificación de instalaciones
│   ├── auditorias/                            # ★ Serie de auditorías (#01–#02 + cierre F1)
│   ├── guia_setup_champions/                  # Lecciones de setup (archivo histórico)
│   └── dashboards/                            # Registros de jornada
│
├── 05_blog/                ← Blog del proyecto (avances públicos)
├── 06_mercadeo/            ← Materiales de mercadeo
│
├── docs/                   ← GitHub Pages (publicado) — dashboard + infográfico + deck + onboarding + research brief
├── ESTADO_PROYECTO.md      ← Estado vivo del proyecto (actualizar diariamente)
├── Makefile                ← Comandos rápidos (make status, make check-security, etc.)
└── README.md               ← Este archivo
```

---

## Cómo navegar

| Si necesitas… | Ve a… |
|---|---|
| Entender el marco conceptual | `00_marco/Manual_Implementacion_Estrategica.md` |
| Ver el plan operativo | `01_piloto/Roadmap_AI_Fluency_UJMD.md` |
| Saber qué se aprende y qué se entrega por licencia | `00_marco/Guia_Aprendizaje_y_Evidencia_por_Licencia.md` ★ |
| Ver el estado actual del proyecto | `ESTADO_PROYECTO.md` (fuente de verdad) |
| Ver los registros individuales de los Champions | `01_piloto/learning_record/` |
| Verificar una instalación de Hermes | `04_herramientas/checklist_artefactos_instalacion_champions.md` ★ |
| Replicar el programa en otra unidad | `02_playbook/AI_Fluency_Playbook_UJMD.docx` |
| Configurar Hermes Agent para un área | `01_piloto/SOUL_plantillas/` |
| Aplicar el diagnóstico baseline | `01_piloto/google_form/` |
| Presentar resultados a coordinadores | `03_comunicacion/Email_Coordinadores_Resultados_F1.html` ★ |
| Presentar a rectoría (resultados F1) | `03_comunicacion/OnePager_Rectoria_F1.html` ★ |
| Brief de investigación aplicada | `03_comunicacion/ResearchBrief_AIFluency_F1.html` ★ |
| Ver el dashboard publicado | `docs/Dashboard_Jornada.html` |

---

## Comandos rápidos

```bash
make status            # Estado: git + stats del repo
make stats             # Estadísticas del repo
make champions-list    # Lista de Champions
make baseline-summary  # Resumen del baseline
make check-security    # Escaneo de PII/secrets expuestos
make backup            # Backup
```

---

## Modelo de escalamiento (4 Capas)

```
CAPA 0 · Piloto (Mes 1)       → 3 Champions, 1 por área ✅ COMPLETADA
CAPA 1 · Dirección IT (M2-3)  → Todo el equipo (F2 — pendiente de arranque)
CAPA 2 · Universidad (M4-8)   → Otras unidades de negocio UJMD
CAPA 3 · Comunidad (M9-18)    → Docentes y estudiantes
```

---

*AI Fluency Program UJMD · v3.0 · Agosto 2026 (Fase 1 completada)*
