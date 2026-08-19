#!/usr/bin/env python3
"""Genera las 5 guias F2 restantes (Jorge, Stephanie, Betty, Bryan, Oscar) desde un template comun."""
import os, re

OUT = "/home/dagalindo/1musa/DSI-UJMD/02-aifluent-champions/docs/fase2"

# ---------- Template comun (CSS + estructura) ----------
CSS = """*{box-sizing:border-box;margin:0;padding:0}
body{background:#03001a;color:#e0e8ff;font-family:'Space Grotesk',sans-serif;min-height:100vh}
a{color:#00e5ff;text-decoration:none}a:hover{text-decoration:underline}
code{background:#00e5ff15;color:#00e5ff;padding:1px 6px;border-radius:4px;font-size:.84em;font-family:monospace}
pre{background:#000d1f;border:1px solid #00e5ff22;border-radius:10px;padding:16px 18px;overflow-x:auto;margin:12px 0;font-family:monospace;font-size:.83rem;color:#80f0ff;line-height:1.7}
.comment{color:#446688}
.site-header{background:#03001a;border-bottom:1px solid #ffffff12;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.back-link{color:#8899bb;font-size:.85rem;display:flex;align-items:center;gap:6px}
.back-link:hover{color:#00e5ff;text-decoration:none}
.hbadge{background:#00e5ff18;border:1px solid #00e5ff44;color:#00e5ff;font-size:11px;font-weight:600;letter-spacing:2px;padding:4px 14px;border-radius:20px;text-transform:uppercase}
.champion-card{background:linear-gradient(135deg,#05002e 0%,#031020 100%);border-bottom:1px solid #ffffff12;padding:28px 24px}
.champion-inner{max-width:760px;margin:0 auto;display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap}
.avatar{width:60px;height:60px;border-radius:14px;background:#00e5ff18;border:2px solid #00e5ff44;display:flex;align-items:center;justify-content:center;font-size:1.7rem;flex-shrink:0}
.champion-info h1{font-family:'Montserrat',sans-serif;font-size:1.4rem;font-weight:900;color:#fff;margin-bottom:4px}
.champion-info .role{color:#7788aa;font-size:.86rem;margin-bottom:12px}
.tags{display:flex;gap:7px;flex-wrap:wrap}
.tag{background:#ffffff08;border:1px solid #ffffff15;border-radius:20px;padding:3px 11px;font-size:.76rem;color:#8899bb}
.tag.cyan{background:#00e5ff12;border-color:#00e5ff33;color:#00e5ff}
.tag.green{background:#00ff8812;border-color:#00ff8833;color:#00ff88}
.tag.yellow{background:#ffcc0012;border-color:#ffcc0033;color:#ffcc00}
.tag.purple{background:#a78bfa12;border-color:#a78bfa44;color:#c4b5fd}
.tag.red{background:#f43f5e12;border-color:#f43f5e44;color:#fb7185}
.prog-section{background:#02000f;border-bottom:1px solid #ffffff10;padding:0 24px}
.prog-inner{max-width:760px;margin:0 auto;display:flex;overflow-x:auto;gap:0}
.day-tab{flex:1;min-width:60px;padding:13px 6px;text-align:center;cursor:pointer;border-bottom:3px solid transparent;color:#446688;font-size:.76rem;font-weight:600;transition:all .15s;white-space:nowrap;background:none;border-left:none;border-right:none;border-top:none;font-family:'Space Grotesk',sans-serif}
.day-tab:hover{color:#8899bb}
.day-tab.active{color:#00e5ff;border-bottom-color:#00e5ff}
.day-num{font-size:.62rem;display:block;margin-bottom:2px;opacity:.7}
.content{max-width:760px;margin:0 auto;padding:28px 24px 80px}
.day-panel{display:none}
.day-panel.active{display:block}
.day-header{margin-bottom:22px}
.day-label{font-size:.74rem;color:#00e5ff;text-transform:uppercase;letter-spacing:2px;font-weight:600;margin-bottom:7px}
.day-title{font-family:'Montserrat',sans-serif;font-size:1.35rem;font-weight:900;color:#fff;margin-bottom:5px}
.day-meta{color:#7788aa;font-size:.86rem}
h3{font-family:'Montserrat',sans-serif;font-size:.98rem;font-weight:700;color:#ccd6ff;margin:22px 0 9px}
p{color:#a0b4cc;line-height:1.7;margin-bottom:11px;font-size:.91rem}
.concept-box{background:#ffffff07;border:1px solid #ffffff12;border-radius:11px;padding:16px 18px;margin:12px 0}
.concept-box .cb-label{font-size:.71rem;color:#556677;text-transform:uppercase;letter-spacing:1px;margin-bottom:7px}
.concept-box .cb-content{font-size:.89rem;color:#c0d0e8;line-height:1.65}
.alert{display:flex;gap:11px;background:#ff800015;border:1px solid #ff800033;border-radius:10px;padding:13px 16px;margin:13px 0}
.alert.info{background:#00e5ff0d;border-color:#00e5ff33}
.alert.success{background:#00ff880d;border-color:#00ff8833}
.alert.security{background:#f43f5e12;border-color:#f43f5e44}
.alert.framework{background:#a78bfa12;border-color:#a78bfa44}
.alert-icon{font-size:1rem;flex-shrink:0;margin-top:1px}
.alert-body{font-size:.86rem;color:#a0b4cc;line-height:1.6}
.alert-body strong{color:#e0e8ff}
.checklist{list-style:none;margin:12px 0}
.checklist li{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid #ffffff08;font-size:.89rem;color:#a0b4cc;cursor:pointer;transition:color .1s;line-height:1.5}
.checklist li:last-child{border-bottom:none}
.checklist li.checked{color:#00ff88}
.check-box{width:19px;height:19px;border:1.5px solid #334455;border-radius:5px;flex-shrink:0;margin-top:1px;display:flex;align-items:center;justify-content:center;font-size:11px;transition:all .15s}
.checklist li.checked .check-box{background:#00ff8820;border-color:#00ff88;color:#00ff88}
.evidence-card{background:#00ff880a;border:1px solid #00ff8822;border-radius:11px;padding:16px 18px;margin:13px 0}
.evidence-card .ev-title{color:#00ff88;font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:9px}
.evidence-card ul{list-style:none;padding:0}
.evidence-card li{color:#a0b4cc;font-size:.87rem;padding:4px 0 4px 16px;position:relative;line-height:1.5}
.evidence-card li::before{content:"→";position:absolute;left:0;color:#00ff88;font-size:.78rem}
.day-nav{display:flex;justify-content:space-between;margin-top:32px;padding-top:18px;border-top:1px solid #ffffff10}
.nav-btn{display:inline-flex;align-items:center;gap:7px;background:#ffffff08;border:1px solid #ffffff15;border-radius:10px;padding:9px 18px;color:#8899bb;font-size:.84rem;cursor:pointer;transition:all .15s;font-family:'Space Grotesk',sans-serif;font-weight:500}
.nav-btn:hover{background:#00e5ff10;color:#00e5ff;border-color:#00e5ff44}
.nav-btn.primary{background:#00e5ff18;border-color:#00e5ff66;color:#00e5ff}
.security-banner{max-width:760px;margin:0 auto 0;padding:14px 18px;background:#2a0a12;border:1px solid #f43f5e55;border-radius:10px;color:#fecdd3;font-size:14px;line-height:1.6;border-bottom:1px solid #ffffff10}
footer{text-align:center;color:#334455;font-size:.77rem;border-top:1px solid #ffffff10;padding:22px}"""

def tabs_html():
    return "\n".join(
        f'    <button class="day-tab{" active" if i==1 else ""}" onclick="showDay({i})"><span class="day-num">DÍA</span>{i}</button>'
        for i in range(1, 15))

def nav(prev, nxt):
    p = f'<button class="nav-btn" onclick="showDay({prev})">← Día {prev}</button>' if prev else "<span></span>"
    n = f'<button class="nav-btn primary" onclick="showDay({nxt})">Día {nxt} →</button>' if nxt else "<span></span>"
    return f'<div class="day-nav">{p}{n}</div>'

def day(num, label, title, meta, body, prev=None, nxt=None):
    return f'''<!-- DÍA {num} -->
<div id="day-{num}" class="day-panel{" active" if num==1 else ""}">
  <div class="day-header">
    <div class="day-label">{label}</div>
    <div class="day-title">{title}</div>
    <div class="day-meta">{meta}</div>
  </div>
{body}
  {nav(prev, nxt)}
</div>'''

def concept(label, content):
    return f'''  <div class="concept-box">
    <div class="cb-label">{label}</div>
    <div class="cb-content">{content}</div>
  </div>'''

def alert(kind, body):
    return f'''  <div class="alert {kind}">
    <span class="alert-icon">{'🔒' if kind=='security' else '📘' if kind=='framework' else '💡' if kind=='info' else '✅'}</span>
    <div class="alert-body">{body}</div>
  </div>'''

def evidence(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'''  <div class="evidence-card">
    <div class="ev-title">📎 Evidencia</div>
    <ul>{lis}</ul>
  </div>'''

def checklist(items):
    lis = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in items)
    return f'  <ul class="checklist">{lis}</ul>'

