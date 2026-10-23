"""Prepare the generated background in Aseprite via the local MCP server.

Python orchestrates MCP and reads exported pixels for verification; image
preparation itself runs in Aseprite. Requires root .mcp.json and mcp/Pillow.
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
    params = StdioServerParameters(command=cfg['command'], args=cfg['args'], env={**os.environ, **cfg['env']})
    calls = []

    async def call(session, name, args):
        start = time.perf_counter()
        result = await session.call_tool(name, args)
        output = '\n'.join(item.text for item in result.content if item.type == 'text')
        if result.isError or any(word in output.lower() for word in ['error:', 'script failed:', 'failed to']):
            raise RuntimeError(output)
        calls.append({'tool': name, 'seconds': round(time.perf_counter()-start, 3), 'result': output})
        return output

    src = json.dumps((HERE / 'fuentes/fondo-generado.png').as_posix())
    target = json.dumps((HERE / 'fondo.aseprite').as_posix())
    # No dedicated MCP tool combines nearest image scaling and palette creation.
    lua = f'''
local s = app.open({src})
assert(s, 'No source sprite')
app.command.SpriteSize{{ui=false,width=640,height=360}}
assert(s.width==640 and s.height==360, 'Unexpected dimensions')
s.layers[1].name = 'arquitectura'
-- Replace the generated wall's tonal grain with one coherent plaster color.
-- This mask preserves dark beams, bottles, window and the yellow lamp.
local architecture=s.layers[1]:cel(1).image
for y=0,97 do
 for x=100,465 do
  local v=architecture:getPixel(x,y)
  local r,g,b=app.pixelColor.rgbaR(v),app.pixelColor.rgbaG(v),app.pixelColor.rgbaB(v)
  if r>155 and g>80 and g<180 and r>g*1.22 and g>b*1.35 then
   architecture:putPixel(x,y,app.pixelColor.rgba(208,136,56,255))
  end
 end
end
local floor = s:newLayer()
floor.name = 'suelo_limpio'
local image = Image(640,160,ColorMode.RGB)
image:clear(app.pixelColor.rgba(177,85,51,255))
s:newCel(floor,1,image,Point(0,200))
app.command.ColorQuantization{{ui=false,maxColors=32,withAlpha=false}}
app.command.ChangePixelFormat{{ui=false,format='indexed',dithering='none'}}
-- Remove isolated quantization speckles; keep edges and intentional accents.
local pixels=s.layers[1]:cel(1).image
for pass=1,3 do
 local previous=Image(pixels)
 for y=1,198 do
  for x=1,638 do
   local counts={{}}
   for dy=-1,1 do for dx=-1,1 do
    local v=previous:getPixel(x+dx,y+dy)
    counts[v]=(counts[v] or 0)+1
   end end
   local current=previous:getPixel(x,y)
   if (counts[current] or 0)<=2 then
    for v,n in pairs(counts) do if n>=5 then pixels:putPixel(x,y,v);break end end
   end
  end
 end
end
s:saveAs({target})
print('OK size='..s.width..'x'..s.height..' palette='..#s.palettes[1]..' layers='..#s.layers)
'''
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            await call(session, 'run_lua_script', {'script': lua})
            await call(session, 'export_sprite', {'filename': str(HERE / 'fondo.aseprite'), 'output_filename': str(HERE / 'fondo.png')})
            info = json.loads(await call(session, 'get_sprite_info', {'filename': str(HERE / 'fondo.aseprite')}))
            assert info['width'] == 640 and info['height'] == 360 and info['frames'] == 1
            await call(session, 'get_palette', {'filename': str(HERE / 'fondo.aseprite')})

    with Image.open(HERE / 'fondo.png') as image:
        rgb = image.convert('RGB')
        colors = sorted(set(rgb.get_flattened_data()))
        assert image.size == (640,360) and len(colors) <= 32
        assert image.convert('RGBA').getextrema()[3] == (255,255)
    report = {'method': 'Image generation, then nearest resize, selective flat wall cleanup, clean flat floor layer, 32-color quantization without dithering, isolated-speckle cleanup, editable indexed original and PNG export through Aseprite MCP.', 'size': [640,360], 'opaque': True, 'unique_colors': len(colors), 'palette_used': ['#%02x%02x%02x' % c for c in colors], 'calls': calls}
    (HERE / 'produccion-mcp.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'size':report['size'],'colors':len(colors),'mcp_calls':len(calls)}))

if __name__ == '__main__':
    asyncio.run(main())
