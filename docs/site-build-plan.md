# 5 Day Plantation Shutters site build plan

Prepared October 1, 2026. This architecture and implementation plan for fivedayplantationshutters.com uses connected Semrush reports, the supplied September 30 desktop report, and the existing live pages. October 2 update: the owner authorized merging the completed 23-page rebuild to GitHub and publishing it on Netlify. This supersedes earlier local-only statements in the historical notes below. The Netlify review deployment remains noindex pending a separate custom-domain cutover; GHL remains a later connection, and separate Tampa pages stay on hold.

Preserve the homepage’s Tampa shutter visibility, build product depth under three clear categories, repair the existing county pages, and add city pages only when they can offer useful local evidence. The differentiator is the actual Largo manufacturing operation and documented installations, supported by straightforward product guidance.

**Current implementation:** all 20 core pages and three city page drafts are built locally, for 23 pages total. Product detail pages, the service-area hub, both county pages, About, Gallery, Contact and existing policies are complete as review drafts. The Contact form prepares an email draft until GHL is connected. Largo, Clearwater, and St. Petersburg have separate content and links from the coverage pages. City project photos and fuller installation stories remain outstanding. Nothing has been pushed or deployed.

**October 2 scope update:** the owner asked to hold off on a separate Tampa or Tampa plantation-shutters page. Keep the homepage's existing Tampa/Tampa Bay role. The Apollo Beach, Brandon, and Riverview source drafts are not registered in `scripts/build.py`, generated, linked, or included in the 23-page count; Hillsborough city selection remains unresolved. The Hillsborough county page is already built. Additional city and full project pages are optional expansion; core-page finishing still includes real project/team media, final product details, GHL delivery, and production migration setup. No new Tampa page, push, or deployment is authorized.

## Owner confirmed product information

Updated October 1 from the owner's follow-up. These facts supersede provisional product assumptions below.

