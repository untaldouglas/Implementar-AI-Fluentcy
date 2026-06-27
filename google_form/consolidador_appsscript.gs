/**
 * Consolidador automático - Cuestionario Baseline AI Literacy UJMD
 * -------------------------------------------------------------------
 * PROPÓSITO:
 *   Lee respuestas de Google Forms (hoja de cálculo conectada),
 *   calcula nivel estimado (L0-L9) por participante, y genera una
 *   nueva pestaña "RESUMEN" con análisis agregado.
 *
 * INSTALACIÓN:
 *   1. Abrir la hoja de cálculo conectada al Google Form
 *   2. Ir al menú "Extensiones" → "Apps Script"
 *   3. Crear proyecto nuevo (o editar el existente)
 *   4. Borrar el contenido default y pegar este script
 *   5. Guardar (Ctrl+S) y ejecutar "ejecutarConsolidador" la primera vez
 *      desde el editor (otorga permisos)
 *
 * RESULTADO:
 *   Genera pestañas nuevas en la hoja:
 *     - RESUMEN_INDIVIDUAL: nivel estimado + nivel dominante por persona
 *     - RESUMEN_AGGREGADO:  promedios por área, bloqueos dominantes
 *     - RESUMEN_CHAMPIONS:  análisis cruzado para selección final
 *
 * AUTOR: @untaldouglas
 * FECHA: 26 junio 2026
 */

// ============================================================
// CONFIGURACIÓN DE COLUMNAS DEL FORMULARIO
// Ajustar si se modifican preguntas o se agregan secciones
// ============================================================

const COLUMNAS = {
  timestamp: 1,         // A - Marca temporal
  correo: 2,            // B - Correo institucional
  nombre: 3,            // C - Nombre completo
  correoConfirma: 4,    // D - Correo (confirmación)
  area: 5,              // E - Área
  rol: 6,               // F - Rol actual
  antiguedad: 7,        // G - Antigüedad
  // P7-P12: herramientas y casos (texto libre o categorías)
  // P13-P22: Escalas lineales Sección 4 (L0-L9)
  autodiagnostico: {
    L0_Taxi: 16,        // P13
    L1_Chofer_Refina: 17, // P14
    L1_Memoria: 18,       // P15
    L2_Archivos: 19,      // P16
    L3_Contexto: 20,      // P17
    L4_Conexiones: 21,    // P18
    L5_Playbooks: 22,     // P19
    L6_Delegacion: 23,    // P20
    L7_Terminal: 24,      // P21
    L8_Agentes: 25        // P22
  },
  // P23-P29: Bloqueos 0-3
  bloqueos: {
    tiempo: 26,           // P23
    conocimiento: 27,     // P24
    confianza: 28,        // P25
    seguridad: 29,        // P26
    acceso: 30,           // P27
    soporte: 31,          // P28
    cultura: 32           // P29
  },
  bloqueoPrincipal: 33,   // P30
  expectativa: 34,        // P31
  asistenteIdeal: 35,     // P32
  disposicionEnseñar: 36, // P33
  condiciones: 37,        // P34
  formatoAprendizaje: 38, // P35
  comentarioFinal: 39     // P36
};

// ============================================================
// FUNCIÓN PRINCIPAL - Ejecutable manualmente
// ============================================================

function ejecutarConsolidador() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const respuestasHojas = ss.getSheetByName('Respuestas de formulario 1') 
                        || ss.getSheets().find(s => s.getName().toLowerCase().includes('respuesta'));
  
  if (!respuestasHojas) {
    SpreadsheetApp.getUi().alert(
      'No encontré la hoja de respuestas del formulario. ' +
      'Verifica que el formulario esté conectado a esta hoja de cálculo.'
    );
    return;
  }
  
  const data = respuestasHojas.getDataRange().getValues();
  const headers = data[0];
  const rows = data.slice(1); // Saltar cabecera
  
  if (rows.length === 0) {
    SpreadsheetApp.getUi().alert('No hay respuestas aún para procesar.');
    return;
  }
  
  // Procesar cada respuesta
  const individual = rows.map(row => procesarIndividual(row, headers));
  
  // Generar resúmenes
  const agregado = procesarAgregado(individual);
  const champions = procesarChampions(individual);
  
  // Escribir resultados
  escribirResumenIndividual(ss, individual);
  escribirResumenAgregado(ss, agregado);
  escribirResumenChampions(ss, champions);
  
  SpreadsheetApp.getUi().alert(
    `✅ Consolidación completada.\n\n` +
    `${individual.length} respuestas procesadas.\n` +
    `Revisa las pestañas: RESUMEN_INDIVIDUAL, RESUMEN_AGGREGADO, RESUMEN_CHAMPIONS`
  );
}

