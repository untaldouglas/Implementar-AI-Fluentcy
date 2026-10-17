# OPP-020 — Small Model First

- **Aprobación:** 2026-10-17
- **Estado:** EXPERIMENT / preparación
- **Prioridad:** alta
- **Iniciativa:** AI Fluency / Human + AI Living Lab
- **Responsable:** por asignar
- **Alcance:** laboratorio, sin acceso a producción

## Pregunta e hipótesis
¿Puede un modelo local compacto clasificar solicitudes sintéticas de Service Desk con calidad comparable a un modelo cloud de referencia, utilizando menos recursos y manteniendo control institucional de datos?

Hipótesis: un modelo compacto alcanzará al menos 95 % de la calidad del modelo de referencia para este conjunto limitado de tareas, con menor costo variable y recursos aceptables.

## Diseño
Comparar (A) modelo local pequeño de referencia, (B) PrismML Ternary Bonsai 2 4B y (C) modelo cloud de referencia. Versionar identificadores exactos, cuantización, runtime, parámetros y hardware. Verificar compatibilidad de Bonsai 2 con runtime soportado antes de la prueba; no asumir soporte en Ollama estándar.

## Golden Cases
Preparar 20 solicitudes **sintéticas** con campos: case_id, description, expected_category, expected_priority, expected_route, ambiguity_flag, expected_abstention. Distribuir categorías (wifi, proyección, cuentas, software, infraestructura) y prioridades. Etiquetas de referencia definidas y revisadas antes de ejecutar los modelos. No incluir datos personales ni incidentes reales.

## Protocolo
1. Congelar dataset y rúbrica; separar etiquetas esperadas del prompt.
2. Definir esquema JSON de salida: category, priority, route, abstain, rationale_short.
3. Ejecutar los mismos 20 casos por modelo con condiciones comparables; repetir tres veces si es viable.
4. Registrar latencia, memoria máxima, tokens, costo estimado, validez JSON, coincidencia por campo, abstenciones, falsos positivos/negativos y corrección humana.
5. Evaluar calidad con métrica compuesta definida **antes** de observar resultados y reportar además cada componente por separado.
6. Revisar discrepancias con experto del dominio; documentar errores y limitaciones.

## Criterios de decisión
- Calidad del candidato >=95 % de la calidad del modelo cloud en la métrica predefinida; no sustituye umbrales mínimos absolutos de seguridad y exactitud.
- Validez JSON >= 95 % y ningún error crítico sin escalamiento en los casos definidos como críticos.
- Menor costo variable o ventaja tangible de privacidad/portabilidad; documentar RAM y latencia.
- Si el tamaño de muestra impide concluir, ampliar Golden Cases antes de adoptar. **No habilitar decisiones automáticas en producción**.

## Artefactos esperados
- cases.jsonl, schema.json, rubric.md
- config.example.yaml (sin credenciales), requirements.txt o pyproject.toml
- runner.py, evaluate.py, tests/
- results/*.csv (sin datos sensibles), REPORT.md, DECISION.md

## Siguiente acción
Confirmar hardware disponible y modelo cloud de referencia; crear 20 Golden Cases sintéticos y congelar rúbrica. Tiempo estimado de primera prueba: 4–6 horas, sujeto a compatibilidad e instalación.

## Fuentes
- https://prismml.com/news/bonsai-2-family
- https://huggingface.co/prism-ml/Ternary-Bonsai-2-4B-gguf
- https://github.com/PrismML-Eng/Bonsai-demo