# ---------- Dias comunes (D1, D3, D4, D5, D8, D11, D14) ----------
def d1(p):
    return day(1, "Día 1 · Lección 1", "¿Qué es un prompt y por qué importa?", "30 min · Gemini (gemini.google.com) con tu cuenta institucional",
        concept("Concepto clave", 'Un <strong>prompt</strong> es la instrucción que le das a la IA. La calidad de lo que obtienes depende de cómo preguntas: rol + tarea + contexto. Hoy empiezas con Gemini, la herramienta estándar del programa (incluida en el contrato Workspace for Education de la UJMD).')
        + '<h3>Abrir Gemini</h3><p>Entra a <code>gemini.google.com</code> con tu cuenta institucional <code>'+p["email"]+'</code> (mismo inicio de sesión que el correo).</p>'
        + '<h3>Las 3 partes de un prompt efectivo</h3>'
        + concept("Estructura", '<strong style="color:#00e5ff">1. Rol</strong> — ¿Quién eres o quién quieres que sea la IA?<br><strong style="color:#00e5ff">2. Tarea</strong> — ¿Qué quieres que haga exactamente?<br><strong style="color:#00e5ff">3. Contexto</strong> — ¿Qué información necesita para hacerlo bien?')
        + '<h3>Práctica — compara estos dos prompts en Gemini</h3>'
        + '<p><strong>Prompt A — Sin estructura:</strong></p><pre>"'+p["promptA"]+'"</pre>'
        + '<p><strong>Prompt B — Con rol + tarea + contexto:</strong></p><pre>'+p["promptB"]+'</pre>'
        + '<h3>Actividades del Día 1</h3>'
        + checklist(["Ejecuté el Prompt A en Gemini y guardé la respuesta","Ejecuté el Prompt B y noté la diferencia de calidad","Creé mi propio prompt con una tarea real de mi puesto (sin datos sensibles)","Guardé los 3 prompts y respuestas en un Google Doc"])
        + alert("info", '<strong>Tu puesto:</strong> '+p["tipD1"])
        + alert("framework", '<strong>Marco de referencia:</strong> '+p["marcoD1"])
        + alert("security", '<strong>Regla de seguridad día 1:</strong> '+p["segD1"])
        + evidence(["Respuesta del Prompt A (para comparar)","Respuesta del Prompt B (el de calidad)","Tu prompt propio con tarea real (datos anonimizados)"]),
        None, 2)

def d3(p):
    return day(3, "Día 3 · Lección 2", "Contexto y memoria: la IA te \"recuerda\" entre sesiones", "30 min · Gemini",
        concept("Concepto clave", 'Gemini guarda el historial de tus conversaciones. Puedes retomar un chat, pedirle ajustes sin repetir todo, y usar "Gemini + Google Workspace" para que consulte tus documentos de Drive (con tu permiso). Esto corresponde al nivel L1-L2 del modelo MCA: pasar de "pregunta → respuesta → cerrar" a dar contexto adicional y refinar.')
        + '<h3>Práctica</h3>'
        + checklist(["Retomé el chat del Día 2 y pedí una mejora específica","Le di contexto adicional y verifiqué que lo aplicó","Probé pedirle que resuma una instrucción larga que le pegué"])
        + alert("security", '<strong>Ojo con el historial:</strong> todo lo que escribes en un chat queda en ese hilo. Si alguna vez necesitas hablar de algo sensible, no lo hagas en el chat — trabaja los datos en los sistemas oficiales de la universidad. El chat de IA es para redacción, análisis y borradores, no para almacenar información confidencial.')
        + evidence(["Captura o enlace del chat retomado con la mejora aplicada","Nota de qué contexto adicional funcionó mejor"]),
        2, 4)

def d4(p):
    return day(4, "Día 4 · Lección 2 (práctica)", "Refinar hasta obtener lo que necesitas", "45 min · Gemini",
        concept("Objetivo", "El refinamiento es la habilidad clave del nivel L1: no aceptar la primera respuesta, sino iterar pidiendo ajustes (tono, extensión, formato, nivel de detalle).")
        + '<h3>Práctica</h3><p>Toma un borrador generado ayer y aplícale al menos 3 refinamientos en cadena:</p>'
        + '<pre>"Acórtalo a 6 líneas."\n"Ahora usa tono formal, como comunicación oficial de la Dirección."\n"Convierte la sección principal en una tabla con 3 columnas."</pre>'
        + alert("info", '<strong>Consejo:</strong> si la IA se equivoca en un tema de tu área, dilo directamente ("eso no es correcto") — es parte del aprendizaje y la IA corrige con la instrucción adecuada. Eres el experto: la IA redacta, tú validas.')
        + evidence(["Versión inicial + versión final del documento tras los refinamientos","Los 3 refinamientos aplicados anotados"]),
        3, 5)

def d5(p):
    return day(5, "Día 5 · Lección 3", "Nivel L2: la IA lee archivos de tu área", "45 min · Gemini + Google Drive",
        concept("Concepto clave", 'Con la extensión de Workspace activada, Gemini puede leer documentos de tu Drive (los que tú le autorices). Es el salto a <strong>L2</strong>: la IA ya no trabaja solo con lo que escribes, sino con los documentos de tu equipo. Tú decides qué archivos comparte — la IA no "ve" todo tu Drive por defecto.')
        + '<h3>Práctica</h3>'
        + checklist(["Verifiqué que la extensión \"Google Workspace\" está activa en Gemini","Subí/seleccioné UN documento real no sensible de mi área","Le pedí: \"Resume este documento en 5 puntos\"","Le pedí: \"¿Qué acciones concretas propone este documento?\""])
        + alert("security", '<strong>Regla de oro:</strong> antes de compartir un archivo con la IA, pregúntate: ¿contiene datos personales de estudiantes/empleados, información confidencial o propiedad intelectual de la universidad? Si la respuesta es SÍ, <strong>no lo subas</strong> — usa una versión anonimizada o un resumen escrito por ti.')
        + evidence(["Nombre del documento usado (no sensible) y el resumen de 5 puntos generado","Anotación de qué tipo de archivos de tu área SÍ se pueden compartir y cuáles NO"]),
        4, 6)

def d8(p):
    return day(8, "Día 8 · Revisión de Semana 1", "Retroalimentación con tu facilitador", "45 min · Sesión con "+p["facilitador"],
        concept("Objetivo", "Revisar los avances de la semana con tu facilitador "+p["facilitador"]+" ("+p["facilitadorDesc"]+"): qué funcionó, qué ajustar, y preparar la Semana 2.")
        + '<h3>Checklist de la sesión</h3>'
        + checklist(["Mostré mis evidencias de los días 1–7 a "+p["facilitador"],"Discutí qué prompts funcionaron mejor para tareas de mi puesto","Validé mi tabla de clasificación de datos con su experiencia de F1","Definí mi caso real de la Semana 2 (proceso de mi área medible con IA)"])
        + evidence(["Nota de la sesión con "+p["facilitador"]+" (acuerdos y ajustes)","Caso real de Semana 2 definido"]),
        7, 9)

def d11(p):
    return day(11, "Día 11 · Lección 6", "Introducción a Hermes Agent (complemento)", "60 min · Hermes Agent en tu estación",
        concept("Concepto clave", 'Hermes Agent es el orquestador del programa (Nous Research, open source). Mientras Gemini es el asistente conversacional estándar, Hermes agrega capacidades de agente: leer archivos locales, ejecutar tareas en tu máquina y seguir procedimientos. En tu nivel actual (L1→L2), lo usas como complemento de Gemini.')
        + '<h3>Práctica</h3>'
        + checklist(["Verifiqué que Hermes está instalado en mi estación (con "+p["facilitador"]+" en la sesión de setup)","Ejecuté mi primer chat: <code>hermes chat -q \"hola, ¿quién eres?\"</code>","Repetí un prompt que ya hice en Gemini y comparé las respuestas"])
        + alert("security", '<strong>Mismas reglas:</strong> lo que no subes a Gemini tampoco se lo das a Hermes. Las reglas de clasificación de datos aplican a TODAS las herramientas por igual.')
        + evidence(["Captura de tu primer chat con Hermes","Comparación de respuestas Gemini vs Hermes para el mismo prompt"]),
        10, 12)

def d14(p):
    return day(14, "Día 14 · Cierre del ciclo", "Entrega, reflexión y siguiente nivel", "45 min · Google Docs + sesión con facilitador",
        concept("Objetivo", "Consolidar la evidencia del ciclo de 14 días, reflexionar sobre el avance L1→L2 y preparar la entrega formal con "+p["facilitador"]+" y Douglas.")
        + '<h3>Checklist de cierre</h3>'
        + checklist(["Completé mi reflexión: qué aprendí, qué aplicaré en mi trabajo diario, qué me costó más","Organicé toda la evidencia de los 14 días en la carpeta del programa (Drive, F2_02_Evidencia_Participantes/"+p["carpeta"]+"/)","Compartí el documento con "+p["facilitador"]+" como comentador → Aprobar cuando esté listo","Presenté mi caso real y medición en la sesión de validación","Confirmé mi siguiente meta: consolidar L2 y avanzar hacia L3 (espacio de contexto propio)"])
        + alert("success", '<strong>Meta del ciclo:</strong> al cerrar estos 14 días habrás demostrado el nivel L2 (la IA lee archivos de tu área) con evidencia real: tu tabla de clasificación, tu caso real medido y tu flujo con Gemini + Hermes. Ese es el camino de L1 → L2 del modelo MCA.')
        + evidence(["Reflexión escrita del ciclo","Evidencia organizada en Drive (carpeta del participante)","Validación: "+p["facilitador"]+" (facilitador) + co-firma Douglas"]),
        13, None)

