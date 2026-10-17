import re, sys, json, os
from playwright.sync_api import sync_playwright
PROJ='jobzee-design/project'
names=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":390,"height":1320}, device_scale_factor=1)
    for n in names:
        ov='{}'
        if ':' in n: n,ov=n.split(':',1)
        src=open(os.path.join(PROJ,n+'.dc.html')).read()
        style=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
        body=re.search(r'</helmet>(.*)</x-dc>',src,re.S).group(1)
        js=re.search(r'data-dc-script[^>]*>(.*?)</script>',src,re.S).group(1)
        vals=pg.evaluate("""([js,ov])=>{class DCLogic{constructor(p){this.props=p||{};this.state={}} setState(){}}
          const C=eval('('+js.replace('class Component','class')+')'); const c=new C({}); Object.assign(c.state,JSON.parse(ov)); const v=c.renderVals(); const o={};
          for(const k in v){o[k]= typeof v[k]==='function'?'':(typeof v[k]==='object'?JSON.parse(JSON.stringify(v[k])):v[k])} return o}""", [js,ov])
        def ev(expr):
            expr=expr.strip()
            if expr in vals: return vals[expr]
            if expr in ('true','false'): return expr=='true'
            return ''
        def scif(m):
            v=ev(m.group(1)); return m.group(2) if v else ''
        def scfor(m):
            lst=vals.get(m.group(1).strip()) or []; var=m.group(2); inner=m.group(3); out=''
            for it in lst:
                out+=re.sub(r'\{\{\s*'+var+r'\.(\w+)\s*\}\}',lambda mm:str((it or {}).get(mm.group(1),'')),inner)
            return out
        body=re.sub(r'<sc-for list="\{\{(.*?)\}\}" as="(\w+)"[^>]*>(.*?)</sc-for>',scfor,body,flags=re.S)
        for _ in range(3):
            body=re.sub(r'<sc-if value="\{\{(.*?)\}\}"[^>]*>(.*?)</sc-if>',scif,body,flags=re.S)
        body=re.sub(r'\{\{(.*?)\}\}',lambda m:str(ev(m.group(1))).replace('True','true').replace('False','false'),body)
        html='<!doctype html><html><head><meta charset="utf-8"><style>'+style+'</style></head><body>'+body+'</body></html>'
        open(os.path.join(PROJ,'_prev.html'),'w').write(html)
        pg.goto('http://127.0.0.1:8765/_prev.html'); pg.wait_for_timeout(4200)
        pg.screenshot(path='shots/'+n+('_'+re.sub(r'[^a-z0-9]','',ov)[:20] if ov!='{}' else '')+'.png')
    b.close()
