"""Build and check the public-only artifact used by Netlify."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import urlsplit

from build import DOMAIN, PAGES, ROOT, build
from check import check

PUBLIC = ROOT / 'dist'


def main():
    # Previews remain unindexable even after the production-domain launch.
    indexable = (os.environ.get('SITE_INDEXABLE', 'false').lower() == 'true'
                 and os.environ.get('CONTEXT', 'production') == 'production')
    origin = os.environ.get('DEPLOY_PRIME_URL') or os.environ.get('URL') or DOMAIN
    parsed = urlsplit(origin)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.path not in ('', '/'):
        raise ValueError('Deploy origin must be an absolute HTTP(S) origin')
    origin = origin.rstrip('/')
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    build(PUBLIC, indexable=indexable, asset_origin=origin)
    # Copy only public media and browser scripts, never research, source templates or Python.
    media = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4', '.woff', '.woff2'}
    for source in (ROOT / 'assets').rglob('*'):
        if source.is_file() and source.suffix.lower() in media:
            target = PUBLIC / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    (PUBLIC / 'scripts').mkdir()
    for name in ('navigation', 'reviews', 'shade-demo', 'gallery', 'contact'):
        shutil.copy2(ROOT / f'scripts/{name}.js', PUBLIC / f'scripts/{name}.js')
    shutil.copy2(ROOT / 'styles.css', PUBLIC / 'styles.css')
    check(PUBLIC, indexable=indexable, asset_origin=origin)
    subprocess.run([sys.executable, str(ROOT / 'scripts/check_customer_copy.py'),
                    '--html', str(PUBLIC), '--strict-review', '--min-html-files', str(len(PAGES))], check=True)
    # Explicit 200 rewrites prevent Netlify's directory URLs from replacing existing canonicals.
    rules = ['/home-7396 / 301!', '/index.html / 301!']
    rules += [f'{route} /{output} 200!' for _, output, route, _, _ in PAGES if route != '/']
    (PUBLIC / '_redirects').write_text('\n'.join(rules) + '\n')
    headers = '/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n'
    if not indexable:
        headers += '  X-Robots-Tag: noindex, nofollow\n'
    (PUBLIC / '_headers').write_text(headers)
    # Netlify redirect rules normalize slashes before matching; an edge function handles
    # alternate URL spellings without creating a /page/ -> /page redirect loop.
    aliases = {'/home-7396': '/', '/home-7396/': '/', '/index.html': '/'}
    for _, _, route, _, _ in PAGES:
        if route != '/':
            aliases.update({route + '/': route, route + '/index.html': route})
    edge = ROOT / 'netlify/edge-functions/canonical-paths.js'
    edge.parent.mkdir(parents=True, exist_ok=True)
    edge.write_text('const aliases = ' + json.dumps(aliases, indent=2) + ';\n\n'
                    'export default function (request) {\n'
                    '  const url = new URL(request.url);\n'
                    '  const target = aliases[url.pathname];\n'
                    '  if (!target || !["GET", "HEAD"].includes(request.method)) return;\n'
                    '  url.pathname = target;\n'
                    '  return Response.redirect(url, 301);\n'
                    '}\n')
    allowed = {output for _, output, _, _, _ in PAGES}
    assert {str(p.relative_to(PUBLIC)) for p in PUBLIC.rglob('*.html')} == allowed
    assert not any(p.name in {'.git', 'docs', 'site', 'SOURCES.md'} or p.suffix == '.py'
                   for p in PUBLIC.rglob('*'))
    print(f'Netlify artifact ready: {len(PAGES)} public pages; indexable={indexable}; publish=dist')


if __name__ == '__main__':
    main()
