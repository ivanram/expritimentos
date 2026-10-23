"""Composition-first table. Keep the camera, alpha placement and scale locked."""
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
X,Y,W,H=164,186,312,156

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
    script=f'''
local master=app.open({q(HERE/'fuentes/01-composicion.png')})
app.command.SpriteSize{{ui=false,width=640,height=360}}
master.layers[1].name='referencia_compuesta'
master:saveAs({q(HERE/'referencia.aseprite')})
local bg=app.open({q(HERE/'fuentes/02-fondo.png')})
app.command.SpriteSize{{ui=false,width=640,height=360}}
bg.layers[1].name='fondo_camara_revisada'
bg:saveAs({q(HERE/'fondo-camara.aseprite')})
local bgi=Image(640,360,ColorMode.RGB)
bgi:drawImage(bg.layers[1]:cel(1).image,bg.layers[1]:cel(1).position)
local src=app.open({q(HERE/'fuentes/03-mesa-alineada.png')})
local raw=src.layers[1]:cel(1).image
for p in raw:pixels() do if app.pixelColor.rgbaA(p())<16 then p(0) end end
app.command.SpriteSize{{ui=false,width=640,height=360}}
local full=Image(640,360,ColorMode.RGB)
full:drawImage(src.layers[1]:cel(1).image,src.layers[1]:cel(1).position)
local table=Sprite({W},{H},ColorMode.RGB)
table:deleteLayer(table.layers[1])
local images={{}}
for _,name in ipairs({{'pedestal','tablero'}}) do
 local im=Image({W},{H},ColorMode.RGB)
 for y=0,{H-1} do for x=0,{W-1} do
  if (name=='tablero' and y+{Y}<=244) or (name=='pedestal' and y+{Y}>244) then
   im:putPixel(x,y,full:getPixel(x+{X},y+{Y}))
  end
 end end
 images[name]=im
 local l=table:newLayer();l.name=name
 table:newCel(l,1,im,Point(0,0))
end
table:saveAs({q(HERE/'mesa.aseprite')})
local scene=Sprite(640,360,ColorMode.RGB)
scene.layers[1].name='fondo_camara_revisada'
scene:newCel(scene.layers[1],1,bgi,Point(0,0))
local sh=scene:newLayer();sh.name='sombra_contacto'
local si=Image(640,360,ColorMode.RGB)
for y=310,340 do for x=237,395 do
 local d=((x-316)/79)^2+((y-325)/15)^2
 if d<1 then si:putPixel(x,y,app.pixelColor.rgba(40,21,34,d<0.4 and 60 or d<0.75 and 38 or 18)) end
end end
scene:newCel(sh,1,si,Point(0,0))
for _,name in ipairs({{'pedestal','tablero'}}) do
 local l=scene:newLayer();l.name=name
 scene:newCel(l,1,images[name],Point({X},{Y}))
end
scene:saveAs({q(HERE/'montaje.aseprite')})
print('OK scene=640x360 table={W}x{H} position={X},{Y}; no independent scale/translation')
'''
    async with stdio_client(params) as (reader,writer):
        async with ClientSession(reader,writer) as session:
            await session.initialize()
            await call(session,'run_lua_script',{'script':script})
            for original,out,scale in [('referencia.aseprite','referencia.png',1),('fondo-camara.aseprite','fondo-camara.png',1),('mesa.aseprite','mesa.png',1),('montaje.aseprite','montaje.png',1),('montaje.aseprite','montaje-2x.png',2)]:
                await call(session,'export_frame',{'filename':str(HERE/original),'frame_index':1,'output_filename':str(HERE/out),'scale':scale})
            for filename in ['mesa.aseprite','montaje.aseprite']:
                info=json.loads(await call(session,'get_sprite_info',{'filename':str(HERE/filename)}))
                assert info['color_mode']=='rgb' and info['frames']==1
    with Image.open(HERE/'mesa.png') as table:
        assert table.size==(W,H)
        a=table.convert('RGBA').getchannel('A')
        assert a.getextrema()==(0,255)
        assert all(a.getpixel(p)==0 for p in [(0,0),(W-1,0),(0,H-1),(W-1,H-1)])
        bounds=a.getbbox()
    with Image.open(HERE/'montaje.png') as native, Image.open(HERE/'montaje-2x.png') as preview:
        assert native.size==(640,360) and preview.size==(1280,720)
        assert native.convert('RGBA').getextrema()[3]==(255,255)
        n,p=native.convert('RGB'),preview.convert('RGB')
        assert all(p.getpixel((2*x+dx,2*y+dy))==n.getpixel((x,y)) for y in range(360) for x in range(640) for dx,dy in [(0,0),(1,0),(0,1),(1,1)])
    manifest={'size':[W,H],'position':[X,Y],'alpha_bounds':bounds,'background':'fondo-camara.png','scene':[640,360],'geometry_source':'fuentes/01-composicion.png','alignment':'Alpha extraction kept on original full frame; all sources resized together to 640x360 before fixed crop. No independent table scaling or translation.','split_scene_row':244}
    (HERE/'mesa.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (HERE/'produccion-mcp.json').write_text(json.dumps({'method':'Integrated scene camera study, then clean plate and aligned transparent extraction via image generation; Aseprite MCP fixed-coordinate separation, composition and RGB exports.','validation':{'alpha':True,'corners_transparent':True,'opaque_scene':True,'preview_exact_nearest_2x':True},'calls':calls},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(manifest,ensure_ascii=False))

if __name__=='__main__':
    asyncio.run(main())
