"""Comprueba los originales, etiquetas, atlas, anclajes y recursos del visor."""
import json, struct
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parent
assets=ROOT/'assets'
m=json.loads((assets/'manifest.json').read_text(encoding='utf-8'))
expected=set(m['tags'])
checked=[]
for p in m['people']:
    data=(ROOT/'art'/(p['id']+'.aseprite')).read_bytes()
    size,magic,frames=struct.unpack_from('<IHH',data)
    assert size==len(data) and magic==0xA5E0 and frames==27,p['id']
    assert len(p['anchors'])==27
    for anchor in p['anchors']:
        assert 12<=anchor['x']<=100 and 11<=anchor['y']<=220,anchor
    for layer in m['passes']:
        prefix=assets/(p['id']+'_'+layer)
        with Image.open(prefix.with_suffix('.png')) as image:
            assert image.size==(3024,240),image.size
            if layer in ('body','arm'):
                for i in range(27):
                    assert image.crop((112*i,0,112*(i+1),240)).getbbox(),(p['id'],layer,i)
        sheet=json.loads(prefix.with_suffix('.json').read_text(encoding='utf-8'))
        assert len(sheet['frames'])==27
        assert {t['name'] for t in sheet['meta']['frameTags']}==expected
        assert all(not x['trimmed'] and x['sourceSize']=={'w':112,'h':240} for x in sheet['frames'])
        checked.append(str(prefix.relative_to(ROOT)))
for name,dims in [('background',(640,360)),('table',(640,360)),('table_props',(640,360)),('payment_props',(72,24))]:
    with Image.open(assets/(name+'.png')) as image:assert image.size==dims
originals=list((ROOT/'art').glob('*.aseprite'))
assert len(originals)==9
report={'originales_aseprite':9,'personajes':5,'fotogramas_por_personaje':27,
        'hojas_verificadas':len(checked),'pases_por_personaje':5,
        'tipos_objeto':['tarjeta','cartera','billetes'],
        'bytes_assets':sum(x.stat().st_size for x in assets.iterdir() if x.is_file()),
        'resultado':'OK','alcance':'Estructura tecnica; calidad artistica pendiente de valoracion del equipo.'}
(ROOT/'validacion-recursos.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
