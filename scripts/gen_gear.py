

# ================================================================ JOBZEE GEAR & GROWTH (Jobzer side, entered from Profil)
_QN, _QP = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qr_path.txt')).read().split('|', 1)


def qr(size=96, fg='#1C1C1E', bg='#FFFFFF'):
    n = int(_QN)
    return ('<svg width="%d" height="%d" viewBox="-2 -2 %d %d" aria-label="Cod QR spre profilul public" role="img" style="display: block; border-radius: 8px; background: %s">'
            '<path d="%s" fill="%s" shape-rendering="crispEdges"></path></svg>') % (size, size, n + 4, n + 4, bg, _QP, fg)


def ui(name, size=24, extra=''):
    return '<img src="assets/ui/%s.png" alt="" style="width: %dpx; height: %dpx; display: block; flex-shrink: 0; %s">' % (name, size, size, extra)


def tile(name, size=56, tint='var(--bsoft)', isz=None):
    return ('<span style="width: %dpx; height: %dpx; border-radius: %dpx; background: %s; display: flex; align-items: center; justify-content: center; flex-shrink: 0">%s</span>'
            % (size, size, int(size * 0.3), tint, ui(name, isz or int(size * 0.55))))


def gtab():
    return tabbar('jobzer', 'cont', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})


GEAR_CSS = SEG_CSS + """
.badge{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:11px;font-size:11px;font-weight:500;white-space:nowrap}
.b-ok{background:var(--oksoft);color:var(--oktext)}.b-mto{background:var(--bsoft);color:var(--btext)}.b-q{background:var(--surf2);color:var(--ink2)}
.card{background:var(--surf);border-radius:24px;padding:14px;display:flex;flex-direction:column;gap:8px;text-decoration:none;color:var(--ink)}
.cta{display:flex;align-items:center;justify-content:center;height:56px;border-radius:28px;background:var(--brand);color:var(--onbrand);font-size:17px;font-weight:500;text-decoration:none;border:0;font-family:inherit;cursor:pointer;box-shadow:0 10px 24px rgba(255,159,10,0.3)}
.cta2{display:flex;align-items:center;justify-content:center;height:50px;border-radius:25px;background:var(--surf);color:var(--ink);font-size:16px;font-weight:500;text-decoration:none;border:0;font-family:inherit;cursor:pointer}
.note{font-size:12px;line-height:1.4;color:var(--ink2);padding:0 6px}
.qty{display:flex;align-items:center;height:30px;border-radius:15px;background:var(--surf2)}
.qty button{width:30px;height:30px;border:0;background:transparent;font-size:17px;color:var(--ink);cursor:pointer;font-family:inherit}
"""

KIT_MONTAJ = [
    dict(k='surub', n='Șurubelniță cu 32 de biți', s='Mâner cu clichet · biți PH, PZ, Torx', p=89, ic='work_tools', av='ok', lvl='s'),
    dict(k='imbus', n='Set chei imbus (9 buc.)', s='1,5–10 mm · oțel CrV', p=39, ic='repair', av='ok', lvl='s'),
    dict(k='nivela', n='Nivelă 60 cm', s='3 bule · magnetică', p=59, ic='match', av='ok', lvl='s'),
    dict(k='ruleta', n='Ruletă 5 m', s='Bandă 19 mm · frână automată', p=35, ic='route', av='ok', lvl='s'),
    dict(k='ciocan', n='Ciocan 300 g', s='Mâner din fibră de sticlă', p=49, ic='repair', av='q', lvl='s'),
    dict(k='cutie', n='Cutie organizator', s='Compartimente reglabile', p=79, ic='briefcase', av='ok', lvl='s'),
    dict(k='masina', n='Mașină de înșurubat 18 V', s='2 acumulatori · 50 Nm', p=499, ic='work_tools', av='ok', lvl='p'),
    dict(k='burghie', n='Set burghie (15 buc.)', s='Lemn, metal, beton', p=69, ic='repair', av='ok', lvl='p'),
    dict(k='detector', n='Detector cabluri și profile', s='Metal, lemn, tensiune', p=129, ic='radar', av='q', lvl='p'),
    dict(k='genunchiere', n='Genunchiere de lucru', s='Gel · reglabile', p=59, ic='shield', av='ok', lvl='p'),
]


def gear_hub():
    mods = [('GearKituri.dc.html', 'work_tools', 'Kituri Jobzee', 'Trusa potrivită pe ce faci', 'Starter · Pro · Custom'),
            ('GearShop.dc.html', 'repair', 'Gear Shop', 'Unelte și consumabile', 'De la parteneri'),
            ('GearIdentity.dc.html', 'profile', 'Identity', 'Haine și ecusoane cu numele tău', 'Se face la comandă'),
            ('PrintStudio.dc.html', 'sparkles', 'Print Studio', 'Cărți de vizită, flyere, QR', 'PDF gratuit')]
    cards = ''.join('<a href="%s" class="card pr u d%d" style="min-height: 132px">%s<span style="font-size: 16px; font-weight: 600; margin-top: 4px">%s</span><span style="font-size: 13px; color: var(--ink2); line-height: 1.3">%s</span><span class="badge b-q" style="align-self: flex-start; margin-top: auto">%s</span></a>'
                    % (h, i + 1, tile(icn, 44), t, s, b) for i, (h, icn, t, s, b) in enumerate(mods))
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('ContJobzer.dc.html', '<a href="GearCos.dc.html" aria-label="Coș, 2 produse" class="pr" style="position: relative; width: 40px; height: 40px; border-radius: 20px; background: var(--surf); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px var(--shadow)">' + ui('wallet', 22) + '<span style="position: absolute; right: -3px; top: -3px; min-width: 18px; height: 18px; border-radius: 9px; background: var(--brand); color: var(--onbrand); font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center">2</span></a>') + '''
  <div class="u" style="display: flex; align-items: flex-end; gap: 10px">
    <span style="flex-grow: 1"><span style="font-size: 13px; font-weight: 500; color: var(--btext)">JOBZEE GEAR &amp; GROWTH</span><h1 style="margin: 2px 0 0; font-size: 30px; line-height: 1.1; font-weight: 600; letter-spacing: -0.8px">Echipează-te și fă-te cunoscut</h1></span>
    <img src="assets/mascot/zee-bani.png" alt="" style="width: 92px; height: 100px; flex-shrink: 0">
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px">''' + cards + '''</div>
  <a href="GearGrowth.dc.html" class="card pr u d5" style="flex-direction: row; align-items: center; gap: 12px">
    <span style="position: relative; width: 52px; height: 52px; flex-shrink: 0"><svg width="52" height="52" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="22" fill="none" stroke="var(--surf3)" stroke-width="6"></circle><circle cx="26" cy="26" r="22" fill="none" stroke="var(--brand)" stroke-width="6" stroke-linecap="round" stroke-dasharray="138" stroke-dashoffset="28" transform="rotate(-90 26 26)"></circle></svg><span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600">80%</span></span>
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Growth</span><span style="font-size: 13px; color: var(--ink2)">Profil 80% complet · 14 scanări QR în 30 de zile</span></span>''' + CHEV + '''
  </a>
  <div class="grp u d6">
    <a href="GearUrmarire.dc.html" class="rw pr">''' + ui('delivery', 26) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Comanda JZ-1042</span><span style="font-size: 12px; color: var(--ink2)">1 pachet expediat · 1 în producție</span></span>''' + CHEV + '''</a>
    <a href="GearDesignuri.dc.html" class="rw pr">''' + ui('photo', 26) + '''<span style="flex-grow: 1; font-size: 15px">Designurile mele</span><span style="font-size: 14px; color: var(--ink2)">2</span>''' + CHEV + '''</a>
    <a href="GearEchipament.dc.html" class="rw pr">''' + ui('briefcase', 26) + '''<span style="flex-grow: 1; font-size: 15px">Echipamentul meu</span><span style="font-size: 14px; color: var(--ink2)">7</span>''' + CHEV + '''</a>
  </div>
  <span class="note">Cumpărăturile nu schimbă locul tău în Radar sau în oferte. Potrivirea ține doar de skill-uri, distanță, disponibilitate și recenzii.</span>
</div>
''' + gtab()
    return page('Gear & Growth', 'L', b, GEAR_CSS, h=1000)


def gear_kituri():
    kits = [('work_tools', 'Montaj', 'Montaj mobilier · Reparații mici', '350', '6', True), ('cleaning', 'Curățenie', 'Curățenie · Geamuri · Călcat', '289', '9', False),
            ('moving', 'Mutat', 'Mutat și cărat · Livrări', '245', '5', False), ('it', 'Tech', 'IT și tehnică', '199', '6', False),
            ('garden', 'Grădină', 'Grădină și curte', '269', '6', False), ('sparkles', 'Zugrăveli', 'Zugrăveli · Gresie', '219', '7', False),
            ('offer', 'Evenimente', 'Evenimente', '179', '5', False), ('repair', 'Handyman', 'Instalații · Electricitate', '329', '7', False)]
    rows = ''.join('<a href="%s" class="card pr" style="flex-direction: row; align-items: center; gap: 12px; padding: 12px %s">%s<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; align-items: center; gap: 6px; font-size: 16px; font-weight: 600">Kit %s%s</span><span style="font-size: 12px; color: var(--ink2)">%s</span><span style="font-size: 13px">Starter de la <b style="font-weight: 600">%s lei</b> · %s produse</span></span>%s</a>'
                   % ('GearKit.dc.html' if mine else 'GearKit.dc.html', '; box-shadow: inset 0 0 0 2px var(--brand)' if mine else '', tile(ic_, 52), t, ' <span class="badge b-mto">Pe skill-urile tale</span>' if mine else '', fam, p, n, CHEV)
                   for ic_, t, fam, p, n, mine in kits)
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearHub.dc.html', '<a href="GearBuilder.dc.html" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--invbg); color: var(--invink); display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500; text-decoration: none">✦ Construiește-l tu</a>') + '''
  ''' + h1('Kituri Jobzee', 'Starter, Pro sau Custom. Vezi fiecare produs și scoate ce ai deja.') + '''
  <div class="u d1" style="display: flex; flex-direction: column; gap: 8px">''' + rows + '''</div>
  <span class="note">Un kit nu adaugă skill-uri și nu e o certificare. Prețurile și stocul vin de la parteneri.</span>
