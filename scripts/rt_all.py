import os, re, json
from playwright.sync_api import sync_playwright
P='jobzee-design/project'
c=json.load(open(P+'/canvas.json')); names=list(c['boards'])
res={}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844})
    cur={'err':[],'miss':set()}
    pg.on('console', lambda m: cur['err'].append(m.text[:160]) if m.type=='error' and '404' not in m.text else None)
    pg.on('pageerror', lambda e: cur['err'].append('PAGEERR '+str(e)[:160]))
    pg.on('response', lambda r: cur['miss'].add(r.url.split('8765/')[-1]) if r.status==404 else None)
    for n in names:
        src=open(os.path.join(P,n)).read().replace('<script src="./support.js"></script>','<script src="./_rt.js"></script>')
        open(os.path.join(P,'_t.html'),'w').write(src)
        cur['err']=[]; cur['miss']=set()
        pg.goto('http://127.0.0.1:8765/_t.html'); pg.wait_for_timeout(900)
        t=pg.inner_text('body')
        holes=sorted(set(re.findall(r'\{\{[^}]*\}\}',t)))
        # elements overflowing root horizontally
        ov=pg.evaluate("""()=>{const r=document.querySelector('.th')||document.querySelector('x-dc *');if(!r)return 0;const R=r.getBoundingClientRect();let n=0;r.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect();if(b.width>0&&(b.right>R.right+2)&&getComputedStyle(e).position!=='absolute')n++});return n}""")
        small=pg.evaluate("""()=>{let n=0;document.querySelectorAll('button,a').forEach(e=>{const b=e.getBoundingClientRect();if(b.width>0&&b.height>0&&(b.height<32||b.width<32))n++});return n}""")
        res[n]=dict(holes=holes,err=cur['err'][:3],miss=sorted(m for m in cur['miss'] if 'woff' not in m and 'favicon' not in m),ov=ov,small=small)
    b.close()
os.remove(os.path.join(P,'_t.html'))
json.dump(res,open('audit_rt.json','w'),ensure_ascii=False,indent=1)
bad={k:v for k,v in res.items() if v['holes'] or v['err'] or v['miss']}
print(len(res),'rendered;',len(bad),'with issues')
for k,v in bad.items(): print(k,v)
print('overflow boards:',{k:v['ov'] for k,v in res.items() if v['ov']})
print('small targets total:',sum(v['small'] for v in res.values()))
