"""Descarga los modelos gratuitos de IP-Adapter al laboratorio local y verifica SHA-256."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

here = Path(__file__).resolve().parent
root = here.parents[2]
manifest = json.loads((here / 'modelos.json').read_text(encoding='utf-8'))

for model in manifest['models']:
    target = root / 'deps/ComfyUI/models' / model['folder'] / model['name']
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + '.part')

    def valid(path):
        if not path.exists() or path.stat().st_size != model['size']:
            return False
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
                digest.update(block)
        return digest.hexdigest() == model['sha256']

    if valid(target):
        print('Verificado:', target.name, flush=True)
        continue
    url = ('https://huggingface.co/h94/IP-Adapter/resolve/'
           + manifest['ipadapter_model_revision'] + '/' + model['file'])
    print('Descargando:', model['name'], flush=True)
    with urlopen(url, timeout=120) as response, temporary.open('wb') as output:
        while block := response.read(8 * 1024 * 1024):
            output.write(block)
    if not valid(temporary):
        raise RuntimeError(f'Archivo incompleto o SHA-256 incorrecto: {model["name"]}')
    temporary.replace(target)
    print('Descargado y verificado:', target.name, flush=True)
