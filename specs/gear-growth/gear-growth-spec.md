# Jobzee Gear & Growth — Specificație de produs

Oct 17, 2026 · @paul · Faza de design, fără cod

## Rezumat și decizii de confirmat

Gear & Growth devine al doilea domeniu comercial al Jobzee, separat de marketplace. Jobzerul își cumpără unelte, kituri, haine personalizate și materiale tipărite, fabricate sau livrate de parteneri, fără stoc propriu la lansare. Intrarea e din profilul Jobzerului, iar cele patru tab-uri din meniul de jos rămân neschimbate. Banii din comenzi nu se amestecă niciodată cu taxa de potrivire.

Înainte de design trebuie confirmate cinci decizii:

1. **Comisionul de potrivire.** Specificația spune „10% separat la client și la Jobzer”. Canvas-ul aprobat azi arată 15% la client și 0% la Jobzer, cu „Jobzerul primește 100%”. Documentul nu schimbă niciuna. Ce variantă rămâne?
2. **Cine vinde.** Propun ca Jobzee să fie vânzătorul (merchant of record) pentru kituri și produsele personalizate, iar pentru uneltele individuale să fie marketplace de parteneri. Asta decide facturarea, TVA-ul și cine răspunde de retururi.
3. **Cine poate cumpăra.** Doar Jobzerii verificați, sau orice cont? Propun: catalogul e vizibil pentru toți, comanda doar după verificarea identității.
4. **Primii parteneri.** Un furnizor de unelte, unul de print-on-demand textil și o tipografie. Fără ei, nu se poate afișa nicio disponibilitate sau termen.
5. **Canvas-ul are acum 135 de ecrane** (light și dark), nu 65. Cele 18 ecrane noi se adaugă după aprobare, tot în ambele teme.

Toate deciziile aprobate anterior rămân: rolurile client/Jobzer, prețul venit doar din oferte, Radarul, mascota oficială și regulile de brand.

## 1. Arhitectura conceptului

Jobzee are de acum două domenii care împărt doar contul și profilul public. Marketplace-ul pune în legătură cereri cu oferte. Gear & Growth vinde produse fizice și digitale. Fiecare are propriul ciclu de viață, propriile plăți și propriul suport.

| Element | Marketplace (existent) | Gear & Growth (nou) |
| --- | --- | --- |
| Ce se vinde | Potrivirea client–Jobzer | Unelte, kituri, haine, print, fișiere digitale |
| Cine plătește | Clientul (și, după decizia 1, Jobzerul) | Jobzerul |
| Bani | Blocare pe card, captură la confirmare | Plată integrală la comandă, rambursare la anulare sau retur |
| Registru | Registrul taxelor de potrivire | Registrul comenzilor comerciale, separat |
| Facturi | Factură Jobzee pentru taxă + documentul Jobzerului | Factura vânzătorului (Jobzee sau partenerul) |
| Suport | Probleme cu lucrarea, dispute | Livrare, retur, garanție |

**Ce leagă cele două domenii, și doar atât:**

- **Contul și identitatea verificată.** Aceeași persoană și același rol de Jobzer.
- **Profilul public aprobat.** Print Studio și Identity citesc din el numele, specializarea și codul QR.
- **Inventarul declarat de echipament.** Jobzerul îl completează singur, iar ce cumpără se poate adăuga cu o atingere. Inventarul e informativ: nu deblochează skill-uri și nu urcă pe nimeni în potrivire.
- **Statisticile reale de creștere.** Scanări QR, vizite pe profil și cereri venite din materialele promoționale, măsurate, niciodată estimate.

**Ce nu se întâmplă niciodată:**

- O cumpărătură nu schimbă locul Jobzerului în Radar sau în lista de oferte.
- O comandă nu se plătește din încasările marketplace și nici nu se compensează cu taxa de potrivire.
- Promovarea plătită din marketplace („Promovat”) rămâne singura formă de vizibilitate plătită și e marcată mereu.

## 2. Modelul comercial

Venitul vine din marja pe produse fabricate la comandă și din comisionul de la parteneri, fără abonament obligatoriu și fără stoc propriu. Taxa de potrivire din marketplace nu se modifică și nu se contabilizează aici.

