# ListGroup

Lista grupată în stil Setări iOS: un card `surface` cu rânduri separate de linii fine, folosită pentru detalii, prețuri și setări.

## Anatomie

- Eticheta de secțiune (`jz-label`) deasupra, majuscule, `ink-2`.
- Cardul `jz-group`: `surface`, `radius-lg`, fără umbră.
- Rândul `jz-row`: minim 48 px, padding 11 × 16 px. Stânga: iconiță opțională în pătrat 30 px colorat, apoi titlu (`body`) și subtitlu (`footnote`, `ink-2`). Dreapta: valoare (`ink-2`) și chevron `ink-3` dacă rândul deschide ceva.
- Separator: 0,5 px `separator`, începe la 16 px din stânga (rândurile 2+).

## Reguli

- Sumele din liste stau aliniate la dreapta, cu `tabular-nums`; totalul e ultimul rând, semibold.
- Rândul care se atinge are chevron și reacție la apăsare (fundal `surface-2`).
- Nu pune carduri în carduri; o listă grupată are maximum 8 rânduri.
