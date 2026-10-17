# Zee — original Jobzee mascot: a chubby orange location pin, after the logo mark. One SVG per expression.
import os
OUT = os.path.join(os.path.dirname(__file__), 'jobzee-design', 'project', 'assets', 'mascot')
os.makedirs(OUT, exist_ok=True)

INK = '#1C1C1E'
ARM = '#F28500'

BODY = ('<defs><linearGradient id="g" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#FFC15E"/><stop offset="1" stop-color="#FF8A00"/></linearGradient></defs>'
        '<ellipse cx="60" cy="126" rx="22" ry="4" fill="#000" opacity=".12"/>'
        '<path d="M60 8C33 8 14 27 14 53c0 30 46 68 46 68s46-38 46-68C106 27 87 8 60 8z" fill="url(#g)"/>'
        '<path d="M30 30c6-10 16-15 27-16" stroke="#FFF" stroke-opacity=".55" stroke-width="6" stroke-linecap="round" fill="none"/>')
CHEEKS = '<ellipse cx="35" cy="66" rx="7" ry="4.5" fill="#FF5C7A" opacity=".45"/><ellipse cx="85" cy="66" rx="7" ry="4.5" fill="#FF5C7A" opacity=".45"/>'


def eyes(dx=0, dy=0):
    s = ''
    for cx in (46, 74):
        s += '<ellipse cx="%d" cy="50" rx="9" ry="10.5" fill="#FFF"/>' % cx
        s += '<circle cx="%.1f" cy="%.1f" r="5.2" fill="%s"/>' % (cx + dx, 51 + dy, INK)
        s += '<circle cx="%.1f" cy="%.1f" r="1.8" fill="#FFF"/>' % (cx + dx + 1.8, 49 + dy)
    return s


def arm(d):
    return '<path d="%s" stroke="%s" stroke-width="9" stroke-linecap="round" fill="none"/>' % (d, ARM)


HAPPY_EYES = ''.join('<path d="M%d 52 Q%d 43 %d 52" stroke="%s" stroke-width="4.5" stroke-linecap="round" fill="none"/>' % (c - 8, c, c + 8, INK) for c in (46, 74))
SLEEP_EYES = ''.join('<path d="M%d 51 Q%d 57 %d 51" stroke="%s" stroke-width="4" stroke-linecap="round" fill="none"/>' % (c - 8, c, c + 8, INK) for c in (46, 74))
SPARK = lambda x, y, s, c='#FFC15E': '<path d="M%g %gl%g %g %g %g -%g %g -%g -%g -%g -%g z" fill="%s"/>' % (x, y - s, s * .3, s * .7, s * .7, s * .3, s * .7, s * .3, s * .3, s * .7, s * .3, s * .7, c)


def spark(x, y, s, c='#FFB000'):
    return ('<path d="M{x} {a} Q{x} {y} {b} {y} Q{x} {y} {x} {c} Q{x} {y} {d} {y} Q{x} {y} {x} {a}z" fill="{col}"/>'
            .format(x=x, y=y, a=y - s, c=y + s, b=x + s, d=x - s, col=c))