// ============================================================
// PROCESAMIENTO INDIVIDUAL
// ============================================================

function procesarIndividual(row, headers) {
  const col = COLUMNAS;
  
  // Extraer puntuaciones L0-L9
  const niveles = {
    L0: Number(row[col.autodiagnostico.L0_Taxi - 1]) || 0,
    L1: Math.max(
      Number(row[col.autodiagnostico.L1_Chofer_Refina - 1]) || 0,
      Number(row[col.autodiagnostico.L1_Memoria - 1]) || 0
    ),
    L2: Number(row[col.autodiagnostico.L2_Archivos - 1]) || 0,
    L3: Number(row[col.autodiagnostico.L3_Contexto - 1]) || 0,
    L4: Number(row[col.autodiagnostico.L4_Conexiones - 1]) || 0,
    L5: Number(row[col.autodiagnostico.L5_Playbooks - 1]) || 0,
    L6: Number(row[col.autodiagnostico.L6_Delegacion - 1]) || 0,
    L7: Number(row[col.autodiagnostico.L7_Terminal - 1]) || 0,
    L8: Number(row[col.autodiagnostico.L8_Agentes - 1]) || 0
  };
  
  // Sumatoria total
  const totalL = Object.values(niveles).reduce((a, b) => a + b, 0);
  
  // Nivel dominante: el de mayor puntuación (en caso de empate, el más alto)
  let nivelDominante = 'L0';
  let maxScore = niveles.L0;
  for (const [nombre, score] of Object.entries(niveles)) {
    if (score > maxScore) {
      nivelDominante = nombre;
      maxScore = score;
    }
  }
  
  // Zona según sumatoria
  const zona = clasificarZona(totalL);
  
  // Extraer bloqueos
  const bloqueos = {
    tiempo: Number(row[col.bloqueos.tiempo - 1]) || 0,
    conocimiento: Number(row[col.bloqueos.conocimiento - 1]) || 0,
    confianza: Number(row[col.bloqueos.confianza - 1]) || 0,
    seguridad: Number(row[col.bloqueos.seguridad - 1]) || 0,
    acceso: Number(row[col.bloqueos.acceso - 1]) || 0,
    soporte: Number(row[col.bloqueos.soporte - 1]) || 0,
    cultura: Number(row[col.bloqueos.cultura - 1]) || 0
  };
  
  const bloqueoDominante = Object.entries(bloqueos)
    .reduce((a, b) => b[1] > a[1] ? b : a, ['tiempo', 0])[0];
  
  return {
    nombre: row[col.nombre - 1] || '(sin nombre)',
    correo: row[col.correo - 1] || '',
    area: row[col.area - 1] || '(sin clasificar)',
    rol: row[col.rol - 1] || '',
    antiguedad: row[col.antiguedad - 1] || '',
    niveles: niveles,
    totalL: totalL,
    nivelDominante: nivelDominante,
    zona: zona,
    bloqueos: bloqueos,
    bloqueoDominante: bloqueoDominante,
    bloqueoPrincipal: row[col.bloqueoPrincipal - 1] || '',
    expectativa: row[col.expectativa - 1] || '',
    asistenteIdeal: row[col.asistenteIdeal - 1] || '',
    disposicionEnseñar: row[col.disposicionEnseñar - 1] || '',
    formatoAprendizaje: row[col.formatoAprendizaje - 1] || '',
    timestamp: row[0]
  };
}

function clasificarZona(totalL) {
  if (totalL <= 20) return 'Pasajero (L0-L2)';
  if (totalL <= 35) return 'Conductor (L3-L5)';
  return 'Piloto Automático (L6-L9)';
}

