# Makefile — Proyecto AI Fluentcy UJMD
# ============================================================
# Autor: Douglas Galindo - Dirección de Servicios Informáticos UJMD
# Herramienta oficial: Hermes Agent (NousResearch)
# ============================================================

.PHONY: help status check validate test backup clean docs stats \
        check-security list-ignored init-piloto \
        champions-list baseline-summary reset

# Variables
TIMESTAMP := $(shell date +%Y%m%d_%H%M%S)
DATE      := $(shell date +%Y-%m-%d)
BACKUP_DIR := respaldos_proyecto

# Archivos del proyecto (nombres exactos del filesystem)
MANUAL       := Manual de Implementación Estratégica_ Dominando la IA mediante el Modelo de Autonomía Vehicular.md
ALINEACION   := Alineacion_Estrategica_Manual_Roadmap_Perfil_Director.md
ROADMAP      := Roadmap_AI_Fluency_UJMD.md
CUESTIONARIO := Cuestionario_Baseline_AI_Literacy.md
ACTA         := Acta_Seleccion_Champions_AI_Fluency.md
README       := README.md

# Colores para output
GREEN  := \033[0;32m
YELLOW := \033[0;33m
BLUE   := \033[0;34m
NC     := \033[0m

.DEFAULT_GOAL := help

# ============================================================
# AYUDA
# ============================================================
help:
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║       AI Fluentcy UJMD — Gestión del repositorio           ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)ESTADO Y DIAGNÓSTICO:$(NC)"
	@echo "  $(YELLOW)make status$(NC)             Estado actual del proyecto"
	@echo "  $(YELLOW)make check$(NC)              Verificar estructura completa"
	@echo "  $(YELLOW)make validate$(NC)           Validar integridad de archivos"
	@echo "  $(YELLOW)make test$(NC)               Ejecutar todas las verificaciones"
	@echo "  $(YELLOW)make stats$(NC)              Estadísticas del repositorio"
	@echo ""
	@echo "$(GREEN)GESTIÓN DEL PILOTO AI FLUENCY:$(NC)"
	@echo "  $(YELLOW)make champions-list$(NC)     Listar Champions seleccionados"
	@echo "  $(YELLOW)make baseline-summary$(NC)   Resumen del instrumento baseline"
	@echo "  $(YELLOW)make init-piloto$(NC)        Crear carpetas de datos privados del piloto"
	@echo ""
	@echo "$(GREEN)SEGURIDAD Y LIMPIEZA:$(NC)"
	@echo "  $(YELLOW)make check-security$(NC)     Verificar que no hay datos sensibles"
	@echo "  $(YELLOW)make list-ignored$(NC)       Mostrar archivos ignorados por .gitignore"
	@echo "  $(YELLOW)make backup$(NC)             Crear respaldo del repositorio"
	@echo "  $(YELLOW)make clean$(NC)              Limpiar archivos temporales"
	@echo ""
	@echo "$(GREEN)DOCUMENTACIÓN:$(NC)"
	@echo "  $(YELLOW)make docs$(NC)               Generar documentación consolidada en docs/"
	@echo "  $(YELLOW)make reset$(NC)              Resetear dashboards/diarios (con confirmación)"
	@echo ""

# ============================================================
# ESTADO Y DIAGNÓSTICO
# ============================================================

status:
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║            ESTADO ACTUAL DEL PROYECTO AI FLUENCY           ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)Fecha:$(NC) $(DATE)"
	@echo ""
	@echo "$(BLUE)Estado del repositorio git:$(NC)"
	@git rev-parse --is-inside-work-tree > /dev/null 2>&1 && { \
		echo "  ✓ Repo git operativo"; \
		echo "  - Branch: $$(git branch --show-current)"; \
		echo "  - Último commit: $$(git log -1 --format='%h - %s (%ar)' 2>/dev/null || echo 'N/A')"; \
		echo "  - Remote: $$(git remote get-url origin 2>/dev/null || echo 'no configurado')"; \
		CHANGED=$$(git status --porcelain 2>/dev/null | wc -l | tr -d ' '); \
		if [ "$$CHANGED" != "0" ]; then \
			echo "  $(YELLOW)⚠ $$CHANGED archivo(s) con cambios sin commit$(NC)"; \
		else \
			echo "  $(GREEN)✓ Repositorio limpio$(NC)"; \
		fi; \
	} || echo "  ✗ No es un repositorio git"
	@echo ""
	@echo "$(BLUE)Archivos versionados (excluyendo .git):$(NC)"
	@find . -type f -not -path './.git/*' | wc -l | xargs -I{} echo "  {} archivos totales"
	@echo "  $$(find . -name '*.md' -type f | wc -l | tr -d ' ') markdown"
	@echo "  $$(find . -name '*.csv' -type f | wc -l | tr -d ' ') CSV"
	@echo "  $$(find . -name '*.gs' -type f | wc -l | tr -d ' ') Google Apps Script"
	@echo ""
	@echo "$(BLUE)Dashboards diarios:$(NC)"
	@ls dashboards/*.md 2>/dev/null | wc -l | xargs -I{} echo "  {} dashboards generados"
	@echo ""

check:
	@echo "$(GREEN)Verificando estructura del repositorio...$(NC)"
	@echo ""
	@ERRORS=0; \
	echo "$(BLUE)Archivos principales:$(NC)"; \
	if [ -f $(README) ]; then echo "  ✓ README.md"; else echo "  ✗ README.md FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -f .gitignore ]; then echo "  ✓ .gitignore"; else echo "  ✗ .gitignore FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -f Makefile ]; then echo "  ✓ Makefile"; else echo "  ✗ Makefile FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	echo ""; \
	echo "$(BLUE)Documentos del marco conceptual:$(NC)"; \
	if [ -f "$(MANUAL)" ]; then echo "  ✓ Manual de Implementación Estratégica"; else echo "  ✗ Manual de Implementación FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -f $(ALINEACION) ]; then echo "  ✓ Alineación Estratégica"; else echo "  ✗ Alineación Estratégica FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -f $(ROADMAP) ]; then echo "  ✓ Roadmap AI Fluency UJMD"; else echo "  ✗ Roadmap FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	echo ""; \
	echo "$(BLUE)Instrumentos de evaluación y pilotos:$(NC)"; \
	if [ -f $(CUESTIONARIO) ]; then echo "  ✓ Cuestionario Baseline AI Literacy"; else echo "  ✗ Cuestionario Baseline FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -f $(ACTA) ]; then echo "  ✓ Acta de Selección de Champions"; else echo "  ✗ Acta de Champions FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	if [ -d google_form ]; then echo "  ✓ google_form/ (implementación digital del cuestionario)"; else echo "  ✗ google_form/ FALTANTE"; ERRORS=$$((ERRORS+1)); fi; \
	echo ""; \
	echo "$(BLUE)Plantillas de configuración:$(NC)"; \
	if [ -d SOUL_plantillas ]; then \
		echo "  ✓ SOUL_plantillas/ (perfiles de agente)"; \
		COUNT=$$(ls SOUL_plantillas/*.md 2>/dev/null | wc -l | tr -d ' '); \
		echo "    $$COUNT plantillas SOUL.md"; \
	else \
		echo "  ✗ SOUL_plantillas/ FALTANTE"; ERRORS=$$((ERRORS+1)); \
	fi; \
	echo ""; \
	echo "$(BLUE)Seguimiento del proyecto:$(NC)"; \
	if [ -d dashboards ]; then \
		echo "  ✓ dashboards/ (cierres y planes diarios)"; \
		COUNT=$$(ls dashboards/*.md 2>/dev/null | wc -l | tr -d ' '); \
		echo "    $$COUNT dashboards"; \
	else \
		echo "  ✗ dashboards/ FALTANTE"; ERRORS=$$((ERRORS+1)); \
	fi; \
	echo ""; \
	if [ $$ERRORS -eq 0 ]; then \
		echo "$(GREEN)✓ Estructura completa y verificada$(NC)"; \
	else \
		echo "$(YELLOW)⚠ $$ERRORS elemento(s) faltante(s)$(NC)"; \
	fi

validate:
	@echo "$(GREEN)Validando integridad de archivos clave...$(NC)"
	@echo ""
	@ERRORS=0; \
	for file in "$(MANUAL)" "$(ALINEACION)" "$(ROADMAP)" "$(CUESTIONARIO)" "$(ACTA)"; do \
		if [ -f "$$file" ]; then \
			LINES=$$(wc -l < "$$file" | tr -d ' '); \
			if [ "$$LINES" -lt 10 ]; then \
				echo "  ✗ $$file tiene muy pocas líneas ($$LINES)"; \
				ERRORS=$$((ERRORS + 1)); \
			else \
				echo "  ✓ $$file ($$LINES líneas)"; \
			fi; \
		else \
			echo "  ✗ $$file NO EXISTE"; \
			ERRORS=$$((ERRORS + 1)); \
		fi; \
	done; \
	echo ""; \
	echo "$(BLUE)Verificando CSV plantilla del formulario:$(NC)"; \
	if [ -f google_form/Plantilla_AI_Literacy_Baseline.csv ]; then \
		COLS=$$(head -1 google_form/Plantilla_AI_Literacy_Baseline.csv | awk -F',' '{print NF}'); \
		echo "  ✓ Plantilla_AI_Literacy_Baseline.csv ($$COLS columnas)"; \
	else \
		echo "  ✗ Plantilla CSV FALTANTE"; \
		ERRORS=$$((ERRORS+1)); \
	fi; \
	echo ""; \
	if [ "$$ERRORS" -eq 0 ]; then \
		echo "$(GREEN)✓ Todos los archivos están completos$(NC)"; \
	else \
		echo "$(YELLOW)⚠ $$ERRORS problema(s) detectado(s)$(NC)"; \
	fi

test:
	@echo "$(GREEN)Ejecutando suite de verificación...$(NC)"
	@echo ""
	@echo "$(BLUE)Test 1: Verificar estructura básica$(NC)"
	@make check > /dev/null 2>&1 && echo "  $(GREEN)✓ Estructura OK$(NC)" || echo "  $(YELLOW)✗ Estructura incompleta$(NC)"
	@echo ""
	@echo "$(BLUE)Test 2: Validar integridad de archivos$(NC)"
	@make validate > /dev/null 2>&1 && echo "  $(GREEN)✓ Archivos válidos$(NC)" || echo "  $(YELLOW)✗ Archivo(s) problemático(s)$(NC)"
	@echo ""
	@echo "$(BLUE)Test 3: Verificar .gitignore de seguridad$(NC)"
	@if [ -f .gitignore ]; then \
		echo "  $(GREEN)✓ .gitignore existe$(NC)"; \
		grep -qE '^\*\*.*respuestas' .gitignore 2>/dev/null && \
			echo "  $(GREEN)✓ Protege archivos de respuestas$(NC)" || \
			echo "  $(YELLOW)⚠ No protege archivos de respuestas$(NC)"; \
		grep -qE '^\*\*.*\.hermes' .gitignore 2>/dev/null && \
			echo "  $(GREEN)✓ Protege archivos Hermes (.hermes/)$(NC)" || \
			echo "  $(YELLOW)⚠ No protege .hermes/$(NC)"; \
		grep -qE '(\.env|credentials)' .gitignore 2>/dev/null && \
			echo "  $(GREEN)✓ Protege secretos (.env, credentials)$(NC)" || \
			echo "  $(YELLOW)⚠ No protege secretos$(NC)"; \
	else \
		echo "  $(YELLOW)✗ .gitignore faltante$(NC)"; \
	fi
	@echo ""
	@echo "$(BLUE)Test 4: Sin datos sensibles del piloto expuestos$(NC)"
	@make check-security > /dev/null 2>&1 && \
		echo "  $(GREEN)✓ Sin datos sensibles expuestos$(NC)" || \
		echo "  $(YELLOW)⚠ Revisar posibles datos sensibles$(NC)"
	@echo ""
	@echo "$(GREEN)Suite de verificación completada$(NC)"
	@echo ""

stats:
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║              ESTADÍSTICAS DEL REPOSITORIO                  ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)Conteo por tipo de archivo:$(NC)"
	@echo "  Markdown:          $$(find . -name '*.md' -type f | wc -l | tr -d ' ')"
	@echo "  CSV:               $$(find . -name '*.csv' -type f | wc -l | tr -d ' ')"
	@echo "  Google Apps Script: $$(find . -name '*.gs' -type f | wc -l | tr -d ' ')"
	@echo "  Makefile:          $$(find . -name 'Makefile' -type f | wc -l | tr -d ' ')"
	@echo "  Otros:             $$(find . -type f -not -name '*.md' -not -name '*.csv' -not -name '*.gs' -not -name 'Makefile' -not -path './.git/*' | wc -l | tr -d ' ')"
	@echo ""
	@echo "$(GREEN)Líneas totales:$(NC)"
	@echo "  Markdown:          $$(find . -name '*.md' -type f -exec cat {} + 2>/dev/null | wc -l | tr -d ' ')"
	@echo "  CSV:               $$(find . -name '*.csv' -type f -exec cat {} + 2>/dev/null | wc -l | tr -d ' ')"
	@echo "  Apps Script:       $$(find . -name '*.gs' -type f -exec cat {} + 2>/dev/null | wc -l | tr -d ' ')"
	@echo ""
	@echo "$(GREEN)Tamaño del repositorio (excluyendo .git):$(NC)"
	@du -sh . --exclude=.git 2>/dev/null | cut -f1 | xargs -I{} echo "  {}"
	@echo ""

# ============================================================
# GESTIÓN DEL PILOTO
# ============================================================

champions-list:
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║              CHAMPIONS SELECCIONADOS                       ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)Douglas Galindo$(NC) (Director + Arquitecto)"
	@echo "  - Correo:   dagalindo@ujmd.edu.sv"
	@echo "  - Rol:      Director de Servicios Informáticos"
	@echo "  - Nivel AI: L8 (Piloto Automático)"
	@echo ""
	@echo "$(GREEN)Patrick Eduardo Orellana Amaya$(NC) (Champion Infraestructura)"
	@echo "  - Correo:   peorellanaa@ujmd.edu.sv"
	@echo "  - SOUL.md:  SOUL_plantillas/SOUL_Infraestructura.md"
	@echo "  - Nivel AI: Por medir (Fase 0.2)"
	@echo ""
	@echo "$(GREEN)Mario Edgardo Valencia Campos$(NC) (Champion Desarrollo)"
	@echo "  - Correo:   mevalenciac@ujmd.edu.sv"
	@echo "  - SOUL.md:  SOUL_plantillas/SOUL_Desarrollo.md"
	@echo "  - Nivel AI: Por medir (Fase 0.2)"
	@echo ""
	@echo "$(GREEN)Irvin Josué Morales Parada$(NC) (Champion Soporte)"
	@echo "  - Correo:   ijmoralespa@ujmd.edu.sv"
	@echo "  - SOUL.md:  SOUL_plantillas/SOUL_Soporte.md"
	@echo "  - Nivel AI: Por medir (Fase 0.2)"
	@echo ""
	@echo "$(BLUE)Fuente: Acta_Seleccion_Champions_AI_Fluency.md$(NC)"
	@echo ""

baseline-summary:
	@echo ""
	@echo "$(BLUE)╔══════════════════════════════════════════════════════════════╗$(NC)"
	@echo "$(BLUE)║       RESUMEN DEL INSTRUMENTO BASELINE                     ║$(NC)"
	@echo "$(BLUE)╚══════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(GREEN)Objetivo:$(NC) Diagnosticar el nivel AI Literacy de los 4 Champions"
	@echo ""
	@echo "$(BLUE)Instrumentos disponibles:$(NC)"
	@echo "  1. $(CUESTIONARIO)"
	@echo "     Formato: Markdown (para entrevista presencial)"
	@echo ""
	@echo "  2. google_form/Plantilla_AI_Literacy_Baseline.csv"
	@echo "     Formato: CSV para Google Forms (37 columnas)"
	@echo "     Subir a Drive → conectar al formulario → respuestas caen ahí"
	@echo ""
	@echo "  3. google_form/Guia_GoogleForm_AI_Literacy.md"
	@echo "     Instrucciones completas de montaje del Form"
	@echo ""
	@echo "  4. google_form/consolidador_appscript.gs"
	@echo "     Script Apps Script que calcula nivel L0-L9 automáticamente"
	@echo "     y genera pestañas RESUMEN_* en la hoja"
	@echo ""
	@echo "$(BLUE)Dimensión de evaluación (4 ejes):$(NC)"
	@echo "  1. Herramientas de IA usadas actualmente"
	@echo "  2. Casos de uso reales aplicados"
	@echo "  3. Nivel de autonomía (L0 → L9)"
	@echo "  4. Bloqueos percibidos (tiempo, técnico, cultural, etc.)"
	@echo ""
	@echo "$(GREEN)Próximo paso:$(NC) Aplicar a los 4 Champions (Fase 0.2)"
	@echo ""

init-piloto:
	@echo "$(GREEN)Creando carpetas privadas para el piloto...$(NC)"
	@echo ""
	@mkdir -p respuestas_piloto
	@mkdir -p notas_personales
	@mkdir -p screenshots
	@touch respuestas_piloto/.gitkeep
	@touch notas_personales/.gitkeep
	@touch screenshots/.gitkeep
	@echo "$(BLUE)✓ Carpetas creadas:$(NC)"
	@echo "  respuestas_piloto/   - para respuestas del formulario (cuando se aplique)"
	@echo "  notas_personales/    - notas privadas del Director sobre el piloto"
	@echo "  screenshots/         - capturas de pantalla (pueden contener datos)"
	@echo ""
	@echo "$(GREEN)✓ Todas protegidas por .gitignore$(NC)"
	@echo "  Estas carpetas NO se subirán a GitHub."
	@echo ""
	@echo "$(BLUE)Plantillas SOUL.md por Champion:$(NC)"
	@test -f SOUL_plantillas/SOUL_Infraestructura.md && echo "  ✓ SOUL_Infraestructura.md (Patrick)"
	@test -f SOUL_plantillas/SOUL_Desarrollo.md && echo "  ✓ SOUL_Desarrollo.md (Mario)"
	@test -f SOUL_plantillas/SOUL_Soporte.md && echo "  ✓ SOUL_Soporte.md (Irvin)"
	@echo ""

# ============================================================
# SEGURIDAD
# ============================================================

check-security:
	@echo "$(GREEN)Verificando que no haya datos sensibles expuestos...$(NC)"
	@echo ""
	@ISSUES=0
	@echo "$(BLUE)Buscando emails institucionales en el repo:$(NC)"
	@EMAILS=$$(grep -rl '@ujmd\.edu\.sv' --exclude-dir=.git . 2>/dev/null | wc -l | tr -d ' ')
	@if [ "$$EMAILS" != "0" ]; then \
		echo "  $(YELLOW)⚠ Emails @ujmd.edu.sv encontrados en $$EMAILS archivo(s):$(NC)"; \
		grep -rl '@ujmd\.edu\.sv' --exclude-dir=.git . 2>/dev/null | head -5; \
		echo "  $(BLUE)Nota: OK si son en documentos públicos (Acta, README, SOUL_plantillas)$(NC)"; \
		echo "  $(YELLOW)NO deben estar en: respuestas_piloto/, notas_personales/, screenshots/$(NC)"; \
	else \
		echo "  $(GREEN)✓ No se encontraron emails en archivos públicos sin contexto$(NC)"; \
	fi
	@echo ""
	@echo "$(BLUE)Buscando archivos de respuestas del cuestionario expuestos:$(NC)"
	@RESP=$$(find . -type f \( -name '*respuestas*' -o -name '*scores*' -o -name '*evaluacion*' \) \
		-not -path './.git/*' \
		-not -path './respuestas_piloto/*' | wc -l | tr -d ' ')
	@if [ "$$RESP" != "0" ]; then \
		echo "  $(YELLOW)⚠ Posibles datos de respuestas encontrados:$(NC)"; \
		find . -type f \( -name '*respuestas*' -o -name '*scores*' -o -name '*evaluacion*' \) \
			-not -path './.git/*' \
			-not -path './respuestas_piloto/*'; \
		echo "     → Muévelos a respuestas_piloto/ (protegido por .gitignore)"; \
	else \
		echo "  $(GREEN)✓ No se encontraron datos de respuestas expuestos$(NC)"; \
	fi
	@echo ""
	@echo "$(BLUE)Verificando secretos (.env, tokens):$(NC)"
	@SECRETS=$$(find . -type f \( -name '.env' -o -name 'credentials.json' -o -name '*.key' -o -name '*.pem' \
		-o -name 'auth.json' \) -not -path './.git/*' | wc -l | tr -d ' ')
	@if [ "$$SECRETS" != "0" ]; then \
		echo "  $(YELLOW)⚠ Archivos de credenciales encontrados:$(NC)"; \
		find . -type f \( -name '.env' -o -name 'credentials.json' -o -name '*.key' -o -name '*.pem' \
			-o -name 'auth.json' \) -not -path './.git/*'; \
	else \
		echo "  $(GREEN)✓ Sin credenciales ni secretos expuestos$(NC)"; \
	fi
	@echo ""
	@echo "$(BLUE)Verificando protección del .gitignore:$(NC)"
	@grep -qE '(\*\*.*\.hermes|\*\*.*hermes_config)' .gitignore && \
		echo "  $(GREEN)✓ Protege archivos Hermes$(NC)" || \
		echo "  $(YELLOW)⚠ No protege archivos Hermes$(NC)"
	@grep -qE '\*\*.*respuestas' .gitignore && \
		echo "  $(GREEN)✓ Protege respuestas del piloto$(NC)" || \
		echo "  $(YELLOW)⚠ No protege respuestas del piloto$(NC)"
	@grep -qE '\*\*.*notas_personal' .gitignore && \
		echo "  $(GREEN)✓ Protege notas personales$(NC)" || \
		echo "  $(YELLOW)⚠ No protege notas personales$(NC)"
	@echo ""

list-ignored:
	@echo "$(GREEN)Archivos/directorios ignorados por .gitignore (categorías):$(NC)"
	@echo ""
	@echo "$(BLUE)Protección de datos sensibles:$(NC)"
	@grep -v '^#' .gitignore | grep -v '^$$' | grep -E '(respuestas|notas|personal|datos|scores|evaluacion)' || echo "  (sin entradas específicas)"
	@echo ""
	@echo "$(BLUE)Protección de credenciales:$(NC)"
	@grep -v '^#' .gitignore | grep -v '^$$' | grep -E '(\.env|credentials|auth\.json|\.key|\.pem)' || echo "  (sin entradas específicas)"
	@echo ""
	@echo "$(BLUE)Protección del entorno Hermes:$(NC)"
	@grep -v '^#' .gitignore | grep -v '^$$' | grep -E '(hermes|\.hermes)' || echo "  (sin entradas específicas)"
	@echo ""
	@echo "$(BLUE)Protección de medios con datos potencialmente sensibles:$(NC)"
	@grep -v '^#' .gitignore | grep -v '^$$' | grep -E '(\.png|\.jpg|\.jpeg|\.gif|\.mp3|\.mp4|\.m4a)' || echo "  (sin entradas específicas)"
	@echo ""
	@echo "$(BLUE)Total de reglas en .gitignore:$(NC)"
	@grep -v '^#' .gitignore | grep -v '^$$' | wc -l | tr -d ' ' | xargs -I{} echo "  {} reglas activas"
	@echo ""

# ============================================================
# BACKUP Y LIMPIEZA
# ============================================================

backup:
	@echo "$(GREEN)Creando respaldo del repositorio...$(NC)"
	@mkdir -p $(BACKUP_DIR)
	@BACKUP_NAME="respaldo_AI_Fluentcy_$(TIMESTAMP).tar.gz"
	@tar -czf "$(BACKUP_DIR)/$$BACKUP_NAME" \
		--exclude='.git' \
		--exclude='$(BACKUP_DIR)' \
		--exclude='respuestas_piloto' \
		--exclude='notas_personales' \
		--exclude='screenshots' \
		--exclude='docs/compilados' \
		--exclude='*.tmp' \
		--exclude='*.log' \
		. 2>/dev/null
	@SIZE=$$(du -h "$(BACKUP_DIR)/$$BACKUP_NAME" | cut -f1)
	@echo "$(BLUE)✓ Respaldo creado: $(BACKUP_DIR)/$$BACKUP_NAME ($$SIZE)$(NC)"
	@echo ""
	@echo "$(YELLOW)Contenido incluido:$(NC)"
	@echo "  - Todos los archivos del repositorio versionados"
	@echo "  - Excluidos automáticamente por el tar:"
	@echo "    • .git/ (historial versionado en GitHub)"
	@echo "    • respuestas_piloto/ (datos sensibles)"
	@echo "    • notas_personales/ (privado)"
	@echo "    • screenshots/ (privado)"
	@echo ""
	@ls -lh $(BACKUP_DIR)/$$BACKUP_NAME
	@echo ""
	@echo "$(GREEN)Últimos 3 respaldos:$(NC)"
	@ls -lh $(BACKUP_DIR)/*.tar.gz 2>/dev/null | tail -3
	@echo ""

clean:
	@echo "$(YELLOW)Limpiando archivos temporales...$(NC)"
	@echo ""
	@find . -name "*.tmp" -type f -delete 2>/dev/null
	@find . -name "*.bak" -type f -delete 2>/dev/null
	@find . -name "*~" -type f -delete 2>/dev/null
	@find . -name ".DS_Store" -type f -delete 2>/dev/null
	@find . -name "._*" -type f -delete 2>/dev/null
	@find . -name "*.swp" -type f -delete 2>/dev/null
	@echo "$(GREEN)✓ Limpieza completada$(NC)"
	@echo ""
	@echo "$(BLUE)Archivos eliminados:$(NC)"
	@echo "  - *.tmp, *.bak, *~"
	@echo "  - .DS_Store, ._* (macOS)"
	@echo "  - *.swp (vim swap)"
	@echo ""

reset:
	@echo "$(YELLOW)ADVERTENCIA: Este comando reseteará los dashboards diarios$(NC)"
	@echo ""
	@echo "Se eliminarán:"
	@echo "  - dashboards/cierre_*.md (cierres diarios)"
	@echo "  - dashboards/plan_*.md (planes diarios)"
	@echo "  - docs/compilados/ (documentación generada)"
	@echo ""
	@read -p "¿Continuar? (s/N): " CONFIRM; \
	if [ "$$CONFIRM" = "s" ] || [ "$$CONFIRM" = "S" ]; then \
		rm -f dashboards/cierre_*.md dashboards/plan_*.md; \
		rm -rf docs/compilados; \
		echo "$(GREEN)✓ Reset completado$(NC)"; \
	else \
		echo "$(BLUE)Reset cancelado$(NC)"; \
	fi

# ============================================================
# DOCUMENTACIÓN
# ============================================================

docs:
	@echo "$(GREEN)Generando documentación consolidada...$(NC)"
	@echo ""
	@mkdir -p docs/compilados
	@TARGET="docs/compilados/AI_Fluentcy_Completo_$(DATE).md"
	@echo "# AI Fluentcy UJMD - Documentación Consolidada" > $$TARGET
	@echo "" >> $$TARGET
	@echo "**Generado:** $(DATE) $(TIMESTAMP)" >> $$TARGET
	@echo "**Fuente:** Implementar AI Fluentcy UJMD" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "---" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "# 1. README" >> $$TARGET
	@echo "" >> $$TARGET
	@cat README.md >> $$TARGET
	@echo "" >> $$TARGET
	@echo "---" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "# 2. Roadmap" >> $$TARGET
	@echo "" >> $$TARGET
	@cat $(ROADMAP) >> $$TARGET
	@echo "" >> $$TARGET
	@echo "---" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "# 3. Manual de Implementación Estratégica" >> $$TARGET
	@echo "" >> $$TARGET
	@cat $(MANUAL) >> $$TARGET
	@echo "" >> $$TARGET
	@echo "---" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "# 4. Alineación Estratégica" >> $$TARGET
	@echo "" >> $$TARGET
	@cat $(ALINEACION) >> $$TARGET
	@echo "" >> $$TARGET
	@echo "---" >> $$TARGET
	@echo "" >> $$TARGET
	@echo "# 5. Cuestionario Baseline" >> $$TARGET
	@echo "" >> $$TARGET
	@cat $(CUESTIONARIO) >> $$TARGET
	@echo "" >> $$TARGET
	@LINES=$$(wc -l < $$TARGET)
	@SIZE=$$(du -h $$TARGET | cut -f1)
	@echo "$(GREEN)✓ Documentación generada:$(NC)"
	@echo "  - Archivo: $$TARGET"
	@echo "  - Tamaño: $$LINES líneas, $$SIZE"
	@echo ""
	@echo "$(YELLOW)Nota: este archivo no se sube a GitHub (está en .gitignore vía docs/)$(NC)"
	@echo "  Lo puedes compartir localmente con quien necesites."
	@echo ""
