"""Generate CTIT's eleven editable HTML pages, using only Python's standard library.

Run this after editing shared copy or components, then restart app.py.
Individual HTML files in templates/ may also be edited directly.
"""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
COMPANY = 'Connecting Tomorrow IT Solutions GmbH'
EMAIL = 'support@connectingtomorrowit.com'
PHONE = '+49 160 8306949'

ICONS = {
    'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    'diagonal': '<path d="M6 18 18 6M6 6h12v12"/>',
    'chevron': '<path d="m7 10 5 5 5-5"/>',
    'server': '<rect x="4" y="3" width="16" height="7" rx="2"/><rect x="4" y="14" width="16" height="7" rx="2"/><path d="M8 6.5h.01M8 17.5h.01M12 6.5h5M12 17.5h5"/>',
    'headset': '<path d="M4 14v-3a8 8 0 0 1 16 0v6a4 4 0 0 1-4 4h-3"/><rect x="2" y="11" width="5" height="8" rx="2"/><rect x="17" y="11" width="5" height="8" rx="2"/>',
    'network': '<rect x="8" y="2" width="8" height="6" rx="1"/><rect x="2" y="16" width="7" height="6" rx="1"/><rect x="15" y="16" width="7" height="6" rx="1"/><path d="M12 8v4M5.5 16v-4h13v4"/>',
    'move': '<path d="M12 3v18M3 12h18m-12-6 3-3 3 3M9 18l3 3 3-3M6 9l-3 3 3 3m12-6 3 3-3 3"/>',
    'tool': '<path d="M14.5 6.5a5 5 0 0 1 6-4l-3.2 3.2 1 3 3-3.2a5 5 0 0 1-6 6L7 20a2 2 0 0 1-3-3l8.5-8.5a5 5 0 0 1 2-2Z"/>',
    'cable': '<path d="M5 2v4M9 2v4M15 18v4M19 18v4M3 6h8v3a4 4 0 0 1-8 0V6Zm10 9a4 4 0 0 1 8 0v3h-8v-3ZM7 13v2a3 3 0 0 0 6 0"/>',
    'code': '<path d="m8 6-6 6 6 6m8-12 6 6-6 6M14 3l-4 18"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18M5 6h14M5 18h14"/>',
    'check': '<path d="m5 12 4 4L19 6"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'phone': '<path d="M7 3H4a1 1 0 0 0-1 1c0 9.4 7.6 17 17 17a1 1 0 0 0 1-1v-3l-5-2-2 2a14 14 0 0 1-7-7l2-2-2-5Z"/>',
    'people': '<circle cx="9" cy="7" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m3 11v-3a6 6 0 0 0-2-4"/>',
    'shield': '<path d="m12 2 8 4v6c0 6-8 10-8 10S4 18 4 12V6l8-4Z"/><path d="m8 12 3 3 5-6"/>',
}


def icon(name, classes=''):
    return f'<svg class="icon {classes}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


def link(label, href, style='text-link', arrow='arrow'):
    return f'<a class="{style}" href="{href}">{label}{icon(arrow)}</a>'


def image(name, alt, classes='', eager=False):
    return f'<img class="{classes}" src="/static/images/{name}.webp" alt="{escape(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async">'


