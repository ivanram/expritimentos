# Nuevas vías para personajes consistentes

24 de octubre de 2026. Ivan R ha señalado que la [lámina de ocho orientaciones](../arte/pruebas/comfy-pepo-v02/README.md) **no le sirve como recurso de juego**: la mano y otros detalles cambian de sitio. Esta revisión corrige nuestra valoración anterior, demasiado optimista. El problema no es que Ivan R no sepa pedirlo: se eligió un método que genera cada postura como una imagen nueva sin una estructura común que obligue a respetar lado, articulaciones y prendas.

## Resultado verificable hasta ahora

- El primer Pepo de ComfyUI gusta a Ivan R como **apariencia inicial**. No está acordado su vestuario frente a la ficha anterior de camiseta y vaqueros.
- ComfyUI con imagen a imagen, instrucciones y dos pesos de IP-Adapter no obtuvo un perfil correcto que conservara a la vez ropa e identidad. [Cinco salidas originales y tiempos](../arte/pruebas/comfy-pepo-v02/README.md).
- Una sola generación de una hoja con ocho vistas produjo giros legibles, pero **no fijó las invariantes** entre celdas. No la usaremos como fuente maestra ni diremos que está aprobada.
- Un flujo nuevo con ControlNet Canny e IP-Adapter se [ensayó por separado](../arte/pruebas/comfy-pepo-v03/README.md). Logró un perfil derecho, pero cambió la sobrecamisa a morado, ocultó la camiseta roja y sustituyó las zapatillas claras. Tardó 534,87 s en esta máquina. El control del contorno no fijó identidad, ropa ni mano.

## Qué debe quedar fijo en el diseño

Un personaje reutilizable necesita un **original canónico** con datos que una instrucción textual no puede imponer por sí sola:

1. Lado anatómico izquierdo/derecho de cada mano, bolsillo y accesorio; especificado desde el personaje y comprobado en cada vista, también al espejar.
2. Proporciones y puntos de articulación de cabeza, cuello, hombros, codos, muñecas, caderas, rodillas y pies; línea de suelo común.
3. Topología y capas de la ropa: cuál prenda va encima, dónde están mangas, cuello, costuras y bolsillos. La espalda debe diseñarse una vez, no inventarse de nuevo en cada imagen.
4. Una paleta y formas de pelo/barba reconocibles, con contorno exterior del personaje y uniones de brazos que no parezcan piezas rodeadas de bordes.
5. Poses de mano vacía, cartera, tarjeta y billetes, con el objeto fijado a la misma mano y con oclusión correcta.

La comprobación de cada vista debe hacerse al tamaño de uso, además de ampliada. Generar PNG, transparencia o una cuadrícula no demuestra que estos puntos se cumplan.

