"""Inspección de originales y comparación tras abrirlos con Aseprite. No dibuja."""
import json
import struct
import subprocess
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ASEPRITE = ROOT / 'aseprite/build/bin/aseprite.exe'
CHECK = ROOT / 'mantenimiento/pxl-pago-v01-verificacion'
CHECK.mkdir(parents=True, exist_ok=True)
results = {}

for name in ('reposo', 'subir', 'sostener', 'bajar', 'pago'):
    original = HERE / 'out/anims' / f'{name}.aseprite'
    data = original.read_bytes()
    _, magic, count, width, height, depth = struct.unpack_from('<I5H', data)
    assert magic == 0xA5E0 and (width, height, depth) == (96, 112, 32)
    layers, offset = [], 128
    for index in range(count):
        size, frame_magic, chunks, duration = struct.unpack_from('<I3H', data, offset)
        assert frame_magic == 0xF1FA
        cursor = offset + 16
        for _ in range(chunks):
            chunk_size, kind = struct.unpack_from('<IH', data, cursor)
            if kind == 0x2004:
                n = struct.unpack_from('<H', data, cursor + 22)[0]
                layers.append(data[cursor + 24:cursor + 24 + n].decode('utf-8'))
            cursor += chunk_size
        offset += size
    assert {'piernas', 'cabeza', 'brazo_pago', 'tarjeta', 'agarre'} <= set(layers), layers
    exported = CHECK / f'{name}.png'
    subprocess.run([str(ASEPRITE), '--batch', str(original), '--sheet', str(exported)], check=True, capture_output=True)
    expected = Image.open(HERE / 'out/anims' / f'{name}.png').convert('RGBA')
    actual = Image.open(exported).convert('RGBA')
    assert actual.size == expected.size and actual.tobytes() == expected.tobytes(), name
    assert set(expected.getchannel('A').tobytes()) <= {0, 255}, name
    # Los pies permanecen apoyados, incluso durante la inclinación del torso.
    foot = expected.crop((0, 98, 96, 112)).tobytes()
    for index in range(count):
        assert expected.crop((index*96, 98, (index+1)*96, 112)).tobytes() == foot
    results[name] = {'frames': count, 'size': [width, height], 'layers': layers,
                     'aseprite_roundtrip_identical': True, 'opaque_or_clear': True,
                     'feet_stable': True}

image = Image.open(HERE / 'out/scenes/contexto.png').convert('RGBA')
results['contexto'] = {'size': list(image.size), 'colors': len(image.getcolors(1_000_000))}
results['scope'] = 'Comprobación técnica; no certifica estética ni calidad de animación.'
(HERE / 'verificacion.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(results, ensure_ascii=False, indent=2))
