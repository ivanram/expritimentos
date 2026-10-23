# Plan de producción: escena de taberna con personajes independientes

Fecha: 23 de octubre de 2026. Preparado a petición de Ivan R (kapichu). Equipo: Ivan R e Ivan S (Alcachofo).

Este documento conserva el **plan de producción**. A petición posterior de Ivan R, se ha construido una [primera muestra funcional](../prototipos/taberna/README.md) con originales y exportaciones mediante MCP. El resultado no convierte las hipótesis de estilo en decisiones artísticas aprobadas. El plan parte de las capacidades del MCP local y la [investigación previa](investigacion-graficos.md).

## 1. Alcance solicitado y decisiones provisionales

**Revisión posterior:** tras probar la primera muestra, Ivan R pidió explorar una mesa redonda, personajes más variados y orgánicos y comenzar por un boceto. El [concepto coloreado](../arte/conceptos/mesa-redonda-v01/README.md) recoge la nueva exploración. Las propuestas de composición frontal de este plan se conservan como contexto de la primera demo; deberán revisarse antes de producir la siguiente.

### Requisitos expresados por Ivan R

- Preparar una escena similar en función a la captura de Pagar la cuenta, buscando un resultado visual mejor y sin obligación de imitar su estética.
- Usar aseprite-mcp en el proceso de creación y revisión.
- Animar a cada personaje de forma independiente; permitir acciones ambientales como charlar.
- Cada personaje debe poder levantar la mano para pagar sujetando una cartera, una tarjeta o billetes.
- Incluir al camarero más adelante; no producirlo en esta entrega.
- Comer se considera una posibilidad, no un requisito cerrado de la primera muestra.

La propuesta inicial conserva cinco plazas como en la captura. La resolución, el elenco, la dirección artística y la cantidad de fotogramas siguientes son parámetros de prueba del asistente, no decisiones globales aprobadas.

## 2. Dirección visual propuesta

**Taberna contemporánea con carácter de cómic costumbrista:** formas claras, rostros expresivos, manos que se entiendan y luz cálida. Buscar personalidad mediante siluetas, posturas y gestos, en lugar de acumular textura.

- Fondo con ocres, tejas y azules oscuros, reduciendo el contraste justo detrás de caras y manos. Unos pocos elementos reconocibles del bar, con espacio visual para la acción.
- Personajes con proporciones ligeramente caricaturizadas: cabeza suficientemente grande para leer cejas y boca, manos suficientes para distinguir el agarre y siluetas diferentes entre sí.
- Colores de identidad acompañados de diferencias de pelo, cara, vestuario y postura. Evitar cinco cuerpos idénticos que solo cambien de color.
- Luz y sombras compartidas, con dos o tres tonos por material como punto de partida. Contorno oscuro selectivo y formas de color limpias; sin copiar personajes ni escenarios SCUMM.
- Una mesa en una perspectiva poco profunda para favorecer la lectura de los cinco participantes. Reservar espacio vertical al brazo levantado y un recorrido libre para el futuro camarero.
- La interfaz ocupa zonas reservadas y se mantiene fuera de las imágenes del escenario. El gesto de pagar no debe chocar con nombres, barras o cabecera.

**Dimensiones de prueba:** pantalla lógica de 640×360 y celdas de personaje alrededor de 96×160, ampliables si el gesto completo lo exige. Antes de detallar, comprobar cinco siluetas, su separación y el alcance del brazo. Si las manos o caras no se leen, ajustar proporciones o escala en ese boceto; no ampliar piezas sueltas con una escala de píxel distinta.

Estas dimensiones son una hipótesis de trabajo para esta muestra, no la resolución final del juego. Se ajustan después de probar la composición y no se deducen de los píxeles de la captura ampliada.

## 3. Estructura de recursos y orden de dibujo

| Recurso propuesto | Contenido y función |
| --- | --- |
| `taberna_fondo.aseprite` | Bar limpio, decoración inmóvil y partes ocultas que podrían quedar visibles al animar. |
| `taberna_mesa.aseprite` | Mesa con transparencia; separar tablero, borde o patas solo si el orden de dibujo lo necesita. |
| `personaje_01.aseprite` … `personaje_05.aseprite` | Originales independientes, con capas editables y etiquetas de acción. IDs temporales, sin fijar nombres ni diseños del elenco. |
| `objetos_pago.aseprite` | Cartera, tarjeta y billetes, con variantes de orientación necesarias para el agarre. Sin marcas comerciales obligatorias. |
| `objetos_mesa.aseprite` | Vasos y tapas reutilizables; la comida manipulada se separaría cuando se pruebe esa acción. |
| `escena_taberna.json` | Propuesta de descripción de plazas, apoyos, recursos, orden de dibujo y versiones. Se implementará al producir la muestra. |
| Vista de composición | Montaje de comprobación y previsualización. No sustituye los originales ni se convierte en la animación final única del juego. |

