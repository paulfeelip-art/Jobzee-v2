

# ---------------------------------------------------------------- Fișa cererii (fără buget: doar estimare)
def fisa():
    css = """
.seg3{display:grid;gap:6px;padding:5px;border-radius:26px;background:var(--surf3)}
.o3{border:0;border-radius:21px;background:transparent;font-family:inherit;color:var(--ink2);cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;transition:background .3s, color .3s, transform .35s cubic-bezier(.2,.9,.3,1.4), box-shadow .3s}
.o3 b{font-size:15px;font-weight:700}.o3 small{font-size:11px;font-weight:500}
.o3[aria-pressed="true"]{background:var(--surf);color:var(--ink);box-shadow:0 4px 14px var(--shadow);transform:scale(1.02)}
.o3.urg[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}
.chip{border:0;height:36px;padding:0 14px;border-radius:18px;background:var(--surf2);font:600 14px/1 inherit;font-family:inherit;color:var(--ink);cursor:pointer;transition:all .25s}
.chip[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}
@keyframes mark{from{left:0}}
"""
    logic = """constructor(props) { super(props); this.state = { when: 'urgent', slot: '16–18', where: 'here' }; }
  renderVals() {
    const s = this.state;
    const slots = ['14–16', '16–18', '18–20'].map(t => ({ t, attr: s.slot === t ? 'true' : 'false', pick: () => this.setState({ slot: t }) }));
    return {
      wU: s.when === 'urgent' ? 'true' : 'false', wA: s.when === 'azi' ? 'true' : 'false', wP: s.when === 'prog' ? 'true' : 'false',
      setU: () => this.setState({ when: 'urgent' }), setA: () => this.setState({ when: 'azi' }), setP: () => this.setState({ when: 'prog' }),
      isU: s.when === 'urgent', isA: s.when === 'azi', isP: s.when === 'prog', slots,
      hH: s.where === 'here' ? 'true' : 'false', hO: s.where === 'other' ? 'true' : 'false',
      setH: () => this.setState({ where: 'here' }), setO: () => this.setState({ where: 'other' }),
      isH: s.where === 'here', isO: s.where === 'other',
      cta: s.when === 'urgent' ? 'Trimite acum · oferte în câteva minute' : (s.when === 'azi' ? 'Trimite · azi între ' + s.slot : 'Trimite · joi, 23 oct, 10:00')
    };
  }"""
    pin = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 22s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"></path><circle cx="12" cy="10" r="2.6" fill="var(--surf)"></circle></svg>'
    plus = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg>'
    lab = lambda t: '<span style="font-size: 13px; font-weight: 600; color: var(--ink2); padding: 0 12px; text-transform: uppercase; letter-spacing: .3px">' + t + '</span>'
    b = '''<div style="padding: 52px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
  <div style="display: flex; align-items: center; justify-content: space-between">
    <a href="Dialog.dc.html" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 600; color: var(--ink2)"><img src="assets/mascot/zee-fericit.svg" alt="" style="width: 26px; height: 28px">Creată cu Jobzee AI</span>
    <a href="Dialog.dc.html" class="pr" style="height: 40px; padding: 0 14px; border-radius: 20px; background: var(--surf); display: flex; align-items: center; font-size: 15px; font-weight: 600; text-decoration: none">Modifică</a>
  </div>
  <h1 class="u" style="margin: 0 4px; font-size: 32px; font-weight: 700; letter-spacing: -0.8px">Fișa cererii</h1>

  <div class="u d1" style="background: var(--surf); border-radius: 26px; padding: 10px 14px 10px 10px; display: flex; align-items: center; gap: 12px">
    <img src="assets/services/service-mobila.webp" alt="" style="width: 56px; height: 56px; border-radius: 28px; object-fit: cover; flex-shrink: 0">
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">Montaj birou + dulap mic</span><span style="font-size: 13px; color: var(--ink2)">Montaj mobilier · 2 poze · ~1 h 30 · unelte aduse</span></span>
  </div>

  ''' + lab('Când') + '''
  <div class="seg3 u d2" style="grid-template-columns: repeat(3, minmax(0, 1fr))">
    <button type="button" class="o3 urg" onClick="{{setU}}" aria-pressed="{{wU}}" style="height: 56px"><b>⚡ Urgent</b><small>în ~60 min</small></button>
    <button type="button" class="o3" onClick="{{setA}}" aria-pressed="{{wA}}" style="height: 56px"><b>Azi</b><small>alegi intervalul</small></button>
    <button type="button" class="o3" onClick="{{setP}}" aria-pressed="{{wP}}" style="height: 56px"><b>Programează</b><small>altă zi</small></button>
  </div>
  <div style="min-height: 44px">
    <sc-if value="{{isU}}" hint-placeholder-val="{{ true }}">
      <div class="u" style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-radius: 20px; background: var(--bsoft); font-size: 13px; line-height: 1.35"><span class="glow" style="width: 8px; height: 8px; border-radius: 4px; background: var(--brand); flex-shrink: 0"></span>Cererea ajunge întâi la Jobzerii online acum, pe o rază de 3 km.</div>
    </sc-if>
    <sc-if value="{{isA}}" hint-placeholder-val="{{ false }}">
      <div class="u" style="display: flex; gap: 8px"><sc-for list="{{slots}}" as="x" hint-placeholder-count="3"><button type="button" class="chip" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.t}}</button></sc-for></div>
    </sc-if>
    <sc-if value="{{isP}}" hint-placeholder-val="{{ false }}">
      <a href="Programare.dc.html" class="u pr" style="display: flex; align-items: center; gap: 10px; padding: 10px 14px; border-radius: 20px; background: var(--surf); color: var(--ink); text-decoration: none">''' + ic('calendar', 18, 'var(--btext)') + '''<span style="flex-grow: 1; font-size: 15px">Joi, 23 oct · 10:00 · flexibil ± 1 h</span>''' + CHEV + '''</a>
    </sc-if>
  </div>

  ''' + lab('Unde') + '''
  <div class="seg3 u d3" style="grid-template-columns: repeat(2, minmax(0, 1fr))">
    <button type="button" class="o3" onClick="{{setH}}" aria-pressed="{{hH}}" style="height: 46px; flex-direction: row; gap: 6px"><span style="color: var(--brand); display: flex">''' + pin + '''</span><b>Locația asta</b></button>
    <button type="button" class="o3" onClick="{{setO}}" aria-pressed="{{hO}}" style="height: 46px; flex-direction: row; gap: 6px">''' + plus + '''<b>Altă adresă</b></button>
  </div>
  <sc-if value="{{isH}}" hint-placeholder-val="{{ true }}">
    <div class="u" style="display: flex; align-items: center; gap: 12px; padding: 8px 14px 8px 8px; border-radius: 22px; background: var(--surf)">
      <span style="position: relative; width: 48px; height: 48px; border-radius: 24px; overflow: hidden; background: var(--land); flex-shrink: 0"><svg width="48" height="48" viewBox="0 0 48 48" aria-hidden="true" style="display: block"><path d="M-2 18 L50 12 M18 -2 L14 50" stroke-width="6" style="stroke: var(--road)"></path><rect x="26" y="26" width="16" height="14" rx="5" style="fill: var(--park)"></rect><circle cx="24" cy="24" r="6" fill="#FF9F0A" stroke="#FFFFFF" stroke-width="3"></circle></svg></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 600">Str. Barbu Văcărescu 120</span><span style="font-size: 12px; color: var(--ink2)">Floreasca · detectată acum · ap. 14, et. 3</span></span>
      <a href="Adresa.dc.html" style="font-size: 14px; font-weight: 600; text-decoration: none">Ajustează</a>
    </div>
  </sc-if>
  <sc-if value="{{isO}}" hint-placeholder-val="{{ false }}">
    <a href="Adresa.dc.html" class="u pr" style="display: flex; align-items: center; gap: 12px; padding: 14px; border-radius: 22px; background: var(--surf); color: var(--ink); text-decoration: none; box-shadow: inset 0 0 0 2px var(--brand)"><span style="width: 34px; height: 34px; border-radius: 17px; background: var(--bsoft); color: var(--btext); display: flex; align-items: center; justify-content: center">''' + plus + '''</span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 600">Definește adresa</span><span style="font-size: 12px; color: var(--ink2)">Caut-o sau pune pinul pe hartă</span></span>''' + CHEV + '''</a>
  </sc-if>

  <div class="u d4" style="background: var(--surf); border-radius: 26px; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px">
    <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 15px; font-weight: 600">Estimare generală</span><span style="font-size: 12px; color: var(--ink2)">montaj mobilier · zona ta</span></span>
    <span style="font-size: 30px; font-weight: 700; letter-spacing: -0.8px">120 – 220 <span style="font-size: 17px; color: var(--ink2)">lei</span></span>
    <span style="position: relative; height: 8px; border-radius: 4px; background: linear-gradient(90deg, #34C759, #FF9F0A 60%, #FF6B3D)"><span style="position: absolute; left: 40%; top: -4px; width: 16px; height: 16px; border-radius: 8px; background: var(--surf); box-shadow: 0 0 0 3px var(--ink), 0 2px 6px var(--shadow); margin-left: -8px; animation: mark 1s cubic-bezier(.2,.8,.2,1) .5s both"></span></span>
    <span style="font-size: 13px; line-height: 1.4; color: var(--ink2)">Nu setezi un preț. <b style="color: var(--ink)">Jobzerii îți trimit oferte</b>, iar tu o alegi pe cea potrivită. Taxa Jobzee de 15% se adaugă peste oferta aleasă.</span>
  </div>

  <div style="flex-grow: 1"></div>
  <a href="FaraOferte.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 600; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.35)">{{cta}}</a>
</div>'''
    return page('Fișa cererii', 'L', b, css, logic)


