

# ================================================================ COMPETENȚE ȘI PORTOFOLIU (Jobzer)
SK_CSS = SEG_CSS + """
@keyframes inUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.in{animation:inUp .35s cubic-bezier(.2,.8,.2,1) both}
.cat{border:0;background:transparent;padding:0;font-family:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:5px;color:var(--ink);font-size:11px;font-weight:500;line-height:1.2;text-align:center}
.cat img{width:100%;aspect-ratio:1;border-radius:30%;display:block;box-shadow:0 4px 12px var(--shadow);transition:transform .25s cubic-bezier(.3,1.4,.4,1),box-shadow .25s}
.cat[aria-pressed="true"] img{box-shadow:0 0 0 3px var(--bg),0 0 0 5.5px var(--brand);transform:scale(.94)}
.chip{border:0;height:32px;padding:0 12px;border-radius:16px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer;transition:all .25s;white-space:nowrap}
.chip[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}.chip[aria-pressed="false"]{background:var(--surf2);color:var(--ink)}
.stp{display:flex;align-items:center;height:36px;border-radius:18px;background:var(--surf2)}
.stp button{width:36px;height:36px;border:0;background:transparent;font-size:18px;color:var(--ink);cursor:pointer;font-family:inherit}
.tag{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:11px;font-size:11px;font-weight:500;white-space:nowrap}
.t-ok{background:var(--oksoft);color:var(--oktext)}.t-wait{background:var(--bsoft);color:var(--btext)}.t-no{background:var(--surf2);color:var(--ink2)}
.fld2{width:100%;box-sizing:border-box;border:0;outline:0;background:var(--surf2);border-radius:14px;padding:10px 12px;font-family:inherit;font-size:15px;color:var(--ink)}
"""

CAT_JSON = json.dumps([{'n': n, 'i': i} for n, g, p, i in FAMILIES], ensure_ascii=False)


def skilluri():
    logic = ("""constructor(props) { super(props); this.state = { sel: { mobila: true, reparatii: true, tamplarie: true }, q: '', all: false, tools: true }; }
  renderVals() {
    const s = this.state, C = """ + CAT_JSON + """;
    const top = ['mobila', 'reparatii', 'curatenie', 'mutat-obiecte', 'sanitar', 'electrica', 'tamplarie', 'zugraveala', 'gradina', 'it', 'animale', 'cumparaturi'];
    const norm = (x) => x.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
    const q = norm(s.q.trim());
    let list = q ? C.filter((c) => norm(c.n).indexOf(q) >= 0) : (s.all ? C : top.map((k) => C.find((c) => c.i === k)));
    const cats = list.map((c) => ({ n: c.n, src: 'assets/cat/' + c.i + '.svg', attr: s.sel[c.i] ? 'true' : 'false', pick: () => { const o = Object.assign({}, s.sel); if (o[c.i]) delete o[c.i]; else o[c.i] = true; this.setState({ sel: o }); } }));
    const n = Object.keys(s.sel).length;
    const chosen = C.filter((c) => s.sel[c.i]).map((c) => c.n);
    return { cats: cats, none: cats.length === 0, q: s.q, onQ: (e) => this.setState({ q: e.target.value }), showAll: !q && !s.all, more: () => this.setState({ all: true }),
      cta: n ? 'Continuă · ' + n + (n === 1 ? ' competență' : ' competențe') : 'Alege cel puțin o competență', ctaOn: n > 0, ctaOff: n === 0,
      chosenTxt: chosen.join(' · '), hasChosen: n > 0,
      toolsAttr: s.tools ? 'true' : 'false', toggleTools: () => this.setState({ tools: !s.tools }) };
  }""")
    b = '''<div style="padding: 54px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  <div style="display: flex; align-items: center; gap: 12px">''' + topbar('DevinoJobzer.dc.html').replace('<div style="display: flex; align-items: center; justify-content: space-between">', '<div>') + '''
    <span style="flex-grow: 1; height: 6px; border-radius: 3px; background: var(--surf3); overflow: hidden"><span style="display: block; width: 50%; height: 100%; border-radius: 3px; background: var(--brand)"></span></span><span style="font-size: 13px; font-weight: 500; color: var(--ink2)">2/4</span></div>
  ''' + h1('Ce știi să faci?', 'Alege tot ce faci bine. Detaliile, prețul și pozele le adaugi după, în profil.') + '''
  <label class="u d1" style="display: flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border-radius: 22px; background: var(--surf); color: var(--ink2); box-shadow: 0 2px 10px var(--shadow)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><span style="position: absolute; left: -9999px">Caută o competență</span><input value="{{q}}" onChange="{{onQ}}" placeholder="Caută: „gresie”, „babysitting”…" style="flex-grow: 1; min-width: 0; border: 0; outline: 0; background: transparent; font-family: inherit; font-size: 16px; color: var(--ink)"></label>
  <div class="u d2" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px 12px; padding: 4px 2px">
    <sc-for list="{{cats}}" as="c" hint-placeholder-count="12"><button type="button" class="cat pr" onClick="{{c.pick}}" aria-pressed="{{c.attr}}"><img src="{{c.src}}" alt="">{{c.n}}</button></sc-for>
  </div>
  <sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><span style="text-align: center; font-size: 14px; color: var(--ink2); padding: 10px">Nu găsim „{{q}}”. Alege cea mai apropiată categorie, iar în profil scrii exact ce faci.</span></sc-if>
  <sc-if value="{{showAll}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{more}}" class="pr" style="align-self: center; height: 36px; padding: 0 16px; border: 0; border-radius: 18px; background: var(--surf); color: var(--btext); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Vezi toate cele 30 de categorii</button></sc-if>
  <div class="grp"><div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Am uneltele mele</span><span style="font-size: 12px; color: var(--ink2)">Primești și cereri „vino cu unelte”</span></span><button type="button" class="jsw" onClick="{{toggleTools}}" aria-pressed="{{toolsAttr}}" aria-label="Am uneltele mele"></button></div></div>
  <div style="flex-grow: 1"></div>
  <sc-if value="{{hasChosen}}" hint-placeholder-val="{{ true }}"><span style="font-size: 12px; color: var(--ink2); text-align: center">{{chosenTxt}}</span></sc-if>
  <sc-if value="{{ctaOn}}" hint-placeholder-val="{{ true }}"><a href="Identitate.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">{{cta}}</a></sc-if>
  <sc-if value="{{ctaOff}}" hint-placeholder-val="{{ false }}"><span style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--surf3); color: var(--ink2); font-size: 16px; font-weight: 500">{{cta}}</span></sc-if>
</div>'''
    return page('Ce știi să faci', 'L', b, SK_CSS, logic, h=1060)


