# Google Form — Cuestionario Baseline AI Literacy
**Estructura para montar en Google Forms**  
**Uso:** Piloto AI Fluency UJMD → Champions (ahora) → escalamiento a Dirección (Fase 2) → toda UJMD (Fase 3+)

---

## 📋 Instrucciones rápidas de montaje

1. Ir a [forms.google.com](https://forms.google.com) → Crear formulario en blanco
2. Nombrar: **"AI Literacy Baseline · Dirección de Informática UJMD"**
3. Agregar descripción (ver abajo)
4. Configurar:
   - ✅ **Recopilar correo electrónico** (verificación institucional)
   - ✅ **Limitar a 1 respuesta**
   - ✅ **Restringir a usuarios de** → `@ujmd.edu.sv`
5. Crear secciones (ver estructura abajo) — usa el botón "Agregar sección" (ícono de dos rectángulos)
6. Al terminar, habilitar "Enviar respuestas a una hoja de cálculo"
7. Compartir enlace en Teams / correo a los Champions

---

## 🏠 Título y descripción del formulario

**Título:**
> Cuestionario Baseline de AI Literacy · Dirección de Servicios Informáticos UJMD

**Descripción:**
> Este cuestionario diagnóstico nos ayuda a conocer tu punto de partida con herramientas de IA. Tus respuestas nos permitirán diseñar un piloto de adopción ajustado a tus necesidades reales.
>
> **Tiempo estimado:** 25–30 minutos  
> **Destinatarios:** Equipo piloto de la Dirección de Servicios Informáticos  
> **Confidencialidad:** Las respuestas se usan exclusivamente para el diseño del programa AI Fluency UJMD. Se aplican mocks sintéticos; ningún dato real de estudiantes o operaciones se incluirá en los análisis.  
> **Herramienta oficial del programa:** Hermes Agent (NousResearch, open source)
>
> 📅 Fecha de aplicación: [Completar]  
> 🎯 Responsable: Douglas Galindo, Director de Servicios Informáticos

---

## 📐 Estructura del formulario — Por secciones

---

### **SECCIÓN 1: Datos del participante**

**Pregunta 1 — Nombre completo**
- Tipo: *Respuesta corta*
- Obligatoria: ✅
- Validación: Texto

**Pregunta 2 — Correo institucional UJMD**
- Tipo: *Respuesta corta*
- Obligatoria: ✅
- Validación: Correo electrónico

**Pregunta 3 — Área**
- Tipo: *Opción múltiple (una respuesta)*
- Obligatoria: ✅
- Opciones:
  - Dirección (Douglas Galindo)
  - Infraestructura
  - Desarrollo
  - Soporte / Mesa de Servicios
  - Otra área UJMD (escalamiento futuro)

**Pregunta 4 — Rol actual en el equipo**
- Tipo: *Respuesta corta*
- Obligatoria: ✅

**Pregunta 5 — Antigüedad en la UJMD**
- Tipo: *Opción múltiple*
- Opciones:
  - Menos de 1 año
  - 1 a 3 años
  - 3 a 5 años
  - Más de 5 años

---

### **SECCIÓN 2: Inventario de herramientas de IA**

**Pregunta 6 — Herramientas de IA que has usado en los últimos 3 meses**
- Tipo: *Casillas (varias respuestas)*
- Obligatoria: ✅
- Opciones:
  - ChatGPT (OpenAI)
  - Claude (Anthropic)
  - Gemini (Google)
  - Copilot de Microsoft (Office 365)
  - GitHub Copilot (IDE)
  - Perplexity u otro buscador con IA
  - Herramientas de generación de imágenes (DALL·E, Midjourney, etc.)
  - Ollama o modelos locales
  - Hermes Agent (NousResearch)
  - Ninguna
  - Otra (especificar al final)

**Pregunta 7 — Frecuencia de uso de la herramienta principal**
- Tipo: *Opción múltiple*
- Pregunta condicional: se activa al responder P6
- Opciones:
  - Diaria (la uso casi todos los días)
  - Semanal (varias veces por semana)
  - Mensual (la uso de vez en cuando)
  - Esporádica (una o dos veces en 3 meses)

**Pregunta 8 — ¿Has dejado de usar alguna herramienta de IA? ¿Por qué?**
- Tipo: *Párrafo*
- Obligatoria: ❌

---

### **SECCIÓN 3: Casos de uso reales**

**Pregunta 9 — Describe un caso donde hayas usado IA en los últimos 3 meses para resolver algo real**
- Tipo: *Párrafo*
- Obligatoria: ✅
- Texto de ayuda: "Describe: (1) Qué tarea hacías, (2) Qué herramienta usaste, (3) Si resolvió a la primera o requirió iteraciones."

**Pregunta 10 — Segundo caso de uso (si aplica)**
- Tipo: *Párrafo*
- Obligatoria: ❌

**Pregunta 11 — Tercer caso de uso (si aplica)**
- Tipo: *Párrafo*
- Obligatoria: ❌

**Pregunta 12 — Si NO has usado IA en el trabajo, ¿qué tareas crees que podrían beneficiarse?**
- Tipo: *Párrafo*
- Obligatoria: ✅
- Lógica de salto: mostrar solo si marca "Ninguna" en P6 o no respondió P9 (opcional; Google Forms no soporta saltos complejos nativos, dejarlo abierto)

---

### **SECCIÓN 4: Autodiagnóstico de autonomía (L0–L9)**

**Instrucción visible en la sección:**
> Para cada afirmación, marca en qué grado se aplica a ti actualmente. 1 = Nunca, 5 = Siempre/Con total confianza.

**Pregunta 13 — L0 · Taxi: Uso chatbots como buscador rápido (pregunta → respuesta → cerrar)**
- Tipo: *Escala lineal*
- Rango: 1 a 5
- Etiquetas: 1="Nunca", 5="Siempre"

**Pregunta 14 — L1 · Chofer: Cuando una IA responde, le doy contexto adicional o pido que refine**
- Tipo: *Escala lineal* 1–5

**Pregunta 15 — L1 · Memoria: La IA que uso me "recuerda" cosas entre sesiones (preferencias, proyectos)**
- Tipo: *Escala lineal* 1–5

**Pregunta 16 — L2 · Archivos locales: Hago que la IA lea archivos de mi equipo (documentos, reportes, contratos)**
- Tipo: *Escala lineal* 1–5

**Pregunta 17 — L3 · Contexto persistente: Tengo un espacio de IA con conocimiento fijo de mi área (proyectos/instructivos)**
- Tipo: *Escala lineal* 1–5

**Pregunta 18 — L4 · Conexiones: La IA se conecta a herramientas que uso (Slack, Drive, Notion, ERP, correo)**
- Tipo: *Escala lineal* 1–5

**Pregunta 19 — L5 · Playbooks: He definido flujos de trabajo reutilizables que la IA sigue al pie de la letra**
- Tipo: *Escala lineal* 1–5

**Pregunta 20 — L6 · Delegación: Delego tareas completas a la IA y las recupero terminadas**
- Tipo: *Escala lineal* 1–5

**Pregunta 21 — L7 · Terminal/navegador: La IA ejecuta comandos en terminal o navega en la web por mí**
- Tipo: *Escala lineal* 1–5

**Pregunta 22 — L8 · Agentes programados: He programado agentes que trabajan solos en horario no laborable (auditorías, reportes)**
- Tipo: *Escala lineal* 1–5

---

### **SECCIÓN 5: Bloqueos percibidos**

**Instrucción visible:**
> En qué medida cada bloqueo te frena para usar más IA en tu trabajo diario.

**Pregunta 23 — Falta de tiempo**
- Tipo: *Escala lineal* 0 a 3
- Etiquetas: 0="Nada", 3="Mucho"

**Pregunta 24 — Conocimiento técnico insuficiente**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 25 — Falta de confianza en la respuesta**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 26 — Seguridad / Privacidad (no sé qué puedo subir)**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 27 — Falta de acceso o permisos**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 28 — Falta de soporte si algo falla**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 29 — Cultura (siento que no es para mi rol)**
- Tipo: *Escala lineal* 0 a 3

**Pregunta 30 — Bloqueo principal (abierta)**
- Tipo: *Párrafo*
- Texto de ayuda: "De los 7 anteriores, ¿cuál es el principal y por qué?"

---

### **SECCIÓN 6: Expectativas y motivación**

**Pregunta 31 — ¿Qué esperas lograr al finalizar el piloto?**
- Tipo: *Párrafo*
- Obligatoria: ✅

**Pregunta 32 — Si tuvieras un "asistente de IA ideal" para tu área, ¿qué 3 tareas haría?**
- Tipo: *Párrafo*
- Texto de ayuda: "Describe: (1), (2), (3)"

**Pregunta 33 — ¿Estarías dispuesto a enseñar lo aprendido a tu equipo al finalizar el piloto?**
- Tipo: *Opción múltiple*
- Opciones:
  - Sí, con gusto
  - Sí, con condiciones (especifica al final)
  - Probablemente no

**Pregunta 34 — Si respondiste "con condiciones", ¿cuáles?**
- Tipo: *Párrafo*
- Obligatoria: ❌

**Pregunta 35 — Formato de aprendizaje preferido**
- Tipo: *Casillas (hasta 2)*
- Opciones:
  - Sesiones presenciales de 2h
  - Videos / tutoriales asincrónicos
  - Documentación escrita (guías, playbooks)
  - Aprender haciendo (problema real + acompañamiento)
  - Pair-working con alguien más avanzado

---

### **SECCIÓN 7: Cierre**

**Pregunta 36 — ¿Algo más que quieras compartir?**
- Tipo: *Párrafo*
- Obligatoria: ❌

**Mensaje de confirmación post-envío:**
> ✅ Gracias por completar el cuestionario. Tus respuestas nos ayudan a diseñar el piloto AI Fluency UJMD ajustado a tu realidad. Douglas revisará tu perfil individual y te contactará para coordinar los siguientes pasos.

---

## ⚙️ Configuraciones recomendadas

### Visibilidad y privacidad
| Opción | Configuración |
|---|---|
| Recopilar direcciones de correo | ✅ Verificada (solo @ujmd.edu.sv) |
| Limitar a 1 respuesta | ✅ |
| Modo anónimo | ❌ (necesitamos identificar para hacer perfiles individuales) |
| Editar después de enviar | ✅ (permitir cambios por si se equivocan) |
| Ver respuestas | ❌ (solo Douglas tiene acceso a la hoja consolidada) |

### Apariencia
- Color del encabezado: usar color institucional UJMD
- Imagen: logo de Dirección de Servicios Informáticos (si existe)
- Tema oscuro: mantener claro (legible)

### Integraciones
- Conectar hoja de cálculo de Google (se crea automáticamente al activar)
- Hoja destino: **"Respuestas_AI_Literacy_Baseline"** (en Drive compartido con Douglas)

---

## 🧮 Clave de calificación — Nivel estimado

Tras recibir las respuestas, el consolidador (ver `consolidador_appsscript.gs`) calculará automáticamente:

| Sumatoria Sección 4 | Nivel dominante | Zona |
|---|---|---|
| 10–20 | L0–L2 | Pasajero |
| 21–35 | L3–L5 | Conductor |
| 36–50 | L6–L9 | Piloto Automático |

Esto alimenta directamente:
- Perfil individual de cada participante
- Selección final de Champions (cruzado con apertura cultural y disponibilidad a enseñar)
- Métricas de progreso pre/post-piloto

---

## 🚀 Escalabilidad

Este mismo formulario sirve para:

| Fase | Audiencia | Adaptación |
|---|---|---|
| **Fase 0/1** | 4 Champions | Formulario tal cual |
| **Fase 2** | 10–25 miembros de Dirección | Mismo formulario, análisis por área |
| **Fase 3 + expansión UJMD** | Otras áreas (Académica, Administrativa, Rectoría) | Mismo formulario, agregar campo "Área/Unidad" con más opciones |
| **Roles adicionales** | Docentes, coordinadores, administrativos | Agregar sección "Rol institucional específico" |

El diseño es **agnóstico al rol** y la sección de área permite analizar por segmento sin modificar el instrumento.

---

## 📦 Cómo montar este formulario (5 minutos)

1. **Crear formulario** → pegar título + descripción
2. **Crear 7 secciones** con los nombres: "Datos", "Herramientas", "Casos de uso", "Autodiagnóstico L0-L9", "Bloqueos", "Expectativas", "Cierre"
3. **Agregar las 36 preguntas** con los tipos indicados arriba
4. **Conectar hoja de cálculo** de respuestas
5. **Configurar restricciones** de dominio `@ujmd.edu.sv`
6. **Probar el formulario** enviándolo a ti mismo primero
7. **Publicar** y compartir enlace

Si prefieres automatización completa (crear el formulario por código via Google Apps Script), revisa el archivo `montaje_automatico_appsscript.gs` en esta misma carpeta.

---

## ✅ Checklist de lanzamiento

- [ ] Formulario creado y probado
- [ ] Hoja de respuestas conectada
- [ ] Restricción de dominio `@ujmd.edu.sv` aplicada
- [ ] Enlace copiado para distribución
- [ ] Consolidador Apps Script instalado (ver `consolidador_appsscript.gs`)
- [ ] Correo de invitación enviado a los 4 Champions
- [ ] Fecha límite de aplicación definida (recomendado: 5 días hábiles)

---

## 🔗 Archivos relacionados en este proyecto

- `Cuestionario_Baseline_AI_Literacy.md` — Versión en markdown (formato entrevista presencial)
- `consolidador_appsscript.gs` — Script para calcular nivel estimado automáticamente
- `montaje_automatico_appsscript.gs` — Script opcional para crear el formulario por código
- `Acta_Seleccion_Champions_AI_Fluency.md` — Champions confirmados
- `SOUL_plantillas/*.md` — Perfiles personalizados por área

---

*Instrumento diseñado por @untaldouglas — Dirección de Servicios Informáticos UJMD.*