</div>
''' + gtab()
    return page('Kituri Jobzee', 'L', b, GEAR_CSS, h=1080)


def gear_kit():
    logic = ("""constructor(props) { super(props); this.state = { lvl: 's', own: { ruleta: true } }; }
  renderVals() {
    const s = this.state, all = """ + json.dumps(KIT_MONTAJ, ensure_ascii=False) + """;
    const lei = v => v.toFixed(2).replace('.', ',') + ' lei';
    const shown = all.filter(x => s.lvl === 's' ? x.lvl === 's' : true);
    const items = shown.map(x => { const own = !!s.own[x.k]; return { n: x.n, sp: x.s, p: lei(x.p), icon: 'assets/ui/' + x.ic + '.png',
      av: x.av === 'ok' ? 'Disponibil la partener' : 'Se confirmă după comandă', avc: 'badge ' + (x.av === 'ok' ? 'b-ok' : 'b-q'),
      attr: own ? 'true' : 'false', toggle: () => { const o = Object.assign({}, s.own); o[x.k] = !o[x.k]; this.setState({ own: o }); },
      rowStyle: 'display: flex; align-items: center; gap: 10px; padding: 10px 12px 10px 0; margin-left: 12px; transition: opacity .25s; ' + (own ? 'opacity: .45' : '') }; });
    const keep = shown.filter(x => !s.own[x.k]);
    const tot = keep.reduce((a, x) => a + x.p, 0), saved = shown.length - keep.length;
    const l = k => ({ attr: s.lvl === k ? 'true' : 'false', pick: () => this.setState({ lvl: k }) });
    return { items, lS: l('s'), lP: l('p'), total: lei(tot), count: keep.length + ' produse', savedTxt: saved ? saved + ' scoase pentru că le ai deja' : 'Bifează „Am deja” ca să scoți un produs' };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearKituri.dc.html', '<span class="badge b-mto">Pe skill-urile tale</span>') + '''
  <div class="u" style="display: flex; align-items: center; gap: 12px">''' + tile('work_tools', 60) + '''<span><h1 style="margin: 0; font-size: 28px; font-weight: 600; letter-spacing: -0.7px">Kit Montaj</h1><span style="font-size: 13px; color: var(--ink2)">Montaj mobilier · Reparații mici · Tâmplărie</span></span></div>
  <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><button type="button" onClick="{{lS.pick}}" aria-pressed="{{lS.attr}}">Starter</button><button type="button" onClick="{{lP.pick}}" aria-pressed="{{lP.attr}}">Pro</button><a href="GearBuilder.dc.html" style="display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 500; color: var(--btext); text-decoration: none">Custom ›</a></div>
  <div style="display: flex; justify-content: space-between; padding: 0 6px"><span class="lbl" style="padding: 0">Ce conține · {{count}}</span><span style="font-size: 12px; color: var(--ink2)">Am deja</span></div>
  <div class="grp">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="6">
      <div style="{{x.rowStyle}}; border-bottom: 0.5px solid var(--sep)">
        <span style="width: 44px; height: 44px; border-radius: 13px; background: var(--bsoft); display: flex; align-items: center; justify-content: center; flex-shrink: 0"><img src="{{x.icon}}" alt="" style="width: 24px; height: 24px"></span>
        <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 500">{{x.n}}</span><span style="font-size: 11px; color: var(--ink2)">{{x.sp}}</span><span class="{{x.avc}}" style="align-self: flex-start">{{x.av}}</span></span>
        <span style="font-size: 14px; font-variant-numeric: tabular-nums; white-space: nowrap">{{x.p}}</span>
        <button type="button" class="jsw" onClick="{{x.toggle}}" aria-pressed="{{x.attr}}" aria-label="Am deja"></button>
      </div>
    </sc-for>
  </div>
  <span class="note">{{savedTxt}}. Kitul nu certifică skill-uri. Livrare de la partener: 2–4 zile lucrătoare, confirmată la comandă.</span>
</div>
<div class="glass" style="position: absolute; left: 0; right: 0; bottom: 0; padding: 12px 16px 30px; display: flex; align-items: center; gap: 12px; box-shadow: 0 -8px 24px var(--shadow)">
  <span style="display: flex; flex-direction: column"><span style="font-size: 12px; color: var(--ink2)">Total cu TVA</span><span style="font-size: 22px; font-weight: 600; font-variant-numeric: tabular-nums">{{total}}</span></span>
  <a href="GearCos.dc.html" class="cta pr" style="flex-grow: 1; height: 52px">Adaugă în coș</a>
</div>'''
    return page('Detaliu kit', 'L', b, GEAR_CSS, logic, h=1060)


def gear_builder():
    logic = """constructor(props) { super(props); this.state = { step: 0, svc: { m: true, r: true }, have: { ruleta: true, ciocan: true }, lvl: '' }; }
  renderVals() {
    const s = this.state;
    const svc = [['m', 'Montaj mobilier'], ['r', 'Reparații mici'], ['t', 'Tâmplărie'], ['c', 'Curățenie']].map(([k, n]) => ({ n, attr: s.svc[k] ? 'true' : 'false', pick: () => { const o = Object.assign({}, s.svc); o[k] = !o[k]; this.setState({ svc: o }); } }));
    const have = [['surub', 'Șurubelniță'], ['imbus', 'Chei imbus'], ['ruleta', 'Ruletă'], ['ciocan', 'Ciocan'], ['nivela', 'Nivelă']].map(([k, n]) => ({ n, attr: s.have[k] ? 'true' : 'false', pick: () => { const o = Object.assign({}, s.have); o[k] = !o[k]; this.setState({ have: o }); } }));
    const lv = (k, t) => ({ t, attr: s.lvl === k ? 'true' : 'false', pick: () => this.setState({ lvl: k, step: 3 }) });
    const owned = Object.keys(s.have).filter(k => s.have[k]).length;
    const base = s.lvl === 'p' ? 1106 : 350, minus = (s.have.ruleta ? 35 : 0) + (s.have.ciocan ? 49 : 0) + (s.have.surub ? 89 : 0) + (s.have.imbus ? 39 : 0) + (s.have.nivela ? 59 : 0);
    const tot = Math.min(base - minus, s.lvl === 'b' ? 300 : 99999);
    return { svc, have, l1: lv('s', 'Starter'), l2: lv('p', 'Pro'), l3: lv('b', 'Buget: 300 lei'),
      s1: s.step >= 1, s2: s.step >= 2, s3: s.step >= 3, s0only: s.step === 0, s1only: s.step === 1, s2only: s.step === 2,
      next1: () => this.setState({ step: 1 }), next2: () => this.setState({ step: 2 }), reset: () => this.setState({ step: 0, lvl: '' }),
      svcTxt: svc.filter(x => x.attr === 'true').map(x => x.n).join(', ') || 'nimic ales', haveTxt: owned ? owned + ' unelte le ai deja' : 'Nu am nimic încă',
      lvlTxt: s.lvl === 'p' ? 'Pro' : s.lvl === 'b' ? 'Buget 300 lei' : 'Starter',
      total: tot.toFixed(2).replace('.', ',') + ' lei', why: 'Am scos ' + owned + ' unelte pe care le ai. Fiecare produs rămas apare pentru că oferi ' + (svc.find(x => x.attr === 'true') || { n: 'Montaj mobilier' }).n + '.' };
  }"""
    bub_ai = lambda t: '<div class="u" style="align-self: flex-start; max-width: 82%; padding: 10px 14px; border-radius: 20px 20px 20px 6px; background: var(--surf); font-size: 15px; line-height: 1.35">' + t + '</div>'
    bub_me = lambda t: '<div class="u" style="align-self: flex-end; max-width: 82%; padding: 10px 14px; border-radius: 20px 20px 6px 20px; background: var(--brand); color: var(--onbrand); font-size: 15px">' + t + '</div>'
    chips = lambda lst: '<div class="u" style="display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-end"><sc-for list="{{' + lst + '}}" as="c" hint-placeholder-count="4"><button type="button" class="fc" onClick="{{c.pick}}" aria-pressed="{{c.attr}}">{{c.n}}</button></sc-for></div>'
    b = '''<div style="padding: 52px 16px 24px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 8px">
  <div style="display: flex; align-items: center; gap: 10px; padding-bottom: 6px">''' + topbar('GearKituri.dc.html') + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600">Smart Kit Builder</span><span style="font-size: 12px; color: var(--ink2)">3 întrebări · sub un minut</span></span><img src="assets/mascot/zee-gandeste.png" alt="" style="width: 40px; height: 43px"></div>
  ''' + bub_ai('Ce servicii oferi? Am bifat ce e deja în profilul tău.') + chips('svc') + '''
  <sc-if value="{{s0only}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{next1}}" class="cta2 pr" style="align-self: flex-end; height: 40px; padding: 0 18px; background: var(--invbg); color: var(--invink)">Gata ›</button></sc-if>
  <sc-if value="{{s1}}" hint-placeholder-val="{{ false }}">''' + bub_me('{{svcTxt}}') + bub_ai('Ce ai deja? Nu-ți propun ce ai.') + chips('have') + '''
    <sc-if value="{{s1only}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 6px; justify-content: flex-end"><button type="button" onClick="{{next2}}" class="fc">Nu știu, arată-mi tot</button><button type="button" onClick="{{next2}}" class="cta2 pr" style="height: 36px; padding: 0 16px; background: var(--invbg); color: var(--invink); font-size: 14px">Gata ›</button></div></sc-if></sc-if>
  <sc-if value="{{s2}}" hint-placeholder-val="{{ false }}">''' + bub_me('{{haveTxt}}') + bub_ai('Ce nivel vrei?') + '''
    <div class="u" style="display: flex; gap: 6px; justify-content: flex-end"><button type="button" class="fc" onClick="{{l1.pick}}" aria-pressed="{{l1.attr}}">{{l1.t}}</button><button type="button" class="fc" onClick="{{l2.pick}}" aria-pressed="{{l2.attr}}">{{l2.t}}</button><button type="button" class="fc" onClick="{{l3.pick}}" aria-pressed="{{l3.attr}}">{{l3.t}}</button></div></sc-if>
  <div style="flex-grow: 1"></div>
  <sc-if value="{{s3}}" hint-placeholder-val="{{ false }}">
    <div class="pop card" style="box-shadow: inset 0 0 0 2px var(--brand)">
      <span style="display: flex; align-items: center; gap: 10px">''' + tile('work_tools', 44) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 600">Kitul tău · {{lvlTxt}}</span><span style="font-size: 12px; color: var(--ink2)">{{why}}</span></span></span>
      <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 13px; color: var(--ink2)">Total estimat cu TVA</span><span style="font-size: 24px; font-weight: 600">{{total}}</span></span>
      <div style="display: flex; gap: 8px"><a href="GearKit.dc.html" class="cta2 pr" style="flex: 1; height: 46px; background: var(--surf2)">Ajustează</a><a href="GearCos.dc.html" class="cta pr" style="flex: 1; height: 46px; font-size: 15px">Adaugă în coș</a></div>
      <button type="button" onClick="{{reset}}" style="border: 0; background: transparent; color: var(--btext); font-family: inherit; font-size: 13px; cursor: pointer">Salvează în „Kiturile mele” și o iau de la capăt</button>
    </div>
  </sc-if>