PORT = [dict(id='p1', src='assets/services/service-mobila.webp', pos='50% 50%', sk='mobila', cap='Dulap cu rafturi, Floreasca'),
        dict(id='p2', src='assets/services/service-electrocasnice.webp', pos='50% 50%', sk='mobila', cap='Bucătărie montată, hotă inclusă'),
        dict(id='p3', src='assets/services/service-sanitar.webp', pos='55% 50%', sk='reparatii', cap='Sifon schimbat'),
        dict(id='p4', src='assets/services/service-electrica.webp', pos='50% 40%', sk='reparatii', cap='Corpuri de iluminat'),
        dict(id='p5', src='assets/services/service-zugraveala.webp', pos='50% 50%', sk='tamplarie', cap='Ușă nouă, finisaj')]
POOL = [dict(src='assets/services/service-mobila.webp', pos='18% 50%', cap='Detaliu: balamale reglate'), dict(src='assets/services/service-mutat-obiecte.webp', pos='50% 50%', cap='Mobilă livrată și montată'),
        dict(src='assets/services/service-electrocasnice.webp', pos='80% 40%', cap='Detaliu: blat și sertare'), dict(src='assets/photos/hero-jobzer-outdoor.webp', pos='60% 40%', cap='Echipamentul meu')]

SKILLS = [dict(i='mobila', n='Montaj mobilier', lvl=2, yrs=8, unit='l', price=120, jobs=54, cert='ok', certName='Calificare tâmplar · verificată',
               specs=[['Mobilier IKEA', True], ['Bucătării', True], ['Dressing', False], ['Montaj TV și rafturi', True], ['Paturi și somiere', False]], mkt='100–180 lei'),
          dict(i='reparatii', n='Reparații mici', lvl=1, yrs=5, unit='h', price=80, jobs=22, cert='no', certName='',
               specs=[['Agățat tablouri și oglinzi', True], ['Reglaj uși și sertare', True], ['Silicon și chituri', False], ['Înlocuit mânere și yale', True]], mkt='70–110 lei/h'),
          dict(i='tamplarie', n='Tâmplărie și uși', lvl=1, yrs=3, unit='l', price=150, jobs=10, cert='wait', certName='Diplomă școală profesională · în verificare',
               specs=[['Montaj uși interioare', True], ['Reglaj și balamale', True], ['Pervaze și plinte', False]], mkt='120–250 lei')]


