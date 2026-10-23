# Del concepto de mesa redonda a una escena jugable

23 de octubre de 2026. Propuesta del asistente tras la valoración positiva de Ivan R del boceto como arte conceptual. Ivan R pide conservar su sensación con gráficos mucho más simplificados. No implica aprobación del elenco, la resolución, la paleta, el motor ni las reglas definitivas; tampoco se atribuye esa valoración a Ivan S.

## Qué conservar y qué simplificar

Conservar la cercanía de los amigos, sus miradas y gestos, siluetas diferentes, formas orgánicas, mesa compacta, luz cálida y contraste con la ventana fría. Esos elementos deben sostener el ambiente cuando se elimine el detalle.

Simplificar textura pictórica, reflejos, pliegues pequeños, decoración y cantidad de tonos. Mantener pocos rasgos decisivos por persona y grandes masas de color. Reducir o pixelar automáticamente la ilustración puede servir de estudio, pero no garantiza un recurso legible, editable ni animable. Hay que diseñar su traducción al tamaño de juego.

## Secuencia propuesta

| Paso | Entrega pequeña | Condición para avanzar |
| --- | --- | --- |
| 1. Pantalla estática simplificada | Dos tratamientos de la misma composición: uno de colores muy planos y otro con algo más de volumen. Probar inicialmente a 640×360, como hipótesis reutilizable del visor. | Miradas, cinco identidades y mano de pago legibles al tamaño de uso; sensación cálida y orgánica conservada. Valorar junto al concepto. |
| 2. Escena preparada para movimiento | Fondo limpio, mesa/objetos y cinco siluetas en sus plazas; poses provisionales de pago para todas, antes de detallarlas. | Los brazos tienen recorrido y los objetos se distinguen en plazas delanteras y traseras; las superposiciones funcionan. |
| 3. Un personaje maestro | Un personaje representativo diseñado en su plaza, con reposo, charla y subida/oferta/bajada de tarjeta. | Misma identidad y volumen en todas las poses, pelo unido, hombros continuos, apoyo estable y gesto legible. La oferta puede sostenerse y cancelarse. |
| 4. Prueba interactiva pequeña | Ese personaje responde al teclado o botón dentro de la escena simplificada; los otros cuatro permanecen como dibujos estáticos. | Respuesta inmediata, cancelación desde una pose intermedia, orden correcto de mesa/brazo/objeto y ausencia de saltos. |
| 5. Extender a los cinco | Aplicar el lenguaje visual acordado a cuerpos y posturas distintos; añadir cartera y billetes, charla y después comida. | Cinco relojes independientes, diferentes combinaciones simultáneas y calidad consistente, sin copiar piernas o cuerpos. |
| 6. Integrar el minijuego | Conectar los estados visuales a las reglas y controles acordados o a los del prototipo existente tras revisar su implementación. | Un ciclo de partida pequeño y completo con inicio, acciones, respuesta y resultado comprensible. Después, probar móviles y sincronización. |

Una escena con botones que reproduce animaciones permite interactuar, pero no demuestra todavía un minijuego completo ni multijugador. El camarero sigue aplazado; la regla de una primera partida sin él se deberá concretar en el punto 02 antes de implementarla. No inventar reglas definitivas como efecto secundario de una prueba de arte.

La resolución inicial facilita comparar dentro del visor existente; no explica ni corrige por sí misma los defectos artísticos anteriores. Ajustarla si las caras, objetos o la composición no se leen. La interfaz debe tener espacio reservado y puede usar una escala legible independiente según lo que se acuerde.

## Preparar las piezas sin crear una marioneta

### Aclaración del proceso tras comparar A y B

Ivan R plantea producir primero el fondo en pixel art y animar después cada personaje por separado. La recomendación del asistente es seguir esa organización: las composiciones generadas son referencias de diseño; el siguiente recurso de producción propuesto es un fondo limpio, sin personajes, dibujado a la resolución elegida. Fijar antes la posición de mesa, sillas y figuras con siluetas provisionales para que el fondo deje sitio a la acción.

Mantener la mesa y los objetos que necesiten superposición como recursos separados del fondo. Cada personaje tendrá un original editable y sus propias poses, clips y reloj de reproducción. La independencia entre personajes no obliga a construir sus cuerpos como piezas rígidas articuladas: dibujar las poses necesarias con silueta continua, especialmente hombro y brazo. Probar primero un personaje dentro de la escena antes de producir los demás.

Esto aclara la propuesta de producción; no implica que el fondo limpio o los nuevos originales animados ya existan, ni que se haya aprobado A, B, una resolución o el elenco.

El concepto generado es una imagen plana. Recortar sus figuras no revela lo que hay detrás: habrá que reconstruir fondo, cuerpos, sillas y objetos ocultos por otras piezas. Los originales deben contener margen y zonas ocultas suficientes para las acciones previstas.

Separar personajes entre sí no obliga a separar cada hueso en un sprite. Para esta prueba se propone dibujar las poses de torso y brazo como formas continuas, reutilizando solo las zonas que no cambian. Separar objetos de pago y dedos cuando ayude al agarre; ocultar o redibujar uniones en lugar de cerrar con contorno oscuro cada segmento. El fondo puede ser una imagen estática; la mesa y sus objetos deben separarse en las pasadas que requieran las superposiciones de cada plaza.

La mesa redonda exige distintas vistas y superposiciones. No resolverla con cinco muñecos frontales ni espejar una animación sin comprobar manos, ropa y perspectiva. Ensayar primero poses simples de pago en todas las plazas evita animar un personaje bonito que después no funciona en la composición.

## Papel de la IA y de Aseprite MCP

La generación de imágenes se propone para explorar la simplificación y preparar referencias coherentes a partir del boceto. No asumir que producirá cuadrícula exacta, capas limpias o fotogramas consistentes sin revisión. Tras elegir una referencia, mantener una ficha corta con silueta, proporciones, colores y poses; evitar regenerar la escena completa por cada acción.

Aseprite MCP y Lua se usarían para montar y editar originales, organizar capas y etiquetas, comprobar poses y automatizar exportaciones. Su uso no sustituye las decisiones de dibujo. Aseprite permite organizar animaciones por rangos etiquetados y exportar hojas por capas/etiquetas: [animación](https://www.aseprite.org/docs/animation/) y [hojas de sprites](https://www.aseprite.org/docs/sprite-sheet/).

El reproductor del visor actual puede servir como banco de pruebas, conservando los estados independientes y adaptando anclajes y superposiciones a los recursos nuevos. Esto no elige la tecnología del juego definitivo.

## Evitar trabajo repetido

Revisar una pantalla y un personaje antes de fabricar los cinco. Tras cada entrega, guardar referencia, cambios y criterio visual; medir tiempo hasta aceptación, revisiones y retoque, además de llamadas y tokens cuando esos datos existan. La guía visual inicial puede limitarse a una página con ejemplos aprobados y defectos que evitar.

**Primera entrega realizada:** [dos tratamientos estáticos de la mesa redonda](../arte/conceptos/mesa-redonda-v02/README.md), uno relativamente más plano y otro con más volumen, con visor comparativo a 640×360. Son referencias generadas, no sprites nativos: la paleta y la cuadrícula exactas no se han obtenido. Su valoración y la selección de un tratamiento siguen pendientes antes de producir animaciones.
