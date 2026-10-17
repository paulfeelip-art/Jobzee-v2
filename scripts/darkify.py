import re, os, glob, sys
D='jobzee-design/project'
sys.path.insert(0,'.')
import importlib; gr=importlib.import_module('gen_roles')
GEN_LIGHT='Email Cont ContJobzer Fisa Servicii Mascota ContTrimitere Notificari Chitante Recurente StartJobzer Disponibilitate Facturi CerereMultipla Statistici Siguranta GearHub GearKituri GearKit GearBuilder GearShop GearProdus GearIdentity PrintStudio GearCarte GearFlyer GearQR GearCos GearCheckout GearConfirmare GearUrmarire GearEchipament GearDesignuri GearGrowth Mesaje Dialog Chat ChatJobzer Skilluri ProfilEdit'.split()
HAVE_DARK={'Splash','Main','Rol','SchimbaRol','Acasa','Castig','Radar','Oferte','PeDrum','Incasari'}
SKIP={'OfertaRapida','Cautare','Descrie','Gasit','Pret','Verifica'}
# --- hand-written boards: color mapping
BG={'#FFFFFF':'#1C1C1E','#F2F2F7':'#2C2C2E','#F9F9F9':'#1C1C1E','#E5E5EA':'#3A3A3C','#E9E9EB':'#2C2C2E','#E9E9EE':'#2C2C2E','#EEEEF0':'#2C2C2E','#E3E3E8':'#3A3A3C','#E9E9EA':'#3A3A3C','#D1D1D6':'#38383A',
    '#FFF4E5':'#3A2A14','#FFE7C2':'#4A3416','#FFE5E3':'#3A1A18','#EAF3FF':'#14283A','#EAF5FF':'#14283A','#EEF8EA':'#182A18','#F3EEFF':'#261C3A','#ECE6DA':'#2A2A2D','#FAFAFC':'#2C2C2E','#FFF8EE':'#3A2A14','#FFFAF2':'#3A2A14','#FFF9F0':'#3A2A14',
    '#F5F1E8':'#1B1C1F','#D3EAC7':'#1C2A20','#BCDDF7':'#17283A','#EDEAE3':'#141416','#8E8A82':'#0E0E10','#E8F7EC':'#14301C','#FCEBF1':'#3A1A26'}
TX={'#1C1C1E':'#FFFFFF','#3A3A3C':'#D1D1D6','#6E6E73':'#98989D','#8E8E93':'#8E8E93','#C7C7CC':'#48484A','#B35600':'#FFB340','#8F4500':'#FFD08A','#1F7A35':'#30D158','#D70015':'#FF6961','#6B0007':'#FFB4AE','#1D6FB8':'#64B5F6','#2E7D32':'#81C784','#6B4FBB':'#B39DDB','#248A3D':'#30D158'}
STRONG_BG=('#FF9F0A','#34C759','#FF3B30','#007AFF','#5856D6','#FF2D55','#AF52DE','#30D158','#FFB340')
HEX=r'#[0-9A-Fa-f]{6}'
def conv_decls(seg):
    # seg: a CSS declaration list (inline style or rule body). Decide per segment.
    m=re.search(r'background(?:-color)?:\s*('+HEX+')',seg)
    bg=m.group(1).upper() if m else None
    hm=re.search(r'(?<![-\w])height:\s*(\d+)px',seg)
    small = bool(hm) and int(hm.group(1))<=60
    inverse = bg=='#1C1C1E' and small
    card = bg=='#1C1C1E' and not small
    strong = bg in STRONG_BG if bg else False
    def bgrep(mm):
        c=mm.group(2).upper()
        if inverse: return mm.group(1)+'#FFFFFF'
        if card: return mm.group(1)+'#2C2C2E'
        return mm.group(1)+BG.get(c,c)
    seg=re.sub(r'(background(?:-color)?:\s*)('+HEX+')',bgrep,seg)
    seg=re.sub(r'(background:\s*(?:repeating-)?(?:linear|radial|conic)-gradient\([^;"]*)',lambda mm: re.sub(HEX,lambda h:BG.get(h.group(0).upper(),h.group(0)),mm.group(1)),seg)
    def colrep(mm):
        c=mm.group(2).upper()
        if inverse and c=='#FFFFFF': return mm.group(1)+'#000000'
        if strong or card: return mm.group(0)
        if inverse: return mm.group(0)
        return mm.group(1)+TX.get(c,c)
    seg=re.sub(r'((?<![-\w])color:\s*)('+HEX+')',colrep,seg)
    seg=re.sub(r'((?:border[-a-z]*|box-shadow|outline):[^;"]*)',lambda mm: re.sub(HEX,lambda h:{'#FFFFFF':'#1C1C1E','#D1D1D6':'#38383A','#E5E5EA':'#3A3A3C','#F2F2F7':'#2C2C2E','#C7C7CC':'#48484A','#1C1C1E':'#3A3A3C'}.get(h.group(0).upper(),h.group(0)),mm.group(1)),seg)
    seg=re.sub(r'rgba\(255,\s*255,\s*255,\s*0?\.([789]\d?)\)',lambda mm:'rgba(44,44,46,0.'+mm.group(1)+')',seg)
    seg=re.sub(r'rgba\(249,\s*249,\s*249,\s*0?\.(\d+)\)',lambda mm:'rgba(28,28,30,0.'+mm.group(1)+')',seg)
    seg=seg.replace('rgba(28,28,30,0.86)','rgba(255,255,255,0.9)').replace('rgba(28,28,30,0.9)','rgba(255,255,255,0.92)')
    return seg
