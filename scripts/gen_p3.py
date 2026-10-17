

# ================================================================ P3 screens
def cerere_multipla():
    logic = """constructor(props) { super(props); this.state = { on: { a: true, b: true, c: false }, mode: 'one' }; }
  renderVals() {
    const s = this.state;
    const all = [
      { k: 'a', n: 'Montaj dulap mic', img: 'service-mobila', lo: 70, hi: 120, t: 60 },
      { k: 'b', n: 'Montaj TV pe perete', img: 'service-electrocasnice', lo: 80, hi: 140, t: 45 },
      { k: 'c', n: 'Mutat canapeaua în dormitor', img: 'service-mutat-obiecte', lo: 50, hi: 90, t: 30 }
    ];
    const items = all.map(x => ({ n: x.n, img: 'assets/services/' + x.img + '.webp', est: x.lo + '–' + x.hi + ' lei · ~' + x.t + ' min',
      attr: s.on[x.k] ? 'true' : 'false', toggle: () => { const o = Object.assign({}, s.on); o[x.k] = !o[x.k]; this.setState({ on: o }); },
      rowStyle: 'display: flex; align-items: center; gap: 12px; padding: 10px 14px 10px 10px; border-radius: 22px; transition: all .3s; ' + (s.on[x.k] ? 'background: var(--surf); box-shadow: inset 0 0 0 2px var(--brand)' : 'background: var(--surf); opacity: .55') }));
    const sel = all.filter(x => s.on[x.k]);
    const lo = sel.reduce((a, x) => a + x.lo, 0), hi = sel.reduce((a, x) => a + x.hi, 0), t = sel.reduce((a, x) => a + x.t, 0);
    const m = k => ({ attr: s.mode === k ? 'true' : 'false', pick: () => this.setState({ mode: k }) });
    return { items, mOne: m('one'), mMany: m('many'), count: sel.length,
      est: sel.length ? lo + ' – ' + hi + ' lei' : '—', dur: '~' + Math.floor(t / 60) + ' h ' + (t % 60) + ' min',
      modeTxt: s.mode === 'one' ? 'Un singur Jobzer face tot, într-o vizită. Oferte mai puține, dar o singură programare.' : 'Fiecare serviciu primește oferte separat. Poți alege specialistul potrivit pentru fiecare.',
      cta: s.mode === 'one' ? 'Trimite ca o singură cerere · ' + sel.length + ' servicii' : 'Trimite ' + sel.length + ' cereri separate' };
  }"""
    b = '''<div style="padding: 52px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Fisa.dc.html', '<span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; color: var(--ink2)"><img src="assets/mascot/zee-gandeste.svg" alt="" style="width: 26px; height: 28px">Jobzee AI a găsit {{count}} servicii</span>') + '''
  ''' + h1('O cerere, mai multe lucrări', 'Bifează ce vrei să faci în aceeași vizită.') + '''
  <div class="u d1" style="display: flex; flex-direction: column; gap: 8px">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="3">
      <button type="button" onClick="{{x.toggle}}" aria-pressed="{{x.attr}}" style="{{x.rowStyle}}; border: 0; font-family: inherit; color: var(--ink); text-align: left; cursor: pointer">
        <img src="{{x.img}}" alt="" style="width: 48px; height: 48px; border-radius: 24px; object-fit: cover; flex-shrink: 0">
        <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">{{x.n}}</span><span style="font-size: 12px; color: var(--ink2)">{{x.est}}</span></span>
        <span class="jsw" aria-pressed="{{x.attr}}" style="pointer-events: none"></span>
      </button>
    </sc-for>
    <a href="Dialog.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; gap: 8px; height: 46px; border-radius: 23px; border: 1.5px dashed var(--ink3); color: var(--ink); text-decoration: none; font-size: 15px; font-weight: 500">+ Adaugă încă un serviciu</a>
  </div>
  <span class="lbl">Cine le face</span>
  <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><button type="button" onClick="{{mOne.pick}}" aria-pressed="{{mOne.attr}}">Un singur Jobzer</button><button type="button" onClick="{{mMany.pick}}" aria-pressed="{{mMany.attr}}">Câte unul pe serviciu</button></div>
  <span style="font-size: 13px; line-height: 1.4; color: var(--ink2); padding: 0 6px">{{modeTxt}}</span>
  <div style="background: var(--surf); border-radius: 24px; padding: 14px 16px; display: flex; justify-content: space-between; align-items: center">
    <span style="display: flex; flex-direction: column"><span style="font-size: 13px; color: var(--ink2)">Estimare generală · {{dur}}</span><span style="font-size: 26px; font-weight: 600; letter-spacing: -0.6px">{{est}}</span></span>
    <span style="font-size: 12px; color: var(--ink2); text-align: right; max-width: 120px">Prețul final vine din oferte · +15% taxă</span>
  </div>
  <div style="flex-grow: 1"></div>
  <a href="Radar.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">{{cta}}</a>
