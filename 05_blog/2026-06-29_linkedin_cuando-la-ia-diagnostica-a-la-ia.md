# LinkedIn Post — 29 junio 2026
# Título: Cuando la IA diagnostica a la IA

---

El diagnóstico de cuánto sabe alguien sobre IA no debería ser un Excel que llenas a mano.

Hoy lo automatizamos.

---

Mañana arranca el piloto del programa AI Fluency en la Dirección de Servicios Informáticos de la UJMD. Tres Champions — uno de Infraestructura, uno de Desarrollo, uno de Soporte — van a llenar un cuestionario de diagnóstico con 37 preguntas que mapean su nivel de autonomía con IA en una escala L0-L9.

El problema: alguien tiene que interpretar esas respuestas, calcular el nivel de cada persona y decidir qué aprende primero. A mano, eso toma tiempo. Cuando el programa escale a 25 personas en agosto, toma demasiado tiempo.

Así que hoy construimos el script que lo hace automático.

---

**Lo que hace el script:**

Lee las respuestas del Google Form directamente en Google Sheets. Calcula el nivel L0-L9 de cada participante. Detecta su zona (Pasajero / Conductor / Piloto Automático). Asigna su licencia de conducción AI. Y genera su itinerario personalizado de aprendizaje para las primeras 4 semanas.

El itinerario no es genérico. Se adapta según tres variables: nivel de entrada, área del trabajo y bloqueo dominante. Alguien en L2 de Soporte con bloqueo de confianza recibe una ruta completamente diferente a alguien en L4 de Infraestructura con bloqueo de tiempo.

---

**Pero lo más interesante no fue el script.**

Fue lo que hicimos después: convertir ese script en un skill de Claude.

Un skill es un proceso automatizable empacado. La próxima vez que el programa arranque con una nueva cohorte, o que el Form cambie de estructura, o que agreguemos un área nueva — no hay que empezar de cero. Solo escribir:

*"Agrega el área de Biblioteca al script. Usan Canva y Google Sites. Su caso de uso ancla: organizar recursos digitales con IA."*

Y el script se regenera con los cambios en segundos.

---

**Lo que aprendí hoy:**

Hay una diferencia entre hacer algo una vez y hacer algo repetible. El script resuelve el diagnóstico de esta cohorte. El skill resuelve el diagnóstico de todas las cohortes que vienen.

El costo de crear el skill fue casi el mismo que el de crear el script. El retorno es exponencialmente mayor.

---

Con esto cerramos la Fase 0 al 100%. Seis compromisos, seis completados.

Mañana — 1 de julio, 9:00 AM — arranca el programa real.

---

Si estás implementando IA en tu organización y quieres ver cómo está estructurado el framework MCA (escala L0-L9, sistema de licencias, estrategia Champion → Equipo), el sitio del programa está en:

🔗 https://untaldouglas.github.io/Implementar-AI-Fluentcy/

---

#AIFluency #InteligenciaArtificial #EducacionSuperior #UJMD #TransformacionDigital #LiderazgoTI #GoogleAppsScript #AdopcionIA
