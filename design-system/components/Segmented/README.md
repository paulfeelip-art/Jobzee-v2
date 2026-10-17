# Segmented

Selectorul segmentat iOS: 2–4 opțiuni egale, una activă, pentru sortare și filtre.

## Reguli

- Șina: `surface-3`, raza 10 px, padding 2 px. Segmentul activ: `surface`, `radius-seg`, umbră mică.
- Text `footnote` semibold, `ink`. Etichete scurte (max. 12 caractere): „Recomandat”, „Preț”, „Distanță”, „Notă”.
- Schimbarea mută fundalul alb în `dur-state`. Conținutul de sub selector se schimbă imediat, cu apariție `jz-enter`.
- Folosește `aria-pressed` (în app: `accessibilityState.selected`).
- Peste 4 opțiuni: chip-uri, nu segmentat.
