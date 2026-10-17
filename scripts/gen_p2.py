

# ================================================================ P2 screens
def topbar(back_href, right=''):
    return ('<div style="display: flex; align-items: center; justify-content: space-between">'
            '<a href="' + back_href + '" aria-label="Înapoi" class="pr" style="width: 40px; height: 40px; border-radius: 20px; background: var(--surf); color: var(--ink); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px var(--shadow)">' + BACK + '</a>'
            + right + '</div>')


def h1(t, sub=''):
    return ('<div class="u"><h1 style="margin: 0 4px; font-size: 32px; line-height: 1.1; font-weight: 600; letter-spacing: -0.8px">' + t + '</h1>'
            + ('<p style="margin: 6px 4px 0; font-size: 15px; line-height: 1.4; color: var(--ink2)">' + sub + '</p>' if sub else '') + '</div>')


SEG_CSS = """
.sg{display:grid;padding:2px;border-radius:10px;background:var(--surf3)}
.sg button{border:0;height:32px;border-radius:8px;background:transparent;font-family:inherit;font-size:13px;font-weight:500;color:var(--ink);cursor:pointer;transition:all .25s}
.sg button[aria-pressed="true"]{background:var(--surf);box-shadow:0 2px 6px var(--shadow)}
.jsw{width:51px;height:31px;border-radius:16px;border:0;padding:2px;cursor:pointer;flex-shrink:0;position:relative;transition:background .25s}
.jsw::after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:14px;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,.2);transition:transform .3s cubic-bezier(.3,1.3,.4,1)}
.jsw[aria-pressed="true"]{background:var(--ok)}.jsw[aria-pressed="true"]::after{transform:translateX(20px)}.jsw[aria-pressed="false"]{background:var(--surf3)}
.lbl{font-size:13px;font-weight:500;color:var(--ink2);padding:0 12px;text-transform:uppercase;letter-spacing:.3px}
.grp{background:var(--surf);border-radius:24px;overflow:hidden}
.rw{display:flex;align-items:center;gap:12px;padding:11px 16px 11px 0;margin-left:16px;color:var(--ink);text-decoration:none}
.rw+.rw{border-top:0.5px solid var(--sep)}
.dchip{border:0;width:40px;height:40px;border-radius:20px;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;transition:all .25s}
.dchip[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}.dchip[aria-pressed="false"]{background:var(--surf);color:var(--ink)}
"""


