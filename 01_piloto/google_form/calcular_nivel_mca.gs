/**
 * ============================================================
 *  AI Fluency · MCA — Calculadora de Nivel e Itinerario
 * ============================================================
 *  Versión: 1.0 | Autor: @untaldouglas | UJMD · 2026
 *
 *  Cómo usar:
 *  1. Abre el Google Sheet vinculado a tu Google Form de diagnóstico
 *  2. Ve a Extensiones → Apps Script
 *  3. Pega este código completo y guarda (Ctrl+S)
 *  4. Ejecuta calcularNivelesMCA() desde el menú "▶ Ejecutar"
 *     o usa el menú personalizado que aparece en el Sheet
 *
 *  Qué genera:
 *  - Hoja "NIVELES_MCA":     nivel L0-L9, licencia, zona, score por participante
 *  - Hoja "ITINERARIOS":     plan de aprendizaje personalizado (metodología Teach)
 *  - Hoja "RESUMEN_GRUPO":   agregados, bloqueos comunes, recomendaciones
 * ============================================================
 */

// ─── CONFIGURACIÓN ───────────────────────────────────────────
const CONFIG = {
  // Nombre de la hoja con respuestas del Form (ajusta si es diferente)
  HOJA_RESPUESTAS: "Respuestas de formulario 1",

  // Columnas de nivel L0–L8 (1-indexadas, según Estructura_Columnas.md)
  COL_L0:  14,  // "Uso chatbots como buscador rápido"
  COL_L1A: 15,  // "Doy contexto adicional"
  COL_L1B: 16,  // "La IA me recuerda cosas"
  COL_L2:  17,  // "Hago que la IA lea archivos"
  COL_L3:  18,  // "Tengo espacio de IA con conocimiento fijo"
  COL_L4:  19,  // "La IA se conecta a herramientas"
  COL_L5:  20,  // "He definido flujos reutilizables"
  COL_L6:  21,  // "Delego tareas completas a la IA"
  COL_L7:  22,  // "La IA ejecuta comandos / navega"
  COL_L8:  23,  // "He programado agentes autónomos"

  // Columnas de bloqueos (escala 0-3)
  COL_BLQ_TIEMPO:    24,
  COL_BLQ_TECNICO:   25,
  COL_BLQ_CONFIANZA: 26,
  COL_BLQ_SEGURIDAD: 27,
  COL_BLQ_ACCESO:    28,
  COL_BLQ_SOPORTE:   29,
  COL_BLQ_CULTURA:   30,

  // Columnas de datos personales
  COL_NOMBRE:   2,
  COL_CORREO:   3,
  COL_AREA:     4,
  COL_ROL:      5,
  COL_HERRAMIENTAS: 7,
  COL_ENSENARIA:   34,
  COL_FORMATO:     36,
};

const NOMBRES_BLOQUEOS = [
  "Tiempo", "Conocimiento técnico", "Confianza",
  "Seguridad/Privacidad", "Acceso/Permisos", "Soporte", "Cultura"
];

// ─── MENÚ PERSONALIZADO ──────────────────────────────────────
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu("🚗 MCA · AI Fluency")
    .addItem("Calcular niveles e itinerarios", "calcularNivelesMCA")
    .addItem("Solo regenerar itinerarios", "regenerarItinerarios")
    .addSeparator()
    .addItem("Exportar resumen de grupo", "exportarResumenGrupo")
    .addToUi();
}

