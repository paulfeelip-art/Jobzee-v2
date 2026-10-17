# LiveActivity

Bara neagră în stil Dynamic Island care arată Jobzerul pe drum: cine vine, progresul și minutele rămase.

## Reguli

- Fundal `island` (negru în ambele teme), 300 × 52 px, `radius-pill`. Avatar 36 px, nume 13 px semibold, bară de progres 4 px `brand`, minutele 20 px bold `brand`.
- Intră lărgindu-se din centru (de la 120 la 300 px) cu `ease-sheet`.
- Progresul și minutele se actualizează live din poziția Jobzerului.
- În aplicație e o bară sus pe ecranul Pe drum. Pe iOS, aceeași informație devine Live Activity reală (ActivityKit) pe ecranul blocat; pe Android, notificare continuă.
