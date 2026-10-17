# Generates the role-based Jobzee boards (light + dark) into the canvas project.
import os, json

OUT = os.path.join(os.path.dirname(__file__), 'jobzee-design', 'project')

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', system-ui, sans-serif"
ROUND = "ui-rounded, 'SF Pro Rounded', -apple-system, BlinkMacSystemFont, system-ui, sans-serif"

THEMES = {
    'L': dict(bg='#F2F2F7', surf='#FFFFFF', surf2='#F2F2F7', surf3='#E5E5EA', ink='#1C1C1E', ink2='#6E6E73', ink3='#C7C7CC',
              sep='#D1D1D6', brand='#FF9F0A', onbrand='#1C1C1E', btext='#B35600', bsoft='#FFF4E5', bsoft2='#FFE7C2',
              ok='#34C759', oktext='#1F7A35', oksoft='#E8F7EC', glass='rgba(255,255,255,0.82)', glass2='rgba(255,255,255,0.94)',
              scrim='rgba(0,0,0,0.38)', shadow='rgba(0,0,0,0.10)', invbg='#1C1C1E', invink='#FFFFFF',
              land='#F5F1E8', road='#FFFFFF', park='#D3EAC7', water='#BCDDF7', aur1='#FFB347', aur2='#FFD8A8', aur3='#FFC2D1'),
    'D': dict(bg='#000000', surf='#1C1C1E', surf2='#2C2C2E', surf3='#3A3A3C', ink='#FFFFFF', ink2='#98989D', ink3='#48484A',
              sep='#38383A', brand='#FF9F0A', onbrand='#1C1C1E', btext='#FFB340', bsoft='rgba(255,159,10,0.16)', bsoft2='rgba(255,159,10,0.28)',
              ok='#30D158', oktext='#30D158', oksoft='rgba(48,209,88,0.16)', glass='rgba(36,36,38,0.78)', glass2='rgba(28,28,30,0.95)',
              scrim='rgba(0,0,0,0.6)', shadow='rgba(0,0,0,0.5)', invbg='#FFFFFF', invink='#000000',
              land='#1B1C1F', road='#2E3035', park='#1C2A20', water='#17283A', aur1='#B35600', aur2='#5A2E00', aur3='#5B1F3A'),
}


def theme_css(t):
    v = THEMES[t]
    return '.th{' + ';'.join('--%s:%s' % (k, val) for k, val in v.items()) + '}'


BASE_CSS = """
body{margin:0}
a{color:var(--btext)}
@keyframes up{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes pop{0%{opacity:0;transform:scale(.5)}65%{opacity:1;transform:scale(1.08)}100%{opacity:1;transform:none}}
@keyframes sheet{from{opacity:0;transform:translateY(70%)}to{opacity:1;transform:none}}
@keyframes ring{0%{transform:scale(.6);opacity:.55}100%{transform:scale(2.6);opacity:0}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
@keyframes drift{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(30px,-24px) scale(1.12)}66%{transform:translate(-26px,18px) scale(.94)}}
@keyframes glow{0%,100%{opacity:.45}50%{opacity:1}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes drop{0%{opacity:0;transform:translateY(-24px) scale(.7)}60%{opacity:1;transform:translateY(3px) scale(1.06)}100%{opacity:1;transform:none}}
@keyframes tick{0%,42%{transform:none}50%,92%{transform:translateY(-40px)}100%{transform:none}}
@keyframes fadeSlide{0%,42%{opacity:1;transform:none}50%,92%{opacity:0;transform:translateY(-8px)}100%{opacity:1;transform:none}}
@keyframes fadeSlide2{0%,42%{opacity:0;transform:translateY(8px)}50%,92%{opacity:1;transform:none}100%{opacity:0;transform:translateY(8px)}}
@keyframes dotA{0%,45%{width:16px;opacity:1}50%,95%{width:6px;opacity:.35}100%{width:16px;opacity:1}}
@keyframes dotB{0%,45%{width:6px;opacity:.35}50%,95%{width:16px;opacity:1}100%{width:6px;opacity:.35}}
@keyframes halo{0%{box-shadow:0 0 0 0 rgba(255,159,10,.55)}100%{box-shadow:0 0 0 18px rgba(255,159,10,0)}}
@keyframes heat{0%,100%{transform:scale(1);opacity:.8}50%{transform:scale(1.15);opacity:1}}
.u{animation:up .55s cubic-bezier(.2,.8,.2,1) both}
.d1{animation-delay:.08s}.d2{animation-delay:.16s}.d3{animation-delay:.24s}.d4{animation-delay:.32s}.d5{animation-delay:.4s}.d6{animation-delay:.48s}
.pop{animation:pop .6s cubic-bezier(.2,.9,.3,1.3) both}
.sheet{animation:sheet .7s cubic-bezier(.2,.9,.25,1) both}
.float{animation:float 4.5s ease-in-out infinite}
.glow{animation:glow 1.8s ease-in-out infinite}
.drop{animation:drop .8s cubic-bezier(.2,.8,.2,1) both}
.pr{transition:transform .22s cubic-bezier(.3,.7,.4,1.4), opacity .2s}.pr:active{transform:scale(.95)}
.ic{display:inline-block;background:currentColor;-webkit-mask-position:center;mask-position:center;-webkit-mask-size:contain;mask-size:contain;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;flex-shrink:0}
.glass{background:var(--glass);backdrop-filter:blur(24px) saturate(1.6);-webkit-backdrop-filter:blur(24px) saturate(1.6)}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
"""


def page(title, theme, body, extra_css='', logic='renderVals() { return {}; }', h=844):
    return ('<!doctype html>\n<html lang="ro">\n<head>\n<meta charset="utf-8">\n<title>Jobzee · ' + title + '</title>\n'
            '<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n<style>\n' + theme_css(theme) + BASE_CSS + extra_css +
            '\n</style>\n</helmet>\n<div class="th" style="width: 390px; height: ' + str(h) + 'px; box-sizing: border-box; background: var(--bg); font-family: ' + FONT +
            '; color: var(--ink); position: relative; overflow: hidden">\n' + body + '\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\n'
            'class Component extends DCLogic {\n  ' + logic + '\n}\n</script>\n</body>\n</html>\n')


def ic(name, size=20, color='currentColor', extra=''):
    url = 'assets/icons/icon-%s.svg' % name
    return ('<span class="ic" aria-hidden="true" style="width: %dpx; height: %dpx; color: %s; -webkit-mask-image: url(%s); mask-image: url(%s); %s"></span>'
            % (size, size, color, url, url, extra))


def mark(size=48, j=None):
    # Official Jobzee mark (pin with wrench cutout), cut from the brand reference sheet.
    return '<img src="assets/brand/jobzee-mark.png" alt="" style="height: %dpx; width: auto; display: block; flex-shrink: 0">' % size

def wordmark(px=40):
    # Official wordmark (grey "job", orange "zee") from the brand files; readable on light and dark.
    return '<img src="assets/brand/jobzee-wordmark.png" alt="jobzee" style="height: %dpx; width: auto; display: block">' % int(px * 1.15)


CHEV = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--ink3)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"></path></svg>'
BACK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"></path></svg>'
CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
CLOSE = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>'
APPLE = '<svg width="18" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.4c-.02-2.3 1.88-3.4 1.97-3.46-1.07-1.57-2.74-1.78-3.33-1.8-1.42-.14-2.77.83-3.49.83-.72 0-1.83-.81-3.01-.79-1.55.02-2.98.9-3.78 2.29-1.61 2.8-.41 6.94 1.16 9.21.77 1.11 1.68 2.36 2.88 2.31 1.16-.05 1.6-.75 3-.75s1.79.75 3.01.72c1.25-.02 2.03-1.13 2.79-2.25.88-1.29 1.24-2.54 1.26-2.6-.03-.01-2.42-.93-2.44-3.7zM14.08 5.65c.64-.77 1.07-1.85.95-2.92-.92.04-2.03.61-2.69 1.38-.59.68-1.11 1.78-.97 2.83 1.03.08 2.07-.52 2.71-1.29z"></path></svg>'
GOOGLE = ('<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true">'
          '<path d="M22.6 12.3c0-.8-.1-1.5-.2-2.2H12v4.2h5.9c-.3 1.4-1 2.5-2.2 3.3v2.7h3.6c2.100-1.900 3.300-4.800 3.300-8z" fill="#4285F4"></path>'
          '<path d="M12 23c3 0 5.500-1 7.300-2.700l-3.600-2.700c-1 .7-2.200 1.100-3.700 1.100-2.900 0-5.300-1.900-6.200-4.500H2.100v2.800C3.900 20.600 7.700 23 12 23z" fill="#34A853"></path>'
          '<path d="M5.800 14.200c-.2-.7-.4-1.400-.4-2.200s.1-1.500.4-2.200V7H2.100C1.400 8.500 1 10.200 1 12s.4 3.500 1.100 5l3.700-2.800z" fill="#FBBC05"></path>'
          '<path d="M12 5.400c1.600 0 3.100.6 4.200 1.700l3.200-3.200C17.500 2.100 15 1 12 1 7.700 1 3.900 3.400 2.100 7l3.700 2.800C6.700 7.300 9.100 5.400 12 5.400z" fill="#EA4335"></path></svg>')
PHONE = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="3.5"></rect><path d="M10.5 18.5h3"></path></svg>'
MAIL = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="4"></rect><path d="M4 7.5l8 5.5 8-5.5"></path></svg>'


def tabbar(role, active, links):
    # role: client / jobzer. links: dict tab -> href
    if role == 'client':
        tabs = [('acasa', 'Acasă', '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"></path>'),
                ('activitate', 'Activitate', '<rect x="4" y="4" width="16" height="16" rx="5"></rect><path d="M8 9h8M8 13h8M8 17h5"></path>'),
                ('mesaje', 'Mesaje', '<path d="M5 5h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H10l-5 4V7a2 2 0 0 1 2-2z"></path>'),
                ('cont', 'Cont', '<circle cx="12" cy="8" r="4"></circle><path d="M4 21c1-4 4-6 8-6s7 2 8 6"></path>')]
    else:
        tabs = [('acasa', 'Acasă', '<path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"></path>'),
                ('sarcini', 'Sarcini', '<rect x="4" y="4" width="16" height="16" rx="5"></rect><path d="M8 9h8M8 13h8M8 17h5"></path>'),
                ('incasari', 'Încasări', '<rect x="3" y="6" width="18" height="13" rx="4"></rect><path d="M16 12.5h2"></path>'),
                ('cont', 'Profil', '<circle cx="12" cy="8" r="4"></circle><path d="M4 21c1-4 4-6 8-6s7 2 8 6"></path>')]
    out = ('<nav aria-label="Meniu" class="glass" style="position: absolute; left: 16px; right: 16px; bottom: 24px; height: 64px; border-radius: 32px; '
           'box-shadow: 0 10px 30px var(--shadow); display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); padding: 6px; box-sizing: border-box; z-index: 5">')
    for key, label, path in tabs:
        on = key == active
        style = ('border-radius: 26px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; font-size: 11px; text-decoration: none; '
                 + ('background: var(--bsoft); color: var(--btext); font-weight: 500' if on else 'color: var(--ink2); font-weight: 500'))
        svg = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               + (path.replace('<path ', '<path fill="currentColor" ') if on and key == 'acasa' else path) + '</svg>')
        out += '<a href="%s" class="pr" %s style="%s">%s%s</a>' % (links.get(key, '#'), 'aria-current="page"' if on else '', style, svg, label)
    return out + '</nav>'


def write(name, html):
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(html)
    print('wrote', name, len(html))


# ---------------------------------------------------------------- Splash / Autentificare
PEOPLE = [('person-jobzer-1', 26, 66, 62, 0), ('person-client-1', 300, 54, 58, .15), ('person-jobzer-2', 322, 168, 48, .3),
          ('person-client-3', 20, 172, 48, .45), ('person-jobzer-3', 172, 22, 44, .6)]


def splash(theme, intro):
    dark = theme == 'D'
    nxt = {'apple': 'RolDark.dc.html' if dark else 'Rol.dc.html', 'google': 'RolDark.dc.html' if dark else 'Rol.dc.html',
           'phone': 'Telefon.dc.html', 'mail': 'Email.dc.html', 'login': 'Telefon.dc.html', 'guest': 'RolDark.dc.html' if dark else 'Rol.dc.html'}
    T = 2.1 if intro else 0.0  # moment the logo lifts and the sign-in sheet arrives
    css = """
@keyframes markIn{0%{opacity:0;transform:scale(.3) rotate(-14deg)}55%{opacity:1;transform:scale(1.12) rotate(4deg)}75%{transform:scale(.96)}100%{opacity:1;transform:none}}
@keyframes letters{from{opacity:0;transform:translateY(14px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
@keyframes lift{from{transform:translateY(0) scale(1)}to{transform:translateY(-232px) scale(.62)}}
@keyframes fadeOut{to{opacity:0}}
.aur{position:absolute;border-radius:50%;filter:blur(60px);animation:drift 14s ease-in-out infinite}
"""
    if intro:
        css += """
.logo{animation:lift .95s cubic-bezier(.65,0,.25,1) %(T)ss both}
.mark{animation:markIn 1s cubic-bezier(.2,.9,.3,1.2) .15s both}
.wm{animation:letters .7s cubic-bezier(.2,.8,.2,1) .75s both}
.loader{animation:fadeOut .3s ease %(T0)ss both}
.late{animation:up .6s cubic-bezier(.2,.8,.2,1) both}
.sh{animation:sheet .8s cubic-bezier(.2,.9,.25,1) %(T2)ss both}
.av{animation:pop .6s cubic-bezier(.2,.9,.3,1.3) both}
""" % dict(T=T, T0=T - .2, T2=T + .3)
    else:
        css += """
.logo{transform:translateY(-232px) scale(.62)}
.loader{display:none}
.late{animation:up .55s cubic-bezier(.2,.8,.2,1) both}
.sh{animation:sheet .7s cubic-bezier(.2,.9,.25,1) .05s both}
.av{animation:pop .6s cubic-bezier(.2,.9,.3,1.3) both}
"""
    b = []
    b.append('<div class="aur" style="width: 320px; height: 320px; left: -90px; top: 40px; background: var(--aur1); opacity: .55"></div>')
    b.append('<div class="aur" style="width: 280px; height: 280px; right: -110px; top: 210px; background: var(--aur3); opacity: .5; animation-delay: -5s"></div>')
    b.append('<div class="aur" style="width: 260px; height: 260px; left: 70px; top: 360px; background: var(--aur2); opacity: .6; animation-delay: -9s"></div>')
    # floating people discs (appear after lift)
    for i, (img, x, y, s, d) in enumerate(PEOPLE):
        b.append('<div class="av" style="position: absolute; left: %dpx; top: %dpx; animation-delay: %.2fs; z-index: 1">'
                 '<div class="float" style="animation-delay: -%.1fs; width: %dpx; height: %dpx; border-radius: 50%%; overflow: hidden; border: 3px solid var(--surf); box-shadow: 0 10px 26px var(--shadow)">'
                 '<img src="assets/people/%s.webp" alt="" style="width: 100%%; height: 100%%; object-fit: cover; display: block"></div></div>'
                 % (x, y, T + .45 + d, i * .9, s, s, img))
    b.append('<div class="av glass" style="position: absolute; left: 0; right: 0; margin: 0 auto; width: max-content; top: 302px; animation-delay: %.2fs; height: 34px; padding: 0 14px 0 10px; border-radius: 17px; display: flex; align-items: center; gap: 7px; font-size: 13px; font-weight: 500; box-shadow: 0 8px 20px var(--shadow); z-index: 2">'
             '<span class="glow" style="width: 8px; height: 8px; border-radius: 4px; background: var(--ok)"></span>128 Jobzeri online lângă tine</div>' % (T + .9))
    # logo group (centered, lifts)
    b.append('<div class="logo" style="position: absolute; left: 0; right: 0; top: 330px; display: flex; flex-direction: column; align-items: center; gap: 16px; z-index: 3; transform-origin: 50% 50%">'
             '<div style="position: relative; width: 104px; height: 104px">'
             + ('<div class="loader" style="position: absolute; inset: 0"><div style="position: absolute; inset: 8px; border-radius: 50%; background: var(--brand); animation: ring 1.6s ease-out .9s infinite"></div>'
                '<div style="position: absolute; inset: 8px; border-radius: 50%; background: var(--brand); animation: ring 1.6s ease-out 1.5s infinite"></div></div>' if intro else '')
             + '<div class="mark" style="position: absolute; inset: 0; border-radius: 32px; background: var(--surf); box-shadow: 0 18px 40px rgba(255,159,10,0.35); display: flex; align-items: center; justify-content: center">' + mark(70) + '</div></div>'
             '<div class="wm">' + wordmark(46) + '</div></div>')
    b.append('<p class="late" style="position: absolute; left: 0; right: 0; top: 252px; margin: 0; text-align: center; font-size: 17px; color: var(--ink2); animation-delay: %.2fs; z-index: 3">Ajutor lângă tine, în câteva minute.</p>' % (T + .5))
    # sign-in sheet
    btn = 'display: flex; align-items: center; justify-content: center; gap: 10px; height: 54px; border-radius: 27px; font-size: 17px; font-weight: 500; text-decoration: none'
    b.append('<div class="sh glass" style="position: absolute; left: 10px; right: 10px; bottom: 10px; border-radius: 38px; padding: 22px 16px 18px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 -10px 40px var(--shadow); z-index: 4; background: var(--glass2)">'
             '<div style="display: flex; flex-direction: column; gap: 4px; padding: 0 6px 6px"><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.6px">Începe în 30 de secunde</span>'
             '<span style="font-size: 15px; color: var(--ink2)">Un singur cont. Alegi apoi dacă ceri ajutor sau câștigi bani.</span></div>'
             '<a href="%s" class="pr" style="%s; background: var(--invbg); color: var(--invink)">%sContinuă cu Apple</a>'
             '<a href="%s" class="pr" style="%s; background: var(--surf); color: var(--ink); box-shadow: inset 0 0 0 1px var(--sep)">%sContinuă cu Google</a>'
             '<a href="%s" class="pr" style="%s; background: var(--brand); color: var(--onbrand); box-shadow: 0 10px 24px rgba(255,159,10,0.32)">%sContinuă cu telefonul</a>'
             '<a href="%s" class="pr" style="%s; height: 46px; color: var(--ink); background: var(--surf2)">%sCreează cont cu e-mail</a>'
             '<p style="margin: 4px 0 0; text-align: center; font-size: 14px; color: var(--ink2)">Ai deja cont? <a href="%s" style="font-weight: 500; text-decoration: none">Intră</a> · <a href="%s" style="font-weight: 500; text-decoration: none">Mă uit întâi, fără cont</a></p>'
             '<p style="margin: 0; text-align: center; font-size: 11px; line-height: 1.4; color: var(--ink2)">Continuând, accepți <a href="#termeni" style="color: inherit">Termenii</a> și <a href="#gdpr" style="color: inherit">Politica de confidențialitate</a>.</p></div>'
             % (nxt['apple'], btn, APPLE, nxt['google'], btn, GOOGLE, nxt['phone'], btn, PHONE, nxt['mail'], btn, MAIL, nxt['login'], nxt['guest']))
    return page('Splash' if intro else 'Autentificare', theme, '\n'.join(b), css)


