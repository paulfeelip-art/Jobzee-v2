# OfferRow

Rândul unei oferte din lista „Oferte primite”: cine, cât de bine se potrivește și cât costă în total, ales cu o atingere.

## Anatomie

- Avatar 46 px (inițiale pe `brand-soft-2`), apoi nume (`headline`) + insigna de nivel (`jz-pill--tier`) + „Promovat” dacă e cazul.
- Meta (`footnote`, `ink-2`): „4,9 ★ · 86 sarcini · 98% potrivire”.
- Dreapta: **totalul cu taxa Jobzee** (`headline`, tabular) și dedesubt „6 min · 1,4 km”.

## Stări

- Normal: `surface` cu contur interior de 1 px `surface-2`.
- Ales: `brand-soft` + contur 2 px `brand`. Butonul de jos se schimbă în „Alege Mihai · 172,50 lei”.
- Promovat: eticheta „Promovat” e obligatorie (regulament UE 2019/1150) și stă lângă nume, nu ascunsă.

## Reguli

- Ordinea „Recomandat”: promovate, apoi după potrivire. Celelalte sortări sunt pure (preț, distanță, notă).
- Rândurile apar decalat cu 70 ms la încărcare.
