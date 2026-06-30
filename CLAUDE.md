# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project** — there is no build, lint, or test suite to run. It is the documentation and operating repository for **AI Fluency / Modelo de Conducción AI (MCA)**, an internal program at UJMD's Dirección de Servicios Informáticos that trains staff ("Champions") to use AI tools progressively, from basic chat (L0) to multi-agent orchestration (L9), via a vehicular-license metaphor (Permiso de Aprendizaje → Instructor de Conducción).

Content is almost entirely Markdown and standalone HTML artifacts (decks, infographics, dashboards). The Makefile drives status/reporting commands, not compilation.

## Repository structure

Numbered top-level folders represent the program's conceptual layers, in read order:

- `00_marco/` — conceptual framework (read first): `Manual_Implementacion_Estrategica.md` (the MCA model, L0–L9), `Licencia_Conduccion_AI.md` (certification system), `Alineacion_Estrategica.md`, `Protocolo_Investigacion.md`.
- `01_piloto/` — Capa 0 pilot (the 3-4 Champions): roadmap, champion selection acta, baseline questionnaire, `SOUL_plantillas/` (per-area agent config: Desarrollo/Soporte/Infraestructura), `google_form/` (Apps Script automation for the diagnostic survey).
- `02_playbook/` — replicable master playbook (`.docx`).
- `03_comunicacion/` — stakeholder comms: emails, decks, one-pagers, infographics, brand assets.
- `04_herramientas/` — operational dashboards (`Dashboard_Jornada.html`, `dashboards/*.md` daily logs), onboarding portal.
- `05_blog/` — public-facing blog posts about the program.
- `docs/` — **GitHub Pages publish folder**. Only a curated subset of `03_comunicacion/*.html` artifacts is copied here (infographic, onboarding, deck, research brief) — it is not a mirror of the whole repo. `docs/.gitignore` excludes the email/comms HTML that shouldn't be public.
- `ESTADO_PROYECTO.md` — **the live project state file**. Read it before answering any question about project status, timelines, or commitments; it is more current than git history or any other doc. It's updated at the end of work sessions with a dated log entry (see existing entries for the expected format: completed items, pending items, next action).

## Known issue: Makefile paths are stale

The Makefile's `MANUAL`, `ALINEACION`, `ROADMAP`, `CUESTIONARIO`, `ACTA` variables (top of file) point to root-level filenames (e.g. `Roadmap_AI_Fluency_UJMD.md`). The actual files now live inside `00_marco/` and `01_piloto/` after the repo was reorganized into numbered folders. As a result, `make check`, `make validate`, `make docs`, and `make create-form` currently report files as missing even though they exist — this is a path bug in the Makefile, not a real repository problem. Don't trust those targets' output without checking actual file locations; fix the path variables if asked to repair tooling.

Working/useful Makefile targets: `make status` (git + repo stats), `make stats`, `make champions-list`, `make baseline-summary`, `make check-security` (greps for exposed PII/secrets), `make list-ignored`, `make backup`, `make clean`, `make open-onboarding` (`open`/`xdg-open` on `onboarding.html` — note: target path is also stale, real file is `04_herramientas/onboarding.html`).

## Sensitive data handling

`.gitignore` is extensive and intentional — it protects real pilot-participant data, emails, Hermes Agent session/credential files, and screenshots from ever being committed. Specifically never commit into tracked paths: filled-in baseline questionnaire responses (`respuestas_piloto/`, `*respuestas*`, `*baseline*.csv`), `notas_personales/`, `screenshots/`, anything under `.hermes/`, or `.env`/`credentials.json`/keys. The CSV *template* (`Plantilla_AI_Literacy_Baseline.csv`) is fine to commit; filled-in response data is not. When in doubt, run `make check-security` before committing new files in `01_piloto/` or `04_herramientas/dashboards/`.

## Domain vocabulary (needed to read the docs coherently)

- **MCA (Modelo de Conducción AI)**: the program's core framework, levels L0 (Taxi/basic chat) through L9 (Flota Logística/multi-agent swarm), grouped into 5 license tiers defined in `00_marco/Licencia_Conduccion_AI.md`.
- **Champions**: the pilot's first cohort (one person per area: Desarrollo, Soporte, Infraestructura, plus the Director), selected via `01_piloto/Acta_Seleccion_Champions_AI_Fluency.md`.
- **SOUL.md**: per-area agent configuration files (`01_piloto/SOUL_plantillas/`) defining role-detection triggers, data-handling rules (e.g. dev work must use synthetic student data, never production records), and expected Skills per area.
- **Hermes Agent** (NousResearch, open source) is the orchestrator tool named throughout the framework docs as the chosen interface; `00_marco/Manual_Implementacion_Estrategica.md` includes an explicit mapping table translating the original manual's Claude Desktop/Cowork/Code/Agent-SDK terminology to Hermes equivalents, since the manual text is kept verbatim for conceptual fidelity but UJMD's actual tooling is Hermes-based.
- **Capas (scaling layers)**: Capa 0 Piloto (Champions, month 1) → Capa 1 Dirección IT → Capa 2 Universidad → Capa 3 Comunidad (docentes/estudiantes).

## Conventions when editing this repo

- Spanish is the working language for all content (docs, commits in this repo, file names).
- Dates in `ESTADO_PROYECTO.md` and dashboard files are session timestamps — preserve the existing log format (don't rewrite history entries) and append new entries rather than editing old ones.
- HTML artifacts in `03_comunicacion/` and `docs/` are self-contained single files (inline CSS, no build step) — edit them directly; there is no templating system.
