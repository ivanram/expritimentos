# Instrucciones para asistentes del proyecto

## Objetivo y contexto

Este repositorio reúne la planificación de Spanish Simulator y la investigación de su producción gráfica. Es un juego con estética pixel art desarrollado entre dos personas con ayuda de IA: minijuegos conectados entre sí sobre tópicos españoles. Algunos o todos podrán jugarse colaborativamente con una pantalla compartida y móviles conectados mediante QR. El reparto exacto de modos sigue pendiente.

Se priorizan estética, consistencia, facilidad de animación, rendimiento y facilidad de corrección. El tamaño mínimo de los archivos no es el objetivo principal.

El objetivo explícito de Ivan R es automatizar la producción de pixel art real con IA. Redibujar los recursos enteros a mano como solución principal no cumple ese objetivo. Distingue generación nativa o dibujo automatizado mediante MCP de ilustración grande reducida; las tapas v01 solo demuestran composición, no validan producción de pixel art. Consulta `docs/automatizar-pixelart.md` y mide intervención, revisiones y coste antes de recomendar un flujo como eficaz.

Restricción confirmada por Ivan R el 24 de octubre de 2026: no contratar más IAs ni añadir suscripciones o consumo de APIs de pago para este flujo. Priorizar las herramientas disponibles y alternativas sin pagos adicionales de IA. Las pruebas gratuitas limitadas no constituyen una solución gratuita sostenible. PixelLab/Retro Diffusion quedan como investigación, no como dependencias elegidas. No atribuir esta restricción presupuestaria a Ivan S.

El equipo son **Ivan R (kapichu)**, usuario de este chat, e **Ivan S (Alcachofo)**. Usa esos nombres y alias para evitar referencias ambiguas como «el otro Ivan». No atribuyas a uno las propuestas o confirmaciones del otro.

## Consultar según la tarea

- Para decisiones de producto y alcance, consulta `docs/decisiones.md`.
- Antes de diseñar o modificar gráficos, consulta `docs/arte.md` y las referencias aprobadas que existan.
- Para coordinar contribuciones, consulta `docs/colaboracion.md`.
- Para trabajar con las herramientas locales o retomar un experimento, consulta `docs/laboratorio.md`.

## Acuerdos de trabajo

