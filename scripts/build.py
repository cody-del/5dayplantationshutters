"""Build dependency-free HTML pages from shared, editable source partials."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://fivedayplantationshutters.com'
PAGES = [
    ('home', 'index.html', '/', 'Plantation Shutters Tampa Bay | Made in Largo | 5 Day Plantation Shutters',
     'Hybrid shutters manufactured in Largo, plus blinds and shades. Free consultations and in-house installation across Pinellas and Hillsborough counties.'),
    ('plantation-shutters', 'plantation-shutters/index.html', '/plantation-shutters',
     'Custom Plantation Shutters | Materials & Options | 5 Day',
     'Compare hybrid, PVC and hardwood plantation shutters. Free in-home measurements and in-house installation across Tampa Bay.'),
    ('blinds', 'blinds/index.html', '/blinds',
     'Custom Blinds Tampa Bay | Faux Wood & Vertical | 5 Day',
     'Compare faux wood and vertical blinds for your Tampa Bay home. Free measurements and in-house installation across Pinellas and Hillsborough counties.'),
    ('shades', 'shades/index.html', '/shades',
     'Custom Window Shades Tampa Bay | 5 Day Plantation Shutters',
     'Explore roller, solar, zebra, cellular and woven wood shades. Free consultations and in-house installation across Pinellas and Hillsborough counties.'),
    ('roller-shades', 'roller-shades/index.html', '/roller-shades',
     'Custom Roller Shades Tampa Bay | Fabrics & Controls | 5 Day',
     'Compare light-filtering and blackout roller shades, mounting and controls. Free consultations and in-house installation across Pinellas and Hillsborough.'),
    ('horizontal-blinds', 'horizontal-blinds/index.html', '/horizontal-blinds',
     'Faux Wood & Horizontal Blinds Tampa Bay | 5 Day Shutters',
     'Custom faux wood horizontal blinds for Tampa Bay homes. Compare finishes, fit and controls with free measurements and in-house installation.'),
]
PAGES += [
    ('vertical-blinds', 'vertical-blinds/index.html', '/vertical-blinds', 'Vertical Blinds Tampa Bay | Sliding Doors & Wide Windows | 5 Day', 'Custom vertical blinds for sliding glass doors and wide windows. Free measurements and in-house installation across Pinellas and Hillsborough counties.'),
    ('solar-shades', 'solar-shades/index.html', '/solar-shades', 'Solar Shades Tampa Bay | Glare, Views & Privacy | 5 Day', 'Compare solar screen fabrics for glare control and outward views. Free in-home consultations and installation by our Tampa Bay team.'),
    ('zebra-shades', 'zebra-shades/index.html', '/zebra-shades', 'Zebra & Layered Shades Tampa Bay | Custom Options | 5 Day', 'Explore zebra shades with alternating sheer and solid fabric bands. Compare light, privacy and controls at a free Tampa Bay consultation.'),
    ('cellular-shades', 'cellular-shades/index.html', '/cellular-shades', 'Cellular & Honeycomb Shades Tampa Bay | 5 Day Shutters', 'Compare cellular shade fabrics, honeycomb construction and controls. Free measurements and in-house installation throughout Tampa Bay.'),
    ('woven-wood-shades', 'woven-wood-shades/index.html', '/woven-wood-shades', 'Woven Wood Shades Tampa Bay | Texture & Privacy | 5 Day', 'Bring natural woven texture to your windows. Compare weaves, available liners and controls with a free in-home consultation in Tampa Bay.'),
    ('motorized-shades', 'motorized-shades/index.html', '/motorized-shades', 'Rechargeable Motorized Shades Tampa Bay | 5 Day Shutters', 'Rechargeable motorized shades measured and installed by our in-house team. Explore remote operation and compare shade styles at a free consultation.'),
    ('service-areas', 'service-areas/index.html', '/service-areas', 'Window Treatment Service Areas | Pinellas & Hillsborough | 5 Day', 'Free consultations and in-house installation for shutters, blinds and shades throughout Pinellas and Hillsborough counties. Based in Largo.'),
    ('pinellas', 'Pinellas-window-treatments/index.html', '/Pinellas-window-treatments', 'Window Treatments Pinellas County | Shutters, Blinds & Shades | 5 Day', 'Hybrid shutters made in Largo, plus PVC, hardwood, blinds and shades. Free consultations and in-house installation throughout Pinellas County.'),
    ('hillsborough', 'Hillsborough-window-treatments/index.html', '/Hillsborough-window-treatments', 'Window Treatments Hillsborough County | In-Home Consultations | 5 Day', 'Custom shutters, blinds and shades for Tampa, Brandon, Riverview and all Hillsborough County. Free measurements and installation by our own team.'),
    ('largo', 'service-areas/largo/index.html', '/service-areas/largo', 'Plantation Shutters Largo | Locally Made Hybrid Shutters | 5 Day', 'Hybrid plantation shutters manufactured in Largo, plus PVC, hardwood, blinds and shades. Free in-home estimates, appointment visits and in-house installation.'),
    ('clearwater', 'service-areas/clearwater/index.html', '/service-areas/clearwater', 'Plantation Shutters Clearwater | Free In-Home Estimates | 5 Day', 'Compare hybrid, PVC and hardwood plantation shutters for your Clearwater home. Free measurements and installation by our in-house team, based in Largo.'),
    ('st-petersburg', 'service-areas/st-petersburg/index.html', '/service-areas/st-petersburg', 'Window Treatments St. Petersburg | Shutters, Blinds & Shades', 'Compare plantation shutters, faux wood and vertical blinds, and five shade styles in St. Petersburg. Free in-home consultations and in-house installation.'),
    ('about', 'about-5day/index.html', '/about-5day', 'About 5 Day Plantation Shutters | Made in Largo, Florida', 'Meet the Largo business manufacturing hybrid plantation shutters and installing shutters, blinds and shades across Tampa Bay with its own team.'),
    ('gallery', 'gallary/index.html', '/gallary', 'Shutter & Shade Photo Gallery | 5 Day Plantation Shutters', 'Browse the 5 Day Plantation Shutters photo gallery for window, door and room ideas. Arrange a free consultation throughout Tampa Bay.'),
    ('contact', 'contact-5day/index.html', '/contact-5day', 'Free Window Treatment Consultation | Contact 5 Day Shutters', 'Request a free in-home consultation for shutters, blinds or shades. Call (813) 317-1077. Visit our Largo location by appointment.'),
    ('privacy', 'privacy-policy/index.html', '/privacy-policy', 'Privacy Policy | 5 Day Plantation Shutters', 'Read the privacy policy for 5 Day Plantation Shutters Tampa Bay LLC, including data use, communications and contact information.'),
    ('terms', 'terms-and-conditions/index.html', '/terms-and-conditions', 'Terms & Conditions | 5 Day Plantation Shutters', 'Read the terms and conditions for the website and services of 5 Day Plantation Shutters Tampa Bay LLC.'),
]
PAGE_LABELS = {'plantation-shutters': 'Plantation shutters', 'blinds': 'Blinds',
               'shades': 'Shades', 'roller-shades': 'Roller shades',
               'horizontal-blinds': 'Faux wood blinds'}
PAGE_LABELS.update({'vertical-blinds': 'Vertical blinds', 'solar-shades': 'Solar shades',
                    'zebra-shades': 'Zebra shades', 'cellular-shades': 'Cellular shades',
                    'woven-wood-shades': 'Woven wood shades', 'motorized-shades': 'Motorized shades',
                    'service-areas': 'Service areas', 'pinellas': 'Pinellas County',
                    'hillsborough': 'Hillsborough County', 'about': 'About us', 'gallery': 'Gallery',
                    'contact': 'Contact us', 'privacy': 'Privacy policy', 'terms': 'Terms & conditions'})
CITY_PAGES = {'largo': 'Largo', 'clearwater': 'Clearwater', 'st-petersburg': 'St. Petersburg'}
PAGE_LABELS.update(CITY_PAGES)
PAGE_PARENTS = {'roller-shades': ('Shades', '/shades'),
                'horizontal-blinds': ('Blinds', '/blinds')}
PAGE_PARENTS.update({'vertical-blinds': ('Blinds', '/blinds'),
                    **{name: ('Shades', '/shades') for name in
                       ['solar-shades', 'zebra-shades', 'cellular-shades', 'woven-wood-shades', 'motorized-shades']},
                    'pinellas': ('Service areas', '/service-areas'),
                    'hillsborough': ('Service areas', '/service-areas')})
PAGE_PARENTS.update({name: ('Pinellas County', '/Pinellas-window-treatments') for name in CITY_PAGES})
HERO_IMAGES = {'home': '/assets/shutters-hero.webp', 'plantation-shutters': '/assets/shutters-hero.webp',
               'blinds': '/assets/horizontal-blinds.webp', 'horizontal-blinds': '/assets/horizontal-blinds.webp',
               'shades': '/assets/roller-shades.webp', 'roller-shades': '/assets/roller-shades.webp',
               'zebra-shades': '/assets/migrated/zebra-shades.webp',
               'cellular-shades': '/assets/migrated/cellular-shades.webp', 'motorized-shades': '/assets/roller-shades.webp',
               'pinellas': '/assets/migrated/gallery-02.webp', 'hillsborough': '/assets/migrated/gallery-06.webp',
               'about': '/assets/migrated/gallery-01.webp'}
HERO_IMAGES.update({'largo': '/assets/migrated/gallery-01.webp',
                    'clearwater': '/assets/migrated/gallery-03.webp',
                    'st-petersburg': '/assets/migrated/gallery-06.webp'})
PAGE_SCRIPTS = {'shades': ['shade-demo.js'], 'motorized-shades': ['shade-demo.js'],
                'gallery': ['gallery.js'], 'contact': ['contact.js?v=consultation-v2']}

# Use a neutral brand image rather than implying a photo shows a job in a named city.
SOCIAL_IMAGE = '/assets/social-preview.jpg'

def business_schema():
    return {'@type': 'LocalBusiness', '@id': DOMAIN + '/#business',
            'name': '5 Day Plantation Shutters', 'url': DOMAIN + '/',
            'logo': DOMAIN + '/assets/logo.png', 'telephone': '+18133171077',
            'email': '5dayshutters@gmail.com',
            'description': 'Hybrid plantation shutters manufactured in Largo, with shutters, blinds and shades measured and installed by our in-house team across Pinellas and Hillsborough counties.',
            'address': {'@type': 'PostalAddress', 'streetAddress': '1876 Lake Ave SE, Unit F',
                        'addressLocality': 'Largo', 'addressRegion': 'FL', 'postalCode': '33771', 'addressCountry': 'US'},
            'areaServed': [{'@type': 'AdministrativeArea', 'name': name + ' County, Florida'}
                           for name in ['Pinellas', 'Hillsborough']]}

def build(output_root=ROOT, indexable=False, asset_origin=DOMAIN):
    layout = (ROOT / 'site/layout.html').read_text()
    partials = {p.stem: p.read_text().strip() for p in (ROOT / 'site/partials').glob('*.html')}
    for name, output, route, title, description in PAGES:
        body = (ROOT / f'site/pages/{name}.html').read_text().strip()
        for key, value in partials.items():
            body = body.replace('{{' + key + '}}', value)
        graph = [business_schema(), {'@type': 'WebPage', '@id': DOMAIN + route + '#webpage',
                 'url': DOMAIN + route, 'name': title, 'description': description,
                 'inLanguage': 'en-US', 'publisher': {'@id': DOMAIN + '/#business'}}]
        if name != 'home':
            crumbs = [('Home', '/')]
            if name in CITY_PAGES:
                crumbs.append(('Service areas', '/service-areas'))
            if name in PAGE_PARENTS:
                crumbs.append(PAGE_PARENTS[name])
            crumbs.append((PAGE_LABELS[name], route))
            data = {'@type': 'BreadcrumbList', '@id': DOMAIN + route + '#breadcrumb', 'itemListElement': [
                {'@type': 'ListItem', 'position': position, 'name': label, 'item': DOMAIN + path}
                for position, (label, path) in enumerate(crumbs, start=1)
            ]}
            graph.append(data)
            graph[1]['breadcrumb'] = {'@id': data['@id']}
        schema = '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}) + '</script>'
        values = {**partials, 'content': body, 'title': escape(title), 'description': escape(description, quote=True),
                  'canonical': DOMAIN + route, 'page_class': name, 'schema': schema,
                  'social_image': asset_origin.rstrip('/') + SOCIAL_IMAGE,
                  'robots': 'index, follow' if indexable else 'noindex, nofollow',
                  'social_image_alt': '5 Day Plantation Shutters — shutters, blinds and shades for Tampa Bay',
                  'page_scripts': ''.join(f'<script src="/scripts/{script}" defer></script>' for script in PAGE_SCRIPTS.get(name, [])),
                  'hero_preload': f'<link rel="preload" as="image" href="{HERO_IMAGES[name]}">' if name in HERO_IMAGES else ''}
        result = layout
        for key, value in values.items():
            result = result.replace('{{' + key + '}}', value)
        if '{{' in result:
            raise ValueError(f'Unresolved template value in {name}')
        target = output_root / output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(line.rstrip() for line in result.splitlines()) + "\n")
        print(f'Built {output}')
    # Launch routing must use these exact canonical URLs. This local draft remains noindex.
    urls = '\n'.join('  <url><loc>' + DOMAIN + route + '</loc></url>' for _, _, route, _, _ in PAGES)
    (output_root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '\n</urlset>\n')
    (output_root / 'robots.txt').write_text('User-agent: *\n' + ('Allow: /\nSitemap: ' + DOMAIN + '/sitemap.xml\n' if indexable else 'Disallow: /\n'))

if __name__ == '__main__':
    build()
