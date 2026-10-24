"""Prepara ocho giros horizontales a partir del primer Pepo, sin editar su imagen."""
import json
from pathlib import Path
from shutil import copyfile

here = Path(__file__).resolve().parent
root = here.parents[2]
reference = root / 'arte/pruebas/comfy-pepo-v01/out/pepo-01-9-0.png'
comfy_input = root / 'deps/ComfyUI/input/pepo-comfy-orientaciones.png'
comfy_input.parent.mkdir(parents=True, exist_ok=True)
copyfile(reference, comfy_input)

source = json.loads((root / 'arte/pruebas/comfy-pepo-v01/workflow-api.json').read_text(encoding='utf-8'))
directions = {
    'frente': ('straight front view, facing the camera, face and chest fully visible', 0.34),
    'frente-derecha': ('three-quarter front view, body and gaze turned 45 degrees toward screen right, face still visible', 0.58),
    'derecha': ('strict right-facing side profile, body and face turned 90 degrees toward screen right, one eye and one ear visible', 0.70),
    'espalda-derecha': ('three-quarter back view, body turned 135 degrees toward screen right, back of shirt dominant, only a sliver of face', 0.78),
    'espalda': ('strict rear view, body turned 180 degrees, facing directly away from camera, back of head and both shoulders visible, no face visible', 0.82),
    'espalda-izquierda': ('three-quarter back view, body turned 135 degrees toward screen left, back of shirt dominant, only a sliver of face', 0.78),
    'izquierda': ('strict left-facing side profile, body and face turned 90 degrees toward screen left, one eye and one ear visible', 0.70),
    'frente-izquierda': ('three-quarter front view, body and gaze turned 45 degrees toward screen left, face still visible', 0.58),
}
identity = ('same original friendly adult man in the supplied image, same tousled black hair and full dark beard, '
            'same blue-gray open short-sleeve overshirt over a rust red t-shirt, same brown straight trousers, '
            'same cream sneakers, same adult proportions and slightly oversized head, same selective dark outlines '
            'and warm chunky pixel-like texture, full body standing, relaxed arms, upright balanced pose, '
            'entire head and both shoes visible, isolated on same plain muted lavender background, no props, no text')
negative = ('extra person, duplicate, two heads, extra limbs, missing arms, asymmetric legs, tilted shoulders, '
            'crooked back, floating head, disconnected hair, mirrored face, altered clothing, blue jeans, '
            'long sleeves, formal suit, bare arms, hat, 3d render, realistic photo, scenery, text, watermark')

out = here / 'workflows'
out.mkdir(exist_ok=True)
for index, (name, (angle, denoise)) in enumerate(directions.items()):
    graph = json.loads(json.dumps(source))
    graph['3']['inputs']['text'] = f'pixel art style character turnaround, {angle}. {identity}.'
    graph['4']['inputs']['text'] = negative
    graph['6']['inputs'].update({'latent_image': ['11', 0], 'seed': 24102026, 'denoise': denoise})
    graph['9']['inputs']['filename_prefix'] = f'pepo-experimento/orientaciones/{index:02d}-{name}'
    graph['10'] = {'class_type': 'LoadImage', 'inputs': {'image': comfy_input.name}}
    graph['11'] = {'class_type': 'VAEEncode', 'inputs': {'pixels': ['10', 0], 'vae': ['7', 0]}}
    del graph['5']
    (out / f'{index:02d}-{name}.json').write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Referencia local copiada a {comfy_input}; workflows: {out}')
