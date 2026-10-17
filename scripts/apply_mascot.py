import re, os
D='jobzee-design/project'
def zee(expr, w, extra='', cls=''):
    h=round(w*130/120)
    return '<img %s src="assets/mascot/zee-%s.svg" alt="" style="width: %dpx; height: %dpx; display: block; %s">' % (('class="%s"'%cls) if cls else '', expr, w, h, extra)
def find_el(s, line_no):
    # start index of line, then balanced end of the element that starts there
    lines=s.split('\n'); start=sum(len(l)+1 for l in lines[:line_no-1]); i=s.index('<',start)
    tag=re.match(r'<(\w+)',s[i:]).group(1); depth=0; j=i
    pat=re.compile(r'<(/?)'+tag+r'\b[^>]*>')
    for m in pat.finditer(s,i):
        depth += -1 if m.group(1) else 1
        if depth==0: return i, m.end()
    raise Exception('unbalanced')
def rep_line(f, line_no, new):
    p=os.path.join(D,f); s=open(p).read(); a,b=find_el(s,line_no); s=s[:a]+new+s[b:]; open(p,'w').write(s); print('ok',f)
FLOATCSS='@keyframes zf{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(-3deg)}}.zf{animation:zf 3.6s ease-in-out infinite}\n@keyframes zw{0%,100%{transform:rotate(0)}20%{transform:rotate(-8deg)}40%{transform:rotate(6deg)}60%{transform:rotate(-4deg)}}.zw{transform-origin:50% 90%;animation:zw 2.4s ease-in-out .6s infinite}\n'
def addcss(f):
    p=os.path.join(D,f); s=open(p).read()
    if '.zf{' not in s: s=s.replace('@media (prefers-reduced-motion','%s@media (prefers-reduced-motion'%FLOATCSS,1)
    open(p,'w').write(s)
jobs=[
 ('FaraInternet.dc.html',35,'<div class="u" style="align-self: center; position: relative">'+zee('ups',120,'',"zf")+'<span style="position: absolute; right: -6px; bottom: 14px; width: 40px; height: 40px; border-radius: 20px; background: #FFFFFF; box-shadow: 0 6px 16px rgba(0,0,0,0.12); display: flex; align-items: center; justify-content: center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8E8E93" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M2 8.5a15 15 0 0 1 20 0M5.5 12a10 10 0 0 1 13 0M9 15.5a5 5 0 0 1 6 0M12 19h.01M3 3l18 18"></path></svg></span></div>'),
 ('PlataRefuzata.dc.html',29,'<span class="shake" style="align-self: center; position: relative; display: block">'+zee('ups',110)+'<span style="position: absolute; right: -8px; bottom: 12px; width: 38px; height: 38px; border-radius: 19px; background: #FFE5E3; color: #D70015; display: flex; align-items: center; justify-content: center; border: 3px solid #FFFFFF"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="3"></rect><path d="M3 10h18"></path></svg></span></span>'),
 ('GPSOprit.dc.html',30,'<span class="zf" style="position: relative; display: block">'+zee('cauta',100)+'</span>'),
 ('OfertaPierduta.dc.html',30,'<span class="zf" style="display: block">'+zee('trist',100)+'</span>'),
 ('Anulare.dc.html',57,'<span class="pop" style="display: block">'+zee('trist',96)+'</span>'),
 ('Plata.dc.html',70,'<span class="pop" style="position: relative; display: block">'+zee('sarbatoare',118)+'<span style="position: absolute; right: -4px; bottom: 10px; width: 38px; height: 38px; border-radius: 19px; background: #34C759; display: flex; align-items: center; justify-content: center; border: 3px solid #FFFFFF"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg></span></span>'),
 ('Permisiuni.dc.html',25,'<div class="pop" style="display: block">'+zee('salut',96,'','zw')+'</div>'),
 ('GolActivitate.dc.html',27,'<div class="u d1" style="position: relative; height: 210px; margin-top: 10px; display: flex; align-items: center; justify-content: center"><span style="position: absolute; width: 190px; height: 190px; border-radius: 95px; background: #FFF4E5"></span><img src="assets/services/service-curatenie.webp" alt="" class="zf" style="position: absolute; left: 44px; top: 30px; width: 54px; height: 54px; border-radius: 27px; object-fit: cover; border: 3px solid #FFFFFF; box-shadow: 0 8px 20px rgba(0,0,0,0.12)"><img src="assets/services/service-mobila.webp" alt="" class="zf" style="position: absolute; right: 40px; top: 120px; width: 60px; height: 60px; border-radius: 30px; object-fit: cover; border: 3px solid #FFFFFF; box-shadow: 0 8px 20px rgba(0,0,0,0.12); animation-delay: -1.5s"><span style="position: relative" class="zw">'+zee('salut',130)+'</span></div>'),
 ('GolMesaje.dc.html',27,'<div class="u d1" style="position: relative; height: 200px; margin-top: 20px; display: flex; align-items: center; justify-content: center"><span style="position: absolute; width: 180px; height: 180px; border-radius: 90px; background: #E9E9EB"></span><span class="zf" style="position: relative">'+zee('doarme',126)+'</span></div>'),
]
for f,l,new in jobs:
    rep_line(f,l,new); addcss(f)