# ---------------------------------------------------------------- Notificări (client)
def notificari():
    data = [
        dict(g='Azi', k='cereri', img='people/person-jobzer-3', t='Mihai I. ți-a trimis o ofertă', s='Montaj birou · 150 lei · ajunge în 6 min', time='acum', href='Oferte.dc.html', cta='Vezi oferta', unread=True),
        dict(g='Azi', k='cereri', img='people/person-jobzer-1', t='Încă 2 oferte pentru montaj', s='Radu C. 170 lei · Elena P. 135 lei', time='2 min', href='Radar.dc.html', cta='Deschide radarul', unread=True),
        dict(g='Azi', k='plati', img='', ic='plati', t='Plată blocată: 172,50 lei', s='Se încasează doar după ce confirmi lucrarea', time='18:44', href='Activitate.dc.html', cta='', unread=False),
        dict(g='Ieri', k='cereri', img='people/person-client-1', t='Elena P. a terminat curățenia', s='Las-o o notă. Ajută ceilalți clienți.', time='ieri', href='Recenzie.dc.html', cta='Evaluează', unread=False),
        dict(g='Ieri', k='plati', img='', ic='verificat', t='Chitanța pentru curățenie e gata', s='138,00 lei · PDF', time='ieri', href='Chitante.dc.html', cta='Vezi chitanța', unread=False),
        dict(g='Săptămâna asta', k='noutati', img='', ic='rapid', t='Nou: cereri recurente', s='Curățenie în fiecare săptămână, cu același Jobzer', time='luni', href='Recurente.dc.html', cta='Încearcă', unread=False),
    ]
    logic = ("""constructor(props) { super(props); this.state = { f: 'all', read: false }; }
  renderVals() {
    const all = """ + json.dumps(data, ensure_ascii=False) + """;
    const f = this.state.f, read = this.state.read;
    const list = all.filter(n => f === 'all' || n.k === f);
    const groups = [];
    list.forEach(n => { let g = groups.find(x => x.name === n.g); if (!g) { g = { name: n.g, items: [] }; groups.push(g); }
      g.items.push({ t: n.t, s: n.s, time: n.time, href: n.href, cta: n.cta, hasCta: !!n.cta,
        picStyle: n.img ? 'background: url(assets/' + n.img + '.webp) center/cover' : 'background: var(--bsoft)',
        icStyle: n.img ? 'display: none' : 'width: 22px; height: 22px; background: var(--btext); -webkit-mask: url(assets/icons/icon-' + n.ic + '.svg) center/contain no-repeat; mask: url(assets/icons/icon-' + n.ic + '.svg) center/contain no-repeat',
        dot: n.unread && !read ? 'width: 9px; height: 9px; border-radius: 5px; background: var(--brand); flex-shrink: 0' : 'display: none' }); });
    const unread = read ? 0 : all.filter(n => n.unread).length;
    const s = k => ({ attr: f === k ? 'true' : 'false', pick: () => this.setState({ f: k }) });
    return { groups, unread, hasUnread: unread > 0, markAll: () => this.setState({ read: true }), fA: s('all'), fC: s('cereri'), fP: s('plati'), fN: s('noutati') };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Acasa.dc.html', '<sc-if value="{{hasUnread}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{markAll}}" class="pr" style="border: 0; height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); font-family: inherit; font-size: 14px; font-weight: 500; color: var(--btext); cursor: pointer">Citește tot ({{unread}})</button></sc-if>') + '''
  ''' + h1('Notificări') + '''
  <div class="sg u d1" style="grid-template-columns: repeat(4, minmax(0, 1fr))">
    <button type="button" onClick="{{fA.pick}}" aria-pressed="{{fA.attr}}">Toate</button><button type="button" onClick="{{fC.pick}}" aria-pressed="{{fC.attr}}">Cereri</button><button type="button" onClick="{{fP.pick}}" aria-pressed="{{fP.attr}}">Plăți</button><button type="button" onClick="{{fN.pick}}" aria-pressed="{{fN.attr}}">Noutăți</button>
  </div>
  <sc-for list="{{groups}}" as="g" hint-placeholder-count="3">
    <div class="u d2" style="display: flex; flex-direction: column; gap: 6px">
      <span class="lbl">{{g.name}}</span>
      <div class="grp">
        <sc-for list="{{g.items}}" as="n" hint-placeholder-count="2">
          <a href="{{n.href}}" class="rw pr" style="align-items: flex-start">
            <span style="{{n.picStyle}}; width: 42px; height: 42px; border-radius: 21px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="{{n.icStyle}}"></span></span>
            <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 15px; font-weight: 500">{{n.t}}</span><span style="font-size: 12px; color: var(--ink2); white-space: nowrap">{{n.time}}</span></span>
              <span style="font-size: 13px; color: var(--ink2)">{{n.s}}</span>
              <sc-if value="{{n.hasCta}}" hint-placeholder-val="{{ true }}"><span style="align-self: flex-start; margin-top: 4px; height: 28px; padding: 0 12px; border-radius: 14px; background: var(--bsoft); color: var(--btext); font-size: 13px; font-weight: 500; display: flex; align-items: center">{{n.cta}}</span></sc-if></span>
            <span style="{{n.dot}}; margin-top: 6px"></span>
          </a>
        </sc-for>
      </div>
    </div>
  </sc-for>
</div>
''' + tabbar('client', 'acasa', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'})
    return page('Notificări', 'L', b, SEG_CSS, logic)


# ---------------------------------------------------------------- Chitanțe și facturi (client)
def chitante():
    data = [
        dict(id='m', m='Octombrie 2026', svc='Montaj birou + dulap', who='Mihai I. · PFA', img='people/person-jobzer-3', d='17 oct.', work='150,00', fee='22,50', tot='172,50', st='Blocată pe card', stOk=False, doc='Factură de la Mihai I. (PFA)'),
        dict(id='e', m='Octombrie 2026', svc='Curățenie 2 h', who='Elena P. · persoană fizică', img='people/person-client-1', d='9 oct.', work='120,00', fee='18,00', tot='138,00', st='Plătită', stOk=True, doc='Document de plată emis de Jobzee pentru Elena P.'),
        dict(id='r', m='Octombrie 2026', svc='Cărat și mutat', who='Radu C. · SRL', img='people/person-jobzer-1', d='2 oct.', work='80,00', fee='12,00', tot='92,00', st='Plătită', stOk=True, doc='Factură de la Radu C. (SRL)'),
    ]
    logic = ("""constructor(props) { super(props); this.state = { sel: 'e', sent: false }; }
  renderVals() {
    const all = """ + json.dumps(data, ensure_ascii=False) + """;
    const sel = this.state.sel;
    const rows = all.map(r => Object.assign({}, r, { img: 'assets/' + r.img + '.webp', open: r.id === sel, closed: r.id !== sel,
      pick: () => this.setState({ sel: r.id === sel ? '' : r.id, sent: false }),
      stStyle: 'height: 24px; padding: 0 9px; border-radius: 12px; font-size: 11px; font-weight: 500; display: inline-flex; align-items: center; ' + (r.stOk ? 'background: var(--oksoft); color: var(--oktext)' : 'background: var(--bsoft); color: var(--btext)') }));
    return { rows, send: () => this.setState({ sent: true }), sent: this.state.sent, notSent: !this.state.sent };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Activitate.dc.html', '<span style="font-size: 13px; color: var(--ink2)">Total octombrie · 402,50 lei</span>') + '''
  ''' + h1('Chitanțe și facturi', 'Pentru fiecare lucrare: documentul Jobzerului și factura Jobzee pentru taxa de 15%.') + '''
  <span class="lbl u d1">Octombrie 2026</span>
  <div class="grp u d1">
    <sc-for list="{{rows}}" as="r" hint-placeholder-count="3">
      <div style="border-top: 0.5px solid var(--sep); margin-top: -0.5px">
        <button type="button" onClick="{{r.pick}}" class="pr" style="width: 100%; border: 0; background: transparent; font-family: inherit; color: var(--ink); display: flex; align-items: center; gap: 12px; padding: 12px 16px; cursor: pointer; text-align: left">
          <img src="{{r.img}}" alt="" style="width: 40px; height: 40px; border-radius: 20px; object-fit: cover; flex-shrink: 0">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">{{r.svc}}</span><span style="font-size: 12px; color: var(--ink2)">{{r.d}} · {{r.who}}</span></span>
          <span style="display: flex; flex-direction: column; align-items: flex-end; gap: 3px"><span style="font-size: 15px; font-weight: 500; font-variant-numeric: tabular-nums">{{r.tot}} lei</span><span style="{{r.stStyle}}">{{r.st}}</span></span>
        </button>
        <sc-if value="{{r.open}}" hint-placeholder-val="{{ false }}">
          <div class="u" style="margin: 0 12px 12px; padding: 12px 14px; border-radius: 18px; background: var(--surf2); display: flex; flex-direction: column; gap: 8px">
            <span style="display: flex; justify-content: space-between; font-size: 14px"><span style="color: var(--ink2)">Lucrare (integral la Jobzer)</span><span>{{r.work}} lei</span></span>
            <span style="display: flex; justify-content: space-between; font-size: 14px"><span style="color: var(--ink2)">Taxă Jobzee 15%</span><span>{{r.fee}} lei</span></span>
            <span style="display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; border-top: 0.5px solid var(--sep); padding-top: 8px"><span>Total · Visa •••• 4821</span><span>{{r.tot}} lei</span></span>
            <a href="#pdf1" class="pr" style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 14px; background: var(--surf); color: var(--ink); text-decoration: none; font-size: 14px">''' + ic('acte', 18, 'var(--btext)') + '''<span style="flex-grow: 1">{{r.doc}}</span><span style="color: var(--btext); font-weight: 500">PDF</span></a>
            <a href="#pdf2" class="pr" style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 14px; background: var(--surf); color: var(--ink); text-decoration: none; font-size: 14px">''' + ic('acte', 18, 'var(--btext)') + '''<span style="flex-grow: 1">Factură Jobzee · taxă {{r.fee}} lei</span><span style="color: var(--btext); font-weight: 500">PDF</span></a>
          </div>
        </sc-if>
      </div>
    </sc-for>
  </div>
  <div class="grp u d2">
    <a href="#firma" class="rw pr"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Facturare pe firmă</span><span style="font-size: 12px; color: var(--ink2)">CUI-ul tău apare pe facturile viitoare</span></span>''' + CHEV + '''</a>
  </div>
  <sc-if value="{{notSent}}" hint-placeholder-val="{{ true }}">
    <button type="button" onClick="{{send}}" class="pr" style="border: 0; height: 54px; border-radius: 27px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 16px; font-weight: 500; cursor: pointer">Trimite toate pe e-mail · octombrie</button>
  </sc-if>
  <sc-if value="{{sent}}" hint-placeholder-val="{{ false }}">
    <div class="pop" style="height: 54px; border-radius: 27px; background: var(--oksoft); color: var(--oktext); font-size: 16px; font-weight: 500; display: flex; align-items: center; justify-content: center">✓ Trimise la andrei@exemplu.ro</div>
  </sc-if>
</div>
''' + tabbar('client', 'activitate', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'})
    return page('Chitanțe', 'L', b, SEG_CSS, logic)


# ---------------------------------------------------------------- Cerere recurentă (client)
def recurente():
    logic = """constructor(props) { super(props); this.state = { fr: 'w', days: { 4: true }, same: true, started: false }; }
  renderVals() {
    const s = this.state, names = ['L', 'Ma', 'Mi', 'J', 'V', 'S', 'D'];
    const days = names.map((n, i) => ({ n, attr: s.days[i] ? 'true' : 'false', pick: () => { const d = Object.assign({}, s.days); d[i] = !d[i]; this.setState({ days: d }); } }));
    const fr = k => ({ attr: s.fr === k ? 'true' : 'false', pick: () => this.setState({ fr: k }) });
    const step = s.fr === 'w' ? 7 : s.fr === '2w' ? 14 : 28;
    const chosen = Object.keys(s.days).filter(k => s.days[k]).map(Number);
    const base = new Date(2026, 9, 19);
    const lun = ['ian.', 'feb.', 'mar.', 'apr.', 'mai', 'iun.', 'iul.', 'aug.', 'sep.', 'oct.', 'nov.', 'dec.'];
    const zile = ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică'];
    const next = [];
    for (let w = 0; next.length < 4 && w < 12; w++) chosen.forEach(di => { if (next.length < 4) { const d = new Date(base.getTime() + (w * step + di) * 86400000); next.push({ t: zile[di] + ', ' + d.getDate() + ' ' + lun[d.getMonth()] + ' · 10:00', first: next.length === 0 }); } });
    return {
      days, fW: fr('w'), f2: fr('2w'), fM: fr('m'), next, hasNext: next.length > 0, none: next.length === 0,
      sameAttr: s.same ? 'true' : 'false', toggleSame: () => this.setState({ same: !s.same }),
      sameTxt: s.same ? 'Elena P., dacă e liberă. Altfel primești oferte noi.' : 'Primești oferte noi la fiecare vizită',
      start: () => this.setState({ started: true }), started: s.started, notStarted: !s.started,
      cta: next.length ? 'Pornește seria · prima pe ' + next[0].t.split(' · ')[0].toLowerCase() : 'Alege cel puțin o zi'
    };
  }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Activitate.dc.html') + '''
  ''' + h1('Cerere recurentă', 'Aceeași lucrare, repetată. Plătești după fiecare vizită și poți opri oricând.') + '''
  <div class="u d1" style="display: flex; align-items: center; gap: 12px; padding: 10px 14px 10px 10px; border-radius: 24px; background: var(--surf)">
    <img src="assets/services/service-curatenie.webp" alt="" style="width: 52px; height: 52px; border-radius: 26px; object-fit: cover">
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 500">Curățenie apartament · 2 h</span><span style="font-size: 13px; color: var(--ink2)">Ultima dată cu Elena P. · ★ 5 · 120 lei</span></span>
  </div>
  <span class="lbl">Cât de des</span>
  <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><button type="button" onClick="{{fW.pick}}" aria-pressed="{{fW.attr}}">Săptămânal</button><button type="button" onClick="{{f2.pick}}" aria-pressed="{{f2.attr}}">La 2 săptămâni</button><button type="button" onClick="{{fM.pick}}" aria-pressed="{{fM.attr}}">Lunar</button></div>
  <span class="lbl">În ce zile · ora 10:00</span>
  <div style="display: flex; justify-content: space-between"><sc-for list="{{days}}" as="d" hint-placeholder-count="7"><button type="button" class="dchip" onClick="{{d.pick}}" aria-pressed="{{d.attr}}">{{d.n}}</button></sc-for></div>
  <div class="grp"><div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Același Jobzer</span><span style="font-size: 12px; color: var(--ink2)">{{sameTxt}}</span></span><button type="button" class="jsw" onClick="{{toggleSame}}" aria-pressed="{{sameAttr}}" aria-label="Același Jobzer"></button></div></div>
  <span class="lbl">Următoarele vizite</span>
  <div class="grp">
    <sc-for list="{{next}}" as="n" hint-placeholder-count="4"><div class="rw" style="font-size: 15px">''' + ic('calendar', 18, 'var(--btext)') + '''<span style="flex-grow: 1">{{n.t}}</span></div></sc-for>
    <sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><div class="rw" style="font-size: 14px; color: var(--ink2)">Alege o zi ca să vezi programul</div></sc-if>
  </div>
  <div style="flex-grow: 1"></div>
  <sc-if value="{{notStarted}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{start}}" class="pr" style="border: 0; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 17px; font-weight: 500; cursor: pointer">{{cta}}</button></sc-if>
  <sc-if value="{{started}}" hint-placeholder-val="{{ false }}"><div class="pop" style="display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 28px; background: var(--oksoft)"><img src="assets/mascot/zee-sarbatoare.svg" alt="" style="width: 44px; height: 48px"><span style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 500; color: var(--oktext)">Seria a pornit</span><span style="font-size: 13px; color: var(--ink2)">Îți amintim cu o zi înainte de fiecare vizită.</span></span></div></sc-if>
</div>'''
    return page('Cerere recurentă', 'L', b, SEG_CSS, logic)


# ---------------------------------------------------------------- Start Jobzer (onboarding scurt)
def start_jobzer():
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
  ''' + topbar('Rol.dc.html', '<span style="font-size: 13px; color: var(--ink2)">Pas 1 din 3 obligatoriu</span>') + '''
  <div class="u" style="display: flex; align-items: flex-end; gap: 12px">
    <span style="flex-grow: 1"><h1 style="margin: 0 4px; font-size: 32px; line-height: 1.1; font-weight: 600; letter-spacing: -0.8px">Începi să câștigi azi</h1>
    <p style="margin: 6px 4px 0; font-size: 15px; line-height: 1.4; color: var(--ink2)">Vezi cererile din zonă chiar acum. Ca să trimiți oferte, ai nevoie doar de identitate verificată.</p></span>
    <img class="float" src="assets/mascot/zee-bani.svg" alt="" style="width: 84px; height: 91px; flex-shrink: 0">
  </div>
  <a href="Castig.dc.html" class="u d1 pr" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 24px; background: var(--invbg); color: var(--invink); text-decoration: none">
    <span class="glow" style="width: 10px; height: 10px; border-radius: 5px; background: var(--brand); flex-shrink: 0"></span>
    <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 500">34 de cereri azi în zona ta</span><span style="font-size: 13px; opacity: .7">Montaj, curățenie, cărat · uită-te fără obligații</span></span>
    <span style="font-size: 20px">›</span>
  </a>
  <span class="lbl">Ce ai nevoie și când</span>
  <div class="grp u d2">
    <a href="Identitate.dc.html" class="rw pr"><span style="width: 30px; height: 30px; border-radius: 15px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; flex-shrink: 0">1</span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 500">Verifică identitatea · 2 min</span><span style="font-size: 12px; color: var(--ink2)">Necesar ca să trimiți oferte</span></span>''' + CHEV + '''</a>
    <a href="Skilluri.dc.html" class="rw pr"><span style="width: 30px; height: 30px; border-radius: 15px; background: var(--surf3); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; flex-shrink: 0">2</span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Alege ce știi să faci · 1 min</span><span style="font-size: 12px; color: var(--ink2)">Primești doar cereri potrivite</span></span>''' + CHEV + '''</a>
    <a href="DevinoJobzer.dc.html" class="rw pr"><span style="width: 30px; height: 30px; border-radius: 15px; background: var(--surf3); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; flex-shrink: 0">3</span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Forma legală și IBAN</span><span style="font-size: 12px; color: var(--ink2)">Abia la prima încasare</span></span>''' + CHEV + '''</a>
  </div>
  <div class="grp u d3">
    <div class="rw"><span style="color: var(--oktext); font-weight: 600">✓</span><span style="flex-grow: 1; font-size: 14px">Păstrezi 100% din prețul tău</span></div>
    <div class="rw"><span style="color: var(--oktext); font-weight: 600">✓</span><span style="flex-grow: 1; font-size: 14px">Tu alegi ce cereri accepți și când lucrezi</span></div>
    <div class="rw"><span style="color: var(--oktext); font-weight: 600">✓</span><span style="flex-grow: 1; font-size: 14px">Banii clientului sunt blocați înainte să pleci</span></div>
  </div>
  <div style="flex-grow: 1"></div>
  <a href="Identitate.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">Verifică identitatea</a>
  <a href="Castig.dc.html" style="align-self: center; font-size: 15px; font-weight: 500; text-decoration: none">Mai târziu, vreau să văd cererile</a>
</div>'''
    return page('Start Jobzer', 'L', b, SEG_CSS)


# ---------------------------------------------------------------- Ofertă în 2 atingeri (din notificare)
def oferta_rapida():
    css = SEG_CSS + """
.pc{border:0;height:52px;border-radius:26px;font-family:inherit;font-size:17px;font-weight:500;cursor:pointer;transition:all .25s cubic-bezier(.2,.9,.3,1.3)}
.pc[aria-pressed="true"]{background:var(--brand);color:#1C1C1E;transform:scale(1.04)}
.pc[aria-pressed="false"]{background:rgba(255,255,255,0.16);color:#FFFFFF}
"""
    logic = """constructor(props) { super(props); this.state = { p: 150, sent: false }; }
  renderVals() {
    const s = this.state;
    const prices = [130, 150, 170].map(v => ({ v: v + ' lei', attr: s.p === v ? 'true' : 'false', pick: () => this.setState({ p: v }) }));
    return { prices, cta: 'Trimite ' + s.p + ' lei', send: () => this.setState({ sent: true }), sent: s.sent, notSent: !s.sent, price: s.p + ' lei', undo: () => this.setState({ sent: false }) };
  }"""
    b = '''<div style="position: absolute; inset: 0; background: radial-gradient(120% 80% at 20% 10%, #FF9F0A 0%, #B35600 35%, #2B1A0A 70%, #0B0B0D 100%)"></div>
<div class="th" style="position: absolute; inset: 0; color: #FFFFFF; padding: 70px 12px 0; display: flex; flex-direction: column; align-items: center; gap: 2px">
  <span style="font-size: 17px; font-weight: 500; opacity: .85">Vineri, 17 octombrie</span>
  <span style="font-size: 86px; font-weight: 600; letter-spacing: -2px; line-height: 1">18:42</span>
  <div class="sheet" style="align-self: stretch; margin-top: 26px; border-radius: 30px; background: rgba(40,40,44,0.62); backdrop-filter: blur(30px) saturate(1.6); -webkit-backdrop-filter: blur(30px) saturate(1.6); padding: 14px; display: flex; flex-direction: column; gap: 12px">
    <div style="display: flex; align-items: center; gap: 8px"><span style="width: 24px; height: 24px; border-radius: 7px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">''' + mark(18) + '''</span><span style="font-size: 13px; font-weight: 500; opacity: .8; flex-grow: 1">JOBZEE</span><span style="font-size: 13px; opacity: .6">acum</span></div>
    <div style="display: flex; gap: 12px; align-items: center">
      <img src="assets/services/service-mobila.webp" alt="" style="width: 56px; height: 56px; border-radius: 16px; object-fit: cover; flex-shrink: 0">
      <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 500">Cerere nouă · montaj birou + dulap</span><span style="font-size: 14px; opacity: .75">2,1 km · urgent · 98% potrivire · estimare 120–220 lei</span></span>
    </div>
    <sc-if value="{{notSent}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; flex-direction: column; gap: 10px">
        <span style="font-size: 13px; opacity: .75">Alege prețul tău (primești 100%)</span>
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px"><sc-for list="{{prices}}" as="x" hint-placeholder-count="3"><button type="button" class="pc" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.v}}</button></sc-for></div>
        <button type="button" onClick="{{send}}" class="pr" style="border: 0; height: 52px; border-radius: 26px; background: #FFFFFF; color: #1C1C1E; font-family: inherit; font-size: 17px; font-weight: 500; cursor: pointer">{{cta}}</button>
        <a href="Oferta.dc.html" style="align-self: center; color: #FFFFFF; opacity: .8; font-size: 14px; text-decoration: none">Altă sumă sau un mesaj › </a>
      </div>
    </sc-if>
    <sc-if value="{{sent}}" hint-placeholder-val="{{ false }}">
      <div class="pop" style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 20px; background: rgba(48,209,88,0.18)">
        <img src="assets/mascot/zee-fericit.svg" alt="" style="width: 40px; height: 43px">
        <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 500">Ofertă trimisă · {{price}}</span><span style="font-size: 13px; opacity: .75">Te anunțăm imediat dacă te alege clientul.</span></span>
        <button type="button" onClick="{{undo}}" style="border: 0; background: transparent; color: #FFB340; font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Anulează</button>
      </div>
    </sc-if>
  </div>
  <span style="margin-top: 14px; font-size: 12px; opacity: .55; text-align: center">Prețurile sugerate vin din estimarea Jobzee pentru zona ta</span>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 10px; display: flex; justify-content: center"><span style="width: 134px; height: 5px; border-radius: 3px; background: #FFFFFF; opacity: .8"></span></div>'''
    return page('Ofertă rapidă', 'D', b, css, logic)


# ---------------------------------------------------------------- Program și zonă (Jobzer)
def disponibilitate():
    logic = """constructor(props) { super(props); this.state = { km: 5, urg: true, d: { 0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 2 } }; }
  renderVals() {
    const s = this.state, names = ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică'];
    const opts = ['Liber', 'După 17:00', 'Toată ziua'];
    const days = names.map((n, i) => { const v = s.d[i] || 0; return { n, v: opts[v], on: v > 0,
      style: 'border: 0; height: 32px; padding: 0 12px; border-radius: 16px; font-family: inherit; font-size: 13px; font-weight: 500; cursor: pointer; transition: all .25s; ' + (v === 2 ? 'background: var(--brand); color: var(--onbrand);' : v === 1 ? 'background: var(--bsoft); color: var(--btext);' : 'background: var(--surf2); color: var(--ink2);'),
      cycle: () => { const d = Object.assign({}, s.d); d[i] = ((d[i] || 0) + 1) % 3; this.setState({ d }); } }; });
    const r = 24 + s.km * 9;
    return { days, km: s.km + ' km', minus: () => this.setState({ km: Math.max(1, s.km - 1) }), plus: () => this.setState({ km: Math.min(15, s.km + 1) }),
      circle: 'position: absolute; left: 50%; top: 50%; width: ' + (2 * r) + 'px; height: ' + (2 * r) + 'px; margin: -' + r + 'px 0 0 -' + r + 'px; border-radius: 50%; background: rgba(255,159,10,0.18); border: 2px solid #FF9F0A; transition: all .4s cubic-bezier(.2,.9,.3,1.2)',
      est: 'cca ' + Math.round(s.km * s.km * 1.4) + ' cereri pe săptămână în zonă',
      urgAttr: s.urg ? 'true' : 'false', toggleUrg: () => this.setState({ urg: !s.urg }) };
  }"""
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('ContJobzer.dc.html', '<a href="Castig.dc.html" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); display: flex; align-items: center; font-size: 14px; font-weight: 500; text-decoration: none">Pauză până mâine</a>') + '''
  ''' + h1('Program și zonă', 'Primești cereri doar când ești disponibil și doar unde vrei.') + '''
  <div class="u d1" style="position: relative; height: 200px; border-radius: 28px; overflow: hidden; background: var(--land)">
    ''' + map_svg(200) + '''
    <span style="{{circle}}"></span>
    <span style="position: absolute; left: 50%; top: 50%; width: 28px; height: 28px; margin: -14px 0 0 -14px; border-radius: 14px; overflow: hidden; border: 3px solid #FFFFFF; box-shadow: 0 4px 10px rgba(0,0,0,.2)"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 100%; height: 100%; object-fit: cover"></span>
    <div class="glass" style="position: absolute; left: 10px; right: 10px; bottom: 10px; display: flex; align-items: center; gap: 10px; padding: 6px 6px 6px 14px; border-radius: 22px">
      <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 500">Raza de lucru · {{km}}</span><span style="font-size: 12px; color: var(--ink2)">{{est}}</span></span>
      <span style="display: flex; align-items: center; height: 36px; border-radius: 18px; background: var(--surf2); padding: 0 2px"><button type="button" onClick="{{minus}}" aria-label="Micșorează raza" class="pr" style="width: 40px; height: 32px; border: 0; background: transparent; font-size: 20px; color: var(--ink); cursor: pointer">−</button><span style="width: 1px; height: 18px; background: var(--sep)"></span><button type="button" onClick="{{plus}}" aria-label="Mărește raza" class="pr" style="width: 40px; height: 32px; border: 0; background: transparent; font-size: 20px; color: var(--ink); cursor: pointer">+</button></span>
    </div>
  </div>
  <span class="lbl">Săptămâna · atinge ca să schimbi</span>
  <div class="grp u d2">
    <sc-for list="{{days}}" as="d" hint-placeholder-count="7"><div class="rw" style="padding-top: 7px; padding-bottom: 7px; padding-right: 12px"><span style="flex-grow: 1; font-size: 15px">{{d.n}}</span><button type="button" onClick="{{d.cycle}}" style="{{d.style}}">{{d.v}}</button></div></sc-for>
  </div>
  <div class="grp u d3"><div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Primesc și cereri urgente</span><span style="font-size: 12px; color: var(--ink2)">Doar când ești online, în ~60 min</span></span><button type="button" class="jsw" onClick="{{toggleUrg}}" aria-pressed="{{urgAttr}}" aria-label="Cereri urgente"></button></div></div>
</div>
''' + tabbar('jobzer', 'cont', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})
    return page('Program și zonă', 'L', b, SEG_CSS, logic, h=980)


# ---------------------------------------------------------------- Facturi și plăți (Jobzer PFA/SRL)
def facturi():
    data = [
        dict(id='42', nr='JBZ-0042', c='Andrei P. · montaj birou', d='17 oct.', v='150,00', st='pending'),
        dict(id='41', nr='JBZ-0041', c='Ioana M. · montaj TV', d='15 oct.', v='90,00', st='ok'),
        dict(id='40', nr='JBZ-0040', c='SC Alfa SRL · rafturi', d='12 oct.', v='240,00', st='err'),
        dict(id='39', nr='JBZ-0039', c='Dan R. · dulap', d='10 oct.', v='170,00', st='ok'),
    ]
    logic = ("""constructor(props) { super(props); this.state = { fixed: false, auto: true }; }
  renderVals() {
    const s = this.state;
    const L = { ok: ['Trimisă în e-Factura ✓', 'var(--oksoft)', 'var(--oktext)'], pending: ['Se trimite…', 'var(--bsoft)', 'var(--btext)'], err: ['Respinsă: CUI greșit', 'rgba(255,59,48,0.12)', '#D70015'] };
    const rows = """ + json.dumps(data, ensure_ascii=False) + """.map(r => { const st = (r.st === 'err' && s.fixed) ? 'pending' : r.st; const l = L[st];
      return { nr: r.nr, c: r.c, d: r.d, v: r.v + ' lei', stTxt: l[0], stStyle: 'height: 24px; padding: 0 9px; border-radius: 12px; font-size: 11px; font-weight: 500; display: inline-flex; align-items: center; background: ' + l[1] + '; color: ' + l[2],
        isErr: st === 'err', fix: () => this.setState({ fixed: true }) }; });
    return { rows, autoAttr: s.auto ? 'true' : 'false', toggleAuto: () => this.setState({ auto: !s.auto }) };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('ContJobzer.dc.html', '<span style="height: 30px; padding: 0 12px; border-radius: 15px; background: var(--surf); display: flex; align-items: center; font-size: 13px; font-weight: 500">PFA · Mihai Ionescu</span>') + '''
  ''' + h1('Facturi și plăți') + '''
  <div class="u d1" style="position: relative; overflow: hidden; border-radius: 28px; background: var(--invbg); color: var(--invink); padding: 16px 18px; display: flex; flex-direction: column; gap: 4px">
    <span style="font-size: 13px; opacity: .65">Următorul virament · luni, 20 oct.</span>
    <span style="font-size: 36px; font-weight: 600; letter-spacing: -1px">412,00 lei</span>
    <span style="font-size: 13px; opacity: .65">În cont BT •••• 2210 · săptămânal, fără comision</span>
    <img src="assets/mascot/zee-bani.svg" alt="" class="float" style="position: absolute; right: 12px; bottom: 4px; width: 70px; height: 76px">
  </div>
  <div class="grp u d2"><div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Factură automată după fiecare lucrare</span><span style="font-size: 12px; color: var(--ink2)">Serie JBZ · trimisă în e-Factura (ANAF)</span></span><button type="button" class="jsw" onClick="{{toggleAuto}}" aria-pressed="{{autoAttr}}" aria-label="Facturare automată"></button></div></div>
  <span class="lbl">Facturi emise · octombrie</span>
  <div class="grp u d3">
    <sc-for list="{{rows}}" as="r" hint-placeholder-count="4">
      <div class="rw" style="align-items: flex-start; padding-right: 14px">
        ''' + ic('acte', 22, 'var(--btext)', 'margin-top: 2px') + '''
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 3px"><span style="display: flex; justify-content: space-between"><span style="font-size: 15px; font-weight: 500">{{r.nr}}</span><span style="font-size: 15px; font-variant-numeric: tabular-nums">{{r.v}}</span></span>
          <span style="font-size: 12px; color: var(--ink2)">{{r.d}} · {{r.c}}</span>
          <span style="display: flex; align-items: center; gap: 8px"><span style="{{r.stStyle}}">{{r.stTxt}}</span><sc-if value="{{r.isErr}}" hint-placeholder-val="{{ false }}"><button type="button" onClick="{{r.fix}}" style="border: 0; background: transparent; padding: 0; font-family: inherit; font-size: 13px; font-weight: 500; color: var(--btext); cursor: pointer">Corectează și retrimite</button></sc-if></span></span>
      </div>
    </sc-for>
  </div>
  <a href="#export" class="u d4 pr" style="display: flex; align-items: center; justify-content: center; height: 50px; border-radius: 25px; background: var(--surf); color: var(--ink); font-size: 15px; font-weight: 500; text-decoration: none">Export pentru contabil · octombrie (ZIP)</a>
</div>
''' + tabbar('jobzer', 'incasari', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})
    return page('Facturi și plăți', 'L', b, SEG_CSS, logic)