| Sursă de venit | Cum funcționează | Cine e vânzătorul | Marjă orientativă de validat |
| --- | --- | --- | --- |
| Kituri Jobzee | Jobzee compune kitul, partenerul îl asamblează și îl livrează | Jobzee | 15–25% peste costul partenerului |
| Gear Shop (unelte individuale) | Catalogul partenerului, comanda trece prin Jobzee | Partenerul, Jobzee intermediază | Comision 5–12% de la partener |
| Identity (textile, insigne, autocolante) | Print-on-demand, fabricat după comandă | Jobzee | 25–40% peste costul de producție |
| Print Studio (cărți, flyere, magneți) | Tipografie parteneră, fișier generat automat | Jobzee | 30–50% peste costul tiparului |
| Fișiere digitale print-ready | Descărcare PDF pentru propria tipografie | Jobzee | Gratuit la lansare; ulterior preț mic per set |
| Instrumente de creștere opționale | Statistici avansate, pagină publică extinsă | Jobzee | De definit după faza 3; mereu opționale |

Marjele sunt ipoteze de pornire, nu date. Se confirmă cu oferte reale de la primii trei parteneri înainte de prețurile din aplicație.

**Reguli de preț:**

- Prețul afișat include TVA și spune separat transportul, înainte de coș.
- Kitul arată prețul fiecărui produs. Kitul nu are „reducere” artificială față de un preț umflat.
- Fără urgență falsă („mai sunt 2 bucatăți”) dacă partenerul nu o confirmă în timp real.

## 3. Cele cinci module

Fiecare modul răspunde unei singure întrebări a Jobzerului, iar toate pleacă din profilul lui aprobat.

| Modul | Întrebarea Jobzerului | Ce oferă | Ce nu face niciodată |
| --- | --- | --- | --- |
| A. Gear Kits | „Ce îmi trebuie ca să încep corect pe ce fac?” | Kituri pe serviciu, în 3 niveluri: Starter, Pro, Custom. Listă transparentă de produse, cantități, specificații, preț, disponibilitate | Nu certifică și nu deblochează skill-uri |
| B. Gear Shop | „Am nevoie de un singur lucru” | Unelte, echipament, consumabile, accesorii, protecție, piese de schimb, filtrate pe specializare | Nu recomandă agresiv și nu arată „alții au cumpărat” inventat |
| C. Identity | „Cum arăt profesionist la client?” | Tricouri, polo, hanorace, șepci, veste, genți de scule, ecusoane, autocolante, magneți auto, cu numele și specializarea | Nu pune insigne de tip „certificat” sau „verificat” dacă nu sunt adevărate în Jobzee |
| D. Print Studio | „Cum mă fac cunoscut în cartier?” | Cărți de vizită, flyere, broșuri, autocolante promo, cărți QR, branding auto, fișiere print-ready | Nu afișează telefonul, e-mailul sau adresa Jobzerului |
| E. Growth | „Ce funcționează pentru mine?” | Profil complet, echipament declarat, skill-uri, portofoliu, QR, materiale, statistici reale | Nu inventează cifre și nu promite mai multe lucrări în schimbul unei cumpărături |

**Ce înseamnă „real” în Growth:** doar evenimente măsurate de Jobzee. Exemple: scanarea unui QR, o vizită pe profilul public, o cerere trimisă de pe acel profil. Când nu există date, ecranul spune „Încă nicio scanare”, fără grafice goale sau estimări.

## 4. Taxonomia kiturilor

Opt kituri acoperă familiile de servicii cu cele mai multe cereri, fiecare în trei niveluri. Kiturile se leagă de cele 30 de familii de servicii din aplicație, nu de o listă separată.

**Niveluri:**

- **Starter:** minimul ca să accepți primele lucrări, 6–10 produse.
- **Pro:** echipament pentru lucru zilnic, cu unelte electrice și protecție completă.
- **Custom:** pleacă din Pro; Jobzerul scoate ce are deja și adaugă din Gear Shop.

