const aliases = {
  "/home-7396": "/",
  "/home-7396/": "/",
  "/index.html": "/",
  "/plantation-shutters/": "/plantation-shutters",
  "/plantation-shutters/index.html": "/plantation-shutters",
  "/blinds/": "/blinds",
  "/blinds/index.html": "/blinds",
  "/shades/": "/shades",
  "/shades/index.html": "/shades",
  "/roller-shades/": "/roller-shades",
  "/roller-shades/index.html": "/roller-shades",
  "/horizontal-blinds/": "/horizontal-blinds",
  "/horizontal-blinds/index.html": "/horizontal-blinds",
  "/vertical-blinds/": "/vertical-blinds",
  "/vertical-blinds/index.html": "/vertical-blinds",
  "/solar-shades/": "/solar-shades",
  "/solar-shades/index.html": "/solar-shades",
  "/zebra-shades/": "/zebra-shades",
  "/zebra-shades/index.html": "/zebra-shades",
  "/cellular-shades/": "/cellular-shades",
  "/cellular-shades/index.html": "/cellular-shades",
  "/woven-wood-shades/": "/woven-wood-shades",
  "/woven-wood-shades/index.html": "/woven-wood-shades",
  "/motorized-shades/": "/motorized-shades",
  "/motorized-shades/index.html": "/motorized-shades",
  "/service-areas/": "/service-areas",
  "/service-areas/index.html": "/service-areas",
  "/Pinellas-window-treatments/": "/Pinellas-window-treatments",
  "/Pinellas-window-treatments/index.html": "/Pinellas-window-treatments",
  "/Hillsborough-window-treatments/": "/Hillsborough-window-treatments",
  "/Hillsborough-window-treatments/index.html": "/Hillsborough-window-treatments",
  "/service-areas/largo/": "/service-areas/largo",
  "/service-areas/largo/index.html": "/service-areas/largo",
  "/service-areas/clearwater/": "/service-areas/clearwater",
  "/service-areas/clearwater/index.html": "/service-areas/clearwater",
  "/service-areas/st-petersburg/": "/service-areas/st-petersburg",
  "/service-areas/st-petersburg/index.html": "/service-areas/st-petersburg",
  "/about-5day/": "/about-5day",
  "/about-5day/index.html": "/about-5day",
  "/gallary/": "/gallary",
  "/gallary/index.html": "/gallary",
  "/contact-5day/": "/contact-5day",
  "/contact-5day/index.html": "/contact-5day",
  "/privacy-policy/": "/privacy-policy",
  "/privacy-policy/index.html": "/privacy-policy",
  "/terms-and-conditions/": "/terms-and-conditions",
  "/terms-and-conditions/index.html": "/terms-and-conditions"
};

export default function (request) {
  const url = new URL(request.url);
  const target = aliases[url.pathname];
  if (!target || !["GET", "HEAD"].includes(request.method)) return;
  url.pathname = target;
  return Response.redirect(url, 301);
}