# ---------- Participantes ----------
P = {
"jorge": dict(
    nombre="Jorge Ernesto López Rivera", email="jelopezr@ujmd.edu.sv", avatar="🗂️",
    rol="Coordinador de Sistemas y Operaciones · Dirección de Informática · UJMD",
    nivel="L2 · Conductor 🟢", zona="Zona: Conductor", meta="Meta: L3 — SOUL.md con contexto fijo",
    facilitador="Irvin Morales", facilitadorDesc="Champion F1 de Soporte/Mesa de Servicios",
    carpeta="Jorge", dominio="Sistemas y Operaciones",
    promptA="redacta un correo sobre el mantenimiento de los sistemas",
    promptB='''"Eres coordinador de sistemas y operaciones de la DSI de la UJMD.
Redacta un correo interno para el equipo de soporte técnico informando
el calendario de mantenimiento preventivo de esta semana (2 laboratorios
por día, horario posterior a las 5 PM, sin interrumpir clases).
Tono: profesional, breve, con instrucciones claras."''',
    tipD1="tus casos típicos son coordinar el soporte técnico, asignar tareas de mantenimiento, atender incidencias de sistemas y supervisar el funcionamiento de los servicios bajo tu responsabilidad.",
    marcoD1="la coordinación del soporte se apoya en ITIL 4 (gestión de incidentes y de cambios) y COBIT (control y alineación con el negocio). A lo largo de la guía vincularás cada ejercicio con estos marcos, más ISO 27001, LEAN y PRINCE2/agile.",
    segD1="nunca pongas nombres reales de estudiantes, credenciales, direcciones internas ni detalles de incidentes reales en los prompts. Usa descripciones genéricas. Esto respeta la protección de datos personales y la propiedad intelectual de la universidad.",
    d2prompts=['''1. "Eres coordinador de sistemas y operaciones. Redacta una lista de
   verificación semanal para supervisar el servicio de soporte técnico:
   tickets atendidos, pendientes, tiempos de respuesta, mantenimientos
   preventivos. Formato: checklist con criterio OK/ALERTA."''',
'''2. "Eres coordinador de sistemas y operaciones. Escribe un
   procedimiento paso a paso de escalamiento de un incidente crítico
   (ej.: caída de un servicio institucional), siguiendo la estructura
   ITIL: detección → clasificación → contención → erradicación →
   recuperación → lecciones aprendidas. Deja espacios para
   responsables y horarios."''',
'''3. "Eres coordinador de sistemas y operaciones. Redacta una minuta de
   asignación de tareas semanales para el equipo de soporte (tickets,
   mantenimientos, actualizaciones), con prioridad alta/media/baja.
   Deja espacios en blanco para nombres y fechas."'''],
    d2fw='''<strong>ITIL + COBIT:</strong> el escalamiento de incidentes sigue la gestión de incidentes de ITIL; la minuta alinea tareas con los procesos de COBIT (APO/DSS). La IA redacta; la clasificación de prioridades y la asignación la decides tú con base en criticidad y riesgo.''',
    d2seg="la minuta NO lleva nombres reales de compañeros ni detalles técnicos de sistemas — los agregas tú después en el documento oficial.",
    d2evid=["3 respuestas de Gemini guardadas en tu Google Doc de evidencia","Anotación de qué prompt dio el mejor resultado y por qué"],
    d6intro="Tu tabla personal de clasificación de información de sistemas y operaciones — el instrumento que usarás toda la fase (y que el programa exige como evidencia de manejo responsable). Se apoya en el control de clasificación de activos de ISO/IEC 27001 y en la política de seguridad de la universidad.",
    d6tabla=[("Reportes de tickets atendidos","Interno","✅ Sí (sin nombres de usuarios)","—"),
             ("Inventario de equipos y software","Interno","✅ Sí (sin IPs ni detalles)","—"),
             ("Credenciales y accesos","Restringido","❌ Nunca","Gestor de contraseñas institucional"),
             ("Incidentes de seguridad reales","Restringido","❌ No (solo anonimizado)","Usar caso ficticio equivalente"),
             ("Datos de estudiantes (notas, listas)","Confidencial","❌ No","Nunca en IA"),
             ("Procedimientos internos de soporte","Confidencial","⚠️ Solo resumen","Describir pasos sin detalles")],
    d6fw='''<strong>Referencias:</strong> la clasificación de activos es un control de ISO/IEC 27001 (A.5.9 y A.5.12); la protección de datos personales sigue los principios internacionales de consentimiento, finalidad y minimización; la propiedad intelectual y confidencialidad institucional se rige por la normativa de la universidad.''',
    d7title="Caso real de tu puesto: procedimiento de soporte o gestión",
    d7goal="Completar tu primer caso real completo: un documento de tu área de sistemas y operaciones (procedimiento de escalamiento, guía de mantenimiento, comunicación al equipo), de principio a fin, con la IA como asistente y tu criterio como responsable.",
    d7items=["Elegí un documento real que necesito producir (procedimiento de escalamiento, guía de mantenimiento, aviso de cambio de servicio)","Redacté el borrador con Gemini usando rol + tarea + contexto","Refiné al menos 2 veces hasta quedar conforme","Revisé y corregí yo mismo el resultado (la IA redacta, yo valido)","Guardé versión final + registro del proceso (prompt usado, refinamientos)"],
    d7fw='''<strong>Enfoque LEAN:</strong> al documentar tu procedimiento, identifica qué pasos del proceso actual son desperdicio (esperas, reprocesos, tareas manuales repetitivas) y márcalos. El programa medirá el antes/después: ese es el corazón de la mejora continua con LEAN.''',
    d7seg="verifica que el documento final no contenga información confidencial (nombres reales, datos de sistemas). La revisión humana final es obligatoria — la IA no firma, tú sí.",
    d9title="Semana 2: ITIL y COBIT con apoyo de IA",
    d9goal="Usar la IA para documentar y mejorar prácticas de gestión de servicios TI (ITIL 4) y de gobierno/control (COBIT 2019) en tu área: gestión de incidentes, gestión de cambios, gestión de activos, monitoreo de servicios.",
    d9items=["Elegí una práctica ITIL de mi área (gestión de incidentes, cambios, activos o nivel de servicio)","Pedí a Gemini: \"describe cómo implementar esta práctica en una dirección de informática universitaria, con roles y pasos\"","Pedí: \"convierte esto en una tabla de responsabilidades (RACI) según COBIT\"","Evalué críticamente: ¿qué aplica a mi realidad y qué no?"],
    d9fw='''<strong>ITIL + COBIT:</strong> ITIL te da el "cómo" operar servicios (incidentes, cambios, activos); COBIT te da el "cómo gobernar" (roles RACI, objetivos de control). La IA genera borradores; el criterio de qué aplica en la UJMD es tuyo.''',
    d10title="LEAN: proceso medible y mejora continua",
    d10goal="Definir tu proceso candidato para la medición antes/después (modelo C19 de F1 + enfoque LEAN): un proceso repetitivo de tu puesto que puedas sistematizar con IA y medir en tiempo.",
    d10items=["Identifiqué 2 procesos repetitivos de mi puesto (ej.: elaborar el reporte semanal de tickets; consolidar incidencias; coordinar mantenimientos)","Con Gemini, describí el paso a paso de uno y el tiempo estimado actual (línea base)","Marqué los pasos que son desperdicio LEAN (esperas, reprocesos, tareas manuales)","Guardé la línea base en la plantilla de proceso medido"],
    d10fw='''<strong>Mejora continua (Kaizen):</strong> el ciclo PDCA (Plan-Do-Check-Act) es la base de LEAN: planifica el cambio (usar IA), hazlo, verifica el resultado medido y actúa ajustando. Tu medición antes/después es exactamente el "Check" de un ciclo PDCA.''',
    d10seg="los tiempos y pasos son tuyos — no incluyen datos de terceros. La plantilla de medición se comparte en Drive del programa sin datos personales.",
    d12title="Hermes con un caso real de sistemas y operaciones",
    d12goal="Usar Hermes para una tarea real de tu área, entendiendo cuándo conviene cada herramienta: Gemini para redacción rápida en el navegador, Hermes para tareas ligadas a tu máquina y archivos locales.",
    d12items=["Le pedí a Hermes que redacte un procedimiento corto de escalamiento (misma regla de clasificación de datos)","Le pedí que liste qué archivos de una carpeta local puedo usar para documentar (sin abrir nada sensible)","Anoté cuándo usaría Gemini vs Hermes en mi trabajo diario"],
    d12fw='''<strong>Gestión de incidentes ITIL:</strong> imagina usar Hermes para documentar incidentes repetitivos de la mesa: un agente que consulte tus procedimientos y genere el reporte con el formato estándar. Esa es la visión de nivel L3+.''',
    d13title="PRINCE2/agile: gestionar un proyecto con IA",
    d13goal="Combinar todo lo aprendido en un flujo completo: gestionar un mini-proyecto de tu área (ej.: renovación de equipos, implementación de un procedimiento de soporte, actualización de software) aplicando conceptos de PRINCE2/agile, con IA como asistente y revisión humana en el cierre.",
    d13items=["Definí el alcance del mini-proyecto (qué se entregará y qué NO — gestión de alcance)","Con Gemini: desglosé el plan en fases con entregables, responsables y tiempos (PRINCE2 o sprint agile)","Identifiqué riesgos del proyecto y su mitigación (con apoyo de IA y mi criterio)","Ejecuté el caso real de la Semana 2 (proceso medible del Día 10) y medí el tiempo CON IA vs línea base","Documenté el delta (ahorro de tiempo) en la plantilla"],
    d13fw='''<strong>PRINCE2/agile:</strong> PRINCE2 te da el control por fases (iniciar → dirigir → entregar) con justificación continua del negocio y gestión de riesgos; agile te da la entrega incremental y la adaptación al cambio. La IA acelera la documentación del plan; la decisión de fase y la aprobación de entregables es tuya como coordinador.''',
    d13seg="verifica que el entregable final no contenga datos personales ni detalles confidenciales. El entregable que se comparte en el programa es la versión anonimizada + la medición.",
    footer="Guía 14 Días · AI Fluency F2 · UJMD DSI · Jorge López (Coordinador de Sistemas y Operaciones) · Facilitador: Irvin Morales · Marcos: ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile · 19/08/2026",
    file="guia_jorge_lopez.html"
),
"steph": dict(
    nombre="Stephanie Miranda Ventura", email="symirandav@ujmd.edu.sv", avatar="💻",
    rol="Coordinadora de Desarrollo y Mantenimiento de Sistemas Informáticos Corporativos · Dirección de Informática · UJMD",
    nivel="L1 · Pasajero 🟤", zona="Zona: Pasajero", meta="Meta: L2 — IA lee archivos del área",
    facilitador="Mario Valencia", facilitadorDesc="Champion F1 de Desarrollo",
    carpeta="Stephanie", dominio="Desarrollo y Mantenimiento de Sistemas",
    promptA="redacta un correo sobre el estado de los sistemas",
    promptB='''"Eres coordinadora de desarrollo y mantenimiento de sistemas
informáticos corporativos de la DSI de la UJMD. Redacta un correo
interno para el equipo de desarrollo informando el estado de los
sistemas en producción esta semana (2 sistemas actualizados, 1 en
pruebas, 1 pendiente de corrección).
Tono: profesional, claro, con una tabla resumen."''',
    tipD1="tus casos típicos son coordinar el equipo de desarrollo, supervisar el portafolio de sistemas, priorizar requerimientos y comunicar estados de proyectos.",
    marcoD1="la gestión de desarrollo se apoya en agile/SCRUM (entregas incrementales) y PRINCE2 (control por fases), con ITIL para la gestión de cambios en producción y COBIT para el gobierno de TI. A lo largo de la guía vincularás cada ejercicio con estos marcos, más ISO 27001 y LEAN.",
    segD1="nunca pongas nombres reales de estudiantes, datos personales, credenciales ni detalles de sistemas en producción en los prompts. Usa descripciones genéricas. Esto respeta la protección de datos personales y la propiedad intelectual de la universidad.",
    d2prompts=['''1. "Eres coordinadora de desarrollo y mantenimiento de sistemas.
   Redacta una lista de verificación semanal para supervisar el estado
   del portafolio de sistemas en producción (operativos, en pruebas,
   pendientes). Formato: checklist con criterio OK/ALERTA."''',
'''2. "Eres coordinadora de desarrollo. Escribe un procedimiento paso a
   paso para solicitar un cambio en un sistema en producción
   (estructura ITIL de gestión de cambios): solicitud → evaluación de
   impacto → aprobación → implementación → verificación → cierre.
   Deja espacios para responsables y fechas."''',
'''3. "Eres coordinadora de desarrollo y mantenimiento. Redacta una
   minuta de asignación de tareas semanales para el equipo de
   desarrollo (mantenimiento, requerimientos nuevos, correcciones),
   con prioridad alta/media/baja. Deja espacios en blanco para
   nombres y fechas."'''],
    d2fw='''<strong>ITIL + agile:</strong> el procedimiento de cambios sigue la gestión de cambios de ITIL (aplicable a producción); la minuta de tareas puede estructurarse como un sprint de SCRUM (backlog priorizado). La IA redacta; las prioridades y la asignación las decides tú.''',
    d2seg="la minuta NO lleva nombres reales de compañeros ni detalles de sistemas en producción — los agregas tú después en el documento oficial.",
    d2evid=["3 respuestas de Gemini guardadas en tu Google Doc de evidencia","Anotación de qué prompt dio el mejor resultado y por qué"],
    d6intro="Tu tabla personal de clasificación de información de desarrollo y sistemas — el instrumento que usarás toda la fase (y que el programa exige como evidencia de manejo responsable). Se apoya en el control de clasificación de activos de ISO/IEC 27001 y en la política de seguridad de la universidad.",
    d6tabla=[("Reportes de estado de sistemas","Interno","✅ Sí (sin datos de usuarios)","—"),
             ("Código fuente y documentación técnica","Interno","⚠️ Solo fragmentos genéricos","Describir patrones sin código sensible"),
             ("Credenciales y accesos a producción","Restringido","❌ Nunca","Gestor de contraseñas institucional"),
             ("Datos de estudiantes (notas, listas, SIED)","Confidencial","❌ No","Nunca en IA"),
             ("Requerimientos de negocio","Interno","✅ Sí (anonimizados)","—"),
             ("Incidentes de producción reales","Restringido","❌ No (solo anonimizado)","Usar caso ficticio equivalente")],
    d6fw='''<strong>Referencias:</strong> la clasificación de activos es un control de ISO/IEC 27001 (A.5.9 y A.5.12); el desarrollo seguro de software sigue los principios del SDLC seguro (OWASP); la propiedad intelectual del código pertenece a la universidad y su uso con IA debe preservar la confidencialidad.''',
    d7title="Caso real de tu puesto: documento de coordinación de desarrollo",
    d7goal="Completar tu primer caso real completo: un documento de tu área de desarrollo (estado de portafolio, procedimiento de solicitud de cambio, comunicación al equipo), de principio a fin, con la IA como asistente y tu criterio como responsable.",
    d7items=["Elegí un documento real que necesito producir (estado del portafolio, procedimiento de cambios, comunicación de avance)","Redacté el borrador con Gemini usando rol + tarea + contexto","Refiné al menos 2 veces hasta quedar conforme","Revisé y corregí yo mismo el resultado (la IA redacta, yo valido)","Guardé versión final + registro del proceso (prompt usado, refinamientos)"],
    d7fw='''<strong>Enfoque LEAN:</strong> al documentar tu proceso, identifica qué pasos actuales son desperdicio (esperas de aprobación, reprocesos, tareas manuales repetitivas) y márcalos. El programa medirá el antes/después: ese es el corazón de la mejora continua con LEAN.''',
    d7seg="verifica que el documento final no contenga información confidencial (nombres reales, datos de sistemas). La revisión humana final es obligatoria — la IA no firma, tú sí.",
    d9title="Semana 2: agile/SCRUM e ITIL con apoyo de IA",
    d9goal="Usar la IA para documentar y mejorar la gestión de tu equipo de desarrollo: estructura de sprints (SCRUM), gestión de requerimientos y gestión de cambios en producción (ITIL), con gobierno de TI (COBIT).",
    d9items=["Elegí una práctica de mi área (planificación de sprint, gestión de requerimientos o gestión de cambios ITIL)","Pedí a Gemini: \"describe cómo estructurar esta práctica en un equipo de desarrollo universitario, con roles y pasos\"","Pedí: \"convierte esto en una tabla de responsabilidades (RACI) según COBIT\"","Evalué críticamente: ¿qué aplica a mi realidad y qué no?"],
    d9fw='''<strong>Agile + ITIL + COBIT:</strong> SCRUM te da la entrega incremental (sprints, backlog); ITIL te da la gestión de cambios en producción; COBIT te da el gobierno (roles RACI, objetivos de control). La IA genera borradores; el criterio de qué aplica en la UJMD es tuyo.''',
    d10title="LEAN: proceso medible y mejora continua",
    d10goal="Definir tu proceso candidato para la medición antes/después (modelo C19 de F1 + enfoque LEAN): un proceso repetitivo de tu puesto que puedas sistematizar con IA y medir en tiempo.",
    d10items=["Identifiqué 2 procesos repetitivos de mi puesto (ej.: elaborar el reporte semanal del portafolio; consolidar avances del equipo; documentar requerimientos)","Con Gemini, describí el paso a paso de uno y el tiempo estimado actual (línea base)","Marqué los pasos que son desperdicio LEAN (esperas, reprocesos, tareas manuales)","Guardé la línea base en la plantilla de proceso medido"],
    d10fw='''<strong>Mejora continua (Kaizen):</strong> el ciclo PDCA (Plan-Do-Check-Act) es la base de LEAN: planifica el cambio (usar IA), hazlo, verifica el resultado medido y actúa ajustando. Tu medición antes/después es exactamente el "Check" de un ciclo PDCA.''',
    d10seg="los tiempos y pasos son tuyos — no incluyen datos de terceros. La plantilla de medición se comparte en Drive del programa sin datos personales.",
    d12title="Hermes con un caso real de desarrollo",
    d12goal="Usar Hermes para una tarea real de tu área, entendiendo cuándo conviene cada herramienta: Gemini para redacción rápida en el navegador, Hermes para tareas ligadas a tu máquina y archivos locales.",
    d12items=["Le pedí a Hermes que redacte un procedimiento corto de solicitud de cambio (misma regla de clasificación de datos)","Le pedí que liste qué archivos de una carpeta local puedo usar para documentar (sin abrir nada sensible)","Anoté cuándo usaría Gemini vs Hermes en mi trabajo diario"],
    d12fw='''<strong>Gestión de cambios ITIL:</strong> imagina usar Hermes para documentar cambios repetitivos del portafolio: un agente que consulte tus procedimientos y genere el reporte con el formato estándar. Esa es la visión de nivel L3+.''',
    d13title="PRINCE2/agile: gestionar un proyecto con IA",
    d13goal="Combinar todo lo aprendido en un flujo completo: gestionar un mini-proyecto de tu área (ej.: implementación de un módulo, actualización de un sistema, mejora de un proceso de desarrollo) aplicando conceptos de PRINCE2/agile, con IA como asistente y revisión humana en el cierre.",
    d13items=["Definí el alcance del mini-proyecto (qué se entregará y qué NO — gestión de alcance)","Con Gemini: desglosé el plan en fases con entregables, responsables y tiempos (PRINCE2 o sprint agile)","Identifiqué riesgos del proyecto y su mitigación (con apoyo de IA y mi criterio)","Ejecuté el caso real de la Semana 2 (proceso medible del Día 10) y medí el tiempo CON IA vs línea base","Documenté el delta (ahorro de tiempo) en la plantilla"],
    d13fw='''<strong>PRINCE2/agile:</strong> PRINCE2 te da el control por fases con justificación continua del negocio y gestión de riesgos; agile te da la entrega incremental (sprints). La IA acelera la documentación del plan; la decisión de fase y la aprobación de entregables es tuya como coordinadora.''',
    d13seg="verifica que el entregable final no contenga datos personales ni detalles confidenciales de sistemas. El entregable que se comparte en el programa es la versión anonimizada + la medición.",
    footer="Guía 14 Días · AI Fluency F2 · UJMD DSI · Stephanie Miranda (Coordinadora de Desarrollo y Mantenimiento de Sistemas) · Facilitador: Mario Valencia · Marcos: ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile · 19/08/2026",
    file="guia_stephanie_miranda.html"
),
"betty": dict(
    nombre="Ana Bety del Carmen Figueroa Guillén", email="bcfigueroac@ujmd.edu.sv", avatar="📞",
    rol="Asistente a la Dirección de Informática y Recepcionista Soporte Mesa de Servicio · UJMD",
    nivel="L1 · Pasajero 🟤", zona="Zona: Pasajero", meta="Meta: L2 — IA lee archivos del área",
    facilitador="Patrick Orellana", facilitadorDesc="Champion F1 de Infraestructura",
    carpeta="Betty", dominio="Atención a usuarios y Mesa de Servicio",
    promptA="redacta un correo de respuesta a un usuario",
    promptB='''"Eres asistente de la dirección de informática y recepcionista de la
mesa de servicio de la UJMD. Redacta una respuesta profesional y
empática para un usuario administrativo (no técnico) que reportó que
su computadora no enciende desde esta mañana. Incluye: saludo,
3 causas básicas que el usuario puede verificar solo, y cómo escalar
si no se resuelve."''',
    tipD1="tus casos típicos son atender a docentes, estudiantes y personal en la mesa de servicio, dar información de los servicios informáticos, redactar respuestas a usuarios y registrar solicitudes.",
    marcoD1="la atención al usuario se apoya en ITIL 4 (práctica de gestión de solicitudes y del service desk) y en los principios de protección de datos personales. A lo largo de la guía incorporarás ISO 27001 (datos personales), LEAN (mejora de tiempos de atención) y conceptos básicos de gestión de proyectos.",
    segD1="nunca pongas nombres reales de estudiantes, docentes o personal, ni datos de sus equipos o cuentas en los prompts. Usa descripciones genéricas (\"un usuario\", \"una docente\"). Esto respeta la protección de datos personales y la propiedad intelectual de la universidad.",
    d2prompts=['''1. "Eres recepcionista de la mesa de servicio de la DSI de la UJMD.
   Redacta una guía de primeros pasos para un usuario que necesita
   restablecer su contraseña del correo institucional. Pasos simples,
   lenguaje no técnico, con qué hacer si no funciona."''',
'''2. "Eres asistente de la mesa de servicio. Escribe un procedimiento
   breve de registro de una solicitud de soporte (estructura ITIL de
   gestión de solicitudes): recepción → registro de datos básicos →
   clasificación → asignación → seguimiento. Deja espacios para
   responsables y tiempos."''',
'''3. "Eres recepcionista de la mesa de servicio. Redacta una plantilla
   de respuesta para las consultas más frecuentes (contraseña,
   correo, wifi, impresión), con tono amable y claro. Deja espacios
   para personalizar cada caso."'''],
    d2fw='''<strong>ITIL service desk:</strong> la mesa de servicio es la puerta de entrada de la gestión de servicios TI (ITIL 4): recibir, registrar, clasificar y escalar. La IA redacta plantillas y guías; la atención personalizada y el criterio de cuándo escalar son tuyos.''',
    d2seg="las respuestas NO llevan datos personales de los usuarios — los agregas tú al personalizar cada caso en los sistemas oficiales.",
    d2evid=["3 respuestas de Gemini guardadas en tu Google Doc de evidencia","Anotación de qué prompt dio el mejor resultado y por qué"],
    d6intro="Tu tabla personal de clasificación de información de la mesa de servicio — el instrumento que usarás toda la fase (y que el programa exige como evidencia de manejo responsable). Se apoya en el control de clasificación de activos de ISO/IEC 27001 y en la política de seguridad de la universidad.",
    d6tabla=[("Respuestas a consultas frecuentes","Interno","✅ Sí","—"),
             ("Registro de solicitudes de soporte","Confidencial","❌ No (tienen datos de usuarios)","Trabajar en los sistemas oficiales"),
             ("Datos personales de docentes/estudiantes (correos, notas)","Confidencial","❌ No","Nunca en IA"),
             ("Credenciales o contraseñas","Restringido","❌ Nunca","Gestor de contraseñas institucional"),
             ("Plantillas de comunicación interna","Interno","✅ Sí","—"),
             ("Horarios y procedimientos de la mesa","Interno","✅ Sí","—")],
    d6fw='''<strong>Referencias:</strong> la clasificación de activos es un control de ISO/IEC 27001 (A.5.9 y A.5.12); la protección de datos personales sigue los principios internacionales de consentimiento, finalidad y minimización; la propiedad intelectual y confidencialidad institucional se rige por la normativa de la universidad.''',
    d7title="Caso real de tu puesto: guía o plantilla de atención",
    d7goal="Completar tu primer caso real completo: un documento de tu mesa de servicio (guía de primeros pasos, plantilla de respuesta, procedimiento de registro), de principio a fin, con la IA como asistente y tu criterio como responsable.",
    d7items=["Elegí un documento real que necesito producir (guía para usuarios, plantilla de respuesta, procedimiento de registro)","Redacté el borrador con Gemini usando rol + tarea + contexto","Refiné al menos 2 veces hasta quedar conforme","Revisé y corregí yo mismo el resultado (la IA redacta, yo valido)","Guardé versión final + registro del proceso (prompt usado, refinamientos)"],
    d7fw='''<strong>Enfoque LEAN:</strong> al documentar tu procedimiento de atención, identifica qué pasos actuales son desperdicio (esperas, reprocesos, traslados innecesarios) y márcalos. El programa medirá el antes/después: ese es el corazón de la mejora continua con LEAN.''',
    d7seg="verifica que el documento final no contenga datos personales de usuarios. La revisión humana final es obligatoria — la IA no firma, tú sí.",
    d9title="Semana 2: ITIL service desk y protección de datos con apoyo de IA",
    d9goal="Usar la IA para documentar y mejorar las prácticas de la mesa de servicio (ITIL 4: gestión de solicitudes, gestión de incidentes, base de conocimiento) y las reglas de protección de datos personales que aplican a tu atención diaria.",
    d9items=["Elegí una práctica de la mesa de servicio (registro de solicitudes, gestión de incidentes, base de conocimiento de consultas frecuentes)","Pedí a Gemini: \"describe cómo implementar esta práctica en la mesa de servicio de una universidad, con roles y pasos\"","Pedí: \"convierte esto en una tabla de responsabilidades (RACI) según COBIT\"","Evalué críticamente: ¿qué aplica a mi realidad y qué no?"],
    d9fw='''<strong>ITIL + COBIT:</strong> ITIL te da el "cómo" atender solicitudes e incidentes (service desk, base de conocimiento); COBIT te da el "cómo gobernar" (roles RACI, objetivos de control). La IA genera borradores; el criterio de qué aplica en la UJMD es tuyo.''',
    d10title="LEAN: proceso medible y mejora continua",
    d10goal="Definir tu proceso candidato para la medición antes/después (modelo C19 de F1 + enfoque LEAN): un proceso repetitivo de tu puesto que puedas sistematizar con IA y medir en tiempo.",
    d10items=["Identifiqué 2 procesos repetitivos de mi puesto (ej.: responder consultas frecuentes por correo; registrar solicitudes; redactar respuestas a usuarios)","Con Gemini, describí el paso a paso de uno y el tiempo estimado actual (línea base)","Marqué los pasos que son desperdicio LEAN (esperas, reprocesos, tareas manuales)","Guardé la línea base en la plantilla de proceso medido"],
    d10fw='''<strong>Mejora continua (Kaizen):</strong> el ciclo PDCA (Plan-Do-Check-Act) es la base de LEAN: planifica el cambio (usar IA), hazlo, verifica el resultado medido y actúa ajustando. Tu medición antes/después es exactamente el "Check" de un ciclo PDCA.''',
    d10seg="los tiempos y pasos son tuyos — no incluyen datos de terceros. La plantilla de medición se comparte en Drive del programa sin datos personales.",
    d12title="Hermes con un caso real de la mesa de servicio",
    d12goal="Usar Hermes para una tarea real de tu área, entendiendo cuándo conviene cada herramienta: Gemini para redacción rápida en el navegador, Hermes para tareas ligadas a tu máquina y archivos locales.",
    d12items=["Le pedí a Hermes que redacte una respuesta corta a una consulta frecuente (misma regla de clasificación de datos)","Le pedí que liste qué archivos de una carpeta local puedo usar para documentar (sin abrir nada sensible)","Anoté cuándo usaría Gemini vs Hermes en mi trabajo diario"],
    d12fw='''<strong>Service desk + IA:</strong> imagina usar Hermes para consultar tus plantillas y generar respuestas consistentes a consultas frecuentes: la IA como apoyo de la base de conocimiento. Esa es la visión de nivel L3+.''',
    d13title="PRINCE2/agile: gestionar un proyecto con IA",
    d13goal="Combinar todo lo aprendido en un flujo completo: gestionar un mini-proyecto de tu área (ej.: mejorar una plantilla de respuestas, implementar una guía para usuarios, organizar la base de conocimiento) aplicando conceptos básicos de PRINCE2/agile, con IA como asistente y revisión humana en el cierre.",
    d13items=["Definí el alcance del mini-proyecto (qué se entregará y qué NO — gestión de alcance)","Con Gemini: desglosé el plan en fases con entregables, responsables y tiempos (PRINCE2 o pasos de un sprint agile)","Identifiqué riesgos del proyecto y su mitigación (con apoyo de IA y mi criterio)","Ejecuté el caso real de la Semana 2 (proceso medible del Día 10) y medí el tiempo CON IA vs línea base","Documenté el delta (ahorro de tiempo) en la plantilla"],
    d13fw='''<strong>PRINCE2/agile:</strong> PRINCE2 te da el control por fases con justificación continua; agile te da la entrega incremental. La IA acelera la documentación del plan; la decisión de fase y la aprobación de entregables la tomas tú con tu facilitador y Douglas.''',
    d13seg="verifica que el entregable final no contenga datos personales de usuarios. El entregable que se comparte en el programa es la versión anonimizada + la medición.",
    footer="Guía 14 Días · AI Fluency F2 · UJMD DSI · Betty Figueroa (Asistente a la Dirección de Informática y Mesa de Servicio) · Facilitador: Patrick Orellana · Marcos: ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile · 19/08/2026",
    file="guia_betty_figueroa.html"
),
"bryan": dict(
    nombre="Bryan Esaú Gómez Chacón", email="begomezch@ujmd.edu.sv", avatar="🛠️",
    rol="Soporte Técnico y Operador de Mesa de Servicio · UJMD",
    nivel="L1 · Pasajero 🟤", zona="Zona: Pasajero", meta="Meta: L2 — IA lee archivos del área",
    facilitador="Irvin Morales", facilitadorDesc="Champion F1 de Soporte/Mesa de Servicios",
    carpeta="Bryan", dominio="Soporte Técnico y Mesa de Servicio",
    promptA="redacta un correo sobre una incidencia de equipo",
    promptB='''"Eres soporte técnico de la DSI de la UJMD. Redacta una respuesta
profesional y empática para un usuario administrativo (no técnico) que
reportó que su computadora de escritorio no enciende desde esta
mañana. Incluye: saludo, 3 causas básicas que el usuario puede
verificar solo, y cómo escalar si no se resuelve."''',
    tipD1="tus casos típicos son atender solicitudes de soporte asignadas por el coordinador, diagnosticar fallas de equipos, instalar software y dar mantenimiento preventivo y correctivo.",
    marcoD1="el soporte técnico se apoya en ITIL 4 (gestión de incidentes y de solicitudes) y en la mejora continua con LEAN. A lo largo de la guía incorporarás ISO 27001 (datos personales), COBIT (control) y conceptos básicos de gestión de proyectos (agile/PRINCE2).",
    segD1="nunca pongas nombres reales de usuarios, datos de sus equipos (códigos de inventario), credenciales ni detalles de incidentes reales en los prompts. Usa descripciones genéricas. Esto respeta la protección de datos personales y la propiedad intelectual de la universidad.",
    d2prompts=['''1. "Eres soporte técnico de la DSI de la UJMD. Redacta una guía de
   diagnóstico rápido para una computadora que no enciende: pasos que
   el usuario puede hacer solo, y qué verificar el técnico. Lenguaje
   claro, no técnico para el usuario."''',
'''2. "Eres soporte técnico. Escribe un procedimiento breve de atención
   de una incidencia (estructura ITIL de gestión de incidentes):
   recepción → diagnóstico → solución o escalamiento → cierre →
   registro. Deja espacios para responsables y tiempos."''',
'''3. "Eres soporte técnico y operador de mesa de servicio. Redacta una
   plantilla de respuesta para consultas frecuentes (contraseña,
   correo, wifi, impresión), con tono amable y claro. Deja espacios
   para personalizar cada caso."'''],
    d2fw='''<strong>ITIL incident management:</strong> la atención de incidencias sigue la práctica de gestión de incidentes de ITIL 4 (restaurar el servicio lo antes posible). La IA redacta guías y plantillas; el diagnóstico técnico y la decisión de escalar son tuyos.''',
    d2seg="las respuestas NO llevan datos personales de los usuarios — los agregas tú al personalizar cada caso en los sistemas oficiales.",
    d2evid=["3 respuestas de Gemini guardadas en tu Google Doc de evidencia","Anotación de qué prompt dio el mejor resultado y por qué"],
    d6intro="Tu tabla personal de clasificación de información de soporte técnico — el instrumento que usarás toda la fase (y que el programa exige como evidencia de manejo responsable). Se apoya en el control de clasificación de activos de ISO/IEC 27001 y en la política de seguridad de la universidad.",
    d6tabla=[("Guías y procedimientos de diagnóstico","Interno","✅ Sí (sin códigos de inventario)","—"),
             ("Registro de incidencias atendidas","Confidencial","❌ No (tienen datos de usuarios)","Trabajar en los sistemas oficiales"),
             ("Datos personales de usuarios","Confidencial","❌ No","Nunca en IA"),
             ("Credenciales o contraseñas","Restringido","❌ Nunca","Gestor de contraseñas institucional"),
             ("Inventario de equipos","Interno","✅ Sí (anonimizado)","—"),
             ("Plantillas de comunicación con usuarios","Interno","✅ Sí","—")],
    d6fw='''<strong>Referencias:</strong> la clasificación de activos es un control de ISO/IEC 27001 (A.5.9 y A.5.12); la protección de datos personales sigue los principios internacionales de consentimiento, finalidad y minimización; la propiedad intelectual y confidencialidad institucional se rige por la normativa de la universidad.''',
    d7title="Caso real de tu puesto: guía o procedimiento de soporte",
    d7goal="Completar tu primer caso real completo: un documento de tu área de soporte (guía de diagnóstico, procedimiento de atención, plantilla de respuesta), de principio a fin, con la IA como asistente y tu criterio como responsable.",
    d7items=["Elegí un documento real que necesito producir (guía de diagnóstico, procedimiento de atención, plantilla de respuesta)","Redacté el borrador con Gemini usando rol + tarea + contexto","Refiné al menos 2 veces hasta quedar conforme","Revisé y corregí yo mismo el resultado (la IA redacta, yo valido)","Guardé versión final + registro del proceso (prompt usado, refinamientos)"],
    d7fw='''<strong>Enfoque LEAN:</strong> al documentar tu procedimiento, identifica qué pasos actuales son desperdicio (esperas, reprocesos, traslados innecesarios) y márcalos. El programa medirá el antes/después: ese es el corazón de la mejora continua con LEAN.''',
    d7seg="verifica que el documento final no contenga datos personales de usuarios. La revisión humana final es obligatoria — la IA no firma, tú sí.",
    d9title="Semana 2: ITIL y COBIT con apoyo de IA",
    d9goal="Usar la IA para documentar y mejorar las prácticas de soporte (ITIL 4: gestión de incidentes y de solicitudes) y de control (COBIT 2019), aplicadas a tu trabajo diario en la mesa de servicio.",
    d9items=["Elegí una práctica de soporte (gestión de incidentes, gestión de solicitudes, base de conocimiento)","Pedí a Gemini: \"describe cómo implementar esta práctica en la mesa de servicio de una universidad, con roles y pasos\"","Pedí: \"convierte esto en una tabla de responsabilidades (RACI) según COBIT\"","Evalué críticamente: ¿qué aplica a mi realidad y qué no?"],
    d9fw='''<strong>ITIL + COBIT:</strong> ITIL te da el "cómo" atender incidentes y solicitudes; COBIT te da el "cómo gobernar" (roles RACI, objetivos de control). La IA genera borradores; el criterio de qué aplica en la UJMD es tuyo.''',
    d10title="LEAN: proceso medible y mejora continua",
    d10goal="Definir tu proceso candidato para la medición antes/después (modelo C19 de F1 + enfoque LEAN): un proceso repetitivo de tu puesto que puedas sistematizar con IA y medir en tiempo.",
    d10items=["Identifiqué 2 procesos repetitivos de mi puesto (ej.: redactar respuestas a incidencias; registrar solicitudes; elaborar reportes de atención)","Con Gemini, describí el paso a paso de uno y el tiempo estimado actual (línea base)","Marqué los pasos que son desperdicio LEAN (esperas, reprocesos, tareas manuales)","Guardé la línea base en la plantilla de proceso medido"],
    d10fw='''<strong>Mejora continua (Kaizen):</strong> el ciclo PDCA (Plan-Do-Check-Act) es la base de LEAN: planifica el cambio (usar IA), hazlo, verifica el resultado medido y actúa ajustando. Tu medición antes/después es exactamente el "Check" de un ciclo PDCA.''',
    d10seg="los tiempos y pasos son tuyos — no incluyen datos de terceros. La plantilla de medición se comparte en Drive del programa sin datos personales.",
    d12title="Hermes con un caso real de soporte",
    d12goal="Usar Hermes para una tarea real de tu área, entendiendo cuándo conviene cada herramienta: Gemini para redacción rápida en el navegador, Hermes para tareas ligadas a tu máquina y archivos locales.",
    d12items=["Le pedí a Hermes que redacte una guía corta de diagnóstico (misma regla de clasificación de datos)","Le pedí que liste qué archivos de una carpeta local puedo usar para documentar (sin abrir nada sensible)","Anoté cuándo usaría Gemini vs Hermes en mi trabajo diario"],
    d12fw='''<strong>Soporte + IA:</strong> imagina usar Hermes para consultar tus procedimientos y generar respuestas consistentes a incidencias frecuentes: la IA como apoyo de tu base de conocimiento. Esa es la visión de nivel L3+.''',
    d13title="PRINCE2/agile: gestionar un proyecto con IA",
    d13goal="Combinar todo lo aprendido en un flujo completo: gestionar un mini-proyecto de tu área (ej.: crear una guía de diagnóstico para el equipo, organizar plantillas de respuesta, implementar un procedimiento de atención) aplicando conceptos básicos de PRINCE2/agile, con IA como asistente y revisión humana en el cierre.",
    d13items=["Definí el alcance del mini-proyecto (qué se entregará y qué NO — gestión de alcance)","Con Gemini: desglosé el plan en fases con entregables, responsables y tiempos (PRINCE2 o pasos de un sprint agile)","Identifiqué riesgos del proyecto y su mitigación (con apoyo de IA y mi criterio)","Ejecuté el caso real de la Semana 2 (proceso medible del Día 10) y medí el tiempo CON IA vs línea base","Documenté el delta (ahorro de tiempo) en la plantilla"],
    d13fw='''<strong>PRINCE2/agile:</strong> PRINCE2 te da el control por fases con justificación continua; agile te da la entrega incremental. La IA acelera la documentación del plan; la decisión de fase y la aprobación de entregables la tomas tú con tu facilitador y Douglas.''',
    d13seg="verifica que el entregable final no contenga datos personales de usuarios. El entregable que se comparte en el programa es la versión anonimizada + la medición.",
    footer="Guía 14 Días · AI Fluency F2 · UJMD DSI · Bryan Gómez (Soporte Técnico y Operador de Mesa de Servicio) · Facilitador: Irvin Morales · Marcos: ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile · 19/08/2026",
    file="guia_bryan_gomez.html"
),
"oscar": dict(
    nombre="Oscar Javier Alfaro Barrera", email="ojalfarob@ujmd.edu.sv", avatar="👨‍💻",
    rol="Programador Analista · Dirección de Informática · UJMD",
    nivel="L1 · Pasajero 🟤", zona="Zona: Pasajero", meta="Meta: L2 — IA lee archivos del área",
    facilitador="Mario Valencia", facilitadorDesc="Champion F1 de Desarrollo",
    carpeta="Oscar", dominio="Desarrollo de Software",
    promptA="redacta un correo sobre el avance de un desarrollo",
    promptB='''"Eres programador analista de la DSI de la UJMD. Redacta un correo
interno para tu coordinadora informando el avance del desarrollo que
estás trabajando (módulo completado, pruebas en curso, pendiente de
revisión). Tono: profesional, claro, con una sección de próximos
pasos."''',
    tipD1="tus casos típicos son desarrollar y mantener sistemas, documentar código y funcionalidades, resolver correcciones y preparar entregas para revisión.",
    marcoD1="el desarrollo de software se apoya en agile/SCRUM (entregas incrementales) y en el SDLC seguro (ISO 27001/OWASP), con ITIL para la gestión de cambios en producción y COBIT para el control. A lo largo de la guía incorporarás estos marcos, más LEAN (mejora continua) y PRINCE2.",
    segD1="nunca pongas datos personales de estudiantes (notas, listas), credenciales, fragmentos de código sensible ni datos de sistemas en producción en los prompts. Usa descripciones genéricas. Esto respeta la protección de datos personales y la propiedad intelectual de la universidad.",
    d2prompts=['''1. "Eres programador analista de la DSI de la UJMD. Redacta una
   lista de verificación para la entrega de un módulo de un sistema:
   código completo, documentación, pruebas, despliegue. Formato:
   checklist con criterio OK/PENDIENTE."''',
'''2. "Eres programador analista. Escribe un procedimiento breve para
   solicitar un cambio en un sistema en producción (estructura ITIL
   de gestión de cambios): solicitud → evaluación → aprobación →
   implementación → verificación → cierre. Deja espacios para
   responsables y fechas."''',
'''3. "Eres programador analista. Redacta una minuta de avance semanal
   de tus tareas de desarrollo (módulos en curso, correcciones,
   documentación), con prioridad alta/media/baja. Deja espacios en
   blanco para nombres y fechas."'''],
    d2fw='''<strong>Agile + ITIL:</strong> la minuta de avance puede estructurarse como un sprint de SCRUM (tareas del backlog); el procedimiento de cambios sigue la gestión de cambios de ITIL (aplicable a producción). La IA redacta; el criterio técnico y las prioridades son tuyos.''',
    d2seg="la minuta NO lleva nombres reales de compañeros ni detalles de sistemas en producción — los agregas tú después en el documento oficial.",
    d2evid=["3 respuestas de Gemini guardadas en tu Google Doc de evidencia","Anotación de qué prompt dio el mejor resultado y por qué"],
    d6intro="Tu tabla personal de clasificación de información de desarrollo — el instrumento que usarás toda la fase (y que el programa exige como evidencia de manejo responsable). Se apoya en el control de clasificación de activos de ISO/IEC 27001 y en la política de seguridad de la universidad.",
    d6tabla=[("Documentación de módulos y funcionalidades","Interno","✅ Sí (fragmentos genéricos)","—"),
             ("Código fuente","Interno","⚠️ Solo fragmentos genéricos","Describir patrones sin código sensible"),
             ("Datos de estudiantes (notas, listas, SIED)","Confidencial","❌ No","Nunca en IA"),
             ("Credenciales o accesos a producción","Restringido","❌ Nunca","Gestor de contraseñas institucional"),
             ("Requerimientos de negocio","Interno","✅ Sí (anonimizados)","—"),
             ("Incidentes de producción reales","Restringido","❌ No (solo anonimizado)","Usar caso ficticio equivalente")],
    d6fw='''<strong>Referencias:</strong> la clasificación de activos es un control de ISO/IEC 27001 (A.5.9 y A.5.12); el desarrollo seguro de software sigue los principios del SDLC seguro (OWASP); la propiedad intelectual del código pertenece a la universidad y su uso con IA debe preservar la confidencialidad.''',
    d7title="Caso real de tu puesto: documentación técnica o minuta",
    d7goal="Completar tu primer caso real completo: un documento de tu área de desarrollo (documentación de un módulo, minuta de avance, procedimiento de cambio), de principio a fin, con la IA como asistente y tu criterio como responsable.",
    d7items=["Elegí un documento real que necesito producir (documentación de módulo, minuta de avance, procedimiento de cambio)","Redacté el borrador con Gemini usando rol + tarea + contexto","Refiné al menos 2 veces hasta quedar conforme","Revisé y corregí yo mismo el resultado (la IA redacta, yo valido)","Guardé versión final + registro del proceso (prompt usado, refinamientos)"],
    d7fw='''<strong>Enfoque LEAN:</strong> al documentar tu proceso de desarrollo, identifica qué pasos actuales son desperdicio (esperas de revisión, reprocesos, documentación manual repetitiva) y márcalos. El programa medirá el antes/después: ese es el corazón de la mejora continua con LEAN.''',
    d7seg="verifica que el documento final no contenga datos personales ni fragmentos de código sensible. La revisión humana final es obligatoria — la IA no firma, tú sí.",
    d9title="Semana 2: agile/SCRUM e ITIL con apoyo de IA",
    d9goal="Usar la IA para documentar y mejorar tu trabajo de desarrollo: estructura de sprints (SCRUM), gestión de requerimientos y gestión de cambios en producción (ITIL), con gobierno de TI (COBIT).",
    d9items=["Elegí una práctica de mi área (planificación de sprint, documentación de requerimientos o gestión de cambios ITIL)","Pedí a Gemini: \"describe cómo estructurar esta práctica en un equipo de desarrollo universitario, con roles y pasos\"","Pedí: \"convierte esto en una tabla de responsabilidades (RACI) según COBIT\"","Evalué críticamente: ¿qué aplica a mi realidad y qué no?"],
    d9fw='''<strong>Agile + ITIL + COBIT:</strong> SCRUM te da la entrega incremental; ITIL te da la gestión de cambios en producción; COBIT te da el gobierno (roles RACI). La IA genera borradores; el criterio de qué aplica en la UJMD es tuyo.''',
    d10title="LEAN: proceso medible y mejora continua",
    d10goal="Definir tu proceso candidato para la medición antes/después (modelo C19 de F1 + enfoque LEAN): un proceso repetitivo de tu puesto que puedas sistematizar con IA y medir en tiempo.",
    d10items=["Identifiqué 2 procesos repetitivos de mi puesto (ej.: documentar módulos; preparar minutas de avance; escribir comentarios de código)","Con Gemini, describí el paso a paso de uno y el tiempo estimado actual (línea base)","Marqué los pasos que son desperdicio LEAN (esperas, reprocesos, tareas manuales)","Guardé la línea base en la plantilla de proceso medido"],
    d10fw='''<strong>Mejora continua (Kaizen):</strong> el ciclo PDCA (Plan-Do-Check-Act) es la base de LEAN: planifica el cambio (usar IA), hazlo, verifica el resultado medido y actúa ajustando. Tu medición antes/después es exactamente el "Check" de un ciclo PDCA.''',
    d10seg="los tiempos y pasos son tuyos — no incluyen datos de terceros. La plantilla de medición se comparte en Drive del programa sin datos personales.",
    d12title="Hermes con un caso real de desarrollo",
    d12goal="Usar Hermes para una tarea real de tu área, entendiendo cuándo conviene cada herramienta: Gemini para redacción rápida en el navegador, Hermes para tareas ligadas a tu máquina y archivos locales.",
    d12items=["Le pedí a Hermes que redacte una documentación corta de un módulo (misma regla de clasificación de datos)","Le pedí que liste qué archivos de una carpeta local puedo usar para documentar (sin abrir nada sensible)","Anoté cuándo usaría Gemini vs Hermes en mi trabajo diario"],
    d12fw='''<strong>Desarrollo + IA:</strong> imagina usar Hermes para documentar módulos y generar minutas de avance con formato estándar: la IA como apoyo de tu flujo de desarrollo. Esa es la visión de nivel L3+.''',
    d13title="PRINCE2/agile: gestionar un proyecto con IA",
    d13goal="Combinar todo lo aprendido en un flujo completo: gestionar un mini-proyecto de tu área (ej.: implementación de un módulo, mejora de un proceso de desarrollo, creación de una documentación técnica) aplicando conceptos de PRINCE2/agile, con IA como asistente y revisión humana en el cierre.",
    d13items=["Definí el alcance del mini-proyecto (qué se entregará y qué NO — gestión de alcance)","Con Gemini: desglosé el plan en fases con entregables, responsables y tiempos (PRINCE2 o sprint agile)","Identifiqué riesgos del proyecto y su mitigación (con apoyo de IA y mi criterio)","Ejecuté el caso real de la Semana 2 (proceso medible del Día 10) y medí el tiempo CON IA vs línea base","Documenté el delta (ahorro de tiempo) en la plantilla"],
    d13fw='''<strong>PRINCE2/agile:</strong> PRINCE2 te da el control por fases con justificación continua y gestión de riesgos; agile te da la entrega incremental (sprints). La IA acelera la documentación del plan; la decisión de fase y la aprobación de entregables la tomas tú con tu coordinadora y facilitador.''',
    d13seg="verifica que el entregable final no contenga datos personales ni código sensible. El entregable que se comparte en el programa es la versión anonimizada + la medición.",
    footer="Guía 14 Días · AI Fluency F2 · UJMD DSI · Oscar Alfaro (Programador Analista) · Facilitador: Mario Valencia · Marcos: ITIL, COBIT, ISO 27001, LEAN, PRINCE2/agile · 19/08/2026",
    file="guia_oscar_alfaro.html"
),
}

