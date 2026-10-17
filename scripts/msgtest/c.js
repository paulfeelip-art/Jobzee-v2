class DCLogic{constructor(p){this.props=p||{};this.state={}}setState(o){Object.assign(this.state,o)}}

class Component extends DCLogic {
  constructor(props) { super(props); this.state = { lvl: 's', own: { ruleta: true } }; }
  renderVals() {
    const s = this.state, all = [{"k": "surub", "n": "Șurubelniță cu 32 de biți", "s": "Mâner cu clichet · biți PH, PZ, Torx", "p": 89, "ic": "work_tools", "av": "ok", "lvl": "s"}, {"k": "imbus", "n": "Set chei imbus (9 buc.)", "s": "1,5–10 mm · oțel CrV", "p": 39, "ic": "repair", "av": "ok", "lvl": "s"}, {"k": "nivela", "n": "Nivelă 60 cm", "s": "3 bule · magnetică", "p": 59, "ic": "match", "av": "ok", "lvl": "s"}, {"k": "ruleta", "n": "Ruletă 5 m", "s": "Bandă 19 mm · frână automată", "p": 35, "ic": "route", "av": "ok", "lvl": "s"}, {"k": "ciocan", "n": "Ciocan 300 g", "s": "Mâner din fibră de sticlă", "p": 49, "ic": "repair", "av": "q", "lvl": "s"}, {"k": "cutie", "n": "Cutie organizator", "s": "Compartimente reglabile", "p": 79, "ic": "briefcase", "av": "ok", "lvl": "s"}, {"k": "masina", "n": "Mașină de înșurubat 18 V", "s": "2 acumulatori · 50 Nm", "p": 499, "ic": "work_tools", "av": "ok", "lvl": "p"}, {"k": "burghie", "n": "Set burghie (15 buc.)", "s": "Lemn, metal, beton", "p": 69, "ic": "repair", "av": "ok", "lvl": "p"}, {"k": "detector", "n": "Detector cabluri și profile", "s": "Metal, lemn, tensiune", "p": 129, "ic": "radar", "av": "q", "lvl": "p"}, {"k": "genunchiere", "n": "Genunchiere de lucru", "s": "Gel · reglabile", "p": 59, "ic": "shield", "av": "ok", "lvl": "p"}];
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
  }
}

const c=new Component({});const v=c.renderVals();console.log(Object.keys(v).length)