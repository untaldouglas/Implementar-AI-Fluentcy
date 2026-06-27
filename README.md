# Implementar AI Fluentcy

Sistema integral para desarrollar competencias de IA en equipos técnicos, basado en el modelo de 10 niveles de autonomía vehicular de Reuven Gorsht.

## 🎯 Propósito

Este repositorio contiene la infraestructura completa para implementar un programa de **AI Fluency** (competencia en IA) en organizaciones. El proyecto está diseñado para:

- Evaluar el nivel actual de uso de IA en un equipo
- Guiar la progresión desde uso básico hasta agentes autónomos
- Construir habilidades reutilizables (Skills) que la IA puede ejecutar
- Medir el avance del equipo mediante cuestionarios y métricas

## 📚 Fundamentos teóricos

El enfoque está basado en el artículo **"Domina la IA Antes de Que la IA Te Domine"** de Reuven Gorsht, que propone una escala de 10 niveles de autonomía:

### Las 3 zonas de competencia

| Zona | Niveles | Descripción |
|------|---------|-------------|
| **Pasajero** | 0-2 | Uso reactivo: preguntas básicas, memoria, acceso local |
| **Conductor** | 3-5 | Uso activo: proyectos persistentes, MCP, Skills personalizados |
| **Piloto automático** | 6-9 | Delegación total: agentes async, enjambres, flotas autónomas |

## 🗂️ Estructura del repositorio

```
Implementar AI Fluentcy/
├── 📄 Roadmap_AI_Fluency_UJMD.md
│   Plan de 6 meses para la Universidad Dr José Matías Delgado
│   Contiene fases, métricas y criterios de éxito
│
├── 📄 Alineacion_Estrategica_Manual_Roadmap.md
│   Documento que conecta la teoría con el roadmap UJMD
│   Incluye el modelo completo de 10 niveles
│
├── 📚 Manual_de_Implementacion_Estrategica.md
│   Marco conceptual completo
│   Explica la metáfora del combustible y los patrones de interacción
│
├── 📋 Cuestionario_Baseline_AI_Literacy.md
│   Instrumento de evaluación inicial
│   Mide el nivel de AI Literacy del equipo
│
├── 📝 Acta_Seleccion_Champions_AI_Fluency.md
│   Proceso de selección de los primeros 3 usuarios avanzados
│   Criterios y metodología
│
├── 📁 SOUL_plantillas/
│   Perfiles de personalidad para el agente de IA
│   ├── SOUL_Infraestructura.md
│   ├── SOUL_Desarrollo.md
│   └── SOUL_Soporte.md
│
├── 📁 google_form/
│   Implementación digital del cuestionario
│   ├── Guia_GoogleForm_AI_Literacy.md
│   ├── Plantilla_AI_Literacy_Baseline.csv
│   ├── Estructura_Columnas.csv
│   ├── consolidador_appscript.gs
│   └── montaje_automatico_script.gs
│
└── 📁 dashboards/
    Seguimiento del avance del proyecto
    ├── dashboard_base.md
    ├── plan_*.md (planes diarios)
    └── cierre_*.md (cierres diarios)
```

## 🚀 Cómo usar este repositorio

### Para equipos que quieren implementar AI Fluentcy

1. **Lee el marco conceptual**
   - Comienza con `Manual_de_Implementacion_Estrategica.md`
   - Entiende los 10 niveles y las 3 zonas

2. **Evalúa tu equipo**
   - Usa `Cuestionario_Baseline_AI_Literacy.md`
   - O despliega la versión digital en `google_form/`

3. **Selecciona tus Champions**
   - Sigue el proceso en `Acta_Seleccion_Champions_AI_Fluency.md`
   - Identifica 3 personas que liderarán la adopción

4. **Configura perfiles de IA**
   - Usa los templates en `SOUL_plantillas/`
   - Adapta según tu contexto organizacional

5. **Sigue el roadmap**
   - Adapta `Roadmap_AI_Fluency_UJMD.md` a tu realidad
   - Define tus propias métricas y milestones

### Para investigadores y educadores

- El modelo de 10 niveles puede aplicarse a cualquier contexto
- Los cuestionarios están validados para equipos técnicos
- La progresión está diseñada para ser incremental y medible

## 📊 Metodología de evaluación

El cuestionario baseline mide 4 dimensiones:

1. **Herramientas actuales**: Qué herramientas de IA usa el equipo
2. **Casos de uso**: En qué contextos aplican IA
3. **Nivel de autonomía**: Cómo evalúan su competencia (L0-L9)
4. **Bloqueos**: Qué impide avanzar

**Resultado**: Cada persona recibe un nivel estimado (L0-L9) y se identifica su zona de competencia.

## 🔧 Componentes técnicos

### Google Form + Apps Script

El directorio `google_form/` contiene:
- Guía para crear el formulario de evaluación
- Plantilla CSV para importar preguntas
- Script de consolidación automática de respuestas
- Script opcional para crear el formulario programáticamente

### Plantillas SOUL.md

Los perfiles SOUL.md definen cómo el agente de IA debe comportarse según el contexto:
- **Infraestructura**: Enfoque en operaciones y disponibilidad
- **Desarrollo**: Enfoque en calidad de código y buenas prácticas
- **Soporte**: Enfoque en resolución de problemas y atención al usuario

### Dashboards de seguimiento

Los dashboards diarios permiten:
- Monitorear el avance contra el roadmap
- Identificar bloqueantes temprano
- Celebrar logros incrementalmente

## 📈 Métricas de éxito

El proyecto define métricas para cada fase:

**Fase 1 (Mes 1)**: 3 Champions con nivel ≥ L5
**Fase 2 (Meses 2-3)**: 80% del equipo supera evaluación
**Fase 3 (Meses 4-6)**: Procesos con IA automatizados documentados

## 🤝 Contribuciones

Este repositorio es un framework abierto. Si lo adaptas a tu contexto:

1. Mantén la estructura conceptual (10 niveles, 3 zonas)
2. Adapta los cuestionarios a tu dominio
3. Comparte tus mejoras con la comunidad

## 📝 Nota sobre los datos

Este repositorio contiene **plantillas y metodologías**, no datos reales de la UJMD. Los archivos de respuestas (CSV con datos de personas) están excluidos del control de versiones por políticas de privacidad.

## 🏛️ Créditos

- **Modelo de 10 niveles**: Reuven Gorsht
- **Adaptación educativa**: @untaldouglas — Dirección de Servicios Informáticos UJMD
- **Fecha de creación**: Junio 2026

## 📄 Licencia

Este material está bajo licencia Creative Commons BY-NC-SA 4.0

Puedes:
- ✅ Compartir y adaptar el material
- ✅ Usar para fines educativos

Con las siguientes condiciones:
- 📌 Atribución: Cita al autor original (Reuven Gorsht)
- 📌 No comercial: No uses para fines comerciales
- 📌 Compartir igual: Si adaptas, comparte bajo la misma licencia

## 🔗 Recursos relacionados

- [Artículo original](https://reuven-gorsht.medium.com/domina-la-ia-antes-de-que-la-ia-te-domine-a-ti-8d23b6b60c4c) de Reuven Gorsht
## 📞 Contacto

Para preguntas sobre la implementación en la UJMD:
- @untaldouglas — Dirección de Servicios Informáticos
- Universidad Dr. José Matías Delgado

---

**Estado del proyecto**: 🟡 En implementación (Fase 1 - Piloto con 3 Champions)

**Última actualización**: 25 de junio de 2026
