/**
 * Consolidador de Diagnóstico MCA — AI Fluency UJMD
 *
 * INSTRUCCIONES DE USO:
 * 1. Abre la Google Sheet vinculada al Form (https://forms.gle/JHd4a8kHyFh59RkH7)
 *    → En el Form: Respuestas → Ver en Hojas de cálculo
 * 2. En la Sheet, ve a Extensiones → Apps Script
 * 3. Pega este código (reemplaza todo lo que haya)
 * 4. Ajusta COLUMNAS_DIMENSIONES abajo según el orden real de preguntas del Form
 * 5. Clic en "Ejecutar" → función consolidarDiagnostico
 * 6. Autoriza los permisos cuando se solicite
 * 7. La hoja "Consolidado_MCA" se creará automáticamente con los resultados
 */

// ─── CONFIGURACIÓN ──────────────────────────────────────────────────────────

// Nombre de la hoja donde el Form guarda respuestas (no cambiar si es la default)
var HOJA_RESPUESTAS = "Respuestas de formulario 1";

// Columna donde está el nombre/email del respondente (0 = primera columna = Timestamp)
// Ajusta este número según tu Form. Si la pregunta "¿Cuál es tu nombre?" es la 2ª columna → índice 1
var COL_NOMBRE = 1;

/**
 * Mapeo de dimensiones a columnas de la Sheet (índice base 0)
 * Ajusta los índices según el orden real de preguntas en tu Form.
 *
 * Si no sabes el orden, ejecuta primero listarColumnas() para verlo en el log.
 *
 * Cada dimensión tiene preguntas con respuestas tipo escala (1-4 o similares)
 * o texto. Si son texto, usa el mapa de TEXTO_A_NIVEL abajo.
 */
var COLUMNAS_DIMENSIONES = {
  dim1_herramientas:   2,  // Familiaridad con herramientas IA
  dim2_frecuencia:     3,  // Frecuencia de uso
  dim3_tareas:         4,  // Tipo de tareas
  dim4_confianza:      5,  // Confianza en resultados
  dim5_actitud:        6   // Actitud hacia el aprendizaje
};

/**
 * Mapa de texto de respuesta → nivel MCA (L0-L3)
 * Ajusta según las opciones exactas que pusiste en el Form.
 * Las claves son fragmentos de texto (búsqueda parcial, sin distinción may/min).
 */
var TEXTO_A_NIVEL = {
  // Dim 1 - Herramientas
  "no uso ninguna":          0,
  "no sé qué son":           0,
  "he oído":                 1,
  "lo probé":                1,
  "uso ocasionalmente":      2,
  "uso varias herramientas": 3,
  "tengo una rutina":        3,
  // Dim 2 - Frecuencia
  "nunca":                   0,
  "menos de una vez":        0,
  "1-2 veces al mes":        1,
  "por curiosidad":          1,
  "varias veces por semana": 2,
  "diariamente":             3,
  "integrado al flujo":      3,
  // Dim 3 - Tareas
  "ninguna":                 0,
  "preguntas generales":     1,
  "búsquedas":               1,
  "traducciones":            1,
  "redacción":               2,
  "resúmenes":               2,
  "automatización":          3,
  "análisis":                3,
  // Dim 4 - Confianza
  "no confío":               0,
  "no lo he probado":        0,
  "a veces sirve":           1,
  "no sé si":                1,
  "puedo evaluar":           2,
  "sé cuándo falla":         3,
  "mejores prompts":         3,
  // Dim 5 - Actitud
  "resistencia":             0,
  "escepticismo":            0,
  "indiferencia":            0,
  "curiosidad pero sin":     1,
  "sin compromiso":          1,
  "motivación":              2,
  "quiere aprender":         2,
  "ya enseña":               3,
  "documenta":               3
};

// ─── FUNCIONES PRINCIPALES ──────────────────────────────────────────────────

/**
 * Función principal. Ejecuta esto para generar el consolidado.
 */
