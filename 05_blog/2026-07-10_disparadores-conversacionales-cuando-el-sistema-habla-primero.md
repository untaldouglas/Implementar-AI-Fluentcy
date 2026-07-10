# Blog Post — 10 julio 2026
# Título: Cuando tu memoria te traiciona, el sistema tiene que hablar primero

---

Tengo un problema. Se llama Douglas, y se le olvidan los nombres.

---

Esta semana me pasó algo que vale la pena contar, porque ilustra un patrón que todo Director de TI va a enfrentar cuando empiece a delegar en IA: **cuando el sistema hace demasiado, el humano empieza a olvidar**.

## La necesidad

Llevo varias semanas trabajando con un agente de IA (Hermes, sobre el orquestador de Nous Research) que me ayuda a gestionar la DSI de la UJMD. En ese tiempo hemos construido juntos un inventario de **ocho skills institucionales** — procedimientos automatizados para cosas como:

- Generar el status consolidado de un proyecto institucional
- Auditar la calidad de datos de Issues y Tasks en ERPNext
- Producir el informe diario de los coordinadores (Luis, Steph, Jorge)
- Armar el portafolio de trabajo en marcha de un técnico
- Actualizar el seguimiento de los Champions de AI Fluency
- Estandarizar la primera respuesta de mesa de servicio
- Evaluar gobernanza con marcos ITIL/COBIT/LEAN

Cada uno tiene un nombre, una carpeta, una sintaxis, un caso de uso. Y ahí está el problema.

Mi memoria no da para más. No es cuestión de inteligencia — es que **el medicamento que tomo me dificulta retener listas largas de nombres**, y eso me obligaba a hacer una de dos cosas: o parar la conversación para abrir la documentación a ver cuál era el nombre exacto del skill, o pedirle al agente "el de las auditorías, ¿cómo se llamaba?" y esperar a que adivinara.

Ambas opciones rompen el flujo de trabajo. Y romper el flujo de trabajo, en una Dirección que atiende 5000+ estudiantes y 18 equipos, es caro.

## Lo que decidimos

Le planteé el problema al agente. No le pedí un skill nuevo — le pedí **un sistema que me obligara a mí a no tener que recordar**.

Me devolvió tres alternativas. Yo elegí la que más se alineaba con cómo trabajo: una **combinación de dos cosas**.

1. **Una tabla de disparadores en `AGENTS.md`** — el archivo de instrucciones que el agente lee cada vez que entra a mi workspace. La tabla mapea frases en español natural a skills. Si yo digo "status inscripción", el agente sabe que tiene que disparar el skill de status. Si digo "qué tiene Steph en cola", sabe que es el portafolio.

2. **Una Regla #0** — el agente, por defecto, me pregunta antes de ejecutar. Literal: *"Voy a usar `audit/erpnext-audit` para auditar los Issues del día, ¿confirmás?"*. Solo dos excepciones documentadas donde la intención es tan clara que ejecuta directo.

Es la diferencia entre un asistente que necesita que yo sepa los nombres, y un asistente que **habla primero y me recuerda lo que existe**.

## El procedimiento (lo que pasó hoy)

Esta mañana, en menos de 30 minutos, validamos el sistema con cinco frases reales:

| Frase que yo dije | Qué pasó |
|---|---|
| "status proyecto inscripción" | Disparó el skill correcto, me generó un MD de 12 KB y un resumen ejecutivo con tres acciones priorizadas. 🟢 |
| "que debo hacer en proyecto AIFluent" | Leyó el `ESTADO_PROYECTO.md`, encontró que hoy 14:00 tengo reunión con los Champions, y me trajo la agenda ya preparada. 🟢 |
| "resumen diario" | Cruzó Gmail, Calendar y ERPNext, y me entregó un briefing con lo importante de la jornada. 🟢 |
| "resumen de issues creados este día" | Detectó un Issue de spam que llegó al sistema, me lo señaló y me dio la acción recomendada. 🟡 |
| "resumen de acciones por trabajar de acuerdo a github" | Aquí el sistema falló parcialmente — yo asumí que los cuatro proyectos eran repos GitHub, pero solo dos lo son. El agente lo aclaró y no inventó datos. 🟠 |

Tres resultados verdes, uno amarillo, uno naranja. **Cinco de cinco respuestas útiles. Cero alucinaciones.**

Lo más importante: en ningún momento tuve que recordar un nombre técnico. Dije lo que necesitaba en español, como se lo diría a un asistente humano, y el sistema hizo su trabajo.

## El resultado que se deberá validar

Un sistema así no se valida en una mañana. Se valida en **dos semanas de uso real**. Estos son los criterios que voy a usar para saber si la inversión valió la pena:

1. **Cobertura**: ¿llego a la tabla de disparadores sin tener que improvisar más de una vez por semana? Si improviso, lo documento para futura referencia.
2. **Cero alucinaciones**: ¿el agente ejecuta el skill correcto sin que yo tenga que corregirlo? Si se equivoca, ajusto la tabla, no le echo la culpa.
3. **Gates respetados**: ¿el agente me pregunta antes de ejecutar cuando hay ambigüedad? El día que ejecute algo destructivo sin gate, el sistema habrá fallado.
4. **Tiempo recuperado**: ¿estoy dedicando menos tiempo a "qué nombre tenía" y más a "qué decisión tomo"? Esto lo voy a medir intuitivamente — si en dos semanas sigo frustrado, repensamos.

## Por qué importa este cambio (más allá de mi memoria)

Lo que descubrí esta semana aplica a cualquier líder que esté adoptando IA en su equipo:

- **Los skills son poderosos, pero invisibles.** Si tu equipo tiene que recordar 12 nombres de procedimientos automatizados, no los va a usar. La fricción mata la adopción.
- **El gate de aprobación no es desconfianza, es arquitectura.** En un sistema donde la IA ejecuta, el humano debe poder vetar antes. Tu workflow de "ok L1, ok L2, ok L3" no es burocracia — es el control que evita errores caros.
- **Lo que se documenta, se puede mejorar.** Cada vez que improviso un disparador nuevo, lo escribo en `AGENTS.md` con sus restricciones. La próxima vez que lo necesite, ya está resuelto.
- **La memoria del agente y la tuya son cosas distintas.** Que el agente recuerde el skill no significa que vos lo recordés. Diseñá para tu peor día, no para tu mejor día.

El sistema que armé hoy no es sofisticado. Es una tabla Markdown y una regla de cinco líneas. Pero es **infraestructura que me permite delegar sin perder control**, que es exactamente lo que un Director de Informática necesita cuando el volumen de trabajo excede la memoria humana.

---

Si estás implementando IA en tu equipo y querés ver cómo está estructurado el programa AI Fluency de la UJMD (escala L0-L9, sistema de licencias, estrategia Champion → Equipo), el sitio está en:

🔗 https://untaldouglas.github.io/Implementar-AI-Fluentcy/

Y si te pasa lo mismo que a mí — que se te olvidan los nombres de tus propias herramientas — te dejo la pregunta que me cambió la conversación: **¿qué solución propones para que te sea fácil recordar, gestionar y utilizar tu inventario de capacidades?**

La respuesta no es más memoria. Es un sistema que hable primero.

---

#AIFluency #InteligenciaArtificial #LiderazgoTI #AdopcionIA #UJMD #TransformacionDigital #DireccionTI #ProductividadConIA #GobernanzaTI
