"""Generate code-native educational SVGs and the source for a branded social card."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
DIAGRAMS = ASSETS / 'diagrams'
DIAGRAMS.mkdir(exist_ok=True)

def save(name, width, height, title, body):
    (DIAGRAMS / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
        f'<title>{title}</title>{body}</svg>\n')

vertical = '<rect width="720" height="400" rx="16" fill="#f5f5f5"/>'
for x, label in [(34, 'Across the opening'), (380, 'Gathered to the side')]:
    vertical += f'<text x="{x}" y="46" fill="#202020" font-family="Arial,sans-serif" font-size="22" font-weight="bold">{label}</text>'
    vertical += f'<rect x="{x}" y="75" width="300" height="250" fill="#e2e8ea" stroke="#a0a5a6" stroke-width="3"/>'
    vertical += f'<path d="M{x+150} 75v250" stroke="#a0a5a6" stroke-width="3"/>'
    vertical += f'<rect x="{x-5}" y="70" width="310" height="12" rx="3" fill="#333"/>'
for x in range(43, 319, 29):
    vertical += f'<rect x="{x}" y="84" width="25" height="240" rx="2" fill="#fff" stroke="#bbb"/>'
for x in range(385, 432, 8):
    vertical += f'<rect x="{x}" y="84" width="7" height="240" rx="2" fill="#fff" stroke="#aaa"/>'
vertical += '<path d="M620 348H455m15-10-15 10 15 10" fill="none" stroke="#cf1726" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
vertical += '<text x="34" y="366" fill="#666" font-family="Arial,sans-serif" font-size="18">Vanes tilt to adjust light</text>'
save('vertical-movement.svg', 720, 400, 'Vertical blind movement illustration', vertical)

woven = '<rect width="720" height="400" rx="16" fill="#f5f5f5"/>'
for x, label, background in [(34, 'Open weave', '#e6ecee'), (380, 'With an opaque backing', '#d4c6b5')]:
    woven += f'<text x="{x}" y="46" fill="#202020" font-family="Arial,sans-serif" font-size="22" font-weight="bold">{label}</text>'
    woven += f'<rect x="{x}" y="75" width="300" height="250" rx="6" fill="{background}"/>'
    for dx in range(8, 295, 23):
        woven += f'<path d="M{x+dx} 75v250" stroke="#b8a386" stroke-width="9"/>'
    for y in range(88, 322, 22):
        woven += f'<path d="M{x} {y}h300" stroke="#8d765b" stroke-width="6"/>'
woven += '<text x="34" y="366" fill="#666" font-family="Arial,sans-serif" font-size="18">Gaps allow light and view</text><text x="380" y="366" fill="#666" font-family="Arial,sans-serif" font-size="18">Backing changes coverage</text>'
save('woven-texture.svg', 720, 400, 'Woven shade weave and backing illustration', woven)

solar = '<rect width="720" height="400" rx="16" fill="#f5f5f5"/>'
solar += '<defs><pattern id="tight" width="18" height="18" patternUnits="userSpaceOnUse"><rect width="18" height="18" fill="#9ba5a2"/><rect x="6" y="6" width="6" height="6" fill="#e9eeee"/></pattern><pattern id="open" width="18" height="18" patternUnits="userSpaceOnUse"><rect width="18" height="18" fill="#9ba5a2"/><rect x="3" y="3" width="12" height="12" fill="#e9eeee"/></pattern></defs>'
for x, label, pattern, detail in [(34, 'Tighter weave', 'tight', 'Less light and view through'), (380, 'More open weave', 'open', 'More light and view through')]:
    solar += f'<text x="{x}" y="46" fill="#202020" font-family="Arial,sans-serif" font-size="22" font-weight="bold">{label}</text><rect x="{x}" y="75" width="300" height="250" rx="6" fill="url(#{pattern})"/><text x="{x}" y="366" fill="#666" font-family="Arial,sans-serif" font-size="18">{detail}</text>'
save('solar-screen.svg', 720, 400, 'Screen openness illustration, not specific fabric samples', solar)

logo = base64.b64encode((ASSETS / 'logo.png').read_bytes()).decode()
(ASSETS / 'social-preview.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630" viewBox="0 0 1200 630">
<title>5 Day Plantation Shutters — Tampa Bay</title>
<rect width="1200" height="630" fill="#e7e7e7"/>
<image x="485" y="48" width="230" height="225" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{logo}"/>
<g fill="#202020" font-family="Arial,sans-serif" text-anchor="middle">
<text x="600" y="355" font-size="52" font-weight="bold">5 Day Plantation Shutters</text>
<text x="600" y="414" font-size="30">Shutters · Blinds · Shades</text>
<text x="600" y="475" font-size="25">Hybrid shutters made in Largo · Serving Tampa Bay</text>
</g><rect x="0" y="555" width="1200" height="75" fill="#cf1726"/>
<text x="600" y="602" fill="#fff" font-family="Arial,sans-serif" font-size="26" text-anchor="middle">Free in-home consultations · (813) 317-1077</text>
</svg>\n''')
print('Generated three educational diagrams and social-preview.svg.')
