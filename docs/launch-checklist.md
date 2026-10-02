# Rebuild and launch checklist

## Current draft — October 2

### Authorized GitHub merge and Netlify publication — October 2

The owner authorized merging this rebuild to GitHub and deploying it on Netlify. This supersedes the earlier local-only restriction below. The publication uses the GitHub `main` branch and a public-only `dist` artifact. The actual Netlify build now gates all 23 rendered pages with structural/link/metadata checks and Customer Copy Guard; a deliberate writer-note fixture failed the build before upload and restored copy passed. Production and deploy-preview indexing contexts were tested separately. The Netlify URL stays noindex while the existing domain remains on its current host; a domain/DNS cutover is separate. The email-draft consultation flow remains in place until the later GHL connection. Team/history/photo inputs and separate Tampa pages retain their previous status.

October 2: separate Tampa/Tampa shutter pages are on hold at the owner's request. The build remains 23 pages: 20 core plus Largo, Clearwater, and St. Petersburg. Apollo Beach, Brandon, and Riverview have unregistered source drafts only, pending city selection; they are not completed preview pages. Both county pages are built. GHL, final media/details, and production migration work remain outstanding.

### Audit fixes implemented locally — October 2

| Pages | What changed |
| --- | --- |
| Homepage, About, Gallery | Stronger confirmed in-house manufacturing/installation story, clearer product guidance, useful gallery-to-product links, and links to the confirmed ChartHouse installation. No invented team biographies or company age. |
| All 11 product pages | More direct headings and answers, fewer repeated qualifications, three comparison tables on the product hubs, and clearer material/light/privacy/control decisions. Vertical, solar, and woven pages have labeled educational diagrams. |
| Service Areas, both counties, Largo, Clearwater, St. Petersburg | Distinct page purposes retained; improved headings, comparisons, appointment guidance, and project links. No city-name-swapped expansion or new office claims. |
| Contact | Form precedes contact details on mobile, estimate buttons reach the form, product/city prefills stay editable, and email-draft delivery steps are explicit. Validation and a repeatable draft link are implemented. |
| Privacy, Terms | Removed automatic promotional-SMS consent from phone-number entry and reconciled service-provider processing with promotional sharing. Dates updated; final program/data-practice review remains pending. |
| Shared technical setup | Open Graph/Twitter image metadata and a 1200 × 630 branded card; internal route links match preserved canonical paths. Existing schema, sitemap, and draft indexing protections are retained. |

The changes use the existing Semrush demand/ranking baseline to preserve the homepage's Tampa/Tampa Bay role and develop product comparisons and three distinct Pinellas city pages. No ranking recovery or new search visibility is claimed. Search Console evidence is still needed before redirecting or merging pages for suspected cannibalization.

What still needs inputs: named team/history, verified installation-photo ownership and city/product labels, fuller local project evidence, exact stocked finishes/controls and written warranty terms, GHL configuration and tested lead delivery, and the final host/routing setup. Production redirects, analytics events, live Core Web Vitals, Google Business Profile changes, and post-launch Search Console monitoring have not been implemented or measured. The owner's instruction against pushing/deploying remains in effect.

Verification: all 23 generated pages pass `scripts/check.py`, including HTML structure, metadata/social assets, canonical internal links, local targets/fragments, schema, and sitemap. Customer Copy Guard checks all 23 outputs with zero blockers or review warnings (`docs/research/2026-10-02-copy-guard.json`). Browser checks at 1280px, 390px, and 320px report one H1 and no page-level overflow (`docs/research/2026-10-02-rendered-checks.json`); no broken loaded images were observed. Required-field validation and Roller Shades/Clearwater prefills were verified without sending a request. A pure-function check confirms the email recipient and multiline/unicode/query-separator encoding. The comparison region accepts keyboard focus and ArrowRight scrolls its columns while page width stays contained. The shade demo starts closed/paused; Up → Stop at a partial position → Down switched to the reverse clip and lowered, and Stop paused both players. Temporary viewport overrides were reset. Screenshot evidence: `tmp/shutter-comparison-refined.jpg`, `tmp/shade-comparison-refined.jpg`, and `tmp/consultation-mobile-refined.jpg`. No emails, leads, pushes, deployments, or monitoring automations were created.