SERVICES = [
    {
        'slug': 'data-center-support-dc-sla', 'name': 'Data center support', 'short': 'Data centers', 'icon': 'server', 'category': 'BUSINESS-CRITICAL INFRASTRUCTURE', 'photo': 'data-center',
        'title': 'Always connected.<br><em>Always supported.</em>',
        'intro': 'Keep your critical infrastructure moving with skilled hands on site, planned maintenance and support built around your service requirements.',
        'summary': 'Expert hands for the infrastructure your business depends on.',
        'heading': 'Your infrastructure.<br>In capable hands.',
        'body': 'From a single component replacement to a coordinated deployment, we support the complete lifecycle of your data center hardware. Our multi-vendor approach brings the right technical expertise to your environment.',
        'bullets': ['On-site smart hands and remote assistance', 'Planned and reactive maintenance', 'Service delivery aligned to an agreed SLA'],
        'capabilities': [('Smart hands & eyes', 'On-site inspections, diagnostics and remote-guided tasks performed by experienced field engineers.'), ('Hardware maintenance', 'Component replacements, device swaps and RMA coordination across multi-vendor environments.'), ('Deployments & upgrades', 'Rack installations, equipment commissioning, firmware changes and planned hardware refreshes.'), ('Ongoing site support', 'Ticket-based assistance and longer-term on-site resources, tailored to your operational needs.')],
        'faq': [('Can you support more than one hardware vendor?', 'Yes. CTIT provides multi-vendor hardware support. Share your equipment inventory and location so we can confirm the technical coverage available.'), ('What service levels are available?', 'Response windows, operating hours, access requirements and escalation paths are agreed during scoping. Availability depends on location and the required service.'), ('Do you provide ongoing support?', 'We support individual tasks, scheduled projects and ongoing maintenance arrangements. We will help define an approach that fits your environment.')],
    },
    {
        'slug': 'it-support-24-7-service-desk', 'name': '24/7 IT support', 'short': '24/7 support', 'icon': 'headset', 'category': 'SUPPORT THAT GOES THE DISTANCE', 'photo': 'service-desk',
        'title': 'Business never stops.<br><em>Neither should support.</em>',
        'intro': 'Connect your teams with technical assistance around the clock. One coordinated approach to incidents, escalation and on-site support.',
        'summary': 'Around-the-clock assistance, wherever your teams work.',
        'heading': 'People first.<br>Problems resolved.',
        'body': 'Your teams need a clear path from a technical issue to the right expertise. We bring service coordination, remote assistance and field resources together to help keep work moving across time zones.',
        'bullets': ['Round-the-clock support arrangements', 'Clear escalation and communication', 'Remote assistance and on-site coordination'],
        'capabilities': [('Incident coordination', 'An agreed point of contact to capture issues, coordinate resources and track the next action.'), ('Remote assistance', 'Technical help for users, devices and everyday IT operations within your agreed scope.'), ('Field dispatch', 'When an issue needs someone on site, we coordinate the right skills and confirm local availability.'), ('Service continuity', 'Structured handovers, escalation paths and updates to keep your stakeholders informed.')],
        'faq': [('Is support available outside normal business hours?', 'Yes. We can arrange 24/7 support. The service scope, contact channels and response expectations are defined in your support agreement.'), ('Can remote support become an on-site visit?', 'Yes, when needed and within the agreed service scope. We confirm engineer availability, site access and timing before dispatch.'), ('How do we start a support arrangement?', 'Send your locations, device types, working hours and preferred response requirements. We will discuss a suitable support model.')],
    },
    {
        'slug': 'windows-migration-windows-roll-out', 'name': 'Rollout & migration', 'short': 'Rollout & migration', 'icon': 'network', 'category': 'CHANGE WITHOUT THE COMPLEXITY', 'photo': 'workplace',
        'title': 'Move forward.<br><em>Keep business moving.</em>',
        'intro': 'Bring new technology into your business with carefully planned rollouts, operating system upgrades and coordinated migration support.',
        'summary': 'Coordinated technology changes, from pilot to final handover.',
        'heading': 'A clear plan.<br>A smoother transition.',
        'body': 'Technology refreshes involve people, devices, data and deadlines. We help coordinate those moving parts, from readiness checks and deployment planning to installation, migration and handover.',
        'bullets': ['Site readiness and deployment planning', 'Device imaging and system rollout', 'Data migration and user handover'],
        'capabilities': [('Readiness & planning', 'Assess the current environment, confirm dependencies and agree the sequence of change.'), ('System deployment', 'Prepare images, configure devices and coordinate installations across your selected sites.'), ('Migration assistance', 'Support operating system changes, application transitions and controlled data transfers.'), ('Validation & handover', 'Check the deployed environment, document the work and help users transition into their new setup.')],
        'faq': [('Can a rollout cover several sites?', 'Yes. We coordinate multi-site projects around a shared plan, with local engineering support subject to availability.'), ('Can work be scheduled outside office hours?', 'Scheduling is agreed during planning. Share your preferred maintenance windows and operational constraints.'), ('Will you help with data migration?', 'Yes. We define the migration scope, backup responsibilities, validation checks and handover requirements with you before work begins.')],
    },
    {
        'slug': 'hardware-break-fix', 'name': 'Hardware & network break fix', 'short': 'Hardware break fix', 'icon': 'tool', 'category': 'GET BACK TO BUSINESS', 'photo': 'hardware',
        'title': 'When hardware fails,<br><em>we step in.</em>',
        'intro': 'Practical, on-site support for enterprise hardware and networks. Get the right expertise to diagnose issues and coordinate repairs.',
        'summary': 'Skilled diagnostics and repairs that help restore your operations.',
        'heading': 'The right skills.<br>Right where you need them.',
        'body': 'A failed component can interrupt an entire business process. Our field support helps you diagnose hardware and network faults, replace components and verify the system before returning it to service.',
        'bullets': ['Multi-vendor hardware diagnostics', 'Component replacement and device swaps', 'Network troubleshooting and recovery checks'],
        'capabilities': [('Fault diagnosis', 'On-site investigation of servers, workstations and network equipment to identify the next action.'), ('Repair & replacement', 'Skilled component swaps and hardware repairs, coordinated with your parts and warranty arrangements.'), ('Network troubleshooting', 'Investigate physical connections, device status and network hardware issues within the agreed scope.'), ('Return to service', 'Post-repair checks and clear service reporting to support your operational handover.')],
        'faq': [('Which equipment can you support?', 'We work across major enterprise hardware and network vendors. Send the make, model and issue description so we can confirm the right skills.'), ('Are replacement parts included?', 'Parts sourcing and responsibility are agreed for each service. Please share warranty status and any available spares when raising a request.'), ('How quickly can an engineer attend?', 'Timing depends on the location, access arrangements, technical skills and the agreed SLA. Contact us to confirm availability for your site.')],
    },
    {
        'slug': 'imac', 'name': 'Install, move, add & change', 'short': 'IMAC services', 'icon': 'move', 'category': 'WORKPLACES READY FOR WHAT’S NEXT', 'photo': 'field-engineer',
        'title': 'New space.<br><em>Same momentum.</em>',
        'intro': 'From one desk to an entire office, our IMAC services help your people, devices and workspaces adapt as your business changes.',
        'summary': 'Install, move, add and change your workplace technology.',
        'heading': 'Business changes.<br>We help IT keep up.',
        'body': 'An office move or team expansion should bring possibilities. We help plan, install, relocate and reconfigure workplace technology, with an emphasis on coordination and a clear handover.',
        'bullets': ['Workstation and peripheral installations', 'Office and equipment relocations', 'Moves, additions and configuration changes'],
        'capabilities': [('Install', 'Set up workstations, peripherals and connectivity so new spaces are ready for your people.'), ('Move', 'Plan and execute equipment relocations with asset tracking and careful handling.'), ('Add', 'Expand your workplace technology to support new colleagues, locations or business requirements.'), ('Change', 'Update configurations, replace equipment and coordinate agreed changes to your existing setup.')],
        'faq': [('What does IMAC stand for?', 'Install, Move, Add and Change. It covers the everyday and project-based changes needed to keep workplace technology aligned with your business.'), ('Can you coordinate an office relocation?', 'Yes. We help scope the equipment, site readiness, move schedule and installation requirements, then agree the delivery responsibilities.'), ('Do you support small changes as well as larger projects?', 'Yes. We can discuss individual tasks, coordinated site visits and larger multi-location projects.')],
    },
    {
        'slug': 'fiber-copper-communication-cabling', 'name': 'Fiber & copper cabling', 'short': 'Fiber & copper cabling', 'icon': 'cable', 'category': 'THE FOUNDATION OF CONNECTION', 'photo': 'network-cabling',
        'title': 'Better connections.<br><em>From the ground up.</em>',
        'intro': 'Build a reliable physical network with structured fiber and copper cabling, installation support and a well-organized infrastructure.',
        'summary': 'A strong physical foundation for your connected business.',
        'heading': 'Reliable networks<br>start with the details.',
        'body': 'Your network is only as strong as the connections behind it. We help plan and deliver structured cabling for offices and technical environments, with organized installation, labeling and handover.',
        'bullets': ['Structured copper and fiber installation', 'Patching, labeling and cable management', 'Site surveys and connectivity checks'],
        'capabilities': [('Site assessment', 'Review the space, routes and connectivity requirements before work begins.'), ('Copper infrastructure', 'Install and organize copper cabling to support your agreed network design and endpoint needs.'), ('Fiber connectivity', 'Coordinate fiber runs, termination requirements and patching for your infrastructure.'), ('Testing & documentation', 'Perform agreed connectivity checks, label connections and document the installation for handover.')],
        'faq': [('Do you work with both fiber and copper?', 'Yes. We scope the installation around the physical environment, network design and agreed technical requirements.'), ('Can you improve an existing cabling installation?', 'Yes. We can review existing cabling, discuss labeling and cable management, and scope repair or expansion work.'), ('Can you provide an initial site survey?', 'Yes. A site survey helps confirm access, cable routes, quantities and the practical requirements for installation.')],
    },
]