| Kit | Familii de servicii acoperite | Starter (exemplu de conținut) | Ce adaugă Pro |
| --- | --- | --- | --- |
| Montaj | Montaj mobilier, Reparații mici, Tâmplărie | Șurubelniță cu bițuri (1 set), chei imbus (1 set), nivelă 60 cm, ruletă 5 m, ciocan, cutie organizator | Mașină de înșurubat cu acumulator, burghie, detector de cabluri, genunchiere |
| Curățenie | Curățenie, Geamuri, Călcat | Laveți microfibră (10), mop cu găleată, perii, mănuși (5 perechi), pulverizatoare (3), sac de transport | Aspirator compact, racletă geamuri telescopică, soluții profesionale |
| Mutat | Mutat și cărat, Livrări locale | Chingi (4), folie stretch, mănuși anti-alunecare, pături de protecție (2) | Cărucior pliabil, centuri de ridicare, cutii refolosibile |
| Tech | IT și tehnică, Foto și video | Set șurubelnițe de precizie, cabluri și adaptoare, brățară antistatică, lanternă frontală | Tester rețea, router de test, rucsac pentru echipament |
| Grădină | Grădină și curte | Foarfecă de grădină, mănuși, greblă, saci de frunze (10), ochelari de protecție | Trimmer cu acumulator, suflantă, genunchiere |
| Zugrăveli | Zugrăveli, Gresie și parchet | Role și pensule (set), tavă, bandă de mascare (5), folie de protecție, spaclu | Pistol de vopsit, scară 2 trepte, nivelă laser |
| Evenimente | Evenimente | Tricouri de staff (identity), bandă adezivă, cutter, cabluri de prelungire | Stație de încărcare, stație radio (2) |
| Handyman general | Instalații, Electricitate, Electrocasnice | Set de chei, clește, multimetru, bandă izolieră, banda teflon, cutie scule | Mașină de găurit cu percuție, detector de tensiune fără contact, lampă de lucru |

Conținutul e un exemplu de pornire. Lista finală, cu specificații și prețuri, vine din catalogul partenerului ales.

**Reguli pentru kituri:**

- Fiecare produs dintr-un kit arată: nume, cantitate, specificații, preț, disponibilitate la partener și termen de producție sau livrare.
- Orice produs se poate scoate. Prețul kitului se recalculează pe loc.
- Produsele pentru instalații și electricitate poartă nota: „Lucrările care cer autorizare (de exemplu ANRE) rămân sub regulile lor; kitul nu înlocuiește autorizarea.”
- Niciun kit nu adaugă automat skill-uri în profil și nu apare ca „certificat”.

## 5. Smart Kit Builder

Trei întrebări scurte, în stilul Jobzee AI, apoi un kit gata de ajustat. Sub un minut până la propunere. Fiecare întrebare are 2–4 răspunsuri rapide și acceptă și text liber.

**Fluxul:**

1. **„Ce servicii oferi?”** Precompletat din skill-urile profilului, cu chip-uri bifate. Jobzerul confirmă sau mai adaugă.
2. **„Ce ai deja?”** Lista de unelte de bază pentru serviciile alese, cu „Am” / „Nu am”. Se poate sări cu „Nu știu, arată-mi tot”. Ce bifează aici ajunge și în inventarul declarat, dacă vrea.
3. **„Ce nivel vrei?”** Starter, Pro sau „Mi-am pus un buget”, cu o sumă introdusă de el.
4. **Propunerea:** kitul, cu prețul total, ce scoate și de ce („arătat pentru că oferi Montaj mobilier”). Pe fiecare rând: scoate, schimbă cu varianta superioară, cantitate, mărime.
5. **Branding opțional:** „Adaugă un tricou și o geantă cu numele tău?”. Doar o întrebare, cu „Nu acum” vizibil.
6. **Salvare sau coș:** kitul se salvează în „Kiturile mele” și poate fi comandat oricând.

**Reguli:**

- Fără chestionare lungi: maximum 3 întrebări înainte de propunere.
- „Nu știu” e mereu un răspuns valid și nu repetă întrebarea.
- Recomandarea explică de ce apare fiecare produs; nu există produse adăugate „cu bifă implicită”.
- Bugetul e o limită: kitul propus nu îl depășește, iar diferența se arată ca „Poți adăuga mai târziu”.
- Mascota oficială în starea „gândește” apare doar cât se calculează propunerea.

## 6. Print Studio și QR

Designul se generează automat din profilul aprobat, iar Jobzerul alege doar șablonul și textele scurte. Fiecare material are un QR permanent spre profilul public.

**Ce intră automat din profil:**

