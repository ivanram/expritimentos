# Instrucciones para asistentes del proyecto

## Objetivo y contexto

Este repositorio reúne la planificación de Spanish Simulator y la investigación de su producción gráfica. Es un juego con estética pixel art desarrollado entre dos personas con ayuda de IA: minijuegos conectados entre sí sobre tópicos españoles. Algunos o todos podrán jugarse colaborativamente con una pantalla compartida y móviles conectados mediante QR. El reparto exacto de modos sigue pendiente.

Se priorizan estética, consistencia, facilidad de animación, rendimiento y facilidad de corrección. El tamaño mínimo de los archivos no es el objetivo principal.

## Consultar según la tarea

- Para decisiones de producto y alcance, consulta `docs/decisiones.md`.
- Antes de diseñar o modificar gráficos, consulta `docs/arte.md` y las referencias aprobadas que existan.
- Para coordinar contribuciones, consulta `docs/colaboracion.md`.
- Para trabajar con las herramientas locales o retomar un experimento, consulta `docs/laboratorio.md`.

## Acuerdos de trabajo

- Distingue decisiones confirmadas, propuestas y cuestiones pendientes. No conviertas una sugerencia de una IA en una decisión del equipo.
- Cuando los responsables confirmen una decisión relevante, actualiza la documentación correspondiente. Conserva su motivo cuando ayude a evitar trabajo repetido.
- El usuario ha pedido mantener en GitHub el contexto que se concrete durante las conversaciones. Al terminar una tarea con información relevante, actualiza el README y los documentos afectados, comprueba los cambios y súbelos al repositorio, salvo que el usuario indique otra cosa. Resume acuerdos y propuestas; no publiques transcripciones completas ni información privada incidental.
- Mantén la documentación en español y usa explicaciones concretas.
- No des por aprobado un motor, una resolución, una paleta ni un estilo de personaje: siguen pendientes. El concepto de minijuegos sobre tópicos españoles y la estética pixel art ya están confirmados.
- Los experimentos anteriores son material de investigación, no referencias artísticas aprobadas.
- El visor SCUMM enlazado en el README se utiliza para estudiar principios de diseño. El usuario ha indicado expresamente que no se busca copiar sus recursos: producir recursos originales para el juego.
- Para gráficos, trabaja en cambios pequeños y comprobables visualmente; revisa la legibilidad al tamaño de uso y la consistencia con los recursos aprobados.
- No afirmes que una imagen es bonita, una animación es fluida o un flujo es eficiente solo porque un script se ejecuta sin errores. Distingue comprobación técnica y revisión visual.
- Mantén los originales editables separados de las exportaciones. Cuando se incorpore producción de recursos, favorece exportaciones reproducibles.
- Evita pisar el trabajo simultáneo de otra persona, especialmente en archivos `.aseprite`.
- Las herramientas, compilaciones, entornos virtuales, registros locales y configuraciones con rutas de una máquina quedan fuera de esta publicación de documentación. No añadas el contenido de las carpetas ignoradas al repositorio como efecto secundario de otra tarea.
- Comprueba los enlaces y revisa `git diff --check` cuando cambies documentación. No hacen falta pruebas de ejecución para cambios exclusivamente documentales.

## Contexto compartido

El repositorio contiene el contexto común. No supongas acceso a las conversaciones privadas de ninguno de los participantes ni que la otra IA conoce cambios locales que aún no se han subido.
