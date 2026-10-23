# Contexto y decisiones

Actualizado: 23 de octubre de 2026.

## Confirmado por el usuario

- El juego se llama **Spanish Simulator** y tendrá estética pixel art.
- La jugabilidad se basa en minijuegos conectados entre sí con tópicos españoles.
- Algunos o todos los minijuegos podrán jugarse colaborativamente, con una pantalla compartida y móviles que se conectan mediante un código QR. Falta concretar los modos y sus límites.
- El primer minijuego conceptual es **Pagar la cuenta**, disponible en [el prototipo web](https://spanish-simulator.salmeinmotion.com/).
- El equipo está formado por **Ivan R (kapichu)**, usuario de este chat, e **Ivan S (Alcachofo)**. Desarrollarán el juego con ayuda de sus respectivas IA; sus roles siguen pendientes de concretar.
- Los intentos gráficos anteriores no han resultado suficientemente satisfactorios y se quiere mejorar el método de producción.
- Importan especialmente la estética, el rendimiento, la facilidad para animar y la capacidad de la IA para generar diseños atractivos y consistentes.
- Ahorrar espacio como en los juegos antiguos no es la prioridad.
- Se quiere investigar cómo usar Aseprite, aseprite-mcp y herramientas relacionadas para crear gráficos de forma eficiente.
- Se ha elegido este repositorio para publicar las instrucciones y el contexto elaborado hasta ahora, de manera que el otro participante y su IA puedan consultarlos.
- El usuario ha pedido ir subiendo el contexto y los acuerdos de las conversaciones a este repositorio.
- Ivan S (Alcachofo) ha creado una [herramienta de exploración de recursos SCUMM](https://scumm.rea.salmeinmotion.com/dott/#room=7). Se usará como inspiración y para aprender principios de diseño; el usuario ha indicado que no se busca copiar esos recursos.
- Ivan R ha pedido numerar las decisiones y mostrar el progreso de acuerdos, partiendo de un 0 % en las decisiones de detalle.

## Requisitos parciales de la muestra de taberna

Confirmados por **Ivan R (kapichu)** el 23 de octubre de 2026 al solicitar el plan. No se atribuyen a Ivan S ni cierran el alcance completo de sus decisiones principales.

| Referencia | Requisito |
| --- | --- |
| 02.1 | El camarero se incorporará después; queda fuera de esta primera entrega. |
| 10.1 | Cada personaje podrá levantar la mano para pagar sujetando cartera, tarjeta o billetes. |
| 10.2 | Prever charla ambiental; comer queda como posibilidad. |
| 18.1 | Los personajes se animarán de forma independiente entre sí. |
| 20.1 | Usar aseprite-mcp en la creación y revisión de esta escena. |

El [plan de producción](plan-escena-taberna.md) desarrolla cómo podría hacerse. Sus propuestas de estética, dimensiones, capas, tiempos y herramientas siguen pendientes de validar. Los subpuntos no añaden peso al contador; este continúa en 0/22.

## Realizado en el laboratorio local

- Las carpetas de Aseprite, aseprite-live, aseprite-mcp y sus dependencias se han reunido bajo una carpeta de trabajo común.
- Se han reparado las rutas locales y se han comprobado el editor, el servidor MCP, el visor y las exportaciones de los proyectos existentes.
- La documentación del proyecto está publicada y se mantiene en este repositorio. Las herramientas y los gráficos locales no se han incorporado.
- El 23 de octubre de 2026 se abrió el prototipo web: se observó la sala con QR y código, la lista de jugadores y las instrucciones para tocar y deslizar desde el móvil. No se ha validado una partida multijugador completa ni su arquitectura interna.
- En la herramienta SCUMM se observó la sala 7 de Day of the Tentacle y las secciones de escenarios, personajes/animaciones y música/sonidos. Esta consulta no supone elegir ese estilo para Spanish Simulator.
- Ivan R aportó una captura de la escena actual de Pagar la cuenta y pidió investigar un proceso más eficaz, planteando separar el fondo. La petición no supone aprobar el estilo de esa captura ni una separación de recursos concreta.
- Se realizó una prueba sintética del MCP local: 20 rectángulos mediante llamadas individuales frente a una llamada con un lote Lua. Las medianas fueron 5,476 s y 0,263 s, con píxeles idénticos en tres rondas. La [investigación](investigacion-graficos.md) documenta condiciones y límites; no se midió calidad artística ni ahorro de tokens.

## Pendiente de decidir con el equipo

El [README](../README.md#decisiones-que-necesitamos-tomar) contiene la lista de referencia con números, alcance y estado de cada decisión. Los puntos **01–15** cubren el juego; los **16–22**, la documentación y producción de gráficos con IA.

El seguimiento se inicia con **0 de 22 decisiones cerradas (0 %)**. Los acuerdos generales de la sección anterior se mantienen y no forman parte de ese denominador. El estado actual se consulta en las tablas y la barra del README para evitar contadores que diverjan entre documentos.

## Cómo registrar y medir un acuerdo

- Referirse siempre al número estable del README, por ejemplo **04: plataformas y distribución** o **17: fichas de personaje**.
- Usar los estados **Pendiente**, **En conversación** y **Acordada**. Solo el último cuenta como cierre; una propuesta o un acuerdo parcial no cierra todo el punto.
- Al cerrar un punto, registrar elección, motivo, quién la confirma y fecha, y actualizar su fila y el progreso global del README. No atribuir la aprobación a ambos integrantes si solo consta la de uno.
- El porcentaje de acuerdos es `puntos acordados / puntos totales × 100`, con el mismo peso para cada punto. No mide desarrollo ni esfuerzo invertido.
- Si se reabre una decisión, conservar el motivo y dejar de contarla como cerrada.
- Añadir nuevos puntos principales al final sin renumerar los existentes y reflejar el nuevo total. Los subpuntos como `08.1` precisan el alcance del 08 y no añaden peso al contador; cerrar el principal cuando se resuelvan sus subpuntos necesarios.

Para desarrollar un punto, registrar:

| Campo | Contenido |
| --- | --- |
| Número y tema | El identificador del README. |
| Estado | Pendiente, En conversación o Acordada. |
| Propuesta y alternativas | Qué se plantea y qué falta por resolver. |
| Elección y motivo | Completar cuando se confirme. |
| Participantes | Quién propone, quién confirma y quién asume el trabajo, si se ha asignado. |
| Fecha y evidencia | Cuándo se acordó y qué prueba o referencia lo sustenta, si corresponde. |

Todavía no se ha registrado un cierre de los puntos 01–22.

## Investigación gráfica en conversación

Los puntos **02, 08, 09, 10 y 16–22** están **En conversación** a raíz de la investigación y el plan sobre la escena actual. El porcentaje de cierre de cada uno sigue en 0 % y el global continúa en 0/22. La organización concreta de capas, el estilo y las herramientas adicionales candidatas son propuestas del asistente. Los requisitos parciales expresados por Ivan R se recogen arriba.

La prueba artística actual propuesta es una composición, un fondo limpio, una mesa independiente y un personaje con reposo, charla y pago con tarjeta, cartera y billetes. Comer es opcional y se pospone; camarero y esquivar quedan fuera de esta primera muestra. Falta producirla, evaluar el resultado visual y acordar el método; no confundir la medición de rectángulos con esa validación.

## Propuestas pendientes de validar

- Crear una guía visual corta con ejemplos aprobados y una biblioteca pequeña de recursos maestros.
- Validar una pantalla representativa antes de producir muchos recursos.
- Comparar MCP y Lua realizando el mismo recurso y midiendo tiempo, llamadas, calidad visual y facilidad de corrección.
- Trabajar con ramas y revisión de cambios antes de incorporarlos a la rama principal.
- Automatizar exportaciones de los originales editables a formatos que pueda usar el motor.

Los ejemplos de personajes de 32×32, paletas de 24–32 colores o animaciones con un número determinado de fotogramas son puntos de partida para pruebas. No son requisitos del juego.

## Mantenimiento del contexto

Cuando el equipo confirme una propuesta, trasladarla a decisiones confirmadas con una explicación breve. Registrar los cambios relevantes y su motivo, actualizar el README si cambia el resumen y subir la documentación a GitHub. Evitar copiar conversaciones enteras o guardar como acuerdos las suposiciones del asistente.
