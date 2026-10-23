# Dirección artística y producción de gráficos

Estado: recomendaciones iniciales pendientes de concretar y validar por el equipo.

## Principio de trabajo

Definir un estilo que las dos personas y sus IA puedan repetir, corregir y animar. Las restricciones voluntarias sirven para mantener coherencia y reducir decisiones; no es necesario imitar límites históricos de memoria.

El acceso a herramientas de dibujo no garantiza calidad artística. Una exportación correcta comprueba el funcionamiento técnico, no la legibilidad, la expresividad ni la consistencia del diseño.

## Guía visual propuesta

Antes de producir muchos recursos, acordar:

- Una referencia visual principal y unas pocas referencias complementarias.
- Paleta común y función de los colores: materiales, interacción, peligro y estados de interfaz.
- Grosor de los contornos, dirección de la luz y cantidad de tonos de sombra.
- Proporciones, perspectiva y nivel de detalle.
- Escala visual de personajes, objetos, fondos e interfaz.
- Ejemplos de lo aprobado y de lo que se quiere evitar.

Todavía no hay una paleta ni una imagen de referencia aprobadas. Los gráficos recuperados del laboratorio no fijan el estilo del juego.

## Resolución e interfaz

- Elegir la resolución de trabajo y probar los recursos dentro de una pantalla representativa, a su tamaño de uso.
- Si se busca una cuadrícula estricta de píxeles uniformes, usar filtrado nearest y escalas enteras. Decidir expresamente cualquier excepción.
- Construir paneles y botones con piezas reutilizables; considerar nueve secciones para conservar esquinas al cambiar de tamaño.
- Definir estados normal, seleccionado, pulsado y deshabilitado.
- Comprobar tipografía, tildes, textos largos, contraste y tamaños de lectura.
- No comunicar información importante únicamente por color.
- Permitir escalas distintas para texto e interfaz si mejora la lectura y se mantiene una regla visual coherente.

## Método propuesto para trabajar con IA

1. Partir de una referencia aprobada y del recurso maestro más cercano.
2. Revisar primero la silueta y las proporciones.
3. Aplicar colores planos, sombras y finalmente detalles.
4. Revisar cada pasada al tamaño de uso y compararla con los recursos aprobados.
5. Animar una vez que el diseño base funcione.

Una silueta confusa debe corregirse antes de añadir texturas. Favorecer variaciones de una base aprobada frente a rediseños independientes de cada objeto.

MCP puede servir para inspeccionar y realizar cambios concretos. Lua puede servir para operaciones repetidas y exportaciones por lotes. Pillow puede generar imágenes que después se ensamblen en Aseprite. Su eficiencia relativa todavía no se ha medido en este proyecto.

La generación de imágenes puede ayudar a explorar conceptos; comprobar cuadrícula, continuidad y posibilidad de edición antes de utilizar el resultado como recurso definitivo.

## Animación

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

## Referencias consultadas

- [Pixel art y animación, de Pedro Medeiros / Saint11](https://saint11.art/blog/pixel-art-tutorials/).
- [Resoluciones y escalado en Godot](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html). Referencia técnica; no supone que se haya elegido Godot.
- [Paneles de nueve secciones en Godot](https://docs.godotengine.org/en/stable/classes/class_ninepatchrect.html).
- [Exportación por línea de comandos en Aseprite](https://www.aseprite.org/docs/cli/).
