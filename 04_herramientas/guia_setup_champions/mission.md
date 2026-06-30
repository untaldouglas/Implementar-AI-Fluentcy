# 🎯 Misión: Setup de Hermes Agent para Champions

## Objetivo final
Cada Champion tendrá Hermes Agent instalado, configurado y verificado en su máquina local antes de la Sesión 0 (martes 01/07/2026 · 9:00 AM).

## Contexto
- **Proyecto:** AI Fluency UJMD — Piloto Mes 1
- **Herramienta central:** Hermes Agent (NousResearch) — orquestador universal
- **Backends:** Claude API (principal) + Ollama local (fallback)
- **Repositorio:** `untaldouglas/mihermes`
- **Plataformas de uso:** CLI local + Telegram (gateway)

## Perfil del learner
- 3 Champions (Patrick, Mario, Irvin) con perfiles técnicos distintos
- Nivel baseline: L2 (familiaridad con terminal básica)
- Meta: L5 al final del piloto
- Tiempo disponible antes de Sesión 0: 2 días (29-30 junio)

## Criterios de éxito
1. `hermes doctor` pasa sin errores críticos
2. El agente responde a una consulta de prueba (`hermes chat -q "..."`)
3. El gateway de Telegram está conectado (`hermes gateway status`)
4. Al menos 1 skill cargado y funcional

## Estructura de aprendizaje
```
guia_setup_champions/
├── mission.md              ← Este archivo
├── lessons/
│   ├── 01_instalacion.md       ← Lección 1: Instalar el core
│   ├── 02_configuracion.md     ← Lección 2: Conectar modelo + provider
│   └── 03_verificacion.md     ← Lección 3: Probar y verificar
├── glossary/
│   └── terminos_hermes.md      ← Glosario de términos clave
├── cheat_sheets/
│   └── comandos_esenciales.md  ← Referencia rápida de comandos
└── learning_record/
    └── progreso_champion.md   ← Template de seguimiento por Champion
```

## Rol del Director (Douglas)
- Facilita la instalación remota vía Teams/Meet si hay bloqueos
- Provee las credenciales API necesarias
- Verifica el estado de cada Champion antes de Sesión 0
