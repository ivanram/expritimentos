"""Descarga los tres modelos públicos en el laboratorio local y comprueba SHA-256."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

here = Path(__file__).resolve().parent
root = here.parents[2]
catalog = json.loads((here / 'modelos.json').read_text(encoding='utf-8'))
for model in catalog['models']:
    target = root / 'deps' / 'ComfyUI' / 'models' / model['local_subfolder'] / model.get('local_filename', model['file'])
    target.parent.mkdir(parents=True, exist_ok=True)
    def valid(path):
        if not path.exists() or path.stat().st_size != model['size']:
            return False
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
                digest.update(chunk)
        return digest.hexdigest() == model['sha256']
    if valid(target):
        print('Verificado:', target.name, flush=True)
        continue
    url = f"https://huggingface.co/{model['repo']}/resolve/{model['revision']}/{model['file']}"
    temporary = target.with_suffix(target.suffix + '.part')
    with urlopen(url, timeout=120) as response, temporary.open('wb') as stream:
        while chunk := response.read(8 * 1024 * 1024):
            stream.write(chunk)
    if not valid(temporary):
        raise RuntimeError(f'Descarga incompleta o SHA-256 incorrecto: {target.name}')
    temporary.replace(target)
    print('Descargado y verificado:', target.name, flush=True)