La [metodología de Discrete Sprite Lab](https://github.com/qiulinfan/discrete-sprite-lab/blob/main/docs/methodology.md) separa los dos problemas que mezclamos: continuidad espacial entre direcciones y continuidad temporal entre poses. Propone reutilizar rasgos estables como una cabeza **solo en la misma vista** y tratar manos, mangas, piernas y botas como geometría específica de cada fase. Es un criterio útil para revisar nuestro trabajo, no una validación de su flujo completo ni una invitación a reducir imágenes sin evaluar los píxeles.

## Vías ordenadas por utilidad para este proyecto

| Vía | Qué controla de verdad | Qué falta | Estado |
| --- | --- | --- | --- |
| **Sprite canónico por capas + rig 2D** | Los mismos píxeles, la misma mano, la misma ropa y las mismas anclas dentro de cada vista; poses de charla, bocado y pago reproducibles. | Preparar una base y capas válidas para cada orientación; resolver oclusiones y uniones sin aspecto de muñeco recortado. | **Primera prueba recomendada para animación.** La implementación libre [AI Sprite Animation](https://github.com/JatCool/AI-Sprite-Animation) muestra un rig que conserva los píxeles; funciona como paquete de Unity, por lo que su código MIT es referencia técnica y no supone escoger Unity. |
| **Base volumétrica única + cámaras fijas** | Proporciones, lado de cada mano, espalda, poses y ocho proyecciones a escala común. | Convertir sus renders en un estilo 2D atractivo y pixel art válido, sin conservar apariencia de 3D. Las texturas ocultas por la vista inicial deben diseñarse. | Blender/MPFB documentados pero **todavía no probados** para Pepo. Serían una guía estructural, no el acabado entregado. |
| **ControlNet estructural + referencia visual en ComfyUI** | Puede imponer contorno/pose y condicionar rasgos con IP-Adapter en la misma generación. | Mantener cara, prendas y lado de la mano; producir capas y píxeles nativos. | [Una prueba local](../arte/pruebas/comfy-pepo-v03/README.md) fijó el perfil pero perdió colores/prendas y tardó casi nueve minutos. No ampliar este ajuste a ocho vistas. [ControlNet Canny SDXL](https://huggingface.co/xinsir/controlnet-canny-sdxl-1.0) tiene licencia Apache 2.0. |
| **Modelo de edición local dentro de Aseprite** | Permite modificar regiones concretas sin mover el resto y pedir otros ángulos. | Comprobar calidad y compatibilidad real en esta máquina; rotar sigue pudiendo inventar zonas ocultas. | [Spriteloom](https://github.com/vkarach/spriteloom) es una pista, **no una solución instalada**: usa FLUX.2 Klein, ~15 GB de modelo, BF16/descarga de capas y 16 GB mínimos de RAM. Nuestra GTX 1080 Ti dio `torch.cuda.is_bf16_supported(including_emulation=False) == False`; no asumir que funcionará en ella. |
| **Diffusión nativa a 64 px** | Produce a resolución lógica, sin depender de reducir un PNG de 1024 px. | Estilo, identidad y ropa de Pepo; vistas y acciones suficientes; licencias de datos. | [PIXEL-T2I](https://github.com/carlosuperb/PIXEL-T2I) investiga cuatro vistas LPC y declara que no es productor listo para juegos. No encaja directamente con la estética buscada. |

### Herramientas prometedoras que aún no resuelven el caso

- [Local Character Generator](https://github.com/JatCool/local-character-generator) genera un sprite de 48 px a partir de SDXL de 1024 px y documenta que su opción `--reference` **guarda** la imagen, pero los perfiles actuales no la usan para condicionamiento. Puede ayudar a generar un personaje aislado y datos de rig; no valida nuestras ocho vistas ni generación nativa directa.
- [Pixel Art Studio](https://github.com/velteyn/pixel-art-studio) anuncia pose + profundidad + referencia. En la revisión local `979168c`, su `ComfyUIClient.img2img` recibe `controlnet` pero no lo pasa a `_build_img2img_workflow`. Por ello esa ruta no aplica realmente el control en ComfyUI sin corregir código. El método estructural sigue siendo interesante; el programa no se recomienda como solución inmediata.
- [Spriteloom](https://github.com/vkarach/spriteloom) sí expone editar, inpaint y rotar desde Aseprite, pero los requisitos anteriores hacen incierta su ejecución en el hardware actual. No descargar otros 15 GB ni prometer resultados antes de verificar compatibilidad de precisión y memoria.

## Prueba siguiente con criterio de descarte

1. La prueba de ControlNet en **un solo perfil** ya se evaluó: orientó bien, pero alteró prendas y fue lenta. No producir siete vistas más con ese ajuste.
2. Preparar una **base canónica con capas y puntos anatómicos** para una única orientación y dos poses: reposo y brazo de pago. La IA realiza la preparación; Ivan R evalúa el resultado, sin redibujar él los recursos. Verificar que la mano conserva lado, tamaño y objeto durante el gesto.
3. Solo si las dos poses son legibles y no aparecen bordes internos o huecos, extender a tres ángulos (frente, perfil, espalda) y después al conjunto de ocho. Mantener cada original editable y exportaciones reproducibles.
4. Medir tiempo humano/IA, intentos descartados, retoques por vista y fallos visibles. Si el método exige rehacer cada fotograma, descartarlo en lugar de presentarlo como producción eficiente.

Esto es una **propuesta de ensayo**, no una elección de motor, modelo, resolución, paleta o estilo final. El contador de decisiones de producto sigue en 0/22.
