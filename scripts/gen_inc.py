

# ================================================================ ÎNCASĂRI v2: încasări + Analiză (strategie: servicii, ore, promovări, preț, răspuns)
INC_SVC = [  # 30 de zile: venit, lucrări, ore lucrate, oferte trimise, câștigate, ofertă medie, mediana zonei
    dict(i='mobila', n='Montaj mobilier', rev=1840, jobs=12, hrs=23.5, sent=19, won=12, avg=152, zone=160),
    dict(i='reparatii', n='Reparații mici', rev=920, jobs=9, hrs=10.0, sent=13, won=9, avg=85, zone=90),
    dict(i='it', n='Montaj TV și rafturi', rev=630, jobs=6, hrs=6.5, sent=15, won=6, avg=118, zone=110),
    dict(i='tamplarie', n='Tâmplărie și uși', rev=410, jobs=2, hrs=5.0, sent=7, won=2, avg=210, zone=180),
]
# cereri în zonă pe intervale (rânduri = intervale orare, coloane = L..D), câștigul tău și cât ai fost online (0..1)
INC_SLOTS = ['07–10', '10–13', '13–16', '16–19', '19–22']
INC_DEM = [[3, 4, 3, 4, 3, 9, 6], [5, 5, 6, 5, 6, 16, 12], [4, 3, 4, 4, 5, 11, 8], [9, 10, 11, 14, 12, 8, 5], [6, 7, 7, 8, 5, 3, 2]]
INC_ON = [[.2, .2, .2, .2, .2, 0, 0], [.6, .5, .6, .5, .6, 0, 0], [.7, .6, .7, .6, .7, .1, 0], [.9, .8, .9, .4, .9, .3, 0], [.5, .4, .5, .2, .4, 0, 0]]
INC_ERN = [[0, 0, 0, 0, 0, 0, 0], [150, 0, 160, 90, 120, 0, 0], [80, 120, 0, 150, 90, 0, 0], [320, 240, 300, 150, 480, 120, 0], [90, 160, 80, 0, 90, 0, 0]]
INC_PROMO = [dict(d='13 oct.', t='Promovare 1 zi', cost=19, views=140, offers=5, won=2, rev=270),
             dict(d='4 oct.', t='Promovare weekend', cost=39, views=260, offers=7, won=2, rev=310),
             dict(d='28 sep.', t='Promovare 1 zi', cost=19, views=95, offers=2, won=0, rev=0)]


