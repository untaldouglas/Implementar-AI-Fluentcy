# Preguntas Frecuentes — Piloto Champions

> Dudas reales que surgieron durante el piloto y cómo se resolvieron. Ver convención de
> actualización en [_dashboard.md](_dashboard.md).
>
> **Consolidado el 17/07/2026 por Claude Code** (decisión de Douglas). Mirror en
> [Drive: Preguntas_Frecuentes](https://docs.google.com/document/d/19bxuLW46jig3vBbsuFA-VViE3mZRlZANlRFD63cHQ8w/edit) (fuente de verdad).

| Pregunta | Respuesta | Contexto/caso que la originó | Agregado por | Fecha |
|---|---|---|---|---|
| ¿Cómo protejo la seguridad de la información cuando delego una tarea técnica a Hermes? | Se aplican protocolos de anonimización: eliminar IPs, credenciales y datos de producción de los prompts y scripts antes de compartirlos con el agente. Ver "Delegación segura" y "Principio de Menor Privilegio" en el Glosario. | Aporte original de Patrick, adaptado al criterio "caso real con Hermes". | Patrick | 17/07/2026 |
| ¿Dónde debe vivir la evidencia de los compromisos (C17-C20), y por qué no en mi carpeta personal? | Toda evidencia colectiva va en la carpeta única de Drive (AIFluent Junio 2026): `02_Conocimiento_Colectivo` para C17, `01_Evidencia_Champions/<compromiso>/<Nombre>` para el resto — nunca en carpetas personales de S2. | El 17/07 se descubrió evidencia real de Patrick e Irvin "enterrada" en carpetas personales, invisible para la verificación porque no seguía la estructura acordada. | Claude Code (consolidado) | 17/07/2026 |
| ¿Qué hago si mi prompt no puede evaluar el riesgo de incluir datos como IPs o nombres de equipo? | Documentarlo explícitamente como limitación conocida en vez de omitirlo. Es preferible declarar el punto de mejora que asumir que no hay riesgo. | Irvin lo declaró así en su C19 de Instalación de Software Remoto. | Irvin | 17/07/2026 |
| ¿Es obligatorio nombrar una técnica de prompting (Chain of Thought, Few-Shot, Iterative Refinement) para que un caso cuente como C19? | No es obligatorio per se, pero si se aplicó una técnica reconocible hay que nombrarla explícitamente. Cuando no se identifica una técnica concreta, se declara honestamente en vez de inventar un nombre. | Contraste entre el caso de Mario (técnicas nombradas) y el de Irvin (sin técnica identificada). | Claude Code (consolidado) | 17/07/2026 |