// ─── FUNCIÓN PRINCIPAL ───────────────────────────────────────
function calcularNivelesMCA() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const hojaResp = ss.getSheetByName(CONFIG.HOJA_RESPUESTAS);

  if (!hojaResp) {
    SpreadsheetApp.getUi().alert(
      `⚠️ No se encontró la hoja "${CONFIG.HOJA_RESPUESTAS}".\n` +
      "Verifica el nombre exacto de la hoja con respuestas del Form."
    );
    return;
  }

  const datos = hojaResp.getDataRange().getValues();
  if (datos.length < 2) {
    SpreadsheetApp.getUi().alert("⚠️ No hay respuestas aún en el formulario.");
    return;
  }

  const participantes = [];

  // Procesar cada fila (omitir encabezado)
  for (let i = 1; i < datos.length; i++) {
    const fila = datos[i];
    if (!fila[CONFIG.COL_NOMBRE - 1]) continue; // fila vacía

    const p = extraerParticipante(fila, i + 1);
    participantes.push(p);
  }

  if (participantes.length === 0) {
    SpreadsheetApp.getUi().alert("⚠️ No se encontraron participantes con datos completos.");
    return;
  }

  crearHojaNiveles(ss, participantes);
  crearHojaItinerarios(ss, participantes);
  crearHojaResumenGrupo(ss, participantes);

  SpreadsheetApp.getUi().alert(
    `✅ Proceso completado.\n\n` +
    `Participantes procesados: ${participantes.length}\n\n` +
    `Hojas generadas:\n` +
    `  • NIVELES_MCA\n` +
    `  • ITINERARIOS\n` +
    `  • RESUMEN_GRUPO`
  );
}

// ─── EXTRACCIÓN Y CÁLCULO ────────────────────────────────────
function extraerParticipante(fila, numFila) {
  const get = (col) => fila[col - 1] || 0;
  const getText = (col) => (fila[col - 1] || "").toString().trim();

  // Scores por nivel (L1 = max de L1a y L1b)
  const scores = {
    L0: parseFloat(get(CONFIG.COL_L0)) || 0,
    L1: Math.max(parseFloat(get(CONFIG.COL_L1A)) || 0, parseFloat(get(CONFIG.COL_L1B)) || 0),
    L2: parseFloat(get(CONFIG.COL_L2)) || 0,
    L3: parseFloat(get(CONFIG.COL_L3)) || 0,
    L4: parseFloat(get(CONFIG.COL_L4)) || 0,
    L5: parseFloat(get(CONFIG.COL_L5)) || 0,
    L6: parseFloat(get(CONFIG.COL_L6)) || 0,
    L7: parseFloat(get(CONFIG.COL_L7)) || 0,
    L8: parseFloat(get(CONFIG.COL_L8)) || 0,
  };

  const sumatoria = Object.values(scores).reduce((a, b) => a + b, 0);

  // Nivel dominante: el nivel con puntuación más alta (en caso de empate, el mayor)
  let nivelDominante = "L0";
  let maxScore = -1;
  for (const [nivel, score] of Object.entries(scores)) {
    if (score > maxScore || (score === maxScore && parseInt(nivel.slice(1)) > parseInt(nivelDominante.slice(1)))) {
      maxScore = score;
      nivelDominante = nivel;
    }
  }

  // Zona según sumatoria
  let zona, licencia, emoji;
  if (sumatoria <= 20) {
    zona = "Pasajero";
    licencia = "🟤 Permiso de Aprendizaje";
  } else if (sumatoria <= 35) {
    zona = "Conductor";
    licencia = "🟢 Licencia Básica";
    if (sumatoria > 28) licencia = "🔵 Licencia Profesional";
  } else {
    zona = "Piloto Automático";
    licencia = "🟣 Licencia Avanzada";
    if (sumatoria >= 45) licencia = "🏆 Instructor de Conducción";
  }

  // Refinamiento de licencia según nivel dominante
  const numNivel = parseInt(nivelDominante.slice(1));
  if (numNivel <= 1)      licencia = "🟤 Permiso de Aprendizaje";
  else if (numNivel <= 3) licencia = "🟢 Licencia Básica";
  else if (numNivel <= 5) licencia = "🔵 Licencia Profesional";
  else if (numNivel <= 7) licencia = "🟣 Licencia Avanzada";
  else                    licencia = "🏆 Instructor de Conducción";

  // Bloqueos
  const bloqueosCols = [
    CONFIG.COL_BLQ_TIEMPO, CONFIG.COL_BLQ_TECNICO, CONFIG.COL_BLQ_CONFIANZA,
    CONFIG.COL_BLQ_SEGURIDAD, CONFIG.COL_BLQ_ACCESO, CONFIG.COL_BLQ_SOPORTE,
    CONFIG.COL_BLQ_CULTURA
  ];
  const bloqueos = bloqueosCols.map((col, i) => ({
    nombre: NOMBRES_BLOQUEOS[i],
    valor: parseFloat(get(col)) || 0
  }));

  const bloqueoMaximo = bloqueos.reduce((a, b) => b.valor > a.valor ? b : a);
  const bloqueosAltos = bloqueos.filter(b => b.valor >= 2).map(b => b.nombre);

  return {
    fila: numFila,
    nombre: getText(CONFIG.COL_NOMBRE),
    correo: getText(CONFIG.COL_CORREO),
    area: getText(CONFIG.COL_AREA),
    rol: getText(CONFIG.COL_ROL),
    herramientas: getText(CONFIG.COL_HERRAMIENTAS),
    formatoPreferido: getText(CONFIG.COL_FORMATO),
    ensenaria: getText(CONFIG.COL_ENSENARIA),
    scores,
    sumatoria,
    nivelDominante,
    zona,
    licencia,
    bloqueos,
    bloqueoMaximo,
    bloqueosAltos,
  };
}