Orden de dibujo inicial: **fondo y sillas → partes de personajes detrás de la mesa → mesa y objetos fijos → brazos y manos delanteros → objetos sostenidos → dedos que pasan por delante del objeto → interfaz**. Ajustar los casos en que un vaso deba tapar otra pieza y documentar las excepciones.

Para cada personaje exportar dos pasadas sincronizadas si hacen falta: una detrás de la mesa y otra delante. Ambas usan el mismo fotograma de su acción. Los objetos de la mano se insertan entre las capas del agarre. Evitar recurrir a una máscara que corte todo a una altura fija si se necesitan piernas visibles bajo el tablero.

No construir un esqueleto completo de muchas piezas desde el principio. Mantener una pose de cuerpo coherente y separar únicamente lo que aporta reutilización o resuelve la superposición. Las poses clave se dibujan; los desplazamientos de piezas rígidas se reservan para movimientos secundarios adecuados.

## 4. Animación independiente de verdad

Cada personaje tendrá su propia acción, tiempo transcurrido, variante de objeto y secuencia ambiental. Un jugador puede pagar mientras otro charla y otro permanece en reposo.

Una línea de tiempo de Aseprite organiza los clips de un personaje. La independencia de los cinco actores la dará el reproductor de la escena al usar cada archivo o exportación por separado, **no** las capas de una sola animación con un reloj global.

### Acciones propuestas

| Acción / etiqueta | Comportamiento | Prioridad para la muestra |
| --- | --- | --- |
| `idle` | Respiración discreta, parpadeo y pequeñas variaciones de mirada. Evitar que los cinco se balanceen a la vez. | Obligatoria. |
| `talk` | Boca, expresión y una pequeña reacción de cabeza o torso que se lea como charla. No presupone voces ni sincronización labial con audio. | Obligatoria. |
| `pay_raise` | Preparación breve, movimiento del brazo y presentación del objeto por encima de la mesa. | Obligatoria para cada personaje. |
| `pay_hold` | Sostener la oferta el tiempo necesario, sin volver automáticamente a reposo. | Obligatoria. |
| `pay_lower` | Bajar el brazo y regresar de forma coherente a una pose de reposo. | Obligatoria. |
| `eat` | Coger una tapa, llevarla a la boca y volver a la mesa; necesita objeto y punto de recogida. | Opcional, después de validar charla y pago. |
| `dodge` | Acción de esquivar del concepto anterior. | Fuera de esta primera muestra, salvo ampliación expresa. |

Como presupuesto inicial, probar 3–4 poses para reposo, 4–6 para charla, 5–6 para elevar y 3–5 para bajar; la oferta sostenida puede usar una pose o una variación mínima. Son estimaciones para ensayar el ritmo, no recuentos aprobados ni una obligación de dibujar fotogramas nuevos cuando se puedan reutilizar.

### Interrupciones y convivencia

- El pago tiene prioridad sobre charla y comida. Al recibir la acción, abandonar el gesto ambiental con una transición breve y coherente; no esperar a terminar una animación larga.
- Si se interrumpe una comida, definir dónde queda el alimento y liberar la mano antes de mostrar el objeto de pago. Para la primera versión se puede devolver a la pose base antes de elevar el brazo; comprobar que no aparezca un salto visual.
- Mientras se paga, no ejecutar a la vez una charla gesticulada que también use ese brazo. No producir todas las combinaciones de acciones, expresiones y objetos como animaciones distintas.
- Una cancelación durante la subida debe permitir regresar desde la pose alcanzada; no saltar a la mano totalmente elevada para iniciar la bajada.
- Las variaciones ambientales arrancan con tiempos distintos por actor. Se detienen o cambian por estado, sin afectar al reloj de los otros personajes.
- Los tiempos de los clips son datos. La regla que decide cuándo cuenta una oferta de pago pertenece al juego; una marca de «objeto presentado» puede ayudar a sincronizar lo visual, sin fijar aquí esa regla.

