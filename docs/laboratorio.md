# Estado del laboratorio local

Comprobaciones realizadas el 23 de octubre de 2026. Este documento describe el entorno recuperado; no es una medición comparativa de calidad artística ni incluye los archivos de trabajo en GitHub.

## Herramientas disponibles localmente

| Herramienta | Uso |
| --- | --- |
| Aseprite, compilación 1.3.18.6-dev | Editor, animación, scripts Lua y exportación por lotes. |
| aseprite-mcp | Servidor MCP para crear, modificar e inspeccionar gráficos. |
| aseprite-live | Visor local de cambios, fotogramas y animaciones. |
| MSVC y Skia | Dependencias de la compilación local de Aseprite. |
| Pillow | Generación y comprobación de imágenes desde Python. |

Las carpetas locales de las herramientas están reunidas en un mismo directorio de trabajo y quedan ignoradas por Git. El entorno MCP utiliza Python 3.13. Los lanzadores y la configuración MCP actuales son locales y no forman parte de esta publicación.

## Experimentos recuperados

Los nombres son rutas relativas dentro de la carpeta local de Aseprite, no enlaces a recursos publicados en este repositorio.

| Proyecto | Tamaño | Fotogramas | Generador identificado |
| --- | --- | --- | --- |
| `cyberpunk_drive.aseprite` | 96×64 | 12 | `generate_demo.py`, mediante Lua. |
| `bar_espanol_tapas.aseprite` | 320×200 | 12 | `build_spanish_bar.py`, Pillow y ensamblaje Lua. |
| `bar_tapas_lucasarts.aseprite` | 320×200 | 4 | `build_lucasarts_bar.py`, llamadas MCP. |
| `tapas_vibes/tapas_vibes.aseprite` | 192×108 | 32 | `tapas_vibes/build_tapas_vibes.py`, listas de llamadas MCP. |
| `la_cuenta.aseprite` | 192×112 | 23 | No identificado. |

Estos experimentos son material de investigación. El equipo todavía no ha aprobado ninguno como referencia de estilo del juego.

## Comprobaciones técnicas completadas

- El ejecutable de Aseprite arranca desde la nueva ubicación.
- El servidor MCP responde y publica 123 herramientas.
- Los cinco proyectos se pueden inspeccionar por MCP y exportar a hojas PNG con datos JSON; el número de fotogramas exportados coincide.
- El visor HTTP responde y renderiza una copia de prueba de la animación cyberpunk.
- CMake se ha reconfigurado con las nuevas rutas; la simulación de compilación de Ninja termina correctamente. No se ha recompilado todo el editor.
- Se verificó un inventario de 28.127 archivos durante la consolidación. Los 16.257 archivos que quedaron en el origen tras un movimiento parcial se comprobaron mediante SHA-256 contra sus copias.

Los registros detallados y las copias de mantenimiento se conservan localmente y no se publican aquí. La guía operativa de esa máquina se conserva en `mantenimiento/README-laboratorio-local.md`, fuera de Git.

## Investigación pendiente

Comparar calidad visual, tiempo y facilidad de corrección de MCP, Lua y las herramientas de generación de imágenes para una misma tarea representativa. Haber ejecutado correctamente los experimentos existentes no demuestra todavía qué método es el más adecuado para producir el juego.
