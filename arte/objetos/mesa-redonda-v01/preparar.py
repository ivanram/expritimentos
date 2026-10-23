"""Prepare table RGBA and a layered placement study using Aseprite MCP."""
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
X,Y=128,100

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
    q=lambda path:json.dumps(path.as_posix())
    script=f'''
local s=app.open({q(HERE/'fuentes/mesa-generada.png')})
assert(s,'No source')
local raw=s.layers[1]:cel(1).image
for p in raw:pixels() do if app.pixelColor.rgbaA(p())<16 then p(0) end end
s:crop(40,55,1460,895)
app.command.SpriteSize{{ui=false,width=384,height=235}}
local cel=s.layers[1]:cel(1)
local full=Image(384,235,ColorMode.RGB)
full:drawImage(cel.image,cel.position)
s:deleteLayer(s.layers[1])
local images={{}}
for _,name in ipairs({{'pedestal','tablero'}}) do
 local layer=s:newLayer();layer.name=name
 local im=Image(384,235,ColorMode.RGB)
 for y=0,234 do for x=0,383 do
  if (name=='tablero' and y<=113) or (name=='pedestal' and y>113) then im:putPixel(x,y,full:getPixel(x,y)) end
 end end
 s:newCel(layer,1,im,Point(0,0))
 images[name]=im
end
s:saveAs({q(HERE/'mesa.aseprite')})
local scene=Sprite(640,360,ColorMode.RGB)
scene.layers[1].name='fondo'
scene:newCel(scene.layers[1],1,Image{{fromFile={q(ROOT/'arte/escenarios/taberna-v02/fondo.png')}}},Point(0,0))
local shadow=scene:newLayer();shadow.name='sombra_contacto'
local si=Image(640,360,ColorMode.RGB)
for y=314,340 do for x=215,425 do
 local d=((x-320)/105)^2+((y-327)/13)^2
 if d<1 then
  local a=d<0.35 and 64 or d<0.7 and 42 or 20
  si:putPixel(x,y,app.pixelColor.rgba(39,24,43,a))
 end
end end
scene:newCel(shadow,1,si,Point(0,0))
for _,name in ipairs({{'pedestal','tablero'}}) do
 local l=scene:newLayer();l.name=name
 scene:newCel(l,1,images[name],Point({X},{Y}))
end
scene:saveAs({q(HERE/'montaje.aseprite')})
print('OK table=384x235 scene=640x360 position={X},{Y} RGBA')
'''
    async with stdio_client(params) as (reader,writer):
        async with ClientSession(reader,writer) as session:
            await session.initialize()
            await call(session,'run_lua_script',{'script':script})
            for original,out,scale in [('mesa.aseprite','mesa.png',1),('montaje.aseprite','montaje.png',1),('montaje.aseprite','montaje-2x.png',2)]:
                await call(session,'export_frame',{'filename':str(HERE/original),'frame_index':1,'output_filename':str(HERE/out),'scale':scale})
            for name in ['mesa.aseprite','montaje.aseprite']:
                info=json.loads(await call(session,'get_sprite_info',{'filename':str(HERE/name)}))
                assert info['color_mode']=='rgb' and info['frames']==1
    with Image.open(HERE/'mesa.png') as table:
        assert table.size==(384,235)
        alpha=table.convert('RGBA').getchannel('A')
        assert alpha.getextrema()==(0,255)
        corners=[alpha.getpixel(p) for p in [(0,0),(383,0),(0,234),(383,234)]]
        assert corners==[0,0,0,0]
        bounds=alpha.getbbox()
    with Image.open(HERE/'montaje.png') as composed, Image.open(HERE/'montaje-2x.png') as big:
        assert composed.size==(640,360) and big.size==(1280,720)
        assert composed.convert('RGBA').getextrema()[3]==(255,255)
        a,b=composed.convert('RGB'),big.convert('RGB')
        for y in range(360):
            for x in range(640):
                assert all(b.getpixel((2*x+dx,2*y+dy))==a.getpixel((x,y)) for dx,dy in [(0,0),(0,1),(1,0),(1,1)])
    manifest={'asset':'mesa-redonda-v01','size':[384,235],'position':[X,Y],'scene':[640,360],'alpha':True,'bounds':bounds,'layers':['pedestal','tablero'],'split_row':113,'source_crop':[40,55,1460,895],'alpha_cleanup_below':16,'background':'../../escenarios/taberna-v02/fondo.png','notes':'Placement and layer split are provisional; food, chairs and actors are separate future assets.'}
    (HERE/'mesa.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (HERE/'produccion-mcp.json').write_text(json.dumps({'method':'Reference-driven image generation with transparency; Aseprite MCP alpha cleanup, crop, RGB nearest sizing, layer split and scene composition. No palette quantization.','validation':{'table_alpha':True,'transparent_corners':corners,'composite_opaque':True,'preview_exact_nearest_2x':True},'calls':calls},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False))

if __name__=='__main__':
    asyncio.run(main())
