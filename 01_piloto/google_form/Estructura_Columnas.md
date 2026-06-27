# Estructura de Columnas — Plantilla AI Literacy
**Guía de referencia rápida para construir el Google Form desde esta plantilla CSV**

---

## 📊 Resumen del archivo

| Dato | Valor |
|---|---|
| Archivo base | `Plantilla_AI_Literacy_Baseline.csv` |
| Total columnas | **38** (1 timestamp + 37 preguntas) |
| Filas iniciales | 1 encabezado + 1 ejemplo (Douglas) + 3 placeholders (Champions) + 20 vacías |
| Codificación |_UTF-8 con BOM_ (compatible con Google Drive y Excel) |

---

## 🗺️ Mapa de columnas

Esta tabla te dice cómo mapear cada columna del CSV al tipo de pregunta que debes crear en Google Forms.

| # Col | Columna CSV | Tipo en Google Forms | Rango / Opciones |
|---|---|---|---|
| 1 | Timestamp | _Automático (Forms lo pone)_ | No se crea manualmente |
| 2 | Nombre completo | Respuesta corta | Validación: texto |
| 3 | Correo institucional UJMD | Respuesta corta | Validación: correo electrónico |
| 4 | Área | Opción múltiple | Dirección / Infraestructura / Desarrollo / Soporte / Otra área UJMD |
| 5 | Rol actual en el equipo | Respuesta corta | Validación: texto |
| 6 | Antigüedad en la UJMD | Opción múltiple | <1 año / 1-3 años / 3-5 años / >5 años |
| 7 | Herramientas de IA usadas últimos 3 meses | **Casillas** (varias respuestas) | 11 opciones (ver Guía_GoogleForm_AI_Literacy.md) |
| 8 | Frecuencia uso herramienta principal | Opción múltiple | Diaria / Semanal / Mensual / Esporádica |
| 9 | ¿Has dejado de usar alguna herramienta de IA? | Párrafo | _Opcional_ |
| 10 | Caso de uso 1 | Párrafo | _Obligatoria_ |
| 11 | Caso de uso 2 | Párrafo | _Opcional_ |
| 12 | Caso de uso 3 | Párrafo | _Opcional_ |
| 13 | Si NO has usado IA ¿qué tareas podrían beneficiarse? | Párrafo | _Mostrar si marcó "Ninguna" en col 7_ |
| 14 | L0 · Uso chatbots como buscador rápido | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 15 | L1a · Doy contexto adicional | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 16 | L1b · La IA me recuerda cosas | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 17 | L2 · Hago que la IA lea archivos | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 18 | L3 · Tengo espacio de IA con conocimiento fijo | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 19 | L4 · La IA se conecta a herramientas que uso | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 20 | L5 · He definido flujos reutilizables | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 21 | L6 · Delego tareas completas a la IA | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 22 | L7 · La IA ejecuta comandos / navega por mí | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 23 | L8 · He programado agentes autónomos | **Escala lineal 1-5** | 1=Nunca, 5=Siempre |
| 24 | Bloqueo · Falta de tiempo | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 25 | Bloqueo · Conocimiento técnico insuficiente | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 26 | Bloqueo · Falta de confianza | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 27 | Bloqueo · Seguridad / Privacidad | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 28 | Bloqueo · Falta de acceso o permisos | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 29 | Bloqueo · Falta de soporte | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 30 | Bloqueo · Cultura | **Escala lineal 0-3** | 0=Nada, 3=Mucho |
| 31 | Bloqueo principal (abierta) | Párrafo | _Opcional_ |
| 32 | ¿Qué esperas lograr al finalizar el piloto? | Párrafo | _Obligatoria_ |
| 33 | Asistente de IA ideal · 3 tareas que haría | Párrafo | _Obligatoria_ |
| 34 | ¿Estarías dispuesto a enseñar lo aprendido? | Opción múltiple | Sí con gusto / Sí con condiciones / Probablemente no |
| 35 | Si 'con condiciones' ¿cuáles? | Párrafo | _Condicional_ |
| 36 | Formato de aprendizaje preferido | **Casillas** (máx 2) | 5 opciones (ver Guía) |
| 37 | ¿Algo más que quieras compartir? | Párrafo | _Opcional_ |