# ---------- Dias 2, 6, 7, 9, 10, 12, 13 (personalizados) ----------
def d2(p):
    pre = "".join("<p><strong>"+("Prompt " if False else "")+"</strong></p>" + f"<pre>{x}</pre>" for x in p["d2prompts"])
    # mejor: numerar
    prompts = "".join(f"<pre>{x}</pre>" for x in p["d2prompts"])
    return day(2, "Día 2 · Lección 1 (práctica)", "3 prompts reales de tu puesto", "45 min · Gemini",
        concept("Objetivo", "Aplicar la estructura rol + tarea + contexto a 3 tareas reales de tu puesto ("+p["rol"].split("·")[0].strip()+").")
        + '<h3>Práctica</h3><p>Crea y ejecuta estos 3 prompts en Gemini (personalízalos con tus datos reales, sin información sensible):</p>' + prompts
        + alert("framework", p["d2fw"])
        + alert("security", "<strong>Regla:</strong> "+p["d2seg"])
        + evidence(p["d2evid"]),
        1, 3)

def d6(p):
    filas = "".join(
        f'<tr><td style="padding:8px;border-bottom:1px solid #ffffff12;">{a}</td><td style="padding:8px;border-bottom:1px solid #ffffff12;">{b}</td><td style="padding:8px;border-bottom:1px solid #ffffff12;">{c}</td><td style="padding:8px;border-bottom:1px solid #ffffff12;">{d}</td></tr>'
        for a,b,c,d in p["d6tabla"])
    tabla = f'''<table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:.85rem;">
    <tr style="background:#ffffff10;"><th style="padding:8px;text-align:left;color:#00e5ff;">Activo de información de mi área</th><th style="padding:8px;text-align:left;color:#00e5ff;">Clasificación</th><th style="padding:8px;text-align:left;color:#00e5ff;">¿Se comparte con IA?</th><th style="padding:8px;text-align:left;color:#00e5ff;">Alternativa segura</th></tr>
    {filas}
  </table>'''
    return day(6, "Día 6 · Lección 3 (práctica)", "Clasificación de activos de información (ISO 27001)", "45 min · Google Docs",
        concept("Objetivo", p["d6intro"])
        + '<h3>Práctica — crea la tabla en un Google Doc</h3>' + tabla
        + '<p>Completa la tabla con al menos 6 filas propias de tu puesto y guárdala como evidencia.</p>'
        + alert("framework", p["d6fw"])
        + evidence(["Tu tabla de clasificación de activos de información completada (Google Doc)"]),
        5, 7)