- Accepted light-gray homepage header/footer, inset estimate/call buttons, and centered transparent logo are preserved.
- All 20 core pages share editable HTML partials. Product detail pages, the service-area hub, both county pages, About, Gallery, Contact, Privacy and Terms are implemented. Run `python3 scripts/build.py` and `python3 scripts/check.py`.
- Shutter page compares locally manufactured Hybrid Plantation Shutters, supplier-made PVC Plantation Shutters, and supplier-made Hardwood Plantation Shutters, with sizing/finish guidance, in-house installation, eight FAQs, and free consultation calls to action.
- Eight owner-supplied Google reviews appear in the shared responsive carousel. No aggregate rating/count or review schema is asserted.
- Owner confirmed contact details, appointment-only Largo visits, free consultations, in-house installation without subcontractors, county coverage, and limited lifetime shutter warranty. No guaranteed five-day completion claim.
- Homepage product descriptions reflect the confirmed offerings; Roman shades and real wood blinds are excluded.
- Root and existing product canonical URLs preserved; draft noindex remains. Production routing must serve the existing no-trailing-slash product URL, with the alternate redirected consistently.
- All migrated navigation and estimate links now use local pages. Contact has native validation and an email-draft adapter; GHL is left for the later connection requested by the owner. No successful lead delivery is simulated.
- Gallery reuses eight photos from the old website with descriptive captions, enlargement, and keyboard navigation. Product/city attribution is still needed before those photos support city-specific project stories.
- LocalBusiness and matching breadcrumb data, unique metadata, a planned sitemap, and a URL migration inventory are implemented. Robots and noindex protect the local draft.
- Rechargeable motors confirmed October 1. No business-age claim is published; the owner will verify the start year. Exact motor brand spelling/model remains to confirm before branded specifications are added.

## Required before production

- Confirm logo/photo rights, current product-specific turnaround and written warranty terms. Address, contact details, active products and county coverage have been confirmed by the owner.
- Check the Google review destination before launch. The current carousel uses the eight owner-supplied screenshots and the place ID from the existing website. Do not add self-serving LocalBusiness AggregateRating markup.
- Confirm appointment scheduling hours before adding opening-hours schema. Largo visits are appointment only.
- Review the completed page copy and media before switching the domain. Product, county, company, contact and policy pages are now migrated locally.
- Preserve /plantation-shutters, /roller-shades, /horizontal-blinds, /Pinellas-window-treatments, /Hillsborough-window-treatments, /about-5day, /gallary, /contact-5day, /privacy-policy and /terms-and-conditions. Do not rename /gallary just for spelling without a redirect.
- Export Search Console query/page history, current indexed URL inventory, analytics conversions and valuable backlinks. Verify cannibalization from switching URLs and intent overlap rather than repeated branded rows.
- Protect / as the main Tampa/Tampa Bay plantation-shutters entry point. Build product depth separately; avoid a competing Tampa shutter page until supported by evidence.
- Add useful Largo, Clearwater and St. Petersburg coverage with real projects, then expand to other served cities based on demand and evidence. Do not generate city-name-swapped duplicates.
- Connect and test the production GHL contact flow (success, validation, failure, spam protection and actual lead delivery). Contact/Privacy/Terms consent language is now consistent, but the final opt-in, messaging program and data practices must match the actual GHL configuration. These local policy edits are not a legal review or compliance certification.
- Validate the implemented LocalBusiness entity and breadcrumbs against the final visible business details. Add hours only if confirmed. No fabricated reviews or unsupported product claims.
- Configure server-side 301 /home-7396 to /. Test real HTTP status and Location headers, canonical consistency, trailing-slash/case behavior, and every changed URL. Do not use blanket homepage redirects for removed service pages.
- The sitemap inventories all 23 planned canonical pages. At launch confirm only final indexable URLs are included, validate robots.txt, and remove draft noindex on production only. Staging remains excluded from indexing.
- Validate mobile layout, keyboard access, working call links, form delivery, Core Web Vitals, metadata, structured data and all internal links. Fonts currently load from Google Fonts; self-host selected WOFF2 files if desired before release.
- Serve video assets with HTTP byte-range support and verify mid-travel reversals in Safari on the final host. Local preview now uses `python3 scripts/preview.py`; a simple server without byte ranges can restart a reverse clip from the top even with correctly encoded media.
- Track call clicks separately from actual calls, and successful form submissions separately from form starts. Compare Search Console landing-page performance and leads after launch.

## Ranking baseline

Source: supplied Semrush US desktop report dated September 30, 2026, cross-checked through connected Semrush organic research. Not a local Maps grid or real-time city ranking.

| Query | Position | URL |
| --- | ---: | --- |
| 5 day plantation shutters | 2 | / |
| plantation shutters tampa | 8 | / |
| tampa plantation shutters | 8 | / |
| indoor shutters tampa | 9 | / |
| plantation shutters in tampa | 12 | / |
| window shutters tampa | 13 | / |
| plantation shutters clearwater | 27 | / |
| window treatments tampa | 51 | / |

No 5 Day project was found in the connected Semrush project list. City/device tracking and Search Console access remain outstanding. No AI visibility score has been measured.

## September 30 local design revision

