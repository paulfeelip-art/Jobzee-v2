import sys, re, os
from playwright.sync_api import sync_playwright
P='jobzee-design/project'
name=sys.argv[1]; acts=sys.argv[2:]
src=open(os.path.join(P,name+'.dc.html')).read().replace('<script src="./support.js"></script>','<script src="./_rt.js"></script>')
open(os.path.join(P,'_t.html'),'w').write(src)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':int(os.environ.get('VH','844'))})
    logs=[]; pg.on('console', lambda m: logs.append(m.type+': '+m.text)); pg.on('pageerror', lambda e: logs.append('ERR '+str(e)))
    pg.goto('http://127.0.0.1:8765/_t.html'); pg.wait_for_timeout(1500)
    for i,a in enumerate(acts):
        k,v=a.split('=',1)
        if k=='click':
            l=pg.get_by_role('button', name=v, exact=True)
            (l.first if l.count() else pg.get_by_role('button', name=re.compile(re.escape(v))).first).click()
        elif k=='type': pg.fill('#msg-in', v); pg.press('#msg-in','Enter')
        elif k=='q': pg.fill('input[placeholder^="Caută"]', v)
        elif k=='wait': pg.wait_for_timeout(int(v))
        elif k=='shot': pg.screenshot(path='shots/rt_%s_%s.png'%(name,v))
        elif k=='text': print('TEXT:', pg.inner_text('body')[:3000])
        pg.wait_for_timeout(200)
    print('\n'.join(logs[:20]))
    b.close()