// ============================================================
// PROCESAMIENTO AGREGADO
// ============================================================

function procesarAgregado(individual) {
  // Por área
  const porArea = {};
  individual.forEach(p => {
    if (!porArea[p.area]) porArea[p.area] = [];
    porArea[p.area].push(p);
  });
  
  const analisisArea = Object.entries(porArea).map(([area, personas]) => {
    const promTotal = personas.reduce((s, p) => s + p.totalL, 0) / personas.length;
    const promBloqueo = personas.reduce((s, p) => {
      return s + Object.values(p.bloqueos).reduce((a, b) => a + b, 0);
    }, 0) / personas.length;
    
    // Bloqueo más mencionado como "principal"
    const bloqueosMencionados = personas
      .map(p => p.bloqueoDominante)
      .reduce((acc, b) => (acc[b] = (acc[b] || 0) + 1, acc), {});
    const masFrecuente = Object.entries(bloqueosMencionados)
      .sort((a, b) => b[1] - a[1])[0];
    
    return {
      area: area,
      personas: personas.length,
      nivelPromedio: promTotal.toFixed(1),
      zonaPredominante: clasificarZona(promTotal),
      bloqueoMasFrecuente: masFrecuente ? masFrecuente[0] : 'N/A',
      personasList: personas.map(p => `${p.nombre} (${p.nivelDominante})`).join(', ')
    };
  });
  
  // Métricas globales
  const global = {
    totalPersonas: individual.length,
    nivelPromedioGeneral: (individual.reduce((s, p) => s + p.totalL, 0) / individual.length).toFixed(2),
    personasPorZona: {
      'Pasajero': individual.filter(p => p.zona.includes('Pasajero')).length,
      'Conductor': individual.filter(p => p.zona.includes('Conductor')).length,
      'Piloto Automático': individual.filter(p => p.zona.includes('Piloto Automático')).length
    },
    bloqueosDominantes: individual
      .map(p => p.bloqueoDominante)
      .reduce((acc, b) => (acc[b] = (acc[b] || 0) + 1, acc), {}),
    disposicionEnseñar: {
      'Sí, con gusto': individual.filter(p => p.disposicionEnseñar.includes('Sí, con gusto')).length,
      'Sí, con condiciones': individual.filter(p => p.disposicionEnseñar.includes('con condiciones')).length,
      'Probablemente no': individual.filter(p => p.disposicionEnseñar.includes('no')).length
    }
  };
  
  return { analisisArea, global };
}

// ============================================================
// PROCESAMIENTO PARA SELECCIÓN DE CHAMPIONS
// ============================================================

function procesarChampions(individual) {
  // Criterios para Champion ideales (ver Manual + Roadmap):
  // 1. Nivel: ni muy novato ni muy experto (L2-L4 mejor)
  // 2. Apertura al cambio (bloqueo "cultura" bajo: 0-1)
  // 3. Disposición a enseñar: "Sí, con gusto" o "Sí, con condiciones"
  // 4. Apertura (formato "aprender haciendo" preferido)
  
  const candidatos = individual.map(p => {
    let scoreChampion = 0;
    const observaciones = [];
    
    // Nivel óptimo (L1-L4 ideales)
    if (['L2', 'L3', 'L4'].includes(p.nivelDominante)) {
      scoreChampion += 10;
      observaciones.push(`Nivel ${p.nivelDominante}: óptimo para Champion`);
    } else if (['L1', 'L5'].includes(p.nivelDominante)) {
      scoreChampion += 6;
      observaciones.push(`Nivel ${p.nivelDominante}: aceptable`);
    } else {
      scoreChampion += 2;
      observaciones.push(`Nivel ${p.nivelDominante}: menos ideal`);
    }
    
    // Baja cultura de resistencia
    if (p.bloqueos.cultura <= 1) {
      scoreChampion += 8;
      observaciones.push(`Baja fricción cultural (${p.bloqueos.cultura}/3)`);
    } else if (p.bloqueos.cultura === 2) {
      scoreChampion += 4;
      observaciones.push(`Fricción cultural moderada (${p.bloqueos.cultura}/3)`);
    } else {
      observaciones.push(`Alta fricción cultural (${p.bloqueos.cultura}/3) - revisar`);
    }
    
    // Disposición a enseñar
    if (p.disposicionEnseñar.includes('Sí, con gusto')) {
      scoreChampion += 10;
      observaciones.push('Disposición total a enseñar');
    } else if (p.disposicionEnseñar.includes('condiciones')) {
      scoreChampion += 5;
      observaciones.push('Disposición con condiciones');
    }
    
    // Preferencia aprender haciendo (apto para construcción de agentes)
    const formato = p.formatoAprendizaje || '';
    if (formato.toLowerCase().includes('haciendo') || formato.toLowerCase().includes('pair')) {
      scoreChampion += 5;
      observaciones.push('Prefiere aprendizaje práctico');
    }
    
    return { ...p, scoreChampion, observaciones };
  });
  
  // Ordenar por score descendente
  return candidatos.sort((a, b) => b.scoreChampion - a.scoreChampion);
}