</div>'''
    return page('Smart Kit Builder', 'L', b, GEAR_CSS + '.fc{border:0;height:34px;padding:0 12px;border-radius:17px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;transition:all .25s}.fc[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}.fc[aria-pressed="false"],.fc:not([aria-pressed]){background:var(--surf);color:var(--ink);box-shadow:inset 0 0 0 1px var(--sep)}', logic)


GEAR_SHOP = [
    dict(n='Biți PH2 · 10 buc.', c='cons', spec='montaj', p='24,00', ic='work_tools', av='ok', d='2–3 zile'),
    dict(n='Mașină de înșurubat 18 V', c='unelte', spec='montaj', p='499,00', ic='work_tools', av='ok', d='2–4 zile'),
    dict(n='Mănuși de protecție · 5 per.', c='prot', spec='curatenie', p='39,00', ic='shield', av='ok', d='2–3 zile'),
    dict(n='Lavete microfibră · 10 buc.', c='cons', spec='curatenie', p='45,00', ic='cleaning', av='ok', d='2–3 zile'),
    dict(n='Chingi de mutat · 4 buc.', c='unelte', spec='mutat', p='79,00', ic='moving', av='q', d='se confirmă'),
    dict(n='Ochelari de protecție', c='prot', spec='gradina', p='29,00', ic='shield', av='ok', d='2–3 zile'),
    dict(n='Multimetru digital', c='unelte', spec='handyman', p='119,00', ic='repair', av='q', d='se confirmă'),
    dict(n='Geantă de scule 16"', c='acc', spec='montaj', p='149,00', ic='briefcase', av='ok', d='3–5 zile'),
]


def gear_shop():
    logic = ("""constructor(props) { super(props); this.state = { f: 'montaj' }; }
  renderVals() {
    const all = """ + json.dumps(GEAR_SHOP, ensure_ascii=False) + """, f = this.state.f;
    const items = all.filter(x => f === 'all' || x.spec === f).map(x => Object.assign({}, x, { icon: 'assets/ui/' + x.ic + '.png', avc: 'badge ' + (x.av === 'ok' ? 'b-ok' : 'b-q'), avt: x.av === 'ok' ? 'Disponibil' : 'Se confirmă', dd: 'Livrare ' + x.d }));
    const ch = (k, n) => ({ n, attr: f === k ? 'true' : 'false', pick: () => this.setState({ f: k }) });
    return { items, chips: [ch('montaj', 'Montaj'), ch('curatenie', 'Curățenie'), ch('mutat', 'Mutat'), ch('handyman', 'Handyman'), ch('all', 'Toate')] };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearHub.dc.html', '<a href="GearCos.dc.html" class="pr" style="height: 36px; padding: 0 12px; border-radius: 18px; background: var(--surf); display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500; text-decoration: none">' + ui('wallet', 18) + 'Coș · 2</a>') + '''
  ''' + h1('Gear Shop') + '''
  <div class="u d1" style="display: flex; align-items: center; gap: 10px; height: 46px; padding: 0 14px; border-radius: 23px; background: var(--surf)">''' + ui('search', 18) + '''<span style="font-size: 15px; color: var(--ink2)">Caută: biți, chingi, mănuși…</span></div>
  <div class="u d1" style="display: flex; gap: 6px; flex-wrap: wrap"><sc-for list="{{chips}}" as="c" hint-placeholder-count="5"><button type="button" class="fc" onClick="{{c.pick}}" aria-pressed="{{c.attr}}">{{c.n}}</button></sc-for></div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="4">
      <a href="GearProdus.dc.html" class="card pr pop" style="padding: 10px; gap: 6px">
        <span style="height: 96px; border-radius: 16px; background: var(--bsoft); display: flex; align-items: center; justify-content: center"><img src="{{x.icon}}" alt="" style="width: 52px; height: 52px"></span>
        <span style="font-size: 13px; font-weight: 500; line-height: 1.25; min-height: 32px">{{x.n}}</span>
        <span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 15px; font-weight: 600">{{x.p}} lei</span><span class="{{x.avc}}">{{x.avt}}</span></span>
        <span style="font-size: 11px; color: var(--ink2)">{{x.dd}}</span>
      </a>
    </sc-for>
  </div>
  <span class="note">Fără „alții au cumpărat”. Recomandăm doar pe specializările din profilul tău.</span>
