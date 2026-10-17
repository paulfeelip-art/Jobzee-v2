# TabBar

Meniul de jos plutitor, din sticlă, cu 4 secțiuni. Clientul și Jobzerul au fiecare meniul lui.

## Conținut

- Client: Acasă, Activitate, Mesaje, Cont.
- Jobzer: Acasă, Sarcini, Încasări, Profil.

## Reguli

- Plutește la `space-6` de jos și 16 px lateral; 64 px înălțime; `radius-pill`; material `glass` cu blur 24 px și `shadow-float`.
- Tab-ul activ: pastilă `brand-soft`, iconiță plină și text `brand-text`. Celelalte: iconiță contur, `ink-2`.
- Etichete `caption` (11 px). Mereu text + iconiță.
- Conținutul ecranului se termină cu 100 px deasupra marginii de jos, ca nimic să nu stea sub meniu.
- În app: `BlurView` peste conținut, `tabBarStyle` absolut.
