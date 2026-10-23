# Colaboración entre dos personas y sus IA

Estado: propuesta inicial de organización; los roles y el flujo definitivo están pendientes de acordar.

## Compartir el contexto

Mantener objetivos, decisiones y reglas artísticas en documentos versionados. Cada participante trabaja con una copia actualizada del repositorio y proporciona a su IA acceso a esa copia o a los documentos relevantes.

Los chats privados no se comparten automáticamente. Para transmitir un acuerdo, resumirlo en el documento correspondiente, subir el cambio y actualizar la copia del otro participante. Distinguir siempre acuerdos y propuestas. El usuario ha pedido que se vayan publicando en GitHub el contexto relevante y los acuerdos de estas conversaciones.

`AGENTS.md` es el punto de entrada para asistentes compatibles. Si una herramienta necesita otro archivo de instrucciones, dirigirlo a la misma documentación para evitar reglas duplicadas que terminen divergiendo. Se desconoce qué IA usará el otro participante.

En Codex, el reconocimiento de `AGENTS.md` está documentado en la [guía oficial de instrucciones del proyecto](https://learn.chatgpt.com/docs/agent-configuration/agents-md). No asumir que todas las herramientas cargan automáticamente todos los documentos del repositorio.

## Flujo de cambios propuesto

1. Actualizar la copia de trabajo y revisar si otra persona está modificando los mismos archivos.
2. Preparar una tarea concreta en una rama.
3. Revisar los cambios y, cuando haya gráficos, adjuntar o consultar una vista previa.
4. Presentar los cambios para revisión antes de incorporarlos a la rama principal.
5. Actualizar la documentación cuando se confirme una decisión que afecte a trabajos posteriores.

El usuario ha autorizado publicar directamente la documentación y mantenerla actualizada en el repositorio. El uso de ramas y revisión para el desarrollo del juego sigue siendo una propuesta pendiente de acordar entre los dos participantes.

## Recursos gráficos

- Guardar originales editables `.aseprite` y distinguirlos de PNG, JSON y otras exportaciones.
- Repartir los archivos gráficos para evitar ediciones simultáneas difíciles de fusionar.
- Definir nombres, capas, etiquetas de animación y formatos de exportación cuando se elija el motor y se inicie la producción.
- Revisar cada recurso dentro de la pantalla del juego y junto a los recursos ya aprobados.
- Acordar quién resuelve bloqueos de dirección artística.

## Herramientas locales

No incorporar compilaciones, dependencias completas ni entornos virtuales al repositorio por defecto. Documentar su preparación y automatizar lo que sea útil para que ambos ordenadores puedan reproducir el flujo.

La primera publicación contiene documentación. Añadir código, gráficos o herramientas compartidas debe hacerse como una tarea explícita, revisando las exclusiones actuales de `.gitignore`.
