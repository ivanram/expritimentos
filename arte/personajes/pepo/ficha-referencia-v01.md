# Pepo · ficha de referencia para la primera prueba de animación

**Estado:** propuesta de trabajo, 24 de octubre de 2026. Ivan R dijo que le gusta bastante el [primer Pepo de ComfyUI](../../pruebas/comfy-pepo-v01/out/pepo-01-9-0.png). Eso permite usarlo como **referencia visual para esta prueba**, pero no aprueba su vestuario, un sprite final ni el estilo del juego. Ivan S aún no ha valorado esta ficha. Las decisiones 08 y 17 siguen pendientes.

![Pepo de ComfyUI, intento 1](../../pruebas/comfy-pepo-v01/out/pepo-01-9-0.png)

## Lectura de la imagen

La figura está casi de frente, con un ligero tres cuartos. Tiene una postura erguida, hombros aproximadamente nivelados, cabeza algo grande para el cuerpo y complexión adulta media. El pelo negro es corto, desordenado y forma una silueta irregular. Se ven cejas oscuras, ojos pequeños, nariz legible, sonrisa discreta y barba oscura bastante más poblada que «algo de barba» de la petición original.

En **esta imagen** viste camiseta rojo teja, sobrecamisa azul grisácea abierta y de manga corta, pantalón marrón de pernera recta y zapatillas claras con zonas oscuras. No podemos afirmar por la imagen que el pantalón sea vaquero. El encargo inicial de Ivan R decía **camiseta y vaqueros**, pelo negro, ojos marrones y algo de barba para un español de 40 años. El color de iris no se distingue con seguridad en este PNG. Para el ensayo de continuidad se propone mantener las prendas visibles en el intento 1; escoger el vestuario definitivo queda pendiente.

La imagen original es una ilustración de 1024 × 1024 con aspecto pixelado, fondo lila y sombra de suelo. No es un sprite transparente, por capas ni pixel art nativo validado. Se usa como guía de diseño, no como original maestro listo para animar.

## Convención anatómica para la prueba

**Izquierda y derecha se nombran desde Pepo, nunca desde quien mira la pantalla.** En la imagen frontal, su brazo **derecho** aparece a la izquierda de la pantalla y cuelga junto al muslo; su mano **izquierda** aparece a la derecha de la pantalla, junto a la abertura del bolsillo. La mano izquierda parece apoyada en el borde del bolsillo, aunque la imagen no permite asegurar que esté metida hasta la muñeca.

Para probar la acción de pago, proponemos **mano derecha libre para sostener la tarjeta** y **mano izquierda cerca del bolsillo**. La tarjeta debe permanecer unida a la mano derecha durante todo el gesto. Al girar o espejar una vista, no se deben intercambiar manos ni bolsillos. Esta asignación es una regla del **ensayo**, no una decisión de personaje aprobada por el equipo.

## Rasgos que debe conservar una versión nueva

| Rasgo | Referencia de esta prueba | Comprobación visual |
| --- | --- | --- |
| Silueta | Adulto de complexión media, cabeza ligeramente grande, hombros amplios y piernas rectas con pequeñas variaciones de contorno. | Reconocible sin dibujar ojos, costuras o textura. |
| Cabeza y cara | Pelo negro irregular; cejas y barba oscuras; nariz separable de boca y barba. | Pelo unido a la cabeza, nariz legible al tamaño de uso y cara sin cambiar entre poses. |
| Prendas visibles | Camiseta rojo teja bajo sobrecamisa azul grisácea abierta; pantalón marrón; zapatillas claras. | La abertura, mangas, bajos y colores no cambian durante la animación. |
| Brazos | Derecho libre junto al muslo; izquierdo junto al bolsillo. Hombros a altura parecida. | El gesto de pago usa el derecho y conserva proporción de brazo y antebrazo. |
| Apoyo | Dos pies separados moderadamente sobre una misma línea de suelo. | Cuerpo y pies no saltan de sitio al levantar el brazo. |
| Contorno | Bordes oscuros selectivos en la silueta, con formas suaves e irregulares. | La unión de hombro, manga y brazo no queda rodeada por un borde que parezca muñeco articulado. |

La relación de tamaños se toma **de la silueta**, no de los bloques aparentes de la imagen: cabeza con pelo de aproximadamente un sexto de la altura de la figura; ancho total de hombros cercano al doble del ancho de cabeza; manos alrededor de la cadera y mitad superior del muslo. Son proporciones orientativas para el boceto de producción, no coordenadas exactas ni resolución aprobada. Los puntos de articulación y la cuadrícula se fijarán al construir el sprite de prueba, tras comprobarlos al tamaño de uso.

## Alcance pendiente

- La parte trasera de cabeza, barba, sobrecamisa y calzado **no está definida por esta imagen**; no inferirla de la [lámina de ocho vistas rechazada](../../pruebas/comfy-pepo-v02/README.md).
- Queda por confirmar con Ivan R e Ivan S si Pepo conservará estas prendas o volverá a camiseta y vaqueros, y qué mano usará definitivamente para pagar.
- Todavía no se han elegido resolución, paleta, escala en la escena ni motor. Esta ficha solo prepara **una orientación y dos poses** para comprobar continuidad.