## 5. Cartera, tarjeta y billetes sin multiplicar el trabajo

Crear **un movimiento de brazo por personaje** como base, y tres variantes de objeto/agarre. No crear tres animaciones completas de cuerpo si solo cambia lo sostenido.

- Definir un apoyo de asiento que permanezca estable y un punto de mano por fotograma de la acción. Los puntos de mano cambian con el movimiento; no basta con una coordenada fija para toda la animación.
- Registrar por pose la posición local del objeto, su orientación discreta y las partes del agarre que lo tapan. Preferir variantes dibujadas de orientación a rotaciones arbitrarias que rompan los bordes de píxel.
- La tarjeta debe leerse como tarjeta, los billetes como un pequeño fajo o abanico y la cartera como un objeto con volumen. El tamaño de cada uno se decide en la prueba de legibilidad.
- Preparar agarres específicos: pellizco para tarjeta, apoyo adecuado para cartera y dedos para sujetar billetes. Compartir el arco del brazo no exige que todas las manos tengan la misma forma.
- Elegir el tipo de objeto antes de iniciar la subida y conservarlo hasta volver al reposo. Su aparición debe quedar justificada por la mano o una zona oculta bajo la mesa; no hacerlo aparecer de golpe sobre una mano ya elevada.
- Dibujar primero brazo/palma, después el objeto y finalmente los dedos delanteros necesarios. Comprobar muñeca, orientación y que nada parezca flotar.
- Mantener un lienzo local y un apoyo constantes entre acciones. Si se recortan las exportaciones, conservar los desplazamientos originales en los metadatos.

Las slices del MCP permiten anotar regiones y pivotes generales. El MCP local revisado no expone una operación específica para actualizar un anclaje móvil de mano por fotograma: se planifica un mapa de coordenadas en los datos de la acción o una operación Lua explícita para generarlo. No asumir que el JSON de una hoja de sprites incluirá esos datos sin prepararlos.

## 6. Uso concreto del MCP de Aseprite

Capacidades comprobadas por lectura del código local. No se han ejecutado todavía para producir esta escena.

| Etapa | Herramientas MCP previstas | Resultado que revisar |
| --- | --- | --- |
| Preparación | `animation_workflow_guide`, `create_canvas`, `add_group`, `add_layer`, herramientas de paleta. | Guía de animación consultada para el caso, dimensiones, grupos, colores y capas con nombres estables. |
| Siluetas y detalle | `draw_rows`, `draw_pixels_at`, herramientas `*_at` y `import_image_as_layer` si existe un original preparado. | Diseño sobre una cuadrícula real, dirigido a capa y fotograma concretos. |
| Poses y clips | `copy_frame`, `erase_region`, `add_frames`, `set_tag`, herramientas de duración y `propagate_cels`. | Eliminar el miembro anterior antes de redibujarlo, conservar identidad y organizar las acciones. |
| Revisión | `view_sprite`, `render_onion_skin`, `compare_frames`, `get_bounds`, `get_color_stats`, `lint_sprite`, `audit_animation`. | Silueta, estabilidad, continuidad y posibles defectos. Los avisos de lint requieren interpretación visual. |
| Montaje y lotes | `run_lua_script`, y `copy_layers_between_sprites` cuando encaje. | Ensamblar o repetir secuencias deterministas con menos aperturas/guardados. |
| Entrega | `export_spritesheet` con datos y etiquetas, `export_tag` / `export_animation`, `list_slices` cuando proceda. | PNG con transparencia, tiempos, etiquetas y metadatos adicionales verificados. |

Puntos de atención en esta instalación:

- La prueba previa de 20 operaciones favorece agrupar el trabajo repetitivo, pero no justifica escribir toda la ilustración como miles de rectángulos. Reservar las llamadas detalladas para decisiones y correcciones que lo necesiten.
- `copy_layers_between_sprites` copia cels y posiciones por índice de fotograma. No establece animaciones independientes, no sincroniza automáticamente sus tiempos y no crea una referencia viva a los originales.
- `export_spritesheet` puede incluir etiquetas con `list_tags=True`, pero no expone la exportación de slices en esa función. Preparar los pivotes con `list_slices` u otra exportación explícita y añadir el mapa de mano por fotograma.
- La validación automática es complementaria. `validate_scene` revisa presencia de capas/cels y su búsqueda actual es de capas de primer nivel; no usarla como prueba de que todos los grupos anidados o la calidad del dibujo sean correctos.
- Aseprite Live sirve para revisar archivos y sus cambios. La independencia temporal y las interrupciones se demostrarán en un compositor de prueba que lea los recursos exportados, sin elegir con ello el motor definitivo del juego.

