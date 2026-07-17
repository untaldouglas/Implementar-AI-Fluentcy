#!/usr/bin/env python3
"""
verificar_evidencia_drive.py — puente automatizado Drive -> GitHub (Protocolo_Evidencia_y_Estado.md §7)

Recorre TODA la carpeta canónica única del proyecto en Google Drive y señala:
  1. Archivos que viven FUERA de la estructura 00-04 (el patrón exacto que enterró la
     evidencia de C17/C19 en carpetas personales tipo "bitacoras cumplimiento S2/<Nombre>/").
  2. Archivos modificados recientemente (por defecto, últimos N días) en cualquier parte
     del árbol — para detectar entregas nuevas sin esperar a que alguien las redescubra
     manualmente, como pasó con C19 el 16-17/07.

No requiere -ni asume- credenciales especiales más allá del token ya usado por gdai/gapi.
Es un script de AUDITORÍA / ritual de sincronización, no un gate de commit: no bloquea
nada y siempre termina con código 0 (a diferencia de check_consistencia.sh).

Uso:
  ~/.hermes/venvs/google-workspace/bin/python 04_herramientas/verificar_evidencia_drive.py [--dias 7]

Deliberadamente NO entra a 04_Diagnostico_RESTRINGIDO (datos de diagnóstico de
participantes, acceso solo Douglas) — ver ESTADO_PROYECTO.md y .gitignore.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERMES_HOME = Path.home() / ".hermes"
TOKEN = HERMES_HOME / "google_token.json"
PROJECT_ID_FILE = HERMES_HOME / "aifluent_project_folder_id"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

CANONICAL_TOP_LEVEL = {
    "00_Gobernanza",
    "01_Evidencia_Champions",
    "02_Conocimiento_Colectivo",
    "03_Material_Programa",
}
RESTRICTED_TOP_LEVEL = "04_Diagnostico_RESTRINGIDO"
FOLDER_MIME = "application/vnd.google-apps.folder"


def build_drive_service():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    if not TOKEN.exists():
        sys.exit(f"ERROR: no existe {TOKEN} — correr el setup de gdai/gapi primero.")
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    return build("drive", "v3", credentials=creds)


def project_folder_id() -> str:
    if not PROJECT_ID_FILE.exists():
        sys.exit(f"ERROR: {PROJECT_ID_FILE} no existe — ver README de gdai.py.")
    return PROJECT_ID_FILE.read_text().strip()


def list_children(service, folder_id: str) -> list[dict]:
    files, page_token = [], None
    while True:
        resp = service.files().list(
            q=f"'{folder_id}' in parents and trashed = false",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, owners(emailAddress))",
            pageToken=page_token,
            pageSize=200,
        ).execute()
        files.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return files


def walk(service, folder_id: str, path_parts: list[str], skip_names: set[str]):
    """Yields (path_str, file_dict) for every non-folder file under folder_id."""
    for item in list_children(service, folder_id):
        if item["name"] in skip_names:
            continue
        parts = path_parts + [item["name"]]
        if item["mimeType"] == FOLDER_MIME:
            yield from walk(service, item["id"], parts, skip_names)
        else:
            yield "/".join(parts), item


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7, help="Ventana en días para 'modificado recientemente'")
    args = ap.parse_args()

    service = build_drive_service()
    root_id = project_folder_id()
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.dias)

    fuera_de_estructura: list[tuple[str, dict]] = []
    recientes: list[tuple[str, dict]] = []

    for path, item in walk(service, root_id, [], skip_names={RESTRICTED_TOP_LEVEL}):
        top = path.split("/", 1)[0]
        is_plantilla = "_PLANTILLA_" in item["name"]
        mtime = datetime.strptime(item["modifiedTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)

        if top not in CANONICAL_TOP_LEVEL and not is_plantilla:
            fuera_de_estructura.append((path, item))
        if mtime >= cutoff and not is_plantilla:
            recientes.append((path, item))

    print(f"== Escaneo de evidencia en Drive — {datetime.now():%Y-%m-%d %H:%M} ==")
    print(f"Carpeta canónica: {root_id} (04_Diagnostico_RESTRINGIDO excluido a propósito)\n")

    print(f"⚠️  FUERA DE LA ESTRUCTURA CANÓNICA (00-03) — {len(fuera_de_estructura)} archivo(s):")
    if fuera_de_estructura:
        print("    (mismo patrón que enterró C17/C19 en carpetas personales — mover antes de la próxima verificación)")
        for path, item in sorted(fuera_de_estructura, key=lambda x: x[1]["modifiedTime"], reverse=True):
            owner = (item.get("owners") or [{}])[0].get("emailAddress", "?")
            print(f"    · {path}  [{item['modifiedTime'][:10]}, {owner}]")
    else:
        print("    (ninguno — toda la evidencia vive dentro de 00-03)")

    print(f"\n🕓 MODIFICADOS EN LOS ÚLTIMOS {args.dias} DÍAS — {len(recientes)} archivo(s):")
    for path, item in sorted(recientes, key=lambda x: x[1]["modifiedTime"], reverse=True):
        marca = "⚠️ fuera de estructura" if path.split("/", 1)[0] not in CANONICAL_TOP_LEVEL else ""
        print(f"    · {path}  [{item['modifiedTime'][:10]}] {marca}")

    print(f"\nRESUMEN: {len(fuera_de_estructura)} fuera de estructura · {len(recientes)} modificado(s) en los últimos {args.dias} días.")
    print("Este script es informativo (ritual de sincronización / auditoría semanal) — no bloquea commits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
