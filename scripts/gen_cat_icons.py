# Iconițele de categorie Jobzee: 30 de familii, desenate în aceeași limbă vizuală:
# plăcuță rotunjită crem-piersică, ilustrație duotone cărbune (#292D33) + portocaliu oficial (#FF9B00), linie 2,6 px rotunjită.
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'jobzee-design/project/assets/cat')
os.makedirs(OUT, exist_ok=True)
C, O, D, L, W = '#292D33', '#FF9B00', '#E57F00', '#FFD49A', '#FFFFFF'
S = 'stroke="%s" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"' % C

ICONS = {
 'mobila': f'''<rect x="15" y="16" width="34" height="30" rx="4" fill="{O}" {S}/><path d="M15 26h34M15 36h34" {S} fill="none"/>
   <circle cx="32" cy="21" r="1.8" fill="{W}"/><circle cx="32" cy="31" r="1.8" fill="{W}"/><circle cx="32" cy="41" r="1.8" fill="{W}"/><path d="M19 46v5M45 46v5" {S}/>
   <path d="M44 9l6 6-3 3-6-6z" fill="{L}" {S}/>''',
 'curatenie': f'''<path d="M23 31h18v17a4 4 0 0 1-4 4H27a4 4 0 0 1-4-4z" fill="{O}" {S}/><rect x="27" y="25" width="10" height="6" rx="1.5" fill="{L}" {S}/>
   <path d="M25 25v-6a2 2 0 0 1 2-2h11l5 4h-5v4" fill="{W}" {S}/><path d="M27 38h10" stroke="{W}" stroke-width="2.6" stroke-linecap="round"/>
   <path d="M14 14l1.6 3.4L19 19l-3.4 1.6L14 24l-1.6-3.4L9 19l3.4-1.6z" fill="{O}"/><path d="M50 10l1 2 2 1-2 1-1 2-1-2-2-1 2-1z" fill="{O}"/>''',
 'mutat-obiecte': f'''<path d="M14 27l18 9v17l-18-9z" fill="{O}" {S}/><path d="M32 36l18-9v17l-18 9z" fill="{D}" {S}/><path d="M14 27l18-9 18 9-18 9z" fill="{L}" {S}/>
   <path d="M23 22.5l18 9" stroke="{W}" stroke-width="3.4" stroke-linecap="round"/><path d="M40 13h10m-4-4l4 4-4 4" {S} fill="none"/>''',
 'sanitar': f'''<rect x="20" y="11" width="14" height="5" rx="2.5" fill="{O}" {S}/><path d="M27 16v6" {S}/>
   <path d="M12 22h24a8 8 0 0 1 8 8v4h-7v-4a1 1 0 0 0-1-1H12z" fill="{O}" {S}/><path d="M40.5 40s-4.5 5.5-4.5 8.5a4.5 4.5 0 0 0 9 0c0-3-4.5-8.5-4.5-8.5z" fill="{L}" {S}/>''',
 'electrica': f'''<path d="M35 9L19 34h11l-4 21 18-27H33z" fill="{O}" {S}/><path d="M12 20h4M48 40h4M14 44l3-3M47 17l3-3" {S}/>''',
 'electrocasnice': f'''<rect x="15" y="10" width="34" height="44" rx="6" fill="{W}" {S}/><path d="M15 19h34" {S}/><circle cx="21" cy="14.5" r="1.8" fill="{O}"/><circle cx="27" cy="14.5" r="1.8" fill="{C}"/>
   <circle cx="32" cy="36" r="11" fill="{O}" {S}/><path d="M25 37c3 3 11 3 14-2" stroke="{W}" stroke-width="2.6" stroke-linecap="round" fill="none"/>''',
 'zugraveala': f'''<rect x="12" y="12" width="32" height="13" rx="5" fill="{O}" {S}/><path d="M44 18h5v10H32v7" {S} fill="none"/><rect x="28" y="35" width="8" height="17" rx="3.5" fill="{C}"/>
   <path d="M19 25v6a2.5 2.5 0 0 0 5 0v-6" fill="{O}" {S}/>''',
 'gradina': f'''<path d="M21 39h22l-3 14H24z" fill="{O}" {S}/><rect x="18" y="35" width="28" height="6" rx="2.5" fill="{D}" {S}/><path d="M32 35V21" {S}/>
   <path d="M32 27c-9 0-13-6-13-13 9 0 13 6 13 13z" fill="{L}" {S}/><path d="M32 23c7 0 11-4 11-11-7 0-11 4-11 11z" fill="{L}" {S}/>''',
 'animale': f'''<ellipse cx="32" cy="41" rx="11" ry="9" fill="{O}" {S}/><ellipse cx="18.5" cy="29" rx="4.5" ry="5.5" fill="{O}" {S}/><ellipse cx="26.5" cy="20" rx="4.5" ry="5.5" fill="{O}" {S}/>
   <ellipse cx="37.5" cy="20" rx="4.5" ry="5.5" fill="{O}" {S}/><ellipse cx="45.5" cy="29" rx="4.5" ry="5.5" fill="{O}" {S}/>''',
 'cumparaturi': f'''<path d="M14 24h36l-3 28H17z" fill="{O}" {S}/><path d="M24 30v-9a8 8 0 0 1 16 0v9" {S} fill="none"/><circle cx="24" cy="30" r="1.8" fill="{C}"/><circle cx="40" cy="30" r="1.8" fill="{C}"/>
   <path d="M22 44h20" stroke="{W}" stroke-width="2.6" stroke-linecap="round"/>''',
 'ingrijire-persoane': f'''<path d="M32 37c-10-7-14-11-14-16a7 7 0 0 1 14-3 7 7 0 0 1 14 3c0 5-4 9-14 16z" fill="{O}" {S}/>
   <path d="M10 44h9l9 3h10a3 3 0 0 1 0 6H19l-9-2" fill="{L}" {S}/><path d="M38 47l10-4a3 3 0 0 1 3 5l-11 5" fill="{L}" {S}/>''',
 'it': f'''<rect x="15" y="14" width="34" height="24" rx="3.5" fill="{C}"/><rect x="18.5" y="17.5" width="27" height="17" rx="1.5" fill="{O}"/>
   <path d="M24 26l-3 3 3 3M40 26l3 3-3 3M34 24l-4 10" stroke="{W}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M9 42h46l-4 8H13z" fill="{L}" {S}/>''',
 'reparatii': f'''<rect x="29" y="27" width="6.5" height="26" rx="3" fill="{C}"/><path d="M19 14h24a5 5 0 0 1 5 5v4a2 2 0 0 1-2 2H18l-4-4v-2a5 5 0 0 1 5-5z" fill="{O}" {S}/>
   <path d="M43 14v11" {S}/>''',
 'tamplarie': f'''<rect x="19" y="10" width="26" height="42" rx="3" fill="{O}" {S}/><rect x="23.5" y="15" width="17" height="14" rx="2" fill="{L}" {S}/><rect x="23.5" y="33" width="17" height="13" rx="2" fill="{L}" {S}/>
   <circle cx="41" cy="31" r="2" fill="{C}"/><path d="M12 53h40" {S}/>''',
 'gresie': f'''<rect x="13" y="13" width="17" height="17" rx="3" fill="{O}" {S}/><rect x="34" y="13" width="17" height="17" rx="3" fill="{L}" {S}/><rect x="13" y="34" width="17" height="17" rx="3" fill="{L}" {S}/>
   <rect x="34" y="34" width="17" height="17" rx="3" fill="{O}" {S}/>''',
 'clima': f'''<rect x="10" y="13" width="44" height="18" rx="5" fill="{W}" {S}/><path d="M17 25h30" {S}/><circle cx="47" cy="19" r="2" fill="{O}"/>
   <path d="M20 37c-3 3 3 6 0 10M32 37c-3 3 3 6 0 10M44 37c-3 3 3 6 0 10" stroke="{O}" stroke-width="3.2" stroke-linecap="round" fill="none"/>''',
 'lacatus': f'''<circle cx="22" cy="23" r="10" fill="{O}" {S}/><circle cx="22" cy="23" r="3.5" fill="{W}" {S}/><path d="M29 30l19 19" stroke="{C}" stroke-width="5.5" stroke-linecap="round"/>
   <path d="M40 41l4-4M45 46l4-4" stroke="{C}" stroke-width="4.5" stroke-linecap="round"/>''',
 'auto': f'''<path d="M10 41v-6l7-11h30l7 11v6a2 2 0 0 1-2 2H12a2 2 0 0 1-2-2z" fill="{O}" {S}/><path d="M21 27h22l4 8H17z" fill="{L}" {S}/>
   <circle cx="20" cy="44" r="5" fill="{C}"/><circle cx="44" cy="44" r="5" fill="{C}"/><path d="M22 9s-3 3.6-3 5.6a3 3 0 0 0 6 0c0-2-3-5.6-3-5.6zM42 9s-3 3.6-3 5.6a3 3 0 0 0 6 0c0-2-3-5.6-3-5.6z" fill="{L}" {S}/>''',
 'livrari': f'''<rect x="26" y="20" width="26" height="24" rx="3.5" fill="{O}" {S}/><path d="M39 20v10" stroke="{W}" stroke-width="3.4" stroke-linecap="round"/><path d="M33 38h6" stroke="{W}" stroke-width="2.6" stroke-linecap="round"/>
   <path d="M10 26h11M14 32h8M10 38h11" {S}/><path d="M24 50h28" {S}/>''',
 'gatit': f'''<path d="M13 31h38v11a8 8 0 0 1-8 8H21a8 8 0 0 1-8-8z" fill="{O}" {S}/><path d="M15 31a17 6.5 0 0 1 34 0z" fill="{L}" {S}/><circle cx="32" cy="23" r="2.5" fill="{C}"/>
   <path d="M13 36H8M51 36h5" {S}/><path d="M24 17c-2-3 2-5 0-8M32 15c-2-3 2-5 0-8M40 17c-2-3 2-5 0-8" stroke="{C}" stroke-width="2.4" stroke-linecap="round" fill="none"/>''',
 'babysitting': f'''<path d="M17 30a15 15 0 0 1 15-15v15z" fill="{O}" {S}/><path d="M17 30h30a12 10 0 0 1-12 11h-7a11 11 0 0 1-11-11z" fill="{L}" {S}/>
   <path d="M47 30l3-11h5" {S} fill="none"/><circle cx="23" cy="49" r="4.5" fill="{C}"/><circle cx="41" cy="49" r="4.5" fill="{C}"/>''',
 'meditatii': f'''<path d="M32 21c-6-4-12-4-19-2v29c7-2 13-2 19 2z" fill="{W}" {S}/><path d="M32 21c6-4 12-4 19-2v29c-7-2-13-2-19 2z" fill="{L}" {S}/>
   <path d="M39 19v13l3-2.5 3 2.5V18" fill="{O}" {S}/><path d="M18 27h8M18 33h8M18 39h6" stroke="{C}" stroke-width="2" stroke-linecap="round"/>''',
 'evenimente': f'''<path d="M26 37c-2 6 4 9 1 16" {S} fill="none"/><path d="M41 33c2 7-6 11-3 20" {S} fill="none"/>
   <ellipse cx="25" cy="24" rx="10" ry="12" fill="{O}" {S}/><ellipse cx="41" cy="22" rx="8.5" ry="10.5" fill="{L}" {S}/><path d="M21 19a5 5 0 0 1 4-4" stroke="{W}" stroke-width="2.4" stroke-linecap="round" fill="none"/>''',
 'foto': f'''<path d="M23 22l3.5-6h11l3.5 6" fill="{C}" {S}/><rect x="10" y="21" width="44" height="29" rx="6" fill="{C}"/><circle cx="32" cy="35.5" r="10" fill="{O}" stroke="{W}" stroke-width="2.6"/>
   <circle cx="32" cy="35.5" r="4.2" fill="{L}"/><rect x="44" y="25" width="6" height="3.5" rx="1.5" fill="{O}"/>''',
 'frumusete': f'''<path d="M27 37L42 11" stroke="{C}" stroke-width="4" stroke-linecap="round"/><path d="M37 37L22 11" stroke="{C}" stroke-width="4" stroke-linecap="round"/>
   <circle cx="23" cy="45" r="7" fill="{O}" {S}/><circle cx="41" cy="45" r="7" fill="{O}" {S}/><circle cx="23" cy="45" r="2.6" fill="{W}"/><circle cx="41" cy="45" r="2.6" fill="{W}"/><circle cx="32" cy="27" r="2.2" fill="{L}" {S}/>
   <path d="M50 12l1.2 2.6 2.8 1.2-2.8 1.2L50 20l-1.2-2.8L46 16l2.8-1.2z" fill="{O}"/>''',
 'fitness': f'''<rect x="20" y="29.5" width="24" height="5" rx="2.5" fill="{C}"/><rect x="13" y="19" width="9" height="26" rx="3.5" fill="{O}" {S}/><rect x="42" y="19" width="9" height="26" rx="3.5" fill="{O}" {S}/>
   <rect x="7" y="24" width="6" height="16" rx="2.5" fill="{L}" {S}/><rect x="51" y="24" width="6" height="16" rx="2.5" fill="{L}" {S}/>''',
 'calcat': f'''<path d="M24 26c2-6 6-9 12-9h12v9" {S} fill="none"/><path d="M11 45c0-12 8-19 22-19h15a6 6 0 0 1 6 6v13z" fill="{O}" {S}/><rect x="9" y="45" width="47" height="5" rx="2.5" fill="{C}"/>
   <circle cx="30" cy="37" r="1.6" fill="{W}"/><circle cx="37" cy="37" r="1.6" fill="{W}"/><circle cx="44" cy="37" r="1.6" fill="{W}"/>''',
 'dezinsectie': f'''<path d="M23 30l-8-4M23 37h-9M24 44l-7 5M41 30l8-4M41 37h9M40 44l7 5M29 17l-4-6M35 17l4-6" {S}/>
   <ellipse cx="32" cy="37" rx="10" ry="13" fill="{O}" {S}/><circle cx="32" cy="21" r="5.5" fill="{C}"/><path d="M32 26v24" {S}/>''',
 'geamuri': f'''<rect x="13" y="11" width="38" height="42" rx="3.5" fill="{L}" {S}/><path d="M32 11v42M13 32h38" {S}/>
   <path d="M18 24l6-6M18 29l3-3M37 45l6-6" stroke="{W}" stroke-width="2.8" stroke-linecap="round"/><path d="M51 6l1.4 3 3 1.4-3 1.4L51 15l-1.4-3.2-3-1.4 3-1.4z" fill="{O}"/>''',
 'acte': f'''<path d="M17 10h20l11 11v31a2 2 0 0 1-2 2H17a2 2 0 0 1-2-2V12a2 2 0 0 1 2-2z" fill="{W}" {S}/><path d="M37 10v11h11" fill="{L}" {S}/>
   <path d="M21 29h16M21 35h16M21 41h9" stroke="{C}" stroke-width="2.2" stroke-linecap="round"/><path d="M38 52l13-13" stroke="{O}" stroke-width="5.5" stroke-linecap="round"/>''',
}

TPL = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="128" height="128">'
       '<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF8EE"/><stop offset="1" stop-color="#FFE3BD"/></linearGradient></defs>'
       '<rect width="64" height="64" rx="18" fill="url(#g)"/>%s</svg>')

if __name__ == '__main__':
    for k, v in ICONS.items():
        open(os.path.join(OUT, k + '.svg'), 'w').write(TPL % v)
    print(len(ICONS), 'icons')