// ============================================================
// ESCRITURA DE RESULTADOS
// ============================================================

function escribirResumenIndividual(ss, individual) {
  let sheet = ss.getSheetByName('RESUMEN_INDIVIDUAL');
  if (!sheet) sheet = ss.insertSheet('RESUMEN_INDIVIDUAL');
  
  const headers = [
    'Nombre', 'Correo', 'Área', 'Rol', 'Sumatoria L',
    'Nivel dominante', 'Zona', 'Bloqueo dominante',
    'Dispuesto a enseñar', 'Observaciones'
  ];
  
  // Limpiar y reescribir
  sheet.clear();
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold').setBackground('#4a86e8').setFontColor('white');
  
  const filas = individual.map(p => [
    p.nombre, p.correo, p.area, p.rol,
    p.totalL, p.nivelDominante, p.zona, p.bloqueoDominante,
    p.disposicionEnseñar,
    `Niveles: ${Object.entries(p.niveles).map(([k,v])=>`${k}=${v}`).join(', ')}`
  ]);
  
  if (filas.length > 0) {
    sheet.getRange(2, 1, filas.length, headers.length).setValues(filas);
  }
  
  // Colorear por zona
  individual.forEach((p, i) => {
    const fila = i + 2;
    let color;
    if (p.zona.includes('Pasajero')) color = '#fff2cc';
    else if (p.zona.includes('Conductor')) color = '#d9ead3';
    else color = '#cfe2f3';
    sheet.getRange(fila, 7).setBackground(color);
  });
  
  sheet.autoResizeColumns(1, headers.length);
}

function escribirResumenAgregado(ss, data) {
  let sheet = ss.getSheetByName('RESUMEN_AGGREGADO');
  if (!sheet) sheet = ss.insertSheet('RESUMEN_AGGREGADO');
  
  sheet.clear();
  
  let fila = 1;
  
  // Métricas globales
  sheet.getRange(fila++, 1).setValue('📊 MÉTRICAS GLOBALES').setFontWeight('bold').setBackground('#f3f3f3');
  sheet.getRange(fila++, 1).setValue(`Total de personas: ${data.global.totalPersonas}`);
  sheet.getRange(fila++, 1).setValue(`Nivel promedio general (sumatoria): ${data.global.nivelPromedioGeneral}`);
  fila++;
  
  sheet.getRange(fila++, 1).setValue('Distribución por zona:').setFontWeight('bold');
  Object.entries(data.global.personasPorZona).forEach(([zona, cant]) => {
    sheet.getRange(fila++, 1).setValue(`  ${zona}: ${cant}`);
  });
  fila++;
  
  sheet.getRange(fila++, 1).setValue('Bloqueos dominantes (conteo):').setFontWeight('bold');
  Object.entries(data.global.bloqueosDominantes)
    .sort((a, b) => b[1] - a[1])
    .forEach(([bloqueo, cant]) => {
      sheet.getRange(fila++, 1).setValue(`  ${bloqueo}: ${cant}`);
    });
  fila++;
  
  sheet.getRange(fila++, 1).setValue('Disposición a enseñar:').setFontWeight('bold');
  Object.entries(data.global.disposicionEnseñar).forEach(([disp, cant]) => {
    sheet.getRange(fila++, 1).setValue(`  ${disp}: ${cant}`);
  });
  fila += 2;
  
  // Análisis por área
  sheet.getRange(fila++, 1).setValue('📈 ANÁLISIS POR ÁREA').setFontWeight('bold').setBackground('#f3f3f3');
  
  const headersArea = ['Área', '# Personas', 'Nivel Prom.', 'Zona Predominante', 'Bloqueo Más Frecuente', 'Personas'];
  sheet.getRange(fila, 1, 1, headersArea.length).setValues([headersArea]).setFontWeight('bold').setBackground('#4a86e8').setFontColor('white');
  fila++;
  
  data.analisisArea.forEach(a => {
    sheet.getRange(fila, 1, 1, headersArea.length).setValues([[
      a.area, a.personas, a.nivelPromedio, a.zonaPredominante,
      a.bloqueoMasFrecuente, a.personasList
    ]]);
    fila++;
  });
  
  sheet.autoResizeColumns(1, 6);
}