## 7. Producción por entregas pequeñas

1. **Boceto de dirección y composición.** Una propuesta visual principal en bloques, con cinco siluetas y la pose de pago más alta. Comparar neutral y oferta; ajustar el espacio antes de dibujar detalle.
2. **Personaje piloto.** Pose sentada y ficha breve con paleta, rasgos y apoyos. Producir reposo, charla y pago con tarjeta. Verificar cada clip aislado y sobre la mesa provisional.
3. **Pago completo del piloto.** Añadir cartera y billetes con sus agarres, oferta sostenida, bajada y cancelación durante subida. Revisar que no se conviertan en variantes incoherentes del cuerpo.
4. **Fondo y mesa acabados.** Desarrollar el bar con el piloto visible; terminar el orden de dibujo y probar las tres variantes de pago sobre el escenario.
5. **Elenco.** Crear cuatro personajes adicionales a partir de las reglas validadas, con siluetas e identidades propias. Reutilizar estructura y herramientas, revisando los anclajes para sus proporciones.
6. **Composición independiente.** Mostrar a unos charlando, a otro en reposo y a otro pagando; cambiar de objeto por actor y lanzar pagos simultáneos. Repetir con las cinco plazas y revisar bordes de pantalla.
7. **Entrega y evaluación.** Originales, exportaciones, metadatos, vista previa conjunta y medición del tiempo hasta un resultado aceptable. Añadir comer solo después si aporta valor y encaja en el presupuesto.

El **primer entregable revisable** sería el boceto con cinco plazas y un personaje piloto que pasa de reposo a ofrecer una tarjeta, la sostiene y baja la mano. Después se amplían los objetos y la charla antes de reproducir el trabajo en todo el elenco.

## 8. Criterios para aceptar la muestra

- Se puede cambiar o animar un personaje sin regenerar el fondo ni la animación de los otros.
- Los cinco actores pueden estar en acciones y fotogramas diferentes; parar uno no detiene al resto.
- Cada uno levanta y baja la mano con los tres tipos de objeto. El agarre se mantiene durante toda la acción, sin flotar ni cortar el objeto.
- El pago se reconoce al tamaño de juego; mesa, dedos y objetos se superponen correctamente. La pose más alta cabe sin invadir el HUD ni al vecino.
- Pagar puede interrumpir la animación ambiental y la oferta se sostiene hasta que el estado cambie. La cancelación no teletransporta el brazo.
- Asiento y proporciones estables, sin saltos de origen entre clips. No hay sincronía ambiental mecánica de los cinco actores.
- La ficha y la paleta bastan para que un cambio localizado no obligue a reinventar el personaje.
- Se revisa una hoja de poses y una animación de cada actor, y también el conjunto. La revisión artística de kapichu y Alcachofo sigue pendiente; no se sustituye por la ausencia de errores técnicos.
- La entrega no contiene camarero. Quedan documentados espacio y orden de dibujo para incorporarlo más adelante, sin producir aún sus recursos.

## 9. Relación con las decisiones del proyecto

Requisitos parciales confirmados por Ivan R para este plan:

- **02.1:** muestra inicial sin camarero; se incorporará después.
- **10.1:** cada personaje ofrece el pago levantando la mano con cartera, tarjeta o billetes.
- **10.2:** prever charla ambiental; comer queda como posibilidad.
- **18.1:** personajes con animaciones independientes entre sí.
- **20.1:** usar aseprite-mcp para la producción y revisión de esta escena.

Quedan propuestas pendientes en **08** (acabado y dimensiones), **09** (elenco), **10** (poses y tiempos), **16–19** (guía y recursos), **20–21** (método y coste aceptado) y **22** (exportación y reproducción). Estos subpuntos no cierran las decisiones principales: el contador global continúa en **0/22**.

## Referencias técnicas

- [Etiquetas de animación en Aseprite](https://www.aseprite.org/docs/tags/): organización de clips.
- [Slices y pivotes en Aseprite](https://www.aseprite.org/docs/slices/): regiones, apoyos y exportación.
- [Investigación previa y medición local](investigacion-graficos.md): separación de recursos, alternativas y operaciones por lotes.
