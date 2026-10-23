# Dirección artística y producción de gráficos

Estado: recomendaciones iniciales pendientes de concretar y validar por el equipo.

## Principio de trabajo

Spanish Simulator tendrá estética pixel art. Las recomendaciones de este documento siguen pendientes de concretar: todavía no están aprobados la paleta, la resolución, los personajes ni el acabado visual final.

Definir un estilo que las dos personas y sus IA puedan repetir, corregir y animar. Las restricciones voluntarias sirven para mantener coherencia y reducir decisiones; no es necesario imitar límites históricos de memoria.

El acceso a herramientas de dibujo no garantiza calidad artística. Una exportación correcta comprueba el funcionamiento técnico, no la legibilidad, la expresividad ni la consistencia del diseño.

**Corrección expresada por Ivan R:** pixel art no significa paredes y suelos planos. El fondo v01 queda descartado por su falta de carácter y su lámpara. Simplificar debe conservar formas, luz, sombras, profundidad y materiales; el número de colores no es un indicador de calidad. La [revisión v02](../arte/escenarios/taberna-v02/README.md) parte del concepto original, reduce microtextura mediante una revisión de imagen y conserva el color en RGB al preparar las exportaciones. Ivan R la ha valorado positivamente; el alcance global de la dirección artística sigue pendiente de acordar.

## Guía visual propuesta

Ivan R ha valorado positivamente el fondo v02 y pidió comprobar la continuidad visual con una mesa. Rechazó la primera mesa por perspectiva incorrecta: igualar materiales no resolvía una cámara distinta. La [revisión v02](../arte/objetos/mesa-redonda-v02/README.md) parte de habitación y mesa juntas, ajusta también las fugas del suelo y separa después los recursos sin recolocarlos. Se documentan la lectura aproximada de horizonte y la revisión del montaje real. La propuesta y el resto de recursos siguen pendientes de valoración; no se ha cerrado el estilo global.

### Revisión de la primera demo por Ivan R · 23 de octubre de 2026

La primera muestra tiene problemas señalados por kapichu: pelo que se percibe separado de algunas cabezas, piernas repetidas, formas demasiado rectas y rígidas, y bordes en las uniones de las piezas articuladas. Su validación técnica no resuelve estos defectos de diseño.

Para la siguiente exploración ha pedido un boceto previo con amigos comiendo tapas alrededor de una mesa redonda normal, diseños variados y un acabado más «cute» y expresivo, afín al carácter de las aventuras SCUMM. El [primer boceto coloreado](../arte/conceptos/mesa-redonda-v01/README.md) usa generación de imágenes y no constituye una dirección artística aprobada ni un recurso pixel art definitivo.

Incorporar estas observaciones a las revisiones: conectar pelo, cabeza y cuello en todas las poses; variar silueta, piernas y apoyos; evitar rigidez geométrica; y mantener el contorno del personaje sin cerrar cada segmento del brazo con una línea oscura. Resolver las uniones mediante superposición o redibujo de la pose cuando proceda. Diseñar y valorar primero la composición y las poses clave antes de repetir la producción de sprites.

### Elementos por acordar

Antes de producir muchos recursos, acordar:

- Una referencia visual principal y unas pocas referencias complementarias.
- Paleta común y función de los colores: materiales, interacción, peligro y estados de interfaz.
- Grosor de los contornos, dirección de la luz y cantidad de tonos de sombra.
- Proporciones, perspectiva y nivel de detalle.
- Escala visual de personajes, objetos, fondos e interfaz.
- Ejemplos de lo aprobado y de lo que se quiere evitar.

Todavía no hay una paleta ni una imagen de referencia aprobadas. Los gráficos recuperados del laboratorio no fijan el estilo del juego.

Se propone una ficha por personaje con silueta y proporciones, paleta, vestuario, vistas necesarias, expresiones, poses principales, animaciones y rasgos que deben conservarse. Su nivel de detalle se decidirá con una prueba de producción.

## Referencia SCUMM para aprender