SOFTWARE = {
    'slug': 'software-development', 'name': 'Software development', 'short': 'Software development', 'icon': 'code', 'category': 'IDEAS INTO EVERYDAY IMPACT', 'photo': 'software',
    'title': 'Built for your business.<br><em>Ready for tomorrow.</em>',
    'intro': 'Turn complex business needs into intuitive digital experiences. Custom software, web platforms and mobile applications, built around you.',
    'summary': 'Purpose-built software that connects your people and processes.',
    'heading': 'Your ambition.<br>Our engineering.',
    'body': 'Your business has its own processes and priorities. We build software to fit them: web platforms, mobile applications and business systems that bring your ideas into everyday use.',
    'bullets': ['Custom web and business applications', 'Mobile experiences and online platforms', 'Modernization, integrations and ongoing care'],
    'capabilities': [('Custom business systems', 'ERP, accounting, inventory, HR and workflow applications shaped around your operational needs.'), ('Web platforms', 'Responsive websites, online stores and scalable portals with thoughtful design and practical functionality.'), ('Mobile applications', 'User-focused mobile experiences that connect your teams and customers with the services they need.'), ('Industry applications', 'Tailored systems for healthcare, education, hospitality, retail and other specialist workflows.'), ('Integration & modernization', 'Connect existing tools, improve data flows and evolve applications as your business grows.'), ('Testing & ongoing care', 'Quality assurance, bug fixes and maintenance scoped around the software we deliver.')],
    'faq': [('Can you build software for our specific workflows?', 'Yes. We begin with discovery to understand your users, processes, integrations and business priorities before proposing an approach.'), ('What technologies do you use?', 'Our capabilities include .NET, SQL Server, MongoDB, Angular, Node.js and web frameworks. We select the stack based on the requirements, existing systems and long-term maintenance needs.'), ('Can you maintain an existing application?', 'We can assess the existing codebase and requirements, then agree a suitable maintenance or modernization scope.')],
}


