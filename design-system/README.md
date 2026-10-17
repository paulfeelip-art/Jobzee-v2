# Jobzee Design System

Jobzee e o aplicație pentru sarcini scurte, aproape de tine: clientul spune de ce are nevoie, Jobzee pregătește fișa cererii, Jobzerii din zonă trimit oferte, clientul alege una. Sistemul de design descrie aspectul aplicației mobile (iOS și Android), în stil Apple: clar, rotunjit, calm, cu portocaliul Jobzee ca singur accent.

Sursa: canvas-ul de design „Jobzee App Screens” (54 de ecrane, octombrie 2026). Valorile de aici sunt cele din ecrane, cu două corecții de contrast notate la Culori.

## Principii

1. **O singură acțiune principală pe ecran.** Butonul portocaliu e mereu jos, pe toată lățimea, la 16 px de margini. Restul acțiunilor sunt secundare (`surface`) sau linkuri (`brand-text`).
2. **Simplu pentru oricine.** Text mare (minim 15 px pentru tot ce se citește), zone de atingere de minim 44 px, cuvinte de zi cu zi. Jobzee completează, omul doar confirmă.
3. **Încredere la fiecare pas.** Unde omul ezită, spunem clar ce se întâmplă cu banii: „Suma doar se blochează pe card”, „Refuzul nu te penalizează”.
4. **Totul e rotund.** Butoane și chip-uri pastilă (`radius-pill`), carduri la 22 px (`radius-lg`), foi la 34 px (`radius-sheet`). Nimic cu colțuri drepte.
5. **Mișcare cu rost.** Animațiile arată ce s-a schimbat: o listă care apare, un pin care cade, o bifă care se desenează. Niciodată decor.

## Voce și ton

- Limba aplicației e româna, cu diacritice. Codul și comentariile sunt în engleză.
- Persoana care face sarcina se numește **Jobzer** (plural Jobzeri). Niciodată „helper” sau „prestator”. Aplicația e **Jobzee**.
- Vorbim la persoana a doua, direct: „Cu ce te ajutăm?”, „Ești online”, „Plătești doar după ce confirmi”.
- Butoanele spun exact ce fac: „Trimite cererea”, „Confirmă · blochează 172,50 lei”, „Am terminat”.
- Erorile spun ce s-a întâmplat și ce poți face, fără scuze: „Banca a refuzat plata. Nu s-a blocat nimic pe card.”
- Fără emoji. Fără exclamații în serie. Un singur „Gata!” la final e în regulă.
- **Jobzee vorbește ca un prieten respectuos și de ajutor.** Spune „eu” când face ceva („Am pregătit cererea”, „Îți scriu imediat ce primești o ofertă”), propune, nu impune. Nu se numește niciodată „AI”, „asistent AI” sau „robot”: este pur și simplu Jobzee.
- Româna e corectă și firească: „de ce ai nevoie” (nu „ce ai nevoie”), diacritice cu virgulă (ș, ț), ghilimele „…”.

## Bani

- Sumele sunt în **lei**, cu virgulă zecimală și două zecimale: `172,50 lei`. Peste 1.000: `1.284,00 lei`.
- În cod, banii sunt întotdeauna numere întregi în **bani** (1 leu = 100 bani). Niciodată float.
- Clientul plătește prețul Jobzerului + **taxa Jobzee de 15%** (minim). Jobzerul primește **100%** din prețul lui.
- Pe fiecare ecran de plată arătăm: prețul Jobzerului, taxa Jobzee 15%, totalul. Mereu în această ordine.
- Cifrele care se schimbă sau stau în coloană folosesc `font-variant-numeric: tabular-nums`.

## Culori

Două teme: **Luminos** (implicit) și **Întunecat**. Fiecare culoare are valoare în ambele.