Ivan S (Alcachofo) ha creado un [visor de recursos SCUMM, enlazado a la sala 7 de Day of the Tentacle](https://scumm.rea.salmeinmotion.com/dott/#room=7). La consulta inicial permite ver escenarios con objetos separados y acceder a personajes, animaciones y audio.

Usarlo para estudiar composición, jerarquía visual, contraste, proporciones, separación de fondos y objetos, reutilización de piezas y ritmo de animación. Registrar qué principio nos sirve y probarlo con diseños propios. El objetivo expresado por el usuario es aprender e inspirarse; no copiar ni incorporar los recursos extraídos al juego.

## Resolución e interfaz

- Elegir la resolución de trabajo y probar los recursos dentro de una pantalla representativa, a su tamaño de uso.
- Si se busca una cuadrícula estricta de píxeles uniformes, usar filtrado nearest y escalas enteras. Decidir expresamente cualquier excepción.
- Construir paneles y botones con piezas reutilizables; considerar nueve secciones para conservar esquinas al cambiar de tamaño.
- Definir estados normal, seleccionado, pulsado y deshabilitado.
- Comprobar tipografía, tildes, textos largos, contraste y tamaños de lectura.
- No comunicar información importante únicamente por color.
- Permitir escalas distintas para texto e interfaz si mejora la lectura y se mantiene una regla visual coherente.

## Método propuesto para trabajar con IA

Tras la valoración positiva de Ivan R del concepto de mesa redonda, el [recorrido propuesto del boceto a una escena jugable](del-concepto-a-jugable.md) concreta la siguiente prueba: conservar composición, gestos y siluetas, reducir detalle y validar una pantalla estática y un personaje antes de producir el elenco. La apreciación positiva del concepto no aprueba su traducción a pixel art ni cierra los puntos 08–10.

La [investigación aplicada a la captura actual de Pagar la cuenta](investigacion-graficos.md) desarrolla la separación de fondo, personajes, mesa, objetos e interfaz; compara alternativas documentadas y mide la ejecución de operaciones repetidas en el MCP local. Sus recomendaciones siguen pendientes de aprobación. Los puntos 08, 10 y 16–22 están en conversación y no cuentan aún como cerrados.

El [plan posterior de la escena de taberna](plan-escena-taberna.md) concreta el alcance solicitado: personajes con animaciones independientes, charla y gesto de pago con cartera, tarjeta o billetes. Camarero aplazado y comida opcional. Su [primera muestra funcional](../prototipos/taberna/README.md) ya permite probar esas acciones, incluido un bocado sencillo. El dibujo se ha programado con Pillow y la producción de originales y exportaciones se ha ejecutado mediante MCP. Es una prueba de este método; la calidad visual sigue pendiente de valoración y no se ha elegido una dirección artística definitiva.

1. Partir de una referencia aprobada y del recurso maestro más cercano.
2. Revisar primero la silueta y las proporciones.
3. Diseñar masas de color y sombras que describan el volumen; añadir detalles selectivos que sobrevivan al tamaño de uso.
4. Revisar cada pasada al tamaño de uso y compararla con los recursos aprobados.
5. Animar una vez que el diseño base funcione.

Una silueta confusa debe corregirse antes de añadir texturas. Favorecer variaciones de una base aprobada frente a rediseños independientes de cada objeto.

MCP puede servir para inspeccionar y realizar cambios concretos. Lua puede servir para operaciones repetidas y exportaciones por lotes. Pillow puede generar imágenes que después se ensamblen en Aseprite. Su eficiencia relativa todavía no se ha medido en este proyecto.

La generación de imágenes puede ayudar a explorar conceptos; comprobar cuadrícula, continuidad y posibilidad de edición antes de utilizar el resultado como recurso definitivo.

## Animación

La [prueba de cuatro tapas](../arte/objetos/tapas-v01/README.md) amplía el montaje con recursos independientes. Se detectó que la extracción generativa cambiaba escala/encuadre: se ajustaron contra la composición conjunta antes de montar sobre la mesa original. El proceso debe comprobar esos cambios, además de perspectiva, apoyo y luz. No asumir alineación exacta porque se pidió en el prompt. La comida de cada plato es por ahora una imagen; la animación de consumo necesitará variantes o bocados separados.

El [fondo independiente actual, v02](../arte/escenarios/taberna-v02/README.md), está disponible como PNG y original Aseprite RGB: 640×360, sin personajes ni mesa. Sustituye como propuesta al fondo v01 descartado por Ivan R. Combina generación de imagen con preparación/exportación mediante MCP, conservando color y sombras. Estas características técnicas no suponen aprobación artística ni elección definitiva de resolución/paleta.

Se han creado [dos tratamientos simplificados de la mesa redonda](../arte/conceptos/mesa-redonda-v02/README.md). El visor los presenta a 640×360; los archivos generados son mayores y no cumplen todavía una cuadrícula/paleta de producción. Valorar esta comparación antes de preparar originales separados o animaciones. La variante A tiene menos detalle que B, pero aún requiere limpieza y redibujo para producción.

- Elegir siluetas claras y rasgos identificativos que puedan conservarse en cada pose.
- Aprobar primero las poses principales y el ritmo, después completar el movimiento.
- Mantener un punto de apoyo y una alineación coherentes entre fotogramas cuando la acción lo requiera.
- Conservar volumen, paleta y detalles identificativos durante el movimiento.
- Presupuestar acciones y direcciones: cuatro direcciones, seis acciones y ocho fotogramas implican 192 fotogramas por personaje antes de considerar reutilización.
- Distinguir un desplazamiento o una deformación de una pieza rígida de una acción que necesita poses nuevas.

## Primera prueba propuesta

Crear una pantalla representativa con un personaje animado, unos objetos y una interfaz funcional. Comprobar estética, legibilidad, coherencia, rendimiento y coste de producción.

Comparar MCP y Lua con el mismo sprite y una animación de reposo. Un tamaño de 32×32 fue sugerido como ejemplo; ajustarlo a la propuesta visual antes de comenzar.

Registrar tiempo total, número de llamadas, facilidad de corregir una parte, coherencia entre fotogramas y exportación. Medir rendimiento en la plataforma objetivo: la baja resolución no garantiza por sí sola un juego rápido.

Medir también tokens o coste de API cuando estén disponibles, tiempo hasta un resultado aceptable, número de revisiones y retoque manual. Comparar los métodos con la misma tarea y referencias: no afirmar eficiencia sin medir. El equipo debe fijar un presupuesto y criterios de aceptación antes de producir grandes cantidades de recursos.

## Referencias consultadas

- [Pixel art y animación, de Pedro Medeiros / Saint11](https://saint11.art/blog/pixel-art-tutorials/).
- [Resoluciones y escalado en Godot](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html). Referencia técnica; no supone que se haya elegido Godot.
- [Paneles de nueve secciones en Godot](https://docs.godotengine.org/en/stable/classes/class_ninepatchrect.html).
- [Exportación por línea de comandos en Aseprite](https://www.aseprite.org/docs/cli/).