// ─── HOJA: NIVELES_MCA ───────────────────────────────────────
function crearHojaNiveles(ss, participantes) {
  let hoja = ss.getSheetByName("NIVELES_MCA");
  if (hoja) ss.deleteSheet(hoja);
  hoja = ss.insertSheet("NIVELES_MCA");

  // Encabezados
  const headers = [
    "Nombre", "Correo", "Área", "Rol",
    "L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8",
    "Sumatoria", "Nivel Dominante", "Zona", "Licencia",
    "Bloqueo Principal", "Bloqueos Altos (≥2)"
  ];

  hoja.getRange(1, 1, 1, headers.length).setValues([headers]);
  hoja.getRange(1, 1, 1, headers.length)
    .setBackground("#0A2540")
    .setFontColor("#FFFFFF")
    .setFontWeight("bold");

  // Datos
  const filas = participantes.map(p => [
    p.nombre, p.correo, p.area, p.rol,
    p.scores.L0, p.scores.L1, p.scores.L2, p.scores.L3, p.scores.L4,
    p.scores.L5, p.scores.L6, p.scores.L7, p.scores.L8,
    p.sumatoria, p.nivelDominante, p.zona, p.licencia,
    p.bloqueoMaximo.nombre + " (" + p.bloqueoMaximo.valor + "/3)",
    p.bloqueosAltos.join(", ") || "Ninguno"
  ]);

  if (filas.length > 0) {
    hoja.getRange(2, 1, filas.length, headers.length).setValues(filas);
  }

  // Color por zona
  participantes.forEach((p, i) => {
    const fila = i + 2;
    let color;
    if (p.zona === "Pasajero")          color = "#FFF3CD";
    else if (p.zona === "Conductor")    color = "#D4EDDA";
    else                                color = "#CCE5FF";
    hoja.getRange(fila, 1, 1, headers.length).setBackground(color);
  });

  hoja.autoResizeColumns(1, headers.length);
  hoja.setFrozenRows(1);
}

// ─── HOJA: ITINERARIOS ───────────────────────────────────────
function crearHojaItinerarios(ss, participantes) {
  let hoja = ss.getSheetByName("ITINERARIOS");
  if (hoja) ss.deleteSheet(hoja);
  hoja = ss.insertSheet("ITINERARIOS");

  const headers = [
    "Nombre", "Área", "Nivel Actual", "Licencia",
    "Objetivo Mes 1", "Semana 1–2", "Semana 3–4",
    "Hito de Nivel", "Bloqueo a trabajar", "Formato sugerido",
    "Herramienta de entrada", "Caso de uso ancla"
  ];

  hoja.getRange(1, 1, 1, headers.length).setValues([headers]);
  hoja.getRange(1, 1, 1, headers.length)
    .setBackground("#0A2540")
    .setFontColor("#FFFFFF")
    .setFontWeight("bold");

  const filas = participantes.map(p => generarItinerario(p));

  if (filas.length > 0) {
    hoja.getRange(2, 1, filas.length, headers.length).setValues(filas);
  }

  hoja.autoResizeColumns(1, headers.length);
  hoja.setFrozenRows(1);
}