| Rol | Token | Notă |
|---|---|---|
| Fundal ecran | `bg` | Gri Apple în luminos, negru pur în întunecat |
| Carduri, foi | `surface` | Alb / gri închis |
| Umplutură în card | `surface-2` | Butoane secundare, câmpuri |
| Text | `ink`, `ink-2` | `ink-3` doar pentru placeholder |
| Accent | `brand` `#ff9f0a` | Butonul principal, pinul tău, traseul, selecția |
| Text pe accent | `ink-on-brand` | Aproape negru. **Niciodată alb pe portocaliu** (2,2:1) |
| Text portocaliu | `brand-text` | Linkuri, „Înapoi”, etichete active |
| Selecție | `brand-soft`, `brand-soft-2` | Fundal pentru elementul ales, avatare |
| Stări | `success*`, `danger*`, `info` | Verde = confirmat/online, roșu = anulare/eroare |
| Hartă | `map-land`, `map-road`, `map-park`, `map-water` | Stil Apple Maps, luminos și întunecat |
| Materiale | `glass`, `scrim`, `island` | Sticlă cu blur 24 px; scrim sub foi modale |

**Corecții față de mockup-uri:** în ecrane, textul portocaliu era `#c25e00` (4,3:1 pe alb, sub pragul de 4,5:1) și textul verde `#248a3d` (4,4:1). Sistemul folosește `brand-text #b35600` (4,9:1) și `success-text #1f7a35` (5,4:1). La implementare se folosesc valorile din sistem.

Reguli:
- Portocaliul plin apare o singură dată pe ecran ca buton. Restul portocaliului e accent mic (selecție, pin, progres).
- Starea selectată se arată prin fundal `brand-soft` + contur `brand` de 2 px, nu doar prin culoare: are și bifă sau contur.
- Verdele și roșul nu se folosesc decorativ.

## Tipografie

Greutăți fine: titlurile sunt semibold (600), rândurile și butoanele medium (500), textul regular (400). Nimic peste 700.


Fontul de sistem Apple (SF Pro pe iOS). Pe Android: fontul de sistem (Roboto), cu aceleași mărimi. Nu încărcăm fonturi externe.

- `large-title` 34/40 bold pentru ecranele din meniu; `title-1` 28 pentru ecranele de pas.
- `headline` 17 semibold pentru nume și butoane; `body` 17 pentru text.
- `footnote` 13 pentru meta (notă, distanță, sarcini). Nimic sub 11 px, iar 11 px doar în meniul de jos și insigne.
- Cifre mari: `numeral-xl` (cronometre), `numeral-l` (sume), `numeral-code` (codul de start, spațiere 8 px).
- Titlurile au spațiere negativă între litere (−0,4 până la −0,9 px), textul de bază nu.

## Spațiere și forme

- Marginea ecranului: `space-4` (16 px). Între carduri: `space-3` (12 px). Padding în card: 14–16 px.
- Listele grupate (stil Setări iOS): card `surface` cu `radius-lg`, rânduri de minim 48 px, separator de 0,5 px `separator` începând de la 16 px din stânga.
- Etichetele de secțiune: `section-label`, majuscule, `ink-2`, deasupra cardului, la 16 px de margine.
- Meniul de jos plutește la `space-6` de jos și 16 px lateral, înălțime 64, `radius-pill`, material `glass`.

## Mișcare

| Animație | Unde | Timp / easing |
|---|---|---|
| Apariție de jos în sus | Titluri, carduri, rânduri; decalaj 80 ms | `dur-enter`, `ease-out` |
| Apăsare | Orice buton sau rând atins: scale 0,96 | `dur-press`, `ease-spring` |
| Foaie care urcă | Foi de jos, plata, muncă în plus | `dur-sheet`, `ease-sheet` |
| Pin care cade | Jobzerii pe hartă, cu mic rebound | 800 ms, `ease-out` |
| Puls | Locația ta, „online” | 2,4 s, buclă |
| Traseu care se desenează | Pe drum, spre client | `dur-draw` |
| Bifă care se desenează | Plată confirmată, ofertă trimisă | 500 ms după `ease-pop` |
| Tremur | Cod greșit, plată refuzată | 500 ms |
| Trei puncte „scrie…” | Jobzee și chat | 1,2 s, buclă |
| Schelet cu luciu | Încărcare | 1,4 s, buclă |

- Dacă telefonul are „Reducere mișcare”, toate animațiile se opresc și elementele apar direct.
- Pe telefon, apăsarea butonului principal are și un haptic ușor; bifele de succes au haptic de succes.

## Iconografie

