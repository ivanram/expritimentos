# Investigación de claude-pxl

24 de octubre de 2026. Ivan R aporta [este hilo de Reddit](https://www.reddit.com/r/aigamedev/comments/1xb3k2l/opus_55_pixel_art_with_claude_pxl/). Se ha revisado y probado el [fork augusto-scarvalho/claude-pxl](https://github.com/augusto-scarvalho/claude-pxl), revisión `e054b073b634026b9b0446ec7779cefeec9aef21`. La [primera prueba propia, con GIF, visor y originales](../arte/pruebas/pxl-pago-v01/README.md), produce un personaje sentado que ofrece pagar y conserva sus capas al exportar a Aseprite. La calidad artística sigue pendiente de valoración.

Ivan R aclara que ya dispone de Claude. Se mantiene su restricción de no contratar más IAs. Tenerlo disponible no obliga a cambiar de asistente: interesa comprobar el método con las herramientas y el asistente actuales. No se presupone igualdad de calidad entre modelos ni superioridad artística del asistente por disponer de las mismas herramientas.

## Qué aporta

Es un lenguaje de dibujo en archivos `.px.js` y un motor local, acompañado de instrucciones para agentes. La IA escribe y modifica el dibujo; el motor produce los recursos. No es otro modelo generativo ni exige Claude como servicio. La [documentación para agentes](https://github.com/augusto-scarvalho/claude-pxl/blob/main/docs/agents.md) contempla Codex y otros asistentes.

El [README](https://github.com/augusto-scarvalho/claude-pxl#readme) documenta cuadrículas de sprites, primitivas, paletas, capas, animaciones y exportación PNG, hojas con JSON, GIF y Aseprite. Permite dibujar directamente a resolución nativa. También admite imágenes importadas y efectos: utilizar pxl no convierte automáticamente cualquier salida en pixel art bien resuelto.

Su [licencia es MIT](https://github.com/augusto-scarvalho/claude-pxl/blob/main/LICENSE). El [paquete](https://github.com/augusto-scarvalho/claude-pxl/blob/main/package.json) requiere Node 22.18 o posterior y no declara dependencias de ejecución ni un proveedor de IA. El dibujo mediante el asistente sigue consumiendo su uso habitual; no implica consumo ilimitado o ausencia de límites del plan existente.

## Lo que se ha contrastado en código

- [`image.ts`](https://github.com/augusto-scarvalho/claude-pxl/blob/main/src/core/image.ts): imagen RGBA sobre una cuadrícula y escritura en coordenadas enteras. No necesita partir de una ilustración grande reducida.
- [`perspective.ts`](https://github.com/augusto-scarvalho/claude-pxl/blob/main/src/core/perspective.ts): proyección de cámara con horizonte, altura y orientación. Hay implementación geométrica, además de una recomendación escrita sobre perspectiva.
- [`rig.ts`](https://github.com/augusto-scarvalho/claude-pxl/blob/main/src/core/rig.ts): piezas con pivotes, puntos de unión y orden según orientación. Encaja con una mano que lleva tarjeta, cartera o billetes; no demuestra todavía nuestro gesto de pago.
- [`aseprite.ts`](https://github.com/augusto-scarvalho/claude-pxl/blob/main/src/node/aseprite.ts): exporta capas y fotogramas. Algunas transformaciones o cambios incompatibles de capas provocan aplanado; habría que verificar el editable exportado en cada prueba.

La revisión del código no equivale a una auditoría completa. La prueba posterior ejecuta dibujo 2D, animación, puntos de unión, inspección y exportación; no prueba perspectiva geométrica ni rigs 3D.

## Aplicación propuesta a Spanish Simulator

Priorizar ensayos pequeños con pxl como autor del dibujo y Aseprite como editor y destino de exportación, antes de rehacer la taberna completa. Ya existe una primera prueba de personaje y contexto; su valoración no cierra decisiones 01–22.

1. Fijar la cámara compartida de una mesa y un plato; validar volumen, apoyo y lectura antes del acabado. No copiar la estética de los ejemplos del repositorio.
2. Dibujar un plato original a resolución nativa y una segunda tapa con la misma perspectiva y lenguaje. Revisar las exportaciones a 1× y ampliación entera.
3. Probar un personaje sentado con reposo y subida/bajada de la mano. Resolver primero las poses y oclusiones, después color y detalle. La tarjeta se une a la mano; el contorno debe funcionar sobre la silueta compuesta, sin anillos alrededor de cada articulación.
4. Exportar originales y hojas, abrirlos en Aseprite y medir tiempo, revisiones, llamadas y trabajo humano. Comprobar el resultado visual, además de los validadores.

El [flujo documentado](https://github.com/augusto-scarvalho/claude-pxl/blob/main/docs/agents.md#blocks-first-then-paint) insiste en probar estructura y movimiento antes de pintar. Sus comandos de inspección permiten consultar solo el recurso o sección necesarios y modificar fragmentos del dibujo, en lugar de regenerar todo en cada ajuste. Es una hipótesis útil para reducir iteraciones, no una eficiencia medida en nuestro proyecto.

El autor publica una [comparación de modelos](https://github.com/augusto-scarvalho/claude-pxl/blob/main/docs/model-study.md): una escena y una ejecución por configuración, con valoraciones humanas y automáticas que discrepan. Sirve para recordar que disponer del motor no garantiza el resultado ni que un validador sustituya la revisión de la animación. No trasladar sus precios estimados por API a facturas reales de nuestro plan ni extrapolar su clasificación a todos los recursos.
