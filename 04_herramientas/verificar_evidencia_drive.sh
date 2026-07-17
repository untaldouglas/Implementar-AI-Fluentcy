#!/usr/bin/env bash
# Wrapper para verificar_evidencia_drive.py — puente Drive -> GitHub (Protocolo §7/§8/§9).
# Requiere el venv de google-workspace que ya usa gdai/gapi (token de Hermes).
# Uso: bash 04_herramientas/verificar_evidencia_drive.sh [--dias N]

set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
GW_VENV="${GW_VENV:-$HOME/.hermes/venvs/google-workspace}"
PY="$GW_VENV/bin/python"

if [ ! -x "$PY" ]; then
  echo "ERROR: no encuentro el venv de google-workspace en $GW_VENV" >&2
  echo "       (el mismo que usa el alias gdai — revisar HERMES_HOME/GW_VENV)" >&2
  exit 1
fi

exec "$PY" "$REPO/04_herramientas/verificar_evidencia_drive.py" "$@"
