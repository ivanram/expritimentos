# Investigación: personajes consistentes sin servicios de pago

24 de octubre de 2026. Ivan R rechaza Pepo v03 por postura y proporciones y solicita investigar métodos que el asistente pueda ejecutar sin comprar herramientas ni contratar más IAs. **La revisión v03 queda rechazada, no es una referencia aprobada.**

## Conclusión

La herramienta de dibujo actual funciona como exportador, pero la producción artística no ha funcionado. No hay evidencia de que seguir ampliando cuadrículas independientes vaya a resolver anatomía, cámara o estilo. La siguiente prueba recomendada es una estructura humana coherente en Blender/MPFB, seguida de una comparación pequeña de acabado. ComfyUI local es una segunda vía gratuita para explorar diseño, con compatibilidad y rendimiento aún por probar.

Son recomendaciones de investigación, no un flujo probado ni una decisión del equipo. En este turno se consultaron fuentes primarias, se revisó el código propio y se comprobó el hardware; no se instalaron Blender, MPFB, ComfyUI ni modelos, ni se produjo otro personaje.

## Qué falló realmente en Pepo

La revisión de `arte/personajes/pepo-v03/pepo.px.js` muestra:

1. Cabeza, camiseta y vaqueros proceden de cuadrículas separadas, recolocadas por offsets. Compartir una altura y una línea de suelo no garantiza un cuerpo equilibrado.
2. Los brazos se describen con filas y desplazamientos independientes; no hay esqueleto común que limite longitudes y articule hombro, codo y muñeca.
3. Las vistas opuestas reflejan bases y cambian brazos. No se derivan de un volumen común; eso permite incoherencias de orientación y de silueta.
4. `shirtHigh` y `legsHigh` eliminan filas, y las variantes bajas repiten otras. Esto cambia la altura aparente, pero no calcula una proyección de cámara. Fue insuficiente presentarlo como picado/contrapicado.
5. La revisión visual del asistente no detectó o no corrigió esos problemas antes de entregar. Las pruebas de alfa, capas y altura no los validaban.

Cambiar de MCP sin cambiar esta construcción no resuelve el problema. Tampoco basta con añadir otra instrucción de estilo o más vistas.

## Alternativas ejecutables por el asistente

| Vía | Cómo se automatiza | Qué aporta | Límite real |
| --- | --- | --- | --- |
| Blender local | API Python y ejecución sin interfaz mediante `--background --python`. | Un modelo y un esqueleto compartidos, cámaras coherentes, poses y exportaciones repetibles. | Un modelo mal diseñado también produce sprites feos. Un render pequeño puede conservar apariencia 3D. |
| MPFB para Blender | Código y servicios Python del complemento; generación, ajuste y rigging de una base humana. | Evita inventar toda la anatomía con tubos o cuadrículas. Permite partir de un humano y modificar proporciones. | Su punto de partida es humano/realista, no el estilo cartoon pedido. Hay que adaptar silueta, cabeza y ropa. |
| ComfyUI local + modelo descargable | API local; workflows guardados, semillas y parámetros registrados. | Explorar diseños con un modelo visual en lugar de depender solo del dibujo del asistente por coordenadas. | Puede cambiar identidad, anatomía y ropa entre vistas. No garantiza cuadrícula limpia, transparencia o animación consistente. |
| Aseprite local + pxl | Lua/CLI/MCP y código de dibujo ya disponibles. | Capas, exportación y ajustes puntuales reproducibles a resolución nativa. | No aportan por sí solos capacidad de diseño anatómico. No continuar como generador principal de vistas independientes. |

