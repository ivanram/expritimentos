# Automatizar pixel art real con IA

23 de octubre de 2026. Ivan R ha aclarado que el objetivo es producir pixel art real de forma eficaz con IA. Redibujar todos los recursos a mano como solución principal pierde la ventaja buscada. Las pruebas existentes no han demostrado todavía ese objetivo.

## Estado de los experimentos

**Restricción añadida el 24 de octubre de 2026 por Ivan R:** no quiere contratar más IAs. El flujo propuesto debe evitar nuevas suscripciones y consumo de APIs de pago, aprovechando las herramientas disponibles. La prueba gratuita de un servicio no equivale a producción gratuita sostenida. Esta restricción no se atribuye a Ivan S ni cierra todos los aspectos de presupuesto del proyecto.

Los ensayos recientes demuestran generación de conceptos, preparación de imágenes, composición por capas y exportaciones reproducibles con Aseprite MCP. Las tapas proceden de ilustraciones generadas y reducidas; no validan producción de pixel art nativo. Tamaño pequeño, nearest y número de colores no certifican diseño de píxeles ni calidad visual.

El proceso buscado permite que la IA produzca el recurso y sus revisiones, mientras las personas eligen dirección y evalúan. Si un recurso solo funciona después de repintarlo entero, ese ensayo no valida la automatización. Hay que medir intervención y correcciones, además del resultado.

## Vías para comparar

| Vía | Aporta | Falta demostrar |
| --- | --- | --- |
| Generador especializado en pixel art | Salida nativa, referencias y variantes por API/MCP. | Calidad, consistencia, cámara, animación y tiempo hasta aceptación. |
| IA dibujando a resolución nativa por Aseprite MCP/Lua | Producción y corrección mediante herramientas/código; no necesita que el usuario dibuje. | Calidad artística y coste de llamadas/tokens/revisiones. La primera demo mostró límites de diseño. |
| Conversión mediante un modelo especializado | Reinterpretar conceptos conservando composición, más allá del reescalado. | Formas y contornos resueltos a baja resolución, conservando volumen y sin redibujo completo. |

## Candidatos investigados, sin probar

**PixelLab:** la documentación v2 ofrece tamaño de salida, referencias, conversión de imágenes, personajes persistentes y animación desde una imagen. Tiene MCP y extensión de Aseprite. Consultar los límites del modelo elegido. Son capacidades declaradas por el proveedor, no resultados medidos aquí. [API v2](https://api.pixellab.ai/v2/docs), [MCP](https://www.pixellab.ai/mcp), [formas de uso](https://www.pixellab.ai/docs/ways-to-use-pixellab).

**Retro Diffusion:** su API admite dimensiones, referencias según modelo, alfa y animación; `upscale_output_factor=1` solicita salida nativa. Publica MCP y consultas de coste previas a generación. También ofrece reconstrucción de cuadrícula, que por sí sola no valida dirección artística. [API y ejemplos oficiales](https://github.com/Retro-Diffusion/api-examples), [MCP oficial](https://github.com/Retro-Diffusion/retro-diffusion-mcp).

Ninguno está conectado en esta sesión y no se han ejecutado generaciones con esos proveedores. Consultar documentación no implica contratar ni gastar saldo. Aseprite MCP local sí está disponible. La prueba debe distinguir funciones publicadas del resultado observado.

## Ensayo mínimo propuesto

1. Un plato a 64×32, o el tamaño nativo que se acuerde, con transparencia, perspectiva y rasgos reconocibles. La IA hace producción y correcciones.
2. Otro plato con el mismo lenguaje para comprobar repetibilidad.
3. Un personaje con reposo y una secuencia breve de levantar/bajar la mano, conservando identidad y apoyos.

Comparar a 1× y ampliación entera, comprobar integración y edición. Registrar herramienta/modelo, resolución realmente generada, referencias, intentos, tiempo, llamadas/tokens/coste cuando estén disponibles y minutos de intervención humana. No imponer 32 colores ni paredes planas como atajo.

La recomendación previa de probar un generador especializado se revisa a raíz de la restricción de coste: la siguiente vía a ensayar es dibujo nativo automatizado mediante el Aseprite MCP disponible, empezando por un recurso pequeño. Eso implica que la IA produzca y revise el dibujo, no que Ivan R lo redibuje entero. Su calidad y eficacia aún deben demostrarse.

PixelLab ofrece una prueba de generaciones y herramientas limitadas; su integración MCP exige suscripción activa según la [documentación de formas de uso](https://www.pixellab.ai/docs/ways-to-use-pixellab), y el [acceso API publica precios por operación](https://www.pixellab.ai/pixellab-api). Sus capacidades documentadas se conservan como investigación, fuera del flujo de producción propuesto sin pagos adicionales. No se ha contratado, conectado ni consumido ese servicio. No se elige proveedor, motor o estilo ni se cierran los puntos 01–22.
