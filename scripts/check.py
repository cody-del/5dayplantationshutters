"""Validate the complete static build without third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import xml.etree.ElementTree as ET
from build import DOMAIN, PAGES, PAGE_LABELS, ROOT


class Page(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__()
        self.ids, self.references, self.anchors, self.images, self.schemas = [], [], [], [], []
        self.h1, self.title, self.capture, self.raw = 0, '', '', ''
        self.canonical, self.robots, self.stack = None, None, []
        self.metadata = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self.capture = 'title'
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.capture, self.raw = 'schema', ''
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots = attrs['content']
        if tag == 'meta' and attrs.get('content'):
            self.metadata[attrs.get('property') or attrs.get('name')] = attrs['content']
        if tag == 'a' and attrs.get('href'):
            self.anchors.append(attrs['href'])
        if tag == 'img':
            self.images.append(attrs)
        for key in ['href', 'src', 'poster']:
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.capture = ''
        if tag == 'script' and self.capture == 'schema':
            self.schemas.append(json.loads(self.raw))
            self.capture = ''
        assert self.stack and self.stack[-1] == tag, f'Invalid nesting: </{tag}> after {self.stack[-5:]}'
        self.stack.pop()

    def handle_data(self, data):
        if self.capture == 'title':
            self.title += data
        elif self.capture == 'schema':
            self.raw += data


def check(root=ROOT, indexable=False, asset_origin=DOMAIN):
    ROOT = root
    parsed = {}
    for name, output, route, title, _ in PAGES:
        text = (ROOT / output).read_text()
        page = Page()
        page.feed(text)
        assert not page.stack, (name, 'unclosed tags')
        assert page.h1 == 1, (name, 'H1 count')
        assert len(page.ids) == len(set(page.ids)), (name, 'duplicate IDs')
        assert '{{' not in text, (name, 'unresolved template')
        assert page.canonical == DOMAIN + route, (name, 'canonical')
        assert page.robots == ('index, follow' if indexable else 'noindex, nofollow'), (name, 'robots do not match build context')
        assert page.title == title, (name, 'title')
        assert page.metadata['og:url'] == page.canonical, (name, 'social canonical')
        assert page.metadata['og:title'] == page.metadata['twitter:title'] == title
        assert page.metadata['og:description'] == page.metadata['twitter:description'] == page.metadata['description']
        assert page.metadata['twitter:card'] == 'summary_large_image'
        social = urlsplit(page.metadata['og:image'])
        assert page.metadata['twitter:image'] == page.metadata['og:image']
        assert social.netloc == urlsplit(asset_origin).netloc and social.path.startswith('/assets/')
        assert social.path.endswith(('.jpg', '.jpeg', '.png', '.webp')), (name, 'social image format')
        assert (ROOT / social.path.lstrip('/')).is_file(), (name, 'missing social image')
        assert page.metadata['og:image:alt'] and page.metadata['twitter:image:alt']
        for image in page.images:
            assert all(key in image for key in ['alt', 'width', 'height']), (name, image)
        graph = page.schemas[0]['@graph']
        business = next(item for item in graph if item['@type'] == 'LocalBusiness')
        assert business['address']['streetAddress'] == '1876 Lake Ave SE, Unit F'
        assert 'aggregateRating' not in business and 'openingHours' not in business
        if name != 'home':
            crumbs = next(item for item in graph if item['@type'] == 'BreadcrumbList')['itemListElement']
            assert [item['position'] for item in crumbs] == list(range(1, len(crumbs) + 1))
            assert crumbs[-1]['item'] == page.canonical
            assert crumbs[-1]['name'] == PAGE_LABELS[name]
        parsed[route] = page

    outputs = {route: output for _, output, route, _, _ in PAGES}
    for route, page in parsed.items():
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            target = ROOT / path.lstrip('/') if path else ROOT / outputs[route]
            if path == '/':
                target = ROOT / 'index.html'
            elif path.endswith('/') or target.is_dir():
                target /= 'index.html'
            assert target.exists(), (route, reference, 'missing target')
            if url.fragment:
                destination = Page()
                destination.feed(target.read_text())
                assert unquote(url.fragment) in destination.ids, (route, reference, 'missing anchor')
        assert not any(link.startswith(DOMAIN) for link in page.anchors), (route, 'internal link still points to live site')
        for link in page.anchors:
            url = urlsplit(link)
            if not url.scheme and not url.netloc and url.path.startswith('/'):
                normalized = url.path.rstrip('/') or '/'
                if normalized in outputs:
                    assert url.path == normalized, (route, link, 'internal route differs from canonical path')

    assert len({page.title for page in parsed.values()}) == len(parsed), 'Duplicate titles'
    assert len({page.canonical for page in parsed.values()}) == len(parsed), 'Duplicate canonicals'
    namespaces = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    urls = {node.text for node in sitemap.findall('.//s:loc', namespaces)}
    assert urls == {page.canonical for page in parsed.values()}, 'Sitemap coverage mismatch'
    print(f'PASS: {len(parsed)} pages; HTML nesting, H1s, IDs, metadata/social images, local links/assets/anchors, image attributes, schema and sitemap.')


if __name__ == '__main__':
    check()