# ---------------------------------------------------------------- Creare cont cu e-mail
def email():
    css = """
@keyframes bar{from{width:0}}
.fld{display:flex;flex-direction:column;gap:2px;padding:10px 16px;background:var(--surf)}
.fld label{font-size:12px;color:var(--ink2);font-weight:500}
.fld input{border:0;outline:0;background:transparent;font:400 17px/24px inherit;font-family:inherit;color:var(--ink);padding:0}
.fld:focus-within{box-shadow:inset 0 0 0 2px var(--brand);border-radius:inherit}
"""
    logic = """constructor(props) { super(props); this.state = { show: false, terms: false }; }
  renderVals() {
    const s = this.state;
    return {
      pwType: s.show ? 'text' : 'password',
      eyeLabel: s.show ? 'Ascunde' : 'Arată',
      toggleEye: () => this.setState({ show: !s.show }),
      toggleTerms: () => this.setState({ terms: !s.terms }),
      termsOn: s.terms, termsOff: !s.terms, termsAttr: s.terms ? 'true' : 'false',
      boxStyle: 'width: 26px; height: 26px; border-radius: 13px; border: 0; cursor: pointer; flex-shrink: 0; display: flex; align-items: center; justify-content: center; transition: background .25s, transform .3s cubic-bezier(.2,.9,.3,1.4); ' +
        (s.terms ? 'background: var(--brand); color: var(--onbrand); transform: scale(1.08);' : 'background: var(--surf); box-shadow: inset 0 0 0 2px var(--ink3); color: transparent;')
    };
  }"""
    b = '''<div style="padding: 58px 16px 34px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
  <div class="u" style="display: flex; align-items: center; justify-content: space-between">
    <a href="Main.dc.html" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    ''' + mark(30) + '''
    <span style="width: 40px"></span>
  </div>
  <div class="u d1" style="padding: 4px 4px 0"><h1 style="margin: 0; font-size: 32px; font-weight: 600; letter-spacing: -0.8px">Creează cont</h1>
    <p style="margin: 6px 0 0; font-size: 16px; color: var(--ink2)">Durează un minut. Îți confirmăm adresa printr-un link.</p></div>
  <div class="u d2" style="border-radius: 22px; overflow: hidden; display: flex; flex-direction: column; gap: 1px; background: var(--sep)">
    <div class="fld"><label for="nm">Nume și prenume</label><input id="nm" value="Andrei Popescu" autocomplete="name"></div>
    <div class="fld"><label for="em">E-mail</label><input id="em" type="email" value="andrei@exemplu.ro" autocomplete="email"></div>
    <div class="fld" style="flex-direction: row; align-items: center; gap: 10px"><span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><label for="pw">Parolă</label><input id="pw" type="{{pwType}}" value="Jobzee2029!" autocomplete="new-password"></span>
      <button type="button" onClick="{{toggleEye}}" class="pr" style="border: 0; background: var(--surf2); color: var(--ink); height: 32px; padding: 0 12px; border-radius: 16px; font: 500 13px/1 inherit; font-family: inherit; cursor: pointer">{{eyeLabel}}</button></div>
  </div>
  <div class="u d3" style="display: flex; flex-direction: column; gap: 8px; padding: 0 6px">
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">
      <span style="height: 6px; border-radius: 3px; background: var(--ok); animation: bar .5s ease .4s both"></span><span style="height: 6px; border-radius: 3px; background: var(--ok); animation: bar .5s ease .55s both"></span><span style="height: 6px; border-radius: 3px; background: var(--ok); animation: bar .5s ease .7s both"></span><span style="height: 6px; border-radius: 3px; background: var(--surf3)"></span></div>
    <span style="font-size: 13px; color: var(--oktext); font-weight: 500">Parolă puternică · minim 8 caractere, o cifră, un simbol</span>
  </div>
  <div class="u d4" style="display: flex; align-items: flex-start; gap: 12px; padding: 4px 6px">
    <button type="button" onClick="{{toggleTerms}}" aria-pressed="{{termsAttr}}" aria-label="Accept termenii" style="{{boxStyle}}">''' + CHECK + '''</button>
    <span style="font-size: 14px; line-height: 1.4; color: var(--ink2)">Accept <a href="#termeni">Termenii</a> și <a href="#gdpr">Politica de confidențialitate</a>. Am peste 18 ani.</span>
  </div>
  <div style="flex-grow: 1"></div>
  <sc-if value="{{termsOn}}" hint-placeholder-val="{{ false }}">
    <a href="Rol.dc.html" class="pop pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.35)">Creează contul</a>
  </sc-if>
  <sc-if value="{{termsOff}}" hint-placeholder-val="{{ true }}">
    <div style="display: flex; flex-direction: column; gap: 8px; align-items: center"><span style="display: flex; align-items: center; justify-content: center; width: 100%; height: 56px; border-radius: 28px; background: var(--surf3); color: var(--ink2); font-size: 17px; font-weight: 500">Creează contul</span>
    <span style="font-size: 13px; color: var(--ink2)">Bifează acordul ca să continui</span></div>
  </sc-if>
</div>'''
    return page('Creează cont', 'L', b, css, logic)


# ---------------------------------------------------------------- Alege rolul
def rol(theme):
    dark = theme == 'D'
    css = """
.card{position:relative;display:flex;flex-direction:column;gap:10px;padding:8px 8px 12px;border-radius:30px;background:var(--surf);border:0;text-align:left;cursor:pointer;font-family:inherit;color:var(--ink);transition:transform .35s cubic-bezier(.2,.9,.3,1.3), box-shadow .3s, opacity .3s}
.card .ph{height:92px;border-radius:22px;overflow:hidden;position:relative}
.card .ph img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.2s cubic-bezier(.2,.8,.2,1)}
.card[aria-pressed="true"]{box-shadow:0 0 0 3px var(--brand), 0 18px 40px rgba(255,159,10,0.22);transform:scale(1)}
.card[aria-pressed="true"] .ph img{transform:scale(1.06)}
.card[aria-pressed="false"]{box-shadow:0 1px 0 var(--sep);transform:scale(.97);opacity:.82}
.radio{position:absolute;right:20px;top:20px;width:30px;height:30px;border-radius:15px;display:flex;align-items:center;justify-content:center;transition:all .3s cubic-bezier(.2,.9,.3,1.4)}
.card[aria-pressed="true"] .radio{background:var(--brand);color:var(--onbrand);transform:scale(1.05)}
.card[aria-pressed="false"] .radio{background:rgba(255,255,255,0.7);color:transparent;box-shadow:inset 0 0 0 2px rgba(255,255,255,0.95)}
.tag{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 9px;border-radius:15px;background:var(--surf2);font-size:12px;font-weight:500;color:var(--ink)}
"""
    logic = """constructor(props) { super(props); this.state = { role: 'client' }; }
  renderVals() {
    const r = this.state.role;
    return {
      pickClient: () => this.setState({ role: 'client' }),
      pickJobzer: () => this.setState({ role: 'jobzer' }),
      cAttr: r === 'client' ? 'true' : 'false', jAttr: r === 'jobzer' ? 'true' : 'false',
      isClient: r === 'client', isJobzer: r === 'jobzer'
    };
  }"""
    tag = lambda i, t: '<span class="tag">' + ic(i, 15, 'var(--btext)') + t + '</span>'
    nextC = 'AcasaDark.dc.html' if dark else 'Acasa.dc.html'
    nextJ = 'StartJobzer.dc.html'
    back = 'MainDark.dc.html' if dark else 'Main.dc.html'
    b = '''<div style="padding: 56px 16px 34px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  <div class="u" style="display: flex; align-items: center; justify-content: space-between">
    <a href="''' + back + '''" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    <span style="display: flex; gap: 6px"><span style="width: 22px; height: 6px; border-radius: 3px; background: var(--brand)"></span><span style="width: 22px; height: 6px; border-radius: 3px; background: var(--brand)"></span><span style="width: 22px; height: 6px; border-radius: 3px; background: var(--surf3)"></span></span>
    <span style="width: 40px"></span>
  </div>
  <div class="u d1" style="padding: 2px 4px 2px"><h1 style="margin: 0; font-size: 28px; line-height: 1.1; font-weight: 600; letter-spacing: -0.7px">Cum vrei să folosești Jobzee?</h1>
    <p style="margin: 6px 0 0; font-size: 15px; color: var(--ink2)">Alegi acum. Poți schimba oricând din Cont.</p></div>

  <button type="button" class="card u d2" onClick="{{pickClient}}" aria-pressed="{{cAttr}}">
    <span class="ph"><img src="assets/photos/hero-client-home.webp" alt="">
      <span class="glass" style="position: absolute; left: 10px; bottom: 10px; height: 28px; padding: 0 10px; border-radius: 14px; display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 500; color: var(--ink)"><span class="glow" style="width: 7px; height: 7px; border-radius: 4px; background: var(--ok)"></span>128 Jobzeri disponibili</span></span>
    <span class="radio">''' + CHECK + '''</span>
    <span style="padding: 0 6px; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.4px">Am nevoie de ajutor</span>
      <span style="font-size: 14px; line-height: 1.35; color: var(--ink2)">Spui de ce ai nevoie și alegi dintre oferte de la Jobzeri din apropiere.</span></span>
    <span style="padding: 0 6px; display: flex; gap: 6px; flex-wrap: wrap">''' + tag('rapid', 'În câteva minute') + tag('plati', 'Plătești la final') + '''</span>
  </button>

  <button type="button" class="card u d3" onClick="{{pickJobzer}}" aria-pressed="{{jAttr}}">
    <span class="ph"><img src="assets/photos/hero-jobzer-outdoor.webp" alt="" style="object-position: 50% 30%">
      <span class="glass" style="position: absolute; left: 10px; bottom: 10px; height: 28px; padding: 0 10px; border-radius: 14px; display: flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 500; color: var(--ink)"><span class="glow" style="width: 7px; height: 7px; border-radius: 4px; background: var(--brand)"></span>34 cereri noi azi în zona ta</span></span>
    <span class="radio">''' + CHECK + '''</span>
    <span style="padding: 0 6px; display: flex; flex-direction: column; gap: 3px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.4px">Vreau să câștig bani</span>
      <span style="font-size: 14px; line-height: 1.35; color: var(--ink2)">Primești cereri pe ce știi să faci. Păstrezi 100% din prețul tău.</span></span>
    <span style="padding: 0 6px; display: flex; gap: 6px; flex-wrap: wrap">''' + tag('calendar', 'Program flexibil') + tag('aproape', 'Sarcini aproape') + '''</span>
  </button>

  <div style="flex-grow: 1"></div>
  <sc-if value="{{isClient}}" hint-placeholder-val="{{ true }}">
    <a href="''' + nextC + '''" class="pop pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.35)">Continuă ca client</a>
  </sc-if>
  <sc-if value="{{isJobzer}}" hint-placeholder-val="{{ false }}">
    <a href="''' + nextJ + '''" class="pop pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--invbg); color: var(--invink); font-size: 17px; font-weight: 500; text-decoration: none">Continuă ca Jobzer</a>
  </sc-if>
  <p style="margin: 0; text-align: center; font-size: 13px; color: var(--ink2)">Poți folosi ambele roluri. Locația o cerem abia la prima cerere.</p>
</div>'''
    return page('Alege rolul', theme, b, css, logic)


# ---------------------------------------------------------------- Schimbă rolul (sheet)
def schimba(theme):
    dark = theme == 'D'
    css = """
.seg{position:relative;display:grid;grid-template-columns:1fr 1fr;padding:5px;border-radius:30px;background:var(--surf2)}
.thumb{position:absolute;top:5px;bottom:5px;left:5px;width:calc(50% - 5px);border-radius:25px;background:var(--surf);box-shadow:0 6px 18px var(--shadow);transition:transform .5s cubic-bezier(.3,1.3,.4,1)}
.opt{position:relative;z-index:1;border:0;background:transparent;height:76px;border-radius:25px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font-family:inherit;font-size:15px;font-weight:500;color:var(--ink2);cursor:pointer;transition:color .3s}
.opt[aria-pressed="true"]{color:var(--ink)}
.opt .bub{width:34px;height:34px;border-radius:17px;display:flex;align-items:center;justify-content:center;background:var(--surf3);color:var(--ink2);transition:all .35s cubic-bezier(.2,.9,.3,1.4)}
.opt[aria-pressed="true"] .bub{background:var(--brand);color:var(--onbrand);transform:scale(1.1)}
.step{display:flex;align-items:center;gap:12px;padding:12px 14px}
.num{width:28px;height:28px;border-radius:14px;background:var(--bsoft);color:var(--btext);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;flex-shrink:0}
"""
    logic = """constructor(props) { super(props); this.state = { role: 'jobzer' }; }
  renderVals() {
    const r = this.state.role;
    return {
      toClient: () => this.setState({ role: 'client' }),
      toJobzer: () => this.setState({ role: 'jobzer' }),
      cAttr: r === 'client' ? 'true' : 'false', jAttr: r === 'jobzer' ? 'true' : 'false',
      isClient: r === 'client', isJobzer: r === 'jobzer',
      thumbStyle: r === 'jobzer' ? 'transform: translateX(100%)' : 'transform: none'
    };
  }"""
    home = 'AcasaDark.dc.html' if dark else 'Acasa.dc.html'
    person = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11l8-7 8 7v9h-5v-6H9v6H4z"></path></svg>'
    tool = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6a4 4 0 0 0-5 5l-6 6 3 3 6-6a4 4 0 0 0 5-5l-2 2-3-1-1-3z"></path></svg>'
    # dimmed Cont behind
    bgrows = ''.join('<div style="height: 48px; margin: 0 16px; border-top: 0.5px solid var(--sep); display: flex; align-items: center; gap: 12px"><span style="width: 30px; height: 30px; border-radius: 9px; background: var(--surf3)"></span><span style="width: %dpx; height: 12px; border-radius: 6px; background: var(--surf3)"></span></div>' % w for w in (120, 150, 110, 140))
    b = '''<div style="padding: 60px 16px 0; display: flex; flex-direction: column; gap: 14px">
  <span style="margin: 0 4px; font-size: 34px; font-weight: 600; letter-spacing: -0.9px">Cont</span>
  <div style="background: var(--surf); border-radius: 26px; padding: 14px 16px; display: flex; align-items: center; gap: 14px"><span style="width: 56px; height: 56px; border-radius: 28px; background: var(--surf3)"></span><span style="display: flex; flex-direction: column; gap: 6px"><span style="width: 110px; height: 14px; border-radius: 7px; background: var(--surf3)"></span><span style="width: 150px; height: 11px; border-radius: 6px; background: var(--surf3)"></span></span></div>
  <div style="background: var(--surf); border-radius: 26px; overflow: hidden; padding: 4px 0">''' + bgrows + '''</div>
</div>
<div class="u" style="position: absolute; inset: 0; background: var(--scrim); animation-duration: .35s"></div>
<div class="sheet" style="position: absolute; left: 8px; right: 8px; bottom: 8px; background: var(--glass2); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px); border-radius: 40px; padding: 10px 16px 18px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 -10px 40px var(--shadow)">
  <span style="align-self: center; width: 38px; height: 5px; border-radius: 3px; background: var(--ink3)"></span>
  <div style="display: flex; align-items: flex-start; justify-content: space-between; padding: 0 4px">
    <span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 24px; font-weight: 600; letter-spacing: -0.6px">Schimbă rolul</span><span style="font-size: 14px; color: var(--ink2)">Același cont, aceleași date. Se schimbă meniul și Acasă.</span></span>
    <a href="''' + ('ContJobzer.dc.html' if False else 'Cont.dc.html') + '''" aria-label="Închide" class="pr" style="width: 32px; height: 32px; border-radius: 16px; background: var(--surf2); color: var(--ink2); display: flex; align-items: center; justify-content: center; flex-shrink: 0">''' + CLOSE + '''</a>
  </div>
  <div class="seg">
    <span class="thumb" style="{{thumbStyle}}"></span>
    <button type="button" class="opt" onClick="{{toClient}}" aria-pressed="{{cAttr}}"><span class="bub">''' + person + '''</span>Client</button>
    <button type="button" class="opt" onClick="{{toJobzer}}" aria-pressed="{{jAttr}}"><span class="bub">''' + tool + '''</span>Jobzer</button>
  </div>

  <sc-if value="{{isJobzer}}" hint-placeholder-val="{{ true }}">
    <div class="u" style="display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; gap: 12px; padding: 12px; border-radius: 24px; background: var(--bsoft)">
        <img src="assets/photos/hero-jobzer-outdoor.webp" alt="" style="width: 56px; height: 56px; border-radius: 28px; object-fit: cover; object-position: 50% 25%; flex-shrink: 0">
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Activează contul de Jobzer</span><span style="font-size: 13px; color: var(--ink2)">3 pași, cam 5 minute. Le faci o singură dată.</span></span>
      </div>
      <div style="background: var(--surf); border-radius: 24px; overflow: hidden">
        <div class="step"><span class="num">1</span><span style="flex-grow: 1; font-size: 15px">Forma legală: PFA, SRL sau independent</span>''' + CHEV + '''</div>
        <div class="step" style="border-top: 0.5px solid var(--sep); margin-left: 54px; padding-left: 0"><span style="flex-grow: 1; font-size: 15px">Skill-uri și prețuri</span>''' + CHEV + '''</div>
        <div class="step" style="border-top: 0.5px solid var(--sep); margin-left: 54px; padding-left: 0"><span style="flex-grow: 1; font-size: 15px">Verificarea identității</span>''' + CHEV + '''</div>
      </div>
      <span style="font-size: 13px; color: var(--ink2); padding: 0 6px">Cererile tale de client rămân în Activitate. Revii la client cu o atingere.</span>
      <a href="StartJobzer.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">Începe activarea</a>
    </div>
  </sc-if>
  <sc-if value="{{isClient}}" hint-placeholder-val="{{ false }}">
    <div class="u" style="display: flex; flex-direction: column; gap: 10px">
      <div style="display: flex; align-items: center; gap: 12px; padding: 12px; border-radius: 24px; background: var(--surf)">
        <img src="assets/photos/hero-client-home.webp" alt="" style="width: 56px; height: 56px; border-radius: 28px; object-fit: cover; flex-shrink: 0">
        <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Treci în modul client</span><span style="font-size: 13px; color: var(--ink2)">Comanzi servicii din același cont. Ca Jobzer apari offline până revii.</span></span>
      </div>
      <div style="display: flex; gap: 8px">
        <span style="flex: 1; padding: 12px; border-radius: 20px; background: var(--surf); display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">0</span><span style="font-size: 12px; color: var(--ink2)">sarcini active pierdute</span></span>
        <span style="flex: 1; padding: 12px; border-radius: 20px; background: var(--surf); display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 600">100%</span><span style="font-size: 12px; color: var(--ink2)">din încasări rămân ale tale</span></span>
      </div>
      <a href="''' + home + '''" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--invbg); color: var(--invink); font-size: 17px; font-weight: 500; text-decoration: none">Treci la client</a>
    </div>
  </sc-if>
</div>'''
    return page('Schimbă rolul', theme, b, css, logic)


# ---------------------------------------------------------------- Reclama încrucișată (house ad)
def ad_logic(extra_state='', extra_vals=''):
    return """constructor(props) { super(props); this.state = { ad: true%s }; }
  renderVals() {
    const s = this.state;
    return {
      ad: s.ad, closeAd: () => this.setState({ ad: false }), reopen: () => this.setState({ ad: true }), noAd: !s.ad%s
    };
  }""" % (extra_state, extra_vals)


def ad_card(kind, href, compact=False):
    if kind == 'earn':
        img, pos, lab = 'assets/photos/hero-jobzer-outdoor.webp', '50% 25%', 'Recomandat de Jobzee'
        a1, b1 = 'Te pricepi la montaj?', 'Câștigă bani în timpul liber, lângă casă.'
        a2, b2 = 'Ai o oră liberă azi?', '34 de cereri noi în zona ta. Tu alegi ce accepți.'
        cta = 'Vezi cât poți câștiga'
    else:
        img, pos, lab = 'assets/photos/hero-client-home.webp', '50% 40%', 'Recomandat de Jobzee'
        a1, b1 = 'Ai și tu nevoie de ajutor?', 'Comandă de la alți Jobzeri, din același cont.'
        a2, b2 = 'Curățenie după o zi lungă?', 'Primești oferte în câteva minute, plătești la final.'
        cta = 'Comandă un serviciu'
    return ('''<sc-if value="{{ad}}" hint-placeholder-val="{{ true }}">
    <div class="pop" style="position: relative; display: flex; align-items: center; gap: 12px; padding: 10px 12px 10px 10px; border-radius: 26px; background: linear-gradient(135deg, var(--bsoft2), var(--bsoft)); overflow: hidden">
      <a href="''' + href + '''" aria-label="''' + cta + '''" style="position: absolute; inset: 0; z-index: 1"></a>
      <span style="position: relative; width: 64px; height: 64px; flex-shrink: 0"><img src="''' + img + '''" alt="" style="width: 64px; height: 64px; border-radius: 32px; object-fit: cover; object-position: ''' + pos + '''; display: block">
        <span style="position: absolute; right: -2px; bottom: -2px; width: 22px; height: 22px; border-radius: 11px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center; border: 2px solid var(--surf)">''' + ic('rapid' if kind == 'earn' else 'verificat', 12, 'var(--onbrand)') + '''</span></span>
      <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px">
        <span style="font-size: 11px; font-weight: 600; letter-spacing: .4px; text-transform: uppercase; color: var(--btext)">''' + lab + '''</span>
        <span style="position: relative; height: 40px; overflow: hidden; display: block"><span style="display: flex; flex-direction: column; animation: tick 9s cubic-bezier(.7,0,.3,1) infinite"><span style="height: 40px; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">''' + a1 + '''</span><span style="font-size: 13px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">''' + b1 + '''</span></span><span style="height: 40px; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">''' + a2 + '''</span><span style="font-size: 13px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">''' + b2 + '''</span></span></span>
        </span>
        <span style="display: flex; align-items: center; gap: 8px; margin-top: 2px"><span style="font-size: 13px; font-weight: 600; color: var(--btext)">''' + cta + ''' ›</span>
          <span style="display: flex; gap: 4px; margin-left: auto"><span style="height: 6px; border-radius: 3px; background: var(--btext); animation: dotA 9s ease-in-out infinite"></span><span style="height: 6px; border-radius: 3px; background: var(--btext); animation: dotB 9s ease-in-out infinite"></span></span></span>
      </span>
      <button type="button" onClick="{{closeAd}}" aria-label="Ascunde recomandarea" class="pr" style="position: absolute; z-index: 2; right: 8px; top: 8px; width: 24px; height: 24px; border: 0; border-radius: 12px; background: rgba(0,0,0,0.08); color: var(--ink2); display: flex; align-items: center; justify-content: center; cursor: pointer; padding: 0">''' + CLOSE + '''</button>
    </div>
  </sc-if>
  <sc-if value="{{noAd}}" hint-placeholder-val="{{ false }}">
    <button type="button" onClick="{{reopen}}" class="u" style="border: 0; background: var(--surf2); border-radius: 18px; height: 40px; font-family: inherit; font-size: 13px; color: var(--ink2); cursor: pointer">Ascuns. Nu-ți mai arătăm asta 7 zile · Anulează</button>
  </sc-if>''')