</div>
''' + gtab()
    return page('Gear Shop', 'L', b, GEAR_CSS + '.fc{border:0;height:34px;padding:0 12px;border-radius:17px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;transition:all .25s}.fc[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}.fc[aria-pressed="false"]{background:var(--surf);color:var(--ink)}', logic, h=1000)


def gear_produs():
    logic = """constructor(props) { super(props); this.state = { q: 1, img: 0 }; }
  renderVals() { const q = this.state.q; return { q, minus: () => this.setState({ q: Math.max(1, q - 1) }), plus: () => this.setState({ q: Math.min(20, q + 1) }), total: (499 * q).toFixed(2).replace('.', ',') + ' lei',
    dots: [0, 1, 2].map(i => ({ st: 'width: ' + (i === this.state.img ? 16 : 6) + 'px; height: 6px; border-radius: 3px; background: ' + (i === this.state.img ? 'var(--brand)' : 'var(--surf3)') + '; transition: all .3s', pick: () => this.setState({ img: i }) })) }; }"""
    spec = [('Tensiune', '18 V'), ('Cuplu maxim', '50 Nm'), ('Acumulatori', '2 × 2,0 Ah, Li-Ion'), ('Greutate', '1,3 kg'), ('Garanție', '24 luni, producător')]
    rows = ''.join('<div class="rw" style="padding-top: 9px; padding-bottom: 9px"><span style="flex-grow: 1; font-size: 14px; color: var(--ink2)">%s</span><span style="font-size: 14px">%s</span></div>' % r for r in spec)
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('GearShop.dc.html', '<button type="button" aria-label="Favorit" class="pr" style="width: 40px; height: 40px; border: 0; border-radius: 20px; background: var(--surf); display: flex; align-items: center; justify-content: center">' + ui('favorite', 20) + '</button>') + '''
  <div class="u" style="height: 220px; border-radius: 30px; background: linear-gradient(160deg, var(--bsoft2), var(--bsoft)); display: flex; align-items: center; justify-content: center; position: relative">''' + ui('work_tools', 120) + '''
    <span style="position: absolute; bottom: 12px; left: 0; right: 0; display: flex; gap: 5px; justify-content: center"><sc-for list="{{dots}}" as="d" hint-placeholder-count="3"><button type="button" onClick="{{d.pick}}" aria-label="Imagine" style="{{d.st}}; border: 0; padding: 0; cursor: pointer"></button></sc-for></span></div>
  <div class="u d1"><span class="badge b-ok">Disponibil la partener · confirmat azi 09:40</span>
    <h1 style="margin: 8px 0 2px; font-size: 24px; line-height: 1.2; font-weight: 600; letter-spacing: -0.5px">Mașină de înșurubat 18 V</h1>
    <span style="font-size: 13px; color: var(--ink2)">Vândut și livrat de un partener Jobzee · retur 14 zile</span></div>
  <div class="u d2" style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 18px; background: var(--bsoft)">''' + ui('match', 22) + '''<span style="font-size: 13px">Folositor pentru <b style="font-weight: 600">Montaj mobilier</b>, din skill-urile tale</span></div>
  <div class="grp u d3">''' + rows + '''</div>
  <div class="grp u d4"><div class="rw">''' + ui('delivery', 22) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 14px">Livrare 2–4 zile lucrătoare</span><span style="font-size: 12px; color: var(--ink2)">Termen dat de partener · transport 19,99 lei</span></span></div></div>
</div>
<div class="glass" style="position: absolute; left: 0; right: 0; bottom: 0; padding: 12px 16px 30px; display: flex; align-items: center; gap: 10px; box-shadow: 0 -8px 24px var(--shadow)">
  <span class="qty"><button type="button" onClick="{{minus}}" aria-label="Mai puțin">−</button><span style="min-width: 22px; text-align: center; font-size: 15px">{{q}}</span><button type="button" onClick="{{plus}}" aria-label="Mai mult">+</button></span>
  <a href="GearCos.dc.html" class="cta pr" style="flex-grow: 1; height: 52px; font-size: 16px">Adaugă · {{total}}</a>
</div>'''
    return page('Detaliu produs', 'L', b, GEAR_CSS, logic, h=980)


def gear_identity():
    logic = """constructor(props) { super(props); this.state = { item: 't', col: 'ink', size: 'L', name: true, spec: true }; }
  renderVals() {
    const s = this.state;
    const C = { ink: ['#292D33', '#FFFFFF'], white: ['#FFFFFF', '#292D33'], orange: ['#FF9B00', '#292D33'] };
    const it = (k, n, p) => ({ n, attr: s.item === k ? 'true' : 'false', pick: () => this.setState({ item: k }), p });
    const items = [it('t', 'Tricou', 79), it('p', 'Polo', 99), it('h', 'Hanorac', 169), it('c', 'Șapcă', 59), it('v', 'Vestă', 89), it('b', 'Ecuson', 25)];
    const cur = items.find(x => x.attr === 'true');
    const cols = Object.keys(C).map(k => ({ st: 'width: 34px; height: 34px; border-radius: 17px; border: 0; cursor: pointer; background: ' + C[k][0] + '; box-shadow: ' + (s.col === k ? '0 0 0 3px var(--bg), 0 0 0 5px var(--brand)' : 'inset 0 0 0 1px var(--sep)'), pick: () => this.setState({ col: k }), lab: k }));
    const sizes = ['S', 'M', 'L', 'XL', 'XXL'].map(z => ({ z, attr: s.size === z ? 'true' : 'false', pick: () => this.setState({ size: z }) }));
    return { items, cols, sizes, fill: C[s.col][0], txt: C[s.col][1], nameOn: s.name, specOn: s.spec,
      nameAttr: s.name ? 'true' : 'false', specAttr: s.spec ? 'true' : 'false', tName: () => this.setState({ name: !s.name }), tSpec: () => this.setState({ spec: !s.spec }),
      cta: 'Adaugă ' + cur.n.toLowerCase() + ' · ' + cur.p + ',00 lei', isBadge: s.item === 'b', notBadge: s.item !== 'b' };
  }"""
    shirt = ('<svg width="210" height="200" viewBox="0 0 210 200" aria-label="Previzualizare produs" role="img"><path d="M60 18 L30 34 L8 70 L36 86 L46 72 L46 190 L164 190 L164 72 L174 86 L202 70 L180 34 L150 18 C140 34 120 40 105 40 C90 40 70 34 60 18 Z" fill="{{fill}}" stroke="rgba(0,0,0,0.12)" stroke-width="1.5"></path>'
             '<image href="assets/brand/jobzee-mark.png" x="66" y="62" width="22" height="28"></image></svg>')
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearHub.dc.html', '<span class="badge b-mto">Se face la comandă · 3–5 zile</span>') + '''
  ''' + h1('Jobzee Identity') + '''
  <div class="u d1" style="display: flex; gap: 6px; overflow: hidden"><sc-for list="{{items}}" as="x" hint-placeholder-count="6"><button type="button" class="fc" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.n}}</button></sc-for></div>
  <div class="u d2" style="position: relative; height: 230px; border-radius: 30px; background: radial-gradient(circle at 50% 40%, var(--surf) 0, var(--surf2) 75%); display: flex; align-items: center; justify-content: center">
    <sc-if value="{{notBadge}}" hint-placeholder-val="{{ true }}"><span style="position: relative; display: block">''' + shirt + '''
      <span style="position: absolute; left: 0; right: 0; top: 104px; display: flex; flex-direction: column; align-items: center; gap: 2px; color: {{txt}}"><sc-if value="{{nameOn}}" hint-placeholder-val="{{ true }}"><span style="font-size: 18px; font-weight: 600; letter-spacing: -0.3px">Mihai I.</span></sc-if><sc-if value="{{specOn}}" hint-placeholder-val="{{ true }}"><span style="font-size: 11px; font-weight: 500; opacity: .8">MONTAJ MOBILIER</span></sc-if></span></span></sc-if>
    <sc-if value="{{isBadge}}" hint-placeholder-val="{{ false }}"><span class="pop" style="width: 150px; height: 200px; border-radius: 18px; background: {{fill}}; color: {{txt}}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; box-shadow: 0 12px 30px rgba(0,0,0,.15)"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 64px; height: 64px; border-radius: 32px; object-fit: cover"><span style="font-size: 16px; font-weight: 600">Mihai I.</span><span style="font-size: 10px; font-weight: 500">JOBZER · MONTAJ</span><span style="background: #FFFFFF; padding: 4px; border-radius: 6px">''' + qr(48) + '''</span></span></sc-if>
  </div>
  <div class="u d3" style="display: flex; align-items: center; justify-content: space-between; padding: 0 4px"><span class="lbl" style="padding: 0">Culoare</span><span style="display: flex; gap: 10px"><sc-for list="{{cols}}" as="c" hint-placeholder-count="3"><button type="button" onClick="{{c.pick}}" aria-label="{{c.lab}}" style="{{c.st}}"></button></sc-for></span></div>
  <div class="u d3" style="display: flex; justify-content: space-between"><sc-for list="{{sizes}}" as="z" hint-placeholder-count="5"><button type="button" class="dchip" onClick="{{z.pick}}" aria-pressed="{{z.attr}}" style="width: 56px">{{z.z}}</button></sc-for></div>
  <div class="grp u d4">
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; font-size: 15px">Numele meu public</span><button type="button" class="jsw" onClick="{{tName}}" aria-pressed="{{nameAttr}}" aria-label="Nume"></button></div>
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; font-size: 15px">Specializarea principală</span><button type="button" class="jsw" onClick="{{tSpec}}" aria-pressed="{{specAttr}}" aria-label="Specializare"></button></div>
  </div>
  <span class="note">Doar date din profilul tău aprobat. Nu tipărim „certificat” sau „verificat” decât dacă e adevărat în Jobzee.</span>
  <a href="GearCos.dc.html" class="cta pr u d5">{{cta}}</a>