// ─── GENERADOR DE ITINERARIO (METODOLOGÍA TEACH) ─────────────
function generarItinerario(p) {
  const nivel = parseInt(p.nivelDominante.slice(1));
  const area = p.area.toLowerCase();
  const bloqueo = p.bloqueoMaximo.nombre;
  const formato = p.formatoPreferido;

  // ── OBJETIVO MES 1 por nivel de entrada ──
  const objetivos = {
    0: "Completar primer prompt útil para una tarea real del área. Documentar resultado.",
    1: "Usar IA de forma autónoma en al menos 3 tareas semanales. Primeras iteraciones de prompt.",
    2: "Tener un espacio de IA con contexto fijo del área. Documentar 2 casos de uso.",
    3: "Conectar IA a al menos 1 herramienta del área. SOUL.md activo.",
    4: "Crear y documentar primer Skill reutilizable. 3 casos de uso con resultado medible.",
    5: "Tener flujo de trabajo IA completo para 1 tarea crítica. Listo para mentorear.",
    6: "1 automatización activa (cron o pipeline). Métricas de impacto documentadas.",
    7: "Agente autónomo productivo. Iniciar rol de mentor con 1 compañero.",
    8: "Certificar a 2 personas. Diseñar 1 Skill institucional compartido.",
  };

  // ── SEMANAS 1-2 por área y nivel ──
  const semana12 = generarSemana12(nivel, area);

  // ── SEMANAS 3-4 ──
  const semana34 = generarSemana34(nivel, area);

  // ── HITO DE NIVEL ──
  const hitos = {
    0: "Nivel L1: Primer prompt con contexto. IA responde en menos de 2 iteraciones.",
    1: "Nivel L2: IA lee archivos del área sin ayuda del instructor.",
    2: "Nivel L3: SOUL.md o espacio de contexto fijo configurado.",
    3: "Nivel L4: IA conectada a 1 herramienta real del área (Drive, Slack, Git, etc).",
    4: "Nivel L5: Skill propio documentado y versionado.",
    5: "Nivel L6: Delegar tarea completa, recuperar resultado sin supervisar.",
    6: "Nivel L7: IA ejecuta en terminal o navega en su nombre.",
    7: "Nivel L8: Agente autónomo corriendo en horario no laboral.",
    8: "Nivel L9: 3 automatizaciones en producción + certificó a otros.",
  };

  // ── BLOQUEO A TRABAJAR ──
  const estrategiasBloqueo = {
    "Tiempo": "Bloque de 20 min/día enfocado. 1 tarea IA por día, no más.",
    "Conocimiento técnico": "Empezar con casos de uso del propio rol. Usar /teach para aprender paso a paso.",
    "Confianza": "Practicar en sandbox (nada en producción hasta L3). Validar siempre antes de usar.",
    "Seguridad/Privacidad": "Sesión específica: qué SÍ y qué NO subir a IA. Definir política de uso del área.",
    "Acceso/Permisos": "Elevar solicitud de acceso en S1. Mientras: usar herramientas web sin instalación.",
    "Soporte": "Canal de Slack/Teams de Champions como línea de soporte inmediato.",
    "Cultura": "Casos de uso de par inmediato. Logro visible en 1ra semana como ancla de credibilidad."
  };

  // ── FORMATO SUGERIDO ──
  let formatoSugerido;
  if (formato.includes("haciendo") || formato.includes("problema real")) {
    formatoSugerido = "Aprender haciendo: 1 tarea real/semana + retrospectiva de 10 min";
  } else if (formato.includes("Pair") || formato.includes("par")) {
    formatoSugerido = "Pair-working con Champion de área más avanzado";
  } else if (formato.includes("presencial")) {
    formatoSugerido = "Sesiones presenciales 2h c/2 semanas + práctica autónoma entre sesiones";
  } else if (formato.includes("video") || formato.includes("asincrónico")) {
    formatoSugerido = "Videos cortos (<10 min) + ejercicio aplicado al área";
  } else {
    formatoSugerido = "Aprender haciendo + documentación escrita de referencia";
  }

  // ── HERRAMIENTA DE ENTRADA según área ──
  const herramientasEntrada = {
    "infraestructura": nivel <= 2 ? "Claude.ai (web) para scripts Bash/PowerShell" : "Hermes Agent + MCP filesystem",
    "desarrollo": nivel <= 2 ? "GitHub Copilot en IDE / Claude.ai para código" : "Hermes Agent + MCP GitHub",
    "soporte": nivel <= 2 ? "Claude.ai para redactar respuestas y clasificar tickets" : "Hermes Agent + MCP para automatizar tickets",
    "dirección": nivel <= 2 ? "Claude.ai para documentos y análisis" : "Hermes Agent + MCP Drive/Calendar",
  };
  const herramienta = herramientasEntrada[area] || "Claude.ai (web) como punto de partida";

  // ── CASO DE USO ANCLA según área ──
  const casosUsoAncla = {
    "infraestructura": "Generar script de monitoreo o diagnóstico de red con IA",
    "desarrollo": "Revisar y refactorizar código legado con IA como pair programmer",
    "soporte": "Clasificar y redactar respuestas a tickets frecuentes con IA",
    "dirección": "Generar reporte ejecutivo o acta de reunión con IA",
  };
  const casoAncla = casosUsoAncla[area] || "Automatizar una tarea repetitiva del área con IA";

  return [
    p.nombre,
    p.area,
    p.nivelDominante + " · " + p.zona,
    p.licencia,
    objetivos[nivel] || objetivos[8],
    semana12,
    semana34,
    hitos[nivel] || hitos[8],
    estrategiasBloqueo[bloqueo] || "Identificar 1 tarea real bloqueada y resolverla con IA esta semana.",
    formatoSugerido,
    herramienta,
    casoAncla
  ];
}