def brand():
    return '<a class="brand" href="/" aria-label="CTIT — Connecting Tomorrow IT home"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span><span class="brand-word">CTIT<small>CONNECTING TOMORROW IT</small></span></a>'


def header(active):
    items = ''.join(f'<a href="/{s["slug"]}/">{icon(s["icon"])}<span>{s["name"]}</span>{icon("arrow")}</a>' for s in SERVICES)
    def current(key):
        return ' aria-current="page"' if active == key else ''
    return f'''<div class="utility-bar"><div class="container utility-inner"><span>GERMAN ROOTS. GLOBAL REACH.</span><a href="tel:+491608306949"><span class="status-dot"></span>24/7 support<span class="utility-phone">&nbsp; · &nbsp; {PHONE}</span></a></div></div>
<header class="site-header"><div class="container header-inner">{brand()}
<button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="main-navigation" aria-expanded="false"><span></span><span></span></button>
<nav id="main-navigation" class="navigation" aria-label="Main navigation">
<a href="/about-us/"{current('about-us')}>Company</a>
<details class="nav-dropdown"><summary{' class="active"' if active in ['services'] + [s['slug'] for s in SERVICES] else ''}>IT services{icon('chevron')}</summary><div class="mega-menu"><div class="mega-heading"><span>IT expertise, wherever you need it.</span><a href="/services/">All services {icon('arrow')}</a></div><div class="mega-grid">{items}</div></div></details>
<a href="/software-development/"{current('software-development')}>Software development</a>
<a href="/about-us/#coverage">Global coverage</a>
{link('Let’s talk', '/kontakt/', 'button button-dark', 'diagonal')}
</nav></div></header>'''


def footer():
    return f'''<footer class="site-footer"><div class="container"><div class="footer-top"><div class="footer-brand">{brand()}<p>Connecting people. Supporting business.<br>Building tomorrow, together.</p><span class="footer-location">{icon('pin')}Germany · Worldwide delivery</span></div>
<div class="footer-links"><p class="footer-label">EXPERTISE</p>{''.join(f'<a href="/{s["slug"]}/">{s["short"]}</a>' for s in SERVICES[:4])}</div>
<div class="footer-links"><p class="footer-label">EXPLORE</p><a href="/about-us/">Our company</a><a href="/services/">All IT services</a><a href="/software-development/">Software development</a><a href="/about-us/#coverage">Global coverage</a><a href="/kontakt/">Contact us</a></div>
<div class="footer-contact"><p class="footer-label">LET’S CONNECT</p><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:+491608306949">{PHONE}</a><p>Tell us where you want to go.<br>We’ll help you get there.</p></div></div>
<div class="footer-bottom"><span>© <span data-current-year>2026</span> {COMPANY}</span><span>Designed for a connected world.</span><a href="#top">Back to top ↑</a></div></div></footer>'''


def cta():
    return f'''<section class="cta-section"><div class="container"><div class="cta-panel"><div><p class="eyebrow">LET’S BUILD WHAT’S NEXT</p><h2>Your next chapter.<br>Our next connection.</h2><p>Tell us what your business needs. We’ll bring the right expertise.</p></div>{link('Start a conversation', '/kontakt/', 'button button-light', 'diagonal')}<span class="cta-orbit" aria-hidden="true"></span></div></div></section>'''


def document(slug, title, description, body):
    canonical = 'https://www.connectingtomorrowit.com/' + (slug + '/' if slug else '')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b222b">