# ---------------------------------------------------------------- Toate serviciile (30 de familii)
FAMILIES = [
    # (name, group, photo or None, icon)
    ('Montaj mobilier', 'rep', 'mobila', 'mobila'), ('Curățenie', 'casa', 'curatenie', 'curatenie'), ('Mutat și cărat', 'casa', 'mutat-obiecte', 'mutat-obiecte'),
    ('Instalații sanitare', 'rep', 'sanitar', 'sanitar'), ('Electricitate', 'rep', 'electrica', 'electrica'), ('Electrocasnice', 'rep', 'electrocasnice', 'electrocasnice'),
    ('Zugrăveli', 'casa', 'zugraveala', 'zugraveala'), ('Grădină și curte', 'casa', 'gradina', 'gradina'), ('Animale de companie', 'pers', 'animale', 'animale'),
    ('Cumpărături', 'alt', 'cumparaturi', 'cumparaturi'), ('Îngrijire persoane', 'pers', 'ingrijire-persoane', 'ingrijire-persoane'), ('IT și tehnică', 'rep', 'it', 'it'),
    ('Reparații mici', 'rep', None, 'reparatii'), ('Tâmplărie și uși', 'rep', None, 'tamplarie'), ('Gresie și parchet', 'casa', None, 'gresie'),
    ('Climă și centrale', 'rep', None, 'clima'), ('Lăcătuș și yale', 'rep', None, 'lacatus'), ('Spălat auto', 'alt', None, 'auto'),
    ('Livrări locale', 'alt', None, 'livrari'), ('Gătit acasă', 'pers', None, 'gatit'), ('Babysitting', 'pers', None, 'babysitting'),
    ('Meditații', 'pers', None, 'meditatii'), ('Evenimente', 'alt', None, 'evenimente'), ('Foto și video', 'alt', None, 'foto'),
    ('Frumusețe acasă', 'pers', None, 'frumusete'), ('Fitness', 'pers', None, 'fitness'), ('Călcat și croitorie', 'casa', None, 'calcat'),
    ('Dezinsecție', 'casa', None, 'dezinsectie'), ('Geamuri', 'casa', None, 'geamuri'), ('Acte și birou', 'alt', None, 'acte'),
]


