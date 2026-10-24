param([string]$PxlRoot)
$ErrorActionPreference='Stop'
if (-not $PxlRoot) { $PxlRoot=Join-Path $PSScriptRoot '../../../deps/claude-pxl' }
$cli=Join-Path $PxlRoot 'bin/pxl.js'
& node $cli check (Join-Path $PSScriptRoot 'estilo.px.js')
if ($LASTEXITCODE -ne 0) { throw 'Ha fallado pxl check' }
& node $cli build (Join-Path $PSScriptRoot 'estilo.px.js') --only amigos,poses,animacion,pago,nora_0,nora_1,nora_2,nora_3,nora_4,ines,teo,personajes --aseprite --share 4
if ($LASTEXITCODE -ne 0) { throw 'Ha fallado pxl build' }