function escribirResumenChampions(ss, candidatos) {
  let sheet = ss.getSheetByName('RESUMEN_CHAMPIONS');
  if (!sheet) sheet = ss.insertSheet('RESUMEN_CHAMPIONS');
  
  sheet.clear();
  
  const headers = [
    'Ranking', 'Nombre', 'Área', 'Nivel Dominante',
    'Bloqueo Cultura (0-3)', 'Dispuesto a Enseñar',
    'Score Champion', 'Observaciones'
  ];
  
  sheet.getRange(1, 1, 1, headers.length).setValues([headers]).setFontWeight('bold').setBackground('#8e7cc3').setFontColor('white');
  
  const filas = candidatos.map((c, i) => [
    i + 1, c.nombre, c.area, c.nivelDominante,
    c.bloqueos.cultura, c.disposicionEnseñar,
    c.scoreChampion, c.observaciones.join(' | ')
  ]);
  
  if (filas.length > 0) {
    sheet.getRange(2, 1, filas.length, headers.length).setValues(filas);
  }
  
  // Resaltar top 3
  for (let i = 0; i < Math.min(3, filas.length); i++) {
    sheet.getRange(i + 2, 1, 1, headers.length).setBackground('#ffd966');
  }
  
  // Nota interpretativa
  const notaFila = filas.length + 3;
  sheet.getRange(notaFila, 1).setValue('⭐ CRITERIOS DE SELECCIÓN (ver Manual):').setFontWeight('bold');
  sheet.getRange(notaFila + 1, 1).setValue('• Nivel dominante L2-L4: óptimo (ni muy novato ni muy experto)');
  sheet.getRange(notaFila + 2, 1).setValue('• Bloqueo cultura ≤1: alta apertura al cambio');
  sheet.getRange(notaFila + 3, 1).setValue('• Disposición a enseñar = "Sí, con gusto"');
  sheet.getRange(notaFila + 4, 1).setValue('• Formato preferido incluye "aprender haciendo" o "pair-working"');
  
  sheet.autoResizeColumns(1, headers.length);
}

// ============================================================
// MENÚ PERSONALIZADO (se agrega al abrir la hoja)
// ============================================================

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🤖 AI Literacy')
    .addItem('Ejecutar consolidador', 'ejecutarConsolidador')
    .addSeparator()
    .addItem('Ver instructivo', 'verInstructivo')
    .addToUi();
}

function verInstructivo() {
  SpreadsheetApp.getUi().alert(
    '🤖 Herramienta de consolidación - AI Literacy Baseline\n\n' +
    'Este script procesa las respuestas del cuestionario y genera:\n' +
    '• RESUMEN_INDIVIDUAL: nivel estimado por persona\n' +
    '• RESUMEN_AGGREGADO: análisis por área\n' +
    '• RESUMEN_CHAMPIONS: ranking para selección\n\n' +
    'Para ejecutar: Menú "AI Literacy" → "Ejecutar consolidador"\n\n' +
    'Programa AI Fluency UJMD\n' +
    'Herramienta oficial: Hermes Agent (NousResearch)'
  );
}
