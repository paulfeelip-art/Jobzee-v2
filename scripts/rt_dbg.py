import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':844})
    pg.on('console', lambda m: print('LOG', m.type, m.text[:300]))
    pg.on('pageerror', lambda e: print('ERR', e))
    pg.goto('http://127.0.0.1:8765/'+sys.argv[1]); pg.wait_for_timeout(2500)
    print(pg.inner_text('body')[:300].replace('\n','|'))
    b.close()