function consolidarDiagnostico() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var hojaResp = ss.getSheetByName(HOJA_RESPUESTAS);

  if (!hojaResp) {
    SpreadsheetApp.getUi().alert(
      'No se encontró la hoja "' + HOJA_RESPUESTAS + '".\n\n' +
      'Verifica que el nombre coincide exactamente con la pestaña de respuestas.'
    );
    return;
  }

  var datos = hojaResp.getDataRange().getValues();

  if (datos.length < 2) {
    SpreadsheetApp.getUi().alert('El formulario aún no tiene respuestas.');
    return;
  }

  // Crear/limpiar hoja de consolidado
  var hojaConsolidado = ss.getSheetByName("Consolidado_MCA");
  if (hojaConsolidado) {
    hojaConsolidado.clear();
  } else {
    hojaConsolidado = ss.insertSheet("Consolidado_MCA");
  }

  // Encabezados
  var encabezados = [
    "Nombre / Email",
    "Dim 1\nHerramientas",
    "Dim 2\nFrecuencia",
    "Dim 3\nTareas",
    "Dim 4\nConfianza",
    "Dim 5\nActitud",
    "Nivel MCA",
    "Licencia",
    "Primera Meta",
    "Bandera",
    "Timestamp"
  ];

  hojaConsolidado.appendRow(encabezados);

  // Procesar cada respuesta (fila 0 = encabezados, saltar)
  for (var i = 1; i < datos.length; i++) {
    var fila = datos[i];
    var nombre = fila[COL_NOMBRE] || "Respondente " + i;
    var timestamp = fila[0];

    // Calcular nivel por dimensión
    var niveles = {
      dim1: calcularNivel(fila[COLUMNAS_DIMENSIONES.dim1_herramientas]),
      dim2: calcularNivel(fila[COLUMNAS_DIMENSIONES.dim2_frecuencia]),
      dim3: calcularNivel(fila[COLUMNAS_DIMENSIONES.dim3_tareas]),
      dim4: calcularNivel(fila[COLUMNAS_DIMENSIONES.dim4_confianza]),
      dim5: calcularNivel(fila[COLUMNAS_DIMENSIONES.dim5_actitud])
    };

    var nivelFinal = calcularNivelFinal(niveles);
    var licencia = nivelALicencia(nivelFinal);
    var meta = primeraMeta(nivelFinal, nombre);
    var bandera = detectarBandera(niveles);

    hojaConsolidado.appendRow([
      nombre,
      "L" + niveles.dim1,
      "L" + niveles.dim2,
      "L" + niveles.dim3,
      "L" + niveles.dim4,
      "L" + niveles.dim5,
      "L" + nivelFinal,
      licencia,
      meta,
      bandera,
      timestamp
    ]);
  }

  // Formato visual
  aplicarFormato(hojaConsolidado);

  // Activar la hoja de resultados
  ss.setActiveSheet(hojaConsolidado);

  SpreadsheetApp.getUi().alert(
    '✅ Consolidado generado con ' + (datos.length - 1) + ' respondente(s).\n\n' +
    'Revisa la hoja "Consolidado_MCA".\n\n' +
    '⚠️ Si los niveles no se ven correctos, ejecuta listarColumnas() ' +
    'para verificar el mapeo de preguntas y ajusta COLUMNAS_DIMENSIONES en el código.'
  );
}

/**
 * Utilitario: muestra en el Log el nombre de cada columna y su índice.
 * Útil para ajustar COLUMNAS_DIMENSIONES.
 * Ejecutar desde: Extensiones → Apps Script → Seleccionar listarColumnas → Ejecutar
 */
function listarColumnas() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var hoja = ss.getSheetByName(HOJA_RESPUESTAS);

  if (!hoja) {
    Logger.log('Hoja "' + HOJA_RESPUESTAS + '" no encontrada.');
    return;
  }

  var encabezados = hoja.getRange(1, 1, 1, hoja.getLastColumn()).getValues()[0];
  Logger.log("=== COLUMNAS DEL FORM (índice → pregunta) ===");
  for (var i = 0; i < encabezados.length; i++) {
    Logger.log("Índice " + i + " → " + encabezados[i]);
  }
  Logger.log("Actualiza COLUMNAS_DIMENSIONES en el script con estos índices.");
}

