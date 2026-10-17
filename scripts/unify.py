import re, glob, os
D='jobzee-design/project'
GEN=set('Splash SplashDark Main MainDark Email Rol RolDark SchimbaRol SchimbaRolDark Acasa AcasaDark Castig CastigDark Cont ContJobzer Fisa Servicii Radar RadarDark Mascota ContTrimitere'.split())
ORPHAN={'Cautare','Descrie','Gasit','Pret','Verifica'}
PH={'MI':'person-jobzer-3','AD':'person-jobzer-2','RC':'person-jobzer-1','EP':'person-client-1'}
def prop(style,k):
    m=re.search(r'(?:^|;)\s*'+k+r':\s*([^;]+)',style); return m.group(1).strip() if m else None
def avatar(m):
    tag,cls,style,ini=m.group(1),m.group(2) or '',m.group(3),m.group(4)
    w,h=prop(style,'width'),prop(style,'height')
    if not w or not h or not w.endswith('px'): return m.group(0)
    keep=[]
    for k in ('box-shadow','flex-shrink','position','left','top','right','bottom','margin','border'):
        v=prop(style,k)
        if v: keep.append('%s: %s'%(k,v))
    st='width: %s; height: %s; border-radius: 50%%; object-fit: cover; display: block; flex-shrink: 0; %s'%(w,h,'; '.join(keep))
    return '<img%s src="assets/people/%s.webp" alt="" style="%s">'%(cls,PH[ini],st.strip('; '))
avpat=re.compile(r'<(span|div)( class="[^"]*")? style="([^"]*)">(MI|AD|RC|EP)</\1>')
backpat=re.compile(r'<a href="([^"]*)" class="pr" style="([^"]*)">\s*<svg[^>]*><path d="M15 5l-7 7 7 7"></path></svg>([^<\n]+?)\s*</a>')
def back(m):
    href,style,label=m.group(1),m.group(2),m.group(3).strip()
    dark='#FFB340' in style or '#FF9F0A' in style and 'color: #FF9F0A' in style
    extra=[]
    for k in ('align-self','position','left','top','right'):
        v=prop(style,k)
        if v: extra.append('%s: %s'%(k,v))
    bg='rgba(44,44,46,0.88); color: #FFFFFF' if dark else '#FFFFFF; color: #1C1C1E'
    return ('<a href="%s" aria-label="Înapoi la %s" class="pr" style="%s; width: 40px; height: 40px; border-radius: 20px; background: %s; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 4px 14px rgba(0,0,0,0.08); text-decoration: none">'
            '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"></path></svg></a>')%(href,label,'; '.join(extra) or 'align-self: flex-start',bg)
TXT=[('Str. [STRADA] nr. [NR], Floreasca','Str. Barbu Văcărescu nr. 120, Floreasca'),('Bd. [BULEVARD] nr. [NR], Pipera','Bd. Dimitrie Pompeiu nr. 5, Pipera'),
     ('[ADRESA EXACTĂ]','Str. Barbu Văcărescu 120'),('•••• [ULTIMELE 4]','Visa •••• 4821'),('[ULTIMELE 4]','4821'),
     ('[DESCRIEREA SCRISĂ DE JOBZER: experiență, specializare, unelte]','Montez mobilier de 8 ani, de la IKEA la bucătării pe comandă. Vin cu toate uneltele și las curat după mine.'),
     ('#C25E00','#B35600'),('#248A3D','#1F7A35')]
stats={}
for p in sorted(glob.glob(D+'/*.dc.html')):
    n=os.path.basename(p)[:-8]
    if n in GEN or n in ORPHAN: continue
    s=open(p).read(); o=s
    s,a=avpat.subn(avatar,s); s,bk=backpat.subn(back,s)
    for x,y in TXT: s=s.replace(x,y)
    if n in ('Oferte','OferteDark'):
        s=re.sub(r'<span style="width: 46px; height: 46px; border-radius: 23px;[^"]*">\{\{o\.ini\}\}</span>','<img src="{{o.img}}" alt="" style="width: 46px; height: 46px; border-radius: 23px; object-fit: cover; flex-shrink: 0">',s)
        s=s.replace("ini: o.ini, name: o.name,","ini: o.ini, img: 'assets/people/' + ({ AD: 'person-jobzer-2', MI: 'person-jobzer-3', RC: 'person-jobzer-1', EP: 'person-client-1' })[o.ini] + '.webp', name: o.name,")
    if s!=o: open(p,'w').write(s); stats[n]=(a,bk)
for k,v in stats.items(): print(k,v)