<title>{escape(title)} | Connecting Tomorrow IT</title><meta name="description" content="{escape(description)}"><link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:title" content="{escape(title)} | CTIT"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://www.connectingtomorrowit.com/static/images/data-center.webp">
<link rel="icon" href="/static/images/favicon.svg" type="image/svg+xml"><link rel="preload" href="/static/assets/bbfc0ac38e-mulish-1ptvg83hx_sghgqk3wot.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/static/css/site.css">
<script>document.documentElement.classList.add('js');</script><script src="/static/js/site.js" defer></script></head>
<body id="top"><a class="skip-link" href="#main">Skip to content</a>{header(slug)}<main id="main">{body}</main>{footer()}</body></html>'''


def service_card(service, number=1):
    return f'''<a class="service-card" href="/{service['slug']}/"><div class="service-card-top"><span class="service-icon">{icon(service['icon'])}</span><span class="card-number">0{number}</span></div><h3>{service['name']}</h3><p>{service['summary']}</p><span class="card-link">Explore service{icon('diagonal')}</span></a>'''


def stats():
    return '<div class="stats"><div><strong>150<span>+</span></strong><p>Service locations</p></div><div><strong>6</strong><p>Continents connected</p></div><div><strong>24<span>/</span>7</strong><p>Support availability</p></div><div><strong>2016</strong><p>Our journey began</p></div></div>'


REGIONS = {
    'europe': ('Europe', 'German roots. European reach.', 'Coordinated from Germany, our network supports businesses across European markets. Talk to us about field services, infrastructure support and technology projects for your locations.'),
    'americas': ('Americas', 'Support across the Atlantic.', 'Keep your business connected across North and South America. We coordinate field support and technology services with local resources, based on your location and requirements.'),
    'asia-pacific': ('Asia-Pacific', 'Expertise across time zones.', 'Bring your technology projects and support requirements to a region that never stands still. We help coordinate delivery across Asia-Pacific through our engineering network.'),
    'middle-east-africa': ('Middle East & Africa', 'Connections that open possibilities.', 'Expand your reach with coordinated technical services across the Middle East and Africa. Share your sites and scope so we can confirm the right local support.'),
}


def coverage():
    buttons = ''.join(f'<button type="button" class="region-button{" is-selected" if key == "europe" else ""}" data-region="{key}" aria-pressed="{"true" if key == "europe" else "false"}">{r[0]}{icon("arrow")}</button>' for key, r in REGIONS.items())
    return f'''<section class="coverage-section section" id="coverage"><div class="container coverage-grid"><div><p class="eyebrow">CLOSER THAN YOU THINK</p><h2>Global reach.<br>Local understanding.</h2><p class="section-copy">One coordinated network. Real people on the ground. The expertise to support your business across six continents.</p><div class="region-list" role="group" aria-label="Explore regional support">{buttons}</div></div><div class="coverage-visual"><img src="/static/images/world-network.svg" alt="Illustrative world map connecting Frankfurt with international regions" loading="lazy"><div class="region-detail" aria-live="polite"><p class="eyebrow" data-region-label>EUROPE</p><h3 data-region-title>{REGIONS['europe'][1]}</h3><p data-region-copy>{REGIONS['europe'][2]}</p><a class="text-link" data-region-link href="/kontakt/?region=europe">Discuss your location{icon('arrow')}</a></div><p class="coverage-note">Tell us your location. We’ll confirm service availability and scope.</p></div></div></section>'''


def faqs(items):
    return '<div class="faq-list">' + ''.join(f'<details class="faq-item"><summary>{escape(q)}<span class="faq-plus" aria-hidden="true"></span></summary><p>{escape(a)}</p></details>' for q, a in items) + '</div>'


def vendors():
    return '<section class="vendors"><div class="container"><p>MULTI-VENDOR EXPERTISE. ONE SERVICE PARTNER.</p><div class="vendor-row" aria-label="Supported technologies include Dell, Cisco, Hewlett Packard Enterprise, IBM, Lenovo and Microsoft"><span class="vendor-dell">DELL</span><span class="vendor-cisco">cisco</span><span class="vendor-hpe">Hewlett Packard<br><b>Enterprise</b></span><span class="vendor-ibm">IBM</span><span class="vendor-lenovo">Lenovo</span><span class="vendor-microsoft"><i aria-hidden="true"></i>Microsoft</span></div></div></section>'


def home():
    return f'''<section class="hero"><div class="container"><div class="hero-grid"><div class="hero-copy"><p class="eyebrow"><span class="eyebrow-line"></span>IT THAT GOES THE DISTANCE</p><h1>Your world.<br><em>Connected.</em></h1><p class="hero-description">From the data center to the last mile. We bring people, infrastructure and technology together, wherever your business goes.</p><div class="button-row">{link('Explore our services', '/services/', 'button button-teal', 'diagonal')}{link('Discover CTIT', '/about-us/', 'hero-text-link')}</div><p class="hero-footnote">{icon('pin')}Based in Germany. Connected to the world.</p></div><div class="hero-visual"><img class="globe" src="/static/images/global-globe.svg" alt="A connected globe representing CTIT’s worldwide IT services" fetchpriority="high"><div class="globe-label"><span class="status-dot"></span><span>FRANKFURT, GERMANY<small>Our home. Your global connection.</small></span></div><div class="globe-support">{icon('headset')}<div><strong>Expertise without borders.</strong><span>Support around the clock.</span></div><span class="small-orbit" aria-hidden="true">↗</span></div></div></div>{stats()}</div><span class="hero-grid-pattern" aria-hidden="true"></span></section>
{vendors()}
<section class="section services-section"><div class="container"><div class="section-heading"><div><p class="eyebrow">WHAT WE DO</p><h2>Technology moves fast.<br>We keep you moving.</h2></div><div><p class="section-copy">From everyday support to your next big transformation, we turn IT complexity into business continuity.</p>{link('View all services','/services/')}</div></div><div class="services-grid">{''.join(service_card(s, i + 1) for i, s in enumerate(SERVICES))}</div><a class="software-strip" href="/software-development/"><span class="software-strip-icon">{icon('code')}</span><span><small>BUILT AROUND YOUR BUSINESS</small><strong>Big ideas deserve great software.</strong></span><span class="software-strip-link">Explore software development{icon('diagonal')}</span></a></div></section>
<section class="human-section"><div class="human-photo">{image('field-engineer', 'Field engineer working on enterprise IT infrastructure')}<span class="photo-caption">REAL PEOPLE. PRACTICAL EXPERTISE.</span></div><div class="human-copy"><p class="eyebrow">TECHNOLOGY, WITH A HUMAN SIDE</p><h2>A global network.<br>A personal commitment.</h2><p>Behind every connected business are people who make it happen. Our engineers and service teams bring technical know-how, local understanding and a shared commitment to your next step.</p><div class="human-points"><div>{icon('people')}<span><strong>Local expertise</strong><small>People who understand your environment.</small></span></div><div>{icon('globe')}<span><strong>One coordinated approach</strong><small>Clear communication across locations.</small></span></div><div>{icon('shield')}<span><strong>Your priorities, our focus</strong><small>Support shaped around your business.</small></span></div></div>{link('Get to know CTIT', '/about-us/', 'hero-text-link')}</div></section>
{coverage()}
<section class="section company-section"><div class="container company-grid"><div class="company-photo">{image('collaboration', 'Team collaborating around a meeting table')}<span class="image-tag">Different expertise. Shared ambition.</span></div><div><p class="eyebrow">CONNECTING TOMORROW, TODAY</p><h2>German precision.<br>Worldwide ambition.</h2><p class="section-copy">Since 2016, Connecting Tomorrow IT has helped businesses keep their technology working and their ambitions moving forward.</p><p class="section-copy">From our base in Germany, we connect you with a worldwide network of engineering expertise. One partner for your infrastructure, your people and your next opportunity.</p>{link('Our story', '/about-us/')}</div></div></section>{cta()}'''


def service_page(s):
    capabilities = ''.join(f'<article class="capability"><span>0{i + 1}</span><h3>{name}</h3><p>{copy}</p></article>' for i, (name, copy) in enumerate(s['capabilities']))
    steps = [('Understand', 'We listen to your needs, locations and operational priorities.'), ('Plan', 'Together, we agree the scope, responsibilities and delivery approach.'), ('Deliver', 'The right people execute the work with clear communication.'), ('Support', 'We document, hand over and agree the next steps with you.')]
    process = ''.join(f'<li><span class="process-number">0{i + 1}</span><h3>{name}</h3><p>{copy}</p></li>' for i, (name, copy) in enumerate(steps))
    others = [item for item in SERVICES if item['slug'] != s['slug']][:3]
    tech = '<div class="tech-stack"><span>TECHNOLOGIES WE WORK WITH</span><div>.NET <i>·</i> Angular <i>·</i> Node.js <i>·</i> SQL Server <i>·</i> MongoDB</div></div>' if s is SOFTWARE else ''
    return f'''<section class="page-hero service-hero"><div class="container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><a href="/services/">Expertise</a><span>/</span><span>{s['name']}</span></div><div class="service-hero-grid"><div><p class="eyebrow">{s['category']}</p><h1>{s['title']}</h1><p class="hero-description">{s['intro']}</p>{link('Discuss your project', '/kontakt/?service=' + s['slug'], 'button button-teal', 'diagonal')}</div><div class="service-hero-photo">{image(s['photo'], s['name'] + ' — Connecting Tomorrow IT', eager=True)}<div class="photo-label">{icon(s['icon'])}<span>{s['name']}<small>Global expertise. Local delivery.</small></span></div></div></div></div></section>