EXPR = {
    # greeting: waving right arm
    'salut': arm('M100 56 Q112 44 110 30') + arm('M21 62 Q12 70 12 80') + eyes() + CHEEKS +
             '<path d="M49 66 Q60 77 71 66" stroke="%s" stroke-width="4.5" stroke-linecap="round" fill="none"/>' % INK +
             '<path d="M114 20 l4 -5 M118 30 l6 -2" stroke="#FFB000" stroke-width="3" stroke-linecap="round"/>',
    # happy: ^^ eyes, open smile
    'fericit': arm('M21 62 Q12 70 12 80') + arm('M99 62 Q108 70 108 80') + HAPPY_EYES + CHEEKS +
               '<path d="M47 64 Q60 64 73 64 Q72 80 60 80 Q48 80 47 64z" fill="%s"/><path d="M53 74 Q60 70 67 74 Q64 79 60 79 Q56 79 53 74z" fill="#FF5C7A"/>' % INK +
               spark(104, 18, 7) + spark(16, 22, 5),
    # thinking: eyes up, hand on chin, thought dots
    'gandeste': arm('M22 62 Q34 82 50 78') + arm('M99 62 Q108 70 108 80') + eyes(2.5, -3) + CHEEKS +
                '<path d="M53 69 Q60 67 68 70" stroke="%s" stroke-width="4" stroke-linecap="round" fill="none"/>' % INK +
                '<circle cx="98" cy="22" r="3.5" fill="#C7C7CC"/><circle cx="106" cy="13" r="4.5" fill="#C7C7CC"/><circle cx="114" cy="4" r="3" fill="#C7C7CC"/>',
    # searching: magnifier
    'cauta': arm('M21 62 Q12 70 12 80') + arm('M99 60 Q104 66 100 74') + eyes(3, 0) + CHEEKS +
             '<path d="M51 67 Q60 73 69 67" stroke="%s" stroke-width="4" stroke-linecap="round" fill="none"/>' % INK +
             '<circle cx="104" cy="84" r="12" fill="#BCDDF7" fill-opacity=".7" stroke="%s" stroke-width="5"/><path d="M112 93 l7 8" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % (INK, INK),
    # oops: worried brows, small mouth, sweat drop
    'ups': arm('M22 60 Q14 50 18 40') + arm('M98 60 Q106 50 102 40') + eyes(0, 1) + CHEEKS +
           '<path d="M39 41 L52 37.5 M81 41 L68 37.5" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % INK +
           '<ellipse cx="60" cy="71" rx="5.5" ry="6.5" fill="%s"/>' % INK +
           '<path d="M96 22 Q102 32 96 36 Q90 32 96 22z" fill="#64B5F6"/>',
    # sad: frown, tear
    'trist': arm('M21 64 Q14 74 16 84') + arm('M99 64 Q106 74 104 84') + eyes(0, 2) +
             '<path d="M38 41 L52 37 M82 41 L68 37" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % INK +
             '<path d="M50 73 Q60 65 70 73" stroke="%s" stroke-width="4.5" stroke-linecap="round" fill="none"/>' % INK +
             '<path d="M38 60 Q42 68 38 71 Q34 68 38 60z" fill="#64B5F6"/>',
    # sleeping: closed eyes, zzz
    'doarme': arm('M24 66 Q32 76 44 76') + arm('M96 66 Q88 76 76 76') + SLEEP_EYES + CHEEKS +
              '<ellipse cx="60" cy="69" rx="4" ry="3.2" fill="%s"/>' % INK +
              '<path d="M92 22 h10 l-10 11 h10 M106 6 h7 l-7 8 h7" stroke="#8E8E93" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
    # celebrating: arms up, confetti
    'sarbatoare': arm('M22 54 Q10 40 12 24') + arm('M98 54 Q110 40 108 24') + HAPPY_EYES + CHEEKS +
                  '<path d="M46 63 Q60 63 74 63 Q73 82 60 82 Q47 82 46 63z" fill="%s"/><path d="M52 75 Q60 70 68 75 Q65 81 60 81 Q55 81 52 75z" fill="#FF5C7A"/>' % INK +
                  '<rect x="4" y="8" width="7" height="4" rx="2" fill="#34C759" transform="rotate(-30 7 10)"/><rect x="104" y="4" width="8" height="4" rx="2" fill="#007AFF" transform="rotate(25 108 6)"/>'
                  '<rect x="30" y="0" width="6" height="4" rx="2" fill="#FF2D55" transform="rotate(40 33 2)"/><rect x="84" y="2" width="6" height="4" rx="2" fill="#AF52DE" transform="rotate(-20 87 4)"/>'
                  + spark(60, 2, 5) + spark(116, 40, 4, '#34C759') + spark(4, 40, 4, '#FF2D55'),
    # earning: holding a coin
    'bani': arm('M21 62 Q12 70 12 80') + arm('M99 62 Q104 70 100 76') + HAPPY_EYES + CHEEKS +
            '<path d="M49 66 Q60 77 71 66" stroke="%s" stroke-width="4.5" stroke-linecap="round" fill="none"/>' % INK +
            '<circle cx="104" cy="86" r="13" fill="#FFD60A" stroke="#E0A800" stroke-width="3"/><text x="104" y="89.5" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="800" fill="#8A5A00">lei</text>'
            + spark(112, 62, 4),
}

for name, inner in EXPR.items():
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="130" viewBox="0 0 124 130">' + BODY + inner + '</svg>'
    with open(os.path.join(OUT, 'zee-%s.svg' % name), 'w') as f:
        f.write(svg)
print(sorted(os.listdir(OUT)))
