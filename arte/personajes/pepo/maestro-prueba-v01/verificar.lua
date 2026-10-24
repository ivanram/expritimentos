-- Ejecutar con `aseprite -b out/pepo.aseprite --script verificar.lua` desde la raíz.
local spr = assert(app.activeSprite, "No hay sprite abierto")
assert(spr.width == 48 and spr.height == 128, "Tamaño de lienzo incorrecto")
assert(#spr.frames == 1, "Se esperaba un fotograma")
local expected = {"piernas", "torso", "brazo_derecho", "brazo_izquierdo", "cabeza"}
assert(#spr.layers == #expected, "Se esperaban cinco capas")
for i, name in ipairs(expected) do
  assert(spr.layers[i].name == name, "Orden o nombre incorrecto en capa " .. i)
end
print("Aseprite: 48x128, un fotograma y cinco capas en el orden previsto")
