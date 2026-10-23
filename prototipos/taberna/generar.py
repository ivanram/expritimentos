"""Arte original procedural + montaje y exportacion reales por Aseprite MCP.

Ejecutar con el Python de aseprite-mcp/.venv. No requiere servicios de pago.
"""
from pathlib import Path
import asyncio, json, math, os, random, time
from PIL import Image, ImageDraw
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
WORK=HERE/'.work'; ART=HERE/'art'; ASSETS=HERE/'assets'
for p in (WORK,ART,ASSETS): p.mkdir(exist_ok=True)
O='#282633'; CREAM='#f4dcaa'; W,H=112,240
PEOPLE=[
 dict(id='lola',name='Lola',color='#d77c60',dark='#8d4850',light='#f3aa79',skin='#e6ac7b',shade='#b87962',shine='#ffcf95',hair='#493340',hairhi='#77505a',kind='curly',side=1,pants='#465469',pantslight='#738391'),
 dict(id='paco',name='Paco',color='#b69b52',dark='#756c42',light='#dfbd6b',skin='#c98b61',shade='#975b51',shine='#edb77c',hair='#3c3338',hairhi='#6a4a45',kind='beard',side=-1,pants='#334e54',pantslight='#587475'),
 dict(id='nora',name='Nora',color='#4d8f87',dark='#355b65',light='#7eb4a0',skin='#efc294',shade='#bc8c77',shine='#ffe0ac',hair='#33313c',hairhi='#5d4654',kind='bob',side=1,pants='#665662',pantslight='#94808a'),
 dict(id='dani',name='Dani',color='#586e89',dark='#3e465f',light='#819baa',skin='#ddb190',shade='#a87972',shine='#f5d0a3',hair='#5a515a',hairhi='#aaa0a1',kind='silver',side=-1,pants='#83705e',pantslight='#ac9475'),
 dict(id='rosa',name='Rosa',color='#9b6d92',dark='#61475e',light='#c89aaf',skin='#bd835f',shade='#8b5850',shine='#e4a471',hair='#824845',hairhi='#b57554',kind='bun',side=1,pants='#464d66',pantslight='#73768a'),
]
GLYPHS={
'A':['01110','10001','10001','11111','10001','10001','10001'],'B':['11110','10001','10001','11110','10001','10001','11110'],
'C':['01111','10000','10000','10000','10000','10000','01111'],'D':['11110','10001','10001','10001','10001','10001','11110'],
'E':['11111','10000','10000','11110','10000','10000','11111'],'F':['11111','10000','10000','11110','10000','10000','10000'],
'G':['01111','10000','10000','10111','10001','10001','01111'],'H':['10001','10001','10001','11111','10001','10001','10001'],
'I':['111','010','010','010','010','010','111'],'J':['00111','00010','00010','00010','10010','10010','01100'],
'L':['10000','10000','10000','10000','10000','10000','11111'],'M':['10001','11011','10101','10101','10001','10001','10001'],
'N':['10001','11001','10101','10011','10001','10001','10001'],'O':['01110','10001','10001','10001','10001','10001','01110'],
'P':['11110','10001','10001','11110','10000','10000','10000'],'R':['11110','10001','10001','11110','10100','10010','10001'],
'S':['01111','10000','10000','01110','00001','00001','11110'],'T':['11111','00100','00100','00100','00100','00100','00100'],
'U':['10001','10001','10001','10001','10001','10001','01110'],'V':['10001','10001','10001','10001','10001','01010','00100'],
'Y':['10001','10001','01010','00100','00100','00100','00100'],' ':['000']*7,
'1':['010','110','010','010','010','010','111'],'2':['1110','0001','0001','0110','1000','1000','1111'],
'3':['1110','0001','0001','0110','0001','0001','1110'],'4':['1001','1001','1001','1111','0001','0001','0001'],
'5':['1111','1000','1000','1110','0001','0001','1110'],'.':['0','0','0','0','0','1','1'],
}
def text(d,s,x,y,color,scale=1):
    for ch in s:
        g=GLYPHS.get(ch,GLYPHS[' '])
        for yy,row in enumerate(g):
            for xx,v in enumerate(row):
                if v=='1': d.rectangle((x+xx*scale,y+yy*scale,x+(xx+1)*scale-1,y+(yy+1)*scale-1),fill=color)
        x+=(len(g[0])+1)*scale
