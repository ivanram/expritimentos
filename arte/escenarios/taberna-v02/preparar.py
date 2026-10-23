"""Preserve the artwork's shading in RGB; use Aseprite MCP for size and export.

No palette reduction, floor repaint, wall mask or automatic smoothing.
"""
import asyncio
import json
import os
import time
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

async def main():
    cfg = json.loads((ROOT / '.mcp.json').read_text(encoding='utf-8'))['mcpServers']['aseprite']
    params = StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})
    calls = []
    async def call(session,name,args):
        start=time.perf_counter()
        result=await session.call_tool(name,args)
        output='\n'.join(c.text for c in result.content if c.type=='text')
        if result.isError or any(w in output.lower() for w in ['error:','script failed:','failed to']):
            raise RuntimeError(output)
        calls.append({'tool':name,'seconds':round(time.perf_counter()-start,3),'result':output})
        return output

    source=json.dumps((HERE/'fuentes/02-textura-controlada.png').as_posix())
    target=HERE/'fondo.aseprite'
    script=f'''
local s=app.open({source})
assert(s,'No source sprite')
app.command.ChangePixelFormat{{ui=false,format='rgb'}}
app.command.SpriteSize{{ui=false,width=640,height=360}}
s.layers[1].name='fondo_compuesto'
s:saveAs({json.dumps(target.as_posix())})
print('OK RGB '..s.width..'x'..s.height..' frames='..#s.frames)
'''
    async with stdio_client(params) as (reader,writer):
        async with ClientSession(reader,writer) as session:
            await session.initialize()
            await call(session,'run_lua_script',{'script':script})
            for scale,name in [(1,'fondo.png'),(2,'vista-2x.png')]:
                await call(session,'export_frame',{'filename':str(target),'frame_index':1,'output_filename':str(HERE/name),'scale':scale})
            info=json.loads(await call(session,'get_sprite_info',{'filename':str(target)}))
            assert info['width']==640 and info['height']==360 and info['frames']==1 and info['color_mode']=='rgb'
    with Image.open(HERE/'fondo.png') as im:
        assert im.size==(640,360)
        assert im.convert('RGBA').getextrema()[3]==(255,255)
        colors=len(set(im.convert('RGB').get_flattened_data()))
    with Image.open(HERE/'vista-2x.png') as enlarged, Image.open(HERE/'fondo.png') as native:
        assert enlarged.size==(1280,720)
        a,b=native.convert('RGB'),enlarged.convert('RGB')
        for y in range(360):
            for x in range(640):
                p=a.getpixel((x,y))
                assert all(b.getpixel((x*2+dx,y*2+dy))==p for dx,dy in [(0,0),(0,1),(1,0),(1,1)])
    report={'method':'Two image-generation passes: redesigned lighting/materials, then targeted reduction of microtexture. Aseprite MCP RGB nearest resize and native/2x exports. No palette quantization or flat repainting.', 'native':[640,360],'preview':[1280,720],'color_mode':'RGB','visible_colors':colors,'opaque':True,'preview_exact_nearest_2x':True,'png_bytes':(HERE/'fondo.png').stat().st_size,'calls':calls}
    (HERE/'produccion-mcp.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='calls'},ensure_ascii=False))

if __name__=='__main__':
    asyncio.run(main())