</div>'''
    return page('Cerere multiplă', 'L', b, SEG_CSS, logic)


def statistici():
    W = [('L', 120), ('Ma', 0), ('Mi', 150), ('J', 90), ('V', 264), ('S', 310), ('D', 80)]
    M = [('S1', 640), ('S2', 820), ('S3', 710), ('S4', 1014)]
    logic = ("""constructor(props) { super(props); this.state = { p: 'w', sel: 4 }; }
  renderVals() {
    const s = this.state, data = s.p === 'w' ? """ + json.dumps(W) + """ : """ + json.dumps(M) + """;
    const max = Math.max.apply(null, data.map(d => d[1])) || 1;
    const sel = Math.min(s.sel, data.length - 1);
    const bars = data.map((d, i) => ({ l: d[0], v: d[1] + ' lei',
      bar: 'width: 100%; border-radius: 10px 10px 6px 6px; transition: height .5s cubic-bezier(.2,.9,.3,1.2), background .25s; height: ' + Math.max(6, Math.round(d[1] / max * 130)) + 'px; background: ' + (i === sel ? 'var(--brand)' : 'var(--bsoft2)'),
      lab: 'font-size: 11px; font-weight: 500; color: ' + (i === sel ? 'var(--ink)' : 'var(--ink2)'),
      pick: () => this.setState({ sel: i }) }));
    const tot = data.reduce((a, d) => a + d[1], 0);
    const t = k => ({ attr: s.p === k ? 'true' : 'false', pick: () => this.setState({ p: k, sel: k === 'w' ? 4 : 3 }) });
    return { bars, tot: tot + ' lei', selTxt: data[sel][0] + ' · ' + data[sel][1] + ' lei', pW: t('w'), pM: t('m'),
      win: s.p === 'w' ? '42%' : '38%', resp: s.p === 'w' ? '3 min' : '4 min', hour: s.p === 'w' ? '78 lei' : '74 lei', jobs: s.p === 'w' ? '9' : '34' };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Castig.dc.html', '<div class="sg" style="grid-template-columns: repeat(2, 90px)"><button type="button" onClick="{{pW.pick}}" aria-pressed="{{pW.attr}}">Săptămâna</button><button type="button" onClick="{{pM.pick}}" aria-pressed="{{pM.attr}}">Luna</button></div>') + '''
  <div class="u"><span style="margin: 0 4px; font-size: 15px; color: var(--ink2)">Ai câștigat</span><h1 style="margin: 2px 4px 0; font-size: 44px; font-weight: 600; letter-spacing: -1.4px">{{tot}}</h1></div>
  <div class="u d1" style="background: var(--surf); border-radius: 26px; padding: 14px 14px 12px; display: flex; flex-direction: column; gap: 10px">
    <span style="font-size: 13px; font-weight: 500; color: var(--btext)">{{selTxt}}</span>
    <div style="height: 150px; display: flex; align-items: flex-end; gap: 8px">
      <sc-for list="{{bars}}" as="b" hint-placeholder-count="7">
        <button type="button" onClick="{{b.pick}}" aria-label="{{b.v}}" style="flex: 1; height: 100%; border: 0; background: transparent; padding: 0; cursor: pointer; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 6px"><span style="{{b.bar}}"></span><span style="{{b.lab}}">{{b.l}}</span></button>
      </sc-for>
    </div>
  </div>
  <div class="u d2" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
    <div style="background: var(--surf); border-radius: 22px; padding: 14px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 24px; font-weight: 600">{{win}}</span><span style="font-size: 12px; color: var(--ink2)">oferte câștigate</span></div>
    <div style="background: var(--surf); border-radius: 22px; padding: 14px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 24px; font-weight: 600">{{hour}}</span><span style="font-size: 12px; color: var(--ink2)">câștig mediu pe oră</span></div>
    <div style="background: var(--surf); border-radius: 22px; padding: 14px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 24px; font-weight: 600">{{resp}}</span><span style="font-size: 12px; color: var(--ink2)">timp mediu de răspuns</span></div>
    <div style="background: var(--surf); border-radius: 22px; padding: 14px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 24px; font-weight: 600">{{jobs}}</span><span style="font-size: 12px; color: var(--ink2)">lucrări finalizate</span></div>
  </div>
  <div class="u d3" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 24px; background: var(--bsoft)">
    <img src="assets/mascot/zee-gandeste.svg" alt="" style="width: 46px; height: 50px; flex-shrink: 0">
    <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">Sfat: răspunde în sub 2 minute</span><span style="font-size: 13px; line-height: 1.35; color: var(--ink2)">Jobzerii care răspund repede câștigă aproape de două ori mai multe oferte. Activează oferta în 2 atingeri.</span></span>
  </div>