def poly(d,pts,c,outline=O,width=1):
    pts=[(round(x),round(y)) for x,y in pts]
    d.polygon(pts,fill=c)
    if outline: d.line(pts+[pts[0]],fill=outline,width=width)
def ell(d,box,c,outline=None,width=1):
    d.ellipse(tuple(round(x) for x in box),fill=c,outline=outline,width=width)
def limb(d,a,b,c,width=12,edge=O):
    a=tuple(round(v) for v in a);b=tuple(round(v) for v in b)
    d.line((a,b),fill=edge,width=width+3)
    r=(width+3)//2
    for x,y in (a,b): ell(d,(x-r,y-r,x+r,y+r),edge)
    d.line((a,b),fill=c,width=width)
    r=width//2
    for x,y in (a,b): ell(d,(x-r,y-r,x+r,y+r),c)

def backgrounds():
    im=Image.new('RGBA',(640,360),'#d4a375');d=ImageDraw.Draw(im)
    # Plaster: large flat shapes, restrained surface marks.
    for y in range(230):
        t=y/230; col=tuple(int(a*(1-t)+b*t) for a,b in zip((213,163,113),(182,113,87)))
        d.line((0,y,639,y),fill=col)
    d.polygon([(0,0),(640,0),(640,41),(0,16)],fill='#80514d')
    for x in (0,206,437,620):
        poly(d,[(x,0),(x+17,0),(x-14,48),(x-31,48)],'#684446')
        d.line((x+3,1,x-20,43),fill='#ab7660',width=3)
    rng=random.Random(19)
    for _ in range(380):
        x,y=rng.randrange(640),rng.randrange(40,226)
        d.line((x,y,x+rng.randrange(1,4),y),fill=rng.choice(['#c58b68','#cd956e','#b98064']))
    # Arched twilight window.
    d.rounded_rectangle((19,36,149,195),radius=55,fill='#704b48',outline='#482f38',width=4)
    d.rounded_rectangle((28,45,140,187),radius=46,fill='#8d7897')
    d.rectangle((29,93,139,187),fill='#8d7897')
    d.rectangle((30,118,138,187),fill='#a48d9d')
    ell(d,(96,62,115,81),'#f9dc9a')
    for x,top,w in [(29,130,23),(46,108,20),(63,135,22),(85,118,25),(109,142,31)]:
        poly(d,[(x,top),(x+w//2,top-8),(x+w,top),(x+w,188),(x,188)],'#574d68',None)
        for yy in range(top+11,184,12):
            for xx in range(x+5,min(x+w-2,139),9):d.rectangle((xx,yy,xx+2,yy+4),fill='#d6b38b')
    d.rectangle((79,48,85,188),fill='#674646');d.rectangle((31,120,137,125),fill='#674646')
    d.rectangle((14,186,154,195),fill='#543b40');d.rectangle((14,186,154,189),fill='#cc9168')
    # Left shelf and a few bottles, all above the moving hands.
    d.rectangle((178,77,273,83),fill='#4f3b3e');d.rectangle((181,76,275,78),fill='#d19b69')
    for x,h,c in [(190,23,'#536b58'),(208,33,'#3d6660'),(232,26,'#7b6747'),(250,20,'#61715c')]:
        poly(d,[(x,76),(x,76-h+8),(x+3,76-h+6),(x+3,76-h),(x+7,76-h),(x+7,76-h+6),(x+10,76-h+8),(x+10,76)],c)
        d.line((x+3,75-h+10,x+3,70),fill='#a2b18b',width=2)
    # Sign, no game HUD baked into the image.
    d.rectangle((285,34,470,73),fill='#644644',outline='#3c3037',width=3)
    d.rectangle((290,39,465,68),fill='#36565b')
    text(d,'LA ULTIMA RONDA',303,47,'#eed7a6',2)
    # Pendant lamps. Warm blocks rather than translucent overlays.
    for cx in (168,490):
        d.line((cx,10,cx,76),fill='#43363c',width=2)
        poly(d,[(cx-16,77),(cx,66),(cx+16,77)],'#573b3d')
        d.rectangle((cx-7,78,cx+7,95),fill='#e4ad65',outline='#624143',width=2)
        d.rectangle((cx-3,79,cx+2,91),fill='#ffe0a0')
        d.rectangle((cx-9,95,cx+9,98),fill='#563b3d')
    # Chalk board and a still-life poster.
    d.rectangle((314,91,414,146),fill='#614747',outline='#44343c',width=2)
    d.rectangle((319,96,409,141),fill='#384b4d')
    text(d,'HOY',348,102,'#e5cb91');text(d,'TAPAS',333,116,'#b5c2a4');text(d,'OLIVAS',331,129,'#a9bba2')
    d.rectangle((461,119,532,197),fill='#573d40',outline='#402e37',width=3)
    d.rectangle((467,125,526,191),fill='#ded0a2')
    ell(d,(477,140,503,166),'#cf8258');ell(d,(496,152,518,176),'#b86550')
    poly(d,[(489,143),(486,134),(502,137)],'#607454',None)
    text(d,'BAR',486,177,'#796151')
    # Door to be used by the waiter later; no waiter created.
    d.rectangle((553,46,632,254),fill='#503b40',outline='#392f3a',width=3)
    d.rectangle((562,55,623,253),fill='#3d3e4b')
    d.rectangle((569,62,616,184),fill='#40535a',outline='#765d51',width=2)
    d.line((568,123,618,123),fill='#715a50',width=3)
    d.rectangle((570,198,615,244),fill='#574848',outline='#776254',width=2)
    ell(d,(612,186,616,190),'#d0ad6b')
    # Dado tiles and skirting.
    d.rectangle((0,211,639,302),fill='#35505a')
    for y in range(216,302,24):
        for x in range(-12,640,24):
            d.rectangle((x+1,y+1,x+22,y+22),fill=('#3e6268' if (x//24+y//24)%2 else '#3c5b63'),outline='#2b444f')
            if y==216:
                d.polygon([(x+6,y+12),(x+12,y+6),(x+18,y+12),(x+12,y+18)],fill='#a5ac8d')
    d.rectangle((0,209,639,214),fill='#c3ae83');d.rectangle((0,298,639,305),fill='#253d49')
    d.rectangle((0,306,639,359),fill='#756167')
    for y in (319,339,359):d.line((0,y,639,y),fill='#574c58',width=2)
    for row,y in enumerate((306,320,340)):
        for x in range(-70+(row%2)*55,640,110):d.line((x,y,x-10,y+18),fill='#574c58',width=2)
    # Fixed chairs behind the actors.
    for cx in (72,196,320,444,568):
        d.rounded_rectangle((cx-24,210,cx+24,288),radius=7,fill='#654b46',outline='#302e39',width=2)
        d.rectangle((cx-17,218,cx+17,252),fill='#9c7455',outline='#bd9063',width=2)
        for x in (cx-16,cx+12):d.rectangle((x,279,x+4,328),fill='#5c4646',outline='#302e39')
    im.save(WORK/'background.png')
    table=Image.new('RGBA',(640,360));d=ImageDraw.Draw(table)
    # Legs show below the tabletop, no solid full-width mask below the rim.
    for x in (42,585):
        poly(d,[(x,263),(x+12,263),(x+19,341),(x+4,341)],'#624a44')
        d.line((x+5,275,x+10,333),fill='#aa7b55',width=3)
    d.rectangle((45,310,600,316),fill='#5e4845',outline='#2b2b36')
    poly(d,[(25,240),(613,240),(626,256),(13,256)],'#bd8c62')
    for y,c in [(242,'#dfb680'),(246,'#c99c6e'),(251,'#b47e59')]:d.line((25,y,614,y),fill=c,width=2)
    d.rectangle((14,256,625,264),fill='#e0b479',outline='#3a3037',width=2)
    d.rectangle((21,265,619,276),fill='#755047',outline='#372e37',width=2)
    d.line((29,268,611,268),fill='#a17050',width=2)
    for x in range(37,612,88):d.line((x,271,x+50,271),fill='#5a4140')
    table.save(WORK/'table.png')
    props=Image.new('RGBA',(640,360));d=ImageDraw.Draw(props)
    for i,cx in enumerate((72,196,320,444,568)):
        ell(d,(cx-17,239,cx+17,248),'#82644f')
        ell(d,(cx-17,236,cx+16,245),'#e5d7ac',O)
        ell(d,(cx-12,238,cx+12,243),'#aaa780')
        for j in range(3):
            x=cx-9+j*7
            ell(d,(x,237+(j%2),x+6,241+(j%2)),['#a5a45d','#d38e55','#b4a75c'][i%3])
            d.point((x+2,238),fill='#e3c381')
        gx=cx-39
        d.rectangle((gx,223,gx+9,243),fill='#ddd3a5',outline='#3d3b40')
        d.rectangle((gx+2,229,gx+7,240),fill='#d4a350')
        d.line((gx+2,225,gx+7,225),fill='#fff1c8',width=2)
    props.save(WORK/'table_props.png')

def head(d,p,cx,top,talk=0,blink=False):
    skin,sh,hi=p['skin'],p['shade'],p['shine'];hair=p['hair'];hh=p['hairhi'];kind=p['kind']
    # Hair silhouette differs before the face is added.
    if kind=='curly':
        for dx,dy,r in [(-17,8,8),(-16,23,8),(16,9,8),(16,24,7),(-10,0,9),(3,-3,10),(13,0,8)]:
            ell(d,(cx+dx-r,top+dy-r,cx+dx+r,top+dy+r),hair,O)
            ell(d,(cx+dx-r+2,top+dy-r+2,cx+dx+2,top+dy+1),hh)
    elif kind=='bun':
        ell(d,(cx+7,top-16,cx+28,top+5),hair,O)
        d.arc((cx+10,top-13,cx+24,top+2),190,340,fill=hh,width=2)
        ell(d,(cx-20,top-7,cx+22,top+32),hair,O)
    elif kind=='bob':
        d.rounded_rectangle((cx-23,top-8,cx+23,top+43),radius=13,fill=hair,outline=O,width=2)
        d.line((cx-20,top+6,cx-20,top+34),fill=hh,width=2)
    else:
        ell(d,(cx-21,top-7,cx+20,top+31),hair,O)
    ell(d,(cx-22,top+14,cx-14,top+27),sh,O)
    ell(d,(cx+14,top+14,cx+22,top+27),sh,O)
    poly(d,[(cx-16,top+4),(cx-7,top-1),(cx+12,top+1),(cx+18,top+11),(cx+16,top+31),(cx+8,top+40),(cx-6,top+39),(cx-16,top+28)],skin)
    poly(d,[(cx+12,top+5),(cx+17,top+12),(cx+14,top+30),(cx+6,top+37),(cx-1,top+37),(cx+9,top+30)],sh,None)
    d.line((cx-10,top+8,cx-12,top+21),fill=hi,width=3)
    # Character-specific fringe and facial hair.
    if kind=='curly':
        for dx in (-12,-3,7,14):ell(d,(cx+dx-5,top-4,cx+dx+5,top+6),hair)
    elif kind=='bob':
        poly(d,[(cx-20,top+15),(cx-17,top-4),(cx+13,top-5),(cx+20,top+10),(cx+2,top+6),(cx-6,top+4)],hair,None)
        d.line((cx-11,top-1,cx+7,top),fill=hh,width=2)
    elif kind=='bun':
        poly(d,[(cx-18,top+14),(cx-17,top+1),(cx-4,top-6),(cx+14,top+1),(cx+17,top+9),(cx+5,top+3),(cx-8,top+6)],hair,None)
        d.line((cx-10,top+2,cx+1,top-1),fill=hh,width=2)
    else:
        poly(d,[(cx-18,top+15),(cx-19,top-1),(cx-6,top-8),(cx+12,top-6),(cx+18,top+6),(cx+4,top+2),(cx-6,top+6)],hair,None)
        for xx in range(-13,12,6):d.line((cx+xx,top-2,cx+xx+4,top-4),fill=hh,width=2)
        if kind=='beard':
            poly(d,[(cx-15,top+25),(cx-8,top+29),(cx+9,top+28),(cx+15,top+23),(cx+13,top+34),(cx+5,top+41),(cx-6,top+39)],hair,None)
            d.line((cx-7,top+36,cx+6,top+37),fill=hh,width=2)
        if kind=='silver':
            d.line((cx-13,top+29,cx-7,top+33),fill=hh,width=2)
            d.line((cx+8,top+30,cx+13,top+28),fill=hh,width=2)
    # Brows, eyes, nose and mouth are deliberately placed pixels.
    brow=p['hair']
    d.line((cx-12,top+14,cx-5,top+14),fill=brow,width=2)
    d.line((cx+4,top+14,cx+11,top+14+(kind=='beard')),fill=brow,width=2)
    for ex in (cx-8,cx+8):
        if blink:d.line((ex-2,top+20,ex+2,top+20),fill=O,width=1)
        else:
            d.rectangle((ex-2,top+18,ex+2,top+21),fill='#f7e3bc')
            d.rectangle((ex,top+18,ex+1,top+21),fill=O)
    poly(d,[(cx+1,top+20),(cx,top+26),(cx+5,top+26)],sh,None)
    d.point((cx+1,top+23),fill=hi)
    if kind=='bob':
        for ex in (cx-8,cx+8):d.rounded_rectangle((ex-6,top+15,ex+6,top+25),radius=3,outline='#c3a368',width=1)
        d.line((cx-2,top+19,cx+2,top+19),fill='#c3a368')
    if talk:
        d.rounded_rectangle((cx-5,top+30,cx+5,top+33+talk),radius=2,fill='#603e45')
        d.line((cx-3,top+31,cx+3,top+31),fill='#f3dcc0')
        if talk>2:d.line((cx-2,top+35,cx+3,top+35),fill='#c88279')
    else:d.line((cx-5,top+31,cx-2,top+34,cx+4,top+34,cx+7,top+31),fill='#70474c',width=1)
    if kind in ('curly','bun'):ell(d,(cx-22,top+27,cx-17,top+33),'#cbaa6c',O)

FRAMES=[('idle',i) for i in range(4)]+[('talk',i) for i in range(6)]+[('eat',i) for i in range(6)]+[('pay',i) for i in range(9)]+[('hold',i) for i in range(2)]
TAGS={'idle':(0,3),'talk':(4,9),'eat':(10,15),'pay_raise':(16,24),'pay_hold':(25,26),'pay_lower':(16,24)}
PASSES=['body','arm','grip_card','grip_wallet','grip_cash']

def character(p,index,action,phase):
    imgs={k:Image.new('RGBA',(W,H)) for k in PASSES}
    d=ImageDraw.Draw(imgs['body'])
    pay=(phase/8 if action=='pay' else 1 if action=='hold' else 0)
    bob=([0,1,1,0][phase%4] if action=='idle' else [0,0,-1,0,1,0][phase%6] if action=='talk' else 0)
    lean=round(p['side']*2*pay)
    cx=56+lean
    # Seated legs, separately shaped shoes, stable seat and floor anchors.
    for side in (-1,1):
        knee=56+side*(19+(index%2)*2)
        hip=56+side*11
        poly(d,[(hip-8,168),(hip+9,168),(knee+10,189),(knee+6,225),(knee-6,225),(knee-10,194)],p['pants'])
        d.line((hip-3,174,knee-3,194,knee-2,218),fill=p['pantslight'],width=3)
        poly(d,[(knee-7,223),(knee+7,223),(knee+12,230),(knee+12,234),(knee-10,234),(knee-10,229)],'#493a42')
        d.line((knee-8,233,knee+11,233),fill='#cfb99a',width=2)
    # Jacket torso and lap, curves are pixel contours rather than rectangles.
    poly(d,[(cx-21,106+bob),(cx-9,100+bob),(cx+9,100+bob),(cx+23,108+bob),(cx+27,159),(cx+21,174),(cx-22,174),(cx-27,159)],p['color'])
    poly(d,[(cx+14,107+bob),(cx+23,111+bob),(cx+25,159),(cx+18,171),(cx+10,171)],p['dark'],None)
    d.line((cx-20,117+bob,cx-22,151),fill=p['light'],width=3)
    poly(d,[(cx-7,103+bob),(cx+7,103+bob),(cx+10,162),(cx-9,162)],CREAM,None)
    if index==4:
        for yy in range(118,159,9):d.line((cx-8,yy,cx+8,yy),fill='#757b88',width=3)
    if index==2:
        poly(d,[(cx-10,102+bob),(cx+8,102+bob),(cx+3,115+bob),(cx-3,113+bob)],'#c37561')
        poly(d,[(cx+2,111),(cx+7,113),(cx+4,131),(cx-1,124)],'#d78e72',None)
    # Lapels, pocket and buttons.
    d.line((cx-10,107+bob,cx-6,123,cx-12,137),fill=p['dark'],width=2)
    d.line((cx+10,108+bob,cx+6,125,cx+13,139),fill=p['light'],width=2)
    d.rectangle((cx+14,134,cx+21,142),fill=p['dark'])
    d.line((cx+14,134,cx+21,134),fill=p['light'])
    for yy in (139,151):d.rectangle((cx-2,yy,cx-1,yy+1),fill='#8e795e')
    # Neck and head share the torso's small lean and bob.
    poly(d,[(cx-7,93+bob),(cx+7,93+bob),(cx+8,106+bob),(cx+1,112+bob),(cx-7,105+bob)],p['shade'])
    d.rectangle((cx-5,94+bob,cx+3,103+bob),fill=p['skin'])
    talk=([0,2,4,1,3,0][phase%6] if action=='talk' else 1 if action=='eat' and phase in (3,4) else 0)
    head(d,p,cx,55+bob,talk=talk,blink=(action=='idle' and phase==2) or (action=='hold' and phase==1))
    # Non-paying arm rests on the table, following body posture.
    s=-p['side']; shoulder=(cx+s*22,112+bob); elbow=(cx+s*30,143); palm=(cx+s*12,155)
    limb(d,shoulder,elbow,p['color'],12);limb(d,elbow,palm,p['skin'],10)
    d.line((elbow[0]-2,elbow[1]-2,palm[0]-2,palm[1]-2),fill=p['shine'],width=2)
    ell(d,(palm[0]-6,palm[1]-4,palm[0]+6,palm[1]+4),p['skin'],O)
    for x in range(round(palm[0]-2),round(palm[0]+4),2):d.point((x,round(palm[1]+2)),fill=p['shade'])
    # Paying arm: three key poses, eased trajectory; no rotation of pixel images.
    s=p['side']; shoulder=(cx+s*22,112+bob)
    if action=='eat':
        e=[0,.45,.85,1,.65,.1][phase]
        elbow=(cx+s*(31-4*e),143-21*e)
        wrist=(cx+s*(30-22*e),155-63*e)
    else:
        t=pay*pay*(3-2*pay)
        elbow=(cx+s*(31+9*t),143-60*t)
        wrist=(cx+s*(30+3*t),155-113*t)
    a=ImageDraw.Draw(imgs['arm'])
    limb(a,shoulder,elbow,p['color'],13)
    limb(a,elbow,wrist,p['skin'],10)
    a.line((round(elbow[0]-s*2),round(elbow[1]-2),round(wrist[0]-s*2),round(wrist[1]-1)),fill=p['shine'],width=2)
    ell(a,(wrist[0]-6,wrist[1]-4,wrist[0]+6,wrist[1]+6),p['skin'],O)
    ell(a,(wrist[0]-4,wrist[1]-3,wrist[0]+3,wrist[1]+3),p['shine'])
    if action=='eat':
        # Small bread/olive bite held at the fingers.
        ell(a,(wrist[0]-5,wrist[1]-6,wrist[0]+5,wrist[1]-1),'#cfa267',O)
        ell(a,(wrist[0]-2,wrist[1]-8,wrist[0]+3,wrist[1]-3),'#8e9b60',O)
    for typ in ('card','wallet','cash'):
        g=ImageDraw.Draw(imgs['grip_'+typ]); wx,wy=round(wrist[0]),round(wrist[1])
        for k in range(3 if typ=='wallet' else 2):
            g.rounded_rectangle((wx-4+k*3,wy-1,wx-2+k*3,wy+4),radius=1,fill=p['skin'],outline=p['shade'])
        g.line((wx-3,wy,wx+1,wy),fill=p['shine'])
    return imgs,dict(x=round(wrist[0]),y=round(wrist[1]),visible=action in ('pay','hold') and pay>.04)

def payment_props():
    im=Image.new('RGBA',(72,24));d=ImageDraw.Draw(im)
    d.rounded_rectangle((3,4,21,15),radius=2,fill='#659d9b',outline=O)
    d.line((5,6,18,6),fill='#a9d1bb');d.rectangle((6,9,9,12),fill='#e7c77c')
    d.line((14,12,18,12),fill='#305d70');d.point((18,9),fill='#e3dfbd')
    d.rounded_rectangle((27,3,46,17),radius=2,fill='#865346',outline=O)
    d.rectangle((28,5,44,7),fill='#bb8260');d.rectangle((40,8,46,13),fill='#a37153',outline=O)
    d.point((43,10),fill='#dbc48b');d.line((29,15,39,15),fill='#583c3b')
    poly(d,[(51,6),(66,2),(70,13),(54,17)],'#9aaf7e')
    poly(d,[(50,3),(67,4),(67,15),(50,14)],'#c8cf9a')
    d.rectangle((52,6,65,12),outline='#718b6f');ell(d,(57,6,61,12),'#92a580')
    im.save(WORK/'payment_props.png')

def prepare():
    backgrounds();payment_props()
    people=[]
    for ix,p in enumerate(PEOPLE):
        anchors=[]
        folder=WORK/p['id'];folder.mkdir(exist_ok=True)
        for fi,(action,phase) in enumerate(FRAMES):
            imgs,anchor=character(p,ix,action,phase)
            anchors.append(anchor)
            for layer,im in imgs.items():im.save(folder/f'{fi:02}_{layer}.png')
        people.append({**p,'anchors':anchors,'x':72+124*ix-56,'y':86})
    manifest={'width':640,'height':360,'cell':{'w':W,'h':H},'frames':len(FRAMES),'tags':TAGS,'people':people,'passes':PASSES,'madeWith':'Python / Pillow + Aseprite MCP','version':1}
    (ASSETS/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (ASSETS/'manifest.js').write_text('window.TABERNA = '+json.dumps(manifest,ensure_ascii=False)+';\n',encoding='utf-8')
    return manifest

async def call(session,name,args,log):
    t=time.perf_counter(); result=await session.call_tool(name,args)
    txt='\n'.join(c.text for c in result.content if c.type=='text')
    assert not result.isError and not any(s in txt.lower() for s in ('error:','failed to','not found')),txt
    log.append({'tool':name,'seconds':round(time.perf_counter()-t,3),'result':txt[:1200]})
    return txt

async def assemble(manifest):
    cfg=json.loads((ROOT/'.mcp.json').read_text())['mcpServers']['aseprite']
    params=StdioServerParameters(command=cfg['command'],args=cfg['args'],env={**os.environ,**cfg['env']})
    log=[]; start=time.perf_counter()
    async with stdio_client(params) as (r,w):
        async with ClientSession(r,w) as session:
            await session.initialize()
            await call(session,'animation_workflow_guide',{'use_case':'character'},log)
            await call(session,'animation_workflow_guide',{'use_case':'idle'},log)
            # Static originals are assembled by dedicated MCP tools.
            for name,png,width,height in [('taberna_fondo','background',640,360),('taberna_mesa','table',640,360),('objetos_mesa','table_props',640,360),('objetos_pago','payment_props',72,24)]:
                target=ART/(name+'.aseprite')
                await call(session,'create_canvas',{'width':width,'height':height,'filename':str(target)},log)
                await call(session,'import_image_as_layer',{'filename':str(target),'image_path':str(WORK/(png+'.png')),'layer_name':name},log)
                await call(session,'export_sprite',{'filename':str(target),'output_filename':str(ASSETS/(png+'.png'))},log)
            for p in PEOPLE:
                target=ART/(p['id']+'.aseprite');folder=(WORK/p['id']).as_posix()
                # The batch preserves named source layers, frame times and tags.
                layers='{'+','.join(json.dumps(x) for x in PASSES)+'}'
                taglua='\n'.join('do local t=s:newTag(%d,%d);t.name=%s;%s end' % (a+1,b+1,json.dumps(name),'t.aniDir=AniDir.REVERSE' if name=='pay_lower' else '') for name,(a,b) in TAGS.items())
                script=f'''
local s=Sprite({W},{H},ColorMode.RGB)
s:deleteLayer(s.layers[1])
local names={layers}
local ls={{}}
for _,name in ipairs(names) do local l=s:newLayer();l.name=name;ls[name]=l end
for fi=1,{len(FRAMES)} do
 if fi>1 then s:newEmptyFrame(fi) end
 local idleTimes={{1.2,0.3,0.1,0.4}}
 s.frames[fi].duration=(fi<=4 and idleTimes[fi] or fi<=10 and 0.13 or fi<=16 and 0.17 or fi<=25 and 0.07 or fi==26 and 3.8 or 0.12)
 for _,name in ipairs(names) do
  local image=Image{{fromFile=string.format({json.dumps(folder)}..'/%02d_%s.png',fi-1,name)}}
  s:newCel(ls[name],s.frames[fi],image,Point(0,0))
 end
end
{taglua}
for _,name in ipairs(names) do if string.sub(name,1,5)=='grip_' then ls[name].isVisible=false end end
s:saveAs({json.dumps(target.as_posix())})
for _,name in ipairs(names) do
 for _,other in ipairs(names) do ls[other].isVisible=(name==other) end
 local out={json.dumps(ASSETS.as_posix())}..'/{p['id']}_'..name..'.png'
 app.command.ExportSpriteSheet{{ui=false,askOverwrite=false,type=SpriteSheetType.HORIZONTAL,textureFilename=out,trim=false,trimSprite=false,listTags=true,dataFilename=string.gsub(out,'.png$','.json'),dataFormat=SpriteSheetDataFormat.JSON_ARRAY}}
end
for _,name in ipairs(names) do ls[name].isVisible=string.sub(name,1,5)~='grip_' end
s:saveAs(s.filename)
print('OK frames='..#s.frames)
'''
                await call(session,'run_lua_script',{'script':script},log)
                info=json.loads(await call(session,'get_sprite_info',{'filename':str(target)},log))
                assert info['frames']==len(FRAMES) and info['width']==W
                await call(session,'audit_animation',{'filename':str(target)},log)
                print(f"MCP: {p['name']} montado y exportado ({info['frames']} fotogramas)",flush=True)
            # Dedicated pixel drawing: stamp a tiny glint on each card master.
            await call(session,'draw_rows',{'filename':str(ART/'objetos_pago.aseprite'),'layer_name':'objetos_pago','frame_index':1,'x':15,'y':7,'rows':['.L.','LLL','.L.'],'legend':{'L':'#e2e9c6'}},log)
            await call(session,'export_sprite',{'filename':str(ART/'objetos_pago.aseprite'),'output_filename':str(ASSETS/'payment_props.png')},log)
            await call(session,'get_color_stats',{'filename':str(ART/'lola.aseprite'),'top':12},log)
    report={'method':'Original pixel art authored procedurally; imported, assembled, tagged, audited and exported through real stdio MCP calls. No generative image model was used.','mcp_seconds':round(time.perf_counter()-start,2),'calls':log}
    (HERE/'produccion-mcp.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'MCP terminado: {len(log)} llamadas, {report["mcp_seconds"]} s',flush=True)

def preview():
    m=json.loads((ASSETS/'manifest.json').read_text(encoding='utf-8'))
    image=Image.open(ASSETS/'background.png').convert('RGBA')
    frames=[5,12,24,25,24]
    def draw(p,layer,fi):
        with Image.open(ASSETS/f"{p['id']}_{layer}.png") as sheet:
            image.alpha_composite(sheet.crop((fi*W,0,(fi+1)*W,H)),(p['x'],p['y']))
    for p,fi in zip(m['people'],frames):draw(p,'body',fi)
    image.alpha_composite(Image.open(ASSETS/'table.png'))
    image.alpha_composite(Image.open(ASSETS/'table_props.png'))
    props=Image.open(ASSETS/'payment_props.png')
    for i,(p,fi) in enumerate(zip(m['people'],frames)):
        draw(p,'arm',fi)
        anchor=p['anchors'][fi]
        if anchor['visible']:
            idx=(i-2)%3;kind=['card','wallet','cash'][idx]
            image.alpha_composite(props.crop((idx*24,0,(idx+1)*24,24)),(p['x']+anchor['x']-12,p['y']+anchor['y']-11))
            draw(p,'grip_'+kind,fi)
    image.resize((1280,720),Image.Resampling.NEAREST).save(HERE/'preview.png')

if __name__=='__main__':
    data=prepare()
    asyncio.run(assemble(data))
    preview()