Rebuilt the homepage using Solomon Shade Solutions as a visual reference for hierarchy and spacing. White centered-logo header, restrained Manrope typography, centered product/location headline, image-led product cards, source-attributed reviews, and consistent section spacing. All work after the owner's no-push instruction stays local; do not push, update the PR, or deploy unless they authorize it.

## Blinds hub — October 1

Built `/blinds` as the comparison hub for faux wood horizontal and vertical blinds. Linked from homepage product card, desktop/mobile Products menus, and footer. Added unique title/description, self-canonical and accurate Blinds breadcrumb markup. The shared layout now preloads each page’s own hero image. No blind-specific warranty, exact slat sizes, motorization, in-house blind manufacturing, or supplier brands are claimed.

Verified generated HTML for local links/assets/anchors, unique IDs, one H1, draft noindex, canonical and JSON-LD; checked browser layout at desktop, 390px and 320px, image loading, comparison anchor and FAQ interaction. Existing horizontal-blinds detail page remains on the live domain pending its own rebuild.

## Shades hub — October 1

Built `/shades` with the five confirmed product categories, explanatory fabric/privacy guidance, conditional control options, eight FAQs, shared reviews, and consultation calls to action. The Products menu, homepage shade card, footer and Blinds comparison link now lead to the local hub. The existing `/roller-shades` detail URL remains on the live domain pending its own rebuild. No Roman shades, unverified brand affiliation, precise performance percentages, guaranteed blackout installation, or universal motor/control compatibility are claimed.

Checks passed for all four generated pages: local links/assets/anchors, unique IDs, one H1, draft noindex, canonical and parsed breadcrumb JSON-LD. Verified desktop layout, 390px mobile hero/category layout, 320px overflow check, shade jump links, expanded FAQ and homepage navigation to Shades. GHL and owner installation photography remain pending.

## Interactive shade demo — October 1

Added a remote on the left and a video on the right after the shade-control comparison. Up and Down each play a separate direction clip; Stop pauses both players. Opposite-direction requests map the current frame to its matching frame in the other clip. Ended playback stays fully open or closed, with no loop or automatic return. Commands cancel stale asynchronous requests; leaving the browser tab pauses movement. Buttons are native keyboard-accessible controls with labels, focus indicators, and live state announcements. Media loads near the section and never autoplays.

Verified in the browser: initial paused state; mid-travel Stop and unchanged time afterward; downward reversal from that stopped position; lower endpoint paused/ended; upper endpoint paused/ended; Up at the upper limit; rapid Down/Up/Stop cancellation; mobile layout and controls at 390px. JavaScript syntax and all four pages’ local assets/anchors/IDs/headings also checked. Remote PNG has real transparency; generated asset provenance is recorded in `assets/SOURCES.md`.

Refined the heading to “Your light. At your command.” and removed the visible captions beneath the video at the owner's request. Live status remains available to screen readers. Rechecked Up → Stop midway → Down in the browser: the reverse clip starts at the corresponding stopped position and lowers immediately.

## Roller Shades detail page — October 1

Built the local `/roller-shades/` preview while preserving `/roller-shades` as the production canonical. Reuses the approved shell, reviews and two-column FAQs. Explains light-filtering and room-darkening/blackout fabrics, edge light and mounting, conditional controls, price factors and in-house installation. Linked from the Shades hub and as a subtype below Shades in both Products menus. Home → Shades → Roller shades appears in visible breadcrumbs and matching BreadcrumbList markup. The interactive remote stays on the Shades hub and is linked from the motorized control section.

All five generated pages passed checks for local assets/anchors, unique IDs, one H1, draft noindex, titles, canonicals and parsed breadcrumb JSON-LD. Browser checks passed for the desktop hero/fabric comparison and expanded FAQ, 390px mobile hero and product-menu navigation, single-column fabric layout, and 320px overflow. No live URLs, redirects, lead forms, deployment or GitHub state were changed. Next: Horizontal Blinds, then the service-area hub and existing county pages. Project photography, GHL integration and production routing remain pending.

## Faux Wood / Horizontal Blinds — October 1

Built the local `/horizontal-blinds/` preview with `/horizontal-blinds` preserved as the production canonical. Public copy focuses on the confirmed faux wood range, tilt/lift operation, mounting clearance, slat and finish selection, privacy, price factors and in-house installation. Reviews remain general customer reviews. Exact slat widths, control systems, manufacturer branding, water resistance and blind warranty terms are not asserted. Blinds hub and desktop/mobile Products menus now use the local detail page. Visible and structured breadcrumbs match Home → Blinds → Faux wood blinds.