</div>
''' + tabbar('jobzer', 'incasari', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})
    return page('Statistici Jobzer', 'L', b, SEG_CSS, logic)


def siguranta():
    css = SEG_CSS + """
@keyframes sosring{0%{transform:scale(1);opacity:.5}100%{transform:scale(1.6);opacity:0}}
.sosr{position:absolute;inset:0;border-radius:50%;background:#FF3B30;animation:sosring 1.8s ease-out infinite}
"""
    logic = """constructor(props) { super(props); this.state = { hold: 0, share: true, called: false }; }
  componentWillUnmount() { clearInterval(this.i); }
  renderVals() {
    const s = this.state;
    const start = () => { if (s.called) return; clearInterval(this.i); this.i = setInterval(() => { const h = this.state.hold + 1; if (h >= 3) { clearInterval(this.i); this.setState({ hold: 3, called: true }); } else this.setState({ hold: h }); }, 1000); this.setState({ hold: 0 }); };
    const stop = () => { if (!this.state.called) { clearInterval(this.i); this.setState({ hold: 0 }); } };
    return {
      start, stop, called: s.called, notCalled: !s.called,
      sosTxt: s.called ? 'Sunăm la 112' : (s.hold > 0 ? 'Ține apăsat… ' + (3 - s.hold) : 'SOS'),
      ring: 'position: absolute; inset: -8px; border-radius: 50%; background: conic-gradient(#FFFFFF ' + (s.hold / 3 * 360) + 'deg, transparent 0); opacity: .9; transition: background .2s',
      shareAttr: s.share ? 'true' : 'false', toggleShare: () => this.setState({ share: !s.share }),
      shareTxt: s.share ? 'Ana (soție) vede unde ești până termini' : 'Nimeni nu îți vede traseul',
      reset: () => this.setState({ hold: 0, called: false })
    };
  }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('JobActiv.dc.html', '<span style="height: 30px; padding: 0 12px; border-radius: 15px; background: var(--surf); display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500"><span class="glow" style="width: 7px; height: 7px; border-radius: 4px; background: var(--ok)"></span>Sarcină activă · Andrei P.</span>') + '''
  ''' + h1('Siguranță', 'Dacă ceva nu e în regulă la lucrare, ai ajutor imediat.') + '''
  <div class="u d1" style="background: var(--surf); border-radius: 30px; padding: 22px 16px 18px; display: flex; flex-direction: column; align-items: center; gap: 14px">
    <sc-if value="{{notCalled}}" hint-placeholder-val="{{ true }}">
      <button type="button" onPointerDown="{{start}}" onPointerUp="{{stop}}" onPointerLeave="{{stop}}" aria-label="SOS, ține apăsat 3 secunde" style="position: relative; width: 140px; height: 140px; border-radius: 70px; border: 0; padding: 0; background: transparent; cursor: pointer">
        <span class="sosr"></span><span style="{{ring}}"></span>
        <span style="position: absolute; inset: 0; border-radius: 70px; background: #FF3B30; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: inherit; font-size: 28px; font-weight: 600; box-shadow: 0 14px 34px rgba(255,59,48,0.45)">{{sosTxt}}</span>
      </button>
      <span style="font-size: 14px; color: var(--ink2); text-align: center">Ține apăsat 3 secunde. Sunăm la 112 și trimitem locația ta exactă.</span>
    </sc-if>
    <sc-if value="{{called}}" hint-placeholder-val="{{ false }}">
      <div class="pop" style="display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center">
        <span style="width: 100px; height: 100px; border-radius: 50px; background: #FF3B30; color: #FFFFFF; display: flex; align-items: center; justify-content: center"><svg width="44" height="44" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 3.5l2.3-.4 1.6 4.3-1.9 1.4a11 11 0 0 0 6.6 6.6l1.4-1.9 4.3 1.6-.4 2.3a2 2 0 0 1-2 1.6A16 16 0 0 1 5 5.5a2 2 0 0 1 1.6-2z"></path></svg></span>
        <span style="font-size: 20px; font-weight: 600">Sunăm la 112…</span>
        <span style="font-size: 14px; color: var(--ink2)">Locația a fost trimisă. Echipa Jobzee e anunțată și te sună imediat după.</span>
        <button type="button" onClick="{{reset}}" style="border: 0; background: transparent; color: var(--btext); font-family: inherit; font-size: 15px; font-weight: 500; cursor: pointer">Am apăsat din greșeală</button>
      </div>
    </sc-if>
  </div>
  <div class="grp u d2">
    <div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Partajează traseul live</span><span style="font-size: 12px; color: var(--ink2)">{{shareTxt}}</span></span><button type="button" class="jsw" onClick="{{toggleShare}}" aria-pressed="{{shareAttr}}" aria-label="Partajează traseul"></button></div>
    <a href="#echipa" class="rw pr"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Mă simt nesigur · anunță echipa Jobzee</span><span style="font-size: 12px; color: var(--ink2)">Discret, fără ca celălalt să știe. Răspuns în 2 min.</span></span>''' + CHEV + '''</a>
    <a href="Problema.dc.html" class="rw pr"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Raportează o problemă cu lucrarea</span><span style="font-size: 12px; color: var(--ink2)">Plata rămâne blocată până se lămurește</span></span>''' + CHEV + '''</a>
  </div>
  <span style="font-size: 12px; line-height: 1.4; color: var(--ink2); padding: 0 6px">Același ecran există și pentru client, pe durata lucrării. Datele de siguranță se păstrează 30 de zile.</span>
</div>'''
    return page('Siguranță', 'L', b, css, logic)