- Numele public, așa cum apare în Jobzee (de exemplu „Mihai I.”).
- Specializarea principală și până la 3 skill-uri.
- Fotografia de profil, doar dacă Jobzerul o bifează.
- Nivelul (Start, Plus, Gold, Black) și nota, doar dacă sunt reale și Jobzerul le alege. Nota se tipărește cu data („4,9 ★ la 17 oct. 2026”), pentru că se schimbă.
- Zona de lucru la nivel de cartier sau oraș.

**Ce nu intră niciodată:** telefonul, e-mailul, adresa, CNP-ul sau CUI-ul personal și textele de tip „certificat Jobzee”, „garantat” sau „autorizat”, dacă nu există un statut real în Jobzee.

**Ce poate edita Jobzerul:** un slogan de maximum 60 de caractere, ordinea skill-urilor, culoarea de accent (doar din paleta Jobzee) și șablonul. Logo-ul și mascota se folosesc doar după regulile din sistemul de design: nu se recolorează, nu se deformează și nu se pun pe portocaliu.

**Codul QR:**

- Duce la o adresă permanentă a profilului, de forma `jobzee.ro/j/<cod-scurt>`. Codul nu se schimbă dacă Jobzerul își schimbă numele, deci materialele tipărite nu expiră.
- Pagina arată profilul public și butonul „Cere o ofertă de la Mihai”. Cererea intră în fluxul normal: fișă, oferte, potrivire. Jobzerul primește întâi cererea, dar clientul vede și alte oferte dacă el nu răspunde în timp.
- Fiecare material are un parametru de sursă (de exemplu cărți de vizită sau magnet auto), ca statisticile să arate ce funcționează. Parametrul nu conține date personale.
- Dacă Jobzerul își dezactivează contul, QR-ul duce la o pagină neutră „Profil indisponibil”, nu la o eroare.

**Previzualizare și fișiere:**

- Previzualizare față/verso la mărimea reală înainte de comandă, cu marginile de tăiere vizibile.
- Fișier print-ready: PDF CMYK, 3 mm bleed, la cerințele tipografiei partenere. Se poate descărca acolo unde tipografia permite.
- Fiecare comandă de print are un pas de aprobare a machetei: „Am verificat numele, textul și QR-ul”. Fără bifă, nu se trimite la tipar.

## 7. Comenzi și fulfillment

O comandă Jobzee se poate împărți în mai multe comenzi la furnizori, fiecare cu starea, termenul și AWB-ul ei. Jobzerul vede o singură comandă cu pachete separate. Nicio stare nu se schimbă fără confirmarea partenerului.

**Două tipuri de produs, marcate peste tot:**

- **„Disponibil la partener”:** stocul confirmat în ultimele 24 h prin conexiunea cu partenerul. Termenul afișat e cel trimis de partener.
- **„Se face la comandă”:** produse personalizate și print. Arată timpul de producție (de exemplu „3–5 zile lucrătoare, după aprobarea machetei”), plus livrarea.

Când partenerul nu are conexiune de stoc, produsul spune „Disponibilitatea se confirmă după comandă”. Banii se încasează doar după confirmare.

| Stare | Cine o schimbă | Ce vede Jobzerul | Se poate anula? |
| --- | --- | --- | --- |
| Plasată | Jobzerul plătește | „Am trimis comanda partenerilor” | Da, gratuit |
| Confirmată de partener | Partenerul (stoc + termen) | Termen confirmat pe fiecare pachet | Da, gratuit, până la producție |
| Machetă de aprobat | Sistemul, pentru print și personalizate | Previzualizarea finală, butonul „Aprob” | Da, gratuit |
| În producție / în asamblare | Partenerul | „Se face acum” + termenul | Personalizatele nu; restul conform partenerului |
| Expediată | Partenerul, cu AWB | Curierul, AWB-ul, urmărirea | Nu; se face retur după livrare |
| Livrată | Curierul / partenerul | Data livrării, butonul „Ceva nu e în regulă” | Retur sau garanție |
| Retur / garanție / rambursată | Suportul Jobzee + partenerul | Starea cererii și suma rambursată | — |

**Reguli comerciale propuse (de validat juridic):**