def conv_svg_attrs(s):
    s=re.sub(r'fill="('+HEX+')"',lambda m:'fill="%s"'%{'#F5F1E8':'#1B1C1F','#D3EAC7':'#1C2A20','#BCDDF7':'#17283A','#ECE6DA':'#2A2A2D','#E5E5EA':'#3A3A3C','#F2F2F7':'#2C2C2E','#1C1C1E':'#FFFFFF'}.get(m.group(1).upper(),m.group(1)),s)
    s=re.sub(r'stroke="#FFFFFF" stroke-width="(\d+)"',lambda m:('stroke="#2E3035" stroke-width="%s"'%m.group(1)) if int(m.group(1))>=6 else m.group(0),s)
    s=re.sub(r'stroke="#C7C7CC"','stroke="#48484A"',s)
    s=re.sub(r'stroke="#1C1C1E"','stroke="#FFFFFF"',s)
    return s
def darken_hand(src):
    # convert every quoted string and every css rule body
    out=re.sub(r'(style=")([^"]*)(")',lambda m:m.group(1)+conv_decls(m.group(2))+m.group(3),src)
    out=re.sub(r"(')([^'\n]*(?:background|color|box-shadow|border)[^'\n]*)(')",lambda m:m.group(1)+conv_decls(m.group(2))+m.group(3),out)
    out=re.sub(r"'(#[0-9A-Fa-f]{6})'",lambda m:"'"+BG.get(m.group(1).upper(),TX.get(m.group(1).upper(),m.group(1)))+"'",out)
    out=re.sub(r'(<style>)(.*?)(</style>)',lambda m:m.group(1)+re.sub(r'\{([^{}]*)\}',lambda r:'{'+conv_decls(r.group(1))+'}',m.group(2))+m.group(3),out,flags=re.S)
    out=conv_svg_attrs(out)
    return out
made=[]
for n in GEN_LIGHT:
    p=os.path.join(D,n+'.dc.html'); s=open(p).read()
    s=s.replace(gr.theme_css('L'),gr.theme_css('D'))
    open(os.path.join(D,n+'Dark.dc.html'),'w').write(s); made.append(n)
for p in sorted(glob.glob(D+'/*.dc.html')):
    n=os.path.basename(p)[:-8]
    if n.endswith('Dark') or n in HAVE_DARK or n in SKIP or n in GEN_LIGHT: continue
    open(os.path.join(D,n+'Dark.dc.html'),'w').write(darken_hand(open(p).read())); made.append(n)
# relink all dark boards to dark targets
darks={os.path.basename(p)[:-8] for p in glob.glob(D+'/*Dark.dc.html')}
for d in darks:
    p=os.path.join(D,d+'.dc.html'); s=open(p).read()
    s=re.sub(r'href="([A-Za-z]+)\.dc\.html"',lambda m:'href="%sDark.dc.html"'%m.group(1) if (m.group(1)+'Dark') in darks and not m.group(1).endswith('Dark') else m.group(0),s)
    s=s.replace('<title>Jobzee · ','<title>Jobzee · ').replace('</title>',' · întunecat</title>',1) if '· întunecat' not in s and '(întunecat)' not in s else s
    open(p,'w').write(s)
print(len(made),'made;', len(darks),'dark boards total')
print(' '.join(made))
# final pass: leftover light greys/tints anywhere in converted darks
FIN={'#E9E9EE':'#2C2C2E','#F6F6F9':'#3A3A3C','#EEEEF0':'#2C2C2E','#D1D1D6':'#48484A','#FFF4E5':'#3A2A14','#FCEBF1':'#3A1A26','#EEF8EA':'#182A18','#E8F4FF':'#14283A',"'#B35600'":"'#FFB340'",'background: #B35600':'background: #FFB340'}
for n in made:
    p=os.path.join(D,n+'Dark.dc.html'); s=open(p).read()
    for a,b in FIN.items(): s=s.replace(a,b).replace(a.lower(),b)
    open(p,'w').write(s)
print('final pass ok')
