# Investigación: producir los gráficos de Pagar la cuenta con eficacia

Fecha: 23 de octubre de 2026. Solicitado por Ivan R (kapichu), a partir de una captura del juego actual. Estado: investigación y propuesta del asistente; **no es una decisión artística aprobada** por Ivan R ni por Ivan S (Alcachofo).

Relacionado con los puntos **08, 10 y 16–22** del README. Investigar estos puntos no los cierra: el progreso de acuerdos continúa en 0/22.

## Conclusión práctica

Sí: crear el fondo aparte es una buena base. La propuesta es producir **escenario reutilizable + personajes independientes + objetos y elementos que tapan otros elementos + interfaz**, y reunirlos en una escena de composición. Así se puede corregir una mano, sustituir un personaje o cambiar un texto sin generar de nuevo toda la imagen.

La separación principal responde a qué cambia, se anima, se reutiliza o debe tapar otra cosa. No hace falta convertir cada botella o azulejo inmóvil en un recurso independiente. En una escena fija, un fondo dibujado como una pieza puede ser más sencillo que construir un sistema de tiles.

Esta división reduce trabajo de producción; su efecto en los fotogramas por segundo debe medirse. El motor seguirá componiendo los elementos que necesite en cada imagen: separar capas no garantiza por sí solo mayor rendimiento.

## Lectura de la captura actual

Observaciones visuales de la imagen aportada, no una auditoría de los originales ni del código:

- La escena de taberna y los cinco personajes se reconocen con facilidad. Son una base para estudiar la composición, sin fijar el acabado final.
- El fondo presenta bastante textura y detalle; los personajes tienen superficies más planas. Conviene decidir una densidad de detalle compatible y comprobar qué atrae la mirada durante la acción.
- Hay información en la cabecera, encima de cada personaje y en la franja inferior. Para jugar desde un sofá, probar qué puede simplificarse o mostrarse solo cuando haga falta.
- El contorno de los brazos, las manos y los billetes importa especialmente: representa la acción que debe entender el jugador.
- La mesa atraviesa la altura de los personajes y oculta parte de sus cuerpos. Una imagen completa recortada no recupera automáticamente las partes que estaban tapadas.

La captura ya está presentada a una escala de pantalla. Para obtener recursos finales conviene usar los originales a su resolución nativa, si existen; no asumir que recortar o reducir esta captura recupera su cuadrícula y sus capas.

## Separación propuesta de la escena

Orden orientativo del fondo al frente, que habrá que adaptar a la acción:

| Elemento | Qué contendría | Cuándo separarlo |
| --- | --- | --- |
| Fondo limpio | Paredes, suelo, ventana, puerta y decoración fija. | Archivo propio, sin personajes, interfaz ni objetos móviles; dibujar también las zonas que podrían quedar al descubierto. |
| Mobiliario posterior | Sillas y otras piezas situadas detrás de los personajes. | Puede integrarse en el fondo si su posición nunca cambia. |
| Personajes | Una fuente editable por personaje, con poses y expresiones. | Independientes del escenario y entre sí; reutilizables en otros minijuegos cuando encaje. |
| Mesa y elementos que ocultan | Tablero, borde frontal y patas según el orden visual necesario. | Con transparencia y capas suficientes para tapar los cuerpos correctamente. |
| Manos y objetos delante de la mesa | Billetes, tarjetas, vasos y brazos que deben aparecer por delante. | Solo las piezas necesarias para resolver la acción y las superposiciones. |
| Camarero y otros actores | Sus animaciones y recorrido. | Orden delante/detrás definido por la escena; no se deduce de una captura fija. |
| Efectos | Avisos visuales, impacto o énfasis de la acción. | Animaciones breves independientes de los fondos. |
| Interfaz | Nombres, barras, puntuación, instrucciones, QR y botones. | Componentes y texto del juego; no incrustarlos en el dibujo del bar. |

Diseñar estas piezas dentro de una **composición común**: misma perspectiva, escala de píxel, luz, paleta y posiciones de apoyo. «Por separado» describe archivos editables, no una generación de cada pieza sin contexto.