<nav class="section-nav" aria-label="On this page"><div class="container"><a href="#overview">Overview</a><a href="#capabilities">What we deliver</a><a href="#approach">Our approach</a><a href="#questions">FAQs</a>{link('Let’s talk', '/kontakt/?service=' + s['slug'])}</div></nav>
<section class="section" id="overview"><div class="container overview-grid"><div><p class="eyebrow">{s['name'].upper()}</p><h2>{s['heading']}</h2></div><div><p class="section-copy">{s['body']}</p><ul class="check-list">{''.join(f'<li>{icon("check")}{b}</li>' for b in s['bullets'])}</ul></div></div></section>
<section class="section soft-section" id="capabilities"><div class="container"><div class="section-heading"><div><p class="eyebrow">WHAT WE DELIVER</p><h2>Expertise where it matters.</h2></div><p class="section-copy">Practical capabilities, shaped around your environment and business priorities.</p></div><div class="capabilities-grid">{capabilities}</div>{tech}</div></section>
<section class="section" id="approach"><div class="container"><p class="eyebrow">A CLEAR PATH FORWARD</p><h2>From first conversation<br>to confident delivery.</h2><ol class="process-grid">{process}</ol></div></section>
<section class="section faq-section" id="questions"><div class="container faq-grid"><div><p class="eyebrow">GOOD QUESTIONS</p><h2>A little clarity.<br>A lot of possibility.</h2><p class="section-copy">Have something else in mind?<br>Let’s talk through it.</p>{link('Contact our team','/kontakt/')}</div>{faqs(s['faq'])}</div></section>
<section class="section"><div class="container"><div class="section-heading"><div><p class="eyebrow">KEEP EXPLORING</p><h2>Connected expertise.</h2></div>{link('All IT services','/services/')}</div><div class="services-grid related-grid">{''.join(service_card(item, i + 1) for i, item in enumerate(others))}</div></div></section>{cta()}'''


def services_page():
    return f'''<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><span>IT services</span></div><div class="page-hero-heading"><div><p class="eyebrow">ONE PARTNER. MANY POSSIBILITIES.</p><h1>Your IT.<br><em>Our expertise.</em></h1></div><div><p class="hero-description">Reliable technology starts with the right people. Explore practical IT services that connect your infrastructure, support your teams and move your business forward.</p>{link('Find your service', '#all-services', 'button button-teal', 'arrow')}</div></div></div></section>