# FaraOferte: radar center
p=os.path.join(D,'FaraOferte.dc.html'); s=open(p).read()
i=s.index('<span style="position: absolute; left: 86px; top: 86px; width: 48px; height: 48px')
ln=s[:i].count('\n')+1; open(p,'w').write(s)
rep_line('FaraOferte.dc.html',ln,'<span style="position: absolute; left: 66px; top: 58px">'+zee('cauta',88)+'</span>')
# GolIncasari: Zee with coin on dark card
p=os.path.join(D,'GolIncasari.dc.html'); s=open(p).read()
s=s.replace('<span style="font-size: 13px; color: #AEAEB2; font-weight: 600">ÎNCĂ 0 LEI</span>','<img src="assets/mascot/zee-bani.svg" alt="" class="zf" style="position: absolute; right: 14px; bottom: 6px; width: 92px; height: 100px"><span style="font-size: 13px; color: #AEAEB2; font-weight: 600">ÎNCĂ 0 LEI</span>',1)
open(p,'w').write(s); addcss('GolIncasari.dc.html')
# Dialog: AI avatar = Zee thinking
p=os.path.join(D,'Dialog.dc.html'); s=open(p).read()
i=s.index('<span class="glow" style="width: 36px; height: 36px; border-radius: 18px; background: #FFF4E5')
ln=s[:i].count('\n')+1; open(p,'w').write(s)
rep_line('Dialog.dc.html',ln,'<span style="width: 40px; height: 40px; border-radius: 20px; background: #FFF4E5; display: flex; align-items: center; justify-content: center; flex-shrink: 0"><img src="assets/mascot/zee-gandeste.svg" alt="" class="zf" style="width: 30px; height: 33px"></span>')
addcss('Dialog.dc.html')
# Logo mark instead of the old "J" squares
MARK='<svg width="26" height="26" viewBox="0 0 48 48" aria-hidden="true"><path d="M24 3C14.6 3 7 10.4 7 19.6 7 31 24 45 24 45s17-14 17-25.4C41 10.4 33.4 3 24 3z" fill="#FF9F0A"></path><path d="M28.6 12.5v10.6a6.6 6.6 0 0 1-12.4 3.2" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"></path></svg>'
for f in ['FaraOferte.dc.html','Incasari.dc.html','Mesaje.dc.html','Plata.dc.html']:
    p=os.path.join(D,f); s=open(p).read()
    s2=re.sub(r'(<span style="[^"]*?)background: #FF9F0A; color: #FFFFFF;([^"]*)">J</span>', lambda m: m.group(1)+'background: #FFFFFF; box-shadow: inset 0 0 0 1px #E5E5EA;'+m.group(2)+'">'+MARK+'</span>', s)
    print(f, s!=s2, s2.count('>J</span>')); open(p,'w').write(s2)
