# Instructivo — Skills de Claude para AI Fluency UJMD
**Dirección de Servicios Informáticos · @untaldouglas**  
**Versión:** 1.0 | **Fecha:** 29 junio 2026

---

## ¿Qué es un skill de Claude?

Un **skill** es un conjunto de instrucciones especializadas que le das a Claude para que sepa hacer una tarea concreta de tu proyecto de forma repetible — sin tener que explicarle el contexto desde cero cada vez.

Piénsalo como una "memoria de proceso": el skill ya sabe el framework MCA, las columnas del Form, las áreas del programa, y la lógica de itinerarios. Solo le dices qué quieres y lo hace.

---

## Skills instalados en este proyecto

### 🔵 `jornada-ritual`

**Qué hace:** Ejecuta los rituales de inicio y cierre de jornada. Lee `ESTADO_PROYECTO.md`, calcula el contexto del programa (día, fase, hitos) y presenta el TOP 3 de acciones al iniciar, o actualiza ambos archivos de estado (`ESTADO_PROYECTO.md` + `Dashboard_Jornada.html`) al cerrar.

**Cuándo usarlo:**
- Al empezar el día de trabajo en el programa
- Al cerrar la jornada para dejar todo al día
- En cualquier momento para consultar qué hacer

**Frases de activación:**
```
inicio de jornada
fin de jornada
cierre de jornada
qué hago hoy
```

**Archivo de referencia:** `04_herramientas/RITUAL.md`

---

### 🟣 `mca-script-generator`

**Qué hace:** Genera o adapta el Google Apps Script (`calcular_nivel_mca.gs`) que calcula automáticamente el nivel L0-L9 de cada participante, asigna su licencia de conducción AI y produce su itinerario personalizado de aprendizaje.

**Cuándo usarlo:**
- Primera vez que necesitas el script (cohorte nueva)
- El Form cambió de estructura (columnas en distinto orden)
- Agregas una nueva área al programa (Biblioteca, RRHH, etc.)
- Quieres ajustar la lógica de itinerarios (nuevas semanas, herramientas)
- Necesitas regenerar el script para otra institución que replica el programa

---

## Cómo invocar el skill

### Método 1 — Frase natural (recomendado)

Escribe cualquiera de estas frases en Cowork (Claude) y el skill se activa automáticamente:

```
genera el script MCA para el form de diagnóstico
```
```
adapta el script, agregamos el área de Biblioteca
```
```
el form cambió de estructura, columna X ahora es la 20, actualiza el script
```
```
regenera el script con nuevas semanas para el piloto de agosto
```
```
calcular niveles itinerario AI Fluency
```

### Método 2 — Descripción explícita del cambio

Si necesitas una adaptación específica, sé directo:

```
El programa ahora tiene 4 áreas: Infraestructura, Desarrollo, Soporte y 
Biblioteca. Biblioteca usa Canva y Notion como herramientas principales.
Genera el script actualizado.
```

```
El Form tiene nueva estructura: los scores de nivel ahora empiezan en la 
columna 16 (no 14) porque agregamos 2 preguntas nuevas al inicio. 
Actualiza el CONFIG del script.
```

---

## Qué produce el script generado

Al pegarlo en Google Apps Script y ejecutarlo, crea 3 hojas en el Google Sheet:

| Hoja | Contenido |
|------|-----------|
| **NIVELES_MCA** | Scores L0-L8, nivel dominante, zona (Pasajero/Conductor/Piloto), licencia y bloqueos por participante |
| **ITINERARIOS** | Plan personalizado por semanas (S1-S2 y S3-S4), objetivo de Mes 1, hito de nivel, formato sugerido y caso de uso ancla |
| **RESUMEN_GRUPO** | Nivel promedio, distribución por zona, bloqueos más comunes y recomendaciones para el programa |

También crea el menú **🚗 MCA · AI Fluency** directamente en el Sheet con accesos directos.

---

## Instalación del script generado (paso a paso)

1. **Abre el Google Sheet** vinculado al Form de diagnóstico  
   → El Sheet donde caen las respuestas de https://forms.gle/JHd4a8kHyFh59RkH7

2. **Ve a:** `Extensiones → Apps Script`

3. **Borra** el código que aparece por defecto (`function myFunction() {...}`)

4. **Pega** el código `.gs` completo que generó Claude

5. **Guarda** con `Ctrl+S` (o el ícono de disco en la barra superior)

6. **Recarga el Google Sheet** → aparece el menú `🚗 MCA · AI Fluency`

7. **Cuando tengas respuestas:** `🚗 MCA · AI Fluency → Calcular niveles e itinerarios`

> **Nota:** Si el nombre de la hoja de respuestas es diferente al default `"Respuestas de formulario 1"`, ajusta `CONFIG.HOJA_RESPUESTAS` en la primera sección del script.

---

## Casos de uso frecuentes

### Nueva cohorte, mismo Form
```
Genera el script MCA para una nueva cohorte de julio
```
El skill genera el mismo script base. No necesitas cambiar nada si el Form no cambió.

### Se agregó un área nueva
```
Agrega el área "Biblioteca" al script. Usan Canva y Google Sites como 
herramientas principales. Su caso de uso ancla es "organizar y etiquetar 
recursos digitales con IA".
```
El skill actualiza los diccionarios `herramientasEntrada` y `casosUsoAncla` dentro del script.

### Columnas del Form cambiaron
```
Actualizamos el Form. Los scores de nivel ahora están en las columnas 18-27 
(antes eran 14-23). Los bloqueos están en 28-34. Actualiza el CONFIG.
```
El skill solo modifica el bloque `CONFIG` al inicio del script, sin tocar la lógica.

### Ajustar duración del programa
```
El piloto ahora dura 8 semanas en vez de 4. Agrega semanas 5-6 y 7-8 
al itinerario con actividades de consolidación y preparación para certificación.
```
El skill agrega funciones `generarSemana56()` y `generarSemana78()` al script.

---

## Archivos relacionados

| Archivo | Propósito |
|---------|-----------|
| `01_piloto/google_form/calcular_nivel_mca.gs` | Script base generado (cohorte julio 2026) |
| `01_piloto/google_form/Estructura_Columnas.md` | Mapa de columnas del Form (referencia para adaptaciones) |
| `01_piloto/Cuestionario_Baseline_AI_Literacy.md` | Instrumento de diagnóstico presencial (fuente del Form) |
| `00_marco/Licencia_Conduccion_AI.md` | Framework de certificación L0-L9 |

---

## Historial de versiones del script

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v1.0 | 2026-06-29 | Versión inicial — 3 áreas, 10 columnas de nivel, 7 bloqueos, itinerarios S1-S4 |

---

*Instructivo del programa AI Fluency · MCA · UJMD · @untaldouglas*