<section class="section" id="all-services"><div class="container"><div class="section-heading"><div><p class="eyebrow">OUR IT SERVICES</p><h2>Support for every connection.</h2></div><p class="section-copy">From a single site to a global footprint, we bring the expertise your business needs.</p></div><div class="services-grid">{''.join(service_card(s, i + 1) for i, s in enumerate(SERVICES))}</div></div></section>
<section class="software-feature"><div class="container software-feature-grid"><div>{image('software','Code on a screen for custom software development')}</div><div><p class="eyebrow">YOUR NEXT DIGITAL POSSIBILITY</p><h2>Built to fit.<br>Built to move you forward.</h2><p class="section-copy">Custom applications, intuitive websites and connected business systems. Turn your ideas into technology that works for you.</p>{link('Explore software development','/software-development/','button button-dark','diagonal')}</div></div></section>
{vendors()}{coverage()}{cta()}'''


def about_page():
    return f'''<section class="page-hero about-hero"><div class="container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><span>Our company</span></div><div class="page-hero-heading"><div><p class="eyebrow">THIS IS CONNECTING TOMORROW IT</p><h1>People. Technology.<br><em>Possibility.</em></h1></div><p class="hero-description">We connect the right people with the right technology, helping businesses move forward wherever opportunity takes them.</p></div><div class="about-hero-image">{image('collaboration','A collaborative team meeting',eager=True)}<span>GERMAN ROOTS. A WORLD OF POSSIBILITIES.</span></div></div></section>
<section class="section"><div class="container overview-grid"><div><p class="eyebrow">OUR STORY</p><h2>Thinking ahead.<br>Showing up.</h2></div><div><p class="section-copy">Established in 2016 and headquartered in Germany, Connecting Tomorrow IT Solutions GmbH is a worldwide provider of multi-vendor IT service solutions.</p><p class="section-copy">We support the lifecycle of enterprise hardware and develop software that solves practical business challenges. Our regional network brings technical skills closer to your locations, while our coordinated approach keeps communication clear.</p><p class="section-copy">We believe the strongest technology partnerships start with understanding people: your teams, your customers and the ambitions behind your business.</p></div></div><div class="container about-stats">{stats()}</div></section>
<section class="section soft-section"><div class="container"><p class="eyebrow">WHAT CONNECTS US</p><h2>Shared principles.<br>Every place we work.</h2><div class="values-grid"><article>{icon('people')}<h3>People make the difference.</h3><p>Technology works best when experienced people understand your needs and take responsibility for the next step.</p></article><article>{icon('globe')}<h3>Think global. Understand local.</h3><p>A worldwide perspective matters. So does understanding the practical requirements of each location.</p></article><article>{icon('shield')}<h3>Build lasting connections.</h3><p>Clear communication, agreed expectations and practical expertise are at the heart of how we work.</p></article></div></div></section>
{coverage()}<section class="section"><div class="container company-grid"><div class="company-photo">{image('field-engineer','Technical specialist supporting enterprise infrastructure')}<span class="image-tag">Expertise that reaches you.</span></div><div><p class="eyebrow">THE TEAM BEHIND YOUR TECHNOLOGY</p><h2>Different skills.<br>One shared commitment.</h2><p class="section-copy">Our engineering, software and service coordination teams bring together the knowledge to support your infrastructure and help you build what comes next.</p><p class="section-copy">Whether you need support for an office in Frankfurt or a technology project across borders, we start with your priorities and connect the right expertise.</p>{link('Explore our capabilities','/services/')}</div></div></section>{cta()}'''


def contact_page():
    options = ''.join(f'<option value="{s["name"]}">{s["name"]}</option>' for s in SERVICES + [SOFTWARE])
    questions = [('Where do you provide services?', 'Our network spans six continents, coordinated from Germany. Share the location and technical requirements for your project so we can confirm service availability.'), ('How should I request support?', 'For an existing support agreement, use your agreed support channel. For a new request, call or email us with the location, equipment and a short description of what you need.'), ('What should I include in a project enquiry?', 'Your locations, the type and number of devices or users, preferred timing and any response requirements help us understand the scope. Please do not include passwords or sensitive credentials.'), ('Does submitting this form send an email?', 'In this local preview, the form saves your enquiry in the project database. It does not send email. Use the email or phone links to contact CTIT directly.')]
    return f'''<section class="contact-section section"><div class="container"><div class="breadcrumb"><a href="/">Home</a><span>/</span><span>Let’s connect</span></div><div class="contact-grid"><div class="contact-intro"><p class="eyebrow">YOUR NEXT CONNECTION STARTS HERE</p><h1>Let’s move<br><em>forward.</em></h1><p class="section-copy">A technical challenge. A new project. A bigger ambition. Tell us what’s on your mind.</p><div class="contact-methods"><a href="mailto:{EMAIL}"><span class="contact-method-icon">{icon('mail')}</span><span><small>EMAIL OUR TEAM</small><strong>{EMAIL}</strong></span>{icon('diagonal')}</a><a href="tel:+491608306949"><span class="contact-method-icon">{icon('phone')}</span><span><small>LET’S TALK</small><strong>{PHONE}</strong></span>{icon('diagonal')}</a><div><span class="contact-method-icon">{icon('globe')}</span><span><small>BASED IN GERMANY</small><strong>Connected worldwide.</strong></span></div></div><div class="contact-image">{image('service-desk','IT service team working together')}</div></div>
