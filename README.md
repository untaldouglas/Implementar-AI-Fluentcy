# AI Fluency Program — UJMD
**Dirección de Servicios Informáticos · @untaldouglas**  
Framework: Modelo de Conducción AI (MCA) · Herramienta: [Hermes Agent](https://github.com/nousresearch/hermes-agent)

---

## Estructura del repositorio

```
ai-fluency-ujmd/
│
├── 00_marco/               ← Framework conceptual (leer primero)
│   ├── Manual_Implementacion_Estrategica.md   # MCA: L0–L9, 5 licencias
│   ├── Alineacion_Estrategica.md              # Puente manual ↔ roadmap
│   ├── Licencia_Conduccion_AI.md              # Sistema de certificación
│   └── Protocolo_Investigacion.md             # Protocolo de investigación
│
├── 01_piloto/              ← Capa 0: Los 3 Champions (Mes 1)
│   ├── Roadmap_AI_Fluency_UJMD.md             # Roadmap operativo v2.0
│   ├── Acta_Seleccion_Champions_AI_Fluency.md # Selección formal + roles
│   ├── Cuestionario_Baseline_AI_Literacy.md   # Diagnóstico de entrada/salida
│   ├── SOUL_plantillas/                       # Configs por área para Hermes
│   │   ├── SOUL_Soporte.md
│   │   ├── SOUL_Desarrollo.md
│   │   └── SOUL_Infraestructura.md
│   └── google_form/                           # Automatización del diagnóstico
│       ├── crear_form_conduccion_ai.gs        # → make create-form
│       ├── consolidador_appsscript.gs
│       ├── Plantilla_AI_Literacy_Baseline.csv
│       ├── Estructura_Columnas.md
│       └── Guia_GoogleForm_AI_Literacy.md
│
├── 02_playbook/            ← Documento maestro replicable y escalable
│   └── AI_Fluency_Playbook_UJMD.docx          # Guía completa Capas 0–3
│
├── 03_comunicacion/        ← Materiales de difusión y stakeholders
│   ├── Email_Invitacion_Champions.html        # Correos a champions
│   ├── EmailPack_AIFluency.html               # Pack de comunicación
│   ├── OnePager_Rectoria.html                 # Resumen ejecutivo
│   ├── Presentacion_AIFluency_Deck.html       # Deck de presentación
│   ├── Infografico_AIFluency_UJMD.html        # Infográfico del programa
│   ├── ResearchBrief_AIFluency.html           # Brief de investigación
│   └── brand/                                 # Identidad visual
│       ├── Brand_Alternativas_AI_Fluency.html
│       └── Brand_VelocidadDigital_LightVersion.html
│
├── 04_herramientas/        ← Dashboards y herramientas operativas
│   ├── onboarding.html                        # Portal de onboarding
│   ├── Dashboard_Jornada.html                 # Dashboard inicio/fin jornada
│   └── dashboards/                            # Registros de jornada
│
├── 05_blog/                ← Blog del proyecto (avances públicos)
│   └── 2026-06-26_aprender-a-manejar-...html # Primer post
│
├── ESTADO_PROYECTO.md      ← Estado vivo del proyecto (actualizar diariamente)
├── Makefile                ← Comandos rápidos (make create-form, etc.)
└── README.md               ← Este archivo
```

---

## Cómo navegar

| Si necesitas… | Ve a… |
|---|---|
| Entender el marco conceptual | `00_marco/Manual_Implementacion_Estrategica.md` |
| Ver el plan operativo | `01_piloto/Roadmap_AI_Fluency_UJMD.md` |
| Replicar el programa en otra unidad | `02_playbook/AI_Fluency_Playbook_UJMD.docx` |
| Configurar Hermes Agent para un área | `01_piloto/SOUL_plantillas/` |
| Aplicar el diagnóstico baseline | `01_piloto/Cuestionario_Baseline_AI_Literacy.md` |
| Ver el estado actual del proyecto | `ESTADO_PROYECTO.md` |
| Presentar a directivos | `03_comunicacion/OnePager_Rectoria.html` |

---

## Comandos rápidos

```bash
make create-form      # Crea el Google Form de diagnóstico MCA
```

---

## Modelo de escalamiento (4 Capas)

```
CAPA 0 · Piloto (Mes 1)       → 3 Champions, 1 por área
CAPA 1 · Dirección IT (M2-3)  → Todo el equipo (10-25 personas)
CAPA 2 · Universidad (M4-8)   → Otras unidades de negocio UJMD
CAPA 3 · Comunidad (M9-18)    → Docentes y estudiantes
```

---

*AI Fluency Program UJMD · v2.0 · Junio 2026*