- **Anulare:** gratuită până la „În producție”. Produsele personalizate nu se mai pot anula după aprobarea machetei.
- **Retur:** 14 zile pentru produsele nepersonalizate, pentru toți cumpărătorii, inclusiv PFA și SRL. Personalizatele se returnează doar pentru defecte sau erori de producție.
- **Garanție:** cea a producătorului, afișată pe pagina produsului. Pentru persoane fizice se aplică și garanția legală de conformitate.
- **Rambursare:** pe același card, după ce partenerul confirmă returul. Jobzerul vede data estimată dată de procesatorul de plată, nu una inventată.
- **Transport:** afișat per pachet înainte de plată. Gratuit doar dacă partenerul îl oferă.
- **Facturi:** emise de vânzător (Jobzee sau partenerul), pe persoană fizică sau pe CUI. Toate apar în „Comenzile mele”, separat de facturile din marketplace.
- **Suport:** un singur canal Jobzee, cu sarcini interne către partener. Jobzerul nu e trimis să vorbească direct cu furnizorul.

## 8. Parcursuri Jobzer

Patru parcursuri acoperă aproape toate situațiile. Fiecare pleacă dintr-un punct care există deja în aplicație, nu dintr-un magazin separat.

**A. Jobzer nou care își face trusa (Mihai, începe cu montaj)**

1. Termină Start Jobzer. Pe ultimul ecran vede „Ai tot ce-ți trebuie? Construiește-ți kitul în 1 minut”, opțional, sub „Vezi cererile”.
2. Smart Kit Builder: confirmă Montaj mobilier, bifează ce are deja, alege Starter.
3. Scoate ruleta, pentru că o are deja. Prețul scade pe loc.
4. Adaugă un tricou cu numele lui, apoi trece prin coș și plată.
5. Urmărește două pachete: uneltele („Disponibil la partener”) și tricoul („Se face la comandă”).
6. La livrare, ce a cumpărat se adaugă cu o atingere în „Echipamentul meu”.

**B. Jobzer activ care are nevoie de o piesă (Radu, își strică bitul)**

1. Din Profil intră în Gear Shop, filtrează „Montaj”, apoi „Consumabile”.
2. Vede livrarea estimată de partener și comandă în două atingeri, cu cardul salvat.

**C. Jobzer care vrea să fie cunoscut în cartier (Elena, curățenie)**

1. Din Profil intră în Gear & Growth, apoi în Print Studio, la cărți de vizită.
2. Designul vine completat din profil. Ea alege șablonul și scrie un slogan scurt.
3. Previzualizează QR-ul, aprobă macheta și comandă 200 de bucăți sau descarcă PDF-ul.
4. Peste două săptămâni, Growth Insights arată numai date reale, de exemplu „14 scanări, 3 cereri din cărțile de vizită”.

**D. Client care scanează un QR (Andrei, de pe un magnet auto)**

1. Scanează codul și ajunge pe profilul public al lui Mihai, fără telefon sau adresă afișate.
2. Apasă „Cere o ofertă de la Mihai”. Dacă nu are cont, cererea se face ca vizitator, iar contul se cere la trimitere, ca în restul aplicației.
3. Fișa se trimite întâi lui Mihai. Dacă el nu răspunde în timpul stabilit, cererea intră în Radarul normal.
4. Clientul alege oferta și plătește prin fluxul de potrivire, cu taxa de potrivire obișnuită. Nimic din această plată nu trece prin Gear & Growth.

## 9. Integrarea în navigație

Gear & Growth nu are tab propriu. Meniul Jobzerului rămâne Acasă, Sarcini, Încasări, Profil. Hub-ul se deschide din Profil, iar celelalte intrări sunt contextuale și se pot ascunde.

| Punct de intrare (ecran existent) | Ce apare | Duce la | Se poate ascunde |
| --- | --- | --- | --- |
| Profil Jobzer (ContJobzer), rând nou în listă | „Gear & Growth · trusă, haine, cărți de vizită” | Hub | Nu (e locul lui permanent) |
| Start Jobzer, sub pașii de activare | Link discret „Construiește-ți kitul” | Smart Kit Builder | Dispare după prima vizită |
| Skill-uri, prețuri, portofoliu (ProfilEdit) | „Adaugă echipamentul pe care îl ai” | Echipamentul meu | Nu |
| Statistici Jobzer | Card „De unde vin vizitele” | Growth Insights | Nu |
| Acasă Jobzer, recomandarea Jobzee (HouseAd) | Un mesaj al rotației, de exemplu „Cărți de vizită cu QR spre profilul tău” | Print Studio | Da, × pentru 7 zile, ca orice recomandare |
| Notificări | Doar stări de comandă (confirmată, expediată, livrată), nu oferte comerciale | Urmărirea comenzii | Se dezactivează în Setări |