</div>'''
    return page('Jobzee Identity', 'L', b, GEAR_CSS + '.fc{border:0;height:34px;padding:0 12px;border-radius:17px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;flex-shrink:0;transition:all .25s}.fc[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}.fc[aria-pressed="false"]{background:var(--surf);color:var(--ink)}', logic, h=1000)


def print_studio():
    items = [('GearCarte.dc.html', 'profile', 'Cărți de vizită', '200 buc. de la 129 lei', '3–4 zile', True), ('GearFlyer.dc.html', 'offer', 'Flyere A5 / A6', '500 buc. de la 189 lei', '3–5 zile', True),
             ('GearFlyer.dc.html', 'activity', 'Broșuri', '100 buc. de la 249 lei', '5–7 zile', False), ('GearQR.dc.html', 'sparkles', 'Autocolante QR', '50 buc. de la 69 lei', '3–4 zile', True),
             ('GearQR.dc.html', 'star', 'Cărți QR pentru clienți', '100 buc. de la 99 lei', '3–4 zile', True), ('GearQR.dc.html', 'route', 'Magnet auto', '2 buc. de la 149 lei', '5–7 zile', False)]
    rows = ''.join('<a href="%s" class="rw pr">%s<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">%s</span><span style="font-size: 12px; color: var(--ink2)">%s · se face la comandă, %s</span></span>%s%s</a>'
                   % (h, tile(icn, 40), t, p, d, '<span class="badge b-ok">PDF gratuit</span>' if pdf else '', CHEV) for h, icn, t, p, d, pdf in items)
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('GearHub.dc.html', '<a href="GearDesignuri.dc.html" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); display: flex; align-items: center; font-size: 14px; font-weight: 500; text-decoration: none">Designurile mele · 2</a>') + '''
  <div class="u" style="display: flex; align-items: flex-end; gap: 10px"><span style="flex-grow: 1"><h1 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -0.8px">Print Studio</h1><p style="margin: 6px 0 0; font-size: 14px; line-height: 1.4; color: var(--ink2)">Designul vine gata din profilul tău. Tu alegi șablonul și verifici macheta.</p></span><img src="assets/mascot/zee-arata.png" alt="" style="width: 84px; height: 91px; flex-shrink: 0"></div>
  <a href="GearQR.dc.html" class="card pr u d1" style="flex-direction: row; align-items: center; gap: 14px; background: var(--invbg); color: var(--invink)"><span style="background: #FFFFFF; padding: 6px; border-radius: 12px">''' + qr(64) + '''</span><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">QR-ul tău permanent</span><span style="font-size: 13px; opacity: .7">jobzee.ro/j/mihai-k7 · duce la profilul public</span></span><span style="font-size: 20px">›</span></a>
  <div class="grp u d2">''' + rows + '''</div>
  <span class="note">Telefonul, e-mailul și adresa ta nu apar pe niciun material. Fiecare comandă cere aprobarea machetei înainte de tipar.</span>
</div>
''' + gtab()
    return page('Print Studio', 'L', b, GEAR_CSS, h=1000)


def gear_carte():
    logic = """constructor(props) { super(props); this.state = { back: false, tpl: 'a', photo: true, rating: true, ok: false }; }
  renderVals() {
    const s = this.state;
    const tpl = (k, n) => ({ n, attr: s.tpl === k ? 'true' : 'false', pick: () => this.setState({ tpl: k }) });
    const T = { a: ['#FFFFFF', '#292D33', '#FF9B00'], b: ['#292D33', '#FFFFFF', '#FF9B00'], c: ['#FF9B00', '#292D33', '#FFFFFF'] }[s.tpl];
    return { tpls: [tpl('a', 'Alb'), tpl('b', 'Cărbune'), tpl('c', 'Portocaliu')], front: !s.back, back: s.back, flip: () => this.setState({ back: !s.back }),
      flipTxt: s.back ? 'Vezi fața' : 'Vezi spatele', bg: T[0], fg: T[1], ac: T[2],
      photoOn: s.photo, ratingOn: s.rating, pA: s.photo ? 'true' : 'false', rA: s.rating ? 'true' : 'false', tP: () => this.setState({ photo: !s.photo }), tR: () => this.setState({ rating: !s.rating }),
      okA: s.ok ? 'true' : 'false', tOk: () => this.setState({ ok: !s.ok }), ok: s.ok, notOk: !s.ok,
      cardStyle: 'width: 336px; height: 192px; border-radius: 14px; box-shadow: 0 18px 40px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(0,0,0,0.06); position: relative; overflow: hidden; animation: pop .5s cubic-bezier(.2,.9,.3,1.3) both; background: ' + T[0] + '; color: ' + T[1] };
  }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('PrintStudio.dc.html', '<button type="button" onClick="{{flip}}" class="pr" style="height: 36px; padding: 0 14px; border: 0; border-radius: 18px; background: var(--surf); font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink); cursor: pointer">↻ {{flipTxt}}</button>') + '''
  ''' + h1('Carte de vizită', '85 × 55 mm · completată din profil') + '''
  <div style="display: flex; justify-content: center; padding: 6px 0">
    <sc-if value="{{front}}" hint-placeholder-val="{{ true }}"><div style="{{cardStyle}}">
      <span style="position: absolute; left: 0; top: 0; bottom: 0; width: 8px; background: {{ac}}"></span>
      <div style="position: absolute; left: 26px; top: 22px; display: flex; align-items: center; gap: 12px"><sc-if value="{{photoOn}}" hint-placeholder-val="{{ true }}"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 54px; height: 54px; border-radius: 27px; object-fit: cover"></sc-if>
        <span style="display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.3px">Mihai I.</span><span style="font-size: 11px; font-weight: 500; color: {{ac}}">MONTAJ MOBILIER · REPARAȚII</span></span></div>
      <span style="position: absolute; left: 26px; top: 96px; font-size: 13px; line-height: 1.35; max-width: 190px">Montez corect, din prima. Floreasca și împrejurimi.</span>
      <sc-if value="{{ratingOn}}" hint-placeholder-val="{{ true }}"><span style="position: absolute; left: 26px; bottom: 18px; font-size: 11px; opacity: .75">4,9 ★ în Jobzee la 17 oct. 2026 · Gold</span></sc-if>
      <span style="position: absolute; right: 18px; bottom: 18px; background: #FFFFFF; padding: 5px; border-radius: 8px">''' + qr(70) + '''</span>
      <img src="assets/brand/jobzee-mark.png" alt="" style="position: absolute; right: 22px; top: 20px; height: 26px; width: auto"></div></sc-if>
    <sc-if value="{{back}}" hint-placeholder-val="{{ false }}"><div style="{{cardStyle}}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px">
      <img src="assets/brand/jobzee-logo.png" alt="jobzee" style="height: 30px; width: auto">
      <span style="font-size: 12px; text-align: center; max-width: 230px; line-height: 1.4">Scanează codul de pe față și cere-mi o ofertă în aplicația Jobzee.</span>
      <span style="font-size: 11px; font-weight: 500; color: {{ac}}">jobzee.ro/j/mihai-k7</span></div></sc-if>
  </div>
  <span class="lbl">Șablon</span>
  <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><sc-for list="{{tpls}}" as="t" hint-placeholder-count="3"><button type="button" onClick="{{t.pick}}" aria-pressed="{{t.attr}}">{{t.n}}</button></sc-for></div>
  <div class="grp">
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Slogan</span><span style="font-size: 12px; color: var(--ink2)">„Montez corect, din prima.” · 26/60</span></span>''' + ui('edit', 20) + '''</div>
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; font-size: 15px">Poza de profil</span><button type="button" class="jsw" onClick="{{tP}}" aria-pressed="{{pA}}" aria-label="Poză"></button></div>
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Nota și nivelul</span><span style="font-size: 12px; color: var(--ink2)">Se tipăresc cu data, pentru că se schimbă</span></span><button type="button" class="jsw" onClick="{{tR}}" aria-pressed="{{rA}}" aria-label="Notă"></button></div>
  </div>
  <div style="display: flex; align-items: flex-start; gap: 10px; padding: 0 6px"><button type="button" class="jsw" onClick="{{tOk}}" aria-pressed="{{okA}}" aria-label="Am verificat macheta" style="transform: scale(.85)"></button><span style="font-size: 13px; line-height: 1.4; color: var(--ink2)">Am verificat numele, textul și QR-ul. Telefonul și adresa nu apar.</span></div>
  <div style="flex-grow: 1"></div>
  <sc-if value="{{ok}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px"><a href="#pdf" class="cta2 pr" style="flex: 1">Descarcă PDF</a><a href="GearCos.dc.html" class="cta pr" style="flex: 1.4; font-size: 15px">200 buc. · 129,00 lei</a></div></sc-if>
  <sc-if value="{{notOk}}" hint-placeholder-val="{{ true }}"><span class="cta" style="background: var(--surf3); color: var(--ink2); box-shadow: none">Aprobă macheta ca să continui</span></sc-if>
