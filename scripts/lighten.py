import re, sys, glob, os
MAP={'800':'700','700':'600','600':'500'}
pat=re.compile(r'(font-weight:\s*|font:\s*|font-weight=")(800|700|600)\b')
def fix(s): return pat.sub(lambda m: m.group(1)+MAP[m.group(2)], s)
gen=set('Splash SplashDark Main MainDark Email Rol RolDark SchimbaRol SchimbaRolDark Acasa AcasaDark Castig CastigDark Cont ContJobzer Fisa Servicii Radar RadarDark Mascota'.split())
# 1) generator source
for p in ['gen_roles.py']:
    s=open(p).read(); n=len(pat.findall(s)); open(p,'w').write(fix(s)); print(p,n)
# 2) hand-written boards
tot=0
for p in sorted(glob.glob('jobzee-design/project/*.dc.html')):
    name=os.path.basename(p)[:-8]
    if name in gen: continue
    s=open(p).read(); n=len(pat.findall(s)); tot+=n; open(p,'w').write(fix(s))
print('boards',tot)