**Unde nu apare niciodată:** în Radar, în Oferte, în ecranele unei sarcini active, în plată și în fluxul clientului. Clientul vede Gear & Growth doar indirect, prin profilul public și QR.

**Notificări:** Gear & Growth nu trimite notificări promoționale implicit. Cele de marketing cer acord separat (opt-in) în Setări.

## 10. Specificație ecran cu ecran

Optsprezece ecrane noi, toate în stilul existent (Apple, crem cald, portocaliu, cărbune, colturi rotunjite, fonturi fine), în light și dark. Fiecare are stare de încărcare (schelet), gol, eroare și fără internet, ca restul aplicației.

| # | Ecran | Scop | Conținut și interacțiuni | Acțiunea principală | Mascotă |
| --- | --- | --- | --- | --- | --- |
| 1 | Gear & Growth Hub | Punctul de intrare | 4 carduri mari: Kituri, Gear Shop, Identity, Print Studio. Card Growth cu profilul complet în %, comenzile active și „Kiturile mele” salvate | Deschide modulul ales | La treabă (o dată, în antet) |
| 2 | Catalog de kituri | Alegerea kitului | Kiturile filtrate pe skill-urile Jobzerului în top, apoi restul. Pe fiecare card: Starter / Pro, preț de la, număr de produse, termen | Deschide kitul | — |
| 3 | Detaliu kit | Ce conține exact | Selector Starter / Pro / Custom. Lista de produse cu cantitate, specificații, preț și badge „Disponibil” / „Se face la comandă”. Comutator „Am deja” pe fiecare rând. Totalul se recalculează live. Nota „Kitul nu certifică skill-uri” | Adaugă în coș · total | — |
| 4 | Smart Kit Builder | Kit în 3 întrebări | Conversație cu chip-uri (secțiunea 5), apoi propunerea editabilă în același ecran | Salvează / Adaugă în coș | Gândește (animat, doar la calcul) |
| 5 | Gear Shop | Un singur produs | Căutare, filtre pe specializare și categorie (unelte, consumabile, protecție…). Grilă de produse cu preț, livrare estimată de partener, badge de disponibilitate | Deschide produsul | — |
| 6 | Detaliu produs | Decizia de cumpărare | Galerie, specificații, garanție, partener, termen, retur. „Folositor pentru: Montaj mobilier”. Fără „cumpărate împreună” inventate | Adaugă în coș | — |
| 7 | Catalog Identity | Haine și insigne | Produse cu previzualizare live: numele și specializarea Jobzerului pe tricou, șapcă, ecuson. Mărimi și culori doar din paleta Jobzee | Personalizează | — |
| 8 | Print Studio | Alegerea materialului | Cărți de vizită, flyere, broșuri, autocolante, cărți QR, branding auto. Fiecare cu preț de la, termen și „PDF gratuit” unde e cazul | Deschide designerul | Arată (pasul următor) |
| 9 | Designer cărți de vizită | Macheta | Față/verso cu flip animat, 3 șabloane, slogan (60 caractere), comutatoare pentru poză, notă și nivel, zoom pe QR | Previzualizează și aprobă | — |
| 10 | Designer flyere | Macheta | Format A5 / A6, titlu, 3 servicii cu preț „de la” doar din profil, zona, QR. Avertizare dacă un preț nu există în profil | Previzualizează și aprobă | — |
| 11 | Previzualizare profil QR | Ce vede cine scanează | Exact pagina publică: poză, nume, skill-uri, notă, „Cere o ofertă”. Listă „Ce NU apare: telefon, e-mail, adresă”. Linkul permanent, copiere | Testează QR-ul / Copiază linkul | — |
| 12 | Coș | Totalul | Grupat pe partener / pachet: „Disponibil” sau „Se face la comandă”, cu termene. Transport per pachet. Cod promoțional | Continuă la plată | — |
| 13 | Checkout | Plata | Adresa de livrare (salvată sau nouă), facturare persoană fizică / CUI, cardul (Apple Pay / Google Pay), rezumatul cu TVA, regulile de anulare și retur | Plătește {total} | — |
| 14 | Confirmare comandă | Liniștire | Numărul comenzii, ce urmează pe fiecare pachet. Dacă există machetă, „Aprobă macheta ca să intre la tipar” | Urmărește comanda | Sare de bucurie |
| 15 | Urmărire comandă | Unde e fiecare pachet | Timeline pe pachet (secțiunea 7), AWB cu link spre curier, „Ceva nu e în regulă”, factura | Vezi la curier | Pe drum (doar când e expediată) |
| 16 | Echipamentul meu | Inventar declarat | Lista echipamentului: adăugat manual sau din comenzi livrate. Pe profilul public apare doar dacă Jobzerul bifează. Nu schimbă potrivirea | Adaugă echipament | La laptop (când e gol) |
| 17 | Designurile mele | Materialele salvate | Cărți, flyere, autocolante, cu „Recomandă”, „Descarcă PDF”, „Actualizează din profil” dacă profilul s-a schimbat | Recomandă | — |
| 18 | Growth Insights | Ce funcționează | Profil complet %, scanări QR, vizite pe profil, cereri din promovare, pe surse (cărți, flyere, magnet). Doar date măsurate, cu „Încă nicio scanare” la zero. Fără promisiuni | Îmbunătățește profilul | Arată (un sfat real, din date) |

