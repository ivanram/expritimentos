"""Encola un workflow local y copia sus PNG sin transformarlos."""
import argparse
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode

parser = argparse.ArgumentParser()
parser.add_argument('--server', default='http://127.0.0.1:8188')
parser.add_argument('--workflow', default=str(Path(__file__).with_name('workflow-api.json')))
parser.add_argument('--name', default='pepo-01')
args = parser.parse_args()
here = Path(__file__).resolve().parent
workflow = json.loads(Path(args.workflow).read_text(encoding='utf-8'))
output = here / 'out'
output.mkdir(exist_ok=True)

def get_json(path):
    with urlopen(args.server + path, timeout=30) as response:
        return json.load(response)

started = time.perf_counter()
body = json.dumps({'prompt': workflow, 'client_id': 'spanish-simulator-local-test'}).encode()
with urlopen(Request(args.server + '/prompt', data=body, headers={'Content-Type': 'application/json'}), timeout=30) as response:
    submitted = json.load(response)
prompt_id = submitted['prompt_id']
print('Encolado:', prompt_id, flush=True)
(output / (args.name + '-request.json')).write_text(json.dumps({'prompt_id':prompt_id,'workflow':workflow}, indent=2, ensure_ascii=False), encoding='utf-8')
while time.perf_counter() - started < 3600:
    entry = get_json('/history/' + prompt_id).get(prompt_id)
    if entry:
        if entry.get('status', {}).get('status_str') == 'error':
            (output / (args.name + '-error.json')).write_text(json.dumps(entry, indent=2), encoding='utf-8')
            raise RuntimeError('ComfyUI ha devuelto un error; ver JSON de diagnóstico.')
        if entry.get('status', {}).get('completed'):
            break
    time.sleep(3)
else:
    raise TimeoutError('Tiempo límite de observación; comprobar la cola local antes de reintentar.')
elapsed = time.perf_counter() - started
images = []
for node, result in entry.get('outputs', {}).items():
    for index, item in enumerate(result.get('images', [])):
        query = urlencode({key: item.get(key, '') for key in ('filename', 'subfolder', 'type')})
        destination = output / f'{args.name}-{node}-{index}.png'
        with urlopen(args.server + '/view?' + query, timeout=60) as response:
            destination.write_bytes(response.read())
        images.append(destination.name)
assert images, 'No se obtuvo ninguna imagen.'
report = {'workflow':Path(args.workflow).name,'prompt_id':prompt_id,'elapsed_seconds':round(elapsed, 2),
          'images':images,'status':entry.get('status'), 'paid_api_calls':0,
          'note':'Tiempo desde encolado; puede incluir carga de modelos. PNG original sin retoques.'}
(output / (args.name + '-result.json')).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False), flush=True)