- Linie de 2 px, capete și colțuri rotunjite, grilă de 24 px, ca SF Symbols. Iconița activă din meniu e plină.
- Iconițele de categorie stau în pătrate rotunjite de 72 px cu fundal pal colorat (Montaj portocaliu, Curățenie albastru, Cărat verde, Reparații violet), doar pe ecranul Acasă.
- Fără emoji, fără ilustrații cu oameni. Avatarele sunt inițiale pe `brand-soft-2` până există poză.

## Logo

Logo-ul oficial: pinul portocaliu cu cheie franceză decupată, plus wordmark-ul „jobzee” (`job` gri, `zee` portocaliu). Fișierele sunt în `assets/brand/`:

| Fișier | Când |
|---|---|
| `jobzee-logo.png` | Orizontal: antete, ecran de autentificare, e-mailuri. |
| `jobzee-logo-stacked.png` | Stivuit: splash, pagini de prezentare. |
| `jobzee-mark.png` | Doar semnul: notificări, avatarul Jobzee, pinul din centrul radarului. |
| `jobzee-wordmark.png` | Doar textul, lângă semn când spațiul e îngust. |

Reguli: semnul nu se rotește, nu se recolorează, nu se deformează (se scalează doar după înălțime, lățimea automată). Spațiu liber minim în jur: jumătate din lățimea semnului. Pe fundal întunecat se folosește același fișier: gri-ul din „job” rămâne lizibil. Fișierele sunt raster din materialele primite; pentru producție e nevoie de master-ul vectorial (SVG).

## Mascota

Mascota e logo-ul cu brațe și pantofi: pinul cu cheie, mâini albe în mănuși, pantofi albi cu detalii portocalii. **Nu are față** (fără ochi sau gură) și nu se redesenează: emoția o dă poza. Fișierele sunt în `assets/mascot/`.

| Poză | Fișier | Unde |
|---|---|---|
| Salut | `zee-salut.png` | Bun venit, permisiuni, suport |
| Gândește (animat) | `zee-gandeste.png` | Jobzee se gândește |
| Caută (animat) | `zee-cauta.png` | Radar fără oferte, locație oprită |
| Potrivește (animat) | `zee-potrivire.png` | Radar cu primele oferte |
| Ascultă (animat) | `zee-asculta.png` | Dictare vocală |
| Bravo | `zee-fericit.png`, `zee-card-bravo.png` | Fișă gata, 3+ oferte |
| Sare de bucurie | `zee-sarbatoare.png` | Plată reușită, serie pornită |
| La treabă | `zee-bani.png` | Start Jobzer, încasări |
| Pe drum | `zee-alearga.png` | Jobzerul vine |
| Arată | `zee-arata.png` | Sfaturi, pasul următor |
| Verifică telefonul | `zee-ups.png` | Fără internet, plată refuzată |
| Ridică din umeri | `zee-trist.png` | Anulare, ofertă pierdută |
| La laptop | `zee-doarme.png`, `zee-card-asistent.png` | Ecrane goale |

Reguli: o singură mascotă pe ecran; niciodată pe butoane, lângă sume de plătit sau în liste. Animațiile rulează la 12 fps și se opresc la „Reducere mișcare”. Pozele `card-*` au fundalul lor crem și se pun pe `#FBF1E3` și în dark.

## Accesibilitate

- Text 4,5:1 pe fundalul lui în ambele teme (3:1 de la 24 px). Tokenii de text sunt verificați la valorile din tabelul de culori.
- Zone de atingere de minim 44 × 44 px.
- Iconițele fără text au etichetă (`accessibilityLabel`).
- Starea nu se transmite doar prin culoare: selecția are contur, erorile au iconiță și text.

## Componente

Brand (logo), mascotă, butoane, liste grupate, selector segmentat, comutator, chip-uri, rândul de ofertă, meniul de jos, foaia de jos, codul de start, bara Live Activity, bule de chat, schelet, selectorul de rol, recomandarea Jobzee, radarul live și butonul SOS. Fiecare are pagina lui cu stări și reguli. Clasele CSS din `components/bundle.css` sunt referința vizuală; aplicația le implementează ca stiluri React Native (vezi secțiunea Implementare).
