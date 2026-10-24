"""Ensayo reproducible de transferencia a una cuadrícula nativa, no sprite aprobado.

Parte de la primera imagen de ComfyUI y separa sus regiones visibles sin pedir
otro modelo. No dibuja las zonas ocultas bajo los brazos ni crea vistas nuevas.
"""

from __future__ import annotations

import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "arte/pruebas/comfy-pepo-v01/out/pepo-01-9-0.png"
OUT = HERE / "out"

# Proporción uniforme aproximada: 344/48 ~= 924/128.
BOX = (360, 50, 704, 974)
SIZE = (48, 128)
LAYER_ORDER = ["piernas", "torso", "brazo_derecho", "brazo_izquierdo", "cabeza"]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    src = np.array(Image.open(SOURCE).convert("RGB"), dtype=np.uint8)
    x0, y0, x1, y1 = BOX
    crop = src[y0:y1, x0:x1]
    height, width = crop.shape[:2]
    bg = np.array([170, 155, 177], dtype=np.int16)
    rgb = crop.astype(np.int16)
    dist = np.linalg.norm(rgb - bg, axis=2)
    foreground = dist > 19

    # La sombra lila del suelo no forma parte del personaje.
    yy = np.arange(y0, y1)[:, None]
    foreground &= ~((yy > 840) & (rgb[:, :, 0] <= rgb[:, :, 2] + 6))
    foreground &= ~((yy > 885) & (np.arange(x0, x1)[None, :] < 414))
    foreground &= ~((yy > 885) & (np.arange(x0, x1)[None, :] > 625))
    xx = np.arange(x0, x1)[None, :]
    foreground &= ~((yy > 545) & (xx > 500) & (xx < 560) & (rgb[:, :, 0] <= rgb[:, :, 2] + 6))

    small_coverage = cv2.resize(
        foreground.astype(np.float32), SIZE, interpolation=cv2.INTER_AREA
    )
    native_mask = small_coverage >= 0.38
    # Mediana de los colores de primer plano de cada celda. Las celdas fronterizas
    # toman un color cercano de figura y no mezclan el fondo lila.
    tw, th = SIZE
    native_rgb = np.zeros((th, tw, 3), dtype=np.uint8)
    for sy in range(th):
        ay = round(sy * height / th)
        by = round((sy + 1) * height / th)
        for sx in range(tw):
            if not native_mask[sy, sx]:
                continue
            ax = round(sx * width / tw)
            bx = round((sx + 1) * width / tw)
            pixels = crop[ay:by, ax:bx][foreground[ay:by, ax:bx]]
            if len(pixels):
                native_rgb[sy, sx] = np.median(pixels, axis=0).astype(np.uint8)

    # Reduce variación cromática espuria. Se conserva el RGB del centro de cada
    # grupo y no se difunde error entre píxeles vecinos.
    pixels = native_rgb[native_mask].astype(np.float32)
    cv2.setRNGSeed(24102026)
    _, labels, centers = cv2.kmeans(
        cv2.cvtColor(pixels.reshape(1, -1, 3).astype(np.uint8), cv2.COLOR_RGB2LAB)
        .reshape(-1, 3)
        .astype(np.float32),
        42,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.15),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    # El color representativo es la mediana RGB de los píxeles asignados.
    palette = np.array(
        [np.median(pixels[labels[:, 0] == i], axis=0) for i in range(42)],
        dtype=np.uint8,
    )
    native_rgb[native_mask] = palette[labels[:, 0]]

    # Clasificación de las partes visibles en coordenadas del PNG de referencia.
    sx = x0 + (np.arange(tw)[None, :] + 0.5) * width / tw
    sy = y0 + (np.arange(th)[:, None] + 0.5) * height / th
    sx = np.broadcast_to(sx, (th, tw))
    sy = np.broadcast_to(sy, (th, tw))
    kind = np.full((th, tw), "", dtype=object)
    kind[native_mask] = "torso"
    kind[native_mask & (sy >= 543)] = "piernas"
    kind[native_mask & (sy >= 265) & (sy < 651) & (sx < 446)] = "brazo_derecho"
    kind[native_mask & (sy >= 286) & (sy < 570) & (sx > 620)] = "brazo_izquierdo"
    kind[native_mask & (sy < 252) & (sx > 437) & (sx < 614)] = "cabeza"

    layers: dict[str, np.ndarray] = {}
    for name in LAYER_ORDER:
        rgba = np.zeros((th, tw, 4), dtype=np.uint8)
        present = kind == name
        rgba[present, :3] = native_rgb[present]
        rgba[present, 3] = 255
        layers[name] = rgba

    # Completa únicamente tela oculta BAJO las mangas, para que al desplazar un
    # brazo no aparezca de inmediato un agujero. El dibujo visible no cambia.
    torso = layers["torso"]
    for row in range(th):
        body_x = np.flatnonzero(kind[row] == "torso")
        if len(body_x) == 0:
            continue
        left = np.flatnonzero((kind[row] == "brazo_derecho") & (sx[row] >= 425))
        right = np.flatnonzero((kind[row] == "brazo_izquierdo") & (sx[row] <= 640))
        if len(left):
            torso[row, left, :3] = native_rgb[row, body_x[0]]
            torso[row, left, 3] = 255
        if len(right):
            torso[row, right, :3] = native_rgb[row, body_x[-1]]
            torso[row, right, 3] = 255

    for name in LAYER_ORDER:
        Image.fromarray(layers[name], "RGBA").save(OUT / f"{name}.png")

    contact = Image.new("RGB", (tw * 5 * 4, th * 4), (176, 162, 181))
    for i, name in enumerate(LAYER_ORDER):
        tile = Image.fromarray(layers[name], "RGBA").resize((tw * 4, th * 4), Image.Resampling.NEAREST)
        contact.paste(tile, (i * tw * 4, 0), tile)
    contact.save(OUT / "capas-4x.png")

    composed = np.zeros((th, tw, 4), dtype=np.uint8)
    composed[native_mask, :3] = native_rgb[native_mask]
    composed[native_mask, 3] = 255
    Image.fromarray(composed, "RGBA").save(OUT / "pepo.png")
    merged = Image.new("RGBA", SIZE)
    for name in LAYER_ORDER:
        merged.alpha_composite(Image.fromarray(layers[name], "RGBA"))
    assert np.array_equal(np.array(merged), composed), "Las capas no reproducen el sprite visible"
    preview = Image.fromarray(composed, "RGBA").resize((tw * 6, th * 6), Image.Resampling.NEAREST)
    preview.save(OUT / "pepo-6x.png")
    room = Image.open(ROOT / "arte/escenarios/taberna-v02/fondo.png").convert("RGBA")
    room.alpha_composite(Image.fromarray(composed, "RGBA"), (296, 155))
    room.convert("RGB").save(OUT / "escena-1x.png")

    metadata = {
        "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "source_box": BOX,
        "size": SIZE,
        "method": "median foreground color per cell; 42 RGB clusters; anatomical region masks; hidden cloth under arms",
        "layers_bottom_to_top": LAYER_ORDER,
        "opaque_pixels": int(native_mask.sum()),
        "palette_colors": len({tuple(v) for v in native_rgb[native_mask]}),
        "note": "Experimental conversion of generated concept, not proof of native AI generation.",
    }
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False))


if __name__ == "__main__":
    main()
