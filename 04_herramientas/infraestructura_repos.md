# Infraestructura de Repositorios — AI Fluency (MCA)

**Programa AI Fluency · Modelo de Conducción AI · UJMD — Dirección de Servicios Informáticos**
**Última actualización:** 18/08/2026 · **Responsable:** Douglas A. Galindo

> Cómo está montado el versionado del programa y cómo trabajar con él. Leer antes de cualquier operación con git.

---

## 1. Dónde vive el código (dos remotes, un solo push)

| Remote | URL | Rol | Visibilidad |
|---|---|---|---|
| `origin` (push #1) | https://repozone.ujmd.edu.sv/DireccionInformatica/aifluent-champions.git | **Repo oficial institucional** (Gitea) | Privado |
| `origin` (push #2) | https://github.com/untaldouglas/Implementar-AI-Fluentcy.git | Mirror + hosting de GitHub Pages | Público |
| `repozone` (remote adicional) | https://repozone.ujmd.edu.sv/DireccionInformatica/aifluent-champions.git | Fetch/pull institucional explícito | Privado |

**Modelo:** `origin` tiene DOS pushurls configuradas. `git push origin main` envía a ambos remotes en un solo comando (verificado 18/08: ambas líneas "Everything up-to-date" / "To ..." por remote).

Branches migradas: `main` + `Fase01` (congelación de F1, commit `3306dfd`).

## 2. Flujo de trabajo diario

```bash
# 1) Antes de commitear (obligatorio, lo valida el Protocolo)
bash 04_herramientas/check_consistencia.sh

# 2) Commit
git add -A
git commit -m "Mensaje en español describiendo el cambio"

# 3) Push dual (GitHub + repozone)
git push origin main
```

No hay prompts de credenciales para repozone: la autenticación la resuelve el credential helper dedicado (sección 3).

## 3. Autenticación

**repozone (Gitea):** credential helper dedicado con scope solo para esa URL:

```bash
# Configuración global (ya instalada en la máquina de Douglas)
git config --global credential.https://repozone.ujmd.edu.sv.helper "store --file=$HOME/.git-credentials-repozone"
# Archivo de credenciales: ~/.git-credentials-repozone (chmod 600, formato https://<usuario>:<token>@repozone.ujmd.edu.sv)
```

- **NO usar SSH** para repozone: el servidor no tiene el SSH de Gitea accesible (el puerto 22 es el sshd del sistema y rechaza las claves registradas en Gitea; los puertos alternativos están bloqueados por firewall). Verificado 18/08/2026.
- GitHub usa el helper de `gh` (`credential.https://github.com.helper=!/usr/bin/gh auth git-credential`), no requiere nada manual.

### Rotar el token de repozone (cuando toque)

1. Crear uno nuevo: repozone → Settings → Applications → Generate New Token (marcar `write:repository`).
2. Actualizar `~/.git-credentials-repozone` con el nuevo token (mismo formato, chmod 600).
3. Revocar el token anterior en la misma pantalla.
4. Verificar: `git push origin main` (debe salir sin pedir credenciales).

## 4. GitHub Pages (hosting público de artefactos)

- Los artefactos HTML públicos viven en `docs/` y se publican en https://untaldouglas.github.io/Implementar-AI-Fluentcy/ (repo GitHub, que se mantiene como mirror justamente para esto).
- repozone es privado: **no** sirve Pages públicos. Si en el futuro se quiere hosting institucional público, habilitar Pages en repozone sería una decisión aparte (requiere configuración del servidor Gitea).

## 5. Resolución de problemas

| Síntoma | Causa probable | Solución |
|---|---|---|
| Push solo llega a un remote | Pushurls incompletas en `remote.origin` | `git config --get-all remote.origin.pushurl` → deben estar AMBAS (repozone + github). Si falta una: `git remote set-url --add --push origin <url-faltante>` |
| "could not read Username for 'https://repozone...'" | Helper de credenciales no configurado o token inválido | Ver sección 3; si el token expiró, rotarlo |
| Push a GitHub rechazado | Sesión de `gh` vencida | `gh auth login` (o `gh auth refresh`) |
| Los renders de Pages no se actualizan | El push a GitHub no llegó (mirror atrasado) | `git ls-remote origin main` vs `git ls-remote repozone main`; si difieren, el push dual está roto (ver primera fila) |

## 6. Notas de la migración (18/08/2026)

- Origen: repo GitHub `untaldouglas/Implementar-AI-Fluentcy` (historial completo preservado, sin reescritura).
- Destino: `DireccionInformatica/aifluent-champions` creado vía API de Gitea con `private: true` (Gitea crea públicos por defecto — verificado).
- El commit `fe914c8` fue el primero con push dual funcionando correctamente. El commit `d5a02f5` fue el último antes de la migración.
- El token de API usado durante la migración no quedó persistido en config ni en el historial del repo (solo en el helper de credenciales, chmod 600).

---

*Documento de infraestructura · Piloto AI Fluency UJMD · 18/08/2026*
