# Implementare

Ghidul pentru dezvoltare: cum ajunge sistemul în aplicația mobilă Jobzee (Expo SDK 57, React Native, Expo Router) din `apps/mobile`.

## Tokeni în cod

- Culorile din `tokens.json` înlocuiesc obiectele `light` și `dark` din `apps/mobile/src/lib/theme.ts`. Numele rămân cele din sistem (`bg`, `surface`, `ink`, `brand`, `brandText`…), în camelCase.
- Tema urmează setarea telefonului (`useColorScheme()`), cu opțiune manuală în Cont → Aspect.
- Mărimile de text devin un obiect `type` cu stilurile `largeTitle`, `title1`… `caption`, `numeralXl`. Pe Android se păstrează mărimile, cu fontul de sistem.
- Spațiere și raze: constante `space[1..8]` și `radius.lg` etc. Nicio valoare scrisă direct în ecrane.

## Biblioteci

| Nevoie | Bibliotecă Expo |
|---|---|
| Sticlă (meniu, butoane peste hartă) | `expo-blur` (`BlurView`, intensitate ~60, tint după temă) |
| Animații (apariții, foi, apăsare cu rebound) | `react-native-reanimated` (deja în Expo) |
| Haptic la butonul principal și la succes | `expo-haptics` |
| Hartă | `react-native-maps`, cu stil personalizat din tokenii `map-*` pentru ambele teme |
| Foi de jos | `@gorhom/bottom-sheet` sau foaie proprie cu Reanimated |
| Reducere mișcare | `AccessibilityInfo.isReduceMotionEnabled()`: dacă e activ, durata animațiilor devine 0 |

Verifică versiunile compatibile cu `npx expo install <pachet>`.

## Componente de construit

| Componentă | Fișier propus | Folosită în |
|---|---|---|
| `Button` (primary, secondary, dark, danger, plain; sm) | `src/components/ui/Button.tsx` | Toate ecranele |
| `ListGroup`, `ListRow`, `SectionLabel` | `ui/List.tsx` | Fișa, Profil, Cont, Plată, Setări |
| `Segmented` | `ui/Segmented.tsx` | Oferte (sortare), Activitate, Programare, Sarcinile mele |
| `Switch` | `ui/Switch.tsx` | Factură, Permisiuni, Disponibilitate |
| `Chip` | `ui/Chip.tsx` | Categorii, etichete recenzie, răspunsuri rapide |
| `StatusPill`, `TierBadge`, `Avatar` | `ui/Badges.tsx` | Rânduri, carduri de sarcină |
| `OfferRow` | `components/OfferRow.tsx` | Oferte primite |
| `TabBar` (plutitor, sticlă) | `components/TabBar.tsx` | Tab-urile client și Jobzer |
| `Sheet` (de jos și modală) | `ui/Sheet.tsx` | Acasă, Oferte, Plată, Muncă în plus |
| `CodeInput` | `components/CodeInput.tsx` | Cod SMS, cod de start |
| `LiveActivity` | `components/LiveActivity.tsx` | Pe drum (în aplicație) + Live Activity iOS reală mai târziu |
| `ChatBubble`, `TypingDots` | `components/Chat.tsx` | Dialog Jobzee, Chat |
| `Skeleton` | `ui/Skeleton.tsx` | Toate listele care se încarcă |

## Ecrane și rute

Rutele existente în `src/app` rămân; ecranele noi se adaugă alături.

| Ecran (canvas) | Rută |
|---|---|
| Bun venit, Telefon, Cod, Permisiuni | `index`, `auth/phone`, `auth/code`, `auth/permissions` (nou) |
| Acasă client | `(tabs)/index` |
| Dialog cu Jobzee | `request/intake` (devine chat) |
| Fișa cererii, Adresa, Programare | `request/sheet` (nou), `request/address` (nou), `request/schedule` (nou) |
| Oferte, Încă nicio ofertă | `request/match` (listă de oferte în loc de potrivire automată) |
| Profil Jobzer public | `jobzer/[id]` |
| Plată, Plată refuzată | `request/pay` (nou) |
| Pe drum, În lucru, Pe oră, Muncă în plus, Confirmă, Recenzie, Anulare, Problemă | `task/[id]` cu stări + `task/[id]/extra`, `task/[id]/cancel`, `task/[id]/report`, `task/[id]/review` |
| Acasă Jobzer, Cerere nouă, Spre client, Lucrez, Cod greșit | `(earn)/index`, `earn/offer`, `earn/task/[id]` cu stări |
| Sarcinile mele, Încasări, Niveluri, Promovare | `(earn)/tasks`, `(earn)/earnings`, `earn/levels`, `earn/boost` |
| Devino Jobzer (4 pași) | `earn/onboarding/[step]` |
| Profilul meu | `(earn)/profile` |
| Activitate, Mesaje, Chat, Cont | `(tabs)/activity`, `(tabs)/messages`, `chat/[id]`, `(tabs)/account` |

## Reguli de business care se schimbă în cod

- Taxa: clientul plătește **15%** peste prețul Jobzerului (minim 15%); comisionul Jobzerului devine **0%**. Se schimbă în `packages/shared/src/money.ts` și în SQL (`fee_service`, `fee_commission`), apoi testele.
- Oferte multiple: cererea primește oferte cu preț și oră de la mai mulți Jobzeri; clientul alege una. Ordinea „Recomandat”: promovate (marcate), apoi potrivire (skill, distanță, preț, disponibilitate).
- Promovare și Pro: produse plătite separat de Jobzer, marcate „Promovat” la client.
- Forma legală a Jobzerului: persoană fizică, PFA/II sau SRL, cu CUI verificat.

## Stări obligatorii pe fiecare ecran cu date

Încărcare (schelet), gol (cu acțiunea următoare), eroare (ce s-a întâmplat + ce poți face), fără internet (banda de sus, date din cache). Exemplele sunt în rândul 10 al canvas-ului.
