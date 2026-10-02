# 5 Day Plantation Shutters

Static HTML/CSS rebuild for the Largo business. All 20 core pages and three city pages are implemented, for 23 pages total. No frontend framework or third-party build dependency. The owner authorized merging to GitHub and deploying to Netlify on October 2, 2026.

## Edit, build, check, preview

Edit bodies in `site/pages/`, shared navigation/footer/reviews/demo in `site/partials/`, the wrapper in `site/layout.html`, and CSS in `styles.css`. Page metadata, routes, breadcrumb parents, and scripts are defined in `scripts/build.py`. Generated `index.html` files are build outputs; do not edit them directly.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 scripts/preview.py
```

Open http://127.0.0.1:4173/. All migrated internal navigation and estimate links stay in the local build. Phone, email, directions, and Google review links retain their real destinations.

## Core page inventory

| Group | Production canonical paths |
| --- | --- |
| Homepage | `/` |
| Shutters | `/plantation-shutters` |
| Blinds | `/blinds`, `/horizontal-blinds`, `/vertical-blinds` |
| Shades | `/shades`, `/roller-shades`, `/solar-shades`, `/zebra-shades`, `/cellular-shades`, `/woven-wood-shades`, `/motorized-shades` |
| Coverage | `/service-areas`, `/Pinellas-window-treatments`, `/Hillsborough-window-treatments` |
| Cities | `/service-areas/largo`, `/service-areas/clearwater`, `/service-areas/st-petersburg` |
| Company | `/about-5day`, `/gallary`, `/contact-5day` |
| Policies | `/privacy-policy`, `/terms-and-conditions` |

Existing path capitalization and the legacy `/gallary` spelling are preserved. The local preview server supports video byte ranges and serves directories with trailing slashes. Netlify serves the listed no-slash canonicals using explicit rewrites; an edge function redirects slash and index-file variants while preserving query strings. `/home-7396` redirects to `/`. `docs/url-migration.csv` records the route inventory.

## Interactions

- Responsive grouped Products menu, native two-column FAQs, and the established Google review carousel.
- Interactive rechargeable-shade illustration on Shades and Motorized Shades. Edit `site/partials/shade-demo.html` and `scripts/shade-demo.js`. Matched reverse clips preserve position on direction changes. Stop pauses; endpoints stay paused. No autoplay or looping.
- Gallery enlarges the eight migrated photos in a native dialog. Buttons and Left/Right keys browse; Escape closes and restores focus. Image links work without the enhancement.
- Contact form validates fields and prepares a `mailto:` draft. It does not submit to a server, store leads, or imply that a request was sent. The customer sends the draft in their email app. Replace this adapter in `scripts/contact.js` with the verified GHL flow later; preserve the field structure.
- City-page estimate links prefill the editable city field on Contact using an allowlist of the three built cities. No request is submitted when following those links.
- Product-page estimate links prefill an editable product choice from the form's actual options. The form appears before the contact details on mobile and has a repeatable email-draft link after validation. It never reports successful delivery.
- Product hubs have keyboard-focusable comparison tables with contained horizontal scrolling on small screens. Educational SVG diagrams explain vertical-blind movement, solar-screen openness, and woven-shade backing without inventing job photography.

## Draft and launch state

Local builds and the initial Netlify deployment remain `noindex, nofollow`; `robots.txt` blocks crawling. Canonicals retain the client's existing domain. The Netlify publication does not by itself switch that domain or its DNS.

## Netlify deployment

The connected GitHub repository's `main` branch uses `netlify.toml`: build command `python3 scripts/build_netlify.py`, publish directory `dist`, Python 3.12. The build renders all 23 pages, copies only public media/browser scripts, checks structure/links/metadata and runs Customer Copy Guard before deployment. Source templates, research, Python files and repository metadata are excluded. The actual build was tested with an injected writer note: it failed before upload, then passed after the fixture was restored.

`SITE_INDEXABLE` is intentionally `false` in `netlify.toml` while the Netlify URL is a review deployment. When the custom domain is ready to replace the old site, change it to `true` in that file and verify the domain, redirects, robots, sitemap and lead flow. Deploy previews remain noindex regardless. Social-image URLs use the deployment origin so the new card loads before the domain switch. GHL remains a later integration; the form explicitly prepares an email draft.

Metadata includes unique titles/descriptions/canonicals, a 1200 × 630 brand card with Open Graph/Twitter tags, matching breadcrumbs, and one stable LocalBusiness entity with the confirmed Largo address and two-county coverage. Internal route links match the production canonicals. No aggregate review rating, invented hours, false local offices, or unverified product brand claims.

The company age remains unconfirmed. Motors are rechargeable; exact brand spelling/model and smart-control accessories still need confirmation. Largo focuses on the actual business address, local hybrid manufacturing, and appointment visits. Clearwater includes the owner-confirmed plantation shutter installation throughout ChartHouse Hotel Clearwater Beach Marina. St. Petersburg compares products for windows and doors. Photos are existing gallery images, not attributed city projects; job photos, dates, and fuller project details remain outstanding. The updated Semrush city shortlist is in `docs/site-build-plan.md`.

See `docs/launch-checklist.md` for remaining production work and `assets/SOURCES.md` for media and content provenance.
