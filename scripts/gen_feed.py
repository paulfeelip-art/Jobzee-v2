

# ================================================================ ACASĂ JOBZER v2: cererile ca listă (și hartă), cu ofertă rapidă, filtre, live
FEED = [
    dict(id='r1', i='mobila', t='Montaj birou + dulap mic', z='Floreasca', km=2.1, cl='Andrei P.', st='4,9', when='u', wt='Urgent · cât mai repede', lo=120, hi=220, dur='~1 h 30', ph=2, tools='Cu uneltele tale', of=3, left=480, m='Montaj mobilier · Expert', x=128, y=250),
    dict(id='r5', i='it', t='Montaj TV 55" pe perete', z='Floreasca', km=0.9, cl='Mara S.', st='5,0', when='u', wt='Urgent · în următoarea oră', lo=100, hi=180, dur='~1 h', ph=1, tools='Suportul îl are clientul', of=5, left=250, m='Montaj TV și rafturi · din Montaj mobilier', x=214, y=318),
    dict(id='r2', i='reparatii', t='Agățat 3 rafturi și o oglindă', z='Dorobanți', km=3.4, cl='Ioana M.', st='5,0', when='a', wt='Azi · 18:00', lo=80, hi=140, dur='~1 h', ph=1, tools='Cu uneltele tale', of=1, left=1320, m='Reparații mici · Experimentat', x=70, y=380),
    dict(id='r3', i='tamplarie', t='Reglat ușa de la baie', z='Aviatorilor', km=1.2, cl='Radu T.', st='4,7', when='a', wt='Azi · 20:00', lo=60, hi=110, dur='~40 min', ph=0, tools='Cu uneltele tale', of=0, left=2100, m='Tâmplărie și uși · Experimentat', x=300, y=210),
    dict(id='r4', i='mobila', t='Montaj pat cu sertare IKEA', z='Herăstrău', km=4.8, cl='Elena D.', st='4,8', when='p', wt='Sâm., 18 oct. · 10:00', lo=150, hi=250, dur='~2 h', ph=3, tools='Cu uneltele tale', of=2, left=10800, m='Montaj mobilier · Expert', x=270, y=440),
    dict(id='r6', i='mobila', t='Dulap PAX de 2 m', z='Pipera', km=6.2, cl='Victor A.', st='4,6', when='p', wt='Dum., 19 oct. · 12:00', lo=250, hi=400, dur='~3 h', ph=2, tools='Cu uneltele tale', of=1, left=18000, m='Montaj mobilier · Expert', x=330, y=150),
]
FEED_NEW = dict(id='r7', i='tamplarie', t='Montaj 2 uși interioare', z='Primăverii', km=2.8, cl='Sorin V.', st='4,9', when='a', wt='Azi · 17:00', lo=200, hi=350, dur='~2 h 30', ph=2, tools='Cu uneltele tale', of=0, left=1800, m='Tâmplărie și uși · Experimentat', x=168, y=180)

FEED_CSS = SEG_CSS + """
@keyframes newIn{0%{opacity:0;transform:translateY(-14px) scale(.97)}60%{opacity:1}100%{transform:none}}
@keyframes flash{0%,100%{box-shadow:0 2px 10px var(--shadow)}30%{box-shadow:0 0 0 3px var(--brand),0 8px 24px rgba(255,159,10,.35)}}
@keyframes pin{0%{transform:translate(-50%,-100%) scale(1)}50%{transform:translate(-50%,-100%) scale(1.08)}100%{transform:translate(-50%,-100%) scale(1)}}
.rq{background:var(--surf);border-radius:24px;padding:12px 12px 10px;display:flex;flex-direction:column;gap:9px;box-shadow:0 2px 10px var(--shadow);animation:newIn .45s cubic-bezier(.2,.8,.2,1) both}
.rq.nw{animation:newIn .5s cubic-bezier(.2,.8,.2,1) both,flash 2.4s ease .3s 2}
.fl{border:0;height:34px;padding:0 13px;border-radius:17px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap;flex-shrink:0;transition:all .25s}
.fl[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}.fl[aria-pressed="false"]{background:var(--surf);color:var(--ink);box-shadow:0 1px 4px var(--shadow)}
.pc{border:0;flex:1;height:40px;border-radius:20px;font-family:inherit;font-size:15px;font-weight:600;cursor:pointer;transition:all .2s}
.pc[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}.pc[aria-pressed="false"]{background:var(--surf2);color:var(--ink)}
.ab{border:0;height:38px;border-radius:19px;font-family:inherit;font-size:14px;font-weight:500;cursor:pointer;display:flex;align-items:center;justify-content:center;text-decoration:none}
.tg{display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:11px;font-size:11px;font-weight:500;white-space:nowrap;background:var(--surf2);color:var(--ink2)}
.mpin{position:absolute;transform:translate(-50%,-100%);border:0;padding:0 9px;height:30px;border-radius:15px;font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;box-shadow:0 4px 12px rgba(0,0,0,.25)}
.mpin::after{content:"";position:absolute;left:50%;bottom:-5px;width:10px;height:10px;transform:translateX(-50%) rotate(45deg);background:inherit;border-radius:2px}
.scroll{scrollbar-width:none}.scroll::-webkit-scrollbar{display:none}
"""