- Distingue decisiones confirmadas, propuestas y cuestiones pendientes. No conviertas una sugerencia de una IA en una decisión del equipo.
- Conserva los números estables 01–22 de las decisiones del README. Añade nuevos números al final, sin renumerar los existentes. Los subpuntos, como 08.1, no cuentan de nuevo en el total. Mantén los estados, el contador y la barra sincronizados: solo «Acordada» cuenta como cerrada. El contador inicial es 0/22; mide acuerdos de detalle, no desarrollo ni el concepto ya confirmado.
- Cuando los responsables confirmen una decisión relevante, actualiza la documentación correspondiente. Conserva su motivo cuando ayude a evitar trabajo repetido.
- El usuario ha pedido mantener en GitHub el contexto que se concrete durante las conversaciones. Al terminar una tarea con información relevante, actualiza el README y los documentos afectados, comprueba los cambios y súbelos al repositorio, salvo que el usuario indique otra cosa. Resume acuerdos y propuestas; no publiques transcripciones completas ni información privada incidental.
- Mantén la documentación en español y usa explicaciones concretas.
- No des por aprobado un motor, una resolución, una paleta ni un estilo de personaje: siguen pendientes. El concepto de minijuegos sobre tópicos españoles y la estética pixel art ya están confirmados.
- Los experimentos anteriores son material de investigación, no referencias artísticas aprobadas.
- El visor SCUMM enlazado en el README se utiliza para estudiar principios de diseño. El usuario ha indicado expresamente que no se busca copiar sus recursos: producir recursos originales para el juego.
- Para gráficos, trabaja en cambios pequeños y comprobables visualmente; revisa la legibilidad al tamaño de uso y la consistencia con los recursos aprobados.
- Ivan R rechazó `arte/objetos/mesa-redonda-v01` por perspectiva incompatible. Antes de dar por integrado un objeto, revisar horizonte/fugas, plano superior, escala, apoyo y altura respecto al escenario. Resolver primero una composición conjunta cuando la cámara no esté fijada y separar después los recursos manteniendo encuadre/coordenadas. Igualar textura y luz no garantiza coherencia geométrica; alfa y tamaño correctos tampoco. No presentar una comprobación técnica como revisión visual suficiente.
- No afirmes que una imagen es bonita, una animación es fluida o un flujo es eficiente solo porque un script se ejecuta sin errores. Distingue comprobación técnica y revisión visual.
- Ivan R rechaza Pepo v03 por postura y proporciones. No continuar sus cuadrículas como referencia aprobada. Consultar `docs/investigacion-personajes-gratis.md`: antes de ampliar vistas, resolver una estructura anatómica común y comprobarla visualmente; no simular picado/contrapicado solo quitando o duplicando filas. Blender/MPFB es una alternativa investigada todavía sin ensayar; ComfyUI se ensayó después, con los límites indicados a continuación. Mantener la restricción de cero pagos adicionales por herramientas o servicios.
- La primera prueba de ComfyUI local se realizó después con dos imágenes de Pepo, documentadas en `arte/pruebas/comfy-pepo-v01`. Mejoró la postura general, pero cambió atributos de identidad y vestuario y produjo imágenes grandes con aspecto pixelado, no sprites nativos listos para animar. No dar por elegido ComfyUI como generador final ni confundir su salida con pixel art ya validado. Blender/MPFB siguen sin probarse aquí.
- Ivan R dijo que le gusta bastante el primer Pepo de esa prueba y pidió orientaciones. `arte/pruebas/comfy-pepo-v02` compara cinco giros locales fallidos en consistencia con una lámina conceptual de ocho vistas obtenida mediante la generación de imágenes incluida en el chat. La valoración de Ivan R se refiere a esa primera imagen; no da por aprobado el vestuario, las ocho vistas ni el estilo global. La lámina no es un conjunto de sprites nativos editables o animables. Mantener separados los dos métodos y no atribuir el acuerdo a Ivan S.
- Ivan R rechaza también la estética de `arte/pruebas/pxl-pago-v01` por percibir demasiado volumen o apariencia 3D. Ha aportado una referencia de personajes pequeños para el ensayo `arte/pruebas/pxl-estilo-v02`: estudiar proporciones, siluetas, caras mínimas, manchas de sombra y bordes selectivos; no conservar el modelado por tubos del ensayo anterior. La nueva referencia guía esta prueba, no implica aprobación global del estilo ni acuerdo de Ivan S.
- Ivan R rechazó el fondo `arte/escenarios/taberna-v01`: pixel art no exige paredes/suelos planos ni una paleta de 32 colores. Conservar volumen, iluminación, materiales y formas con carácter al simplificar. No repintar grandes zonas ni cuantizar colores por defecto; revisar siempre la exportación real al tamaño de uso. Ivan R ha valorado positivamente v02 y ha pedido comprobar ese lenguaje visual en una mesa independiente. No atribuir esa valoración a Ivan S ni convertirla en cierre de la dirección artística global.
- Mantén los originales editables separados de las exportaciones. Cuando se incorpore producción de recursos, favorece exportaciones reproducibles.
- Evita pisar el trabajo simultáneo de otra persona, especialmente en archivos `.aseprite`.
- Las herramientas, compilaciones, entornos virtuales, registros locales y configuraciones con rutas de una máquina quedan fuera de esta publicación de documentación. No añadas el contenido de las carpetas ignoradas al repositorio como efecto secundario de otra tarea.
- Comprueba los enlaces y revisa `git diff --check` cuando cambies documentación. No hacen falta pruebas de ejecución para cambios exclusivamente documentales.

## Contexto compartido

El repositorio contiene el contexto común. No supongas acceso a las conversaciones privadas de ninguno de los participantes ni que la otra IA conoce cambios locales que aún no se han subido.
