"""Crea un mapa Canny de perfil para probar control estructural local."""
from pathlib import Path
import cv2
from PIL import Image

here = Path(__file__).resolve().parent
root = here.parents[2]
source = root / 'arte/pruebas/comfy-pepo-v02/out/02-derecha-texto-9-0.png'
target = here / 'out/side-guide-canny.png'
target.parent.mkdir(parents=True, exist_ok=True)
image = cv2.imread(str(source))
if image is None:
    raise FileNotFoundError(source)
edge = cv2.Canny(cv2.GaussianBlur(image, (5, 5), 1.5), 80, 160)
Image.fromarray(edge).convert('RGB').save(target)
print(target)