function generarSemana12(nivel, area) {
  if (nivel <= 1) {
    return "Lección 1 (Teach): ¿Qué es un prompt? · " +
           "Práctica: 3 prompts reales del área · " +
           "Ejercicio: prompt con contexto vs sin contexto · " +
           "Meta: 1 resultado útil documentado";
  }
  if (nivel <= 3) {
    return "Configurar SOUL.md personal · " +
           "Cargar 1 documento del área como contexto · " +
           "Lección 2 (Teach): Memoria y contexto en IA · " +
           "Meta: IA responde sobre documentos propios del área";
  }
  if (nivel <= 5) {
    return "Crear primer Skill del área con /teach · " +
           "Conectar IA a 1 herramienta del flujo de trabajo · " +
           "Documentar 2 casos de uso en SOUL.md · " +
           "Meta: Skill reutilizable versionado en Git";
  }
  return "Diseñar automatización para tarea repetitiva del área · " +
         "Configurar cron job o pipeline de fondo · " +
         "Lección: arquitectura de agentes autónomos · " +
         "Meta: 1 agente activo sin supervisión continua";
}

function generarSemana34(nivel, area) {
  if (nivel <= 1) {
    return "Lección 2 (Teach): Contexto y memoria · " +
           "Práctica: Pedir a IA que refine y mejore una respuesta · " +
           "Caso de uso real documentado con herramienta + resultado · " +
           "Meta: Primer caso de uso del área completado y registrado";
  }
  if (nivel <= 3) {
    return "Explorar conexión IA ↔ 1 herramienta real del área · " +
           "Definir 1 flujo reutilizable (checklist de pasos) · " +
           "Revisar y mejorar SOUL.md con aprendizajes de S1-S2 · " +
           "Meta: 2 casos de uso documentados con resultado medible";
  }
  if (nivel <= 5) {
    return "Practicar delegación completa de 1 tarea (sin supervisar) · " +
           "Medir tiempo antes vs después de IA en 1 proceso · " +
           "Preparar sesión de transferencia para el equipo · " +
           "Meta: Lista para sesión grupal como mentor";
  }
  return "Documentar métricas de impacto del agente · " +
         "Preparar sesión de certificación para 1 compañero · " +
         "Diseñar Skill institucional compartido con el equipo · " +
         "Meta: Primer compañero certificado en nivel L2+";
}

