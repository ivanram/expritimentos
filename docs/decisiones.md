# Contexto y decisiones

Actualizado: 23 de octubre de 2026.

## Confirmado por el usuario

- El juego se llama **Spanish Simulator** y tendrá estética pixel art.
- La jugabilidad se basa en minijuegos conectados entre sí con tópicos españoles.
- Algunos o todos los minijuegos podrán jugarse colaborativamente, con una pantalla compartida y móviles que se conectan mediante un código QR. Falta concretar los modos y sus límites.
- El primer minijuego conceptual es **Pagar la cuenta**, disponible en [el prototipo web](https://spanish-simulator.salmeinmotion.com/).
- Se quiere desarrollar un juego entre dos personas, con ayuda de sus respectivas IA.
- Los intentos gráficos anteriores no han resultado suficientemente satisfactorios y se quiere mejorar el método de producción.
- Importan especialmente la estética, el rendimiento, la facilidad para animar y la capacidad de la IA para generar diseños atractivos y consistentes.
- Ahorrar espacio como en los juegos antiguos no es la prioridad.
- Se quiere investigar cómo usar Aseprite, aseprite-mcp y herramientas relacionadas para crear gráficos de forma eficiente.
- Se ha elegido este repositorio para publicar las instrucciones y el contexto elaborado hasta ahora, de manera que el otro participante y su IA puedan consultarlos.
- El usuario ha pedido ir subiendo el contexto y los acuerdos de las conversaciones a este repositorio.
- El compañero ha creado una [herramienta de exploración de recursos SCUMM](https://scumm.rea.salmeinmotion.com/dott/#room=7). Se usará como inspiración y para aprender principios de diseño; el usuario ha indicado que no se busca copiar esos recursos.

## Realizado en el laboratorio local

- Las carpetas de Aseprite, aseprite-live, aseprite-mcp y sus dependencias se han reunido bajo una carpeta de trabajo común.
- Se han reparado las rutas locales y se han comprobado el editor, el servidor MCP, el visor y las exportaciones de los proyectos existentes.
- La documentación del proyecto está publicada y se mantiene en este repositorio. Las herramientas y los gráficos locales no se han incorporado.
- El 23 de octubre de 2026 se abrió el prototipo web: se observó la sala con QR y código, la lista de jugadores y las instrucciones para tocar y deslizar desde el móvil. No se ha validado una partida multijugador completa ni su arquitectura interna.
- En la herramienta SCUMM se observó la sala 7 de Day of the Tentacle y las secciones de escenarios, personajes/animaciones y música/sonidos. Esta consulta no supone elegir ese estilo para Spanish Simulator.

## Pendiente de decidir con el equipo

- Mecánicas concretas, catálogo de minijuegos, conexión entre ellos y alcance de la primera versión.
- Modos cooperativo, competitivo o mixto, número de jugadores y posibilidad de jugar en solitario.
- Plataformas para la pantalla principal, dispositivos/navegadores del mando móvil y controles alternativos.
- Motor, tecnología de interfaz, comunicación en tiempo real, alojamiento y costes operativos.
- Gestión de salas, incorporación de jugadores, desconexiones, reconexión y sincronización.
- Perspectiva, resolución de trabajo, escalado y tamaños de los recursos.
- Referencias visuales aprobadas, paleta, contornos, iluminación y proporciones.
- Cantidad de personajes, direcciones y animaciones.
- Personalidad y fichas de los personajes, tono de humor, textos, idiomas, música y efectos de sonido.
- Accesibilidad, rendimiento mínimo y condiciones para considerar validado cada minijuego.
- Método de producción con IA, presupuesto de tiempo/tokens/coste, recursos maestros y criterios de calidad.
- Reparto de tareas y quién resuelve los desacuerdos artísticos.

El [README](../README.md) contiene el mapa de decisiones y un orden de trabajo propuesto.

## Propuestas pendientes de validar

- Crear una guía visual corta con ejemplos aprobados y una biblioteca pequeña de recursos maestros.
- Validar una pantalla representativa antes de producir muchos recursos.
- Comparar MCP y Lua realizando el mismo recurso y midiendo tiempo, llamadas, calidad visual y facilidad de corrección.
- Trabajar con ramas y revisión de cambios antes de incorporarlos a la rama principal.
- Automatizar exportaciones de los originales editables a formatos que pueda usar el motor.

Los ejemplos de personajes de 32×32, paletas de 24–32 colores o animaciones con un número determinado de fotogramas son puntos de partida para pruebas. No son requisitos del juego.

## Mantenimiento del contexto

Cuando el equipo confirme una propuesta, trasladarla a decisiones confirmadas con una explicación breve. Registrar los cambios relevantes y su motivo, actualizar el README si cambia el resumen y subir la documentación a GitHub. Evitar copiar conversaciones enteras o guardar como acuerdos las suposiciones del asistente.