// ─── FUNCIONES DE CÁLCULO ───────────────────────────────────────────────────

/**
 * Convierte una respuesta (texto o número) a nivel 0-3.
 */
function calcularNivel(respuesta) {
  if (respuesta === null || respuesta === undefined || respuesta === "") return 0;

  var resp = String(respuesta).trim();

  // Si es número directo (escala 1-4 o 0-3)
  var num = parseFloat(resp);
  if (!isNaN(num)) {
    if (num <= 1) return 0;
    if (num <= 2) return 1;
    if (num <= 3) return 2;
    return 3;
  }

  // Búsqueda por texto parcial (insensible a mayúsculas)
  var respLower = resp.toLowerCase();
  for (var clave in TEXTO_A_NIVEL) {
    if (respLower.indexOf(clave.toLowerCase()) !== -1) {
      return TEXTO_A_NIVEL[clave];
    }
  }

  // Default: L1 si hay texto pero no se reconoce
  return 1;
}

/**
 * Nivel final = mínimo de las 5 dimensiones (conservador: nivel más bajo).
 * Opción alternativa: Math.round(promedio) — descomenta si prefieres promedio.
 */
function calcularNivelFinal(niveles) {
  var vals = Object.values(niveles);

  // Opción A: conservador (mínimo)
  return Math.min.apply(null, vals);

  // Opción B: promedio — comenta línea de arriba y descomenta esta:
  // var suma = vals.reduce(function(a,b){ return a+b; }, 0);
  // return Math.round(suma / vals.length);
}

function nivelALicencia(nivel) {
  if (nivel <= 1) return "🚗 Permiso (L0-L1)";
  if (nivel <= 3) return "🚙 Básica (L2-L3)";
  if (nivel <= 5) return "🏎️ Profesional (L4-L5)";
  if (nivel <= 7) return "🚀 Avanzada (L6-L7)";
  return "👨‍🏫 Instructor (L8-L9)";
}

function primeraMeta(nivel, nombre) {
  if (nivel === 0) return "Probar ChatGPT/Hermes con 1 tarea real de su área antes de S1";
  if (nivel === 1) return "Usar IA 3 veces esta semana y documentar resultado en SOUL.md";
  if (nivel === 2) return "Crear un prompt reutilizable para su flujo más repetitivo";
  if (nivel === 3) return "Documentar un proceso automatizable y presentarlo en S2";
  return "Definir objetivo personalizado en Sesión 0";
}

function detectarBandera(niveles) {
  // Resistencia activa (dim5 = 0)
  if (niveles.dim5 === 0) return "🔴 Resistencia — conversación 1:1 antes de S1";

  // Gran brecha entre dimensiones
  var vals = Object.values(niveles);
  var max = Math.max.apply(null, vals);
  var min = Math.min.apply(null, vals);
  if (max - min >= 2) return "🟡 Brecha alta entre dimensiones — revisar dim individual";

  // L2+ en todo
  if (min >= 2) return "🟢 L2+ en todo — candidato para acelerar";

  return "⚪ Sin banderas";
}

// ─── FORMATO ────────────────────────────────────────────────────────────────

function aplicarFormato(hoja) {
  // Encabezados en negrita
  hoja.getRange(1, 1, 1, 11).setFontWeight("bold")
      .setBackground("#1a237e")
      .setFontColor("#ffffff")
      .setWrap(true);

  // Auto-resize columnas
  hoja.autoResizeColumns(1, 11);

  // Filas alternas
  var numFilas = hoja.getLastRow();
  for (var i = 2; i <= numFilas; i++) {
    var color = (i % 2 === 0) ? "#e8eaf6" : "#ffffff";
    hoja.getRange(i, 1, 1, 11).setBackground(color);
  }

  // Columna "Nivel MCA" en negrita
  hoja.getRange(2, 7, numFilas - 1, 1).setFontWeight("bold");

  // Fijar encabezado
  hoja.setFrozenRows(1);
}