</div>'''
    return page('Carte de vizită', 'L', b, GEAR_CSS, logic, h=1000)


def gear_flyer():
    logic = """constructor(props) { super(props); this.state = { fmt: 'a6', q: 500 }; }
  renderVals() {
    const s = this.state, P = { a6: { 250: 129, 500: 189, 1000: 299 }, a5: { 250: 169, 500: 249, 1000: 389 } };
    const f = (k, n) => ({ n, attr: s.fmt === k ? 'true' : 'false', pick: () => this.setState({ fmt: k }) });
    const q = v => ({ n: v + ' buc.', attr: s.q === v ? 'true' : 'false', pick: () => this.setState({ q: v }) });
    return { fmts: [f('a6', 'A6 · 105 × 148'), f('a5', 'A5 · 148 × 210')], qs: [q(250), q(500), q(1000)], price: P[s.fmt][s.q] + ',00 lei',
      flyer: 'width: ' + (s.fmt === 'a5' ? 200 : 168) + 'px; height: ' + (s.fmt === 'a5' ? 284 : 238) + 'px; transition: all .4s cubic-bezier(.2,.9,.3,1.2); border-radius: 10px; background: #FFFFFF; color: #292D33; box-shadow: 0 16px 36px rgba(0,0,0,.16); padding: 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 6px; position: relative; overflow: hidden' };
  }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('PrintStudio.dc.html') + '''
  ''' + h1('Flyer') + '''
  <div style="display: flex; justify-content: center; align-items: flex-end; min-height: 290px">
    <div style="{{flyer}}">
      <span style="position: absolute; left: 0; right: 0; top: 0; height: 64px; background: #FF9B00"></span>
      <span style="position: relative; display: flex; align-items: center; gap: 6px"><img src="assets/brand/jobzee-mark.png" alt="" style="height: 20px; width: auto; filter: brightness(0) invert(1)"><span style="font-size: 10px; font-weight: 600; color: #FFFFFF">JOBZER ÎN CARTIERUL TĂU</span></span>
      <span style="position: relative; margin-top: 18px; font-size: 17px; font-weight: 600; line-height: 1.15">Mobila montată corect, din prima</span>
      <span style="font-size: 10px; line-height: 1.5"><b>Montaj mobilier</b> · de la 120 lei<br><b>Montaj TV și rafturi</b> · de la 90 lei<br><b>Reparații mici</b> · 80 lei/h</span>
      <span style="font-size: 9px; opacity: .7">Prețuri „de la” din profilul meu Jobzee. Oferta finală o primești în aplicație.</span>
      <span style="margin-top: auto; display: flex; align-items: center; gap: 8px">''' + qr(54) + '''<span style="font-size: 10px; font-weight: 500; line-height: 1.3">Mihai I.<br>Floreasca și împrejurimi</span></span>
    </div>
  </div>
  <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><sc-for list="{{fmts}}" as="f" hint-placeholder-count="2"><button type="button" onClick="{{f.pick}}" aria-pressed="{{f.attr}}">{{f.n}}</button></sc-for></div>
  <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><sc-for list="{{qs}}" as="q" hint-placeholder-count="3"><button type="button" onClick="{{q.pick}}" aria-pressed="{{q.attr}}">{{q.n}}</button></sc-for></div>
  <div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 18px; background: var(--bsoft)">''' + ui('info', 20) + '''<span style="font-size: 12px; line-height: 1.35">Pe flyer apar doar prețurile „de la” din profilul tău. Un serviciu fără preț în profil nu poate fi pus.</span></div>
  <div style="flex-grow: 1"></div>
  <a href="GearCos.dc.html" class="cta pr">Previzualizează și aprobă · {{price}}</a>
</div>'''
    return page('Flyer', 'L', b, GEAR_CSS, logic, h=980)


def gear_qr():
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('PrintStudio.dc.html', '<a href="#copiaza" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); display: flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500; text-decoration: none">' + ui('attach', 18) + 'Copiază linkul</a>') + '''
  ''' + h1('Ce vede cine scanează') + '''
  <div class="u d1" style="display: flex; align-items: center; gap: 14px"><span style="background: #FFFFFF; padding: 8px; border-radius: 16px; box-shadow: 0 8px 22px var(--shadow)">''' + qr(104) + '''</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 15px; font-weight: 500">jobzee.ro/j/mihai-k7</span><span style="font-size: 12px; line-height: 1.4; color: var(--ink2)">Link permanent. Nu se schimbă dacă îți schimbi numele, deci ce ai tipărit nu expiră.</span></span></div>
  <div class="u d2" style="border-radius: 34px; background: var(--surf); padding: 8px; box-shadow: 0 16px 40px var(--shadow), inset 0 0 0 6px var(--surf2)">
    <div style="border-radius: 28px; background: var(--bg); padding: 16px 14px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">
      <img src="assets/brand/jobzee-logo.png" alt="jobzee" style="height: 18px; width: auto; align-self: flex-start">
      <img src="assets/people/person-jobzer-3.webp" alt="" style="width: 72px; height: 72px; border-radius: 36px; object-fit: cover; border: 3px solid var(--brand); margin-top: 4px">
      <span style="font-size: 19px; font-weight: 600">Mihai I. <span class="badge b-mto" style="vertical-align: 3px">Gold</span></span>
      <span style="font-size: 12px; color: var(--ink2)">4,9 ★ · 86 sarcini · Floreasca</span>
      <span style="display: flex; gap: 5px; flex-wrap: wrap; justify-content: center"><span class="badge b-q">Montaj mobilier</span><span class="badge b-q">Montaj TV</span><span class="badge b-q">Reparații mici</span></span>
      <span class="cta" style="align-self: stretch; height: 46px; font-size: 15px; margin-top: 6px">Cere o ofertă de la Mihai</span>
      <span style="font-size: 10px; color: var(--ink2)">Cererea trece prin fișă, oferte și potrivire, ca orice cerere Jobzee.</span>
    </div>
  </div>
  <div class="grp u d3">
    <div class="rw"><span style="color: var(--oktext); font-weight: 600">✓</span><span style="flex-grow: 1; font-size: 14px">Apar: nume public, poză, skill-uri, notă, zonă</span></div>
    <div class="rw"><span style="color: #FF3B30; font-weight: 600">✕</span><span style="flex-grow: 1; font-size: 14px">Nu apar: telefon, e-mail, adresă, CNP sau CUI</span></div>
  </div>
</div>
''' + gtab()
    return page('Profil QR', 'L', b, GEAR_CSS, h=980)


def gear_cos():
    logic = """constructor(props) { super(props); this.state = { q1: 1, q2: 1 }; }
  renderVals() {
    const s = this.state, lei = v => v.toFixed(2).replace('.', ',') + ' lei';
    const kit = 315 * s.q1, tee = 79 * s.q2, ship = 19.99 * 2, tot = kit + tee + ship;
    return { q1: s.q1, q2: s.q2, m1: () => this.setState({ q1: Math.max(0, s.q1 - 1) }), p1: () => this.setState({ q1: s.q1 + 1 }), m2: () => this.setState({ q2: Math.max(0, s.q2 - 1) }), p2: () => this.setState({ q2: s.q2 + 1 }),
      kit: lei(kit), tee: lei(tee), ship: lei(ship), tot: lei(tot), vat: lei(tot - tot / 1.21), cta: 'Continuă la plată · ' + lei(tot) };
  }"""
    pack = lambda title, badge, cls, when, body: ('<div class="grp u"><div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 14px 4px"><span style="font-size: 13px; font-weight: 600">' + title + '</span><span class="badge ' + cls + '">' + badge + '</span></div>'
                                                  '<span style="display: block; padding: 0 14px 6px; font-size: 12px; color: var(--ink2)">' + when + '</span>' + body + '</div>')
    line = lambda icn, n, sub, price, m, p, q: ('<div class="rw" style="padding-right: 12px">' + tile(icn, 46) + '<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 500">' + n + '</span><span style="font-size: 12px; color: var(--ink2)">' + sub + '</span><span style="font-size: 14px; font-weight: 600">' + price + '</span></span>'
                                                '<span class="qty"><button type="button" onClick="{{' + m + '}}" aria-label="Mai puțin">−</button><span style="min-width: 18px; text-align: center">{{' + q + '}}</span><button type="button" onClick="{{' + p + '}}" aria-label="Mai mult">+</button></span></div>')
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearHub.dc.html') + '''
  ''' + h1('Coș') + '''
  ''' + pack('Pachet 1 · Partener unelte', 'Disponibil la partener', 'b-ok', 'Livrare 2–4 zile lucrătoare, confirmată la comandă', line('work_tools', 'Kit Montaj · Starter', '5 produse · fără ruletă (o ai deja)', '{{kit}}', 'm1', 'p1', 'q1')) + '''
  ''' + pack('Pachet 2 · Partener textil', 'Se face la comandă', 'b-mto', 'Producție 3–5 zile după aprobarea machetei + livrare', line('profile', 'Tricou Jobzee · cărbune · L', 'Nume + specializare', '{{tee}}', 'm2', 'p2', 'q2')) + '''
  <div class="grp u d1">
    <div class="rw"><span style="flex-grow: 1; font-size: 14px; color: var(--ink2)">Transport · 2 pachete</span><span style="font-size: 14px">{{ship}}</span></div>
    <div class="rw"><span style="flex-grow: 1; font-size: 14px; color: var(--ink2)">din care TVA</span><span style="font-size: 14px">{{vat}}</span></div>
    <div class="rw"><span style="flex-grow: 1; font-size: 16px; font-weight: 600">Total</span><span style="font-size: 18px; font-weight: 600">{{tot}}</span></div>
  </div>
  <span class="note">Plata pentru produse e separată de plățile din lucrări și nu se ia din încasările tale.</span>
  <a href="GearCheckout.dc.html" class="cta pr u d2">{{cta}}</a>