def d7(p):
    items = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in p["d7items"])
    return day(7, "Día 7 · Lección 4", p["d7title"], "60 min · Gemini + Google Docs",
        concept("Objetivo", p["d7goal"])
        + '<h3>Actividad integradora (Semana 1)</h3>'
        + f'<ul class="checklist">{items}</ul>'
        + alert("framework", p["d7fw"])
        + alert("security", "<strong>Antes de publicar:</strong> "+p["d7seg"])
        + evidence(["Documento final del procedimiento/política","Registro del proceso: prompt inicial + refinamientos + tiempo invertido","Nota LEAN: pasos identificados como desperdicio a mejorar"]),
        6, 8)

def d9(p):
    items = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in p["d9items"])
    return day(9, "Día 9 · Lección 5", p["d9title"], "45 min · Gemini + Google Docs",
        concept("Objetivo", p["d9goal"])
        + '<h3>Práctica</h3>'
        + f'<ul class="checklist">{items}</ul>'
        + alert("framework", p["d9fw"])
        + evidence(["Borrador de la práctica + matriz RACI COBIT generados","Tu evaluación de aplicabilidad en la UJMD"]),
        8, 10)

def d10(p):
    items = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in p["d10items"])
    return day(10, "Día 10 · Lección 5 (práctica)", p["d10title"], "60 min · Gemini + plantilla de proceso medido",
        concept("Objetivo", p["d10goal"])
        + '<h3>Actividad</h3>'
        + f'<ul class="checklist">{items}</ul>'
        + alert("framework", p["d10fw"])
        + alert("security", "<strong>Datos de la medición:</strong> "+p["d10seg"])
        + evidence(["2 procesos candidatos identificados con sus desperdicios LEAN","Línea base del proceso elegido (plantilla C19/F2)"]),
        9, 11)

