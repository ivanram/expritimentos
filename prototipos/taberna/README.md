# La última ronda: prueba de arte y animación

**[Abrir la demo pública](https://spanish-simulator-ultima-ronda.ivanra.chatgpt.site)** · Sin instalación. Pulsa «Escena de prueba» para ver los tres objetos de pago a la vez.

Muestra funcional de Spanish Simulator creada el 23 de octubre de 2026 para kapichu y Alcachofo. Cinco personajes originales, escenario y mesa separados, charla, comida sencilla y pago con tres objetos. El camarero no está incluido.

## Probar

Abrir `index.html` en un navegador o ejecutar `ABRIR.bat`. No necesita instalar paquetes ni un servidor: todos los recursos son locales. También puede servirse como una web estática.

- Seleccionar un personaje haciendo clic en él, en su tarjeta o con las teclas 1–5.
- Elegir reposo, charla o picar algo.
- Elegir tarjeta, cartera o billetes antes de levantar la mano.
- «Yo invito» levanta y sostiene el objeto; «Bajar la mano» devuelve al personaje al reposo. Con el foco fuera de botones, también se puede mantener Espacio y soltarlo para bajar.
- Pausar solo al actor seleccionado y comprobar que los demás siguen moviéndose.
- «Escena de prueba» pone a tres actores a pagar con objetos diferentes y a los otros en acciones ambientales.
- En «Mirar entre bastidores» se puede ocultar fondo/mesa, mostrar anclajes, cambiar la velocidad y consultar el fotograma de cada actor.

La casilla de ambiente permite acciones autónomas con tiempos distintos. Una acción manual toma el control de ese actor; reactivar el ambiente devuelve los actores al comportamiento autónomo.

Esta es una prueba de recursos y reproducción. No implementa la puntuación del minijuego, salas, móviles, multijugador ni audio.

## Qué se ha hecho realmente con MCP

El dibujo original se ha programado con Python/Pillow: no se han utilizado una imagen de SCUMM, la captura del juego ni un modelo de generación de imágenes como recursos del prototipo.

Después se han ejecutado llamadas reales al servidor `aseprite-mcp` por stdio para crear/importar originales estáticos, montar las capas y fotogramas, etiquetar las acciones, inspeccionar y auditar los cinco personajes y exportar sus hojas. Un detalle del objeto de pago se ha dibujado con `draw_rows`. El montaje de animaciones y la exportación por capas se han agrupado en Lua mediante el MCP.

`produccion-mcp.json` registra las herramientas utilizadas y su duración en la generación más reciente. Cada generación realiza 32 llamadas. El tiempo registrado excluye escribir el generador, preparar las imágenes y revisar/implementar el visor; no mide coste de tokens ni calidad artística.

## Archivos

- `art/`: nueve originales `.aseprite`: fondo, mesa, objetos de mesa, objetos de pago y cinco personajes. Cada personaje tiene 27 fotogramas y capas para cuerpo, brazo y tres agarres.
- `assets/`: PNG exportados, datos de hojas y manifiesto con posiciones de los actores y anclajes de mano por fotograma.
- `generar.py`: dibujo y producción mediante MCP, reproducibles con las herramientas del laboratorio.
- `animacion.js`: estados y relojes independientes de los actores.
- `visor.js`, `index.html`, `estilo.css`: compositor y controles del ensayo.
- `prueba-animacion.cjs`: comprobaciones de independencia, cancelación, oferta sostenida y variantes de objeto.
- `preview.png`: composición estática de los recursos, ampliada a 2× con nearest.
- `captura-visor.png`: captura del compositor funcionando en el navegador.
- `validar-recursos.py` y `validacion-recursos.json`: verificación de originales, fotogramas, etiquetas, atlas y anclajes.

Los agarres y objetos se componen después del brazo y antes de los dedos delanteros. El tipo de objeto se bloquea durante el pago. La bajada usa los mismos fotogramas en orden inverso y puede comenzar desde cualquier pose alcanzada.

## Regenerar

Requiere Python con `pillow` y `mcp`, Aseprite y el servidor aseprite-mcp. `generar.py` toma la configuración MCP local de `.mcp.json` en la raíz del repositorio, que no se publica porque contiene rutas de la máquina. En otro ordenador hay que preparar ese archivo con el intérprete, PYTHONPATH y ASEPRITE_PATH correspondientes.

Desde la raíz del laboratorio en Windows:

```powershell
& '.\aseprite-mcp\.venv\Scripts\python.exe' '.\prototipos\taberna\generar.py'
node --test '.\prototipos\taberna\prueba-animacion.cjs'
```

La carpeta `.work/` guarda las imágenes intermedias y está ignorada. Las capas y tiempos exportados proceden de los originales montados en Aseprite. El visor conoce las etiquetas y tiempos de esta muestra; una integración en el motor definitivo deberá conservar esos datos y las reglas de estado.

## Publicación

Publicado el 23 de octubre de 2026 en Sites con acceso público, a petición de Ivan R, para que Alcachofo pueda probarlo. El enlace también está al principio del README principal.

`node prototipos/taberna/preparar-web.mjs` prepara `dist/` con los archivos del visor y los recursos exportados. No requiere dependencias. `.openai/hosting.json` conserva la identidad del sitio y su directorio estático para actualizar el mismo despliegue. `dist/` está ignorado en este repositorio.

Para actualizarlo con Sites, reutilizar ese `project_id`, obtener acceso a su repositorio de publicación y seguir el flujo de sincronización, empaquetado y despliegue del plugin. La copia de publicación actual se encuentra localmente en `mantenimiento/site-ultima-ronda/`, ignorada en GitHub. No cambiar el remoto de este repositorio de GitHub. El sitio sirve HTML, JavaScript y PNG estáticos; no contiene claves ni necesita servicios del laboratorio para reproducir las animaciones.

## Comprobaciones

- Cinco pruebas automatizadas de estados: relojes independientes, pausa local, quince combinaciones de actor/objeto, oferta sostenida, cancelación desde distintas poses y vuelta a una acción ambiental.
- Validación de nueve originales Aseprite y 25 hojas de sprites, con 27 fotogramas por personaje y sin recortes que cambien su origen.
- En el navegador: selección de Nora, bajada de tarjeta, cambio a cartera, nueva oferta y pausa de ese actor mientras los demás continúan. También se ha comprobado la escena con los tres objetos a la vez y la visualización de anclajes.
- La escena se ha inspeccionado visualmente; esta comprobación no es una aprobación artística atribuida al equipo.

## Evaluación pendiente

El resultado demuestra la separación de recursos y la independencia de reproducción. Su calidad visual debe valorarla el equipo: las cinco identidades, la paleta, el acabado y los nombres son propuestas de esta prueba, no decisiones finales del juego.

La comida es una secuencia breve con un bocado; no hay recogida/eliminación de comida de un inventario de mesa. No se ha implementado sincronización labial con voces ni un sistema general de esqueleto o interpolación.
