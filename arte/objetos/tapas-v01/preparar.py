"""Scene-referenced tapas, assembled on the unchanged table scene via MCP."""
import asyncio
import json
import os
import time
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=ROOT/'arte/objetos/mesa-redonda-v02'
# Visible widths and upper-left positions read from the composition study.
# Crop bounds refer to the isolated generated sources, alpha >=16.
ITEMS=[
    {'id':'bravas','crop':[476,294,743,396],'width':68,'height':36,'x':286,'y':168},
    {'id':'croquetas','crop':[226,290,877,353],'width':82,'height':33,'x':200,'y':186},
    {'id':'calamares','crop':[59,167,1555,645],'width':84,'height':35,'x':356,'y':184},
    {'id':'aceitunas','crop':[364,229,933,546],'width':50,'height':29,'x':296,'y':200},
]

async def main():
    cfg=json.loads((ROOT/'.mcp.json').read_text(encoding='utf-8'))['mcpServers']['aseprite']
    params=StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})
    calls=[]
    async def call(session,name,args):
        start=time.perf_counter()
        result=await session.call_tool(name,args)
        output='\n'.join(c.text for c in result.content if c.type=='text')
        if result.isError or any(w in output.lower() for w in ['error:','script failed:','failed to']):
            raise RuntimeError(output)
        calls.append({'tool':name,'seconds':round(time.perf_counter()-start,3),'result':output})
        return output
    q=lambda p:json.dumps(p.as_posix())
    chunks=[]
    for p in ITEMS:
        n=p['id'];cx,cy,cw,ch=p['crop'];w,h=p['width'],p['height']
        chunks.append(f'''
do
 local src=app.open({q(HERE/'fuentes'/f'{n}.png')})
 local raw=src.layers[1]:cel(1).image
 for pixel in raw:pixels() do
  local v=pixel();local a=app.pixelColor.rgbaA(v)
  if a<16 then pixel(0)
  elseif a>=240 then pixel(app.pixelColor.rgba(app.pixelColor.rgbaR(v),app.pixelColor.rgbaG(v),app.pixelColor.rgbaB(v),255)) end
 end
 src:crop({cx},{cy},{cw},{ch})
 app.command.SpriteSize{{ui=false,width={w},height={h}}}
 local food=Image({w},{h},ColorMode.RGB)
 food:drawImage(src.layers[1]:cel(1).image,src.layers[1]:cel(1).position)
 local prop=Sprite({w+4},{h+8},ColorMode.RGB)
 prop.layers[1].name='sombra'
 local shadow=Image({w+4},{h+8},ColorMode.RGB)
 for y={h-2},{h+5} do for x=2,{w+1} do
  local d=((x-{w/2+2})/{w*.46})^2+((y-{h+1})/3.5)^2
  if d<1 then shadow:putPixel(x,y,app.pixelColor.rgba(49,22,18,d<0.4 and 74 or d<0.75 and 45 or 22)) end
 end end
 prop:newCel(prop.layers[1],1,shadow,Point(0,0))
 local layer=prop:newLayer();layer.name='{n}'
 prop:newCel(layer,1,food,Point(2,2))
 prop:saveAs({q(HERE/f'{n}.aseprite')})
 local full=Image({w+4},{h+8},ColorMode.RGB)
 full:drawImage(shadow,Point(0,0));full:drawImage(food,Point(2,2))
 images['{n}']=full
end
''')
    script="local images={}\n"+'\n'.join(chunks)+f'''
local reference=app.open({q(HERE/'fuentes/01-composicion.png')})
app.command.SpriteSize{{ui=false,width=640,height=360}}
reference:saveAs({q(HERE/'referencia.aseprite')})
local scene=app.open({q(BASE/'montaje.aseprite')})
assert(scene.width==640 and scene.height==360,'Unexpected base scene')
'''+ '\n'.join(f"do local l=scene:newLayer();l.name='{p['id']}';scene:newCel(l,1,images['{p['id']}'],Point({p['x']-2},{p['y']-2})) end" for p in ITEMS)+f'''
scene:saveAs({q(HERE/'montaje.aseprite')})
scene.layers[#scene.layers].isVisible=false
scene:saveAs({q(HERE/'sin-aceitunas.png')})
scene.layers[#scene.layers].isVisible=true
scene:saveAs({q(HERE/'montaje.aseprite')})
print('OK base preserved; four independent tapas layers; olive toggle proof exported')
'''
    async with stdio_client(params) as (reader,writer):
        async with ClientSession(reader,writer) as session:
            await session.initialize()
            await call(session,'run_lua_script',{'script':script})
            exports=[(p['id']+'.aseprite',p['id']+'.png',1) for p in ITEMS]+[('referencia.aseprite','referencia.png',1),('montaje.aseprite','montaje.png',1),('montaje.aseprite','montaje-2x.png',2)]
            for original,out,scale in exports:
                await call(session,'export_frame',{'filename':str(HERE/original),'frame_index':1,'output_filename':str(HERE/out),'scale':scale})
            info=json.loads(await call(session,'get_sprite_info',{'filename':str(HERE/'montaje.aseprite')}))
            assert info['frames']==1 and info['width']==640 and info['height']==360 and len(info['layers'])==8
    rectangles=[]
    for p in ITEMS:
        with Image.open(HERE/(p['id']+'.png')) as im:
            assert im.size==(p['width']+4,p['height']+8)
            a=im.convert('RGBA').getchannel('A');assert a.getextrema()==(0,255)
            assert all(a.getpixel(point)==0 for point in [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)])
        rectangles.append((p['x']-2,p['y']-2,p['x']+p['width']+2,p['y']+p['height']+6))
    with Image.open(BASE/'montaje.png') as before,Image.open(HERE/'montaje.png') as after,Image.open(HERE/'montaje-2x.png') as big,Image.open(HERE/'sin-aceitunas.png') as no_olives:
        a,b,c,d=[im.convert('RGBA') for im in [before,after,big,no_olives]]
        assert b.size==(640,360) and c.size==(1280,720) and b.getextrema()[3]==(255,255)
        changed=0;olive_changed=0;ox0,oy0,ox1,oy1=rectangles[-1]
        for y in range(360):
            for x in range(640):
                pixel=b.getpixel((x,y))
                if a.getpixel((x,y))!=pixel:
                    changed+=1;assert any(x0<=x<x1 and y0<=y<y1 for x0,y0,x1,y1 in rectangles)
                if d.getpixel((x,y))!=pixel:
                    olive_changed+=1;assert ox0<=x<ox1 and oy0<=y<oy1
                assert all(c.getpixel((x*2+dx,y*2+dy))==pixel for dx,dy in [(0,0),(1,0),(0,1),(1,1)])
        assert changed>0 and olive_changed>0
    manifest={'scene':[640,360],'base':'../mesa-redonda-v02/montaje.aseprite','alpha_cleanup':{'below_16':'transparent','at_least_240':'opaque'},'items':[{**p,'png':p['id']+'.png','position':[p['x']-2,p['y']-2]} for p in ITEMS],'alignment_note':'Generator changed framing of extractions; objects cropped and fitted to measured sizes/positions in the scene reference. Original base scene kept pixel-for-pixel outside overlay rectangles.'}
    (HERE/'tapas.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    report={'method':'Scene-first image generation, four separate transparent extractions; Aseprite MCP alpha cleanup, measured crop/resize, separate shadow+food originals and composition on the original unmodified table scene.','validation':{'rgba_assets':4,'scene_layers':8,'changed_pixels':changed,'only_food_rectangles_changed':True,'olive_toggle_changed_pixels':olive_changed,'olive_toggle_local_only':True,'preview_exact_nearest_2x':True},'calls':calls}
    (HERE/'produccion-mcp.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report['validation']))

if __name__=='__main__':
    asyncio.run(main())