---

## 🔢 Clave de calificación del Nivel L0-L9

### Sumatoria de la Sección 4 (columnas 14-23)

| Sumatoria | Nivel dominante | Zona |
|---|---|---|
| 10–20 | L0–L2 | Pasajero |
| 21–35 | L3–L5 | Conductor |
| 36–50 | L6–L9 | Piloto Automático |

### Nivel dominante individual

Para cada fila, el nivel dominante se calcula así:
- Para L1, tomar el **máximo** entre L1a y L1b (columnas 15 y 16)
- Encontrar el nivel con la puntuación más alta (L0, L1, L2, ..., L8)
- En caso de empate, se asigna el nivel más alto

### Ejemplo con Douglas (ya registrado en columna)
- Sumatoria L: 10 × 5 = **50** → Piloto Automático
- Nivel dominante: **L8** (agentes autónomos)
- Bloqueos: todos **0** → sin fricciones

---

## 📋 Cómo usar esta plantilla

### Opción A: Subir a Google Drive y luego crear el Form
1. Subir `Plantilla_AI_Literacy_Baseline.csv` a una carpeta de Google Drive
2. Drive lo convertirá automáticamente a Google Sheet
3. Verificar que los acentos y caracteres especiales se ven bien (gracias al BOM UTF-8)
4. Desde el Sheet: `Extensiones → Crear un nuevo formulario`
5. Esto crea un Google Form vinculado como destino de respuestas
6. **Después** debes crear las preguntas manualmente en el Form (una por columna)
7. Usar esta tabla como referencia de tipos y opciones

### Opción B: Crear Form desde cero, respuestas van a la plantilla
1. Crear el Form en forms.google.com
2. Seguir `Guia_GoogleForm_AI_Literacy.md` para crear las 37 preguntas
3. Al activar "Hoja de cálculo de destino", **seleccionar esta plantilla**
4. Google Forms respetará la estructura de columnas y empezará a llenar respuestas en las filas vacías

### Opción C: Usar el consolidador (Apps Script)
1. Una vez que las respuestas caigan en este Sheet
2. Abrir `Extensiones → Apps Script`
3. Pegar el código de `consolidador_appsscript.gs`
4. Ejecutar: generará pestañas RESUMEN_INDIVIDUAL, RESUMEN_AGGREGADO, RESUMEN_CHAMPIONS

---

## 🎯 Fila de ejemplo: Douglas Galindo

Ya está registrada para que:
- Sirva de prueba al crear el Form (validar que las escalas funcionan)
- Muestre el formato esperado para respuestas de texto
- Dé un primer punto de datos del consolidador
- Confirme que Douglas opera en Nivel L8 (score 50, sumatoria máxima)

### Sus valores clave de ejemplo:
- Área: Dirección (Douglas Galindo)
- Herramientas: ChatGPT, Claude, Gemini, Copilot, Perplexity, Ollama, Hermes
- Frecuencia: Diaria
- Niveles L0-L8: todos 5
- Bloqueos: todos 0
- Dispuesto a enseñar: Sí con gusto
- Formato preferido: Aprender haciendo + Pair-working

---

## 🚨 Notas importantes

1. **No modificar encabezados** una vez vinculado a Google Forms (se rompe el mapeo)
2. **No borrar la fila de Douglas** si ya está conectada (sirve de test)
3. **Si Google Drive no respeta tildes/ñ**: reabrir el CSV en un editor plano y volverlo a subir (el BOM ya está incluido)
4. **Los separadores de casillas**: Google Forms usa comas en la misma celda, pero el CSV usa QUOTE_ALL para evitar conflictos
5. **Al escalar a otros roles**: solo agregar opciones a la columna 4 (Área), no modificar la estructura

---

## 🔗 Archivos relacionados

- `Plantilla_AI_Literacy_Baseline.csv` — el archivo CSV de esta documentación
- `Guia_GoogleForm_AI_Literacy.md` — instrucciones completas de montaje del Form
- `consolidador_appsscript.gs` — script para análisis automático
- `Estructura_Columnas.md` — este archivo
- `../Cuestionario_Baseline_AI_Literacy.md` — versión de entrevista presencial
