/**
 * ═══════════════════════════════════════════════════════════════
 *  CREAR FORM — DIAGNÓSTICO DE CONDUCCIÓN AI
 *  Modelo de Conducción AI (MCA) — Sistema de Certificación
 * ═══════════════════════════════════════════════════════════════
 *
 * INSTRUCCIONES:
 *   1. Ir a script.google.com → Nuevo proyecto
 *   2. Pegar este script completo
 *   3. Ejecutar la función: crearFormDiagnosticoMCA()
 *   4. Aceptar permisos cuando Google los solicite
 *   5. Al finalizar, el link del formulario aparece en el Log
 *
 * RESULTADO:
 *   - Formulario completo creado en tu Google Drive
 *   - Hoja de cálculo de respuestas conectada automáticamente
 *   - Listo para compartir como template
 *
 * AUTOR: @untaldouglas
 * FECHA: 26 junio 2026
 * VERSIÓN: 2.0 — Modelo de Conducción AI
 * ═══════════════════════════════════════════════════════════════
 */

function crearFormDiagnosticoMCA() {

  // ──────────────────────────────────────────────
  // 1. CREAR EL FORMULARIO BASE
  // ──────────────────────────────────────────────
  var form = FormApp.create('Diagnóstico de Conducción AI · Modelo de Certificación MCA');

  form.setDescription(
    'Este diagnóstico mide tu punto de partida en el Modelo de Conducción AI (MCA), ' +
    'una escala de 10 niveles que va desde el uso básico de IA hasta la operación de ' +
    'agentes autónomos.\n\n' +
    'Tu resultado determina tu Licencia de Conducción AI inicial:\n' +
    '🟤 Permiso de Aprendizaje (L0-L1)\n' +
    '🟢 Licencia Básica (L2-L3)\n' +
    '🔵 Licencia Profesional (L4-L5)\n' +
    '🟣 Licencia Avanzada (L6-L7)\n' +
    '🏆 Instructor de Conducción (L8-L9)\n\n' +
    '⏱ Tiempo estimado: 15–20 minutos\n' +
    '🔒 Tus respuestas son confidenciales y se usan exclusivamente para diseñar tu itinerario personalizado.\n\n' +
    'Diseñado por @untaldouglas · Modelo de Conducción AI v2.0'
  );

  form.setCollectEmail(true);
  form.setLimitOneResponsePerUser(true);
  form.setAllowResponseEdits(true);
  form.setShowLinkToRespondAgain(false);
  form.setConfirmationMessage(
    '✅ ¡Gracias! Tu diagnóstico fue recibido.\n\n' +
    'En los próximos días recibirás tu Licencia de Conducción AI inicial y tu itinerario personalizado.\n\n' +
    '— @untaldouglas · Modelo de Conducción AI'
  );

  // ──────────────────────────────────────────────
  // SECCIÓN 1: DATOS DEL PARTICIPANTE
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('1. Datos del participante')
    .setHelpText('Información básica para personalizar tu itinerario de conducción AI.');

  form.addTextItem()
    .setTitle('Nombre completo')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Área')
    .setChoiceValues([
      'Dirección',
      'Infraestructura',
      'Desarrollo',
      'Soporte / Mesa de Servicios',
      'Otra área (especificar al final)'
    ])
    .setRequired(true);

  form.addTextItem()
    .setTitle('Rol actual en el equipo')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Antigüedad en la organización')
    .setChoiceValues([
      'Menos de 1 año',
      '1 a 3 años',
      '3 a 5 años',
      'Más de 5 años'
    ])
    .setRequired(false);

  // ──────────────────────────────────────────────
  // SECCIÓN 2: INVENTARIO DE HERRAMIENTAS
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('2. Herramientas de IA que usas')
    .setHelpText('Marca todas las que hayas usado en los últimos 3 meses, en el trabajo o de forma personal.');

  var checkboxHerramientas = form.addCheckboxItem();
  checkboxHerramientas.setTitle('¿Cuáles herramientas de IA has usado recientemente?')
    .setChoiceValues([
      'ChatGPT (OpenAI)',
      'Claude (Anthropic)',
      'Gemini (Google)',
      'Copilot de Microsoft (Office 365)',
      'GitHub Copilot / Cursor / Codeium (IDE)',
      'Perplexity u otro buscador con IA',
      'Herramientas de generación de imágenes (DALL·E, Midjourney, Firefly...)',
      'Modelos locales (Ollama, LM Studio...)',
      'Hermes Agent (NousResearch) — agente de IA open source',
      'Agente de IA personalizado (propio o de tu organización)',
      'Ninguna hasta ahora'
    ])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('¿Con qué frecuencia usas tu herramienta principal de IA?')
    .setChoiceValues([
      'Diaria — casi todos los días',
      'Semanal — varias veces por semana',
      'Mensual — de vez en cuando',
      'Esporádica — una o dos veces en los últimos 3 meses',
      'No la he usado aún'
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('¿Hay alguna herramienta que hayas probado y dejado de usar? ¿Por qué?')
    .setRequired(false);

  // ──────────────────────────────────────────────
  // SECCIÓN 3: CASOS DE USO REALES
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('3. Casos de uso reales')
    .setHelpText(
      'Describe situaciones concretas donde hayas usado IA para resolver algo del trabajo.\n' +
      'Para cada caso: (1) Qué tarea hacías, (2) Qué herramienta usaste, (3) Cómo resultó.\n' +
      'Si aún no has usado IA en el trabajo, describe lo que crees que podría resolver.'
    );

  form.addParagraphTextItem()
    .setTitle('Caso 1 — Describe un uso real de IA en tu trabajo')
    .setHelpText('Tarea → Herramienta → Resultado. ¿Requirió varios intentos o salió a la primera?')
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Caso 2 (opcional)')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('Caso 3 (opcional)')
    .setRequired(false);

  form.addMultipleChoiceItem()
    .setTitle('Si AÚN NO usas IA en el trabajo, ¿qué tarea te gustaría que resolviera?')
    .setChoiceValues([
      'Redactar y responder correos / documentos',
      'Analizar datos o generar reportes',
      'Depurar o escribir código',
      'Clasificar tickets o solicitudes de soporte',
      'Buscar información rápidamente',
      'Automatizar tareas repetitivas',
      'Ya uso IA en el trabajo (respondí arriba)'
    ])
    .showOtherOption(true)
    .setRequired(false);

  // ──────────────────────────────────────────────
  // SECCIÓN 4: AUTODIAGNÓSTICO DE NIVEL DE CONDUCCIÓN
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('4. Nivel de conducción AI — Autodiagnóstico')
    .setHelpText(
      'Para cada afirmación, indica qué tan bien te describe hoy.\n' +
      '1 = Nunca lo hago · 5 = Lo hago siempre con total confianza\n\n' +
      'Responde con honestidad — no hay respuestas correctas o incorrectas.'
    );

  var escala = ['1 — Nunca', '2', '3', '4', '5 — Siempre'];

  var afirmaciones = [
    ['🟤 L0-L1 · PERMISO · Uso chatbots como buscador rápido (pregunta → respuesta → cerrar)',
     'Zona del Pasajero: la IA te lleva, tú no conduces todavía.'],
    ['🟤 L1 · PERMISO · Cuando una IA me responde, le doy contexto adicional o le pido que refine',
     'Empiezas a tomar el volante: ajustas, corriges, guías.'],
    ['🟢 L1-L2 · BÁSICA · La IA que uso ya me "recuerda" entre sesiones (preferencias, proyectos activos)',
     'Estableces una relación continua con tu herramienta.'],
    ['🟢 L2-L3 · BÁSICA · Hago que la IA lea archivos de mi equipo (documentos, reportes, contratos locales)',
     'Le das información propia: ya no depende solo de lo que sabe.'],
    ['🔵 L3-L4 · PROFESIONAL · Tengo un "espacio" de IA configurado con conocimiento fijo de mi área',
     'Tu vehículo tiene el mapa de tu territorio cargado.'],
    ['🔵 L4-L5 · PROFESIONAL · La IA se conecta a herramientas que uso (correo, Drive, Slack, ERP...)',
     'Integración: la IA opera dentro de tu ecosistema de trabajo.'],
    ['🔵 L5 · PROFESIONAL · He definido flujos de trabajo reutilizables que la IA sigue al pie de la letra',
     'Playbooks/Skills: instrucciones que la IA ejecuta sin tener que explicarle cada vez.'],
    ['🟣 L6-L7 · AVANZADA · Delego tareas completas a la IA y las recupero terminadas',
     'Piloto automático activado: supervisas el destino, no cada semáforo.'],
    ['🟣 L7 · AVANZADA · La IA ejecuta comandos en terminal o navega en la web por mí',
     'Tu vehículo tiene control sobre otros sistemas.'],
    ['🏆 L8-L9 · INSTRUCTOR · He programado agentes que trabajan solos en horario no laborable',
     'Flota autónoma: tus agentes trabajan mientras duermes.']
  ];

  afirmaciones.forEach(function(af) {
    form.addScaleItem()
      .setTitle(af[0])
      .setHelpText(af[1])
      .setBounds(1, 5)
      .setLabels('Nunca', 'Siempre')
      .setRequired(true);
  });

  form.addMultipleChoiceItem()
    .setTitle('¿Con qué licencia de conducción AI te identificas actualmente?')
    .setHelpText('Elige la que más se acerca a cómo operas hoy, aunque aún no sea perfecta.')
    .setChoiceValues([
      '🟤 Permiso de Aprendizaje — Uso IA con ayuda o de vez en cuando (L0-L1)',
      '🟢 Licencia Básica — La uso sola pero solo en tareas rutinarias (L2-L3)',
      '🔵 Licencia Profesional — Tengo flujos configurados, uso Skills o perfiles (L4-L5)',
      '🟣 Licencia Avanzada — Delego tareas, tengo automatizaciones activas (L6-L7)',
      '🏆 Instructor — Opero agentes autónomos y enseño a otros (L8-L9)'
    ])
    .setRequired(true);

  // ──────────────────────────────────────────────
  // SECCIÓN 5: BLOQUEOS PERCIBIDOS
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('5. Bloqueos para avanzar')
    .setHelpText('¿Qué te frena para usar más IA en tu trabajo diario?\n0 = No me frena · 3 = Es un bloqueo importante.');

  var bloqueos = [
    ['⏱ Tiempo — no tengo espacio para aprender o practicar', ''],
    ['🧠 Conocimiento técnico — no entiendo cómo funciona o qué pedirle', ''],
    ['🤔 Confianza — me preocupa que la respuesta sea incorrecta', ''],
    ['🔒 Seguridad / Privacidad — no sé qué datos puedo usar con IA', ''],
    ['🔧 Acceso / Permisos — no tengo las herramientas necesarias instaladas', ''],
    ['🆘 Soporte — si algo falla, no sé a quién acudir', ''],
    ['🌍 Cultura — siento que "la IA no es para mi rol"', '']
  ];

  bloqueos.forEach(function(b) {
    form.addScaleItem()
      .setTitle(b[0])
      .setBounds(0, 3)
      .setLabels('No me frena', 'Bloqueo importante')
      .setRequired(true);
  });

  form.addParagraphTextItem()
    .setTitle('¿Cuál es tu principal bloqueo y por qué?')
    .setHelpText('De los 7 anteriores, señala el que más te pesa y explica brevemente.')
    .setRequired(false);

  // ──────────────────────────────────────────────
  // SECCIÓN 6: EXPECTATIVAS Y CERTIFICACIÓN
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('6. Expectativas y aspiración de licencia')
    .setHelpText('Última sección — cuéntanos qué quieres lograr con este programa.');

  form.addParagraphTextItem()
    .setTitle('¿Qué esperas lograr al finalizar el piloto?')
    .setHelpText('Una o dos líneas concretas. Ej: "Automatizar el reporte semanal de tickets."')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('¿Qué licencia de conducción AI aspiras obtener al finalizar el piloto?')
    .setChoiceValues([
      '🟢 Licencia Básica — usar IA de forma autónoma en mis tareas diarias',
      '🔵 Licencia Profesional — tener un SOUL/perfil propio y al menos un Skill creado',
      '🟣 Licencia Avanzada — tener automatizaciones activas en mi área',
      '🏆 Instructor — poder certificar y enseñar a otros miembros del equipo'
    ])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Si tuvieras un asistente de IA ideal para tu área, ¿qué 3 tareas haría?')
    .setHelpText('Describe: (1) tarea, (2) tarea, (3) tarea.')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('¿Estarías dispuesto a enseñar lo aprendido a tu equipo al finalizar el piloto?')
    .setChoiceValues([
      'Sí, con gusto',
      'Sí, con condiciones',
      'Probablemente no por ahora'
    ])
    .setRequired(true);

  var checkboxFormato = form.addCheckboxItem();
  checkboxFormato.setTitle('¿Qué formato de aprendizaje prefieres?')
    .setChoiceValues([
      'Sesiones presenciales de 2h',
      'Videos / tutoriales asincrónicos',
      'Documentación escrita (guías, playbooks)',
      'Aprender haciendo (problema real + acompañamiento)',
      'Pair-working con alguien más avanzado'
    ])
    .setRequired(false);

  // ──────────────────────────────────────────────
  // SECCIÓN 7: CIERRE
  // ──────────────────────────────────────────────
  form.addSectionHeaderItem()
    .setTitle('7. Cierre')
    .setHelpText('¡Ya casi terminas!');

  form.addTextItem()
    .setTitle('Área alternativa o comentario adicional (si marcaste "Otra área" arriba)')
    .setRequired(false);

  form.addParagraphTextItem()
    .setTitle('¿Algo más que quieras compartir?')
    .setHelpText('Cualquier comentario, duda o contexto que consideres relevante.')
    .setRequired(false);

  // ──────────────────────────────────────────────
  // 2. CONECTAR HOJA DE RESPUESTAS
  // ──────────────────────────────────────────────
  var ss = SpreadsheetApp.create('Respuestas_Diagnostico_Conduccion_AI');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());

  // Compartir la hoja con el propietario
  ss.addEditor(Session.getActiveUser().getEmail());

  // ──────────────────────────────────────────────
  // 3. LOG DE RESULTADOS
  // ──────────────────────────────────────────────
  var formUrl = form.getPublishedUrl();
  var editUrl = form.getEditUrl();
  var ssUrl = ss.getUrl();

  Logger.log('═══════════════════════════════════════════════');
  Logger.log('✅ FORMULARIO CREADO EXITOSAMENTE');
  Logger.log('═══════════════════════════════════════════════');
  Logger.log('📋 Formulario (responder): ' + formUrl);
  Logger.log('✏️  Formulario (editar):   ' + editUrl);
  Logger.log('📊 Hoja de respuestas:     ' + ssUrl);
  Logger.log('═══════════════════════════════════════════════');
  Logger.log('PRÓXIMOS PASOS:');
  Logger.log('1. Abre el link de edición y ajusta el color/logo institucional');
  Logger.log('2. Configura "Restringir a @ujmd.edu.sv" en Configuración → Respuestas');
  Logger.log('3. Instala el consolidador (consolidador_appsscript.gs) en la hoja de respuestas');
  Logger.log('4. Comparte el link de respuesta con los participantes');
  Logger.log('═══════════════════════════════════════════════');

  // Mostrar también en UI si se ejecuta desde el editor
  SpreadsheetApp.getUi && SpreadsheetApp.getUi().alert(
    '✅ Formulario creado\n\n' +
    'Link para responder:\n' + formUrl + '\n\n' +
    'Revisa el Log (Ver → Registros) para todos los links.'
  );
}


/**
 * ──────────────────────────────────────────────────────────────
 * FUNCIÓN AUXILIAR — CALCULAR NIVEL MCA DESDE RESPUESTAS
 * Úsala en el consolidador una vez tengas respuestas
 * ──────────────────────────────────────────────────────────────
 */
function calcularNivelMCA(puntajeTotal) {
  // puntajeTotal = suma de las 10 preguntas de escala 1-5 (rango: 10-50)
  if (puntajeTotal <= 20) {
    return { nivel: 'L0-L1', licencia: '🟤 Permiso de Aprendizaje', zona: 'Pasajero' };
  } else if (puntajeTotal <= 30) {
    return { nivel: 'L2-L3', licencia: '🟢 Licencia Básica', zona: 'Conductor' };
  } else if (puntajeTotal <= 38) {
    return { nivel: 'L4-L5', licencia: '🔵 Licencia Profesional', zona: 'Conductor Avanzado' };
  } else if (puntajeTotal <= 45) {
    return { nivel: 'L6-L7', licencia: '🟣 Licencia Avanzada', zona: 'Piloto Automático' };
  } else {
    return { nivel: 'L8-L9', licencia: '🏆 Instructor de Conducción', zona: 'Flota Autónoma' };
  }
}
