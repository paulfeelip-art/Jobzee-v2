

# ---------------------------------------------------------------- Cont cerut abia la trimiterea cererii (client vizitator)
def cont_trimitere():
    btn = 'display: flex; align-items: center; justify-content: center; gap: 10px; height: 54px; border-radius: 27px; font-size: 17px; font-weight: 500; text-decoration: none'
    ghost = ''.join('<div style="height: %dpx; border-radius: 24px; background: var(--surf)"></div>' % h for h in (76, 120, 110, 150))
    b = '''<div style="padding: 52px 16px 0; display: flex; flex-direction: column; gap: 12px; filter: blur(3px); opacity: .7">
  <div style="height: 40px"></div><span style="font-size: 32px; font-weight: 600; letter-spacing: -0.8px">Fișa cererii</span>''' + ghost + '''
</div>
<div class="u" style="position: absolute; inset: 0; background: var(--scrim); animation-duration: .35s"></div>
<div class="sheet" style="position: absolute; left: 8px; right: 8px; bottom: 8px; background: var(--glass2); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px); border-radius: 40px; padding: 12px 16px 18px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 -10px 40px var(--shadow)">
  <span style="align-self: center; width: 38px; height: 5px; border-radius: 3px; background: var(--ink3)"></span>
  <div style="display: flex; align-items: center; gap: 14px; padding: 4px 4px 6px">
    <img class="pop" src="assets/mascot/zee-fericit.svg" alt="" style="width: 70px; height: 76px; flex-shrink: 0">
    <span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.5px">Cererea e gata</span><span style="font-size: 14px; line-height: 1.4; color: var(--ink2)">Salvează-o într-un cont ca Jobzerii să-ți trimită oferte și să te putem anunța. Durează 10 secunde.</span></span>
  </div>
  <div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 20px; background: var(--surf)">
    <img src="assets/services/service-mobila.webp" alt="" style="width: 40px; height: 40px; border-radius: 20px; object-fit: cover">
    <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 500">Montaj birou + dulap mic</span><span style="font-size: 12px; color: var(--ink2)">Urgent · Floreasca · estimare 120–220 lei</span></span>
    <span style="font-size: 12px; font-weight: 500; color: var(--oktext)">✓ păstrată</span>
  </div>
  <a href="Radar.dc.html" class="pr" style="''' + btn + '''; background: var(--invbg); color: var(--invink)">''' + APPLE + '''Continuă cu Apple</a>
  <a href="Radar.dc.html" class="pr" style="''' + btn + '''; background: var(--surf); color: var(--ink); box-shadow: inset 0 0 0 1px var(--sep)">''' + GOOGLE + '''Continuă cu Google</a>
  <a href="Telefon.dc.html" class="pr" style="''' + btn + '''; background: var(--brand); color: var(--onbrand)">''' + PHONE + '''Cu numărul de telefon</a>
  <p style="margin: 2px 0 0; text-align: center; font-size: 12px; line-height: 1.4; color: var(--ink2)">Numărul tău nu e arătat Jobzerilor. Continuând, accepți <a href="#termeni" style="color: inherit">Termenii</a>.</p>
</div>'''
    return page('Cont la trimitere', 'L', b)
