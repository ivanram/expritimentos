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

- A petición de Ivan R se creó un primer fondo independiente, que rechazó por su simplificación excesiva y la lámpara. Se ha preparado la [revisión v02](../arte/escenarios/taberna-v02/README.md), sin personajes ni mesa, a 640×360 en RGB, con PNG, ampliación y original Aseprite. Conserva luz y volumen mediante una nueva generación y revisión de textura, seguida de preparación/exportación por MCP sin cuantización. Su valoración y la composición con los futuros personajes siguen pendientes; estos parámetros de prueba no cierran decisiones.

- Las carpetas de Aseprite, aseprite-live, aseprite-mcp y sus dependencias se han reunido bajo una carpeta de trabajo común.
- Se han reparado las rutas locales y se han comprobado el editor, el servidor MCP, el visor y las exportaciones de los proyectos existentes.
- La documentación del proyecto está publicada y se mantiene en este repositorio. Las herramientas y los gráficos locales no se han incorporado.
- El 23 de octubre de 2026 se abrió el prototipo web: se observó la sala con QR y código, la lista de jugadores y las instrucciones para tocar y deslizar desde el móvil. No se ha validado una partida multijugador completa ni su arquitectura interna.
- En la herramienta SCUMM se observó la sala 7 de Day of the Tentacle y las secciones de escenarios, personajes/animaciones y música/sonidos. Esta consulta no supone elegir ese estilo para Spanish Simulator.
- Ivan R aportó una captura de la escena actual de Pagar la cuenta y pidió investigar un proceso más eficaz, planteando separar el fondo. La petición no supone aprobar el estilo de esa captura ni una separación de recursos concreta.
- Se realizó una prueba sintética del MCP local: 20 rectángulos mediante llamadas individuales frente a una llamada con un lote Lua. Las medianas fueron 5,476 s y 0,263 s, con píxeles idénticos en tres rondas. La [investigación](investigacion-graficos.md) documenta condiciones y límites; no se midió calidad artística ni ahorro de tokens.
- Ivan R autorizó ejecutar el plan para probar su viabilidad y resultado. Se ha construido [una muestra local](../prototipos/taberna/README.md) con cinco actores independientes, charla, comida sencilla y pago con tres tipos de objeto, sin camarero. Se publican su código, nueve originales `.aseprite` y exportaciones; los experimentos antiguos y las herramientas instaladas siguen fuera del repositorio.
- La prueba usa arte original programado con Pillow y llamadas reales a MCP para importar, montar, etiquetar, auditar y exportar. No se ha utilizado generación de imágenes ni recursos extraídos de SCUMM en esa muestra. El detalle de herramientas y tiempos está en `prototipos/taberna/produccion-mcp.json`.

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

El 24 de octubre de 2026 Ivan R ha indicado que no quiere pagar por más IAs. Se registra como restricción del flujo investigado: sin nuevas suscripciones ni APIs de pago adicionales. Se prioriza una prueba de dibujo nativo automatizado con el Aseprite MCP disponible; los proveedores especializados quedan como investigación, no como dependencias elegidas. No se atribuye esa restricción a Ivan S ni se considera cerrado el presupuesto global del proyecto.

Ivan R ha insistido en que el objetivo es crear pixel art real con IA de forma eficaz; redibujarlo todo a mano no cumpliría el propósito. El asistente reconoce que las tapas generadas/reducidas no demuestran ese flujo. Se documentan [vías y candidatos para una prueba nativa](automatizar-pixelart.md): PixelLab y Retro Diffusion aún sin conectar/probar, y dibujo automatizado mediante el MCP disponible. No se ha elegido proveedor ni presupuesto y el contador permanece en 0/22.

Ivan R pidió demostrar el proceso añadiendo croquetas, bravas, calamares y aceitunas a la mesa. Se ha creado una [composición con cuatro tapas separadas](../arte/objetos/tapas-v01/README.md), sobre el montaje original, con prueba de retirada de un plato. La valoración de esta entrega sigue pendiente; no implica aprobación de la mesa, dirección artística o sistema de animación.

