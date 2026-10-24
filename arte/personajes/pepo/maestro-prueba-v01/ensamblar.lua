-- Ensambla en Aseprite las cinco capas visibles creadas por generar.py.
-- Ejecutar con el directorio raíz del repositorio como directorio actual.
local base = "arte/personajes/pepo/maestro-prueba-v01/out/"
local names = {"piernas", "torso", "brazo_derecho", "brazo_izquierdo", "cabeza"}
local spr = Sprite(48, 128, ColorMode.RGB)
for i, name in ipairs(names) do
  local layer = i == 1 and spr.layers[1] or spr:newLayer()
  layer.name = name
  local img = Image{fromFile=base .. name .. ".png"}
  assert(img.width == 48 and img.height == 128, "Dimension incorrecta: " .. name)
  spr:newCel(layer, 1, img, Point(0, 0))
end
assert(spr:saveAs(base .. "pepo.aseprite"), "No se pudo guardar el original")
print("Guardado " .. base .. "pepo.aseprite")
