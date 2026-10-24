param([string]$PxlRoot, [switch]$Verificar)
$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
if (-not $PxlRoot) { $PxlRoot = Join-Path $projectRoot 'deps/claude-pxl' }
$cli = Join-Path $PxlRoot 'bin/pxl.js'
if (-not (Test-Path -LiteralPath $cli)) { throw 'Falta claude-pxl. Consulta README.md.' }
& node $cli check (Join-Path $PSScriptRoot 'pago.px.js')
if ($LASTEXITCODE -ne 0) { throw 'pxl check ha fallado.' }
& node $cli build (Join-Path $PSScriptRoot 'pago.px.js') --only pago,reposo,subir,sostener,bajar,personaje,contexto,fondo,sombras,silla,mesa,croquetas,aceitunas --aseprite --share 4
if ($LASTEXITCODE -ne 0) { throw 'pxl build ha fallado.' }
if ($Verificar) {
  & (Join-Path $projectRoot 'aseprite-mcp/.venv/Scripts/python.exe') (Join-Path $PSScriptRoot 'verificar.py')
  if ($LASTEXITCODE -ne 0) { throw 'La verificación de exportación ha fallado.' }
}