</div>'''
    return page('Coș', 'L', b, GEAR_CSS, logic)


def gear_checkout():
    logic = """constructor(props) { super(props); this.state = { firm: true, paying: false }; }
  renderVals() { const s = this.state; return { firm: s.firm, fA: s.firm ? 'true' : 'false', tF: () => this.setState({ firm: !s.firm }), bill: s.firm ? 'Mihai Ionescu PFA · CUI RO41234567' : 'Mihai Ionescu · persoană fizică' }; }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
  ''' + topbar('GearCos.dc.html', '<span style="display: flex; align-items: center; gap: 6px; font-size: 13px; color: var(--ink2)">' + ui('shield', 18) + 'Plată securizată</span>') + '''
  ''' + h1('Finalizează comanda') + '''
  <span class="lbl">Livrare</span>
  <div class="grp"><a href="Adresa.dc.html" class="rw pr">''' + ui('location', 24) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Str. Barbu Văcărescu 120, ap. 14</span><span style="font-size: 12px; color: var(--ink2)">Floreasca, București · Mihai I. · telefonul tău, doar pentru curier</span></span>''' + CHEV + '''</a></div>
  <span class="lbl">Facturare</span>
  <div class="grp">
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Factură pe firmă</span><span style="font-size: 12px; color: var(--ink2)">{{bill}}</span></span><button type="button" class="jsw" onClick="{{tF}}" aria-pressed="{{fA}}" aria-label="Factură pe firmă"></button></div>
  </div>
  <span class="lbl">Plată</span>
  <div class="grp"><div class="rw">''' + ui('wallet', 24) + '''<span style="flex-grow: 1; font-size: 15px">Visa •••• 4821</span><span style="font-size: 13px; color: var(--btext)">Schimbă</span></div></div>
  <div class="grp">
    <div class="rw"><span style="flex-grow: 1; font-size: 14px; color: var(--ink2)">Produse</span><span style="font-size: 14px">394,00 lei</span></div>
    <div class="rw"><span style="flex-grow: 1; font-size: 14px; color: var(--ink2)">Transport · 2 pachete</span><span style="font-size: 14px">39,98 lei</span></div>
    <div class="rw"><span style="flex-grow: 1; font-size: 16px; font-weight: 600">Total cu TVA</span><span style="font-size: 18px; font-weight: 600">433,98 lei</span></div>
  </div>
  <span class="note">Anulare gratuită până intră în producție. Produsele personalizate nu se mai anulează după aprobarea machetei. Retur 14 zile pentru nepersonalizate. <a href="#termeni">Termeni</a></span>
  <div style="flex-grow: 1"></div>
  <a href="GearConfirmare.dc.html" class="cta pr" style="background: var(--invbg); color: var(--invink); box-shadow: none">Plătește cu Apple Pay · 433,98 lei</a>
</div>'''
    return page('Checkout', 'L', b, GEAR_CSS, logic)


def gear_confirmare():
    b = '''<div style="padding: 70px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; align-items: stretch">
  <img class="pop" src="assets/mascot/zee-sarbatoare.png" alt="" style="width: 150px; height: 162px; align-self: center">
  <div class="u" style="text-align: center"><h1 style="margin: 0; font-size: 28px; font-weight: 600; letter-spacing: -0.7px">Comanda e plasată</h1><p style="margin: 6px 0 0; font-size: 15px; color: var(--ink2)">JZ-1042 · 433,98 lei · factura vine pe e-mail</p></div>
  <div class="grp u d1">
    <div class="rw">''' + tile('work_tools', 40) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Kit Montaj · Starter</span><span style="font-size: 12px; color: var(--ink2)">Așteptăm confirmarea partenerului (de obicei în 2 h)</span></span><span class="badge b-q">Trimisă</span></div>
    <div class="rw">''' + tile('profile', 40) + '''<span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Tricou Jobzee</span><span style="font-size: 12px; color: var(--ink2)">Aprobă macheta ca să intre în producție</span></span><span class="badge b-mto">De aprobat</span></div>
  </div>
  <a href="GearCarte.dc.html" class="u d2" style="display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-radius: 20px; background: var(--bsoft); color: var(--ink); text-decoration: none">''' + ui('warning', 22) + '''<span style="flex-grow: 1; font-size: 14px">Un produs așteaptă aprobarea machetei</span><span style="font-size: 14px; font-weight: 500; color: var(--btext)">Aprobă ›</span></a>
  <span class="note" style="text-align: center">Nu îți spunem „expediat” până nu confirmă partenerul cu un AWB.</span>
  <div style="flex-grow: 1"></div>
  <a href="GearUrmarire.dc.html" class="cta pr">Urmărește comanda</a>
  <a href="GearHub.dc.html" class="cta2 pr" style="background: transparent">Înapoi la Gear &amp; Growth</a>
</div>'''
    return page('Comandă plasată', 'L', b, GEAR_CSS)


def gear_urmarire():
    logic = """constructor(props) { super(props); this.state = { p: 0 }; }
  renderVals() {
    const P = [
      { n: 'Pachet 1 · Kit Montaj', st: ['Plasată · 17 oct., 11:30', 'Confirmată de partener · 17 oct., 12:10', 'Expediată · Sameday, AWB 1Z84 2210', 'Livrare estimată · 21 oct. (de la curier)'], at: 2, mto: false },
      { n: 'Pachet 2 · Tricou Jobzee', st: ['Plasată · 17 oct., 11:30', 'Machetă aprobată · 17 oct., 11:42', 'În producție · gata în 3–5 zile', 'Expediere · după producție'], at: 2, mto: true }];
    const cur = P[this.state.p];
    const steps = cur.st.map((t, i) => ({ t, dot: 'width: 14px; height: 14px; border-radius: 7px; flex-shrink: 0; margin-top: 3px; ' + (i < cur.at ? 'background: var(--ok)' : i === cur.at ? 'background: var(--brand); box-shadow: 0 0 0 5px var(--bsoft)' : 'background: var(--surf3)'),
      line: i < cur.st.length - 1 ? 'position: absolute; left: 6px; top: 20px; bottom: -6px; width: 2px; background: ' + (i < cur.at ? 'var(--ok)' : 'var(--surf3)') : 'display: none', txt: 'font-size: 14px; ' + (i > cur.at ? 'color: var(--ink2)' : i === cur.at ? 'font-weight: 600' : '') }));
    const tab = i => ({ n: 'Pachet ' + (i + 1), attr: this.state.p === i ? 'true' : 'false', pick: () => this.setState({ p: i }) });
    return { steps, tabs: [tab(0), tab(1)], name: cur.n, isShip: !cur.mto, isMto: cur.mto, zee: cur.mto ? 'assets/mascot/zee-gandeste.png' : 'assets/mascot/zee-alearga.png' };
  }"""
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('GearHub.dc.html', '<span style="font-size: 13px; color: var(--ink2)">JZ-1042</span>') + '''
  <div class="u" style="display: flex; align-items: flex-end; gap: 10px"><span style="flex-grow: 1"><h1 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -0.8px">Urmărire comandă</h1><span style="font-size: 14px; color: var(--ink2)">2 pachete, de la 2 parteneri</span></span><img src="{{zee}}" alt="" style="width: 76px; height: 82px"></div>
  <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><sc-for list="{{tabs}}" as="t" hint-placeholder-count="2"><button type="button" onClick="{{t.pick}}" aria-pressed="{{t.attr}}">{{t.n}}</button></sc-for></div>
  <div class="card u d1" style="gap: 14px"><span style="font-size: 16px; font-weight: 600">{{name}}</span>
    <sc-for list="{{steps}}" as="s" hint-placeholder-count="4"><div style="position: relative; display: flex; gap: 12px; align-items: flex-start"><span style="{{s.dot}}"></span><span style="{{s.line}}"></span><span style="{{s.txt}}">{{s.t}}</span></div></sc-for>
  </div>
  <sc-if value="{{isShip}}" hint-placeholder-val="{{ true }}"><a href="#curier" class="cta pr">Vezi la curier · AWB 1Z84 2210</a></sc-if>
  <sc-if value="{{isMto}}" hint-placeholder-val="{{ false }}"><div class="card" style="flex-direction: row; align-items: center; gap: 10px">''' + ui('clock', 24) + '''<span style="font-size: 14px">Se face acum. Te anunțăm când partenerul îl predă curierului.</span></div></sc-if>
  <div class="grp u d2">
    <a href="Problema.dc.html" class="rw pr">''' + ui('question', 22) + '''<span style="flex-grow: 1; font-size: 15px">Ceva nu e în regulă</span>''' + CHEV + '''</a>
    <a href="Chitante.dc.html" class="rw pr">''' + ui('wallet', 22) + '''<span style="flex-grow: 1; font-size: 15px">Factura comenzii</span>''' + CHEV + '''</a>
  </div>
</div>
''' + gtab()
    return page('Urmărire comandă', 'L', b, GEAR_CSS, logic)