## 11. Modele de date conceptuale

Unsprezece entități noi, toate în domeniul comercial, legate de marketplace doar prin contul Jobzerului și profilul public.

| Entitate | Câmpuri cheie | Legături |
| --- | --- | --- |
| Partener | nume, tip (unelte / print / textil), CUI, conexiune de stoc da/nu, termene standard | produse, comenzi la furnizor |
| Produs | partener, categorie, specializări, specificații, preț cu TVA, tip (disponibil / la comandă), garanție, regulă de retur | variantă, articol de kit |
| Variantă | mărime, culoare, SKU partener, stoc confirmat + data confirmării | produs |
| Kit | serviciu, nivel (Starter / Pro), articole cu cantități | articole de kit |
| Configurație kit | Jobzer, kit de bază, articole scoase / adăugate / îmbunătățite, salvată da/nu | Jobzer, coș |
| Design | Jobzer, tip (carte / flyer / autocolant…), șablon, câmpuri din profil la acea dată, slogan, versiune, machetă aprobată da/nu | profil public, articol de comandă |
| Cod QR | cod scurt permanent, Jobzer, sursă (material), activ da/nu | design, eveniment de creștere |
| Comandă | Jobzer, adresă, date de facturare, totaluri, TVA, stare de plată (registru comercial separat) | comenzi la furnizor, facturi, rambursari |
| Comandă la furnizor | partener, articole, stare, termen confirmat, AWB, curier | comandă |
| Echipament declarat | Jobzer, articol (liber sau din comandă), public da/nu | Jobzer |
| Eveniment de creștere | tip (scanare / vizită / cerere), cod QR, dată — fără date personale ale vizitatorului | cod QR, cerere din marketplace (doar ID) |

Regula de separare: în baza de date, comenzile și taxele de potrivire stau în registre diferite. Singura legătură permisă e ID-ul cererii pe un eveniment de creștere, ca să se poată număra „cereri venite din QR”.

## 12. Dependențe operaționale și legale

Nimic nu se lansează fără parteneri contractați și o verificare juridică a rolului de vânzător. Lista de mai jos e de verificat cu un jurist și un contabil din România.