def servicii():
    H = 1320
    css = """
.fc{border:0;height:36px;padding:0 14px;border-radius:18px;background:var(--surf);font-family:inherit;font-size:14px;font-weight:600;color:var(--ink);cursor:pointer;transition:all .25s;box-shadow:0 1px 0 var(--sep)}
.fc[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}
.tile{display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none;color:var(--ink);font-size:12px;font-weight:600;text-align:center;line-height:1.2}
.tile .pic{width:100%;aspect-ratio:1;border-radius:50%;overflow:hidden;background-size:cover;background-position:center;position:relative;box-shadow:0 6px 16px var(--shadow)}
"""
    data = json.dumps([{'n': n, 'g': g, 'p': p, 'i': i} for n, g, p, i in FAMILIES], ensure_ascii=False)
    logic = ("""constructor(props) { super(props); this.state = { g: 'all' }; }
  renderVals() {
    const all = """ + data + """;
    const g = this.state.g;
    const tint = { casa: '#E8F4FF', rep: '#FFF4E5', pers: '#FCEBF1', alt: '#EEF8EA' };
    const items = all.filter(x => g === 'all' || x.g === g).map(x => ({
      name: x.n,
      picStyle: x.p ? 'background-image: url(assets/services/service-' + x.p + '.webp)' : 'background: ' + tint[x.g] + '; display: flex; align-items: center; justify-content: center',
      icStyle: x.p ? 'display: none' : 'width: 34px; height: 34px; background: #B35600; -webkit-mask: url(assets/icons/icon-' + x.i + '.svg) center/contain no-repeat; mask: url(assets/icons/icon-' + x.i + '.svg) center/contain no-repeat'
    }));
    const f = (k) => ({ attr: g === k ? 'true' : 'false', pick: () => this.setState({ g: k }) });
    return { items, count: items.length, fAll: f('all'), fCasa: f('casa'), fRep: f('rep'), fPers: f('pers'), fAlt: f('alt') };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 14px">
  <div style="display: flex; align-items: center; justify-content: space-between">
    <a href="Acasa.dc.html" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    <span style="font-size: 13px; font-weight: 600; color: var(--ink2)">{{count}} familii de servicii</span>
  </div>
  <div class="u" style="display: flex; align-items: flex-end; justify-content: space-between">
    <h1 style="margin: 0 4px; font-size: 34px; line-height: 1.05; font-weight: 700; letter-spacing: -0.9px">Toate<br>serviciile</h1>
    <img class="float" src="assets/mascot/zee-cauta.svg" alt="" style="width: 86px; height: 92px; margin-right: 6px">
  </div>
  <a href="Dialog.dc.html" class="u d1 pr" style="display: flex; align-items: center; gap: 10px; height: 50px; padding: 0 16px; border-radius: 25px; background: var(--surf); color: var(--ink2); text-decoration: none; font-size: 16px; box-shadow: 0 4px 14px var(--shadow)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-3.5-3.5"></path></svg>Caută: „robinet”, „TV pe perete”…</a>
  <div class="u d2" style="display: flex; gap: 8px; flex-wrap: wrap">
    <button type="button" class="fc" onClick="{{fAll.pick}}" aria-pressed="{{fAll.attr}}">Toate</button>
    <button type="button" class="fc" onClick="{{fCasa.pick}}" aria-pressed="{{fCasa.attr}}">Casă</button>
    <button type="button" class="fc" onClick="{{fRep.pick}}" aria-pressed="{{fRep.attr}}">Reparații</button>
    <button type="button" class="fc" onClick="{{fPers.pick}}" aria-pressed="{{fPers.attr}}">Persoane</button>
    <button type="button" class="fc" onClick="{{fAlt.pick}}" aria-pressed="{{fAlt.attr}}">Altele</button>
  </div>
  <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px 10px; padding: 4px 0">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="30">
      <a href="Dialog.dc.html" class="tile pr pop"><span class="pic" style="{{x.picStyle}}"><span style="{{x.icStyle}}"></span></span>{{x.name}}</a>
    </sc-for>
  </div>
  <a href="Dialog.dc.html" class="pr" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 26px; background: var(--bsoft); color: var(--ink); text-decoration: none">
    <img src="assets/mascot/zee-gandeste.svg" alt="" style="width: 48px; height: 52px; flex-shrink: 0">
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 700">Nu găsești ce cauți?</span><span style="font-size: 13px; color: var(--ink2)">Descrie-i lui Jobzee AI și îți găsește familia potrivită.</span></span>''' + CHEV + '''</a>
</div>
''' + tabbar('client', 'acasa', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'})
    return page('Toate serviciile', 'L', b, css, logic, h=H)