// ─── HOJA: RESUMEN_GRUPO ─────────────────────────────────────
function crearHojaResumenGrupo(ss, participantes) {
  let hoja = ss.getSheetByName("RESUMEN_GRUPO");
  if (hoja) ss.deleteSheet(hoja);
  hoja = ss.insertSheet("RESUMEN_GRUPO");

  const total = participantes.length;
  const sumatoriasAll = participantes.map(p => p.sumatoria);
  const promedio = sumatoriasAll.reduce((a, b) => a + b, 0) / total;

  // Distribución por zona
  const zonas = {};
  participantes.forEach(p => zonas[p.zona] = (zonas[p.zona] || 0) + 1);

  // Bloqueo más común (el que suma más puntos en total)
  const totalBloqueos = NOMBRES_BLOQUEOS.map((nombre, i) => ({
    nombre,
    total: participantes.reduce((sum, p) => sum + (p.bloqueos[i]?.valor || 0), 0)
  })).sort((a, b) => b.total - a.total);

  // Nivel más bajo y más alto
  const niveles = participantes.map(p => parseInt(p.nivelDominante.slice(1)));
  const nivelMin = Math.min(...niveles);
  const nivelMax = Math.max(...niveles);
  const nivelProm = niveles.reduce((a, b) => a + b, 0) / total;

  const datos = [
    ["═══ RESUMEN DEL GRUPO · AI Fluency MCA ═══", ""],
    ["Fecha de análisis", new Date().toLocaleDateString("es-SV")],
    ["Total participantes", total],
    ["", ""],
    ["── NIVELES ──", ""],
    ["Score promedio (de 50)", promedio.toFixed(1)],
    ["Nivel mínimo", "L" + nivelMin],
    ["Nivel máximo", "L" + nivelMax],
    ["Nivel promedio", "L" + nivelProm.toFixed(1)],
    ["", ""],
    ["── DISTRIBUCIÓN POR ZONA ──", ""],
    ["🟤 Pasajeros (L0–L2)", zonas["Pasajero"] || 0],
    ["🟢 Conductores (L3–L5)", zonas["Conductor"] || 0],
    ["🟣 Pilotos Automáticos (L6+)", zonas["Piloto Automático"] || 0],
    ["", ""],
    ["── BLOQUEOS (de más a menos frecuente) ──", "Puntuación total"],
    ...totalBloqueos.map((b, i) => [`${i + 1}. ${b.nombre}`, b.total]),
    ["", ""],
    ["── RECOMENDACIONES PARA EL PROGRAMA ──", ""],
    ...generarRecomendacionesGrupo(participantes, promedio, totalBloqueos, zonas),
    ["", ""],
    ["── PARTICIPANTES ──", ""],
    ["Nombre", "Nivel · Licencia"],
    ...participantes.map(p => [p.nombre, p.nivelDominante + " · " + p.licencia])
  ];

  hoja.getRange(1, 1, datos.length, 2).setValues(datos);

  // Estilo de encabezados
  hoja.getRange(1, 1, 1, 2).setBackground("#0A2540").setFontColor("#FFFFFF").setFontWeight("bold");
  hoja.autoResizeColumns(1, 2);
}