En Aseprite pueden usarse cels enlazados para propagar un cambio estático entre fotogramas del mismo documento. No son enlaces automáticos entre archivos: para actualizar una escena desde varios originales se necesitaría un ensamblador o la composición del motor. [Documentación de cels enlazados](https://www.aseprite.org/docs/linked-cels/).

## Flujo recomendado para la primera prueba artística

1. **Composición antes de detalle.** Boceto con bloques que sitúe mesa, cinco plazas, zonas de movimiento e interfaz. Revisar que las poses no choquen con las barras y que el camarero resulte legible.
2. **Una pequeña referencia común.** Aprobar perspectiva, escala, tratamiento del contorno, luz y ejemplos de materiales. Trabajar a una resolución nativa acordada y revisar al tamaño real. Mantener una regla explícita para cualquier diferencia entre mundo e interfaz; no escoger tamaños a partir de esta captura ampliada. [Criterios de consistencia de Saint11](https://saint11.art/blog/consistency/).
3. **Fondo limpio.** Crear el bar sin personas ni HUD, reservar espacio para la acción y ajustar el contraste para que destaque lo jugable. Aprobarlo en composición con un personaje provisional antes de pulirlo.
4. **Un personaje maestro.** Crear una ficha corta con proporciones, colores, rasgos y pose sentada; comprobar el tamaño de cabeza y manos. No comenzar produciendo cinco personajes ni todas las vistas si esta escena solo necesita una.
5. **Tres acciones de prueba.** Reposo, ofrecer el pago y esquivar, con las variantes necesarias para comprobar ambos lados. Definir las poses principales y el punto de apoyo. Elegir el número de fotogramas después de comprobar la lectura del movimiento.
6. **Composición y corrección.** Verificar manos delante de la mesa, pies y asiento estables, identidad del personaje y ausencia de huecos al moverse. Corregir solo la pieza que falla, con referencia al original aprobado.
7. **Producción del resto.** Cuando esta muestra funcione visual y técnicamente, derivar el resto del elenco y los objetos con las mismas reglas. Mantener una vista previa conjunta para detectar desviaciones.

Estas son propuestas para conseguir algo mejor que la captura, no pasos ya realizados. El acabado podría mantener la taberna cálida y dar más protagonismo a siluetas, expresiones y gestos, con menos ruido detrás de las manos. Esa preferencia deberá validarla el equipo.

## Métodos de creación: qué usar y qué comprobar

| Método | Dónde puede ayudar | Límite o prueba pendiente |
| --- | --- | --- |
| Generación de imágenes con referencias | Explorar una dirección visual, preparar fondos y variantes de diseño. | Una apariencia pixelada no garantiza cuadrícula nativa ni fotogramas consistentes. Conservar referencias y probar cambios localizados en vez de regenerar toda la escena. |
| Aseprite y herramientas MCP | Capas, revisión, lectura de píxeles, cambios concretos y control de animaciones. | El servidor local abre Aseprite en modo batch para ejecutar las operaciones; muchas llamadas pequeñas tienen un coste fijo. |
| Lua por lotes y Pillow | Montaje, recolores controlados, variaciones, exportaciones y comprobaciones repetibles. | Proporcionan control y repetibilidad; no garantizan buen diseño de caras, manos o poses. La API Lua y la CLI permiten automatizar partes de este flujo. [API](https://www.aseprite.org/api/), [CLI](https://www.aseprite.org/docs/cli/). |
| PixelLab, como candidato especializado | Su documentación incluye generación con referencias, personajes y animación guiada por poses. | No se ha probado con Spanish Simulator ni se ha contratado. Evaluar un personaje sentado y un gesto concreto; no dar por hecho que sus modelos encajen con el estilo. [API oficial](https://api.pixellab.ai/v2/llms.txt). |
| Referencias de personaje y, más adelante, modelos entrenados | Mantener una identidad reutilizable entre imágenes. | Empezar comprobando referencias antes de asumir el coste de entrenamiento; Scenario propone ese orden. No se ha entrenado ni probado ningún modelo aquí. [Guía del proveedor](https://help.scenario.com/articles/4280773511-train-a-consistent-character-model). |
| Piezas articuladas o modelos 3D | Reutilizar movimientos si aparecen muchas poses y vistas. | Añaden preparación. Rotar o deformar piezas pixel art puede alterar sus bordes; comprobar el resultado a resolución nativa antes de elegir esta vía. [Nota técnica de los desarrolladores de Spine](https://github.com/EsotericSoftware/spine-editor/issues/554). |

Para esta escena proponemos empezar con **poses de sprite y reutilización limitada de piezas**, por ejemplo expresiones u objetos de la mano. Separar un personaje en muchos huesos desde el principio no está justificado todavía. Si el futuro catálogo exige muchas vistas y acciones, reevaluar articulación o 3D.

No se han comparado muestras artísticas de estos proveedores, ni se ha medido su coste real de producción. Las capacidades documentadas no demuestran que uno sea la mejor elección para el proyecto.

## Medición local: llamadas individuales frente a lote Lua

Se inspeccionó el código del servidor local: `AsepriteCommand.run_command` utiliza `subprocess.run` para abrir Aseprite; `draw_rectangle` carga el archivo y guarda el resultado de cada operación. Agrupar operaciones permite reducir aperturas y guardados. Esto es una observación de esta instalación, no de todos los servidores MCP.

Se ejecutó una prueba en Windows, Python 3.13.17 y Aseprite 1.3.18.6-dev:

- Lienzos nuevos de 64×64, 20 rectángulos de 7×9, sin superposición, en una cuadrícula de 5 columnas y 4 filas.
- Posición del rectángulo `i` (de 0 a 19): `x = 3 + (i % 5) × 12`, `y = 3 + floor(i / 5) × 14`. Colores alternados: `#ba684c`, `#dfc68a`, `#526c72` y `#675176`.
- Ruta individual: 20 llamadas MCP `draw_rectangle`. Ruta por lote: una llamada MCP `run_lua_script` con las mismas 20 operaciones `app.useTool`, una transacción y un guardado final.
- Tres rondas con orden alternado y servidor ya inicializado. Se excluyeron arranque del servidor, creación del lienzo y exportación a PNG.
- Se compararon los píxeles RGBA exportados mediante SHA-256: idénticos en cada pareja. Los seis resultados contienen los 1.260 píxeles opacos esperados, para descartar que fueran imágenes vacías.

| Ronda | 20 llamadas individuales | 1 lote Lua |
| --- | --- | --- |
| 1 | 6,424 s | 0,403 s |
| 2 | 5,476 s | 0,232 s |
| 3 | 5,389 s | 0,263 s |
| Mediana | **5,476 s** | **0,263 s** |

La relación de medianas es aproximadamente **20,8×** para esta prueba sintética. No es una promesa de acelerar el arte por ese factor. No se midieron tokens de un modelo, calidad artística ni tiempo de revisión.

El script, el JSON sin redondear, el registro y los archivos desechables quedan localmente en `mantenimiento/benchmark-lotes.py` y `mantenimiento/benchmark-lotes/`, fuera de Git. Esta tabla publica el método y sus resultados.

## Cómo reducir tiempo y tokens en la producción

- Conservar una referencia visual corta y los originales aprobados; no reconstruir el estilo desde una conversación larga para cada recurso.
- Usar nombres estables para personaje, capa, pose y versión. Pedir un cambio concreto sobre una pieza, con dimensiones y referencia.
- Dejar en scripts las repeticiones y reglas deterministas. Enviar datos o parámetros en vez de describir cada rectángulo o píxel en llamadas independientes.
- Usar herramientas de alto nivel como filas de píxeles, rellenos o recolores cuando resuelvan la tarea; reservar el lote Lua para secuencias repetidas o montaje que lo justifiquen.
- Revisar por etapas útiles, no tras cada píxel. Conservar hitos intermedios para detectar dónde empezó a desviarse el resultado.
- Medir coste por **recurso aceptado**, incluyendo intentos descartados y retoque, no solo coste por imagen generada o llamada más rápida.

La recomendación de reducir intercambio repetitivo es razonable por el diseño del flujo, pero el ahorro de tokens aún no se ha cuantificado.

## Qué debería decidirse después de la muestra

Registrar en los puntos existentes, sin inventar acuerdos:

- **08 y 16:** dirección visual, escala y material de referencia mínimo.
- **10 y 17:** poses, animaciones y ficha del personaje de prueba.
- **18 y 19:** división de recursos y etapas de revisión que funcionen.
- **20 y 21:** métodos elegidos y coste real hasta aceptar la muestra.
- **22:** originales, exportaciones, puntos de apoyo, orden de composición y procedimiento para comprobarlos.

La próxima prueba propuesta es **un fondo limpio, una mesa independiente y un personaje con reposo, ofrecer y esquivar**, montados con una interfaz provisional. Esa muestra permitirá comparar calidad y coste antes de encargar toda la escena o elegir una herramienta de pago.
