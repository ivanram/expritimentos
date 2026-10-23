# Spanish Simulator

Juego con estética **pixel art** compuesto por **minijuegos conectados entre sí sobre tópicos españoles**. Se desarrollará entre dos personas con ayuda de IA.

Algunos o todos los minijuegos podrán jugarse colaborativamente: una pantalla compartida muestra la partida y los jugadores conectan sus móviles mediante un código QR para utilizarlos como mandos. El reparto exacto entre modos cooperativos, competitivos o mixtos está pendiente de decidir.

Este repositorio reúne el concepto, las decisiones y la investigación para producir el juego. Se priorizan una estética atractiva y coherente, buenas animaciones, rendimiento y un proceso eficaz de creación con IA. El ahorro de espacio al estilo de las máquinas antiguas no es la prioridad.

## Primer minijuego: Pagar la cuenta

El primer concepto ya está disponible en [este prototipo de Pagar la cuenta](https://spanish-simulator.salmeinmotion.com/).

En una revisión inicial realizada el 23 de octubre de 2026 se observó una sala con QR y código de acceso, lista de jugadores e instrucciones para usar el móvil como mando: tocar para ofrecer el pago y deslizar al lado contrario del camarero para esquivar. No se ha probado una partida multijugador completa ni auditado su implementación. La tecnología del prototipo no se da por elegida para el juego definitivo y su aspecto no fija todavía la dirección artística final.

## Decisiones que necesitamos tomar

El concepto y la estética pixel art están confirmados. Las cuestiones de esta tabla son **decisiones pendientes**, no requisitos técnicos ya aprobados.

| Área | Qué debemos concretar |
| --- | --- |
| Experiencia y público | A quién va dirigido, tono del humor y tratamiento de los tópicos; duración de una sesión, dificultad y motivos para volver a jugar. |
| Minijuegos y conexión | Catálogo inicial, reglas y objetivos; cómo se pasa de uno a otro y qué comparten: personajes, puntuación, historia, economía o progresión. Definir alcance de la primera versión. |
| Modos de juego | Qué minijuegos son cooperativos, competitivos o mixtos; mínimo y máximo de jugadores, posibilidad de jugar solo, sustitución de ausentes y participación de espectadores. |
| Plataformas y distribución | Dónde funciona la pantalla principal: navegador, ordenador, televisión, consola u otra opción; si requiere instalación y cómo se distribuye. Elegir una primera plataforma antes de ampliar. |
| Dispositivos y controles | Móviles, sistemas y navegadores compatibles; orientación, tamaño de botones, gestos y respuesta táctil. Decidir alternativas con teclado o mando, y qué ocurre si alguien no tiene móvil. |
| Tecnología y arquitectura | Motor o tecnología del juego y de los mandos; comunicación en tiempo real, autoridad sobre el estado de partida, reutilización entre minijuegos y herramientas de desarrollo. Comprobar qué conviene conservar del prototipo. |
| Salas y conexión | Creación de sala, acceso por QR y código manual, quién inicia y pausa; misma Wi-Fi o acceso por Internet, incorporación tardía, desconexión/reconexión, latencia, sincronización y caducidad de salas. |
| Dirección artística | Perspectiva, resolución base, escalado, paleta, iluminación, contornos, proporciones y nivel de detalle. Definir cómo se relacionan fondos, personajes, objetos e interfaz. |
| Personajes | Elenco, personalidad, función en los minijuegos, siluetas, vestuario, expresiones y personalización. Decidir qué vistas, poses y animaciones necesita cada uno. |
| Animación y audio | Tipo y ritmo de animación, prioridades y reutilización; música, efectos, posibles voces, identidad sonora, controles de volumen y procedencia de los recursos. |
| Textos e idiomas | Voz del juego, humor, nombres y terminología; idiomas iniciales, traducción de referencias culturales, fuentes y espacio para textos de distinta longitud. |
| Usabilidad y accesibilidad | Legibilidad a distancia en la pantalla y en el móvil, contraste, señales que no dependan solo del color, subtítulos, aprendizaje de controles y opciones para distintos ritmos o capacidades. |
| Rendimiento y calidad | Dispositivos mínimos, fluidez y tiempos de carga; respuesta de los mandos, presupuesto de gráficos/efectos y pruebas con varios móviles y conexiones reales. |
| Operación y datos | Alojamiento y coste recurrente; si hacen falta cuentas o bastan invitados, qué progreso se guarda, duración de las sesiones y mantenimiento tras publicar. |
| Trabajo conjunto y alcance | Reparto de tareas y decisiones, revisión de cambios, organización de archivos, criterios para dar algo por terminado y tamaño de la primera versión jugable. |

## Cómo crear los gráficos con IA

Necesitamos encontrar un método que produzca recursos **bonitos, coherentes, editables y fáciles de animar**, con un coste razonable de tiempo, tokens y revisiones. Las herramientas disponibles no garantizan por sí solas esa calidad.

Propuestas que debemos investigar y validar:

- **Guía visual común:** referencias aprobadas, paleta, proporciones, luz, contornos, perspectiva, tipografía, interfaz y ejemplos de lo que encaja y lo que queremos evitar.
- **Fichas de personaje:** diseño base, silueta, colores, vestuario, vistas, expresiones, poses y rasgos que deben mantenerse al animar. Decidir cuánto detalle necesita cada ficha para ser útil a personas e IA.
- **Recursos maestros y piezas reutilizables:** una pequeña biblioteca aprobada de personajes, objetos y componentes de interfaz de la que derivar variantes.
- **Proceso por etapas:** referencia y silueta, colores, sombras, detalles y animación; revisión al tamaño real de uso y dentro de una pantalla del juego.
- **Comparación de métodos:** probar MCP, Lua, Pillow y generación de imágenes en tareas equivalentes. Investigar buenas prácticas, hacer pruebas pequeñas y documentar lo que funcione en este proyecto.
- **Medición de eficiencia:** tiempo hasta un resultado aceptable, tokens o coste de API cuando se puedan obtener, número de llamadas y revisiones, retoque manual, coherencia y facilidad para modificar una parte. No confundir que un script funcione con que el resultado sea bueno.
- **Entrega reproducible:** definir originales editables, capas, etiquetas, puntos de apoyo, nombres y exportación para el motor. Fijar criterios de aceptación y un presupuesto de producción antes de crear muchos recursos.

No están decididos el tamaño de los sprites, el número de colores ni los fotogramas. Las cifras mencionadas en conversaciones anteriores son ejemplos para pruebas.

## Referencia de estudio: recursos SCUMM

El compañero del proyecto ha creado una [herramienta de exploración de recursos SCUMM, enlazada a Day of the Tentacle, sala 7](https://scumm.rea.salmeinmotion.com/dott/#room=7). El visor permite consultar escenarios y objetos en contexto y dispone de secciones de personajes, animaciones, música y sonidos.

La idea es **aprender e inspirarnos, creando recursos originales para Spanish Simulator**. Podemos estudiar composición, jerarquía visual, paletas, proporciones, separación de fondos y objetos, reutilización de piezas y ritmo de animación. No se busca copiar ni incorporar los recursos extraídos al juego. Su uso como referencia no implica haber elegido el estilo de Day of the Tentacle.

## Orden de trabajo propuesto

1. Acordar público, experiencia de juego y alcance de la primera versión, usando Pagar la cuenta como caso inicial.
2. Elegir plataformas iniciales y validar el recorrido pantalla–QR–móvil con varios jugadores, incluida la reconexión; comparar tecnologías con esa necesidad concreta.
3. Explorar unas pocas direcciones visuales en una pantalla representativa y aprobar una antes de producir el resto de recursos.
4. Crear una guía visual y una primera ficha de personaje; comparar métodos de producción de un mismo recurso estático y animado, midiendo calidad y esfuerzo.
5. Completar una versión pequeña de Pagar la cuenta, probarla con personas y usar lo aprendido para decidir qué elementos compartirán los siguientes minijuegos.

Este orden es una propuesta, pendiente de acordar entre los dos responsables.

## Mantener el contexto compartido

Por indicación del usuario, iremos resumiendo y subiendo a GitHub el contexto relevante y los acuerdos de las conversaciones. Las propuestas se identificarán como tales. Las conversaciones privadas no se sincronizan automáticamente ni hace falta publicar transcripciones completas.

Para cada decisión importante conviene anotar: pregunta, alternativas, estado, elección y motivo cuando se resuelva, responsable y una prueba o referencia si la necesita. Actualizaremos el resumen de este README y el [registro de decisiones](docs/decisiones.md).

## Documentación y estado del repositorio

- [AGENTS.md](AGENTS.md): instrucciones para las IA, incluida la pauta de mantener el contexto publicado.
- [Contexto y decisiones](docs/decisiones.md): acuerdos confirmados y cuestiones pendientes.
- [Dirección artística](docs/arte.md): recomendaciones de pixel art, animación y producción con IA.
- [Colaboración](docs/colaboracion.md): organización del trabajo entre dos personas y sus asistentes.
- [Laboratorio local](docs/laboratorio.md): Aseprite, MCP, visor y experimentos gráficos recuperados.

Actualmente este repositorio contiene planificación y documentación. El prototipo está en el enlace externo; su código, las herramientas instaladas y los gráficos del laboratorio no están incluidos aquí.

Para incorporarse con una IA, pedirle que lea primero AGENTS.md y los documentos que correspondan a su tarea. No todas las herramientas cargan automáticamente los mismos archivos.
