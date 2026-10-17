# ChatBubble

Bulele de mesaj din chat și din dialogul cu Jobzee, cu indicatorul „scrie…”.

## Reguli

- Ale tale: dreapta, `brand` cu text `ink-on-brand`, colțul de jos-dreapta 6 px.
- Ale celuilalt (sau Jobzee): stânga, `surface-2`, colțul de jos-stânga 6 px.
- Text `callout` (16 px), maxim 76% din lățime. Bulele noi intră cu `jz-up` în 380 ms.
- Înainte de un răspuns automat: trei puncte (`jz-typing`) ~1 s.
- Pozele trimise: miniatură 150 × 100 px, `radius-lg`, deasupra textului.
- Sus, o etichetă mică `ink-3`: numerele de telefon rămân ascunse.

## Conversații

- Fiecare cerere are conversația ei. Când cererea se încheie (trimisă, finalizată, anulată), conversația trece în Istoric, doar pentru citire, iar pentru o lucrare nouă pornește o conversație nouă, marcată cu „Conversație nouă · azi, 12:03”.
- Fiecare mesaj are id unic. Cât timp celălalt scrie, nu se mai trimite nimic; dublul tap pe același răspuns rapid e ignorat. Un răspuns rapid folosit dispare.
- Jobzee nu repetă o întrebare la care s-a răspuns deja; dacă nu înțelege, cere o singură clarificare, cu alte cuvinte.
