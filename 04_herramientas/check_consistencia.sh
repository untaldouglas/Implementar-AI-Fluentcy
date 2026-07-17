#!/usr/bin/env bash
# Chequeo de consistencia del repo — Protocolo de Evidencia y Estado (00_marco/Protocolo_Evidencia_y_Estado.md)
# Ejecutar antes de cada commit de cierre de sesión: bash 04_herramientas/check_consistencia.sh
# Origen: consultoría 17/07/2026 tras auditoría #02 (previene recurrencia de I9/I10 y divergencia de renders).

set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
FALLOS=0

ok()   { printf '  \033[32m✔\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✘\033[0m %s\n' "$1"; FALLOS=$((FALLOS+1)); }
warn() { printf '  \033[33m⚠\033[0m %s\n' "$1"; }

echo "== Chequeo de consistencia — $(date +%F) =="

# 1. Las dos copias del dashboard deben ser idénticas (render duplicado, fuente: ESTADO)
if diff -q "$REPO/04_herramientas/Dashboard_Jornada.html" "$REPO/docs/Dashboard_Jornada.html" >/dev/null 2>&1; then
  ok "Dashboard_Jornada.html idéntico en 04_herramientas/ y docs/"
else
  fail "Dashboard_Jornada.html DIVERGE entre 04_herramientas/ y docs/ — copiar desde la versión recién editada"
fi

# 2. Punteros tipo I9: nadie debe citar los formularios archivados como "detalle con evidencia"
#    (se excluye el Protocolo mismo, que documenta el patrón)
I9_HITS=$(grep -rn --include='*.md' "detalle con evidencia" "$REPO/01_piloto" "$REPO/00_marco" 2>/dev/null | grep -v "Protocolo_Evidencia_y_Estado.md" || true)
if [ -n "$I9_HITS" ]; then
  fail "Reapareció un puntero 'detalle con evidencia' (patrón I9) — verificar que el destino exista y esté lleno:"
  printf '%s\n' "$I9_HITS" | sed 's/^/      /'
else
  ok "Sin punteros 'detalle con evidencia' hacia archivos vacíos (patrón I9)"
fi

# 3. Carpeta de Drive: solo el ID canónico debe aparecer en documentos vivos
#    (mientras la decisión del §7 del Protocolo esté pendiente, este chequeo lista todos los IDs en uso)
IDS=$(grep -rhoE 'folders/[A-Za-z0-9_-]{20,}' "$REPO/ESTADO_PROYECTO.md" "$REPO/00_marco" "$REPO/01_piloto" "$REPO/04_herramientas/agendas" 2>/dev/null | sort -u)
N_IDS=$(printf '%s\n' "$IDS" | grep -c . || true)
if [ "$N_IDS" -le 1 ]; then
  ok "Un solo ID de carpeta Drive en documentos vivos: ${IDS#folders/}"
else
  fail "Hay $N_IDS IDs de carpeta Drive distintos en documentos vivos (decisión §7 del Protocolo pendiente):"
  printf '%s\n' "$IDS" | sed 's/^/      /'
fi

# 4. Patrón I10 (advisory): lenguaje de hecho consumado sospechoso en el log
if grep -nE "(cerrados|completad[oa]s?) antes de la reunión" "$REPO/ESTADO_PROYECTO.md" >/dev/null 2>&1; then
  warn "El log contiene '(cerrados|completados) antes de la reunión' — revisar que no sea un hito futuro escrito en pasado (regla §5 del Protocolo). Entradas históricas ya corregidas no cuentan."
else
  ok "Sin lenguaje de hecho consumado sospechoso nuevo en el log (patrón I10)"
fi

# 5. Seguridad (reutiliza la intención de make check-security): nada de PII obvia en rutas trackeadas nuevas
if git -C "$REPO" status --porcelain | grep -E "respuestas|baseline.*\.csv|notas_personales|screenshots" >/dev/null 2>&1; then
  fail "Hay archivos con pinta de datos sensibles en el working tree — revisar .gitignore antes de commitear"
else
  ok "Sin archivos con pinta de datos sensibles pendientes de commit"
fi

echo
if [ "$FALLOS" -eq 0 ]; then
  echo "RESULTADO: ✅ consistente ($(date +%H:%M))"
else
  echo "RESULTADO: ❌ $FALLOS chequeo(s) fallaron — corregir antes de commitear"
  exit 1
fi