# ---------------------------------------------------------------- Acasă client (map)
SERV = [('service-mobila', 'Montaj'), ('service-curatenie', 'Curățenie'), ('service-mutat-obiecte', 'Cărat'), ('service-sanitar', 'Instalații')]
PINS = [('person-jobzer-1', 50, 196, '4,9', .2), ('person-jobzer-3', 262, 196, '5,0', .35), ('person-jobzer-2', 250, 312, '4,8', .5), ('person-client-2', 26, 318, '4,7', .65)]


def map_svg(h=520):
    return ('<svg width="390" height="%d" viewBox="0 0 390 %d" aria-hidden="true" style="position: absolute; left: 0; top: 0; display: block">'
            '<rect width="390" height="%d" fill="var(--land)"></rect>'
            '<path d="M-10 430 C 80 390 170 460 270 420 S 400 400 400 400 L400 %d L-10 %d Z" style="fill: var(--water)"></path>'
            '<rect x="150" y="236" width="96" height="70" rx="22" style="fill: var(--park)"></rect><rect x="18" y="60" width="74" height="52" rx="16" style="fill: var(--park)"></rect>'
            '<path d="M-10 140 L400 100 M-10 340 L400 372 M120 -10 L92 %d M282 -10 L312 %d" stroke-width="16" stroke-linecap="round" fill="none" style="stroke: var(--road)"></path>'
            '<path d="M-10 236 L400 250 M200 -10 L188 %d" stroke-width="7" fill="none" style="stroke: var(--road)"></path></svg>') % (h, h, h, h + 10, h + 10, h + 10, h + 10, h + 10)


def acasa(theme):
    dark = theme == 'D'
    S = lambda n: n.replace('.dc.html', 'Dark.dc.html') if dark else n
    cont = 'Cont.dc.html'
    b = [map_svg()]
    b.append('<div style="position: absolute; left: 172px; top: 262px; width: 44px; height: 44px"><div style="position: absolute; inset: 0; border-radius: 22px; background: var(--brand); animation: ring 2.4s ease-out infinite"></div>'
             '<div style="position: absolute; left: 11px; top: 11px; width: 22px; height: 22px; border-radius: 11px; background: var(--brand); border: 4px solid var(--surf); box-sizing: border-box; box-shadow: 0 2px 8px rgba(0,0,0,0.25)"></div></div>')
    for img, x, y, r, d in PINS:
        b.append('<div class="drop glass" style="position: absolute; left: %dpx; top: %dpx; animation-delay: %.2fs; height: 38px; padding: 0 12px 0 4px; border-radius: 19px; box-shadow: 0 8px 20px var(--shadow); display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500">'
                 '<img src="assets/people/%s.webp" alt="" style="width: 30px; height: 30px; border-radius: 15px; object-fit: cover">%s ★</div>' % (x, y, d, img, r))
    b.append('''<div style="position: absolute; left: 16px; right: 16px; top: 56px; display: flex; flex-direction: column; gap: 10px">
    <div style="display: flex; justify-content: space-between; align-items: center">
      <div class="glass" style="height: 40px; padding: 0 14px; border-radius: 20px; display: flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 500; box-shadow: 0 4px 14px var(--shadow)">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="var(--brand)" aria-hidden="true"><path d="M12 22s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"></path><circle cx="12" cy="10" r="2.6" fill="#FFFFFF"></circle></svg>Floreasca</div>
      <span style="display: flex; gap: 8px"><a href="Notificari.dc.html" aria-label="Notificări, 2 noi" class="pr" style="position: relative; width: 42px; height: 42px; border-radius: 21px; background: var(--surf); color: var(--ink); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px var(--shadow)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"></path><path d="M10 20a2 2 0 0 0 4 0"></path></svg><span class="pop" style="position: absolute; right: -3px; top: -3px; min-width: 18px; height: 18px; padding: 0 5px; box-sizing: border-box; border-radius: 9px; background: #FF3B30; color: #FFFFFF; font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center; animation-delay: .8s">2</span></a>
      <a href="''' + cont + '''" aria-label="Contul meu" class="pr" style="position: relative; width: 42px; height: 42px; border-radius: 21px; background: var(--surf); color: var(--ink); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; text-decoration: none; box-shadow: 0 4px 14px var(--shadow)">AP<span style="position: absolute; right: -2px; bottom: -2px; width: 14px; height: 14px; border-radius: 7px; background: var(--ok); border: 2.5px solid var(--surf)"></span></a></span>
    </div>
    <a href="Dialog.dc.html" class="pr glass" style="display: flex; align-items: center; gap: 12px; height: 62px; padding: 0 8px 0 18px; border-radius: 31px; color: var(--ink); text-decoration: none; box-shadow: 0 14px 34px var(--shadow)">
      <svg class="glow" width="22" height="22" viewBox="0 0 24 24" fill="var(--brand)" aria-hidden="true"><path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8z"></path></svg>
      <span style="flex-grow: 1; font-size: 18px; font-weight: 500; letter-spacing: -0.3px">Cu ce te ajutăm?</span>
      <span style="width: 46px; height: 46px; border-radius: 23px; background: var(--brand); display: flex; align-items: center; justify-content: center; color: var(--onbrand)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0M12 18v3"></path></svg></span>
    </a>
  </div>''')
    tiles = ''.join('<a href="Dialog.dc.html" class="u d%d pr" style="display: flex; flex-direction: column; align-items: center; gap: 6px; color: var(--ink); text-decoration: none; font-size: 11px; font-weight: 500">'
                    '<span style="width: 100%%; height: 62px; border-radius: 31px; overflow: hidden; display: block"><img src="assets/services/%s.webp" alt="" style="width: 100%%; height: 100%%; object-fit: cover; display: block"></span>%s</a>' % (i + 2, img, lab)
                    for i, (img, lab) in enumerate(SERV))
    tiles += ('<a href="Servicii.dc.html" class="u d6 pr" style="display: flex; flex-direction: column; align-items: center; gap: 6px; color: var(--ink); text-decoration: none; font-size: 11px; font-weight: 500">'
              '<span style="position: relative; width: 100%; height: 62px; border-radius: 31px; background: var(--bsoft); color: var(--btext); display: flex; align-items: center; justify-content: center">' + ic('toate', 26, 'var(--btext)') +
              '<span style="position: absolute; right: -2px; top: -4px; height: 20px; padding: 0 6px; border-radius: 10px; background: var(--brand); color: var(--onbrand); font-size: 10px; font-weight: 700; display: flex; align-items: center">+26</span></span>Alte servicii</a>')
    b.append('''<div class="sheet" style="position: absolute; left: 10px; right: 10px; bottom: 100px; background: var(--glass2); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-radius: 34px; padding: 18px 14px 14px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 -6px 30px var(--shadow); animation-delay: .1s">
    <div class="u d1" style="display: flex; justify-content: space-between; align-items: baseline; padding: 0 4px">
      <span style="font-size: 20px; font-weight: 600; letter-spacing: -0.4px">Populare acum</span>
      <span style="font-size: 13px; color: var(--ink2); display: flex; align-items: center; gap: 6px"><span class="glow" style="width: 8px; height: 8px; border-radius: 4px; background: var(--ok)"></span>12 Jobzeri online</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px">''' + tiles + '''</div>
    ''' + ad_card('earn', S('SchimbaRol.dc.html')) + '''
  </div>''')
    b.append(tabbar('client', 'acasa', {'acasa': S('Acasa.dc.html'), 'activitate': 'Activitate.dc.html', 'mesaje': S('Chat.dc.html') if dark else 'Mesaje.dc.html', 'cont': cont}))
    return page('Acasă (client)', theme, '\n'.join(b), '', ad_logic())


