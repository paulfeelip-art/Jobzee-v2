

# ---------------------------------------------------------------- Radar live (după trimiterea cererii)
def radar(theme):
    dark = theme == 'D'
    css = """
@keyframes sweep{to{transform:rotate(360deg)}}
@keyframes ringp{0%{transform:scale(.2);opacity:.5}100%{transform:scale(1);opacity:0}}
@keyframes dots{0%,80%,100%{opacity:.25}40%{opacity:1}}
.sweep{position:absolute;border-radius:50%;background:conic-gradient(from 0deg, rgba(255,159,10,0.0) 0deg, rgba(255,159,10,0.0) 280deg, rgba(255,159,10,0.38) 360deg);animation:sweep 3.2s linear infinite}
.ring{position:absolute;border-radius:50%;border:1.5px dashed var(--ink3)}
.ringp{position:absolute;border-radius:50%;background:var(--brand);animation:ringp 3.2s ease-out infinite}
.pinj{position:absolute;transition:left .6s cubic-bezier(.2,.9,.3,1.2), top .6s cubic-bezier(.2,.9,.3,1.2)}
.srt{border:0;height:34px;padding:0 12px;border-radius:17px;font-family:inherit;font-size:13px;font-weight:500;color:var(--ink);cursor:pointer;transition:all .25s}
.srt[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}
.srt[aria-pressed="false"]{background:var(--glass);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
.typing span{display:inline-block;width:5px;height:5px;border-radius:3px;background:var(--ink2);margin-right:2px;animation:dots 1.2s infinite}
.typing span:nth-child(2){animation-delay:.15s}.typing span:nth-child(3){animation-delay:.3s}
.row{display:flex;align-items:center;gap:10px;padding:9px 4px;transition:transform .5s cubic-bezier(.2,.9,.3,1.2)}
"""
    J = [
        dict(n='Mihai I.', img='people/person-jobzer-3', tier='Gold', eta=6, m=98, sk='Montaj mobilier · IKEA', a=-40, show=1, offer=150, at=5),
        dict(n='Ana D.', img='people/person-jobzer-2', tier='Plus', eta=14, m=84, sk='Montaj · curățenie', a=200, show=2, offer=120, at=7),
        dict(n='Radu C.', img='people/person-jobzer-1', tier='Gold', eta=4, m=95, sk='Montaj · electrice', a=110, show=3, offer=170, at=9),
        dict(n='Elena P.', img='people/person-client-1', tier='Start', eta=11, m=80, sk='Montaj mobilier', a=300, show=4, offer=135, at=12),
        dict(n='Andrei M.', img='people/person-client-3', tier='Plus', eta=18, m=76, sk='Tâmplărie · montaj', a=20, show=6, offer=0, at=99),
    ]
    logic = ("""constructor(props) { super(props); this.state = { t: 0, sort: 'eta' }; }
  componentDidMount() { this.i = setInterval(() => this.setState({ t: this.state.t >= 18 ? 0 : this.state.t + 1 }), 900); }
  componentWillUnmount() { clearInterval(this.i); }
  renderVals() {
    const J = """ + json.dumps(J, ensure_ascii=False) + """;
    const t = this.state.t, sort = this.state.sort, cx = 195, cy = 300;
    const vis = J.filter(j => t >= j.show);
    const offered = j => j.offer && t >= j.at;
    const pins = vis.map(j => {
      const r = 34 + j.eta * 8.5, a = j.a * Math.PI / 180, x = cx + r * Math.cos(a) - 24, y = cy + r * Math.sin(a) - 24;
      const off = offered(j);
      return {
        img: 'assets/' + j.img + '.webp', eta: j.eta + ' min',
        pos: 'left: ' + Math.round(x) + 'px; top: ' + Math.round(y) + 'px',
        ring: 'width: 48px; height: 48px; border-radius: 24px; object-fit: cover; display: block; box-sizing: border-box; border: 3px solid ' + (off ? '#FF9F0A' : 'var(--surf)') + '; box-shadow: 0 8px 20px var(--shadow)',
        price: off ? j.offer + ' lei' : '', priceStyle: off ? 'display: flex' : 'display: none'
      };
    });
    const key = { eta: j => j.eta, skill: j => -j.m, pret: j => offered(j) ? j.offer : 9999 }[sort];
    const rows = vis.slice().sort((a, b) => key(a) - key(b)).slice(0, 3).map((j, i) => ({
      img: 'assets/' + j.img + '.webp', n: j.n, tier: j.tier, sk: j.sk, eta: j.eta + ' min', m: j.m + '%',
      price: offered(j) ? j.offer + ' lei' : '', isOff: offered(j), notOff: !offered(j),
      sep: i > 0 ? 'border-top: 0.5px solid var(--sep)' : ''
    }));
    const offers = J.filter(offered).length;
    const s = (k) => ({ attr: sort === k ? 'true' : 'false', pick: () => this.setState({ sort: k }) });
    const mm = Math.floor((t * 9) / 60), ss = (t * 9) % 60;
    return {
      pins, rows, found: vis.length, offers, hasOffers: offers > 0, noOffers: offers === 0,
      sEta: s('eta'), sSkill: s('skill'), sPret: s('pret'),
      zee: offers >= 3 ? 'assets/mascot/zee-fericit.svg' : 'assets/mascot/zee-cauta.svg',
      status: offers === 0 ? 'Jobzerii văd cererea și pregătesc oferte' : (offers === 1 ? 'Prima ofertă a sosit' : offers + ' oferte primite până acum'),
      elapsed: mm + ':' + (ss < 10 ? '0' + ss : ss),
      cta: 'Vezi ofertele (' + offers + ')',
      bar: 'display: block; height: 100%; border-radius: 3px; background: var(--brand); transition: width .6s; width: ' + Math.min(100, offers * 25) + '%'
    };
  }""")
    nxt = 'OferteDark.dc.html' if dark else 'Oferte.dc.html'
    rings = ''.join('<span class="ring" style="left: %dpx; top: %dpx; width: %dpx; height: %dpx"></span><span style="position: absolute; left: %dpx; top: %dpx; font-size: 10px; font-weight: 600; color: var(--ink2); background: var(--land); padding: 0 4px; border-radius: 6px">%d min</span>'
                    % (195 - r, 300 - r, 2 * r, 2 * r, 195 - 14, 300 - r - 7, m) for m, r in ((5, 77), (10, 119), (15, 162)))
    b = (map_svg(844).replace('height="844" viewBox="0 0 390 844"', 'height="844" viewBox="0 0 390 844"') + '''
  <div style="position: absolute; inset: 0; background: radial-gradient(circle at 195px 300px, transparent 0, transparent 160px, var(--land) 330px); opacity: .55"></div>
  ''' + rings + '''
  <span class="sweep" style="left: 33px; top: 138px; width: 324px; height: 324px"></span>
  <span class="ringp" style="left: 165px; top: 270px; width: 60px; height: 60px"></span>
  <span style="position: absolute; left: 179px; top: 284px; width: 32px; height: 32px; border-radius: 16px; background: var(--surf); box-shadow: 0 6px 16px var(--shadow); display: flex; align-items: center; justify-content: center">''' + mark(22) + '''</span>
  <sc-for list="{{pins}}" as="p" hint-placeholder-count="5">
    <span class="pinj pop" style="{{p.pos}}">
      <img src="{{p.img}}" alt="" style="{{p.ring}}">
      <span style="position: absolute; left: 50%; bottom: -10px; transform: translateX(-50%); height: 18px; padding: 0 6px; border-radius: 9px; background: var(--invbg); color: var(--invink); font-size: 10px; font-weight: 600; white-space: nowrap; display: flex; align-items: center">{{p.eta}}</span>
      <span class="pop" style="{{p.priceStyle}}; position: absolute; left: 36px; top: -12px; height: 22px; padding: 0 8px; border-radius: 11px; background: var(--brand); color: var(--onbrand); font-size: 12px; font-weight: 600; white-space: nowrap; align-items: center; box-shadow: 0 4px 12px rgba(255,159,10,0.4)">{{p.price}}</span>
    </span>
  </sc-for>

  <div style="position: absolute; left: 16px; right: 16px; top: 54px; display: flex; flex-direction: column; gap: 10px">
    <div class="glass u" style="display: flex; align-items: center; gap: 10px; padding: 6px 14px 6px 6px; border-radius: 26px; box-shadow: 0 8px 24px var(--shadow)">
      <a href="Fisa.dc.html" aria-label="Înapoi la fișă" class="pr" style="width: 40px; height: 40px; border-radius: 20px; background: var(--surf2); color: var(--ink); display: flex; align-items: center; justify-content: center">''' + BACK + '''</a>
      <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="display: flex; align-items: center; gap: 6px; font-size: 16px; font-weight: 600"><span class="glow" style="width: 8px; height: 8px; border-radius: 4px; background: #FF3B30"></span>Radar live</span><span style="font-size: 12px; color: var(--ink2)">Montaj mobilier · Urgent · rază 5 km</span></span>
      <span style="font-size: 15px; font-weight: 500; color: var(--ink2); font-variant-numeric: tabular-nums">{{elapsed}}</span>
    </div>
    <div class="u d1" style="display: flex; gap: 6px">
      <button type="button" class="srt" onClick="{{sEta.pick}}" aria-pressed="{{sEta.attr}}">⏱ Cel mai rapid</button>
      <button type="button" class="srt" onClick="{{sSkill.pick}}" aria-pressed="{{sSkill.attr}}">✓ Potrivire skill</button>
      <button type="button" class="srt" onClick="{{sPret.pick}}" aria-pressed="{{sPret.attr}}">Preț ofertă</button>
    </div>
  </div>

  <div class="sheet" style="position: absolute; left: 8px; right: 8px; bottom: 8px; background: var(--glass2); backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px); border-radius: 38px; padding: 10px 14px 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 -10px 40px var(--shadow)">
    <span style="align-self: center; width: 38px; height: 5px; border-radius: 3px; background: var(--ink3)"></span>
    <div style="display: flex; align-items: center; gap: 10px; padding: 0 4px">
      <img src="{{zee}}" alt="" class="float" style="width: 40px; height: 43px; flex-shrink: 0">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 18px; font-weight: 600; letter-spacing: -0.3px">{{found}} Jobzeri găsiți · {{offers}} oferte</span><span style="font-size: 13px; color: var(--ink2)">{{status}}</span></span>
    </div>
    <span style="height: 5px; border-radius: 3px; background: var(--surf3); overflow: hidden; margin: 0 4px"><span style="{{bar}}"></span></span>
    <div style="display: flex; flex-direction: column">
      <sc-for list="{{rows}}" as="r" hint-placeholder-count="3">
        <div class="row" style="{{r.sep}}">
          <img src="{{r.img}}" alt="" style="width: 44px; height: 44px; border-radius: 22px; object-fit: cover; flex-shrink: 0">
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px">
            <span style="display: flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 600">{{r.n}}<span style="height: 18px; padding: 0 6px; border-radius: 9px; background: var(--bsoft); color: var(--btext); font-size: 10px; font-weight: 600; display: inline-flex; align-items: center">{{r.tier}}</span></span>
            <span style="font-size: 12px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{r.eta}} · {{r.m}} potrivire · {{r.sk}}</span>
          </span>
          <sc-if value="{{r.isOff}}" hint-placeholder-val="{{ true }}"><span class="pop" style="font-size: 16px; font-weight: 600; font-variant-numeric: tabular-nums; white-space: nowrap">{{r.price}}</span></sc-if>
          <sc-if value="{{r.notOff}}" hint-placeholder-val="{{ false }}"><span class="typing" style="display: flex; align-items: center; gap: 4px; font-size: 12px; color: var(--ink2); white-space: nowrap"><span></span><span></span><span></span></span></sc-if>
        </div>
      </sc-for>
    </div>
    <span style="font-size: 11px; color: var(--ink2); padding: 0 4px">Prețurile sunt ofertele Jobzerilor. Taxa Jobzee de 15% se adaugă la oferta aleasă.</span>
    <sc-if value="{{hasOffers}}" hint-placeholder-val="{{ true }}">
      <a href="''' + nxt + '''" class="pr" style="display: flex; align-items: center; justify-content: center; height: 54px; border-radius: 27px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 600; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">{{cta}}</a>
    </sc-if>
    <sc-if value="{{noOffers}}" hint-placeholder-val="{{ false }}">
      <a href="FaraOferte.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 54px; border-radius: 27px; background: var(--surf3); color: var(--ink2); font-size: 16px; font-weight: 500; text-decoration: none">Aștept ofertele… · Opțiuni</a>
    </sc-if>
  </div>''')
    return page('Radar live', theme, b, css, logic)