<div class="contact-form-panel" id="contact-form"><p class="eyebrow">TELL US WHAT YOU HAVE IN MIND</p><h2>How can we help?</h2><p>Share a few details to get the conversation started.</p><form class="ctit-contact" action="/contact/" method="post"><input type="hidden" name="csrf" value="__CSRF_TOKEN__"><div class="form-row"><label for="contact-name">Full name <span>*</span><input id="contact-name" name="name" autocomplete="name" placeholder="Your name" required maxlength="120"></label><label for="contact-email">Work email <span>*</span><input id="contact-email" name="email" type="email" autocomplete="email" placeholder="you@company.com" required maxlength="254"></label></div><label for="contact-service">What can we help you with? <span>*</span><select id="contact-service" name="subject" required><option value="" disabled selected>Select a service</option>{options}<option value="Global IT support">Global IT support</option><option value="General enquiry">Something else / general enquiry</option></select></label><label for="contact-message">Tell us about your project <span>*</span><textarea id="contact-message" name="message" rows="5" placeholder="Your locations, requirements and preferred timing…" required maxlength="10000"></textarea></label><label class="ctit-consent"><input type="checkbox" name="consent" required><span>I agree that CTIT may use these details to respond to my enquiry.</span></label><button class="button button-dark" type="submit">Save enquiry{icon('diagonal')}</button><p class="ctit-form-note">Local preview: enquiries are saved to this project. No email is sent. To reach CTIT directly, use the email or phone links.</p></form></div></div></div></section>
<section class="section faq-section"><div class="container faq-grid"><div><p class="eyebrow">BEFORE WE CONNECT</p><h2>A few helpful answers.</h2><p class="section-copy">Every business is different.<br>We’re happy to talk through your needs.</p></div>{faqs(questions)}</div></section>'''


def build():
    pages = {
        '': ('Global IT services. Local expertise.', 'Worldwide IT support, data center services, field engineering and custom software. German roots. Global reach.', home()),
        'about-us': ('Our company — German roots, global reach', 'Meet Connecting Tomorrow IT: a Germany-based provider of worldwide IT services and software solutions, established in 2016.', about_page()),
        'services': ('IT services for a connected world', 'Explore global data center support, 24/7 assistance, rollout, hardware repair, IMAC and structured cabling services.', services_page()),
        'software-development': ('Custom software development', SOFTWARE['intro'], service_page(SOFTWARE)),
        'kontakt': ('Contact our team', 'Talk to Connecting Tomorrow IT about your support requirements, technology projects and global IT service needs.', contact_page()),
    }
    for s in SERVICES:
        pages[s['slug']] = (s['name'], s['intro'], service_page(s))
    for slug, (title, description, body) in pages.items():
        (ROOT / 'templates' / ((slug or 'index') + '.html')).write_text(document(slug, title, description, body), encoding='utf-8')
    (ROOT / 'static/js/regions.json').write_text(json.dumps(REGIONS, ensure_ascii=False), encoding='utf-8')
    (ROOT / 'static/images/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="12" fill="#0b222b"/><g stroke="#59e0b4" stroke-width="6" stroke-linecap="round"><path d="m13 30 8-15m3 18 8-18m0 18 5-10"/></g></svg>')
    print(f'Built {len(pages)} pages. Run python app.py to preview.')


if __name__ == '__main__':
    build()
