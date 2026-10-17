# Button

Butonul pastilă al Jobzee: unul portocaliu pe ecran pentru acțiunea principală, restul secundare sau linkuri.

## Variante

| Variantă | Clasă | Când |
|---|---|---|
| Principal | `jz-btn jz-btn--primary` | Acțiunea care duce mai departe: „Trimite cererea”, „Confirmă · blochează 172,50 lei”. Una pe ecran. |
| Secundar | `jz-btn--secondary` | A doua opțiune: „Păstrează sarcina”, „Scrie adresa”. |
| Închis | `jz-btn--dark` | Plata cu Face ID / Apple Pay, „Continuă cu Apple”. |
| Pericol | `jz-btn--danger` | Anulare. Fundal `danger-soft`, text `danger-text`. |
| Simplu | `jz-btn--plain` | Linkuri în bară: „Înapoi”, „Modifică”, „Mai târziu”. |
| Mic | `jz-btn--sm` | Butoane în carduri și foi (44 px). |

## Reguli

- Înălțime 56 px (44 px mic), lățime toată pe ecrane, `radius-pill`, text `headline`.
- Pe portocaliu textul e `ink-on-brand`, niciodată alb.
- Eticheta spune exact ce se întâmplă și, la plăți, include suma.
- Apăsare: scale 0,96 cu `ease-spring`, plus haptic ușor pe telefon.
- Dezactivat: fundal `surface-3`, text `ink-2`, fără umbră. Explică lângă buton de ce e dezactivat.
- Focus vizibil: contur 3 px `brand-text`.
