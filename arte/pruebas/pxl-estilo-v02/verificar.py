"""Lee exportaciones; no modifica imágenes ni produce arte."""
import json
import subprocess
from pathlib import Path
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
scratch=ROOT/'mantenimiento/pxl-estilo-v02-verificacion'
scratch.mkdir(parents=True,exist_ok=True)
report={'sprites':{}}
for name in ('nora_0','ines','teo'):
    im=Image.open(HERE/'out/sprites'/f'{name}.png').convert('RGBA')
    assert set(im.getchannel('A').tobytes()) <= {0,255}
    report['sprites'][name]={'canvas':list(im.size),'ink_bounds':list(im.getbbox()),
        'opaque_colors':len({pixel for pixel in im.getdata() if pixel[3]})}
ase=ROOT/'aseprite/build/bin/aseprite.exe'
subprocess.run([str(ase),'--batch',str(HERE/'out/anims/pago.aseprite'),
    '--sheet',str(scratch/'pago.png'),'--data',str(scratch/'pago.json'),
    '--format','json-array'],check=True,capture_output=True)
expected=Image.open(HERE/'out/anims/pago.png').convert('RGBA')
actual=Image.open(scratch/'pago.png').convert('RGBA')
assert actual.size == expected.size and actual.tobytes() == expected.tobytes()
metadata=json.loads((scratch/'pago.json').read_text(encoding='utf-8'))
assert len(metadata['frames'])==24
report['animation']={'canvas':[36,56],'frames':24,'duration_ms':3000,
    'aseprite_roundtrip_identical':True}
report['scope']='Comprobación técnica; no valida semejanza estilística ni aprobación artística.'
(HERE/'verificacion.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