def gear_echipament():
    logic = """constructor(props) { super(props); this.state = { pub: { masina: true, nivela: true } }; }
  renderVals() {
    const s = this.state;
    const L = [['masina', 'Mașină de înșurubat 18 V', 'Din comanda JZ-0987', 'work_tools'], ['nivela', 'Nivelă laser', 'Adăugat de tine', 'match'], ['ruleta', 'Ruletă 5 m', 'Adăugat de tine', 'route'], ['scara', 'Scară 3 trepte', 'Adăugat de tine', 'job'], ['aspirator', 'Aspirator de șantier', 'Adăugat de tine', 'cleaning'], ['detector', 'Detector cabluri', 'Din comanda JZ-0987', 'radar'], ['cutie', 'Cutie organizator', 'Adăugat de tine', 'briefcase']];
    const items = L.map(([k, n, src, ic]) => ({ n, src, icon: 'assets/ui/' + ic + '.png', attr: s.pub[k] ? 'true' : 'false', toggle: () => { const o = Object.assign({}, s.pub); o[k] = !o[k]; this.setState({ pub: o }); } }));
    const pubN = Object.keys(s.pub).filter(k => s.pub[k]).length;
    return { items, pubTxt: pubN + ' din ' + L.length + ' apar pe profilul public' };
  }"""
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('GearHub.dc.html', '<button type="button" class="pr" style="height: 36px; padding: 0 14px; border: 0; border-radius: 18px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">+ Adaugă</button>') + '''
  ''' + h1('Echipamentul meu', 'Ce ai declarat tu. Clienții îl văd doar dacă bifezi.') + '''
  <div style="display: flex; justify-content: space-between; padding: 0 6px"><span class="lbl" style="padding: 0">{{pubTxt}}</span><span style="font-size: 12px; color: var(--ink2)">Public</span></div>
  <div class="grp u d1">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="7"><div class="rw" style="padding-right: 12px; border-bottom: 0.5px solid var(--sep)"><span style="width: 40px; height: 40px; border-radius: 12px; background: var(--bsoft); display: flex; align-items: center; justify-content: center; flex-shrink: 0"><img src="{{x.icon}}" alt="" style="width: 22px; height: 22px"></span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">{{x.n}}</span><span style="font-size: 12px; color: var(--ink2)">{{x.src}}</span></span><button type="button" class="jsw" onClick="{{x.toggle}}" aria-pressed="{{x.attr}}" aria-label="Public"></button></div></sc-for>
  </div>
  <div class="u d2" style="display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-radius: 20px; background: var(--surf2)">''' + ui('info', 22) + '''<span style="font-size: 13px; line-height: 1.4">Echipamentul declarat e informativ. Nu deblochează skill-uri și nu te urcă în potrivire.</span></div>
</div>
''' + gtab()
    return page('Echipamentul meu', 'L', b, GEAR_CSS, logic, h=960)


def gear_designuri():
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('PrintStudio.dc.html', '<a href="PrintStudio.dc.html" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; font-size: 14px; font-weight: 500; text-decoration: none">+ Design nou</a>') + '''
  ''' + h1('Designurile mele') + '''
  <div class="card u d1" style="gap: 10px">
    <div style="display: flex; gap: 12px; align-items: center"><span style="width: 120px; height: 70px; border-radius: 8px; background: #FFFFFF; box-shadow: 0 4px 12px rgba(0,0,0,.12), inset 4px 0 0 #FF9B00; position: relative; flex-shrink: 0"><span style="position: absolute; left: 12px; top: 12px; font-size: 9px; font-weight: 600; color: #292D33">Mihai I.</span><span style="position: absolute; left: 12px; top: 24px; font-size: 6px; color: #FF9B00; font-weight: 600">MONTAJ MOBILIER</span><span style="position: absolute; right: 8px; bottom: 8px">''' + qr(26) + '''</span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 15px; font-weight: 500">Carte de vizită · Alb</span><span style="font-size: 12px; color: var(--ink2)">Comandată 200 buc. · 2 oct.</span><span class="badge b-mto" style="align-self: flex-start">Profil schimbat după design</span></span></div>
    <div style="display: flex; gap: 6px"><a href="GearCarte.dc.html" class="cta2 pr" style="flex: 1; height: 40px; font-size: 14px; background: var(--surf2)">Actualizează din profil</a><a href="GearCos.dc.html" class="cta pr" style="flex: 1; height: 40px; font-size: 14px; box-shadow: none">Recomandă</a></div>
  </div>
  <div class="card u d2" style="gap: 10px">
    <div style="display: flex; gap: 12px; align-items: center"><span style="width: 70px; height: 98px; border-radius: 6px; background: #FFFFFF; box-shadow: 0 4px 12px rgba(0,0,0,.12); position: relative; overflow: hidden; flex-shrink: 0; margin: 0 25px"><span style="position: absolute; left: 0; right: 0; top: 0; height: 26px; background: #FF9B00"></span><span style="position: absolute; left: 6px; top: 32px; font-size: 7px; font-weight: 600; color: #292D33; width: 58px">Mobila montată corect</span><span style="position: absolute; left: 6px; bottom: 6px">''' + qr(20) + '''</span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 15px; font-weight: 500">Flyer A6</span><span style="font-size: 12px; color: var(--ink2)">Salvat · necomandat</span><span class="badge b-ok" style="align-self: flex-start">La zi cu profilul</span></span></div>
    <div style="display: flex; gap: 6px"><a href="#pdf" class="cta2 pr" style="flex: 1; height: 40px; font-size: 14px; background: var(--surf2)">Descarcă PDF</a><a href="GearFlyer.dc.html" class="cta pr" style="flex: 1; height: 40px; font-size: 14px; box-shadow: none">Comandă</a></div>
  </div>
  <span class="note">Când îți schimbi profilul, îți spunem ce designuri nu mai sunt la zi. QR-ul rămâne același.</span>
</div>
''' + gtab()
    return page('Designurile mele', 'L', b, GEAR_CSS)


def gear_growth():
    logic = """constructor(props) { super(props); this.state = { p: 30 }; }
  renderVals() {
    const p = this.state.p;
    const D = { 7: { scan: 3, visit: 11, req: 1, src: [['Cărți de vizită', 2], ['Magnet auto', 1], ['Flyere', 0]] }, 30: { scan: 14, visit: 41, req: 3, src: [['Cărți de vizită', 9], ['Magnet auto', 4], ['Flyere', 1]] } }[p];
    const max = Math.max.apply(null, D.src.map(x => x[1])) || 1;
    const src = D.src.map(([n, v]) => ({ n, v: v ? v + ' scanări' : 'Încă nicio scanare', bar: 'height: 8px; border-radius: 4px; background: var(--brand); transition: width .5s; width: ' + Math.round(v / max * 100) + '%' }));
    const t = k => ({ attr: p === k ? 'true' : 'false', pick: () => this.setState({ p: k }), n: k + ' zile' });
    return { scan: D.scan, visit: D.visit, req: D.req, src, p7: t(7), p30: t(30) };
  }"""
    steps = [('Adaugă 3 poze în portofoliu', '+10%'), ('Scrie o descriere de 2 rânduri', '+5%'), ('Adaugă preț la Montaj TV', '+5%')]
    todo = ''.join('<a href="ProfilEdit.dc.html" class="rw pr"><span style="width: 22px; height: 22px; border-radius: 11px; box-shadow: inset 0 0 0 2px var(--ink3); flex-shrink: 0"></span><span style="flex-grow: 1; font-size: 14px">%s</span><span style="font-size: 13px; color: var(--btext)">%s</span></a>' % s for s in steps)
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('GearHub.dc.html', '<div class="sg" style="grid-template-columns: repeat(2, 76px)"><button type="button" onClick="{{p7.pick}}" aria-pressed="{{p7.attr}}">{{p7.n}}</button><button type="button" onClick="{{p30.pick}}" aria-pressed="{{p30.attr}}">{{p30.n}}</button></div>') + '''
  ''' + h1('Growth Insights', 'Doar evenimente măsurate de Jobzee. Nicio estimare.') + '''
  <div class="u d1" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">
    <div class="card" style="gap: 2px"><span style="font-size: 26px; font-weight: 600">{{scan}}</span><span style="font-size: 12px; color: var(--ink2)">scanări QR</span></div>
    <div class="card" style="gap: 2px"><span style="font-size: 26px; font-weight: 600">{{visit}}</span><span style="font-size: 12px; color: var(--ink2)">vizite pe profil</span></div>
    <div class="card" style="gap: 2px; box-shadow: inset 0 0 0 2px var(--brand)"><span style="font-size: 26px; font-weight: 600">{{req}}</span><span style="font-size: 12px; color: var(--ink2)">cereri din promovare</span></div>
  </div>
  <span class="lbl">Scanări pe material</span>
  <div class="card u d2" style="gap: 12px"><sc-for list="{{src}}" as="s" hint-placeholder-count="3"><div style="display: flex; flex-direction: column; gap: 5px"><span style="display: flex; justify-content: space-between; font-size: 14px"><span>{{s.n}}</span><span style="color: var(--ink2)">{{s.v}}</span></span><span style="height: 8px; border-radius: 4px; background: var(--surf2)"><span style="{{s.bar}}; display: block"></span></span></div></sc-for></div>
  <span class="lbl">Profil 80% complet</span>
  <div class="grp u d3">''' + todo + '''</div>
  <div class="u d4" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 22px; background: var(--bsoft)"><img src="assets/mascot/zee-arata.png" alt="" style="width: 50px; height: 54px; flex-shrink: 0"><span style="font-size: 13px; line-height: 1.4">Cărțile de vizită au adus cele mai multe scanări luna asta. Nu promitem lucrări în plus: arătăm doar ce s-a întâmplat.</span></div>
</div>
''' + gtab()
    return page('Growth Insights', 'L', b, GEAR_CSS, logic, h=980)


GEAR_PAGES = [('GearHub', gear_hub), ('GearKituri', gear_kituri), ('GearKit', gear_kit), ('GearBuilder', gear_builder), ('GearShop', gear_shop), ('GearProdus', gear_produs),
              ('GearIdentity', gear_identity), ('PrintStudio', print_studio), ('GearCarte', gear_carte), ('GearFlyer', gear_flyer), ('GearQR', gear_qr), ('GearCos', gear_cos),
              ('GearCheckout', gear_checkout), ('GearConfirmare', gear_confirmare), ('GearUrmarire', gear_urmarire), ('GearEchipament', gear_echipament), ('GearDesignuri', gear_designuri), ('GearGrowth', gear_growth)]