def profil_edit():
    logic = ("""constructor(props) {
    super(props);
    this.n = 10;
    this.state = { skills: """ + json.dumps(SKILLS, ensure_ascii=False) + """, open: 'mobila', photos: """ + json.dumps(PORT, ensure_ascii=False) + """, pool: """ + json.dumps(POOL, ensure_ascii=False) + """,
      pf: 'all', add: 0, pick: '', nlvl: 1, nunit: 'l', nprice: 100, q: '', bio: 'Montez mobilier de 8 ani, de la IKEA la bucătării pe comandă. Vin cu toate uneltele și las curat după mine.',
      days: { L: true, Ma: true, Mi: true, J: true, V: true, S: true, D: false }, radius: 5, toast: '', bioEdit: false };
  }
  componentWillUnmount() { clearTimeout(this.tt); }
  toast(t, at) { this.setState({ toast: t, toastAt: at || 'sk' }); clearTimeout(this.tt); this.tt = setTimeout(() => this.setState({ toast: '' }), 2200); }
  upd(i, fn) { this.setState({ skills: this.state.skills.map((k) => k.i === i ? fn(Object.assign({}, k)) : k) }); }
  renderVals() {
    const s = this.state, C = """ + CAT_JSON + """;
    const LV = ['Începător', 'Experimentat', 'Expert'];
    const lei = (k) => k.price + (k.unit === 'h' ? ' lei/h' : ' lei');
    const nPh = (i) => s.photos.filter((p) => p.sk === i).length;
    const skills = s.skills.map((k) => {
      const open = s.open === k.i;
      return { n: k.n, src: 'assets/cat/' + k.i + '.svg', sub: LV[k.lvl] + ' · ' + k.yrs + ' ani · de la ' + lei(k) + (k.unit === 'h' ? '' : ' / lucrare'),
        jobs: k.jobs + ' lucrări în Jobzee', hasJobs: k.jobs > 0, ph: nPh(k.i) + (nPh(k.i) === 1 ? ' poză' : ' poze'), phTag: 'tag ' + (nPh(k.i) ? 't-no' : 't-wait'),
        certTag: 'tag ' + (k.cert === 'ok' ? 't-ok' : k.cert === 'wait' ? 't-wait' : 't-no'), certTxt: k.cert === 'ok' ? '✓ Calificare verificată' : k.cert === 'wait' ? 'Act în verificare' : 'Fără act',
        open: open, closed: !open, toggle: () => this.setState({ open: open ? '' : k.i }),
        lvls: LV.map((t, li) => ({ t: t, attr: k.lvl === li ? 'true' : 'false', pick: () => this.upd(k.i, (x) => { x.lvl = li; return x; }) })),
        lvlHint: ['Ai făcut lucrarea de câteva ori și o faci corect.', 'O faci des, fără ajutor, și știi să rezolvi neprevăzutele.', 'Peste 5 ani sau peste 50 de lucrări. Clienții te pot întreba de detalii tehnice.'][k.lvl],
        yrs: k.yrs + (k.yrs === 1 ? ' an' : ' ani'), yMinus: () => this.upd(k.i, (x) => { x.yrs = Math.max(0, x.yrs - 1); return x; }), yPlus: () => this.upd(k.i, (x) => { x.yrs = Math.min(40, x.yrs + 1); return x; }),
        uL: k.unit === 'l' ? 'true' : 'false', uH: k.unit === 'h' ? 'true' : 'false', setL: () => this.upd(k.i, (x) => { x.unit = 'l'; return x; }), setH: () => this.upd(k.i, (x) => { x.unit = 'h'; return x; }),
        price: lei(k), pMinus: () => this.upd(k.i, (x) => { x.price = Math.max(10, x.price - 10); return x; }), pPlus: () => this.upd(k.i, (x) => { x.price = x.price + 10; return x; }), mkt: 'În zona ta, alți Jobzeri cer ' + k.mkt + '.',
        specs: k.specs.map((sp, si) => ({ t: sp[0], attr: sp[1] ? 'true' : 'false', pick: () => this.upd(k.i, (x) => { x.specs = x.specs.map((y, yi) => yi === si ? [y[0], !y[1]] : y); return x; }) })),
        certOk: k.cert === 'ok', certWait: k.cert === 'wait', certNo: k.cert === 'no', certName: k.certName,
        upCert: () => { this.upd(k.i, (x) => { x.cert = 'wait'; x.certName = 'Document încărcat · în verificare (de obicei 24 h)'; return x; }); this.toast('Am primit documentul. Îl verificăm în 24 de ore.', 'sk'); },
        addPh: () => { this.setState({ pf: k.i }); this.addPhoto(k.i); },
        del: () => { this.setState({ skills: s.skills.filter((x) => x.i !== k.i), photos: s.photos.map((p) => p.sk === k.i ? Object.assign({}, p, { sk: '' }) : p), open: '' }); this.toast(k.n + ' a fost scoasă din profil.'); } };
    });
    // portofoliu
    const sname = (i) => (s.skills.find((k) => k.i === i) || { n: 'Fără competență' }).n;
    const shown = s.photos.filter((p) => s.pf === 'all' || p.sk === s.pf);
    const photos = shown.map((p) => ({ id: p.id, st: 'background-image: url(' + p.src + '); background-size: cover; background-position: ' + p.pos, cap: p.cap, sk: sname(p.sk),
      rm: () => { this.setState({ photos: s.photos.filter((x) => x.id !== p.id), pool: s.pool.concat([{ src: p.src, pos: p.pos, cap: p.cap }]) }); this.toast('Poza a fost ștearsă.', 'ph'); } }));
    const pfs = [{ t: 'Toate · ' + s.photos.length, k: 'all' }].concat(s.skills.map((k) => ({ t: k.n + ' · ' + nPh(k.i), k: k.i }))).map((x) => ({ t: x.t, attr: s.pf === x.k ? 'true' : 'false', pick: () => this.setState({ pf: x.k }) }));
    // adăugare competență: 0 închis, 1 alege categoria, 2 detalii
    const q = s.q.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
    const avail = C.filter((c) => !s.skills.some((k) => k.i === c.i) && (!q || c.n.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').indexOf(q) >= 0));
    const cats = avail.slice(0, 16).map((c) => ({ n: c.n, src: 'assets/cat/' + c.i + '.svg', pick: () => this.setState({ pick: c.i, add: 2, nlvl: 1, nunit: 'l', nprice: 100 }) }));
    const pc = C.find((c) => c.i === s.pick) || C[0];
    const nl = LV.map((t, li) => ({ t: t, attr: s.nlvl === li ? 'true' : 'false', pick: () => this.setState({ nlvl: li }) }));
    const save = () => {
      const k = { i: pc.i, n: pc.n, lvl: s.nlvl, yrs: 1, unit: s.nunit, price: s.nprice, jobs: 0, cert: 'no', certName: '', specs: [], mkt: 'prețuri diferite, după lucrare' };
      this.setState({ skills: s.skills.concat([k]), add: 0, pick: '', q: '', open: pc.i }); this.toast(pc.n + ' a fost adăugată. Pune și 2–3 poze cu lucrări.');
    };
    // completare profil: doar lucruri pe care Jobzerul le poate face
    const checks = [['Poză de profil', true], ['Descriere', s.bio.trim().length >= 40], ['Cel puțin 3 competențe', s.skills.length >= 3], ['Minim 6 poze în portofoliu', s.photos.length >= 6], ['Un act pentru fiecare meserie calificată', s.skills.every((k) => k.cert !== 'no' || k.i === 'reparatii')]];
    const done = checks.filter((c) => c[1]).length, pct = Math.round(done / checks.length * 100);
    const next = checks.find((c) => !c[1]);
    const days = ['L', 'Ma', 'Mi', 'J', 'V', 'S', 'D'].map((d) => ({ t: d, attr: s.days[d] ? 'true' : 'false', pick: () => { const x = Object.assign({}, s.days); x[d] = !x[d]; this.setState({ days: x }); } }));
    const radii = [3, 5, 10, 20].map((r) => ({ t: r + ' km', attr: s.radius === r ? 'true' : 'false', pick: () => this.setState({ radius: r }) }));
    return { skills: skills, nSk: s.skills.length, photos: photos, nPh: s.photos.length, pfs: pfs, emptyPh: photos.length === 0,
      addPhoto: () => this.addPhoto(s.pf === 'all' ? (s.skills[0] || { i: '' }).i : s.pf), canAddPh: s.pool.length > 0,
      add0: s.add === 0, add1: s.add === 1, add2: s.add === 2, openAdd: () => this.setState({ add: 1, q: '' }), closeAdd: () => this.setState({ add: 0, pick: '', q: '' }), backAdd: () => this.setState({ add: 1 }),
      q: s.q, onQ: (e) => this.setState({ q: e.target.value }), cats: cats, noCats: cats.length === 0,
      pcN: pc.n, pcSrc: 'assets/cat/' + pc.i + '.svg', nl: nl, nuL: s.nunit === 'l' ? 'true' : 'false', nuH: s.nunit === 'h' ? 'true' : 'false', setNL: () => this.setState({ nunit: 'l' }), setNH: () => this.setState({ nunit: 'h' }),
      nprice: s.nprice + (s.nunit === 'h' ? ' lei/h' : ' lei'), npM: () => this.setState({ nprice: Math.max(10, s.nprice - 10) }), npP: () => this.setState({ nprice: s.nprice + 10 }), save: save,
      pct: pct + '%', ring: 'stroke-dashoffset: ' + (138 - 138 * pct / 100).toFixed(1) + '; transition: stroke-dashoffset .6s', nextTxt: next ? 'Pasul următor: ' + next[0].toLowerCase() + '.' : 'Profil complet. Clienții văd tot ce trebuie ca să te aleagă.',
      checks: checks.map((c) => ({ t: c[0], st: 'width: 18px; height: 18px; border-radius: 9px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 11px; ' + (c[1] ? 'background: var(--ok); color: #FFFFFF' : 'box-shadow: inset 0 0 0 1.5px var(--ink3); color: transparent'), tx: 'font-size: 13px; ' + (c[1] ? 'color: var(--ink2)' : 'color: var(--ink); font-weight: 500') })),
      bio: s.bio, onBio: (e) => this.setState({ bio: e.target.value.slice(0, 220) }), bioN: s.bio.length + '/220', bioEdit: s.bioEdit, bioView: !s.bioEdit, editBio: () => this.setState({ bioEdit: true }), doneBio: () => { this.setState({ bioEdit: false }); this.toast('Descrierea a fost salvată.', 'bio'); },
      days: days, radii: radii, toast: s.toast, hasToast: !!s.toast, saveAll: () => this.toast('Profilul a fost salvat. Clienții văd modificările imediat.', 'end'),
      tSk: !!s.toast && s.toastAt === 'sk', tPh: !!s.toast && s.toastAt === 'ph', tBio: !!s.toast && s.toastAt === 'bio', tEnd: !!s.toast && s.toastAt === 'end' };
  }
  addPhoto(sk) {
    const s = this.state; if (!s.pool.length) { this.toast('Ai adăugat toate pozele din galerie.', 'ph'); return; }
    const p = s.pool[0];
    this.setState({ photos: [{ id: 'n' + (this.n++), src: p.src, pos: p.pos, cap: p.cap, sk: sk }].concat(s.photos), pool: s.pool.slice(1) });
    this.toast('Poza a fost adăugată la ' + ((s.skills.find((k) => k.i === sk) || { n: 'portofoliu' }).n) + '.', 'ph');
  }""")
    stepper = lambda m, v, p, lab: ('<span class="stp"><button type="button" onClick="{{' + m + '}}" aria-label="Mai puțin ' + lab + '">−</button><span style="min-width: 70px; text-align: center; font-size: 15px; font-weight: 500; font-variant-numeric: tabular-nums">{{' + v + '}}</span><button type="button" onClick="{{' + p + '}}" aria-label="Mai mult ' + lab + '">+</button></span>')
    b = '''<div style="padding: 52px 16px 120px; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('ContJobzer.dc.html', '<a href="Profil.dc.html" class="pr" style="height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); display: flex; align-items: center; font-size: 14px; font-weight: 500; text-decoration: none">Cum te văd clienții ›</a>') + '''
  ''' + h1('Profilul meu') + '''
  <div class="card u d1" style="background: var(--surf); border-radius: 24px; padding: 14px; display: flex; gap: 14px; align-items: center">
    <span style="position: relative; width: 60px; height: 60px; flex-shrink: 0"><svg width="60" height="60" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="22" fill="none" stroke="var(--surf3)" stroke-width="5"></circle><circle cx="26" cy="26" r="22" fill="none" stroke="var(--brand)" stroke-width="5" stroke-linecap="round" stroke-dasharray="138" style="{{ring}}" transform="rotate(-90 26 26)"></circle></svg><span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600">{{pct}}</span></span>
    <span style="display: flex; flex-direction: column; gap: 5px; flex-grow: 1"><sc-for list="{{checks}}" as="c" hint-placeholder-count="5"><span style="display: flex; align-items: center; gap: 8px"><span style="{{c.st}}">✓</span><span style="{{c.tx}}">{{c.t}}</span></span></sc-for></span>
  </div>
  <span style="font-size: 13px; color: var(--ink2); padding: 0 6px; margin-top: -4px">{{nextTxt}}</span>

  <div style="display: flex; align-items: baseline; justify-content: space-between; padding: 6px 6px 0"><span class="lbl" style="padding: 0">Competențe · {{nSk}}</span><span style="font-size: 12px; color: var(--ink2)">Atinge una ca s-o editezi</span></div>
  <sc-if value="{{tSk}}" hint-placeholder-val="{{ false }}"><div class="in" style="padding: 11px 14px; border-radius: 16px; background: var(--invbg); color: var(--invink); font-size: 14px; line-height: 1.35">✓ {{toast}}</div></sc-if>
  <sc-for list="{{skills}}" as="k" hint-placeholder-count="3">
    <div class="in" style="background: var(--surf); border-radius: 24px; overflow: hidden; margin-bottom: 8px">
      <button type="button" onClick="{{k.toggle}}" style="width: 100%; border: 0; background: transparent; padding: 12px 14px; display: flex; gap: 12px; align-items: center; font-family: inherit; color: var(--ink); text-align: left; cursor: pointer">
        <img src="{{k.src}}" alt="" style="width: 50px; height: 50px; border-radius: 15px; flex-shrink: 0">
        <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 16px; font-weight: 600">{{k.n}}</span><span style="font-size: 12px; color: var(--ink2)">{{k.sub}}</span>
          <span style="display: flex; gap: 5px; flex-wrap: wrap"><sc-if value="{{k.hasJobs}}" hint-placeholder-val="{{ true }}"><span class="tag t-no">{{k.jobs}}</span></sc-if><span class="{{k.certTag}}">{{k.certTxt}}</span><span class="{{k.phTag}}">{{k.ph}}</span></span></span>
        <sc-if value="{{k.closed}}" hint-placeholder-val="{{ true }}">''' + CHEV + '''</sc-if>
        <sc-if value="{{k.open}}" hint-placeholder-val="{{ false }}"><span style="transform: rotate(90deg); display: flex">''' + CHEV + '''</span></sc-if>
      </button>
      <sc-if value="{{k.open}}" hint-placeholder-val="{{ false }}"><div class="in" style="padding: 2px 14px 14px; display: flex; flex-direction: column; gap: 12px; box-shadow: inset 0 0.5px 0 var(--sep)">
        <span style="font-size: 13px; font-weight: 500; color: var(--ink2); padding-top: 10px">Nivel</span>
        <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: -6px"><sc-for list="{{k.lvls}}" as="l" hint-placeholder-count="3"><button type="button" onClick="{{l.pick}}" aria-pressed="{{l.attr}}">{{l.t}}</button></sc-for></div>
        <span style="font-size: 12px; line-height: 1.35; color: var(--ink2); margin-top: -6px">{{k.lvlHint}}</span>
        <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px">Experiență</span>''' + stepper('k.yMinus', 'k.yrs', 'k.yPlus', 'experiență') + '''</div>
        <div style="display: flex; flex-direction: column; gap: 8px"><span style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px">Preț de pornire</span>''' + stepper('k.pMinus', 'k.price', 'k.pPlus', 'preț') + '''</span>
          <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><button type="button" onClick="{{k.setL}}" aria-pressed="{{k.uL}}">Pe lucrare</button><button type="button" onClick="{{k.setH}}" aria-pressed="{{k.uH}}">Pe oră</button></div>
          <span style="font-size: 12px; color: var(--ink2)">{{k.mkt}} Clientul vede „de la”, iar prețul final îl dai în ofertă.</span></div>
        <span style="font-size: 13px; font-weight: 500; color: var(--ink2)">Ce faci exact</span>
        <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-top: -6px"><sc-for list="{{k.specs}}" as="x" hint-placeholder-count="4"><button type="button" class="chip" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.t}}</button></sc-for></div>
        <div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 16px; background: var(--surf2)">
          <img src="assets/ui/shield.png" alt="" style="width: 24px; height: 24px">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 14px; font-weight: 500">Calificare sau certificat</span>
            <sc-if value="{{k.certNo}}" hint-placeholder-val="{{ false }}"><span style="font-size: 12px; color: var(--ink2)">Opțional. Un act verificat primește insigna ✓ pe profil.</span></sc-if>
            <sc-if value="{{k.certOk}}" hint-placeholder-val="{{ true }}"><span style="font-size: 12px; color: var(--oktext)">{{k.certName}}</span></sc-if>
            <sc-if value="{{k.certWait}}" hint-placeholder-val="{{ false }}"><span style="font-size: 12px; color: var(--btext)">{{k.certName}}</span></sc-if></span>
          <sc-if value="{{k.certNo}}" hint-placeholder-val="{{ false }}"><button type="button" onClick="{{k.upCert}}" class="pr" style="height: 32px; padding: 0 12px; border: 0; border-radius: 16px; background: var(--invbg); color: var(--invink); font-family: inherit; font-size: 13px; font-weight: 500; cursor: pointer">Încarcă</button></sc-if>
        </div>
        <div style="display: flex; gap: 8px"><button type="button" onClick="{{k.addPh}}" class="pr" style="flex: 1; height: 42px; border: 0; border-radius: 21px; background: var(--bsoft); color: var(--btext); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">+ Adaugă poze</button>
          <button type="button" onClick="{{k.del}}" class="pr" style="height: 42px; padding: 0 14px; border: 0; border-radius: 21px; background: transparent; color: #D70015; font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Scoate</button></div>
      </div></sc-if>
    </div>
  </sc-for>

  <sc-if value="{{add0}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{openAdd}}" class="pr" style="height: 52px; border: 0; border-radius: 26px; background: var(--surf); color: var(--btext); font-family: inherit; font-size: 16px; font-weight: 500; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; box-shadow: inset 0 0 0 1.5px var(--bsoft2)"><span style="width: 24px; height: 24px; border-radius: 12px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center; font-size: 18px">+</span>Adaugă o competență</button></sc-if>
  <sc-if value="{{add1}}" hint-placeholder-val="{{ false }}"><div class="in" style="background: var(--surf); border-radius: 24px; padding: 14px; display: flex; flex-direction: column; gap: 12px; box-shadow: inset 0 0 0 2px var(--brand)">
    <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 16px; font-weight: 600">Ce competență adaugi?</span><button type="button" onClick="{{closeAdd}}" class="pr" style="height: 30px; padding: 0 10px; border: 0; border-radius: 15px; background: var(--surf2); color: var(--ink); font-family: inherit; font-size: 13px; cursor: pointer">Renunță</button></div>
    <label><span style="position: absolute; left: -9999px">Caută categoria</span><input class="fld2" value="{{q}}" onChange="{{onQ}}" placeholder="Caută: gresie, fitness, meditații…"></label>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px 10px"><sc-for list="{{cats}}" as="c" hint-placeholder-count="8"><button type="button" class="cat pr" onClick="{{c.pick}}"><img src="{{c.src}}" alt="">{{c.n}}</button></sc-for></div>
    <sc-if value="{{noCats}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; color: var(--ink2); text-align: center">Nicio categorie nu se potrivește. Încearcă alt cuvânt.</span></sc-if>
  </div></sc-if>
  <sc-if value="{{add2}}" hint-placeholder-val="{{ false }}"><div class="in" style="background: var(--surf); border-radius: 24px; padding: 14px; display: flex; flex-direction: column; gap: 12px; box-shadow: inset 0 0 0 2px var(--brand)">
    <div style="display: flex; align-items: center; gap: 12px"><img src="{{pcSrc}}" alt="" style="width: 50px; height: 50px; border-radius: 15px"><span style="flex-grow: 1; font-size: 17px; font-weight: 600">{{pcN}}</span><button type="button" onClick="{{backAdd}}" class="pr" style="height: 30px; padding: 0 10px; border: 0; border-radius: 15px; background: var(--surf2); color: var(--ink); font-family: inherit; font-size: 13px; cursor: pointer">Schimbă</button></div>
    <span style="font-size: 13px; font-weight: 500; color: var(--ink2)">Cât de bine o faci?</span>
    <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: -6px"><sc-for list="{{nl}}" as="l" hint-placeholder-count="3"><button type="button" onClick="{{l.pick}}" aria-pressed="{{l.attr}}">{{l.t}}</button></sc-for></div>
    <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><button type="button" onClick="{{setNL}}" aria-pressed="{{nuL}}">Pe lucrare</button><button type="button" onClick="{{setNH}}" aria-pressed="{{nuH}}">Pe oră</button></div>
    <div style="display: flex; align-items: center; justify-content: space-between"><span style="font-size: 15px">Preț de pornire</span>''' + stepper('npM', 'nprice', 'npP', 'preț') + '''</div>
    <button type="button" onClick="{{save}}" class="pr" style="height: 50px; border: 0; border-radius: 25px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 16px; font-weight: 500; cursor: pointer">Adaugă în profil</button>
    <span style="font-size: 12px; color: var(--ink2); text-align: center">Experiența, actele și pozele le completezi imediat după.</span>
  </div></sc-if>

  <div style="display: flex; align-items: baseline; justify-content: space-between; padding: 10px 6px 0"><span class="lbl" style="padding: 0">Portofoliu · {{nPh}} poze</span><span style="font-size: 12px; color: var(--ink2)">Lucrări reale, făcute de tine</span></div>
  <sc-if value="{{tPh}}" hint-placeholder-val="{{ false }}"><div class="in" style="padding: 11px 14px; border-radius: 16px; background: var(--invbg); color: var(--invink); font-size: 14px; line-height: 1.35">✓ {{toast}}</div></sc-if>
  <div class="scroll" style="display: flex; gap: 6px; overflow-x: auto; margin: 0 -16px; padding: 0 16px; scrollbar-width: none"><sc-for list="{{pfs}}" as="f" hint-placeholder-count="4"><button type="button" class="chip" onClick="{{f.pick}}" aria-pressed="{{f.attr}}" style="flex-shrink: 0">{{f.t}}</button></sc-for></div>
  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">
    <sc-if value="{{canAddPh}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{addPhoto}}" class="pr" style="aspect-ratio: 1; border: 0; border-radius: 18px; background: var(--bsoft); color: var(--btext); font-family: inherit; font-size: 12px; font-weight: 500; cursor: pointer; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px"><img src="assets/ui/camera.png" alt="" style="width: 30px; height: 30px">Adaugă poze</button></sc-if>
    <sc-for list="{{photos}}" as="p" hint-placeholder-count="5">
      <div class="in" style="position: relative; aspect-ratio: 1; border-radius: 18px; overflow: hidden; {{p.st}}">
        <span style="position: absolute; left: 0; right: 0; bottom: 0; padding: 18px 7px 6px; background: linear-gradient(transparent, rgba(0,0,0,.62)); color: #FFFFFF; font-size: 10px; line-height: 1.25; font-weight: 500">{{p.cap}}<br><span style="opacity: .75">{{p.sk}}</span></span>
        <button type="button" onClick="{{p.rm}}" aria-label="Șterge poza" style="position: absolute; right: 5px; top: 5px; width: 24px; height: 24px; border: 0; border-radius: 12px; background: rgba(0,0,0,.45); color: #FFFFFF; font-size: 13px; cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 0">✕</button>
      </div>
    </sc-for>
  </div>
  <span style="font-size: 12px; line-height: 1.4; color: var(--ink2); padding: 0 6px">Leagă fiecare poză de o competență: clienții care caută „montaj mobilier” văd întâi pozele de montaj. Fără fețe de clienți și fără adrese în poze.</span>

  <div style="display: flex; align-items: baseline; justify-content: space-between; padding: 10px 6px 0"><span class="lbl" style="padding: 0">Despre tine</span><span style="font-size: 12px; color: var(--ink2)">{{bioN}}</span></div>
  <div style="background: var(--surf); border-radius: 22px; padding: 12px 14px; display: flex; flex-direction: column; gap: 8px">
    <sc-if value="{{bioView}}" hint-placeholder-val="{{ true }}"><span style="font-size: 15px; line-height: 1.45">{{bio}}</span><button type="button" onClick="{{editBio}}" style="align-self: flex-start; border: 0; background: transparent; padding: 0; color: var(--btext); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Editează</button></sc-if>
    <sc-if value="{{bioEdit}}" hint-placeholder-val="{{ false }}"><label><span style="position: absolute; left: -9999px">Despre tine</span><textarea class="fld2" value="{{bio}}" onChange="{{onBio}}" style="height: 96px; resize: none; line-height: 1.4"></textarea></label><button type="button" onClick="{{doneBio}}" style="align-self: flex-end; height: 34px; padding: 0 14px; border: 0; border-radius: 17px; background: var(--invbg); color: var(--invink); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Gata</button></sc-if>
  </div>

  <sc-if value="{{tBio}}" hint-placeholder-val="{{ false }}"><div class="in" style="padding: 11px 14px; border-radius: 16px; background: var(--invbg); color: var(--invink); font-size: 14px; line-height: 1.35">✓ {{toast}}</div></sc-if>
  <span class="lbl" style="padding: 10px 6px 0">Disponibilitate</span>
  <div style="background: var(--surf); border-radius: 22px; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px">
    <div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 4px"><sc-for list="{{days}}" as="d" hint-placeholder-count="7"><button type="button" class="dchip" onClick="{{d.pick}}" aria-pressed="{{d.attr}}" style="width: 100%">{{d.t}}</button></sc-for></div>
    <span style="font-size: 14px">Cât de departe mergi</span>
    <div class="sg" style="grid-template-columns: repeat(4, minmax(0, 1fr))"><sc-for list="{{radii}}" as="r" hint-placeholder-count="4"><button type="button" onClick="{{r.pick}}" aria-pressed="{{r.attr}}">{{r.t}}</button></sc-for></div>
    <a href="Disponibilitate.dc.html" style="font-size: 14px; font-weight: 500; color: var(--btext); text-decoration: none">Program detaliat pe ore ›</a>
  </div>

  <span class="lbl" style="padding: 10px 6px 0">Verificări și acte</span>
  <div class="grp">
    <div class="rw"><img src="assets/ui/profile.png" alt="" style="width: 24px; height: 24px"><span style="flex-grow: 1; font-size: 15px">Identitate</span><span class="tag t-ok">✓ Verificată</span></div>
    <div class="rw"><img src="assets/ui/briefcase.png" alt="" style="width: 24px; height: 24px"><span style="flex-grow: 1; font-size: 15px">PFA · CUI RO41234567</span><span class="tag t-ok">✓ Verificat</span></div>
    <div class="rw"><img src="assets/ui/shield.png" alt="" style="width: 24px; height: 24px"><span style="flex-grow: 1; font-size: 15px">Cazier</span><span class="tag t-wait">În analiză</span></div>
    <a href="#asigurare" class="rw pr"><img src="assets/ui/check.png" alt="" style="width: 24px; height: 24px"><span style="flex-grow: 1; font-size: 15px">Asigurare de răspundere</span><span style="font-size: 14px; color: var(--btext)">Adaugă</span>''' + CHEV + '''</a>
    <a href="GearEchipament.dc.html" class="rw pr"><img src="assets/ui/work_tools.png" alt="" style="width: 24px; height: 24px"><span style="flex-grow: 1; font-size: 15px">Echipamentul meu</span><span style="font-size: 14px; color: var(--ink2)">7 declarate</span>''' + CHEV + '''</a>
  </div>
</div>
<div class="glass" style="position: absolute; left: 0; right: 0; bottom: 0; padding: 12px 16px 30px; box-shadow: 0 -8px 24px var(--shadow); display: flex; flex-direction: column; gap: 8px"><sc-if value="{{tEnd}}" hint-placeholder-val="{{ false }}"><div class="in" style="padding: 11px 14px; border-radius: 16px; background: var(--invbg); color: var(--invink); font-size: 14px; line-height: 1.35">✓ {{toast}}</div></sc-if><button type="button" onClick="{{saveAll}}" class="pr" style="width: 100%; height: 54px; border: 0; border-radius: 27px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 17px; font-weight: 500; cursor: pointer; box-shadow: 0 10px 24px rgba(255,159,10,0.3)">Salvează</button></div>'''
    return page('Profilul meu (Jobzer)', 'L', b, SK_CSS, logic, h=2200)


SKILL_PAGES = [('Skilluri', skilluri), ('ProfilEdit', profil_edit)]