function generarRecomendacionesGrupo(participantes, promedio, totalBloqueos, zonas) {
  const recomendaciones = [];
  const totalP = participantes.length;

  if (promedio < 20) {
    recomendaciones.push(["⚠️ Grupo en zona Pasajero", "Priorizar fundamentos antes de conectar herramientas avanzadas"]);
  } else if (promedio < 35) {
    recomendaciones.push(["✅ Grupo listo para Fase Conductor", "Enfocarse en SOUL.md y primer Skill por área"]);
  } else {
    recomendaciones.push(["🚀 Grupo avanzado", "Iniciar automatizaciones y preparar mentoreo a equipo"]);
  }

  const bloqueoTop = totalBloqueos[0];
  recomendaciones.push([`🔴 Bloqueo crítico del grupo: ${bloqueoTop.nombre}`, "Abordarlo en la primera sesión colectiva"]);

  if ((zonas["Pasajero"] || 0) > totalP / 2) {
    recomendaciones.push(["📚 Mayoría en zona Pasajero", "Sesión extra de onboarding antes de avanzar a Skills"]);
  }

  const disposicionEnsenar = participantes.filter(p =>
    p.ensenaria.toLowerCase().includes("sí") || p.ensenaria.toLowerCase().includes("si")
  ).length;
  recomendaciones.push([`👥 Dispuestos a enseñar: ${disposicionEnsenar}/${totalP}`, "Estos son candidatos para extender el programa al equipo"]);

  return recomendaciones;
}

// ─── FUNCIONES AUXILIARES ────────────────────────────────────
function regenerarItinerarios() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const hojaResp = ss.getSheetByName(CONFIG.HOJA_RESPUESTAS);
  if (!hojaResp) return;
  const datos = hojaResp.getDataRange().getValues();
  const participantes = [];
  for (let i = 1; i < datos.length; i++) {
    const fila = datos[i];
    if (!fila[CONFIG.COL_NOMBRE - 1]) continue;
    participantes.push(extraerParticipante(fila, i + 1));
  }
  crearHojaItinerarios(ss, participantes);
  SpreadsheetApp.getUi().alert("✅ Itinerarios regenerados.");
}

function exportarResumenGrupo() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const hojaResp = ss.getSheetByName(CONFIG.HOJA_RESPUESTAS);
  if (!hojaResp) return;
  const datos = hojaResp.getDataRange().getValues();
  const participantes = [];
  for (let i = 1; i < datos.length; i++) {
    const fila = datos[i];
    if (!fila[CONFIG.COL_NOMBRE - 1]) continue;
    participantes.push(extraerParticipante(fila, i + 1));
  }
  crearHojaResumenGrupo(ss, participantes);
  SpreadsheetApp.getUi().alert("✅ Resumen de grupo actualizado.");
}

/**
 * ─── INSTRUCCIONES DE INSTALACIÓN ────────────────────────────
 *
 * 1. Abre el Google Sheet vinculado al Form de diagnóstico
 *    https://forms.gle/JHd4a8kHyFh59RkH7
 *
 * 2. Menú: Extensiones → Apps Script
 *
 * 3. Borra el código que aparece por defecto (function myFunction() {...})
 *
 * 4. Pega TODO este archivo
 *
 * 5. Guarda (Ctrl+S o el ícono de disco)
 *
 * 6. Recarga el Google Sheet — aparecerá el menú "🚗 MCA · AI Fluency"
 *
 * 7. Cuando tengas respuestas: Menú → "Calcular niveles e itinerarios"
 *
 * ─── PERSONALIZACIÓN ──────────────────────────────────────────
 *
 * Si el nombre de tu hoja de respuestas es diferente:
 *   - Cambia CONFIG.HOJA_RESPUESTAS en la línea 28
 *
 * Si el Form tiene columnas en orden diferente:
 *   - Ajusta los números en CONFIG (sección líneas 29-50)
 *   - El número = posición de la columna en el Sheet (1 = columna A)
 *
 * ─────────────────────────────────────────────────────────────
 */