Blender es software libre, admite scripts Python y uso comercial del arte generado. MPFB es gratuito sin funciones premium obligatorias; sus recursos básicos están bajo CC0. ComfyUI es software libre y ofrece una API local. Los modelos y complementos que se añadan tienen sus propias licencias: usar únicamente descargas que permitan el uso previsto. Fuentes: [Blender](https://www.blender.org/features/), [licencia Blender](https://www.blender.org/about/license/), [CLI de Blender](https://docs.blender.org/manual/id/4.0/advanced/command_line/arguments.html), [MPFB gratuito](https://static.makehumancommunity.org/mpfb/faq/is_it_really_free.html), [licencias MPFB](https://github.com/makehumancommunity/mpfb2/blob/master/LICENSE.md), [API de ComfyUI](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/basic_api_example.py).

## Blender y MPFB: control estructural

MPFB documenta creación de humanos, ajustes de forma, rig estándar, ropa y helpers de cinemática inversa para manos. Sus recursos de desarrollo describen el código y el sistema de poses. Esto permite plantear que el asistente construya y controle la prueba desde scripts; **aún no se ha demostrado esa integración en este repositorio**. [Guía MPFB](https://static.makehumancommunity.org/mpfb/docs/getting_started.html), [desarrollo](https://static.makehumancommunity.org/mpfb/developer.html).

Propuesta: una base humana vestida, simplificada y estilizada, con columna, pelvis y extremidades relacionadas. Renderizar esa misma base desde frontal, perfil y tres cuartos; después mover la cámara en elevación. Una cámara ortográfica conserva escala sin convergencia de paralelas, pero su elevación sigue cambiando visibilidad y acortamiento aparente. [Documentación de proyección](https://docs.blender.org/manual/en/3.0/editors/3dview/navigate/projections.html).

Usar 3D como estructura no obliga a aceptar un acabado volumétrico. Se pueden ensayar materiales planos, sombras discretas y contornos selectivos. Sin embargo, renderizar a baja resolución no equivale automáticamente a pixel art con agrupaciones de píxeles bien diseñadas. El acabado se debe evaluar por separado. Evitar repetir el ensayo de brazos tubulares con otra aplicación.

## ComfyUI: vía generativa local condicionada

El proyecto publica ejemplos de API que permiten encolar un workflow desde Python. ControlNet documenta condicionamiento por pose y profundidad; se podrían usar guías procedentes del modelo 3D. La inferencia propuesta es que eso reduzca libertad geométrica respecto a prompts solos, no que garantice identidad o poses correctas. [ComfyUI](https://github.com/Comfy-Org/ComfyUI), [ControlNet](https://github.com/lllyasviel/ControlNet).

Existe, por ejemplo, la LoRA descargable [nerijs/pixel-art-xl](https://huggingface.co/nerijs/pixel-art-xl), para estudiar acabado pixel art con SDXL. Su ficha declara licencia CreativeML Open RAIL-M. No es un modelo autónomo: necesita la base compatible. No se ha probado aquí y no demuestra generación nativa a 64×88 ni consistencia entre direcciones. Tampoco debe mezclarse con un ControlNet de SD 1.5: las familias de modelos deben coincidir. La selección final de base, control y estilo queda pendiente de una prueba pequeña.

Comprobación local con `nvidia-smi`: **GTX 1080 Ti, 11264 MiB de VRAM**. La memoria disponible no basta para inferir compatibilidad ni velocidad. El README oficial actual de ComfyUI ofrece un portable con **CUDA 12.6 y Python 3.12** para NVIDIA serie 10 y anteriores; el portable estándar está dirigido a serie 20 y posteriores. Esta es la ruta documentada que habría que ensayar, sin cambiar el controlador global ni el entorno de Aseprite. [Instalación oficial](https://github.com/Comfy-Org/ComfyUI#installing).

La prueba debería empezar con una imagen y batch 1, registrar VRAM, tiempo y errores y ampliar solo si funciona. Sin inferencia medida no se puede prometer una velocidad útil. Los costes monetarios adicionales de licencias/API serían cero para la configuración local propuesta; permanecen electricidad, almacenamiento, descargas y uso del asistente ya contratado.

## Qué aprender del proceso artístico

SLYNYRD describe partir de proporciones y de un maniquí simplificado antes de detallar y animar. Su tutorial distingue modelos de proporciones realistas y estilizadas; no corresponde imponer ocho cabezas al personaje cute del juego. El principio aplicable es resolver primero estructura y silueta, y después conservarlas al añadir detalle. [Anatomía](https://www.slynyrd.com/blog?offset=1716987540396), [maniquí y animación](https://www.slynyrd.com/blog).

Consultar estas explicaciones públicas no requiere comprar sus packs; los dibujos del tutorial no se incorporarán al juego.

## Prueba mínima recomendada, con criterio de descarte

1. **Estructura:** un solo Pepo en frontal, perfil y tres cuartos, sin microdetalle. Base humana común, pose neutral, manos fuera de bolsillos para ver los brazos. Revisar equilibrio, hombros/cadera, longitudes, cuello y apoyo. No producir ocho vistas si estas tres fallan.
2. **Acabado:** comparar una versión plana obtenida de la estructura con una pequeña muestra generativa local, si ComfyUI funciona. Mantener vestuario, escala y pose. Evaluar rostro, silueta y agrupaciones de píxeles, no solo paleta y resolución. Las imágenes generativas son propuestas visuales hasta demostrar salida utilizable.
3. **Repetición:** producir una segunda pose de pago desde la misma estructura. Comprobar identidad, agarre y articulaciones. Después añadir las cámaras alta y baja, renderizadas desde el mismo modelo.
4. **Medir:** tiempo de preparación y ejecución, tamaño de descargas, intentos descartados, cambios manuales del asistente, intervención exigida al usuario y tokens si hay medición disponible. Guardar fuentes, parámetros y versiones.

Si el acabado sigue pareciendo un muñeco 3D o necesita repintado completo en cada vista, la vía no cumple el objetivo artístico/eficiencia. Si la IA local cambia el personaje o produce píxeles inconsistentes, no sirve como productora final de sprites aunque algún concepto sea atractivo. El asistente realiza instalación, programación, producción y correcciones; no se traslada a Ivan R la tarea de aprender a dibujar o usar Blender.

## Fuera del flujo propuesto

PixelLab y Retro Diffusion siguen excluidos por requerir servicios de pago para el flujo considerado. Pixor también se ha descartado como dependencia: su aplicación de escritorio es de pago, aunque ofrezca demo web gratuita. No recomendar una demo limitada como sustituto de un proceso gratuito sostenible. [FAQ Pixor](https://pixor.art/faq/).

No se presenta la generación de imágenes incluida en otra interfaz como ilimitada ni se asume acceso automatizado gratuito por disponer de una suscripción. Tampoco se propone contratar un MCP o proveedor de nube: Blender se puede controlar por Python/CLI y ComfyUI por su API local.