def d12(p):
    items = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in p["d12items"])
    return day(12, "Día 12 · Lección 6 (práctica)", p["d12title"], "45 min · Hermes Agent",
        concept("Objetivo", p["d12goal"])
        + '<h3>Práctica</h3>'
        + f'<ul class="checklist">{items}</ul>'
        + alert("framework", p["d12fw"])
        + evidence(["Respuesta de Hermes a tu caso real","Tu criterio documentado: Gemini vs Hermes, cuándo cada uno"]),
        11, 13)

def d13(p):
    items = "".join(f'<li onclick="toggle(this)"><div class="check-box"></div>{i}</li>' for i in p["d13items"])
    return day(13, "Día 13 · Lección 7", p["d13title"], "60 min · Gemini + Hermes + Google Docs",
        concept("Objetivo", p["d13goal"])
        + '<h3>Actividad integradora (Semana 2)</h3>'
        + f'<ul class="checklist">{items}</ul>'
        + alert("framework", p["d13fw"])
        + alert("security", "<strong>Cierre seguro:</strong> "+p["d13seg"])
        + evidence(["Plan del mini-proyecto (fases, entregables, riesgos)","Entregable final de tu caso real + medición antes/después con delta"]),
        12, 14)

def build(p):
    body = "".join([
        d1(p), d2(p), d3(p), d4(p), d5(p), d6(p), d7(p), d8(p),
        d9(p), d10(p), d11(p), d12(p), d13(p), d14(p)
    ])
    tags = f'''        <span class="tag cyan">{p["nivel"]}</span>
        <span class="tag">{p["zona"]}</span>
        <span class="tag green">{p["meta"]}</span>
        <span class="tag purple">Facilitador: {p["facilitador"]}</span>
        <span class="tag red">Dominio: {p["dominio"]}</span>
        <span class="tag">Herramientas: Gemini (principal) + Hermes (complemento)</span>'''
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Guía 14 Días · {p["nombre"]} · AI Fluency F2 UJMD</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