Ivan R ha valorado positivamente el fondo v02 y ha pedido probar el mismo lenguaje visual en otros elementos, empezando por la mesa. Rechazó la mesa v01 por perspectiva incorrecta y exigió que el asistente detectase esos fallos antes de presentar resultados. Se ha creado una [revisión de composición y mesa v02](../arte/objetos/mesa-redonda-v02/README.md), resolviendo habitación/mesa juntas y separando después los recursos. Incluye una cámara revisada; su valoración y la composición con cinco actores siguen pendientes. No se atribuye aprobación a Ivan S y el progreso continúa en 0/22.

Ivan R valora positivamente el boceto de mesa redonda como arte conceptual y pide transmitir el mismo ambiente con gráficos simplificados. Autorizó iniciar el [recorrido propuesto](del-concepto-a-jugable.md) y ya se han preparado [dos tratamientos estáticos](../arte/conceptos/mesa-redonda-v02/README.md), comparables en un visor a 640×360. Son referencias generadas, sin cuadrícula y paleta de producción verificadas; su selección y los parámetros definitivos siguen pendientes. La valoración no se atribuye a Ivan S y el contador continúa en 0/22.

El 23 de octubre de 2026, Ivan R revisó la demo y señaló pelo que parece flotar, piernas repetidas, diseños rígidos y contornos en piezas articuladas. Pidió un boceto previo con una mesa redonda, personajes más variados y un acabado más «cute» y expresivo. Se ha creado [una ilustración de concepto](../arte/conceptos/mesa-redonda-v01/README.md) con generación de imágenes. Está pendiente de valoración; no sustituye los sprites ni cierra dirección artística, elenco o animación.

Los puntos **02, 08, 09, 10 y 16–22** están **En conversación** a raíz de la investigación y el plan sobre la escena actual. El porcentaje de cierre de cada uno sigue en 0 % y el global continúa en 0/22. La organización concreta de capas, el estilo y las herramientas adicionales candidatas son propuestas del asistente. Los requisitos parciales expresados por Ivan R se recogen arriba.

La primera muestra ya permite probar la composición, el fondo y la mesa independientes, cinco actores con reposo y charla y el pago con tarjeta, cartera y billetes. Incluye comida sencilla; camarero y esquivar quedan fuera. Falta evaluar el resultado visual y acordar si este método y acabado sirven para producción. La autorización de construir el ensayo no equivale a aprobar su estética ni a cerrar los puntos 01–22.

Ivan R pidió publicar esta muestra para que Alcachofo pudiera verla y destacar su acceso al principio del README. La [demo pública](https://spanish-simulator-ultima-ronda.ivanra.chatgpt.site) se publicó el 23 de octubre de 2026. Esta publicación no fija la plataforma ni la tecnología del juego definitivo.

## Propuestas pendientes de validar

- Crear una guía visual corta con ejemplos aprobados y una biblioteca pequeña de recursos maestros.
- Validar una pantalla representativa antes de producir muchos recursos.
- Comparar MCP y Lua realizando el mismo recurso y midiendo tiempo, llamadas, calidad visual y facilidad de corrección.
- Trabajar con ramas y revisión de cambios antes de incorporarlos a la rama principal.
- Automatizar exportaciones de los originales editables a formatos que pueda usar el motor.

Los ejemplos de personajes de 32×32, paletas de 24–32 colores o animaciones con un número determinado de fotogramas son puntos de partida para pruebas. No son requisitos del juego.

## Mantenimiento del contexto

Cuando el equipo confirme una propuesta, trasladarla a decisiones confirmadas con una explicación breve. Registrar los cambios relevantes y su motivo, actualizar el README si cambia el resumen y subir la documentación a GitHub. Evitar copiar conversaciones enteras o guardar como acuerdos las suposiciones del asistente.