- **Contracte cu parteneri:** prețuri, termene, stoc, retururi, garanție, SLA de confirmare, acces la stoc (API sau feed zilnic).
- **Rolul de vânzător:** dacă Jobzee revinde, devine comerciant cu toate obligațiile: TVA, facturare, garanție. Dacă doar intermediază, trebuie să spună clar cine e vânzătorul pe fiecare produs.
- **Facturare:** e-Factura pentru facturile emise, TVA la cota în vigoare, facturi pe persoană fizică și pe CUI.
- **Drepturile consumatorului:** dreptul de retragere și garanția de conformitate pentru persoane fizice; excepția legală pentru produse personalizate.
- **Plăți:** un cont comercial separat de cel al marketplace-ului (Stripe) sau un flux separat, ca banii să nu se amestece.
- **GDPR:** QR-ul și statisticile nu colectează date personale ale celor care scanează; acord separat pentru marketing.
- **Brand:** regulile de folosire a logo-ului și mascotei pe produse; master vectorial pentru tipar.
- **Siguranța produselor:** produse electrice și echipament de protecție doar de la parteneri care garantează conformitatea (marcaj CE).
- **Autorizări:** lucrările electrice și de gaze cer autorizări; vinderea uneltelor nu le acordă și nu sugerează asta.

## 13. Lansare pe faze

Print Studio și QR-ul vin primele: un singur partener, fabricare la comandă și cel mai mic risc de stoc. Kiturile vin abia după ce există date reale despre ce cumpără Jobzerii.

| Fază | Ce intră | Condiția ca să treacă mai departe |
| --- | --- | --- |
| 0 · Fundație | Profil public cu link permanent, QR, Previzualizare profil QR, Growth Insights cu date reale, Echipamentul meu | Profilul public e live; scanările se măsoară corect |
| 1 · Print Studio | Cărți de vizită, flyere, autocolante QR; o tipografie parteneră; PDF gratuit; coș, plată, urmărire | Primele 100 de comenzi fără erori de machetă |
| 2 · Identity | Tricouri, șepci, veste, ecusoane; partener print-on-demand textil | Retururi pentru defecte sub ținta stabilită cu partenerul |
| 3 · Gear Shop | Unelte individuale de la 1–2 parteneri cu stoc confirmat; pachete separate | Partenerul confirmă stocul și termenul automat |
| 4 · Kituri + Smart Kit Builder | Kituri Starter / Pro pe 3–4 servicii, apoi toate 8; configurare | Marja confirmată cu partenerii și ritm de comenzi stabil |

## 14. Venituri și costuri

Venitul vine din marja pe produse și din comisioanele partenerilor; cele mai mari costuri sunt suportul, retururile și erorile de personalizare. Cifrele concrete se pun abia după ofertele partenerilor; acest document nu estimează volume.

| Venituri | Costuri |
| --- | --- |
| Marjă pe kituri, Identity, Print | Cost partener (produs, producție, ambalare) |
| Comision de la partenerii din Gear Shop | Transport neacoperit de client |
| Fișiere digitale premium (mai târziu) | Taxa procesatorului de plată |
| Instrumente de creștere opționale (mai târziu) | Suport clienți, retururi, garanții |
|  | Re-tipăriri după erori de machetă |
|  | Integrări cu partenerii, foto de produs, catalog |
|  | Juridic, contabilitate, e-Factura |

## 15. Riscuri și decizii deschise

Cel mai mare risc e de încredere: un Jobzer care crede că trebuie să cumpere ca să primească lucrări. De aceea toate textele spun explicit contrariul.

| Risc | Ce îl reduce |
| --- | --- |
| Jobzerii cred că un kit cumpărat îi urcă în potrivire | Notă pe fiecare kit și în Hub; potrivirea nu citește comenzile |
| Stoc sau termene greșite | Doar date confirmate de partener; „Se confirmă după comandă” când lipsesc |
| Erori pe cărțile tipărite | Aprobare obligatorie a machetei; previzualizare la mărime reală |
| QR care expune date private | Doar profilul public; telefon și adresă excluse din design |
| Folosire greșită a brandului pe produse | Șabloane blocate; logo și mascotă doar din fișierele oficiale |
| Amestec de bani între domenii | Registre și conturi de plată separate |

**Decizii deschise:**

- [ ] Comisionul de potrivire: 10% la client și 10% la Jobzer, sau 15% la client și 0% la Jobzer, ca în canvas?
- [x] Jobzee e vânzător sau doar intermediar, pe fiecare modul?
- [ ] Pot cumpăra și Jobzerii neverificați?
- [x] Primii trei parteneri (unelte, textil, tipografie).
- [ ] Politica de retur de 14 zile se aplică și firmelor (PFA, SRL)?
- [x] Echipamentul declarat apare pe profilul public implicit sau doar la bifare?