<div class="site-header">
  <a class="back-link" href="index.html">← Inicio</a>
  <span class="hbadge">🎓 Guía 14 Días · AI Fluency F2</span>
</div>

<div class="security-banner">
  <strong style="color:#fb7185;">🔒 Tema transversal de esta guía: SEGURIDAD DE LA INFORMACIÓN.</strong>
  Todas las lecciones incorporan el manejo responsable de información: protección de datos personales de estudiantes y propiedad intelectual de la universidad, con marcos de buenas prácticas (ITIL, COBIT, ISO/IEC 27001, LEAN y PRINCE2/agile). Las reglas aplican SIEMPRE, con Gemini, Hermes o cualquier herramienta.
</div>

<div class="champion-card">
  <div class="champion-inner">
    <div class="avatar">{p["avatar"]}</div>
    <div class="champion-info">
      <h1>{p["nombre"]}</h1>
      <div class="role">{p["rol"]}</div>
      <div class="tags">
{tags}
      </div>
    </div>
  </div>
</div>

<div class="prog-section">
  <div class="prog-inner">
{tabs_html()}
  </div>
</div>

<div class="content">
{body}
</div>

<footer>{p["footer"]}</footer>

<script>
function showDay(n){{
  document.querySelectorAll('.day-panel').forEach(function(p){{p.classList.remove('active');}});
  document.getElementById('day-'+n).classList.add('active');
  document.querySelectorAll('.day-tab').forEach(function(t,i){{t.classList.toggle('active', i===n-1);}});
  window.scrollTo({{top:0,behavior:'smooth'}});
}}
function toggle(li){{li.classList.toggle('checked');}}
</script>
</body>
</html>'''
    return html

for key, p in P.items():
    html = build(p)
    path = os.path.join(OUT, p["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    # verificaciones
    checks = []
    checks.append(("nombre", p["nombre"] in html))
    checks.append(("facilitador", p["facilitador"] in html))
    checks.append(("rol", p["rol"].split("·")[0].strip() in html))
    checks.append(("14 dias", html.count('class="day-panel') == 14))
    checks.append(("sin placeholders", "{{" not in html and "}}" not in html))
    checks.append(("cierre html", html.rstrip().endswith("</html>")))
    bad = [c for c, ok in checks if not ok]
    print(f"{p['file']}: {len(html)} bytes | {'OK' if not bad else 'FALLO: '+str(bad)}")