All six generated pages passed asset/anchor checks, unique titles/canonicals/IDs, one H1, draft robots and parsed breadcrumb JSON-LD. Browser checks passed for desktop hero and detail layout, hub and Products-menu navigation, product jump link, FAQ activation with Enter, 390px mobile hero/menu navigation and 320px overflow/single-column FAQ layout. Work remains local. Next: service-area hub, then Pinellas and Hillsborough county rewrites. City project evidence, GHL and production routing remain pending.

## Bulk completion — October 1

Added the remaining 14 core pages, bringing the local site to 20. Product pages are complete for vertical blinds and solar, zebra/layered, cellular/honeycomb, woven wood, and rechargeable motorized shades. Service-area hub, both existing county routes, About, Gallery, Contact, Privacy and Terms are migrated. Desktop and mobile menus and all estimate links now reach local pages. County copy has distinct purposes: Largo manufacturing and visits in Pinellas, in-home consultation logistics in Hillsborough. Full legacy coverage lists are retained; no thin city pages or invented city projects were generated.

All 20 pages passed `scripts/check.py`: valid nesting, one H1, unique titles/canonicals/IDs, local references and fragments, image attributes, matching breadcrumb markup, confirmed LocalBusiness data, and sitemap coverage. Browser checks covered all 20 at 1280px, 390px and 320px with no horizontal overflow. Product heroes/media loaded; mobile FAQs use one column. Desktop/mobile Products navigation and keyboard FAQ controls work. Gallery enlargement, Next/Previous and Left/Right keys, Escape close, and focus return passed. Contact's required-field and invalid-email behavior passed; valid field values and email recipient/encoding were checked without sending a request.

The new Motorized page exposed a preview-server byte-range issue. Both clips were re-encoded with uniform timestamps, and the preview server now returns 206/Content-Range for supported byte requests. Partial, suffix, open-ended, HEAD and out-of-range requests were checked. Browser reversal now starts at the corresponding paused position; both endpoints remain paused. This supersedes the earlier simple-server video check. The GHL submission adapter, actual lead delivery and production routing remain pre-launch tasks.

## First three city page drafts — October 1

The owner authorized building the first three city pages. Routes: `/service-areas/largo`, `/service-areas/clearwater`, and `/service-areas/st-petersburg`. Largo covers the actual business location, locally manufactured hybrid shutters, appointment visits, and material selection. Clearwater focuses on shutter finish/louver/panel decisions, condo requirements supplied by the customer, privacy, and the owner-confirmed ChartHouse Hotel Clearwater Beach Marina shutter installation. St. Petersburg compares shutter/blind/shade operation, sliding-door access, and fabric privacy. Service coverage, consultation policy, products, and in-house labor are already owner-confirmed.

The owner supplied only the hotel project for now: plantation shutters installed throughout ChartHouse Hotel Clearwater Beach Marina. Its official name and Clearwater Beach identity were cross-checked against [the hotel's website](https://charthousemarinahotel.com/). That website corroborates the property identity only; the installation scope comes from the owner. Material, room/window counts, installation date, outcomes, customer testimonial, and photo permissions for that project remain unknown. No hotel images, logo, or endorsement are used. The text feature states only the confirmed property, product, and scope.

The pages use existing gallery photos with descriptive alternatives; none is labeled a Largo, Clearwater, St. Petersburg, or ChartHouse installation. Additional real job stories and permitted city photos remain a prelaunch content improvement, particularly for St. Petersburg. All pages remain local review drafts with noindex and blocked crawling. No new office addresses or aggregate review ratings are asserted. General reviews remain identified as customer reviews, without city attribution.

Each city is discoverable from Service Areas and linked from the Pinellas community list. Visible breadcrumbs and BreadcrumbList match Home → Service areas → Pinellas County → City. Unique metadata, hero preloads, one shared Largo business entity, planned sitemap entries, and migration inventory rows are included. City estimate buttons reach Contact with a safe editable city prefill. The email-draft flow remains in place until GHL is supplied. These edits do not authorize publication, pushing, or deployment.

Verification for this city-page build: all 23 outputs passed `scripts/check.py` for nesting, headings, metadata, references, anchors, image attributes, schema, and sitemap coverage. The six changed public page outputs passed Customer Copy Guard with zero findings or review warnings, and were manually reviewed for unsupported city/project claims. `node --check scripts/contact.js` passed. All three city pages were checked at the normal 1652px desktop viewport and at 390px and 320px, with loaded hero images and no horizontal overflow; grids and FAQs collapse to one column on mobile. Keyboard FAQ expansion was verified on St. Petersburg. Each city's hero estimate link was followed to Contact and produced the correct editable city value with the other contact fields empty. Service Areas → Clearwater navigation and the ChartHouse section were verified in the browser. Temporary viewport overrides were reset. Screenshots are saved in `tmp/city-*-desktop.png` and `tmp/city-clearwater-project.png`. Nothing was pushed or deployed.
