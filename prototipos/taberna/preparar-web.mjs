// Buildless static distribution. Run from any directory; no external packages.
import { cpSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const target = join(root, 'dist');
mkdirSync(target, { recursive: true });
for (const name of ['index.html', 'estilo.css', 'animacion.js', 'visor.js', 'assets']) {
  cpSync(join(root, name), join(target, name), { recursive: true });
}
console.log(target);