def incasari_v2(theme):
    dark = theme == 'D'
    S = lambda n: n.replace('.dc.html', 'Dark.dc.html') if dark else n
    logic = ("""constructor(props) { super(props); this.state = { tab: 'an', p: 30, sort: 'rev', hm: 'dem', cell: [5, 1], pf: 0 }; }
  renderVals() {
    const s = this.state, K = { 7: 0.26, 30: 1, 90: 2.85 }[s.p], prevK = { 7: 0.9, 30: 0.88, 90: 0.93 }[s.p];
    const SV = """ + json.dumps(INC_SVC, ensure_ascii=False) + """, SL = """ + json.dumps(INC_SLOTS, ensure_ascii=False) + """;
    const DEM = """ + json.dumps(INC_DEM) + """, ON = """ + json.dumps(INC_ON) + """, ERN = """ + json.dumps(INC_ERN) + """, PR = """ + json.dumps(INC_PROMO, ensure_ascii=False) + """;
    const D = ['L', 'Ma', 'Mi', 'J', 'V', 'S', 'D'], DL = ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică'];
    const lei = (v) => Math.round(v).toLocaleString('ro-RO') + ' lei';
    const rnd = (v) => Math.max(0, Math.round(v));
    const sv = SV.map((x) => ({ i: x.i, n: x.n, rev: x.rev * K, jobs: rnd(x.jobs * K) || 1, hrs: x.hrs * K, sent: rnd(x.sent * K) || 1, won: rnd(x.won * K) || 1, avg: x.avg, zone: x.zone }));
    const tot = sv.reduce((a, x) => a + x.rev, 0), jobs = sv.reduce((a, x) => a + x.jobs, 0), hrs = sv.reduce((a, x) => a + x.hrs, 0);
    const sent = sv.reduce((a, x) => a + x.sent, 0), won = sv.reduce((a, x) => a + x.won, 0);
    const kpi = (t, v, d, up) => ({ t: t, v: v, d: (up ? '↑ ' : '↓ ') + d, dSt: 'font-size: 12px; font-weight: 600; color: ' + (up ? 'var(--oktext)' : '#D70015') });
    const kpis = [kpi('Câștig net', lei(tot), Math.round((1 / prevK - 1) * 100) + '%', true), kpi('Lucrări', String(jobs), '2', true),
      kpi('Câștig pe oră', lei(tot / hrs), '4 lei', true), kpi('Oferte câștigate', Math.round(won / sent * 100) + '%', '3 p.p.', false)];
    // servicii
    const key = { rev: (x) => x.rev, ph: (x) => x.rev / x.hrs, win: (x) => x.won / x.sent }[s.sort];
    const ord = sv.slice().sort((a, b) => key(b) - key(a)), mx = key(ord[0]);
    const svc = ord.map((x) => ({ n: x.n, src: 'assets/cat/' + x.i + '.svg', main: s.sort === 'rev' ? lei(x.rev) : s.sort === 'ph' ? lei(x.rev / x.hrs) + '/h' : Math.round(x.won / x.sent * 100) + '%',
      sub: x.jobs + (x.jobs === 1 ? ' lucrare' : ' lucrări') + ' · ' + Math.round(x.rev / x.hrs) + ' lei/h · câștigi ' + Math.round(x.won / x.sent * 100) + '% din oferte',
      bar: 'height: 6px; border-radius: 3px; background: var(--brand); transition: width .5s; width: ' + Math.max(6, Math.round(key(x) / mx * 100)) + '%' }));
    const byH = sv.slice().sort((a, b) => b.rev / b.hrs - a.rev / a.hrs);
    const svcTip = byH[0].n + ' îți aduce cel mai mult pe oră (' + Math.round(byH[0].rev / byH[0].hrs) + ' lei/h), deși ' + ord[0].n.toLowerCase() + (s.sort === 'rev' ? ' aduce cei mai mulți bani în total.' : ' e pe primul loc la ce ai ales.');
    const so = (k, t) => ({ t: t, attr: s.sort === k ? 'true' : 'false', pick: () => this.setState({ sort: k }) });
    // harta orelor
    const M = s.hm === 'dem' ? DEM : s.hm === 'ern' ? ERN : ON, mmax = Math.max.apply(null, M.map((r) => Math.max.apply(null, r))) || 1;
    const rows = SL.map((sl, ri) => ({ sl: sl, cells: D.map((d, ci) => { const v = M[ri][ci], a = v / mmax, sel = s.cell[0] === ci && s.cell[1] === ri;
      const gap = DEM[ri][ci] >= 8 && ON[ri][ci] < 0.3;
      return { st: 'height: 30px; border: 0; border-radius: 8px; cursor: pointer; padding: 0; position: relative; transition: transform .2s; background: ' + (v ? 'rgba(255,159,10,' + (0.12 + a * 0.88).toFixed(2) + ')' : 'var(--surf2)') + (sel ? '; box-shadow: 0 0 0 2.5px var(--invbg); transform: scale(1.06)' : ''),
        dot: gap && s.hm === 'dem', pick: () => this.setState({ cell: [ci, ri] }), lab: DL[ci] + ' ' + sl }; }) }));
    const c = s.cell, cd = DEM[c[1]][c[0]], co = ON[c[1]][c[0]], ce = ERN[c[1]][c[0]];
    const cellTxt = DL[c[0]] + ', ' + SL[c[1]] + ': ' + rnd(cd * K) + ' cereri în zona ta · ai fost online ' + Math.round(co * 100) + '% din timp · ai câștigat ' + lei(ce * K);
    const cellGap = cd >= 8 && co < 0.3;
    const hmo = (k, t) => ({ t: t, attr: s.hm === k ? 'true' : 'false', pick: () => this.setState({ hm: k }) });
    // promovări
    const pr = PR.map((x) => ({ d: x.d, t: x.t, cost: lei(x.cost), v: x.views + ' vizualizări în plus', o: x.offers + ' cereri primite, ' + x.won + ' câștigate', rev: x.rev ? lei(x.rev) : '0 lei',
      roi: x.rev ? 'x' + (x.rev / x.cost).toFixed(1).replace('.', ',') : 'fără câștig', roiSt: 'height: 24px; padding: 0 9px; border-radius: 12px; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; ' + (x.rev / x.cost >= 3 ? 'background: var(--oksoft); color: var(--oktext)' : x.rev ? 'background: var(--bsoft); color: var(--btext)' : 'background: var(--surf2); color: var(--ink2)') }));
    const pc = PR.reduce((a, x) => a + x.cost, 0), prv = PR.reduce((a, x) => a + x.rev, 0);
    // preț vs zonă (Montaj mobilier): rată de câștig pe benzi de preț
    const bands = [['sub 130', 74], ['130–150', 66], ['150–170', 58], ['170–190', 31], ['peste 190', 12]];
    const bandBars = bands.map((b, i) => ({ t: b[0], v: b[1] + '%', st: 'width: 100%; border-radius: 8px 8px 4px 4px; height: ' + Math.round(b[1] * 1.1) + 'px; background: ' + (i === 2 ? 'var(--brand)' : 'var(--bsoft2)') }));
    const resp = [['sub 2 min', 61], ['2–10 min', 38], ['peste 10 min', 12]].map((r) => ({ t: r[0], v: r[1] + '%', bar: 'height: 8px; border-radius: 4px; background: var(--brand); width: ' + r[1] + '%' }));
    const per = (k, t) => ({ t: t, attr: s.p === k ? 'true' : 'false', pick: () => this.setState({ p: k }) });
    return { isIn: s.tab === 'in', isAn: s.tab === 'an', tI: s.tab === 'in' ? 'true' : 'false', tA: s.tab === 'an' ? 'true' : 'false', goI: () => this.setState({ tab: 'in' }), goA: () => this.setState({ tab: 'an' }),
      pers: [per(7, '7 zile'), per(30, '30 de zile'), per(90, '3 luni')], kpis: kpis, sorts: [so('rev', 'Venit'), so('ph', 'Lei pe oră'), so('win', 'Rată de câștig')], svc: svc, svcTip: svcTip,
      hms: [hmo('dem', 'Cereri în zonă'), hmo('on', 'Când ești online'), hmo('ern', 'Câștigul tău')], days: D.map((d) => ({ d: d })), rows: rows, cellTxt: cellTxt, cellGap: cellGap,
      promos: pr, promoSum: 'Ai plătit ' + lei(pc) + ' pe promovări și ai câștigat ' + lei(prv) + ' din cererile venite în timpul lor (x' + (prv / pc).toFixed(1).replace('.', ',') + ').',
      bands: bandBars, resp: resp };
  }""")
    sec = lambda t, sub='': ('<div style="display: flex; flex-direction: column; gap: 2px; padding: 12px 4px 0"><span style="font-size: 19px; font-weight: 600; letter-spacing: -0.3px">' + t + '</span>' + ('<span style="font-size: 12px; color: var(--ink2)">' + sub + '</span>' if sub else '') + '</div>')
    tip = lambda body, cta='', href='': ('<div style="display: flex; gap: 10px; align-items: flex-start; padding: 12px; border-radius: 18px; background: var(--bsoft)"><img src="assets/ui/sparkles.png" alt="" style="width: 22px; height: 22px; flex-shrink: 0">'
                                        '<span style="flex-grow: 1; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; line-height: 1.4">' + body + '</span>' + ('<a href="' + href + '" style="font-size: 13px; font-weight: 600; color: var(--btext); text-decoration: none">' + cta + ' ›</a>' if cta else '') + '</span></div>')
    card = 'background: var(--surf); border-radius: 24px; padding: 14px; display: flex; flex-direction: column; gap: 12px'
    inc_tab = '''<div class="in" style="display: flex; flex-direction: column; gap: 12px">
      <div style="background: var(--invbg); color: var(--invink); border-radius: 28px; padding: 18px; display: flex; flex-direction: column; gap: 6px">
        <span style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 500; opacity: .7"><span>SĂPTĂMÂNA ASTA</span><span>13–19 oct.</span></span>
        <span style="font-size: 40px; font-weight: 600; letter-spacing: -1.2px; color: var(--brand)">460,00 lei</span>
        <span style="font-size: 13px; opacity: .75">Primești 100% din prețurile tale. Taxa Jobzee o plătește clientul.</span>
      </div>
      <div style="display: flex; gap: 8px"><a href="#transfer" class="pr" style="flex: 1; height: 50px; border-radius: 25px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 500; text-decoration: none">Transfer acum</a><a href="''' + S('Facturi.dc.html') + '''" class="pr" style="flex: 1; height: 50px; border-radius: 25px; background: var(--surf); color: var(--ink); display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 500; text-decoration: none">Facturi PFA</a></div>
      <div class="grp">
        <div class="rw"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Montaj mobilier</span><span style="font-size: 12px; color: var(--ink2)">Vineri · Andrei</span></span><span style="font-size: 15px; font-weight: 600; color: var(--oktext)">+150,00</span></div>
        <div class="rw"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Bacșiș</span><span style="font-size: 12px; color: var(--ink2)">Vineri · Andrei</span></span><span style="font-size: 15px; font-weight: 600; color: var(--oktext)">+60,00</span></div>
        <div class="rw"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Reparații mici · 2 h</span><span style="font-size: 12px; color: var(--ink2)">Miercuri · Radu</span></span><span style="font-size: 15px; font-weight: 600; color: var(--oktext)">+160,00</span></div>
        <div class="rw"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Montaj TV</span><span style="font-size: 12px; color: var(--ink2)">Luni · Elena</span></span><span style="font-size: 15px; font-weight: 600; color: var(--oktext)">+90,00</span></div>
        <div class="rw"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Promovare 1 zi</span><span style="font-size: 12px; color: var(--ink2)">Plătită separat, cu cardul</span></span><span style="font-size: 15px; color: var(--ink2)">−19,00</span></div>
      </div>
    </div>'''
    an_tab = '''<div class="in" style="display: flex; flex-direction: column; gap: 10px">
      <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><sc-for list="{{pers}}" as="p" hint-placeholder-count="3"><button type="button" onClick="{{p.pick}}" aria-pressed="{{p.attr}}">{{p.t}}</button></sc-for></div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px"><sc-for list="{{kpis}}" as="k" hint-placeholder-count="4"><div style="background: var(--surf); border-radius: 20px; padding: 12px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: var(--ink2)">{{k.t}}</span><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.4px; font-variant-numeric: tabular-nums">{{k.v}}</span><span style="{{k.dSt}}">{{k.d}} față de perioada anterioară</span></div></sc-for></div>

      ''' + sec('Ce servicii merg cel mai bine', 'Din lucrările tale finalizate în Jobzee') + '''
      <div style="''' + card + '''">
        <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><sc-for list="{{sorts}}" as="o" hint-placeholder-count="3"><button type="button" onClick="{{o.pick}}" aria-pressed="{{o.attr}}">{{o.t}}</button></sc-for></div>
        <sc-for list="{{svc}}" as="x" hint-placeholder-count="4"><div style="display: flex; gap: 10px; align-items: center"><img src="{{x.src}}" alt="" style="width: 40px; height: 40px; border-radius: 12px; flex-shrink: 0">
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 14px; font-weight: 600">{{x.n}}</span><span style="font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; white-space: nowrap">{{x.main}}</span></span>
            <span style="height: 6px; border-radius: 3px; background: var(--surf2)"><span style="{{x.bar}}; display: block"></span></span><span style="font-size: 11px; color: var(--ink2)">{{x.sub}}</span></span></div></sc-for>
        ''' + tip('{{svcTip}} Pune preț și poze bune la serviciul care îți aduce cel mai mult pe oră.', 'Ajustează competențele', S('ProfilEdit.dc.html')) + '''
      </div>

      ''' + sec('Când apar cererile', 'Atinge o căsuță ca să vezi detaliile') + '''
      <div style="''' + card + '''">
        <div class="sg" style="grid-template-columns: repeat(3, minmax(0, 1fr))"><sc-for list="{{hms}}" as="h" hint-placeholder-count="3"><button type="button" onClick="{{h.pick}}" aria-pressed="{{h.attr}}" style="font-size: 12px">{{h.t}}</button></sc-for></div>
        <div style="display: grid; grid-template-columns: 44px repeat(7, minmax(0, 1fr)); gap: 4px; align-items: center">
          <span></span><sc-for list="{{days}}" as="d" hint-placeholder-count="7"><span style="font-size: 11px; font-weight: 500; color: var(--ink2); text-align: center">{{d.d}}</span></sc-for>
        </div>
        <sc-for list="{{rows}}" as="r" hint-placeholder-count="5"><div style="display: grid; grid-template-columns: 44px repeat(7, minmax(0, 1fr)); gap: 4px; align-items: center; margin-top: -8px">
          <span style="font-size: 11px; color: var(--ink2); font-variant-numeric: tabular-nums">{{r.sl}}</span>
          <sc-for list="{{r.cells}}" as="c" hint-placeholder-count="7"><button type="button" onClick="{{c.pick}}" aria-label="{{c.lab}}" style="{{c.st}}"><sc-if value="{{c.dot}}" hint-placeholder-val="{{ false }}"><span style="position: absolute; right: 4px; top: 4px; width: 7px; height: 7px; border-radius: 4px; background: var(--invbg)"></span></sc-if></button></sc-for>
        </div></sc-for>
        <span style="font-size: 13px; line-height: 1.4; padding: 10px 12px; border-radius: 14px; background: var(--surf2)">{{cellTxt}}</span>
        <span style="display: flex; align-items: center; gap: 6px; font-size: 11px; color: var(--ink2)"><span style="width: 7px; height: 7px; border-radius: 4px; background: var(--invbg)"></span>Multe cereri și tu offline: aici pierzi cele mai multe lucrări.</span>
        ''' + tip('Sâmbătă între 10 și 13 apar cele mai multe cereri din zona ta, iar tu nu ești online. Dacă pornești programul sâmbăta dimineața, ai acces la cererile din vârful săptămânii.', 'Adaugă sâmbăta în program', S('Disponibilitate.dc.html')) + '''
      </div>

      ''' + sec('Promovările tale', 'Câștigul socotit doar din cererile venite cât a fost activă promovarea') + '''
      <div style="''' + card + '''">
        <sc-for list="{{promos}}" as="x" hint-placeholder-count="3"><div style="display: flex; gap: 10px; align-items: center; padding-bottom: 10px; box-shadow: inset 0 -0.5px 0 var(--sep)">
          <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 600">{{x.t}} · {{x.d}}</span><span style="font-size: 12px; color: var(--ink2)">{{x.v}} · {{x.o}}</span><span style="font-size: 12px; color: var(--ink2)">Cost {{x.cost}} · câștig {{x.rev}}</span></span>
          <span style="{{x.roiSt}}">{{x.roi}}</span></div></sc-for>
        <span style="font-size: 13px; line-height: 1.4">{{promoSum}}</span>
        ''' + tip('Promovarea de weekend ți-a adus cele mai multe cereri. Cea din 28 sep. (o zi lucrătoare, la prânz) nu a adus nicio lucrare: promovează în intervalele cu multe cereri.', 'Programează o promovare', S('Promovare.dc.html')) + '''
      </div>

      ''' + sec('Prețul tău față de zonă', 'Montaj mobilier · câte oferte câștigi, după preț') + '''
      <div style="''' + card + '''">
        <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px; align-items: end; height: 120px"><sc-for list="{{bands}}" as="b" hint-placeholder-count="5"><span style="display: flex; flex-direction: column; align-items: center; gap: 4px; justify-content: flex-end; height: 100%"><span style="font-size: 12px; font-weight: 600">{{b.v}}</span><span style="{{b.st}}"></span></span></sc-for></div>
        <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px; margin-top: -6px"><sc-for list="{{bands}}" as="b" hint-placeholder-count="5"><span style="font-size: 10px; color: var(--ink2); text-align: center">{{b.t}}</span></sc-for></div>
        <span style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: var(--ink2)">Oferta ta medie</span><span style="font-weight: 600">152 lei</span></span>
        <span style="display: flex; justify-content: space-between; font-size: 13px; margin-top: -6px"><span style="color: var(--ink2)">Mediana în zona ta</span><span style="font-weight: 600">160 lei</span></span>
        ''' + tip('Între 150 și 170 lei câștigi mai mult de jumătate din oferte. Peste 170 lei șansele scad la o treime: urcă prețul doar la lucrările mari sau urgente.') + '''
      </div>

      ''' + sec('Cât de repede răspunzi', 'Oferte câștigate, după timpul de răspuns') + '''
      <div style="''' + card + '''">
        <sc-for list="{{resp}}" as="r" hint-placeholder-count="3"><div style="display: flex; flex-direction: column; gap: 4px"><span style="display: flex; justify-content: space-between; font-size: 13px"><span>{{r.t}}</span><span style="font-weight: 600">{{r.v}}</span></span><span style="height: 8px; border-radius: 4px; background: var(--surf2)"><span style="{{r.bar}}; display: block"></span></span></div></sc-for>
        <span style="font-size: 13px; color: var(--ink2)">Tu răspunzi de obicei în 3 min. Oferta rapidă din Acasă te ajută să ajungi sub 2 min.</span>
      </div>
      <span style="font-size: 11px; line-height: 1.4; color: var(--ink2); padding: 0 6px">Cifrele vin din activitatea ta în Jobzee. Cererile din zonă sunt numărate anonim. Nimic din această pagină nu schimbă felul în care ești ales de clienți.</span>
    </div>'''
    b = '''<div class="scroll colfix" style="position: absolute; inset: 0; overflow-y: auto; padding: 56px 16px 110px; display: flex; flex-direction: column; gap: 12px">
  <div style="display: flex; align-items: center; justify-content: space-between"><h1 style="margin: 0 4px; font-size: 34px; font-weight: 600; letter-spacing: -0.9px">Încasări</h1><img src="assets/mascot/zee-bani.png" alt="" style="width: 54px; height: 58px"></div>
  <div class="sg" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><button type="button" onClick="{{goI}}" aria-pressed="{{tI}}">Încasări</button><button type="button" onClick="{{goA}}" aria-pressed="{{tA}}">Analiză și strategie</button></div>
  <sc-if value="{{isIn}}" hint-placeholder-val="{{ false }}">''' + inc_tab + '''</sc-if>
  <sc-if value="{{isAn}}" hint-placeholder-val="{{ true }}">''' + an_tab + '''</sc-if>
</div>
''' + tabbar('jobzer', 'incasari', {'acasa': S('Castig.dc.html'), 'sarcini': S('SarciniJobzer.dc.html'), 'incasari': S('Incasari.dc.html'), 'cont': S('ContJobzer.dc.html')})
    css = SEG_CSS + '.colfix>*{flex-shrink:0}.scroll{scrollbar-width:none}.scroll::-webkit-scrollbar{display:none}@keyframes inUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}.in{animation:inUp .3s cubic-bezier(.2,.8,.2,1) both}'
    return page('Încasări și analiză', theme, b, css, logic)