- ShutterSMART is manufactured in-house. The locally offered louver sizes are 3 and 4 inches. The manufacturer describes this line as PolyClad Wood; do not describe it as solid PVC. Its broader catalog also lists SolidCore louver options, but those are not confirmed as locally offered. [Manufacturer reference](https://shuttersmart.com/our-shutters/shuttersmart/).
- The PVC/poly shutter line is confirmed as Elegant Window Fashions Broadleaf Poly, ordered from the manufacturer. Owner confirms 2.5, 3.5 and 4.5-inch louvers and painted/color-matched options. Final colors and custom-finish availability should be checked against the current ordering program. Elegant's Broadleaf page specifies aluminum reinforcement in louvers and stiles; use that component terminology rather than the earlier informal reference to rails.
- Hardwood shutters are confirmed as Elegant Window Fashions Chelsea Wood, ordered from the manufacturer and available painted or stained. Owner confirmed hardwood louver sizes of 3.5 and 4 inches on October 1; retain that local offering and verify against the final order sheet before launch. Use current Chelsea documentation for other specifications. Only the PolyClad line is manufactured in-house.
- Confirmed blinds: faux wood and vertical. Horizontal blinds is suitable terminology for the faux wood offering. The owner explicitly requested leaving real wood blinds off the site for now; aluminum blinds are not offered.
- Confirmed shades: roller, solar, zebra/layered, cellular/honeycomb, and woven wood. Cellular/honeycomb share one page; zebra/layered share one page. The owner explicitly requested leaving Roman shades off the site for now.
- Motorized, manual and cordless options are available across much of the shade range, with applicability varying by product. Do not claim every control is available on every product.
- Projects have been completed throughout Pinellas and Hillsborough counties. Specific project cities, photos and permissions still need collecting.
- Use fast turnaround without a fixed five-day completion promise. The business name does not establish a five-day delivery or installation guarantee.
- Measuring and installation are handled by the in-house team with no subcontractors. PolyClad shutters are manufactured in Largo; Broadleaf Poly and Chelsea Wood are supplier-made.
- Owner confirms a limited lifetime warranty on plantation shutters. Exact terms, exclusions, supplier-specific coverage and installation/labor coverage still need the applicable documents; do not expand this into an unconditional guarantee.
- Address confirmed: 1876 Lake Ave SE, Unit F, Largo, FL 33771. Customer visits are by appointment only. Do not advertise walk-ins or unconfirmed public opening hours.
- Phone confirmed: (813) 317-1077. Email confirmed: 5dayshutters@gmail.com.
- In-home consultations and measurements are free throughout Pinellas and Hillsborough counties, confirmed by the owner.
- Website estimate requests will eventually connect to the client's GoHighLevel account. Account/form details and lead notifications remain a pre-launch integration task. Do not simulate successful submissions or claim delivery before the integration is working and tested.
- Owner has installation photos and will supply them. City attribution and publication permissions remain to collect with the assets.

The requested A Shade Above reference was found in the local project and the chat titled “Repository · A Shade Above connection.” It supplied a manufacturer research lead. The owner has now independently confirmed Broadleaf Poly and Chelsea Wood for 5 Day. Manufacturer references checked October 1: [Broadleaf Poly](https://elegantwf.com/broadleaf-poly-shutters/), [Chelsea Wood](https://elegantwf.com/chelsea-wood-shutters/), and [warranty](https://elegantwf.com/review-warranty/). Do not transfer another client's branding, reviews, jobs or warranty promises.

## Evidence and limitations

Semrush reports were retrieved October 1 from the US desktop database. Organic Research keyword observations include August and September dates. These are modeled organic estimates, not Search Console results, real-time local searches, Maps rankings, or verified leads. No matching 5 Day project was present in the 14 projects returned by the connected account, so city/device Position Tracking and a project Site Audit were unavailable. No AI visibility measurement was performed.

The supplied September 30 PDF reports 50 keywords and an estimated eight monthly organic visits. Do not use eight as the business’s measured traffic. The latest connector reports and that PDF are separate snapshots.

| Keyword | Organic Research position | Landing page | Interpretation |
| --- | ---: | --- | --- |
| 5 day plantation shutters | 2 | / | Preserve brand homepage |
| plantation shutters tampa | 8 | / | Preserve homepage ownership of this cluster |
| tampa plantation shutters | 8 | / | Same commercial cluster, not another page |
| indoor shutters tampa | 9 | / | Supporting homepage terminology |
| plantation shutters in tampa | 12 | / | Improvement opportunity on existing page |
| window shutters tampa | 13 | / | Same shutter cluster |
| plantation shutters clearwater | 27 | / | Candidate for a useful Clearwater landing page |
| window treatments tampa | 51 | / | Broad commercial opportunity, secondary to shutters |

Source: [Semrush Organic Research](https://www.semrush.com/analytics/organic/positions/?db=us&q=fivedayplantationshutters.com) and saved [organic export](research/2026-10-01-5day-organic.csv).

The separate keyword SERP report places the homepage at 10 for “plantation shutters tampa,” versus 8 in Organic Research. Different report refreshes can disagree; this is not proof of a new drop. Use one consistent city/device tracking campaign plus Search Console to measure changes.

Repeated brand rows for About, Gallery, and the county page do not establish harmful cannibalization. Confirm problems from query-to-page history, URL switching, intent overlap, and leads before merging pages. Irrelevant Pennsylvania/Texas terms, competitor brands, and exterior shutter queries should not drive new content unless those are genuinely relevant services and markets.

## Local competitors and lessons

| Competitor | Semrush common keywords | Evidence and practical lesson |
| --- | ---: | --- |
| Sunburst Shutters Tampa | 12 | Tampa keyword SERP position 2; Clearwater city page position 1. Product types, specialty window applications, and local coverage are accessible through its navigation. Build product detail and authentic local project evidence. |
| IWS Shutters and Blinds | 12 | Tampa keyword SERP position 4; Clearwater city page position 3. Its Clearwater page connects shoppers to specific products and explains consultation and installation. Make our city pages useful shopping destinations. |
| Florida Shutters and Blinds | 11 | Tampa keyword SERP position 1. Clear shutters/blinds/shades/motorization categories and regional links. Keep the three primary categories the user selected. |
| shuttersandshades.com | 12 | Organic Research shows a dedicated Tampa window-shutters route for “shutter installation tampa.” Homepage fetch failed, so its current page content was not audited. Secondary keyword benchmark only. |

Common-keyword counts are from [Semrush Competitors](https://www.semrush.com/analytics/organic/competitors/?db=us&q=fivedayplantationshutters.com). SERP positions are from the separate phrase reports, not Maps positions. These domains are a research shortlist, not a definitive ranking of local businesses.

Page observations: [Sunburst](https://www.sunburstshutterstampa.com/), [Sunburst Clearwater](https://www.sunburstshutterstampa.com/communities/clearwater-2), [IWS Clearwater](https://www.iwsshuttersandblinds.com/clearwater-fl), [Florida Shutters and Blinds](https://flshuttersandblinds.com/). The lesson is the information architecture, not copying their text or producing every product/city combination.

Semrush also surfaced 5dayplantationshutters.com and 5dayplantationshuttersec.com. Their relationship to this client is unconfirmed. Do not redirect, merge, or treat them as independent competitors until ownership and affiliation are established.

## Keyword demand and priorities

Latest batch Keyword Overview estimates below are US monthly volumes for the literal city-qualified queries. They are not searches measured only inside those cities. Close variants overlap; do not sum them into a traffic forecast. Zero/missing data is not proof of no demand, and returned KD zero values should not be treated as assured easy wins.

| Query | Estimated monthly volume | Planning use |
| --- | ---: | --- |
| blinds tampa | 320 | Broad Blinds category opportunity |
| plantation shutters tampa | 260 | Protect and strengthen homepage |
| window treatments tampa | 170 | Secondary regional theme |
| motorized shades tampa | 40 | Candidate product page if actively sold |
| roller shades tampa | 30 | Improve existing page |
| plantation shutters clearwater | 30 | First expansion city candidate |
| plantation shutters brandon | 30 | Later city candidate if supported by jobs |
| plantation shutters riverview | 30 | Later city candidate if supported by jobs |
| plantation shutters st petersburg | 20 | First expansion city candidate |
| solar shades tampa | 20 | Distinct product intent |
| roman shades tampa | 20 | Distinct product intent |
| plantation shutters largo | 10 | Business base and manufacturing proof |
| cellular shades tampa | 10 | One cellular/honeycomb page |
| honeycomb shades tampa | 10 | Same product cluster, not another page |
| plantation shutters seminole | 10 | Evidence-led later expansion |
| plantation shutters palm harbor | 10 | Evidence-led later expansion |

Source: [saved keyword batch](research/2026-10-01-keywords.csv). “Window treatments largo” was omitted by the report; its volume is unknown. The Largo phrase SERP report returned no data. The Organic Research report has a different “window treatments tampa” volume; preserve that distinction rather than treating the reports as a time series.

## Proposed sitemap and keyword ownership

These are logical navigation relationships. Existing flat URLs can remain flat; moving pages into folders is not necessary for a clear hierarchy. New slugs remain provisional until the complete live URL inventory is checked.

| Page and proposed URL | Role and target intent | Action |
| --- | --- | --- |
| Home / | Brand, plantation shutters Tampa/Tampa Bay, regional introduction | Preserve URL and regional relevance; finish draft |
| /plantation-shutters | Detailed custom shutter selection, manufacturing, configuration, installation | Rebuild existing URL; do not duplicate homepage copy |
| /blinds | Compare available blind types; custom blinds Tampa Bay | New category hub if multiple meaningful types are offered |
| /horizontal-blinds | Faux wood horizontal/Venetian blinds | Rebuild existing URL; keep Venetian terminology here initially |
| /vertical-blinds | Vertical blinds for suitable windows and doors | New; confirmed product category, specifications pending |
| /shades | Compare shade types and light/privacy needs | New category hub |
| /roller-shades | Roller fabrics, opacity, mounting and controls | Rebuild existing URL |
| /solar-shades | Solar fabrics, openness, views and privacy tradeoffs | New if current range/specifications confirmed |
| /cellular-shades | Cellular/honeycomb construction and options | One new page for both names if confirmed |
| /zebra-shades | Layered/zebra fabric operation, privacy and light adjustment | New; one page for both names |
| /woven-wood-shades | Natural materials, weave, lining/privacy and controls | New; confirm available specifications |
| /motorized-shades | Controls, power, compatibility and service | Conditional new page; use a section first if offering is limited |
| /service-areas | Coverage overview and county navigation | New short, useful hub |
| /Pinellas-window-treatments | Pinellas coverage, projects and city navigation | Preserve exact URL/case; rewrite |
| /Hillsborough-window-treatments | Hillsborough coverage, consultation logistics and projects | Preserve exact URL/case; rewrite |
| /service-areas/largo | Local manufacturing and service in the business’s home city | New when evidence ready |
| /service-areas/clearwater | Clearwater shutters first; blinds/shades secondary | New when evidence ready |
| /service-areas/st-petersburg | St. Petersburg shutters and window treatments | New when evidence ready |
| /about-5day | People, factory, business story and verified credentials | Rebuild existing URL |
| /gallary | Real installation photography, product/city captions, project links | Keep existing spelling for migration; label navigation Gallery |
| /projects/descriptive-project-slug | A specific installation and its decisions/results | Add from real projects, not generic SEO topics |
| /contact-5day | Consultation form, contact details, visit arrangements | Rebuild and connect working lead delivery |
| /privacy-policy and /terms-and-conditions | Existing policies and necessary updates for final integrations | Preserve routes and review content |

Do not create a separate Tampa plantation-shutters landing page in the first release. The homepage already owns that search cluster. The Hillsborough page serves county coverage and other communities. Revisit Tampa-specific expansion only if Search Console and real customer needs justify a distinct destination.

The Blinds hub now compares the confirmed faux wood and vertical offerings and links to their separate detail pages. Zebra/layered and cellular/honeycomb each share one detail page under Shades. Repair, commercial, real wood/aluminum blinds, Roman shades and separate shutter-material routes are not added without confirmed services and a distinct buyer need.

Navigation: Products → Plantation Shutters, Blinds, Shades; About Us; Gallery; Service Areas. Keep estimate and phone actions. Blinds/Shades hubs link to their actual subtypes. City pages link to relevant product pages and examples; product pages link to selected installations and the coverage hub. Breadcrumbs reflect the hierarchy even with existing flat URLs.

## Product page structures

Reuse the approved visual design, header, footer, typography, review treatment, and mobile controls. Share layouts through build-time templates/partials while serving complete static HTML. Avoid hand-copying the header into many files where links can drift.

**Category hubs:** a concise product-specific hero and estimate CTA; sourced reviews below it; comparison cards/table showing actual types; room/light/privacy selection guidance; a few real installations; links to product details; short FAQs and final CTA. Blinds and Shades must explain differences rather than repeat every child page.

**Product detail pages:**

1. Product-specific H1, actual product image, short benefit statement and estimate CTA.
2. Relevant real reviews directly below the hero. Do not label a review as shade/blind-specific without evidence.
3. What the product is, who it suits, and practical limitations.
4. Available configurations with close-up photos and verified specifications.
5. Real installations and customer decisions; link to full projects where useful.
6. Selection, measuring and installation explained plainly, without the decorative numbered-process treatment the user rejected.
7. Price factors, confirmed lead-time information, warranty/support terms and what is included.
8. Product-specific FAQs, appropriate service links, and estimate CTA/form.

| Product | Distinct information needed from the business |
| --- | --- |
| Plantation shutters | Actual materials, louver sizes, frames, tilt controls, divider/split options, specialty shapes, sliding-door capability, what is manufactured in Largo, written warranty |
| Horizontal blinds | Available faux wood products, slat sizes, finishes, controls, mounting and suitable rooms |
| Vertical blinds | Vane materials and widths, track/stack choices, controls and door access |
| Roller shades | Fabric types, light-filtering versus blackout options, side-gap limitations, valances/cassettes and controls |
| Solar shades | Available openness factors, glare/view tradeoffs, product-backed UV data, daytime versus nighttime privacy limitations |
| Cellular shades | Cell styles, opacity, top-down/bottom-up availability, controls and supported performance claims |
| Zebra shades | Alternating fabric layers, privacy limitations, alignment, fabrics and controls |
| Woven wood shades | Actual materials, weave, lining/privacy options, finishes and controls |
| Motorized shades | Rechargeable motors confirmed; verify exact brand/model, remote/app compatibility, charging instructions and support |

Do not infer technical specifications or quantified savings from competitors. Local manufacturing claims apply only to hybrid shutters. Treat the name “5 Day” separately from a guaranteed five-day completion promise.

## Location pages that earn their place

A shared layout is fine. The unique value should come from real service evidence and helpful local details, not rewording or swapping city names. Google's [doorway guidance](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse) addresses substantially similar pages designed primarily to funnel search visitors elsewhere.

Our editorial publication gate, not a Google numerical requirement: a confirmed service area, at least one substantive local project or equivalent first-hand evidence, and practical information that makes the page useful on its own. Aim for several authentic images and a detailed project explanation. If evidence is absent, cover the city on the county page first.

**City page order:** city-specific service statement and estimate CTA → relevant review(s) with verified attribution → featured local installation → locally relevant product choices linked to main product pages → consultation/installation logistics → additional evidence and local FAQs → estimate form/call action. A visitor should be able to decide and inquire on the page itself.

| Page | Distinct evidence and possible angle | What must not be invented |
| --- | --- | --- |
| Largo | Actual factory/team photos, how a shutter is made, a nearby installation, accurate visit/appointment instructions | Public showroom access or walk-in hours |
| Clearwater | A real condo or home installation demonstrating privacy, views, slider access or room-by-room choices | Condo projects, resident testimonials, building rules or coastal performance |
| St. Petersburg | A documented home with an unusual window shape, depth, trim or privacy constraint and how it was solved | Historic-home expertise or specific neighborhoods served without evidence |
| Brandon or Riverview | A real whole-home/new-build project showing coordinated products and scheduling decisions | New-build specialization, completion times or project costs |
| Seminole, Dunedin, Palm Harbor and other communities | Select later pages using confirmed jobs, lead value, demand and Search Console impressions | City lists turned automatically into pages |

These are proposed angles to substantiate, not claims about jobs already completed. The same local problem can occur in several cities; uniqueness comes from the actual installation, photos, measurements, choices and outcome. Avoid padding pages with tourism/history paragraphs or arbitrary word-count targets.

For each project collect city (not the homeowner's street address), approved photos, product, window/door type, customer goal, installation constraint, chosen solution, completion month, factual result, and permission to feature it. Add an authentic review only when available. Never attach an unverified city to the reviews already supplied.

Use the actual Largo business address and one consistent business identity. City pages describe service coverage; they are not additional offices. City content can support organic relevance, but it cannot remove Google's distance factor in Maps. See [Google local ranking guidance](https://support.google.com/business/answer/7091).

## Cleanup and ranking protection

The [Pinellas](https://fivedayplantationshutters.com/Pinellas-window-treatments) and [Hillsborough](https://fivedayplantationshutters.com/Hillsborough-window-treatments) pages contain unrelated roofing copy. The [shutter](https://fivedayplantationshutters.com/plantation-shutters) page's review introduction also references roofing, and the [horizontal blinds](https://fivedayplantationshutters.com/horizontal-blinds) page repeats roofing service cards. Replace these during migration.

The live homepage also references Fort Myers. The user has confirmed Largo; other facilities, experience claims, turnaround, in-house labor, guarantees and warranty terms need business confirmation before reuse. Distinguish outdated copy from verified business facts.

Before launch, inventory all live URLs from crawl, sitemap, Search Console and backlinks. The web tool could not retrieve /sitemap.xml; this is not proof the sitemap is absent or broken. Preserve valuable paths and useful content. Determine the role of /home-7396; if it is a duplicate homepage with no distinct purpose, configure a direct server-side 301 to /. Keep the root canonical. Do not bulk-redirect valid service pages to the homepage.

Build a mapping with old URL, response/canonical, queries, links, leads, action, destination and rationale. For genuine competing pages, prefer the stronger relevant destination using Search Console history, conversions and backlinks; merge useful material and redirect only when justified. No mass consolidation is supported by the current branded ranking rows.

## SEO and AI implementation

Write clear answer-first explanations with visible specifications, comparison tables, useful FAQs, real project captions and a named business/team responsible for the information. Keep main content and links in initial HTML. Ensure descriptive titles, one clear page H1, logical sections, image alternatives, self-canonicals for distinct pages and an accurate XML sitemap.

Represent one real business with consistent contact details and a stable entity identifier; use relevant LocalBusiness/Organization data and BreadcrumbList, with markup matching visible facts. Do not manufacture review counts, city addresses, product prices, or rich-result eligibility. Do not use self-serving business review markup to seek stars. [Google LocalBusiness documentation](https://developers.google.com/search/docs/appearance/structured-data/local-business).

FAQs are for users and clear answers, not a promised FAQ rich result. Google states that AI Overviews/AI Mode do not need special AI files or special schema. Strong crawlable content and accurate business information are the foundation; no AI citation or ranking is guaranteed. [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features).

Keep GBP name, primary category, accurate additional categories, address/service-area settings, hours, products, photos and website aligned with the verified business. Confirm the exact category labels in GBP; do not add unrelated categories to broaden reach. Keep the Largo address truthful while describing Tampa Bay service coverage.

## Build sequence and completion criteria

| Stage | Deliverables | Completion criteria |
| --- | --- | --- |
| 1. Establish migration baseline | Full URL inventory, Search Console query/page export, analytics/lead baseline, confirmed product list and business facts | Every existing important URL has an action; major claims approved |
| 2. Build reusable static layouts | Product hub/detail, county/city, About, Gallery/project, Contact layouts using approved design | Complete HTML, responsive/keyboard-friendly, working internal navigation; no design regression |
| 3. Rebuild essential pages | Existing 3 product pages, useful Blinds/Shades hubs, 2 county pages, service-area hub, About, Gallery, Contact and legal routes | Accurate copy and real assets; no roofing leftovers; no unfinished destination links |
| 4. Add distinct content | Confirmed shade subtypes and strongest supported Largo/Clearwater/St. Petersburg pages and project stories | Each page has unique purpose, product details or local proof; no filler placeholders |
| 5. Test conversion and launch setup | Contact validation/success/error handling, spam protection, actual lead delivery, phone links, analytics, redirects, canonicals, sitemap, robots, metadata, image performance | No broken routes; forms reach intended recipient; draft noindex remains until an authorized launch |
| 6. Measure and expand | City/device rank baseline, Maps baseline where available, Search Console landing pages, qualified leads by product/city | Check migration errors immediately; compare at 2, 4 and 8 weeks; expand from evidence |

The current local draft includes 23 pages: all 20 core pages plus Largo, Clearwater, and St. Petersburg. The October 2 audit fixes add clearer product comparisons, stronger confirmed manufacturing and project evidence, mobile-first form order, consistent communication wording, canonical internal links, and social-image metadata. The implementation and remaining-input checklist is in `docs/launch-checklist.md`. Robots meta remains intentionally noindex,nofollow, and robots.txt blocks crawling. The planned sitemap and URL migration inventory are generated, but production redirects and GHL delivery are not connected. Separate Tampa pages remain on hold; Apollo Beach, Brandon, and Riverview are unregistered sources only. This plan does not schedule monitoring or authorize a deployment.

Track phone-link clicks separately from completed calls and form starts separately from successful submissions. Keep city/device tracking consistent. Compare nonbrand clicks, query/page stability, qualified inquiries and sales; do not treat keyword count or modelled traffic alone as success. Record observed AI citations separately if later testing actual platforms.

## Inputs needed to finish

- Core product types and shutter collections are confirmed; enough information is available to begin the product-page build. Obtain detailed control options and applicable written warranties before publishing detailed claims. Keep turnaround qualitative and do not add a repair-service page without confirmation.
- Provide approved project photos with city and short job notes, factory/team photos, and permission to use them. The supplied reviews can be retained, but no city attribution should be guessed.
- Main contact details, appointment-only visits and coverage in both counties are confirmed. Any Fort Myers connection and ownership of similarly named domains remain unresolved and should not be assumed.
- Supply Search Console query/page history and current conversion reporting. Connect the client's GoHighLevel account and confirm notification recipients before launch. Access/export scope should stay with this client.
- Confirm production hosting and redirect support when implementation reaches launch preparation. Publishing remains a separate decision.

Next priority: review the completed pages, collect city/project attribution, and connect/test GHL when supplied. The business start year is unconfirmed and omitted. The owner described the rechargeable motor brand as “Rolie's”; verify the spelling and exact model before publishing branded specifications. The owner authorized migration of the existing policies, which is complete with the Unit F address and formatting corrections. Align their communications clauses with the final GHL consent flow before launch.

## Customer-facing shutter names — October 1 correction

Use **Hybrid Plantation Shutters**, **PVC Plantation Shutters**, and **Hardwood Plantation Shutters** throughout visible copy, metadata and future pages. Hybrid is our plain-language category label for the locally manufactured ShutterSmart line; explain its wood structure and protective vinyl surface. Do not call it MDF/composite or solid PVC. PolyClad, ShutterSmart, Broadleaf, Chelsea and Elegant remain internal product-source references only. The earlier build used supplier names publicly; that has been corrected.

Confirmed louver sizes: hybrid 3 and 4 inches; PVC 2.5, 3.5 and 4.5 inches; hardwood 3.5 and 4 inches (latest owner confirmation). Do not silently change hardwood 4 to 4.5. Exact finish availability and written warranty terms still require the ordering documents.

## Expanded city demand check — October 1

At the owner's request, rechecked the existing county city/community lists and a wider city-qualified keyword batch through connected Semrush Keyword Analytics (`phrase_these`, US database). Source: [saved batch](research/2026-10-01-city-demand.csv). The full county lists are now visible on the two county pages; those communities are coverage, not extra offices.

Volumes below are modeled US monthly searches for the literal phrases, not actual traffic, city-resident counts, Maps rankings, or lead forecasts. Similar variants overlap and must not be summed. Returned zero KD values do not establish easy rankings. Missing terms have unknown volume, not zero. County queries can still serve useful navigation even when the tool returns little volume.

| City / community | Sample phrase | Volume | Page decision |
| --- | --- | ---: | --- |
| Tampa | plantation shutters tampa | 260 | Keep ownership on homepage; blinds tampa also 320 and window treatments tampa 170 |
| Clearwater | plantation shutters clearwater | 30 | First city candidate; existing homepage observation at position 27 provides a relevant baseline |
| St. Petersburg | plantation shutters st petersburg / blinds st petersburg | 20 / 70 | First city candidate with a broader shutter/blind choice, supported by an actual job |
| Largo | plantation shutters largo | 10 | Strong business evidence: physical address, manufacturing, appointment visit; add verified local photos |
| Apollo Beach | plantation shutters apollo beach | 40 | High Hillsborough expansion candidate once a useful local project is available |
| Brandon | plantation shutters brandon | 30 | Project-led Hillsborough candidate |
| Riverview | plantation shutters riverview | 30 | Project-led Hillsborough candidate |
| Valrico | plantation shutters valrico | 30 | Project-led Hillsborough candidate |
| Lithia | plantation shutters lithia | 30 | Project-led Hillsborough candidate |
| Temple Terrace | plantation shutters temple terrace | 20 | Later candidate, compare evidence and actual leads |
| Lutz | plantation shutters lutz | 20 | Limit coverage claims to the confirmed Hillsborough area |
| Sun City Center | plantation shutters sun city center | 20 | Later candidate with confirmed local evidence |
| Seminole, Palm Harbor, Tarpon Springs, Safety Harbor, Belleair | plantation shutters + community | 10 each | Cover now on Pinellas page; add a distinct page when supported |
| Carrollwood, Westchase, Ruskin | plantation shutters + community | 10 each | Cover now on Hillsborough page; prioritize using actual jobs and leads |

There is no Google-prescribed city-page count. The practical first expansion is Largo, Clearwater and St. Petersburg, followed by whichever of Apollo Beach, Brandon, Riverview, Valrico or Lithia has the strongest project evidence. This is a planning judgment from demand, current rankings and the business's physical base, not an asserted algorithm requirement. Google's [doorway policy](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse) supports avoiding substantially similar regional pages that merely funnel visitors elsewhere.

Each future city page should have a local installation story, useful photos and decisions, verified service logistics, appropriate product links and its own inquiry action. Do not invent an office, city-specific testimonial, neighborhood expertise, special price, or completion date. A city listed on the county page is already covered even if it never gets a separate URL.

## First three city page drafts — October 1

The owner authorized building the first three city pages. Routes: `/service-areas/largo`, `/service-areas/clearwater`, and `/service-areas/st-petersburg`. Largo covers the actual business location, locally manufactured hybrid shutters, appointment visits, and material selection. Clearwater focuses on shutter finish/louver/panel decisions, condo requirements supplied by the customer, privacy, and the owner-confirmed ChartHouse Hotel Clearwater Beach Marina shutter installation. St. Petersburg compares shutter/blind/shade operation, sliding-door access, and fabric privacy. Service coverage, consultation policy, products, and in-house labor are already owner-confirmed.

The owner supplied only the hotel project for now: plantation shutters installed throughout ChartHouse Hotel Clearwater Beach Marina. Its official name and Clearwater Beach identity were cross-checked against [the hotel's website](https://charthousemarinahotel.com/). That website corroborates the property identity only; the installation scope comes from the owner. Material, room/window counts, installation date, outcomes, customer testimonial, and photo permissions for that project remain unknown. No hotel images, logo, or endorsement are used. The text feature states only the confirmed property, product, and scope.

The pages use existing gallery photos with descriptive alternatives; none is labeled a Largo, Clearwater, St. Petersburg, or ChartHouse installation. Additional real job stories and permitted city photos remain a prelaunch content improvement, particularly for St. Petersburg. All pages remain local review drafts with noindex and blocked crawling. No new office addresses or aggregate review ratings are asserted. General reviews remain identified as customer reviews, without city attribution.

Each city is discoverable from Service Areas and linked from the Pinellas community list. Visible breadcrumbs and BreadcrumbList match Home → Service areas → Pinellas County → City. Unique metadata, hero preloads, one shared Largo business entity, planned sitemap entries, and migration inventory rows are included. City estimate buttons reach Contact with a safe editable city prefill. The email-draft flow remains in place until GHL is supplied. These edits do not authorize publication, pushing, or deployment.