# ---------------------------------------------------------------- Acasă Jobzer (heat map)
def castig(theme):
    dark = theme == 'D'
    S = lambda n: n.replace('.dc.html', 'Dark.dc.html') if dark else n
    css = """
@keyframes notif{from{opacity:0;transform:translateY(-30px) scale(.9)}to{opacity:1;transform:none}}
.notif{animation:notif .8s cubic-bezier(.2,.9,.25,1.1) .6s both}
.heat{transform-box:fill-box;transform-origin:center;animation:heat 3.2s ease-in-out infinite}.h2{animation-delay:1s}.h3{animation-delay:2s}
"""
    logic = """constructor(props) { super(props); this.state = { on: true, ad: true }; }
  renderVals() {
    const s = this.state, on = s.on;
    return {
      on, onAttr: on ? 'true' : 'false', toggle: () => this.setState({ on: !on }),
      goLabel: on ? 'ON' : 'OFF', title: on ? 'Ești online' : 'Ești offline',
      sub: on ? 'Primești cereri pe skill-urile tale, în 5 km' : 'Atinge ca să primești cereri',
      goStyle: 'width: 66px; height: 66px; border-radius: 33px; border: 0; cursor: pointer; font-family: inherit; font-size: 15px; font-weight: 700; flex-shrink: 0; transition: background .3s, color .3s; ' +
        (on ? 'background: var(--brand); color: var(--onbrand); animation: halo 1.6s ease-out infinite;' : 'background: var(--invbg); color: var(--invink);'),
      ad: s.ad, closeAd: () => this.setState({ ad: false }), reopen: () => this.setState({ ad: true }), noAd: !s.ad
    };
  }"""
    b = [('<svg width="390" height="844" viewBox="0 0 390 844" aria-hidden="true" style="position: absolute; left: 0; top: 0; display: block">'
          '<rect width="390" height="844" style="fill: var(--land)"></rect>'
          '<path d="M-10 470 C 80 440 170 500 270 465 S 400 450 400 450 L400 560 L-10 560 Z" style="fill: var(--water)"></path>'
          '<path d="M-10 130 L400 90 M-10 330 L400 370 M120 -10 L92 860 M282 -10 L312 860 M-10 600 L400 620" stroke-width="16" stroke-linecap="round" fill="none" style="stroke: var(--road)"></path>'
          '<path d="M-10 230 L400 245 M200 -10 L188 860" stroke-width="7" fill="none" style="stroke: var(--road)"></path>'
          '<circle class="heat" cx="110" cy="270" r="80" fill="#FF9F0A" fill-opacity="0.22"></circle><circle class="heat h2" cx="292" cy="380" r="62" fill="#FF9F0A" fill-opacity="0.3"></circle>'
          '<circle class="heat h3" cx="236" cy="190" r="44" fill="#FF9F0A" fill-opacity="0.16"></circle>'
          '<circle cx="196" cy="306" r="10" style="fill: var(--invbg); stroke: var(--surf)" stroke-width="4"></circle></svg>')]
    b.append('<span style="position: absolute; left: 70px; top: 262px; font-size: 12px; font-weight: 600; color: var(--btext)">Cerere mare</span><span style="position: absolute; left: 262px; top: 374px; font-size: 12px; font-weight: 600; color: var(--btext)">Herăstrău</span>')
    b.append('''<div style="position: absolute; left: 16px; right: 16px; top: 52px; display: flex; justify-content: space-between; align-items: center">
    <a href="ContJobzer.dc.html" aria-label="Profilul meu" class="pr" style="position: relative; width: 44px; height: 44px; border-radius: 22px; display: block; box-shadow: 0 4px 14px var(--shadow)"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 44px; height: 44px; border-radius: 22px; object-fit: cover; display: block; border: 2px solid var(--surf); box-sizing: border-box"><span style="position: absolute; right: -2px; bottom: -2px; width: 14px; height: 14px; border-radius: 7px; background: var(--brand); border: 2.5px solid var(--surf)"></span></a>
    <a href="Incasari.dc.html" class="pr" style="height: 44px; padding: 0 18px; border-radius: 22px; background: var(--invbg); color: var(--invink); display: flex; align-items: center; font-size: 19px; font-weight: 600; letter-spacing: -0.4px; text-decoration: none">264 lei azi</a>
    <a href="Promovare.dc.html" aria-label="Promovare" class="pr" style="width: 44px; height: 44px; border-radius: 22px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z"></path></svg></a>
  </div>
  <sc-if value="{{on}}" hint-placeholder-val="{{ true }}">
    <a href="OfertaRapida.dc.html" class="notif pr glass" style="position: absolute; left: 12px; right: 12px; top: 110px; display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 28px; color: var(--ink); text-decoration: none; box-shadow: 0 14px 34px var(--shadow)">
      <img src="assets/services/service-mobila.webp" alt="" style="width: 44px; height: 44px; border-radius: 22px; object-fit: cover; flex-shrink: 0">
      <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="display: flex; justify-content: space-between"><span style="font-size: 15px; font-weight: 500">Cerere nouă · montaj mobilier</span><span style="font-size: 12px; color: var(--ink2)">acum</span></span><span style="font-size: 14px; color: var(--ink2)">Estimare 120–220 lei · 2,1 km · 98% potrivire</span></span>
    </a>
  </sc-if>
  <div class="sheet" style="position: absolute; left: 10px; right: 10px; bottom: 100px; background: var(--glass2); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border-radius: 34px; padding: 16px 14px 14px; display: flex; flex-direction: column; gap: 14px; box-shadow: 0 -6px 30px var(--shadow)">
    <div class="u d1" style="display: flex; align-items: center; gap: 14px">
      <button type="button" onClick="{{toggle}}" aria-pressed="{{onAttr}}" aria-label="Online" class="pr" style="{{goStyle}}">{{goLabel}}</button>
      <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 20px; font-weight: 600; letter-spacing: -0.4px">{{title}}</span><span style="font-size: 13px; color: var(--ink2)">{{sub}}</span></span>
    </div>
    <div class="u d2" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">
      <a href="Statistici.dc.html" class="pr" style="background: var(--surf2); border-radius: 20px; padding: 12px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 18px; font-weight: 600">78 lei/h</span><span style="font-size: 12px; color: var(--ink2)">statistici ›</span></a>
      <a href="Niveluri.dc.html" class="pr" style="background: var(--surf2); border-radius: 20px; padding: 12px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 18px; font-weight: 600">Plus</span><span style="font-size: 12px; color: var(--ink2)">38/50 → Gold</span></a>
      <a href="Promovare.dc.html" class="pr" style="background: var(--bsoft); border-radius: 20px; padding: 12px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 18px; font-weight: 600">1 h 20</span><span style="font-size: 12px; color: var(--btext); font-weight: 500">promovat</span></a>
    </div>
    ''' + ad_card('order', S('SchimbaRol.dc.html')) + '''
  </div>''')
    b.append(tabbar('jobzer', 'acasa', {'acasa': S('Castig.dc.html'), 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'}))
    return page('Acasă Jobzer', theme, '\n'.join(b), css, logic)


# ---------------------------------------------------------------- Cont (client) and Profil (Jobzer)
def row(href, color, icon_svg, label, value='', first=False):
    return ('<a href="%s" class="pr" style="display: flex; align-items: center; gap: 12px; padding: 11px 16px 11px 0; margin-left: 16px; %s color: var(--ink); text-decoration: none">'
            '<span style="width: 30px; height: 30px; border-radius: 9px; background: %s; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex-shrink: 0">%s</span>'
            '<span style="flex-grow: 1; font-size: 16px">%s</span>%s%s</a>') % (
        href, '' if first else 'border-top: 0.5px solid var(--sep);', color, icon_svg, label,
        ('<span style="font-size: 15px; color: var(--ink2)">%s</span>' % value) if value else '', CHEV)


def role_switch(active, href):
    c_on = active == 'client'
    pill = lambda on, t: ('<span style="flex: 1; height: 34px; border-radius: 17px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 500; %s">%s</span>'
                          % ('background: var(--surf); color: var(--ink); box-shadow: 0 3px 10px var(--shadow)' if on else 'color: var(--ink2)', t))
    return ('<a href="%s" class="pr" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--ink); padding-top: 12px; border-top: 0.5px solid var(--sep)">'
            '<span style="font-size: 14px; color: var(--ink2); flex-shrink: 0">Rol activ</span>'
            '<span style="flex-grow: 1; display: flex; padding: 3px; border-radius: 20px; background: var(--surf2)">%s%s</span></a>') % (href, pill(c_on, 'Client'), pill(not c_on, 'Jobzer'))


I_CARD = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="3"></rect><path d="M3 10h18"></path></svg>'
I_HEART = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"></path></svg>'
I_PIN = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 22s-7-6.2-7-12a7 7 0 0 1 14 0c0 5.8-7 12-7 12z"></path></svg>'
I_GIFT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="9" width="18" height="12" rx="2"></rect><path d="M12 9v12M3 13h18M12 9c-2-4-6-4-6-1s6 1 6 1 6 2 6-1-4-3-6 1"></path></svg>'
I_GEAR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"></circle><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"></path></svg>'


I_DOC2 = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h9l4 4v14H6z"></path><path d="M9 12h7M9 16h7"></path></svg>'
I_REP = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12a8 8 0 0 1 14-5.3L20 9M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15M4 20v-5h5"></path></svg>'
I_CAL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="16" height="15" rx="4"></rect><path d="M4 10h16M9 3v4M15 3v4"></path></svg>'


def cont():
    b = '''<div style="padding: 60px 16px 0; display: flex; flex-direction: column; gap: 14px">
  <h1 class="u" style="margin: 0 4px; font-size: 34px; font-weight: 600; letter-spacing: -0.9px">Cont</h1>
  <div class="u d1" style="background: var(--surf); border-radius: 26px; padding: 14px 16px; display: flex; flex-direction: column; gap: 12px">
    <a href="#profil" style="display: flex; align-items: center; gap: 14px; color: var(--ink); text-decoration: none">
      <span class="pop" style="width: 58px; height: 58px; border-radius: 29px; background: var(--bsoft2); color: var(--btext); display: flex; align-items: center; justify-content: center; font-size: 21px; font-weight: 600">AP</span>
      <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 20px; font-weight: 500">Andrei P.</span><span style="font-size: 14px; color: var(--ink2)">★ 4,9 ca client · 12 cereri</span></span>''' + CHEV + '''
    </a>
    ''' + role_switch('client', 'SchimbaRol.dc.html') + '''
  </div>
  <div class="u d2">''' + ad_card('earn', 'SchimbaRol.dc.html') + '''</div>
  <div class="u d3" style="background: var(--surf); border-radius: 26px; overflow: hidden">
    ''' + row('#plati', '#34C759', I_CARD, 'Plăți și carduri', first=True) + row('Chitante.dc.html', '#007AFF', I_DOC2, 'Chitanțe și facturi') + row('Recurente.dc.html', '#5856D6', I_REP, 'Cereri recurente', '1') + row('#favoriti', '#FF2D55', I_HEART, 'Jobzeri favoriți', '2') + row('#invita', '#FF9F0A', I_GIFT, 'Invită prieteni') + row('#setari', '#8E8E93', I_GEAR, 'Setări, temă și siguranță') + '''
  </div>
</div>
''' + tabbar('client', 'cont', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'})
    return page('Cont (client)', 'L', b, '', ad_logic())


def cont_jobzer():
    I_STAR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"></path></svg>'
    I_BOLT = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z"></path></svg>'
    I_DOC = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h9l4 4v14H6z"></path><path d="M9 12h7M9 16h7"></path></svg>'
    I_TOOL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6a4 4 0 0 0-5 5l-6 6 3 3 6-6a4 4 0 0 0 5-5l-2 2-3-1-1-3z"></path></svg>'
    b = '''<div style="padding: 60px 16px 0; display: flex; flex-direction: column; gap: 14px">
  <h1 class="u" style="margin: 0 4px; font-size: 34px; font-weight: 600; letter-spacing: -0.9px">Profil</h1>
  <div class="u d1" style="background: var(--surf); border-radius: 26px; padding: 14px 16px; display: flex; flex-direction: column; gap: 12px">
    <a href="Profil.dc.html" style="display: flex; align-items: center; gap: 14px; color: var(--ink); text-decoration: none">
      <span class="pop" style="position: relative; width: 60px; height: 60px; flex-shrink: 0"><img src="assets/people/person-jobzer-3.webp" alt="" style="width: 60px; height: 60px; border-radius: 30px; object-fit: cover; display: block">
        <span style="position: absolute; right: -2px; bottom: -2px; width: 22px; height: 22px; border-radius: 11px; background: var(--ok); color: #FFFFFF; display: flex; align-items: center; justify-content: center; border: 2px solid var(--surf)">''' + CHECK.replace('width="14" height="14"', 'width="11" height="11"') + '''</span></span>
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; align-items: center; gap: 8px; font-size: 20px; font-weight: 500">Mihai I. <span style="height: 22px; padding: 0 8px; border-radius: 11px; background: linear-gradient(135deg, #F7D774, #D4A017); color: #3B2A00; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center">GOLD</span></span><span style="font-size: 14px; color: var(--ink2)">4,9 ★ · 86 sarcini · PFA</span></span>''' + CHEV + '''
    </a>
    ''' + role_switch('jobzer', 'SchimbaRol.dc.html') + '''
  </div>
  <div class="u d2">''' + ad_card('order', 'SchimbaRol.dc.html') + '''</div>
  <div class="u d3" style="background: var(--surf); border-radius: 26px; overflow: hidden">
    ''' + row('ProfilEdit.dc.html', '#FF9F0A', I_TOOL, 'Skill-uri, prețuri, portofoliu', '6', True) + row('GearHub.dc.html', '#FF9F0A', I_TOOL, 'Gear & Growth · trusă, haine, cărți de vizită', 'nou') + row('Promovare.dc.html', '#FF2D55', I_BOLT, 'Promovare', 'activă') + row('Disponibilitate.dc.html', '#5856D6', I_CAL, 'Program și zonă', '5 km') + row('Facturi.dc.html', '#34C759', I_DOC, 'Facturi și plăți', '412 lei') + row('Niveluri.dc.html', '#D4A017', I_STAR, 'Nivel și beneficii', 'Gold') + row('#setari', '#8E8E93', I_GEAR, 'Setări, temă și siguranță') + '''
  </div>
</div>
''' + tabbar('jobzer', 'cont', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})
    return page('Profil (Jobzer)', 'L', b, '', ad_logic())



# ---------------------------------------------------------------- Fișa cererii (fără buget: doar estimare)
def fisa():
    css = """
.seg3{display:grid;gap:6px;padding:5px;border-radius:26px;background:var(--surf3)}
.o3{border:0;border-radius:21px;background:transparent;font-family:inherit;color:var(--ink2);cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;transition:background .3s, color .3s, transform .35s cubic-bezier(.2,.9,.3,1.4), box-shadow .3s}
.o3 b{font-size:15px;font-weight:600}.o3 small{font-size:11px;font-weight:500}
.o3[aria-pressed="true"]{background:var(--surf);color:var(--ink);box-shadow:0 4px 14px var(--shadow);transform:scale(1.02)}
.o3.urg[aria-pressed="true"]{background:var(--brand);color:var(--onbrand)}
.chip{border:0;height:36px;padding:0 14px;border-radius:18px;background:var(--surf2);font:500 14px/1 inherit;font-family:inherit;color:var(--ink);cursor:pointer;transition:all .25s}
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
    lab = lambda t: ('<span style="display: flex; justify-content: space-between; align-items: center; padding: 0 12px"><span style="font-size: 13px; font-weight: 500; color: var(--ink2); text-transform: uppercase; letter-spacing: .3px">' + t + '</span>'
                     '<span style="font-size: 12px; font-weight: 500; color: var(--oktext)">✓ din conversația cu Jobzee</span></span>')
    b = '''<div style="padding: 52px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
  <div style="display: flex; align-items: center; justify-content: space-between">
    <a href="Dialog.dc.html" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; color: var(--ink2)"><img src="assets/mascot/zee-fericit.png" alt="" style="width: 26px; height: 28px">Pregătită împreună cu Jobzee</span>
    <a href="Dialog.dc.html" class="pr" style="height: 40px; padding: 0 14px; border-radius: 20px; background: var(--surf); display: flex; align-items: center; font-size: 15px; font-weight: 500; text-decoration: none">Modifică</a>
  </div>
  <h1 class="u" style="margin: 0 4px; font-size: 32px; font-weight: 600; letter-spacing: -0.8px">Fișa cererii</h1>

  <div class="u d1" style="background: var(--surf); border-radius: 26px; padding: 10px 14px 10px 10px; display: flex; align-items: center; gap: 12px">
    <img src="assets/services/service-mobila.webp" alt="" style="width: 56px; height: 56px; border-radius: 28px; object-fit: cover; flex-shrink: 0">
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 17px; font-weight: 500">Montaj birou + dulap mic</span><span style="font-size: 13px; color: var(--ink2)">Montaj mobilier · 2 poze · ~1 h 30 · unelte aduse</span></span>
    <a href="CerereMultipla.dc.html" class="pr" style="height: 30px; padding: 0 10px; border-radius: 15px; background: var(--bsoft); color: var(--btext); font-size: 13px; font-weight: 500; text-decoration: none; display: flex; align-items: center; white-space: nowrap; flex-shrink: 0">+ serviciu</a>
  </div>

  ''' + lab('Când') + '''
  <div class="seg3 u d2" style="grid-template-columns: repeat(3, minmax(0, 1fr))">
    <button type="button" class="o3 urg" onClick="{{setU}}" aria-pressed="{{wU}}" style="height: 56px"><b><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="vertical-align: -2px"><path d="M13 2L4 14h7l-1 8 9-12h-7z"></path></svg> Urgent</b><small>în ~60 min</small></button>
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
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 500">Str. Barbu Văcărescu 120</span><span style="font-size: 12px; color: var(--ink2)">Floreasca · detectată acum · ap. 14, et. 3</span></span>
      <a href="Adresa.dc.html" style="font-size: 14px; font-weight: 500; text-decoration: none">Ajustează</a>
    </div>
  </sc-if>
  <sc-if value="{{isO}}" hint-placeholder-val="{{ false }}">
    <a href="Adresa.dc.html" class="u pr" style="display: flex; align-items: center; gap: 12px; padding: 14px; border-radius: 22px; background: var(--surf); color: var(--ink); text-decoration: none; box-shadow: inset 0 0 0 2px var(--brand)"><span style="width: 34px; height: 34px; border-radius: 17px; background: var(--bsoft); color: var(--btext); display: flex; align-items: center; justify-content: center">''' + plus + '''</span><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 500">Definește adresa</span><span style="font-size: 12px; color: var(--ink2)">Caut-o sau pune pinul pe hartă</span></span>''' + CHEV + '''</a>
  </sc-if>

  <div class="u d4" style="background: var(--surf); border-radius: 26px; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px">
    <span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 15px; font-weight: 500">Estimare generală</span><span style="font-size: 12px; color: var(--ink2)">montaj mobilier · zona ta</span></span>
    <span style="font-size: 30px; font-weight: 600; letter-spacing: -0.8px">120 – 220 <span style="font-size: 17px; color: var(--ink2)">lei</span></span>
    <span style="position: relative; height: 8px; border-radius: 4px; background: linear-gradient(90deg, #34C759, #FF9F0A 60%, #FF6B3D)"><span style="position: absolute; left: 40%; top: -4px; width: 16px; height: 16px; border-radius: 8px; background: var(--surf); box-shadow: 0 0 0 3px var(--ink), 0 2px 6px var(--shadow); margin-left: -8px; animation: mark 1s cubic-bezier(.2,.8,.2,1) .5s both"></span></span>
    <span style="font-size: 13px; line-height: 1.4; color: var(--ink2)">Nu setezi un preț. <b style="color: var(--ink)">Jobzerii îți trimit oferte</b>, iar tu o alegi pe cea potrivită. Taxa Jobzee de 15% se adaugă peste oferta aleasă.</span>
  </div>

  <div style="flex-grow: 1"></div>
  <a href="ContTrimitere.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.35)">{{cta}}</a>
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
    H = 1240
    css = """
.fc{border:0;height:34px;padding:0 11px;border-radius:17px;background:var(--surf);font-family:inherit;font-size:13px;font-weight:500;color:var(--ink);cursor:pointer;transition:all .25s;box-shadow:0 1px 0 var(--sep)}
.fc[aria-pressed="true"]{background:var(--invbg);color:var(--invink)}
.tile{display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none;color:var(--ink);font-size:11px;font-weight:500;text-align:center;line-height:1.2}
.tile .pic{width:100%;aspect-ratio:1;border-radius:30%;overflow:hidden;background-size:cover;background-position:center;position:relative;box-shadow:0 6px 16px var(--shadow)}
"""
    data = json.dumps([{'n': n, 'g': g, 'p': p, 'i': i} for n, g, p, i in FAMILIES], ensure_ascii=False)
    logic = ("""constructor(props) { super(props); this.state = { g: 'all' }; }
  renderVals() {
    const all = """ + data + """;
    const g = this.state.g;
    const tint = { casa: '#E8F4FF', rep: '#FFF4E5', pers: '#FCEBF1', alt: '#EEF8EA' };
    const items = all.filter(x => g === 'all' || x.g === g).map(x => ({
      name: x.n,
      picStyle: 'background-image: url(assets/cat/' + x.i + '.svg)',
      icStyle: 'display: none'
    }));
    const f = (k) => ({ attr: g === k ? 'true' : 'false', pick: () => this.setState({ g: k }) });
    return { items, count: items.length, fAll: f('all'), fCasa: f('casa'), fRep: f('rep'), fPers: f('pers'), fAlt: f('alt') };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 14px">
  <div style="display: flex; align-items: center; justify-content: space-between">
    <a href="Acasa.dc.html" aria-label="Înapoi" class="pr glass" style="width: 40px; height: 40px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: var(--ink); box-shadow: 0 4px 14px var(--shadow)">''' + BACK + '''</a>
    <span style="font-size: 13px; font-weight: 500; color: var(--ink2)">{{count}} familii de servicii</span>
  </div>
  <div class="u" style="display: flex; align-items: flex-end; justify-content: space-between">
    <h1 style="margin: 0 4px; font-size: 34px; line-height: 1.05; font-weight: 600; letter-spacing: -0.9px">Toate<br>serviciile</h1>
    <img class="float" src="assets/mascot/zee-cauta.png" alt="" style="width: 86px; height: 92px; margin-right: 6px">
  </div>
  <a href="Dialog.dc.html" class="u d1 pr" style="display: flex; align-items: center; gap: 10px; height: 50px; padding: 0 16px; border-radius: 25px; background: var(--surf); color: var(--ink2); text-decoration: none; font-size: 16px; box-shadow: 0 4px 14px var(--shadow)">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-3.5-3.5"></path></svg>Caută: „robinet”, „TV pe perete”…</a>
  <div class="u d2" style="display: flex; gap: 6px; flex-wrap: wrap">
    <button type="button" class="fc" onClick="{{fAll.pick}}" aria-pressed="{{fAll.attr}}">Toate</button>
    <button type="button" class="fc" onClick="{{fCasa.pick}}" aria-pressed="{{fCasa.attr}}">Casă</button>
    <button type="button" class="fc" onClick="{{fRep.pick}}" aria-pressed="{{fRep.attr}}">Reparații</button>
    <button type="button" class="fc" onClick="{{fPers.pick}}" aria-pressed="{{fPers.attr}}">Persoane</button>
    <button type="button" class="fc" onClick="{{fAlt.pick}}" aria-pressed="{{fAlt.attr}}">Altele</button>
  </div>
  <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 14px 8px; padding: 4px 0">
    <sc-for list="{{items}}" as="x" hint-placeholder-count="30">
      <a href="Dialog.dc.html" class="tile pr pop"><span class="pic" style="{{x.picStyle}}"><span style="{{x.icStyle}}"></span></span>{{x.name}}</a>
    </sc-for>
  </div>
  <a href="Dialog.dc.html" class="pr" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 26px; background: var(--bsoft); color: var(--ink); text-decoration: none">
    <img src="assets/mascot/zee-gandeste.png" alt="" style="width: 48px; height: 52px; flex-shrink: 0">
    <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">Nu găsești ce cauți?</span><span style="font-size: 13px; color: var(--ink2)">Spune-i lui Jobzee de ce ai nevoie și îți găsește categoria potrivită.</span></span>''' + CHEV + '''</a>
</div>
''' + tabbar('client', 'acasa', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'})
    return page('Toate serviciile', 'L', b, css, logic, h=H)



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
.jsw{width:51px;height:31px;border-radius:16px;border:0;padding:2px;cursor:pointer;flex-shrink:0;position:relative;transition:background .25s}.jsw::after{content:"";position:absolute;top:2px;left:2px;width:27px;height:27px;border-radius:14px;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,.2);transition:transform .3s cubic-bezier(.3,1.3,.4,1)}.jsw[aria-pressed="true"]{background:var(--ok)}.jsw[aria-pressed="true"]::after{transform:translateX(20px)}.jsw[aria-pressed="false"]{background:var(--surf3)}
.row{display:flex;align-items:center;gap:8px;padding:7px 4px;transition:transform .5s cubic-bezier(.2,.9,.3,1.2)}
"""
    J = [
        dict(n='Mihai I.', img='people/person-jobzer-3', tier='Gold', eta=6, m=98, sk='Montaj mobilier · IKEA', a=-40, show=1, offer=150, at=5),
        dict(n='Ana D.', img='people/person-jobzer-2', tier='Plus', eta=14, m=84, sk='Montaj · curățenie', a=200, show=2, offer=120, at=7),
        dict(n='Radu C.', img='people/person-jobzer-1', tier='Gold', eta=4, m=95, sk='Montaj · electrice', a=110, show=3, offer=170, at=9),
        dict(n='Elena P.', img='people/person-client-1', tier='Start', eta=11, m=80, sk='Montaj mobilier', a=300, show=4, offer=135, at=12),
        dict(n='Andrei M.', img='people/person-client-3', tier='Plus', eta=18, m=76, sk='Tâmplărie · montaj', a=235, show=6, offer=0, at=99),
    ]
    logic = ("""constructor(props) { super(props); this.state = { t: 0, sort: 'eta', notif: 'ask', auto: false }; }
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
      askNotif: this.state.notif === 'ask', notifOn: this.state.notif === 'on',
      allowNotif: () => this.setState({ notif: 'on' }), skipNotif: () => this.setState({ notif: 'no' }),
      autoAttr: this.state.auto ? 'true' : 'false', toggleAuto: () => this.setState({ auto: !this.state.auto }),
      autoTxt: this.state.auto ? 'Activ: alegem prima ofertă Gold sub 160 lei' : 'Alege automat prima ofertă Gold sub 160 lei',
      zee: offers >= 3 ? 'assets/mascot/zee-fericit.png' : (offers > 0 ? 'assets/mascot/zee-potrivire.png' : 'assets/mascot/zee-cauta.png'),
      status: offers === 0 ? 'Jobzerii văd cererea și pregătesc oferte' : (offers === 1 ? 'Prima ofertă a sosit' : offers + ' oferte primite până acum'),
      elapsed: mm + ':' + (ss < 10 ? '0' + ss : ss),
      cta: 'Vezi ofertele (' + offers + ')',
      bar: 'display: block; height: 100%; border-radius: 3px; background: var(--brand); transition: width .6s; width: ' + Math.min(100, offers * 25) + '%'
    };
  }""")
    nxt = 'OferteDark.dc.html' if dark else 'Oferte.dc.html'
    rings = ''.join('<span class="ring" style="left: %dpx; top: %dpx; width: %dpx; height: %dpx"></span><span style="position: absolute; left: %dpx; top: %dpx; font-size: 10px; font-weight: 500; color: var(--ink2); background: var(--land); padding: 0 4px; border-radius: 6px">%d min</span>'
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
      <span style="position: absolute; left: 50%; bottom: -10px; transform: translateX(-50%); height: 18px; padding: 0 6px; border-radius: 9px; background: var(--invbg); color: var(--invink); font-size: 10px; font-weight: 500; white-space: nowrap; display: flex; align-items: center">{{p.eta}}</span>
      <span class="pop" style="{{p.priceStyle}}; position: absolute; left: 36px; top: -12px; height: 22px; padding: 0 8px; border-radius: 11px; background: var(--brand); color: var(--onbrand); font-size: 12px; font-weight: 500; white-space: nowrap; align-items: center; box-shadow: 0 4px 12px rgba(255,159,10,0.4)">{{p.price}}</span>
    </span>
  </sc-for>

  <div style="position: absolute; left: 16px; right: 16px; top: 54px; display: flex; flex-direction: column; gap: 10px">
    <div class="glass u" style="display: flex; align-items: center; gap: 10px; padding: 6px 14px 6px 6px; border-radius: 26px; box-shadow: 0 8px 24px var(--shadow)">
      <a href="Fisa.dc.html" aria-label="Înapoi la fișă" class="pr" style="width: 40px; height: 40px; border-radius: 20px; background: var(--surf2); color: var(--ink); display: flex; align-items: center; justify-content: center">''' + BACK + '''</a>
      <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="display: flex; align-items: center; gap: 6px; font-size: 16px; font-weight: 500"><span class="glow" style="width: 8px; height: 8px; border-radius: 4px; background: #FF3B30"></span>Radar live</span><span style="font-size: 12px; color: var(--ink2)">Montaj mobilier · Urgent · rază 5 km</span></span>
      <span style="font-size: 15px; font-weight: 500; color: var(--ink2); font-variant-numeric: tabular-nums">{{elapsed}}</span>
    </div>
    <div class="u d1" style="display: flex; gap: 6px">
      <button type="button" class="srt" onClick="{{sEta.pick}}" aria-pressed="{{sEta.attr}}">Cel mai rapid</button>
      <button type="button" class="srt" onClick="{{sSkill.pick}}" aria-pressed="{{sSkill.attr}}">Potrivire skill</button>
      <button type="button" class="srt" onClick="{{sPret.pick}}" aria-pressed="{{sPret.attr}}">Preț ofertă</button>
    </div>
  </div>

  <sc-if value="{{askNotif}}" hint-placeholder-val="{{ true }}">
    <div class="glass pop" style="position: absolute; left: 16px; right: 16px; top: 160px; display: flex; align-items: center; gap: 10px; padding: 10px 10px 10px 14px; border-radius: 22px; box-shadow: 0 10px 28px var(--shadow); animation-delay: 1.2s">
      <span style="width: 34px; height: 34px; border-radius: 17px; background: var(--bsoft); color: var(--btext); display: flex; align-items: center; justify-content: center; flex-shrink: 0"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"></path><path d="M10 20a2 2 0 0 0 4 0"></path></svg></span>
      <span style="flex-grow: 1; font-size: 14px; line-height: 1.3">Te anunțăm când vin ofertele, chiar dacă închizi app-ul?</span>
      <button type="button" onClick="{{allowNotif}}" class="pr" style="border: 0; height: 32px; padding: 0 12px; border-radius: 16px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 13px; font-weight: 500; cursor: pointer">Da</button>
      <button type="button" onClick="{{skipNotif}}" aria-label="Nu acum" class="pr" style="border: 0; width: 28px; height: 28px; border-radius: 14px; background: var(--surf2); color: var(--ink2); display: flex; align-items: center; justify-content: center; cursor: pointer; padding: 0"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg></button>
    </div>
  </sc-if>
  <sc-if value="{{notifOn}}" hint-placeholder-val="{{ false }}">
    <div class="glass pop" style="position: absolute; left: 0; right: 0; margin: 0 auto; width: max-content; top: 160px; display: flex; align-items: center; gap: 8px; height: 36px; padding: 0 14px; border-radius: 18px; font-size: 13px; font-weight: 500; box-shadow: 0 8px 20px var(--shadow)"><span style="color: var(--oktext)">✓</span>Notificări pornite pentru această cerere</div>
  </sc-if>
  <div class="sheet" style="position: absolute; left: 8px; right: 8px; bottom: 8px; background: var(--glass2); backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px); border-radius: 38px; padding: 10px 14px 16px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 -10px 40px var(--shadow)">
    <span style="align-self: center; width: 38px; height: 5px; border-radius: 3px; background: var(--ink3)"></span>
    <div style="display: flex; align-items: center; gap: 10px; padding: 0 4px">
      <img src="{{zee}}" alt="" class="float" style="width: 40px; height: 43px; flex-shrink: 0">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 18px; font-weight: 500; letter-spacing: -0.3px">{{found}} Jobzeri găsiți · {{offers}} oferte</span><span style="font-size: 13px; color: var(--ink2)">{{status}}</span></span>
    </div>
    <span style="height: 5px; border-radius: 3px; background: var(--surf3); overflow: hidden; margin: 0 4px"><span style="{{bar}}"></span></span>
    <div style="display: flex; flex-direction: column">
      <sc-for list="{{rows}}" as="r" hint-placeholder-count="3">
        <div class="row" style="{{r.sep}}">
          <img src="{{r.img}}" alt="" style="width: 44px; height: 44px; border-radius: 22px; object-fit: cover; flex-shrink: 0">
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px">
            <span style="display: flex; align-items: center; gap: 6px; font-size: 15px; font-weight: 500">{{r.n}}<span style="height: 18px; padding: 0 6px; border-radius: 9px; background: var(--bsoft); color: var(--btext); font-size: 10px; font-weight: 500; display: inline-flex; align-items: center">{{r.tier}}</span></span>
            <span style="font-size: 12px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{r.eta}} · {{r.m}} potrivire · {{r.sk}}</span>
          </span>
          <sc-if value="{{r.isOff}}" hint-placeholder-val="{{ true }}"><span class="pop" style="display: flex; flex-direction: column; align-items: flex-end; gap: 3px"><span style="font-size: 16px; font-weight: 500; font-variant-numeric: tabular-nums; white-space: nowrap">{{r.price}}</span><a href="Plata.dc.html" class="pr" style="height: 24px; padding: 0 10px; border-radius: 12px; background: var(--brand); color: var(--onbrand); font-size: 12px; font-weight: 500; text-decoration: none; display: flex; align-items: center">Alege</a></span></sc-if>
          <sc-if value="{{r.notOff}}" hint-placeholder-val="{{ false }}"><span class="typing" style="display: flex; align-items: center; gap: 4px; font-size: 12px; color: var(--ink2); white-space: nowrap"><span></span><span></span><span></span></span></sc-if>
        </div>
      </sc-for>
    </div>
    <div style="display: flex; align-items: center; gap: 10px; padding: 8px 10px 8px 12px; border-radius: 18px; background: var(--surf2)">
      <span style="flex-grow: 1; display: flex; flex-direction: column; gap: 1px"><span style="font-size: 14px; font-weight: 500">{{autoTxt}}</span><span style="font-size: 11px; color: var(--ink2)">Prețurile sunt ofertele Jobzerilor · +15% taxă Jobzee</span></span>
      <button type="button" onClick="{{toggleAuto}}" aria-pressed="{{autoAttr}}" aria-label="Alegere automată" class="jsw"></button>
    </div>
    <sc-if value="{{hasOffers}}" hint-placeholder-val="{{ true }}">
      <a href="''' + nxt + '''" class="pr" style="display: flex; align-items: center; justify-content: center; height: 54px; border-radius: 27px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">{{cta}}</a>
    </sc-if>
    <sc-if value="{{noOffers}}" hint-placeholder-val="{{ false }}">
      <a href="FaraOferte.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 54px; border-radius: 27px; background: var(--surf3); color: var(--ink2); font-size: 16px; font-weight: 500; text-decoration: none">Aștept ofertele… · Opțiuni</a>
    </sc-if>
  </div>''')
    return page('Radar live', theme, b, css, logic)



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
    <img class="pop" src="assets/mascot/zee-card-bravo.png" alt="" style="width: 92px; height: auto; border-radius: 18px; background: #FBF1E3; flex-shrink: 0">
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
        dict(g='Ieri', k='cereri', img='people/person-client-1', t='Elena P. a terminat curățenia', s='Lasă-i o notă. Îi ajută pe ceilalți clienți.', time='ieri', href='Recenzie.dc.html', cta='Evaluează', unread=False),
        dict(g='Ieri', k='plati', img='', ic='verificat', t='Chitanța pentru curățenie e gata', s='138,00 lei · PDF', time='ieri', href='Chitante.dc.html', cta='Vezi chitanța', unread=False),
        dict(g='Săptămâna asta', k='noutati', img='', ic='rapid', t='Nou: cereri recurente', s='Curățenie în fiecare săptămână, cu același Jobzer', time='luni', href='Recurente.dc.html', cta='Încearcă', unread=False),
    ]
    logic = ("""constructor(props) { super(props); this.state = { f: 'all', read: false }; }
  renderVals() {
    const all = """ + json.dumps(data, ensure_ascii=False) + """;
    const f = this.state.f, read = this.state.read;
    const list = all.filter(n => f === 'all' || n.k === f);
    const items = []; let last = '';
    list.forEach(n => { const head = n.g !== last; last = n.g;
      items.push({ head: n.g, headStyle: head ? 'display: block; padding: 14px 16px 6px; font-size: 13px; font-weight: 500; color: var(--ink2); text-transform: uppercase; letter-spacing: .3px; background: var(--bg)' : 'display: none', t: n.t, s: n.s, time: n.time, href: n.href, cta: n.cta, ctaStyle: n.cta ? 'align-self: flex-start; margin-top: 4px; height: 28px; padding: 0 12px; border-radius: 14px; background: var(--bsoft); color: var(--btext); font-size: 13px; font-weight: 500; display: flex; align-items: center' : 'display: none',
        picStyle: n.img ? 'background: url(assets/' + n.img + '.webp) center/cover' : 'background: var(--bsoft)',
        icStyle: n.img ? 'display: none' : 'width: 22px; height: 22px; background: var(--btext); -webkit-mask: url(assets/icons/icon-' + n.ic + '.svg) center/contain no-repeat; mask: url(assets/icons/icon-' + n.ic + '.svg) center/contain no-repeat',
        dot: n.unread && !read ? 'width: 9px; height: 9px; border-radius: 5px; background: var(--brand); flex-shrink: 0' : 'display: none' }); });
    const unread = read ? 0 : all.filter(n => n.unread).length;
    const s = k => ({ attr: f === k ? 'true' : 'false', pick: () => this.setState({ f: k }) });
    return { items, unread, hasUnread: unread > 0, markAll: () => this.setState({ read: true }), fA: s('all'), fC: s('cereri'), fP: s('plati'), fN: s('noutati') };
  }""")
    b = '''<div style="padding: 56px 16px 0; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('Acasa.dc.html', '<sc-if value="{{hasUnread}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{markAll}}" class="pr" style="border: 0; height: 36px; padding: 0 14px; border-radius: 18px; background: var(--surf); font-family: inherit; font-size: 14px; font-weight: 500; color: var(--btext); cursor: pointer">Citește tot ({{unread}})</button></sc-if>') + '''
  ''' + h1('Notificări') + '''
  <div class="sg u d1" style="grid-template-columns: repeat(4, minmax(0, 1fr))">
    <button type="button" onClick="{{fA.pick}}" aria-pressed="{{fA.attr}}">Toate</button><button type="button" onClick="{{fC.pick}}" aria-pressed="{{fC.attr}}">Cereri</button><button type="button" onClick="{{fP.pick}}" aria-pressed="{{fP.attr}}">Plăți</button><button type="button" onClick="{{fN.pick}}" aria-pressed="{{fN.attr}}">Noutăți</button>
  </div>
  <div class="grp u d2" style="background: transparent">
    <sc-for list="{{items}}" as="n" hint-placeholder-count="6">
      <div><span style="{{n.headStyle}}">{{n.head}}</span>
        <a href="{{n.href}}" class="pr" style="display: flex; align-items: flex-start; gap: 12px; padding: 12px 14px; margin-bottom: 1px; background: var(--surf); color: var(--ink); text-decoration: none; border-radius: 18px">
          <span style="{{n.picStyle}}; width: 42px; height: 42px; border-radius: 21px; flex-shrink: 0; display: flex; align-items: center; justify-content: center"><span style="{{n.icStyle}}"></span></span>
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; justify-content: space-between; gap: 8px"><span style="font-size: 15px; font-weight: 500">{{n.t}}</span><span style="font-size: 12px; color: var(--ink2); white-space: nowrap">{{n.time}}</span></span>
            <span style="font-size: 13px; color: var(--ink2)">{{n.s}}</span>
            <span style="{{n.ctaStyle}}">{{n.cta}}</span></span>
          <span style="{{n.dot}}; margin-top: 6px"></span>
        </a></div>
    </sc-for>
  </div>
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
</div>'''
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
  <sc-if value="{{started}}" hint-placeholder-val="{{ false }}"><div class="pop" style="display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 28px; background: var(--oksoft)"><img src="assets/mascot/zee-sarbatoare.png" alt="" style="width: 44px; height: 48px"><span style="display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 500; color: var(--oktext)">Seria a pornit</span><span style="font-size: 13px; color: var(--ink2)">Îți amintim cu o zi înainte de fiecare vizită.</span></span></div></sc-if>
</div>'''
    return page('Cerere recurentă', 'L', b, SEG_CSS, logic)


# ---------------------------------------------------------------- Start Jobzer (onboarding scurt)
def start_jobzer():
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
  ''' + topbar('Rol.dc.html', '<span style="font-size: 13px; color: var(--ink2)">Pas 1 din 3 obligatoriu</span>') + '''
  <div class="u" style="display: flex; align-items: flex-end; gap: 12px">
    <span style="flex-grow: 1"><h1 style="margin: 0 4px; font-size: 32px; line-height: 1.1; font-weight: 600; letter-spacing: -0.8px">Începi să câștigi azi</h1>
    <p style="margin: 6px 4px 0; font-size: 15px; line-height: 1.4; color: var(--ink2)">Vezi cererile din zonă chiar acum. Ca să trimiți oferte, ai nevoie doar de identitate verificată.</p></span>
    <img class="float" src="assets/mascot/zee-bani.png" alt="" style="width: 84px; height: 91px; flex-shrink: 0">
  </div>
  <a href="Castig.dc.html" class="u d1 pr" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 24px; background: var(--invbg); color: var(--invink); text-decoration: none">
    <span class="glow" style="width: 10px; height: 10px; border-radius: 5px; background: var(--brand); flex-shrink: 0"></span>
    <span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 16px; font-weight: 500">34 de cereri azi în zona ta</span><span style="font-size: 13px; opacity: .7">Montaj, curățenie, cărat · uită-te fără obligații</span></span>
    <span style="font-size: 20px">›</span>
  </a>
  <span class="lbl">De ce ai nevoie și când</span>
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
  <a href="GearBuilder.dc.html" style="align-self: center; font-size: 13px; color: var(--ink2); text-decoration: none">Nu ai unelte încă? Vezi ce îți trebuie, opțional ›</a>
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
        <img src="assets/mascot/zee-fericit.png" alt="" style="width: 40px; height: 43px">
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
    <img src="assets/mascot/zee-bani.png" alt="" class="float" style="position: absolute; right: 12px; bottom: 4px; width: 70px; height: 76px">
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
  ''' + topbar('Fisa.dc.html', '<span style="display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; color: var(--ink2)"><img src="assets/mascot/zee-gandeste.png" alt="" style="width: 26px; height: 28px">Jobzee a găsit {{count}} servicii</span>') + '''
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
    <img src="assets/mascot/zee-gandeste.png" alt="" style="width: 46px; height: 50px; flex-shrink: 0">
    <span style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 15px; font-weight: 500">Sfat: răspunde în sub 2 minute</span><span style="font-size: 13px; line-height: 1.35; color: var(--ink2)">Jobzerii care răspund repede câștigă aproape de două ori mai multe oferte. Activează oferta în 2 atingeri.</span></span>
  </div>
  <a href="GearGrowth.dc.html" class="u d4 pr" style="display: flex; align-items: center; gap: 12px; padding: 12px 14px; border-radius: 24px; background: var(--surf); color: var(--ink); text-decoration: none"><img src="assets/ui/sparkles.png" alt="" style="width: 26px; height: 26px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 500">Growth Insights</span><span style="font-size: 12px; color: var(--ink2)">Scanări QR, vizite pe profil, cereri din promovare</span></span>''' + CHEV + '''</a>
</div>
''' + tabbar('jobzer', 'incasari', {'acasa': 'Castig.dc.html', 'sarcini': 'SarciniJobzer.dc.html', 'incasari': 'Incasari.dc.html', 'cont': 'ContJobzer.dc.html'})
    return page('Statistici Jobzer', 'L', b, SEG_CSS, logic, h=920)


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


if __name__ == '__main__':
    write('Splash.dc.html', splash('L', True))
    write('SplashDark.dc.html', splash('D', True))
    write('Main.dc.html', splash('L', False))
    write('MainDark.dc.html', splash('D', False))
    write('Email.dc.html', email())
    write('Rol.dc.html', rol('L'))
    write('RolDark.dc.html', rol('D'))
    write('SchimbaRol.dc.html', schimba('L'))
    write('SchimbaRolDark.dc.html', schimba('D'))
    write('Acasa.dc.html', acasa('L'))
    write('AcasaDark.dc.html', acasa('D'))
    write('Castig.dc.html', castig('L'))
    write('CastigDark.dc.html', castig('D'))
    write('Cont.dc.html', cont())
    write('ContJobzer.dc.html', cont_jobzer())
    write('Fisa.dc.html', fisa())
    write('Servicii.dc.html', servicii())
    write('ContTrimitere.dc.html', cont_trimitere())
    write('Notificari.dc.html', notificari())
    write('Chitante.dc.html', chitante())
    write('Recurente.dc.html', recurente())
    write('StartJobzer.dc.html', start_jobzer())
    write('OfertaRapida.dc.html', oferta_rapida())
    write('Disponibilitate.dc.html', disponibilitate())
    write('Facturi.dc.html', facturi())
    write('CerereMultipla.dc.html', cerere_multipla())
    write('Statistici.dc.html', statistici())
    write('Siguranta.dc.html', siguranta())
    write('Radar.dc.html', radar('L'))
    write('RadarDark.dc.html', radar('D'))


def mascota():
    items = [('salut', 'Salut', 'Bun venit, permisiuni, suport', False), ('gandeste', 'Gândește', 'Jobzee se gândește', True), ('cauta', 'Caută', 'Radar fără oferte, GPS', True),
             ('potrivire', 'Potrivește', 'Radar cu primele oferte', True), ('asculta', 'Ascultă', 'Dictare vocală', True), ('fericit', 'Bravo', 'Fișă gata, 3+ oferte', False),
             ('sarbatoare', 'Sare de bucurie', 'Plată reușită, serie pornită', False), ('bani', 'La treabă', 'Start Jobzer, încasări', False), ('alearga', 'Pe drum', 'Jobzerul vine spre tine', False),
             ('arata', 'Arată', 'Sfaturi, pasul următor', False), ('ups', 'Verifică telefonul', 'Fără internet, plată refuzată', False), ('trist', 'Ridică din umeri', 'Anulare, ofertă pierdută', False),
             ('doarme', 'La laptop', 'Ecrane goale', False)]
    cells = ''.join('<div class="pop" style="animation-delay: %.2fs; background: var(--surf); border-radius: 24px; padding: 10px 6px; display: flex; flex-direction: column; align-items: center; gap: 2px; text-align: center; position: relative">'
                    '<img src="assets/mascot/zee-%s.png" alt="" style="width: 70px; height: 76px">%s<span style="font-size: 13px; font-weight: 500">%s</span><span style="font-size: 10px; line-height: 1.25; color: var(--ink2)">%s</span></div>'
                    % (i * .04, e, '<span style="position: absolute; right: 8px; top: 8px; height: 16px; padding: 0 5px; border-radius: 8px; background: var(--bsoft); color: var(--btext); font-size: 9px; font-weight: 600; display: flex; align-items: center">LIVE</span>' if a else '', t, u)
                    for i, (e, t, u, a) in enumerate(items))
    b = '''<div style="padding: 52px 14px 0; display: flex; flex-direction: column; gap: 12px">
  <div class="u" style="display: flex; align-items: center; gap: 10px">''' + mark(40) + wordmark(30) + '''</div>
  <div class="u d1"><h1 style="margin: 0 2px; font-size: 28px; font-weight: 600; letter-spacing: -0.7px">Mascota oficială</h1>
  <p style="margin: 6px 2px 0; font-size: 13px; line-height: 1.4; color: var(--ink2)">Pinul portocaliu cu cheie franceză, cu brațe și pantofi. Nu are față: emoția o dă poza. Nu se redesenează, nu se recolorează. Apare la stări goale, erori, succes și în conversațiile cu Jobzee, niciodată pe butoane sau lângă sume.</p></div>
  <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">''' + cells + '''</div>
</div>'''
    return page('Mascota Jobzee', 'L', b, '', 'renderVals() { return {}; }', h=1000)

if __name__ == '__main__':
    write('Mascota.dc.html', mascota())


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
  <div class="u d1" style="display: flex; gap: 6px; overflow-x: auto; scrollbar-width: none; margin: 0 -16px; padding: 0 16px"><sc-for list="{{items}}" as="x" hint-placeholder-count="6"><button type="button" class="fc" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.n}}</button></sc-for></div>
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
      flyer: 'width: ' + (s.fmt === 'a5' ? 200 : 180) + 'px; height: ' + (s.fmt === 'a5' ? 284 : 256) + 'px; transition: all .4s cubic-bezier(.2,.9,.3,1.2); border-radius: 10px; background: #FFFFFF; color: #292D33; box-shadow: 0 16px 36px rgba(0,0,0,.16); padding: 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 6px; position: relative; overflow: hidden' };
  }"""
    b = '''<div style="padding: 56px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  ''' + topbar('PrintStudio.dc.html') + '''
  ''' + h1('Flyer') + '''
  <div style="display: flex; justify-content: center; align-items: flex-end; min-height: 290px">
    <div style="{{flyer}}">
      <span style="position: absolute; left: 0; right: 0; top: 0; height: 44px; background: #FF9B00"></span>
      <span style="position: relative; display: flex; align-items: center; gap: 6px"><img src="assets/brand/jobzee-mark.png" alt="" style="height: 20px; width: auto; filter: brightness(0) invert(1)"><span style="font-size: 10px; font-weight: 600; color: #FFFFFF">JOBZER ÎN CARTIERUL TĂU</span></span>
      <span style="position: relative; margin-top: 14px; font-size: 15px; font-weight: 600; line-height: 1.15">Mobila montată corect, din prima</span>
      <span style="font-size: 9px; line-height: 1.55"><b>Montaj mobilier</b> · de la 120 lei<br><b>Montaj TV</b> · de la 90 lei<br><b>Reparații mici</b> · 80 lei/h</span>
      <span style="font-size: 8px; line-height: 1.3; opacity: .7">Prețuri „de la” din profilul meu Jobzee. Oferta finală o primești în aplicație.</span>
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
  <a href="GearCarte.dc.html" class="u d2" style="display: flex; align-items: center; gap: 10px; padding: 12px 14px; border-radius: 20px; background: var(--bsoft); color: var(--ink); text-decoration: none">''' + ui('warning', 22) + '''<span style="flex-grow: 1; font-size: 14px">Un produs așteaptă aprobarea machetei</span><span style="font-size: 14px; font-weight: 500; color: var(--btext); white-space: nowrap">Aprobă ›</span></a>
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

if __name__ == '__main__':
    for _n, _f in GEAR_PAGES:
        write(_n + '.dc.html', _f())


# ================================================================ MESAGERIE: un singur motor pentru Mesaje, Dialog, Chat, ChatJobzer
# Reguli: fiecare mesaj are id unic; nu se trimite nimic cât timp celălalt „scrie”; dublu-tap ignorat;
# un răspuns automat nu se repetă niciodată; o cerere închisă mută conversația în Istoric (doar citire)
# și pornește o conversație nouă; nicio mențiune „AI”: vorbește Jobzee.

MSG_CSS = SEG_CSS + """
@keyframes bubIn{from{opacity:0;transform:translateY(8px) scale(.97)}to{opacity:1;transform:none}}
@keyframes dotB{0%,80%,100%{transform:translateY(0);opacity:.35}40%{transform:translateY(-4px);opacity:1}}
.bub{animation:bubIn .28s cubic-bezier(.2,.8,.2,1) both}
.dot{width:7px;height:7px;border-radius:4px;background:var(--ink2);display:block;animation:dotB 1.2s infinite}
.dot2{animation-delay:.15s}.dot3{animation-delay:.3s}
.qr{border:0;height:38px;padding:0 15px;border-radius:19px;background:var(--surf);color:var(--btext);box-shadow:inset 0 0 0 1.5px var(--brand);font-family:inherit;font-size:15px;font-weight:500;cursor:pointer;white-space:nowrap;animation:bubIn .3s both}
.ib{width:40px;height:40px;border-radius:20px;border:0;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;padding:0}
.fld{flex-grow:1;min-width:0;height:40px;border-radius:20px;border:0;box-shadow:inset 0 0 0 1px var(--sep);background:var(--surf);padding:0 14px;font-family:inherit;font-size:16px;color:var(--ink);outline:0}
.fld::placeholder{color:var(--ink2)}
.scroll{scrollbar-width:none}.scroll::-webkit-scrollbar{display:none}
.row{display:flex;align-items:center;gap:12px;width:100%;padding:10px 14px 10px 12px;border:0;background:transparent;font-family:inherit;color:var(--ink);text-align:left;cursor:pointer}
.row+.row{box-shadow:inset 0 0.5px 0 var(--sep)}
"""

MSG_ENGINE = r"""constructor(props) {
    super(props);
    this.n = 0;
    const C = __CFG__;
    this.C = C;
    const threads = C.seed.map((th) => Object.assign({ step: 0, ss: '', retry: 0, data: {}, used: [], unread: 0 }, th, { msgs: th.msgs.map((m) => Object.assign({ id: 's' + (this.n++), kind: 'text', t: th.when || '' }, m)) }));
    this.state = { view: C.view, tab: 'active', tid: C.tid, draft: '', typing: '', q: '', threads: threads };
  }
  componentWillUnmount() { clearTimeout(this.t1); }
  now() { const d = new Date(); return String(d.getHours()).padStart(2, '0') + ':' + String(d.getMinutes()).padStart(2, '0'); }
  mk(me, text, x) { return Object.assign({ id: 'm' + (this.n++), me: me, text: text, t: this.now(), kind: 'text' }, x || {}); }
  norm(s) { return String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').trim(); }
  cur() { const s = this.state; return s.threads.find((t) => t.id === s.tid); }
  put(id, add, patch, extra) {
    const threads = this.state.threads.map((t) => t.id === id ? Object.assign({}, t, patch || {}, { msgs: t.msgs.concat(add || []) }) : t);
    this.setState(Object.assign({ threads: threads }, extra || {}));
  }
  later(id, r, ms) {
    if (!r || !r.msgs.length) { if (r && r.patch) this.put(id, [], r.patch); return; }
    this.setState({ typing: id });
    clearTimeout(this.t1);
    this.t1 = setTimeout(() => { this.setState({ typing: '' }); this.put(id, r.msgs, r.patch); }, ms || 800);
  }
  send(raw) {
    const text = String(raw || '').trim();
    const th = this.cur();
    if (!text || !th || this.state.typing || th.status !== 'active') return;
    const last = th.msgs[th.msgs.length - 1];
    if (last && last.me && last.text === text && Date.now() - (this.at || 0) < 2000) return;
    this.at = Date.now();
    const photo = text === '__photo' || this.norm(text) === 'adaug o poza';
    const mine = photo ? this.mk(true, 'Poză atașată', { kind: 'photo' }) : this.mk(true, text);
    const r = th.kind === 'jobzee' ? this.jz(th, photo ? '__photo' : text) : this.reply(th, text);
    this.put(th.id, [mine], r && r.now ? r.now : {}, { draft: '' });
    this.later(th.id, r, th.kind === 'jobzee' ? 750 : 1300);
  }
  // ---------- conversația cu Jobzee: pregătește cererea, pas cu pas, fără să repete întrebări
  svcOf(t) {
    const L = [[/montaj|mobil|ikea|dulap|birou|raft|pat\b|comoda/, 'Montaj mobilier'], [/curat|geam|aspir|calcat|menaj/, 'Curățenie'], [/repar|robinet|priz|bec|usa|yala|instal|chiuveta|scurge/, 'Reparații mici'],
      [/mut|transport|car\b|cara|duba/, 'Mutat și transport'], [/gradin|iarba|gazon|tuns|curte/, 'Grădină'], [/calculator|laptop|imprimant|wifi|router|televizor|\btv\b/, 'IT și tehnică'], [/zugrav|vopsi|perete|gresie|faianta/, 'Zugrăveli și finisaje']];
    const hit = L.find((x) => x[0].test(t));
    return hit ? hit[1] : null;
  }
  est(svc) { return { 'Montaj mobilier': '120–220 lei', 'Curățenie': '150–300 lei', 'Reparații mici': '80–180 lei', 'Mutat și transport': '200–450 lei', 'Grădină': '100–250 lei', 'IT și tehnică': '90–200 lei', 'Zugrăveli și finisaje': '300–900 lei' }[svc] || ''; }
  review(d, out, upd) {
    out.push(this.mk(false, upd ? 'Am actualizat cererea. Uită-te încă o dată peste ea.' : 'Am pregătit cererea. Uită-te peste ea înainte s-o trimit.'));
    const rows = [['Serviciu', d.svc], ['Când', d.cand], ['Unde', d.unde], ['Detalii', d.det || (d.photo ? '1 poză atașată' : 'Fără detalii în plus')]];
    out.push(this.mk(false, '', { kind: 'card', rows: rows.map((r) => ({ k: r[0], v: r[1] })), est: this.est(d.svc), photo: !!d.photo }));
  }
  jz(th, text) {
    const t = this.norm(text), d = Object.assign({}, th.data), out = [];
    let step = th.step, sub = th.ss || '', retry = th.retry, edit = th.edit, status = th.status, label = th.closedLabel, title = th.topic;
    const J = (x) => out.push(this.mk(false, x));
    const next = (n, q) => { retry = 0; sub = ''; if (edit || n === 4) { const u = edit; edit = false; step = 4; this.review(d, out, u); } else { step = n; if (q) J(q); } };
    const lc = (x) => x.charAt(0).toLowerCase() + x.slice(1);
    const cu = { 'Montaj mobilier': 'montajul mobilei', 'Curățenie': 'curățenia', 'Reparații mici': 'reparația', 'Mutat și transport': 'mutatul', 'Grădină': 'grădina', 'IT și tehnică': 'partea tehnică', 'Zugrăveli și finisaje': 'zugrăveala' };
    if (text === '__photo') {
      d.photo = true;
      if (step === 3) { J('Mulțumesc, poza îi ajută mult pe Jobzeri.'); next(4); }
      else J('Mulțumesc, am atașat poza la cerere.');
      return { msgs: out, patch: { data: d, step: step, ss: sub, retry: retry, edit: edit } };
    }
    if (step === 0) {
      if (sub === '' && t === 'altceva') { J('Sigur. Descrie-mi în câteva cuvinte de ce ai nevoie și găsesc eu categoria potrivită.'); sub = 'free'; }
      else {
        let svc = this.svcOf(t);
        if (!svc && retry === 0) { J('Ca să-ți găsesc Jobzerii potriviți, spune-mi ce fel de lucrare este. De exemplu: un montaj, o curățenie sau o reparație.'); retry = 1; }
        else {
          if (!svc) { svc = 'Alte servicii'; d.det = text; } else if (text.length > 24) d.det = text;
          d.svc = svc; title = svc;
          next(1, svc === 'Alte servicii' ? 'Am notat. Când ai nevoie de cineva?' : 'Perfect, te ajut cu ' + cu[svc] + '. Când ai nevoie de cineva?');
        }
      }
    } else if (step === 1) {
      let c = null, say = '';
      if (sub === 'prog') { c = text; say = 'Am notat: ' + lc(text) + '.'; }
      else if (/^programez/.test(t)) { sub = 'prog'; J('Ce zi și ce oră ți se potrivesc?'); }
      else if (/urgent|acum|imediat|repede|cat mai/.test(t)) { c = 'Urgent'; say = 'Bine, caut Jobzeri care pot ajunge cât mai repede.'; }
      else if (/azi|astazi|diseara|in seara|dupa-amiaza|dupa ora|pranz/.test(t)) { c = 'Azi' + (t === 'azi' ? '' : ', ' + text); say = 'Bine, caut Jobzeri liberi azi.'; }
      else if (/maine|poimaine|luni|marti|miercuri|joi|vineri|sambata|duminica|saptamana|dimineata|seara|\d/.test(t)) { c = text; say = 'Am notat: ' + lc(text) + '.'; }
      else if (retry === 0) { J('Spune-mi doar cât de repede: urgent, azi sau într-o anumită zi.'); retry = 1; }
      else { c = text; say = 'Am notat.'; }
      if (c) { d.cand = c; next(2, say + ' Unde să vină Jobzerul?'); }
    } else if (step === 2) {
      let u = null, say = '';
      if (sub === 'addr') { u = text; say = 'Mulțumesc, am salvat adresa.'; }
      else if (/locatia asta|aici|acasa|la mine/.test(t)) { u = 'Str. Barbu Văcărescu 120, Floreasca'; say = 'Folosesc adresa ta: Str. Barbu Văcărescu 120, Floreasca.'; }
      else if (/^alta adresa/.test(t)) { sub = 'addr'; J('Scrie-mi adresa completă: strada, numărul și, dacă e cazul, blocul și apartamentul.'); }
      else if (/\d|str\b|strada|bd\b|bulevard|calea|sos|aleea|piata/.test(t)) { u = text; say = 'Mulțumesc, am salvat adresa.'; }
      else if (retry === 0) { J('Ca să știe Jobzerul unde să vină, alege „Locația asta” sau scrie-mi adresa.'); retry = 1; }
      else { u = text; say = 'Am notat.'; }
      if (u) { d.unde = u; next(3, say + ' Mai vrei să adaugi ceva? O poză sau un detaliu îi ajută pe Jobzeri să-ți facă o ofertă corectă.'); }
    } else if (step === 3) {
      if (!/^(e suficient|nu|gata|nimic|atat|asta e tot)/.test(t)) { d.det = (d.det ? d.det + ' · ' : '') + text; J('Am adăugat detaliul.'); }
      next(4);
    } else if (step === 4) {
      if (sub === 'edit') {
        const m = /servic/.test(t) ? [0, 'Ce serviciu îți trebuie?'] : /cand/.test(t) ? [1, 'Când ai nevoie de cineva?'] : /adres|unde/.test(t) ? [2, 'Unde să vină Jobzerul?'] : /detal|poz/.test(t) ? [3, 'Ce vrei să adaugi?'] : null;
        if (m) { step = m[0]; sub = ''; edit = true; retry = 0; J(m[1]); }
        else J('Alege ce vrei să schimbi: serviciul, ziua, adresa sau detaliile.');
      } else if (/^(trimite|da\b|ok|gata|e bine|perfect|trimite-o)/.test(t)) {
        J('Am trimis cererea. Îți scriu aici imediat ce primești prima ofertă.');
        out.push(this.mk(false, 'Cerere trimisă · ' + d.svc + ' · ' + this.now(), { kind: 'system' }));
        step = 5; status = 'closed'; label = 'Cerere trimisă';
      } else if (/modific|schimb/.test(t)) { sub = 'edit'; J('Sigur. Ce vrei să schimbi?'); }
      else { J(['Dacă totul e în regulă, apasă „Trimite cererea”. Dacă nu, alege „Modific ceva”.', 'Pot trimite cererea așa cum e sau o modificăm împreună. Cum preferi?'][retry % 2]); retry++; }
    }
    return { msgs: out, patch: { data: d, step: step, ss: sub, retry: retry, edit: edit, status: status, closedLabel: label, topic: title, closedAt: status === 'closed' ? Date.now() : th.closedAt, when: status === 'closed' ? 'azi, ' + this.now() : th.when } };
  }
  quickJz(th) {
    if (th.status !== 'active') return [];
    const s = th.step, b = th.ss || '';
    if (s === 0) return b ? [] : ['Montaj mobilier', 'Curățenie', 'Reparații mici', 'Altceva'];
    if (s === 1) return b === 'prog' ? ['Mâine dimineață', 'Mâine seară', 'Sâmbătă'] : ['Urgent', 'Azi', 'Programez'];
    if (s === 2) return b === 'addr' ? [] : ['Locația asta', 'Altă adresă'];
    if (s === 3) return ['Adaug o poză', 'E suficient'];
    if (s === 4) return b === 'edit' ? ['Serviciul', 'Când', 'Adresa', 'Detaliile'] : ['Trimite cererea', 'Modific ceva'];
    return [];
  }
  // ---------- chat cu un om (Jobzer, client, suport): răspunsurile simulate nu se repetă niciodată
  reply(th, text) {
    const t = this.norm(text), used = th.used || [];
    const i = (th.replies || []).findIndex((x, k) => used.indexOf(k) < 0 && (x.k === '' || new RegExp(x.k).test(t)));
    if (i < 0) return { msgs: [], patch: {} };
    return { msgs: [this.mk(false, th.replies[i].r)], now: { used: used.concat([i]) }, patch: {} };
  }
  // ---------- ciclu de viață
  closeChat() {
    const th = this.cur(); if (!th || th.status !== 'active') return;
    this.put(th.id, [this.mk(false, th.closeMsg, { kind: 'system' })], { status: 'closed', closedLabel: th.closeLabel, closedAt: Date.now(), when: 'azi, ' + this.now() });
  }
  newJz(draft) {
    const s = this.state;
    const live = s.threads.find((t) => t.kind === 'jobzee' && t.status === 'active');
    let threads = s.threads;
    if (live && live.msgs.length <= 1) { this.setState({ tid: live.id, view: 'thread', draft: draft || '' }); return; }
    if (live) threads = threads.map((t) => t === live ? Object.assign({}, t, { status: 'closed', closedLabel: 'Neterminată', closedAt: Date.now(), when: 'azi, ' + this.now() }) : t);
    const id = 'jz' + (this.n++);
    const th = { id: id, kind: 'jobzee', title: 'Jobzee', topic: 'Conversație nouă', sub: 'Te ajut să pregătești cererea', status: 'active', step: 0, ss: '', retry: 0, data: {}, used: [], unread: 0, when: 'azi',
      msgs: [this.mk(false, 'Conversație nouă · azi, ' + this.now(), { kind: 'divider' }), this.mk(false, 'Bună din nou, Paul! Cu ce te pot ajuta de data asta?')] };
    this.setState({ threads: [th].concat(threads), tid: id, view: 'thread', draft: draft || '', typing: '' });
  }
  resume(id) {
    const s = this.state;
    let threads = s.threads.filter((t) => !(t.kind === 'jobzee' && t.status === 'active' && t.msgs.length <= 2 && t.id !== id));
    threads = threads.map((t) => t.kind === 'jobzee' && t.status === 'active' ? Object.assign({}, t, { status: 'closed', closedLabel: 'Neterminată', closedAt: Date.now(), when: 'azi, ' + this.now() }) : t);
    threads = threads.map((t) => t.id === id ? Object.assign({}, t, { status: 'active', closedLabel: '' }) : t);
    this.setState({ threads: threads, tid: id, view: 'thread' });
  }
  open(id) { this.setState({ tid: id, view: 'thread', draft: '', threads: this.state.threads.map((t) => t.id === id ? Object.assign({}, t, { unread: 0 }) : t) }); }
  // ---------- ce vede ecranul
  lastTxt(th) {
    for (let i = th.msgs.length - 1; i >= 0; i--) { const m = th.msgs[i];
      if (m.kind === 'text') return (m.me ? 'Tu: ' : '') + m.text;
      if (m.kind === 'photo') return (m.me ? 'Tu: ' : '') + 'Poză';
      if (m.kind === 'card') return 'Cererea e gata de trimis';
      if (m.kind === 'system') return m.text; }
    return '';
  }
  renderVals() {
    const s = this.state, C = this.C;
    const zee = (th) => th.status === 'closed' ? 'assets/mascot/zee-fericit.png' : s.typing === th.id ? 'assets/mascot/zee-gandeste.png' : 'assets/mascot/zee-salut.png';
    const chip = (th) => th.status === 'closed' ? th.closedLabel : '';
    const chipSt = (l) => 'height: 20px; padding: 0 8px; border-radius: 10px; font-size: 11px; font-weight: 500; display: inline-flex; align-items: center; white-space: nowrap; ' +
      (l === 'Finalizată' || l === 'Lucrare încheiată' ? 'background: var(--oksoft); color: var(--oktext)' : l === 'Anulată' ? 'background: var(--surf2); color: var(--ink2)' : 'background: var(--bsoft); color: var(--btext)');
    const q = this.norm(s.q);
    const row = (th) => ({ id: th.id, title: th.kind === 'jobzee' ? 'Jobzee' : th.title, sub: th.kind === 'jobzee' ? (th.topic || 'Conversație nouă') : th.topic, last: this.lastTxt(th), when: th.when || '',
      isZee: th.kind === 'jobzee' || th.kind === 'support', img: th.kind === 'jobzee' || th.kind === 'support' ? zee(th) : th.avatar, chip: chip(th), hasChip: !!chip(th), chipStyle: chipSt(chip(th)),
      unread: th.unread, hasUnread: th.unread > 0, open: () => this.open(th.id) });
    const match = (th) => !q || this.norm([th.title, th.topic, this.lastTxt(th)].join(' ')).indexOf(q) >= 0;
    const act = s.threads.filter((t) => t.status === 'active' && match(t)).sort((a, b) => (a.kind === 'jobzee' ? -1 : 0) - (b.kind === 'jobzee' ? -1 : 0)).map(row);
    const hist = s.threads.filter((t) => t.status === 'closed' && match(t)).sort((a, b) => (b.closedAt || 0) - (a.closedAt || 0)).map(row);
    const nAct = s.threads.filter((t) => t.status === 'active').length, nHist = s.threads.filter((t) => t.status === 'closed').length;
    const th = this.cur() || s.threads[0];
    const isJz = th.kind === 'jobzee', active = th.status === 'active', typing = s.typing === th.id;
    const bub = 'max-width: 80%; padding: 10px 14px; font-size: 16px; line-height: 1.38; white-space: pre-wrap; word-break: break-word; ';
    const msgs = th.msgs.map((m, i) => {
      const nx = th.msgs[i + 1];
      const tail = !nx || nx.me !== m.me || nx.kind === 'divider' || nx.kind === 'system';
      return { id: m.id, text: m.text, t: m.t, rows: m.rows || [], est: m.est || '', hasEst: !!m.est, noEst: !m.est,
        isText: m.kind === 'text', isPhoto: m.kind === 'photo', isCard: m.kind === 'card', isDiv: m.kind === 'divider', isSys: m.kind === 'system',
        wrap: 'display: flex; flex-direction: column; gap: 3px; ' + (m.me ? 'align-items: flex-end' : 'align-items: flex-start') + '; margin-bottom: ' + (tail ? 8 : 0) + 'px',
        style: bub + (m.me ? 'background: var(--brand); color: var(--onbrand); border-radius: ' + (tail ? '20px 20px 6px 20px' : '20px') : 'background: var(--surf); color: var(--ink); border-radius: ' + (tail ? '20px 20px 20px 6px' : '20px')),
        meta: tail, metaTxt: m.me && i === th.msgs.length - 1 ? 'Livrat · ' + m.t : m.t };
    });
    const qs = isJz ? this.quickJz(th) : (active ? (th.quick || []).filter((x) => !th.msgs.some((m) => m.me && m.text === x)) : []);
    const quick = typing ? [] : qs.map((x) => ({ text: x, pick: () => this.send(x) }));
    const d = th.data || {};
    const fl = [['Serviciu', !!d.svc], ['Când', !!d.cand], ['Unde', !!d.unde], ['Detalii', th.step >= 4]];
    const fields = fl.map((f) => ({ label: (f[1] ? '✓ ' : '') + f[0], style: 'height: 26px; padding: 0 10px; border-radius: 13px; font-size: 12px; font-weight: 500; display: flex; align-items: center; transition: all .3s; ' + (f[1] ? 'background: var(--bsoft); color: var(--btext)' : 'background: var(--surf2); color: var(--ink2)') }));
    const canSend = active && !typing && s.draft.trim().length > 0;
    const sample = ['Am de montat un birou IKEA și un dulap mic', 'Azi, după ora 17', 'La mine acasă', 'Cutiile sunt deja în sufragerie', 'Trimite cererea'][Math.min(th.step, 4)];
    return {
      isList: s.view === 'list', isThread: s.view === 'thread', isAct: s.tab === 'active', isHist: s.tab === 'hist',
      tA: s.tab === 'active' ? 'true' : 'false', tH: s.tab === 'hist' ? 'true' : 'false', goA: () => this.setState({ tab: 'active' }), goH: () => this.setState({ tab: 'hist' }),
      labA: 'Active · ' + nAct, labH: 'Istoric · ' + nHist, act: act, hist: hist, histEmpty: hist.length === 0, actEmpty: act.length === 0,
      q: s.q, onQ: (e) => this.setState({ q: e.target.value }),
      back: () => this.setState({ view: 'list', typing: '', draft: '' }),
      title: isJz ? 'Jobzee' : th.title, sub: typing ? (isJz ? 'Jobzee scrie…' : th.title.split(' ')[0] + ' scrie…') : active ? th.sub : th.closedLabel + ' · ' + (th.when || ''),
      isZee: isJz || th.kind === 'support', img: isJz || th.kind === 'support' ? zee(th) : th.avatar, isJz: isJz, isPerson: th.kind === 'jobzer' || th.kind === 'client',
      topic: th.topic || '', hasTopic: !isJz && !!th.topic, fields: fields, showFields: isJz && active,
      msgs: msgs, typing: typing, quick: quick, hasQuick: quick.length > 0,
      active: active, closed: !active, jzClosed: !active && isJz, chatClosed: !active && !isJz && th.kind !== 'support',
      sent: !active && isJz && th.closedLabel === 'Cerere trimisă', unfinished: !active && isJz && th.closedLabel === 'Neterminată',
      canClose: active && !!th.closeAsk, closeAsk: th.closeAsk || '', closeBtn: th.closeBtn || '', doClose: () => this.closeChat(),
      draft: s.draft, onDraft: (e) => this.setState({ draft: e.target.value }), onKey: (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); this.send(this.state.draft); } },
      doSend: () => this.send(this.state.draft), sendStyle: 'background: ' + (canSend ? 'var(--brand)' : 'var(--surf3)') + '; color: ' + (canSend ? 'var(--onbrand)' : 'var(--ink2)') + '; transition: background .2s',
      ph: !active ? 'Conversația s-a încheiat' : typing ? 'Așteaptă o clipă…' : isJz ? 'Scrie-i lui Jobzee…' : 'Mesaj către ' + th.title.split(' ')[0],
      photo: () => this.send('__photo'), dictate: () => { if (active && !typing) this.setState({ draft: sample }); },
      newJz: () => this.newJz(''), again: () => this.newJz(th.againDraft || ''), resume: () => this.resume(th.id),
      isHub: C.mode === 'hub', notHub: C.mode !== 'hub'
    };
  }"""


def _seed_hub():
    return [
        dict(id='jz1', kind='jobzee', title='Jobzee', topic='Conversație nouă', status='active', when='azi', sub='Te ajut să pregătești cererea',
             msgs=[dict(me=False, text='Bună, Paul! Sunt Jobzee. Spune-mi pe scurt cu ce te pot ajuta și pregătesc eu cererea pentru tine.', t='11:52')]),
        dict(id='mihai', kind='jobzer', title='Mihai I.', avatar='assets/people/person-jobzer-3.webp', topic='Montaj mobilier · 150 lei', sub='Pe drum · ajunge în 10 min', status='active', when='11:48', unread=1,
             quick=['Sunt acasă', 'Interfonul e 12', 'Poți parca în curte', 'Mulțumesc!'],
             replies=[dict(k='acasa|astept', r='Perfect, ne vedem imediat.'), dict(k='interfon', r='Am notat, sun la 12 când ajung.'),
                      dict(k='parc|curte', r='Mulțumesc că mi-ai spus, parchez în curte.'), dict(k='cat|cand|unde esti|intarzi|mai ai', r='Mai am cam 5 minute, sunt pe Barbu Văcărescu.'),
                      dict(k='pret|cost|lei|plat', r='Rămâne cum am stabilit în ofertă: 150 lei, plătești din aplicație la final.'), dict(k='multum|mersi', r='Cu plăcere!'), dict(k='', r='Am văzut, mulțumesc!')],
             closeAsk='Lucrarea e gata? Confirm-o și conversația trece în Istoric.', closeBtn='Confirmă', closeMsg='Lucrare confirmată · 150 lei · plata s-a făcut din aplicație', closeLabel='Finalizată',
             againDraft='Aș vrea din nou ajutorul lui Mihai I. pentru ',
             msgs=[dict(me=False, text='Bună! Am văzut pozele, plec acum spre tine.', t='11:41'), dict(me=True, text='Super, mulțumesc! Totul e încă în cutii.', t='11:42'),
                   dict(me=False, text='Ajung în aproximativ 10 minute. Am la mine toate uneltele.', t='11:48')]),
        dict(id='sup', kind='support', title='Suport Jobzee', topic='Suntem aici 24/7', sub='Răspundem de obicei în câteva minute', status='active', when='1 oct.',
             replies=[dict(k='', r='Mulțumim! Un coleg din echipa Jobzee îți răspunde în câteva minute.'), dict(k='', r='Am adăugat mesajul la discuție. Revenim imediat.')],
             msgs=[dict(me=False, text='Bună, Paul! Dacă ai nevoie de ajutor cu o cerere sau cu o plată, scrie-ne aici.', t='1 oct.')]),
        dict(id='jz0', kind='jobzee', title='Jobzee', topic='Curățenie', status='closed', closedLabel='Cerere trimisă', when='9 oct.',
             msgs=[dict(me=False, text='Bună, Paul! Cu ce te pot ajuta azi?'), dict(me=True, text='Am nevoie de o curățenie generală, 2 camere.'),
                   dict(me=False, text='Perfect, te ajut cu curățenia. Când ai nevoie de cineva?'), dict(me=True, text='Sâmbătă dimineață'),
                   dict(me=False, text='Am notat: sâmbătă dimineață. Am trimis cererea și îți scriu aici la prima ofertă.'), dict(me=False, kind='system', text='Cerere trimisă · Curățenie · 9 oct.')]),
        dict(id='elena', kind='jobzer', title='Elena P.', avatar='assets/people/person-client-1.webp', topic='Curățenie · 180 lei', status='closed', closedLabel='Finalizată', when='11 oct.',
             againDraft='Aș vrea din nou o curățenie cu Elena P. ',
             msgs=[dict(me=False, text='Bună ziua! Ajung la 9:00, cum am stabilit.'), dict(me=True, text='Bună ziua, vă aștept. Mulțumesc!'),
                   dict(me=False, text='Am terminat. Am lăsat produsele de curățat sub chiuvetă.'), dict(me=True, text='Arată impecabil, mulțumesc mult!'),
                   dict(me=False, text='Mulțumesc și eu, o zi bună!'), dict(me=False, kind='system', text='Lucrare confirmată · 180 lei · 11 oct.')]),
        dict(id='radu', kind='jobzer', title='Radu C.', avatar='assets/people/person-jobzer-1.webp', topic='Instalare imprimantă', status='closed', closedLabel='Anulată', when='2 oct.',
             againDraft='Am nevoie de ajutor cu instalarea unei imprimante ',
             msgs=[dict(me=False, text='Bună! Ce model de imprimantă ai?'), dict(me=True, text='HP LaserJet. Aș vrea să meargă pe Wi-Fi.'),
                   dict(me=False, kind='system', text='Cerere anulată de tine înainte de start · fără costuri')]),
    ]


def _msg_thread_markup(close_href, close_label, mode):
    """Antet + fir de mesaje + răspunsuri rapide + bară de scriere / bară de final. Comun pentru toate modurile."""
    back = ('<button type="button" onClick="{{back}}" aria-label="Înapoi la conversații" class="ib pr" style="background: transparent; color: var(--btext)">' + BACK + '</button>') if mode == 'hub' else \
           ('<a href="' + close_href + '" aria-label="' + close_label + '" class="ib pr" style="background: var(--surf2); color: var(--ink); text-decoration: none">' + (CLOSE if close_label == 'Închide' else BACK) + '</a>')
    hist = '' if mode == 'hub' else '<a href="Mesaje.dc.html" aria-label="Istoric conversații" class="ib pr" style="background: var(--surf2); color: var(--ink); text-decoration: none"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"></path><path d="M3 3v5h5M12 7v5l3 2"></path></svg></a>'
    return '''<div style="height: 100%; display: flex; flex-direction: column">
  <div class="glass" style="padding: 50px 12px 10px; box-shadow: 0 0.5px 0 var(--sep); display: flex; flex-direction: column; gap: 10px; z-index: 2">
    <div style="display: flex; align-items: center; gap: 10px">
      ''' + back + '''
      <sc-if value="{{isZee}}" hint-placeholder-val="{{ true }}"><span style="width: 42px; height: 42px; border-radius: 21px; background: var(--bsoft); display: flex; align-items: center; justify-content: center; flex-shrink: 0"><img src="{{img}}" alt="" style="width: 32px; height: 35px"></span></sc-if>
      <sc-if value="{{isPerson}}" hint-placeholder-val="{{ false }}"><img src="{{img}}" alt="" style="width: 42px; height: 42px; border-radius: 21px; object-fit: cover; flex-shrink: 0"></sc-if>
      <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column"><span style="font-size: 17px; font-weight: 600">{{title}}</span><span style="font-size: 12px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{sub}}</span></span>
      <sc-if value="{{isJz}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{newJz}}" class="pr" style="height: 34px; padding: 0 12px; border: 0; border-radius: 17px; background: var(--surf2); color: var(--ink); font-family: inherit; font-size: 13px; font-weight: 500; cursor: pointer; flex-shrink: 0">+ Nouă</button></sc-if>
      ''' + hist + '''
    </div>
    <sc-if value="{{showFields}}" hint-placeholder-val="{{ true }}"><div style="display: flex; gap: 6px"><sc-for list="{{fields}}" as="f" hint-placeholder-count="4"><span style="{{f.style}}">{{f.label}}</span></sc-for></div></sc-if>
    <sc-if value="{{hasTopic}}" hint-placeholder-val="{{ false }}"><span style="font-size: 12px; color: var(--ink2); padding-left: 52px">{{topic}}</span></sc-if>
  </div>
  <sc-if value="{{canClose}}" hint-placeholder-val="{{ false }}"><div style="margin: 10px 12px 0; padding: 10px 10px 10px 14px; border-radius: 18px; background: var(--bsoft); display: flex; align-items: center; gap: 10px"><span style="flex-grow: 1; font-size: 13px; line-height: 1.35">{{closeAsk}}</span><button type="button" onClick="{{doClose}}" class="pr" style="height: 34px; padding: 0 14px; border: 0; border-radius: 17px; background: var(--invbg); color: var(--invink); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer; white-space: nowrap; flex-shrink: 0">{{closeBtn}}</button></div></sc-if>
  <div class="scroll" style="flex-grow: 1; min-height: 0; overflow-y: auto; display: flex; flex-direction: column-reverse; padding: 12px 14px 6px">
    <div style="display: flex; flex-direction: column">
      <sc-for list="{{msgs}}" as="m" hint-placeholder-count="3">
        <sc-if value="{{m.isDiv}}" hint-placeholder-val="{{ false }}"><div class="bub" style="align-self: center; margin: 6px 0 12px; height: 24px; padding: 0 12px; border-radius: 12px; background: var(--surf2); color: var(--ink2); font-size: 12px; font-weight: 500; display: flex; align-items: center">{{m.text}}</div></sc-if>
        <sc-if value="{{m.isSys}}" hint-placeholder-val="{{ false }}"><div class="bub" style="align-self: center; margin: 4px 0 12px; max-width: 86%; padding: 6px 12px; border-radius: 12px; background: var(--oksoft); color: var(--oktext); font-size: 12px; font-weight: 500; text-align: center">✓ {{m.text}}</div></sc-if>
        <sc-if value="{{m.isText}}" hint-placeholder-val="{{ true }}"><div class="bub" style="{{m.wrap}}"><div style="{{m.style}}">{{m.text}}</div><sc-if value="{{m.meta}}" hint-placeholder-val="{{ true }}"><span style="font-size: 11px; color: var(--ink2); padding: 0 6px">{{m.metaTxt}}</span></sc-if></div></sc-if>
        <sc-if value="{{m.isPhoto}}" hint-placeholder-val="{{ false }}"><div class="bub" style="{{m.wrap}}"><img src="assets/photos/hero-client-home.webp" alt="Poză atașată" style="width: 170px; height: 120px; border-radius: 18px; object-fit: cover; display: block"><span style="font-size: 11px; color: var(--ink2); padding: 0 6px">{{m.metaTxt}}</span></div></sc-if>
        <sc-if value="{{m.isCard}}" hint-placeholder-val="{{ false }}"><div class="bub" style="align-self: flex-start; width: 84%; margin-bottom: 8px; border-radius: 22px; background: var(--surf); box-shadow: inset 0 0 0 1.5px var(--brand); padding: 12px 14px; display: flex; flex-direction: column; gap: 8px">
          <span style="display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 600; color: var(--btext)"><img src="assets/brand/jobzee-mark.png" alt="" style="height: 18px; width: auto">Cererea ta</span>
          <sc-for list="{{m.rows}}" as="r" hint-placeholder-count="4"><span style="display: flex; gap: 10px; font-size: 14px; line-height: 1.3"><span style="width: 64px; flex-shrink: 0; color: var(--ink2)">{{r.k}}</span><span style="flex-grow: 1">{{r.v}}</span></span></sc-for>
          <sc-if value="{{m.hasEst}}" hint-placeholder-val="{{ true }}"><span style="padding-top: 8px; box-shadow: inset 0 0.5px 0 var(--sep); display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: var(--ink2)">De obicei, în zona ta</span><span style="font-size: 18px; font-weight: 600">{{m.est}}</span><span style="font-size: 11px; color: var(--ink2)">Prețul final vine din ofertele Jobzerilor.</span></span></sc-if>
          <sc-if value="{{m.noEst}}" hint-placeholder-val="{{ false }}"><span style="padding-top: 8px; box-shadow: inset 0 0.5px 0 var(--sep); font-size: 12px; color: var(--ink2)">Prețul îl afli din ofertele Jobzerilor.</span></sc-if>
          <a href="Fisa.dc.html" style="font-size: 13px; font-weight: 500; color: var(--btext); text-decoration: none">Vezi fișa completă ›</a>
        </div></sc-if>
      </sc-for>
      <sc-if value="{{typing}}" hint-placeholder-val="{{ false }}"><div class="bub" style="align-self: flex-start; display: flex; gap: 5px; padding: 14px 16px; border-radius: 20px 20px 20px 6px; background: var(--surf); margin-bottom: 8px"><span class="dot"></span><span class="dot dot2"></span><span class="dot dot3"></span></div></sc-if>
    </div>
  </div>
  <sc-if value="{{hasQuick}}" hint-placeholder-val="{{ true }}"><div style="padding: 4px 12px 10px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end"><sc-for list="{{quick}}" as="x" hint-placeholder-count="3"><button type="button" onClick="{{x.pick}}" class="qr pr">{{x.text}}</button></sc-for></div></sc-if>
  <sc-if value="{{active}}" hint-placeholder-val="{{ true }}"><div class="glass" style="padding: 8px 12px 30px; display: flex; gap: 8px; align-items: center; box-shadow: 0 -0.5px 0 var(--sep)">
    <button type="button" onClick="{{photo}}" aria-label="Atașează o poză" class="ib pr" style="background: var(--surf2); color: var(--ink)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h3l2-3h6l2 3h3v11H4z"></path><circle cx="12" cy="13" r="3.5"></circle></svg></button>
    <label for="msg-in" style="position: absolute; left: -9999px">Mesaj</label>
    <input id="msg-in" class="fld" value="{{draft}}" onChange="{{onDraft}}" onKeyDown="{{onKey}}" placeholder="{{ph}}" autocomplete="off">
    <sc-if value="{{isJz}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{dictate}}" aria-label="Dictează" class="ib pr" style="background: var(--surf2); color: var(--ink)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0M12 18v3"></path></svg></button></sc-if>
    <button type="button" onClick="{{doSend}}" aria-label="Trimite" class="ib pr" style="{{sendStyle}}"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"></path></svg></button>
  </div></sc-if>
  <sc-if value="{{closed}}" hint-placeholder-val="{{ false }}"><div class="glass" style="padding: 12px 14px 30px; display: flex; flex-direction: column; gap: 10px; box-shadow: 0 -0.5px 0 var(--sep)">
    <span style="font-size: 13px; color: var(--ink2); text-align: center">Conversația s-a încheiat. O găsești oricând în Istoric, doar pentru citire.</span>
    <sc-if value="{{sent}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px"><a href="Radar.dc.html" class="pr" style="flex: 1; height: 48px; border-radius: 24px; background: var(--surf2); color: var(--ink); display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500; text-decoration: none">Urmărește pe radar</a><button type="button" onClick="{{newJz}}" class="pr" style="flex: 1; height: 48px; border: 0; border-radius: 24px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 15px; font-weight: 500; cursor: pointer">Conversație nouă</button></div></sc-if>
    <sc-if value="{{unfinished}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px"><button type="button" onClick="{{resume}}" class="pr" style="flex: 1; height: 48px; border: 0; border-radius: 24px; background: var(--surf2); color: var(--ink); font-family: inherit; font-size: 15px; font-weight: 500; cursor: pointer">Continuă de aici</button><button type="button" onClick="{{newJz}}" class="pr" style="flex: 1; height: 48px; border: 0; border-radius: 24px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 15px; font-weight: 500; cursor: pointer">Conversație nouă</button></div></sc-if>
    <sc-if value="{{chatClosed}}" hint-placeholder-val="{{ false }}"><div style="display: flex; gap: 8px">''' + (
        '<a href="Recenzie.dc.html" class="pr" style="flex: 1; height: 48px; border-radius: 24px; background: var(--surf2); color: var(--ink); display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500; text-decoration: none">Lasă o recenzie</a>'
        if mode != 'chatj' else '<a href="Incasari.dc.html" class="pr" style="flex: 1; height: 48px; border-radius: 24px; background: var(--surf2); color: var(--ink); display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500; text-decoration: none">Vezi încasarea</a>') + (
        '<button type="button" onClick="{{again}}" class="pr" style="flex: 1; height: 48px; border: 0; border-radius: 24px; background: var(--brand); color: var(--onbrand); font-family: inherit; font-size: 15px; font-weight: 500; cursor: pointer">Cerere nouă</button>' if mode == 'hub' else
        '<a href="' + ('Dialog.dc.html' if mode == 'chat' else 'Castig.dc.html') + '" class="pr" style="flex: 1; height: 48px; border-radius: 24px; background: var(--brand); color: var(--onbrand); display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500; text-decoration: none">' + ('Cerere nouă' if mode == 'chat' else 'Cereri noi') + '</a>') + '''</div></sc-if>
  </div></sc-if>
</div>'''


def _msg_page(title, cfg, body, extra=''):
    import json as _j
    logic = MSG_ENGINE.replace('__CFG__', _j.dumps(cfg, ensure_ascii=False))
    return page(title, 'L', body, MSG_CSS + extra, logic)


def mesaje_hub():
    cfg = dict(mode='hub', view='list', tid='jz1', seed=_seed_hub())
    row = '''<button type="button" onClick="{{r.open}}" class="row pr">
          <sc-if value="{{r.isZee}}" hint-placeholder-val="{{ true }}"><span style="width: 50px; height: 50px; border-radius: 25px; background: var(--bsoft); display: flex; align-items: center; justify-content: center; flex-shrink: 0"><img src="{{r.img}}" alt="" style="width: 36px; height: 39px"></span></sc-if>
          <sc-if value="{{r.notZee}}" hint-placeholder-val="{{ false }}"><img src="{{r.img}}" alt="" style="width: 50px; height: 50px; border-radius: 25px; object-fit: cover; flex-shrink: 0"></sc-if>
          <span style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px">
            <span style="display: flex; align-items: center; gap: 6px"><span style="font-size: 16px; font-weight: 600; white-space: nowrap">{{r.title}}</span><span style="font-size: 13px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex-grow: 1">{{r.sub}}</span><span style="font-size: 12px; color: var(--ink2); flex-shrink: 0">{{r.when}}</span></span>
            <span style="display: flex; align-items: center; gap: 6px"><span style="font-size: 14px; color: var(--ink2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex-grow: 1">{{r.last}}</span>
              <sc-if value="{{r.hasChip}}" hint-placeholder-val="{{ false }}"><span style="{{r.chipStyle}}">{{r.chip}}</span></sc-if>
              <sc-if value="{{r.hasUnread}}" hint-placeholder-val="{{ false }}"><span style="min-width: 20px; height: 20px; border-radius: 10px; background: var(--brand); color: var(--onbrand); font-size: 12px; font-weight: 600; display: flex; align-items: center; justify-content: center">{{r.unread}}</span></sc-if></span>
          </span>
        </button>'''
    b = '''<sc-if value="{{isList}}" hint-placeholder-val="{{ true }}"><div style="padding: 60px 16px 0; display: flex; flex-direction: column; gap: 12px">
  <h1 class="u" style="margin: 0 4px; font-size: 34px; font-weight: 600; letter-spacing: -0.9px">Mesaje</h1>
  <label class="u d1" style="display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 12px; border-radius: 12px; background: var(--surf2); color: var(--ink2)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><span style="position: absolute; left: -9999px">Caută în conversații</span><input value="{{q}}" onChange="{{onQ}}" placeholder="Caută o persoană sau o lucrare" style="flex-grow: 1; min-width: 0; border: 0; outline: 0; background: transparent; font-family: inherit; font-size: 16px; color: var(--ink)"></label>
  <div class="sg u d1" style="grid-template-columns: repeat(2, minmax(0, 1fr))"><button type="button" onClick="{{goA}}" aria-pressed="{{tA}}">{{labA}}</button><button type="button" onClick="{{goH}}" aria-pressed="{{tH}}">{{labH}}</button></div>
  <sc-if value="{{isAct}}" hint-placeholder-val="{{ true }}"><div class="grp u d2" style="border-radius: 22px">
    <sc-for list="{{act}}" as="r" hint-placeholder-count="3">''' + row + '''</sc-for>
  </div>
  <sc-if value="{{actEmpty}}" hint-placeholder-val="{{ false }}"><span style="font-size: 14px; color: var(--ink2); text-align: center; padding: 20px">Nicio conversație activă pentru „{{q}}”.</span></sc-if>
  <span class="note" style="font-size: 12px; line-height: 1.4; color: var(--ink2); padding: 0 6px">Fiecare cerere are conversația ei. Când cererea se încheie, conversația trece în Istoric. Numărul tău de telefon rămâne ascuns.</span></sc-if>
  <sc-if value="{{isHist}}" hint-placeholder-val="{{ false }}"><div class="grp" style="border-radius: 22px">
    <sc-for list="{{hist}}" as="r" hint-placeholder-count="3">''' + row + '''</sc-for>
  </div>
  <sc-if value="{{histEmpty}}" hint-placeholder-val="{{ false }}"><div style="display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 24px"><img src="assets/mascot/zee-doarme.png" alt="" style="width: 110px; height: 119px"><span style="font-size: 14px; color: var(--ink2); text-align: center">Aici apar conversațiile încheiate.</span></div></sc-if>
  <span style="font-size: 12px; line-height: 1.4; color: var(--ink2); padding: 0 6px">Conversațiile din Istoric se pot citi oricând, dar nu se mai scrie în ele. Pentru o lucrare nouă, Jobzee pornește o conversație nouă.</span></sc-if>
</div>
''' + tabbar('client', 'mesaje', {'acasa': 'Acasa.dc.html', 'activitate': 'Activitate.dc.html', 'mesaje': 'Mesaje.dc.html', 'cont': 'Cont.dc.html'}) + '''</sc-if>
<sc-if value="{{isThread}}" hint-placeholder-val="{{ false }}">''' + _msg_thread_markup('', '', 'hub') + '''</sc-if>'''
    # rândul are nevoie și de opusul lui isZee
    out = _msg_page('Mesaje', cfg, b)
    return out.replace("isZee: th.kind === 'jobzee' || th.kind === 'support', img: th.kind === 'jobzee' || th.kind === 'support' ? zee(th) : th.avatar, chip:",
                       "isZee: th.kind === 'jobzee' || th.kind === 'support', notZee: !(th.kind === 'jobzee' || th.kind === 'support'), img: th.kind === 'jobzee' || th.kind === 'support' ? zee(th) : th.avatar, chip:")


def dialog_jz():
    seed = [dict(id='jz1', kind='jobzee', title='Jobzee', topic='Conversație nouă', status='active', when='azi', sub='Te ajut să pregătești cererea',
                 msgs=[dict(me=False, text='Bună, Paul! Sunt Jobzee. Spune-mi pe scurt cu ce te pot ajuta și pregătesc eu cererea pentru tine.', t='11:52')])]
    return _msg_page('Conversație cu Jobzee', dict(mode='dialog', view='thread', tid='jz1', seed=seed), _msg_thread_markup('Acasa.dc.html', 'Închide', 'dialog'))


def chat_client():
    hub = {t['id']: t for t in _seed_hub()}
    m = dict(hub['mihai']); m['unread'] = 0
    return _msg_page('Chat cu Mihai', dict(mode='chat', view='thread', tid='mihai', seed=[m]), _msg_thread_markup('Mesaje.dc.html', 'Înapoi', 'chat'))


def chat_jobzer():
    a = dict(id='andrei', kind='client', title='Andrei P.', avatar='assets/people/person-client-2.webp', topic='Montaj birou și dulap · Str. Barbu Văcărescu 120, ap. 12, et. 3', sub='Client · ★ 4,9 · numărul rămâne ascuns', status='active', when='11:42',
             quick=['Am ajuns', 'Întârzii 5 minute', 'Care e interfonul?', 'Am terminat'],
             replies=[dict(k='ajuns|jos|la poarta', r='Cobor imediat!'), dict(k='intarzi|minute', r='Nicio problemă, mulțumesc că m-ai anunțat.'),
                      dict(k='interfon|etaj|apartament', r='Interfonul e 12, etajul 3.'), dict(k='terminat|gata', r='Super! Mă uit acum și confirm în aplicație.'),
                      dict(k='multum|mersi', r='Eu îți mulțumesc!'), dict(k='', r='Am văzut, mulțumesc!')],
             closeAsk='Ai terminat lucrarea? Clientul primește cererea de confirmare.', closeBtn='Am terminat', closeMsg='Clientul a confirmat lucrarea · 150 lei intră în încasări', closeLabel='Lucrare încheiată',
             msgs=[dict(me=True, text='Bună! Am văzut pozele, plec acum spre tine.', t='11:41'), dict(me=False, text='Super, mulțumesc! Totul e încă în cutii.', t='11:42')])
    return _msg_page('Chat cu clientul', dict(mode='chatj', view='thread', tid='andrei', seed=[a]), _msg_thread_markup('JobActiv.dc.html', 'Înapoi', 'chatj'))


MSG_PAGES = [('Mesaje', mesaje_hub), ('Dialog', dialog_jz), ('Chat', chat_client), ('ChatJobzer', chat_jobzer)]

if __name__ == '__main__':
    for _n, _f in MSG_PAGES:
        write(_n + '.dc.html', _f())


# ================================================================ COMPETENȚE ȘI PORTOFOLIU (Jobzer)
SK_CSS = SEG_CSS + """
.colfix>*{flex-shrink:0}
.scroll{scrollbar-width:none}.scroll::-webkit-scrollbar{display:none}
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
    b = '''<div class="colfix" style="padding: 54px 16px 28px; height: 100%; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px">
  <div style="display: flex; align-items: center; gap: 12px">''' + topbar('DevinoJobzer.dc.html').replace('<div style="display: flex; align-items: center; justify-content: space-between">', '<div>') + '''
    <span style="flex-grow: 1; height: 6px; border-radius: 3px; background: var(--surf3); overflow: hidden"><span style="display: block; width: 50%; height: 100%; border-radius: 3px; background: var(--brand)"></span></span><span style="font-size: 13px; font-weight: 500; color: var(--ink2)">2/4</span></div>
  ''' + h1('Ce știi să faci?', 'Alege tot ce faci bine. Detaliile, prețul și pozele le adaugi după, în profil.') + '''
  <label class="u d1" style="display: flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border-radius: 22px; background: var(--surf); color: var(--ink2); box-shadow: 0 2px 10px var(--shadow)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><span style="position: absolute; left: -9999px">Caută o competență</span><input value="{{q}}" onChange="{{onQ}}" placeholder="Caută: „gresie”, „babysitting”…" style="flex-grow: 1; min-width: 0; border: 0; outline: 0; background: transparent; font-family: inherit; font-size: 16px; color: var(--ink)"></label>
  <div class="scroll" style="flex-grow: 1; flex-shrink: 1; min-height: 0; overflow-y: auto; margin: 0 -16px; padding: 4px 16px 8px; display: flex; flex-direction: column; gap: 12px">
  <div class="u d2" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px 12px; padding: 4px 2px">
    <sc-for list="{{cats}}" as="c" hint-placeholder-count="12"><button type="button" class="cat pr" onClick="{{c.pick}}" aria-pressed="{{c.attr}}"><img src="{{c.src}}" alt="">{{c.n}}</button></sc-for>
  </div>
  <sc-if value="{{none}}" hint-placeholder-val="{{ false }}"><span style="text-align: center; font-size: 14px; color: var(--ink2); padding: 10px">Nu găsim „{{q}}”. Alege cea mai apropiată categorie, iar în profil scrii exact ce faci.</span></sc-if>
  <sc-if value="{{showAll}}" hint-placeholder-val="{{ true }}"><button type="button" onClick="{{more}}" class="pr" style="align-self: center; height: 36px; padding: 0 16px; border: 0; border-radius: 18px; background: var(--surf); color: var(--btext); font-family: inherit; font-size: 14px; font-weight: 500; cursor: pointer">Vezi toate cele 30 de categorii</button></sc-if>
  </div>
  <div class="grp"><div class="rw" style="padding-right: 12px"><span style="flex-grow: 1; display: flex; flex-direction: column"><span style="font-size: 15px">Am uneltele mele</span><span style="font-size: 12px; color: var(--ink2)">Primești și cereri „vino cu unelte”</span></span><button type="button" class="jsw" onClick="{{toggleTools}}" aria-pressed="{{toolsAttr}}" aria-label="Am uneltele mele"></button></div></div>
  <sc-if value="{{hasChosen}}" hint-placeholder-val="{{ true }}"><span style="font-size: 12px; color: var(--ink2); text-align: center">{{chosenTxt}}</span></sc-if>
  <sc-if value="{{ctaOn}}" hint-placeholder-val="{{ true }}"><a href="Identitate.dc.html" class="pr" style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--brand); color: var(--onbrand); font-size: 17px; font-weight: 500; text-decoration: none; box-shadow: 0 10px 24px rgba(255,159,10,0.32)">{{cta}}</a></sc-if>
  <sc-if value="{{ctaOff}}" hint-placeholder-val="{{ false }}"><span style="display: flex; align-items: center; justify-content: center; height: 56px; border-radius: 28px; background: var(--surf3); color: var(--ink2); font-size: 16px; font-weight: 500">{{cta}}</span></sc-if>
</div>'''
    return page('Ce știi să faci', 'L', b, SK_CSS, logic)


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
        hasSpecs: k.specs.length > 0, specs: k.specs.map((sp, si) => ({ t: sp[0], attr: sp[1] ? 'true' : 'false', pick: () => this.upd(k.i, (x) => { x.specs = x.specs.map((y, yi) => yi === si ? [y[0], !y[1]] : y); return x; }) })),
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
    b = '''<div class="scroll colfix" style="height: 100%; overflow-y: auto; box-sizing: border-box; padding: 52px 16px 120px; display: flex; flex-direction: column; gap: 12px">
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
        <sc-if value="{{k.hasSpecs}}" hint-placeholder-val="{{ true }}"><span style="font-size: 13px; font-weight: 500; color: var(--ink2)">Ce faci exact</span>
        <div style="display: flex; gap: 6px; flex-wrap: wrap"><sc-for list="{{k.specs}}" as="x" hint-placeholder-count="4"><button type="button" class="chip" onClick="{{x.pick}}" aria-pressed="{{x.attr}}">{{x.t}}</button></sc-for></div></sc-if>
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
    return page('Profilul meu (Jobzer)', 'L', b, SK_CSS, logic, )


SKILL_PAGES = [('Skilluri', skilluri), ('ProfilEdit', profil_edit)]

if __name__ == '__main__':
    for _n, _f in SKILL_PAGES:
        write(_n + '.dc.html', _f())


# ================================================================ ACASĂ JOBZER v2: cererile ca listă (și hartă), cu ofertă rapidă, filtre, live
FEED = [
    dict(id='r1', i='mobila', t='Montaj birou + dulap mic', z='Floreasca', km=2.1, cl='Andrei P.', st='4,9', when='u', wt='Urgent · cât mai repede', lo=120, hi=220, dur='~1 h 30', ph=2, tools='Cu uneltele tale', of=3, left=480, m='Montaj mobilier · Expert', x=128, y=150),
    dict(id='r5', i='it', t='Montaj TV 55" pe perete', z='Floreasca', km=0.9, cl='Mara S.', st='5,0', when='u', wt='Urgent · în următoarea oră', lo=100, hi=180, dur='~1 h', ph=1, tools='Suportul îl are clientul', of=5, left=250, m='Montaj TV și rafturi · din Montaj mobilier', x=222, y=190),
    dict(id='r2', i='reparatii', t='Agățat 3 rafturi și o oglindă', z='Dorobanți', km=3.4, cl='Ioana M.', st='5,0', when='a', wt='Azi · 18:00', lo=80, hi=140, dur='~1 h', ph=1, tools='Cu uneltele tale', of=1, left=1320, m='Reparații mici · Experimentat', x=70, y=225),
    dict(id='r3', i='tamplarie', t='Reglat ușa de la baie', z='Aviatorilor', km=1.2, cl='Radu T.', st='4,7', when='a', wt='Azi · 20:00', lo=60, hi=110, dur='~40 min', ph=0, tools='Cu uneltele tale', of=0, left=2100, m='Tâmplărie și uși · Experimentat', x=305, y=110),
    dict(id='r4', i='mobila', t='Montaj pat cu sertare IKEA', z='Herăstrău', km=4.8, cl='Elena D.', st='4,8', when='p', wt='Sâm., 18 oct. · 10:00', lo=150, hi=250, dur='~2 h', ph=3, tools='Cu uneltele tale', of=2, left=10800, m='Montaj mobilier · Expert', x=268, y=250),
    dict(id='r6', i='mobila', t='Dulap PAX de 2 m', z='Pipera', km=6.2, cl='Victor A.', st='4,6', when='p', wt='Dum., 19 oct. · 12:00', lo=250, hi=400, dur='~3 h', ph=2, tools='Cu uneltele tale', of=1, left=18000, m='Montaj mobilier · Expert', x=320, y=60),
]
FEED_NEW = dict(id='r7', i='tamplarie', t='Montaj 2 uși interioare', z='Primăverii', km=2.8, cl='Sorin V.', st='4,9', when='a', wt='Azi · 17:00', lo=200, hi=350, dur='~2 h 30', ph=2, tools='Cu uneltele tale', of=0, left=1800, m='Tâmplărie și uși · Experimentat', x=150, y=80)

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
      return { id: r.id, t: r.t, src: 'assets/cat/' + r.i + '.svg', meta: r.z + ' · ' + String(r.km).replace('.', ',') + ' km · client ★ ' + r.st, wt: r.wt, wst: 'height: 24px; padding: 0 9px; border-radius: 12px; font-size: 12px; font-weight: 600; display: inline-flex; align-items: center; white-space: nowrap; ' + wc,
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
      head: cnt('all') + (cnt('all') === 1 ? ' cerere' : ' cereri'), newBadge: s.gotNew, sub: 'Pe competențele tale, în 5 km',
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
              '<circle cx="196" cy="170" r="95" fill="#FF9F0A" fill-opacity="0.07" stroke="#FF9F0A" stroke-opacity="0.35" stroke-dasharray="4 5"></circle>'
              '<circle cx="196" cy="170" r="9" style="fill: var(--invbg); stroke: var(--surf)" stroke-width="4"></circle></svg>')
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
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 6px">
      <a href="''' + S('Statistici.dc.html') + '''" class="pr" style="background: var(--surf); border-radius: 16px; padding: 8px 10px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 15px; font-weight: 600">78 lei/h</span><span style="font-size: 11px; color: var(--ink2)">statistici ›</span></a>
      <a href="''' + S('Niveluri.dc.html') + '''" class="pr" style="background: var(--surf); border-radius: 16px; padding: 8px 10px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 15px; font-weight: 600">Plus</span><span style="font-size: 11px; color: var(--ink2)">38/50 → Gold</span></a>
      <a href="''' + S('Promovare.dc.html') + '''" class="pr" style="background: var(--bsoft); border-radius: 16px; padding: 8px 10px; display: flex; flex-direction: column; color: var(--ink); text-decoration: none"><span style="font-size: 15px; font-weight: 600">1 h 20</span><span style="font-size: 11px; color: var(--btext); font-weight: 500">promovat ›</span></a>
    </div>
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
    <div style="position: absolute; left: 12px; right: 12px; bottom: 100px; z-index: 5"><sc-for list="{{sel}}" as="c" hint-placeholder-count="1">''' + rq + '''</sc-for></div>
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

if __name__ == '__main__':
    write('Castig.dc.html', castig_v2('L'))
    write('CastigDark.dc.html', castig_v2('D'))


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
      bands: bandBars, resp: resp, cmpTxt: 'Săgețile compară cu ' + { 7: 'cele 7 zile', 30: 'cele 30 de zile', 90: 'cele 3 luni' }[s.p] + ' dinainte.' };
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
        <div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 8px; align-items: end; height: 82px; margin-top: 6px"><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 38px; border-radius: 7px; background: rgba(128,128,128,.45)"></div><span style="font-size: 11px; opacity: .7">L</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 12px; border-radius: 7px; background: rgba(128,128,128,.45)"></div><span style="font-size: 11px; opacity: .7">Ma</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 30px; border-radius: 7px; background: rgba(128,128,128,.45)"></div><span style="font-size: 11px; opacity: .7">Mi</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 6px; border-radius: 7px; background: rgba(128,128,128,.45)"></div><span style="font-size: 11px; opacity: .7">J</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 60px; border-radius: 7px; background: var(--brand)"></div><span style="font-size: 11px; opacity: 1">V</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 6px; border-radius: 7px; background: rgba(128,128,128,.3)"></div><span style="font-size: 11px; opacity: .7">S</span></div><div style="display: flex; flex-direction: column; align-items: center; gap: 4px"><div style="width: 100%; height: 6px; border-radius: 7px; background: rgba(128,128,128,.3)"></div><span style="font-size: 11px; opacity: .7">D</span></div></div>
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
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px"><sc-for list="{{kpis}}" as="k" hint-placeholder-count="4"><div style="background: var(--surf); border-radius: 20px; padding: 12px; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 12px; color: var(--ink2)">{{k.t}}</span><span style="font-size: 22px; font-weight: 600; letter-spacing: -0.4px; font-variant-numeric: tabular-nums">{{k.v}}</span><span style="{{k.dSt}}">{{k.d}}</span></div></sc-for></div>
      <span style="font-size: 11px; color: var(--ink2); padding: 0 6px; margin-top: -4px">{{cmpTxt}}</span>

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

if __name__ == '__main__':
    write('Incasari.dc.html', incasari_v2('L'))
    write('IncasariDark.dc.html', incasari_v2('D'))