def castig_v2(theme):
    dark = theme == 'D'
    S = lambda n: n.replace('.dc.html', 'Dark.dc.html') if dark else n
    logic = ("""constructor(props) {
    super(props);
    this.state = { on: true, view: 'list', f: 'all', sort: 0, items: """ + json.dumps(FEED, ensure_ascii=False) + """, hidden: {}, sent: {}, quick: '', price: {}, t: 0, gotNew: false, undo: '', mapSel: 'r1', ad: true };
  }
  componentDidMount() {
    this.tick = setInterval(() => this.setState({ t: this.state.t + 1 }), 1000);
    this.nw = setTimeout(() => { if (this.state.on) this.setState({ items: [Object.assign({ fresh: true }, """ + json.dumps(FEED_NEW, ensure_ascii=False) + """)].concat(this.state.items), gotNew: true }); }, 7000);
  }
  componentWillUnmount() { clearInterval(this.tick); clearTimeout(this.nw); clearTimeout(this.ut); }
  sugg(r) { const r10 = (v) => Math.round(v / 10) * 10; return [r10(r.lo + (r.hi - r.lo) * 0.2), r10((r.lo + r.hi) / 2), r10(r.lo + (r.hi - r.lo) * 0.8)]; }
  renderVals() {
    const s = this.state;
    const mm = (sec) => sec >= 3600 ? Math.floor(sec / 3600) + ' h ' + String(Math.floor(sec % 3600 / 60)).padStart(2, '0') + ' min' : Math.floor(sec / 60) + ':' + String(sec % 60).padStart(2, '0');
    const live = s.items.filter((r) => !s.hidden[r.id]);
    const cnt = (k) => live.filter((r) => k === 'sent' ? s.sent[r.id] : (!s.sent[r.id] && (k === 'all' || r.when === k))).length;
    const SORTS = ['Cele mai noi', 'Cele mai aproape', 'Cele mai bine plătite'];
    let list = live.filter((r) => s.f === 'sent' ? s.sent[r.id] : (!s.sent[r.id] && (s.f === 'all' || r.when === s.f)));
    if (s.sort === 1) list = list.slice().sort((a, b) => a.km - b.km);
    if (s.sort === 2) list = list.slice().sort((a, b) => b.hi - a.hi);
    const card = (r) => {
      const left = Math.max(0, r.left - s.t), sent = s.sent[r.id], q = s.quick === r.id, sg = this.sugg(r), pr = s.price[r.id] || sg[1];
      const wc = r.when === 'u' ? 'background: rgba(255,59,48,.12); color: #D70015' : r.when === 'a' ? 'background: var(--bsoft); color: var(--btext)' : 'background: var(--surf2); color: var(--ink2)';
      const eta = Math.max(8, Math.round(r.km * 6));
      return { id: r.id, t: r.t, src: 'assets/cat/' + r.i + '.svg', meta: r.z + ' · ' + String(r.km).replace('.', ',') + ' km · ' + r.cl + ' ★ ' + r.st, wt: r.wt, wst: 'height: 24px; padding: 0 9px; border-radius: 12px; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; white-space: nowrap; ' + wc,
        est: r.lo + '–' + r.hi + ' lei', dur: r.dur, ph: r.ph ? r.ph + (r.ph === 1 ? ' poză' : ' poze') : 'Fără poze', tools: r.tools, m: r.m,
        comp: r.of === 0 ? 'Fii primul care trimite ofertă' : r.of + (r.of === 1 ? ' ofertă trimisă' : ' oferte trimise'), first: r.of === 0,
        left: left > 0 ? 'Mai poți oferta ' + mm(left) : 'Timpul de ofertare s-a încheiat', leftSt: 'font-size: 12px; font-weight: 500; font-variant-numeric: tabular-nums; color: ' + (left < 120 ? '#D70015' : 'var(--ink2)'),
        open: left > 0, cls: 'rq' + (r.fresh ? ' nw' : ''), isNew: !!r.fresh,
        sent: !!sent, notSent: !sent, sentTxt: sent ? 'Ofertă trimisă · ' + sent + ' lei · ajungi în ~' + eta + ' min' : '', q: q && !sent, nq: !q && !sent,
        doQuick: () => this.setState({ quick: q ? '' : r.id }),
        chips: sg.map((v) => ({ t: v + ' lei', attr: pr === v ? 'true' : 'false', pick: () => { const p = Object.assign({}, s.price); p[r.id] = v; this.setState({ price: p }); } })),
        sendTxt: 'Trimite ' + pr + ' lei · ajung în ~' + eta + ' min',
        send: () => { const x = Object.assign({}, s.sent); x[r.id] = pr; this.setState({ sent: x, quick: '' }); },
        retract: () => { const x = Object.assign({}, s.sent); delete x[r.id]; this.setState({ sent: x }); },
        hide: () => { const h = Object.assign({}, s.hidden); h[r.id] = true; this.setState({ hidden: h, undo: r.id, quick: '' }); clearTimeout(this.ut); this.ut = setTimeout(() => this.setState({ undo: '' }), 4000); } };
    };
    const cards = list.map(card);
    const fl = (k, n) => ({ t: n + (cnt(k) ? ' · ' + cnt(k) : ''), attr: s.f === k ? 'true' : 'false', pick: () => this.setState({ f: k }) });
    const pins = live.filter((r) => !s.sent[r.id]).map((r) => ({ t: (r.when === 'u' ? '⚡ ' : '') + r.lo + '–' + r.hi,
      st: 'left: ' + r.x + 'px; top: ' + r.y + 'px; ' + (s.mapSel === r.id ? 'background: var(--brand); color: var(--onbrand); z-index: 3; animation: pin 1.6s ease-in-out infinite' : 'background: var(--surf); color: var(--ink); z-index: 2'),
      pick: () => this.setState({ mapSel: r.id, quick: '' }) }));
    const selR = live.find((r) => r.id === s.mapSel) || live[0];
    return { on: s.on, off: !s.on, toggle: () => this.setState({ on: !s.on }),
      onTxt: s.on ? 'Online · 5 km' : 'Offline', onSt: 'height: 40px; padding: 0 14px 0 10px; border: 0; border-radius: 20px; display: flex; align-items: center; gap: 8px; font-family: inherit; font-size: 15px; font-weight: 600; cursor: pointer; box-shadow: 0 4px 14px var(--shadow); transition: all .3s; ' + (s.on ? 'background: var(--surf); color: var(--ink)' : 'background: var(--invbg); color: var(--invink)'),
      dotSt: 'width: 12px; height: 12px; border-radius: 6px; ' + (s.on ? 'background: var(--ok); animation: halo 1.8s ease-out infinite' : 'background: var(--ink3)'),
      isList: s.view === 'list' && s.on, isMap: s.view === 'map' && s.on, vL: s.view === 'list' ? 'true' : 'false', vM: s.view === 'map' ? 'true' : 'false', goL: () => this.setState({ view: 'list' }), goM: () => this.setState({ view: 'map' }),
      head: cnt('all') + (cnt('all') === 1 ? ' cerere pentru tine' : ' cereri pentru tine'), newBadge: s.gotNew, sub: 'Doar pe competențele tale, în 5 km',
      fl: [fl('all', 'Toate'), fl('u', 'Urgente'), fl('a', 'Azi'), fl('p', 'Programate'), fl('sent', 'Trimise')],
      sortTxt: '↕ ' + SORTS[s.sort], sortNext: () => this.setState({ sort: (s.sort + 1) % 3 }),
      cards: cards, empty: cards.length === 0, emptyTxt: s.f === 'sent' ? 'Încă n-ai trimis nicio ofertă azi.' : 'Nicio cerere aici acum. Te anunțăm imediat ce apare una.',
      undo: !!s.undo, doUndo: () => { const h = Object.assign({}, s.hidden); delete h[s.undo]; this.setState({ hidden: h, undo: '' }); },
      pins: pins, sel: selR ? [card(selR)] : [], ad: s.ad, closeAd: () => this.setState({ ad: false }) };
  }""")
    rq = '''<div class="{{c.cls}}">
          <div style="display: flex; gap: 11px; align-items: flex-start">
            <img src="{{c.src}}" alt="" style="width: 46px; height: 46px; border-radius: 14px; flex-shrink: 0">
            <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px">
              <span style="display: flex; align-items: center; gap: 6px"><span style="{{c.wst}}">{{c.wt}}</span><sc-if value="{{c.isNew}}" hint-placeholder-val="{{ false }}"><span class="tg" style="background: var(--brand); color: var(--onbrand)">Nouă</span></sc-if></span>
              <span style="font-size: 16px; font-weight: 600; line-height: 1.25">{{c.t}}</span>
              <span style="font-size: 12px; color: var(--ink2)">{{c.meta}}</span>
            </span>
            <span style="display: flex; flex-direction: column; align-items: flex-end; flex-shrink: 0"><span style="font-size: 11px; color: var(--ink2)">estimare</span><span style="font-size: 15px; font-weight: 600; white-space: nowrap">{{c.est}}</span></span>
          </div>
          <div style="display: flex; gap: 5px; flex-wrap: wrap"><span class="tg">{{c.dur}}</span><span class="tg">{{c.ph}}</span><span class="tg">{{c.tools}}</span></div>
          <span style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--oktext)"><span style="font-weight: 600">✓</span>{{c.m}}</span>
          <div style="display: flex; align-items: center; justify-content: space-between; padding-top: 8px; box-shadow: inset 0 0.5px 0 var(--sep)">
            <sc-if value="{{c.first}}" hint-placeholder-val="{{ false }}"><span style="font-size: 12px; font-weight: 600; color: var(--btext)">{{c.comp}}</span></sc-if>
            <sc-if value="{{c.notFirst}}" hint-placeholder-val="{{ true }}"><span style="font-size: 12px; color: var(--ink2)">{{c.comp}}</span></sc-if>
            <span style="{{c.leftSt}}">{{c.left}}</span>
          </div>
          <sc-if value="{{c.nq}}" hint-placeholder-val="{{ true }}"><div style="display: flex; gap: 6px">
            <button type="button" onClick="{{c.hide}}" class="ab pr" style="width: 38px; background: var(--surf2); color: var(--ink2)" aria-label="Ascunde cererea"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button>
            <a href="''' + S('Oferta.dc.html') + '''" class="ab pr" style="flex: 1; background: var(--surf2); color: var(--ink)">Detalii</a>
            <button type="button" onClick="{{c.doQuick}}" class="ab pr" style="flex: 1.4; background: var(--brand); color: var(--onbrand)">Ofertă rapidă</button>
          </div></sc-if>
          <sc-if value="{{c.q}}" hint-placeholder-val="{{ false }}"><div class="in" style="display: flex; flex-direction: column; gap: 8px; padding: 10px; border-radius: 18px; background: var(--bsoft)">
            <span style="font-size: 12px; color: var(--ink2)">Alege prețul. Primești integral suma, taxa o plătește clientul.</span>
            <div style="display: flex; gap: 6px"><sc-for list="{{c.chips}}" as="p" hint-placeholder-count="3"><button type="button" class="pc pr" onClick="{{p.pick}}" aria-pressed="{{p.attr}}">{{p.t}}</button></sc-for></div>
            <button type="button" onClick="{{c.send}}" class="ab pr" style="height: 44px; border-radius: 22px; background: var(--invbg); color: var(--invink); font-size: 15px">{{c.sendTxt}}</button>
            <div style="display: flex; justify-content: space-between"><a href="''' + S('Oferta.dc.html') + '''" style="font-size: 13px; font-weight: 500; color: var(--btext); text-decoration: none">Alt preț sau un mesaj ›</a><button type="button" onClick="{{c.doQuick}}" style="border: 0; background: transparent; padding: 0; font-family: inherit; font-size: 13px; color: var(--ink2); cursor: pointer">Renunță</button></div>
          </div></sc-if>
          <sc-if value="{{c.sent}}" hint-placeholder-val="{{ false }}"><div style="display: flex; align-items: center; gap: 8px; padding: 9px 12px; border-radius: 16px; background: var(--oksoft)"><span style="flex-grow: 1; font-size: 13px; font-weight: 500; color: var(--oktext)">✓ {{c.sentTxt}}</span><button type="button" onClick="{{c.retract}}" style="border: 0; background: transparent; padding: 0; font-family: inherit; font-size: 13px; font-weight: 500; color: var(--ink2); cursor: pointer">Retrage</button></div></sc-if>
        </div>'''
    mapsvg = ('<svg width="390" height="560" viewBox="0 0 390 560" aria-hidden="true" style="position: absolute; left: 0; top: 0; display: block">'
              '<rect width="390" height="560" style="fill: var(--land)"></rect>'
              '<path d="M-10 470 C 80 440 170 500 270 465 S 400 450 400 450 L400 560 L-10 560 Z" style="fill: var(--water)"></path>'
              '<path d="M240 60 h90 v70 h-90z" style="fill: var(--park)"></path><path d="M30 420 h70 v40 h-70z" style="fill: var(--park)"></path>'
              '<path d="M-10 130 L400 90 M-10 330 L400 370 M120 -10 L92 600 M282 -10 L312 600" stroke-width="14" stroke-linecap="round" fill="none" style="stroke: var(--road)"></path>'
              '<path d="M-10 230 L400 245 M200 -10 L188 600" stroke-width="6" fill="none" style="stroke: var(--road)"></path>'
              '<circle cx="196" cy="280" r="90" fill="#FF9F0A" fill-opacity="0.07" stroke="#FF9F0A" stroke-opacity="0.35" stroke-dasharray="4 5"></circle>'
              '<circle cx="196" cy="280" r="9" style="fill: var(--invbg); stroke: var(--surf)" stroke-width="4"></circle></svg>')
    b = '''<div style="position: absolute; inset: 0; display: flex; flex-direction: column">
  <div style="padding: 52px 16px 10px; display: flex; flex-direction: column; gap: 10px; position: relative; z-index: 4">
    <div style="display: flex; align-items: center; justify-content: space-between">
      <a href="''' + S('ContJobzer.dc.html') + '''" aria-label="Profilul meu" class="pr" style="width: 40px; height: 40px; border-radius: 20px; overflow: hidden; display: block; box-shadow: 0 4px 14px var(--shadow)"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 40px; height: 40px; object-fit: cover"></a>
      <button type="button" onClick="{{toggle}}" style="{{onSt}}" aria-label="Schimbă disponibilitatea"><span style="{{dotSt}}"></span>{{onTxt}}</button>
      <a href="''' + S('Incasari.dc.html') + '''" class="pr" style="height: 40px; padding: 0 14px; border-radius: 20px; background: var(--invbg); color: var(--invink); display: flex; align-items: center; font-size: 16px; font-weight: 600; text-decoration: none">264 lei azi</a>
    </div>
    <sc-if value="{{on}}" hint-placeholder-val="{{ true }}">
      <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 10px">
        <span style="display: flex; flex-direction: column"><span style="display: flex; align-items: center; gap: 8px"><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.6px">{{head}}</span><sc-if value="{{newBadge}}" hint-placeholder-val="{{ false }}"><span class="tg" style="background: var(--brand); color: var(--onbrand)">+1 nouă</span></sc-if></span><span style="font-size: 12px; color: var(--ink2)">{{sub}}</span></span>
        <div class="sg" style="grid-template-columns: repeat(2, 64px); flex-shrink: 0"><button type="button" onClick="{{goL}}" aria-pressed="{{vL}}">Listă</button><button type="button" onClick="{{goM}}" aria-pressed="{{vM}}">Hartă</button></div>
      </div>
      <div class="scroll" style="display: flex; gap: 6px; overflow-x: auto; margin: 0 -16px; padding: 2px 16px 4px"><sc-for list="{{fl}}" as="f" hint-placeholder-count="5"><button type="button" class="fl pr" onClick="{{f.pick}}" aria-pressed="{{f.attr}}">{{f.t}}</button></sc-for></div>
    </sc-if>
  </div>
  <sc-if value="{{isList}}" hint-placeholder-val="{{ true }}"><div class="scroll" style="flex-grow: 1; min-height: 0; overflow-y: auto; padding: 0 12px 104px; display: flex; flex-direction: column; gap: 10px">
    <div style="display: flex; justify-content: flex-end; margin-top: -2px"><button type="button" onClick="{{sortNext}}" style="border: 0; background: transparent; padding: 0 4px; font-family: inherit; font-size: 13px; font-weight: 500; color: var(--btext); cursor: pointer">{{sortTxt}}</button></div>
    <sc-if value="{{undo}}" hint-placeholder-val="{{ false }}"><div class="in" style="display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 16px; background: var(--invbg); color: var(--invink); font-size: 14px"><span style="flex-grow: 1">Am ascuns cererea. Nu te penalizează.</span><button type="button" onClick="{{doUndo}}" style="border: 0; background: transparent; padding: 0; font-family: inherit; font-size: 14px; font-weight: 600; color: var(--brand); cursor: pointer">Anulează</button></div></sc-if>
    <sc-for list="{{cards}}" as="c" hint-placeholder-count="3">''' + rq + '''</sc-for>
    <sc-if value="{{empty}}" hint-placeholder-val="{{ false }}"><div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 30px 20px; text-align: center"><img src="assets/mascot/zee-cauta.png" alt="" style="width: 100px; height: 108px"><span style="font-size: 15px; color: var(--ink2)">{{emptyTxt}}</span></div></sc-if>
    <sc-if value="{{ad}}" hint-placeholder-val="{{ true }}"><div style="margin-top: 4px">''' + ad_card('order', S('SchimbaRol.dc.html')) + '''</div></sc-if>
  </div></sc-if>
  <sc-if value="{{isMap}}" hint-placeholder-val="{{ false }}"><div style="position: relative; flex-grow: 1; min-height: 0">
    <div style="position: absolute; left: 0; right: 0; top: -14px; height: 560px; overflow: hidden">''' + mapsvg + '''
      <sc-for list="{{pins}}" as="p" hint-placeholder-count="6"><button type="button" class="mpin" onClick="{{p.pick}}" style="{{p.st}}">{{p.t}}</button></sc-for>
    </div>
    <div style="position: absolute; left: 12px; right: 12px; bottom: 100px"><sc-for list="{{sel}}" as="c" hint-placeholder-count="1">''' + rq + '''</sc-for></div>
  </div></sc-if>
  <sc-if value="{{off}}" hint-placeholder-val="{{ false }}"><div style="flex-grow: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; padding: 0 30px 120px; text-align: center">
    <img src="assets/mascot/zee-doarme.png" alt="" style="width: 150px; height: 162px">
    <span style="font-size: 22px; font-weight: 600; letter-spacing: -0.4px">Ești offline</span>
    <span style="font-size: 15px; line-height: 1.4; color: var(--ink2)">Nu primești cereri noi. Ofertele trimise rămân valabile.</span>
    <button type="button" onClick="{{toggle}}" class="pr" style="height: 52px; padding: 0 28px; border: 0; border-radius: 26px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 17px; font-weight: 500; cursor: pointer">Pornește</button>
  </div></sc-if>
</div>
''' + tabbar('jobzer', 'acasa', {'acasa': S('Castig.dc.html'), 'sarcini': S('SarciniJobzer.dc.html'), 'incasari': S('Incasari.dc.html'), 'cont': S('ContJobzer.dc.html')})
    css = FEED_CSS + '@keyframes inUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}.in{animation:inUp .3s cubic-bezier(.2,.8,.2,1) both}'
    out = page('Acasă Jobzer · cereri', theme, b, css, logic)
    return out.replace("comp: r.of === 0 ?", "notFirst: r.of !== 0, comp: r.of === 0 ?")
