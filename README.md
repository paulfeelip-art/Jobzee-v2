# Jobzee v2 — design import (`claude-design-import`)

This branch is an export of the **existing** Jobzee visual design project, exactly as it was published in Claude Design on 17 Oct 2026. Nothing was redesigned, regenerated or simplified. The screen files are byte-for-byte the published versions.

- Design canvas source: Claude Design artifact, published version `1792245486-c551`
- Design system source: Claude Design System artifact, published version `1792228199-d7e6`
- Gear & Growth spec source: Claude Docs, revision 16

The file-by-file list with SHA-256 hashes is in [`INVENTORY.md`](INVENTORY.md).

## Structure

```
canvas/project/              The design canvas: 173 screens + canvas.json + 172 assets
  canvas.json                Board layout: position, size, title and order of all 173 screens, plus 30 notes
  *.dc.html                  One file per screen (87 light, 86 dark; OfertaRapida has no dark variant)
  assets/brand/              Logo, wordmark, mark, app icons (PNG)
  assets/mascot/             Official mascot poses (PNG)
  assets/cat/                30 category illustrations (SVG, 64×64 grid)
  assets/icons/              39 line icons (SVG, 24×24)
  assets/ui/                 60 UI icons (PNG)
  assets/services/           12 service photos (WebP)
  assets/people/, photos/    Avatars and hero photos (WebP)
design-system/               Jobzee Design System
  README.md                  Principles, voice, money, colors, type, motion, logo, mascot, accessibility (RO)
  Implementare.md            How the system maps to the Expo / React Native app (RO)
  tokens.json                All design tokens: color (light + dark), type, spacing, radius, shadow, duration, easing
  design-system.json         Design-system manifest
  components/<Name>/         README.md (rules) + preview.html (visual reference) for 20 components (Cover has a preview only)
  components/bundle.css      CSS reference for the component styles
  assets/                    Copies of brand, mascot, people and photos assets used by the previews
scripts/                     The Python/Node scripts used to generate and check the screens
specs/
  gear-growth/               Gear & Growth product specification (exported) + the original brief
  monetization-4.0/          The Monetization 4.0 BRIEF only (no specification was written; see below)
  talk-engine/               The Talk engine (request engine) brief
source-assets/               Original asset packs and reference screenshots supplied by Paul
```

## Changes since the first import

- **19 Oct 2026:** new board `00 Splash de lansare` (`SplashLive.dc.html` + dark), and board `01 Splash` (`Splash.dc.html` + dark) redesigned: Zee says „Salut!”, condenses into the pin, the pin becomes the horizontal logo, then the sign-in screen settles in. `canvas.json` lists the new board first.

## How a screen file works

Each `*.dc.html` is a Claude Design board: an HTML fragment with an `<x-dc>` root, `{{holes}}` for values, `sc-if` / `sc-for` attributes for conditions and lists, and a `class Component extends DCLogic` script holding the screen's state and interactions. Light and dark variants are separate files (`Acasa.dc.html`, `AcasaDark.dc.html`).

The boards need the **Claude Design runtime** (`dc-runtime.js`) and the canvas `support.js` to render interactively. Both belong to Claude Design, not to this project, so they are **not** in this repository. Opened directly in a browser, a board shows its static markup and styles, but the holes stay unfilled and the interactions do not run.

So the practical uses are:

1. **As the visual and behavioral reference for the React Native app.** Copy, layout, colors, spacing, state names and flows are all readable in the markup and the `DCLogic` class.
2. **As the canvas source of truth.** `canvas.json` keeps the board order, titles (numbered by flow) and positions.

## Using it in Cursor

1. Open the repo in Cursor and check out the branch: `git checkout claude-design-import`.
2. Add `design-system/README.md`, `design-system/tokens.json` and `design-system/Implementare.md` to your Cursor rules or context (for example `@design-system/tokens.json`). They hold the naming, the color/type/spacing values and the screen-to-route table.
3. To build a screen, give Cursor the board file plus the tokens, for example: *"Implement `@canvas/project/Oferte.dc.html` as `apps/mobile/src/app/request/match.tsx` in React Native, using `@design-system/tokens.json` and the components listed in `@design-system/Implementare.md`. Keep the Romanian copy exactly."*
4. Use `canvas/project/canvas.json` to find a screen by its title: titles start with the flow number (`07 Acasă client…`).
5. Take images from `canvas/project/assets/`. They are the same files the screens use.

Rules carried over from the design system, which Cursor should follow:

- App copy is Romanian with diacritics (ș, ț with a comma). Code and comments are English.
- The person doing the work is a **Jobzer**. The app speaks as **Jobzee**, never as "AI", "asistent AI" or "robot".
- Money is stored as integers in bani (1 leu = 100 bani), never as floats.
- Text on orange is near-black (`ink-on-brand`), never white.

## Scripts

`scripts/` contains the generators used to build the screens. `gen_roles.py` is the main generator; `gen_gear.py`, `gen_msg.py`, `gen_skills.py`, `gen_feed.py` and `gen_inc.py` extend it. `darkify.py` produces the dark variants, `gen_cat_icons.py` writes `assets/cat/*.svg`, and `render.py`, `rt_*.py` and `msgtest/` are rendering and test tools.

They were written against a working folder named `jobzee-design/project` and write screen files there. **Running them overwrites screens.** The screens in `canvas/` include edits made directly on the canvas after the last generator run, so regenerating would lose those edits. Treat the scripts as a record of how the screens were made, not as a build step.

## Not included, or not available

| Item | Status |
|---|---|
| Monetization 4.0 **specification** | **Not written.** Only the brief exists, committed as `specs/monetization-4.0/BRIEF-monetization-4.0.md`. Work was stopped before the spec was produced. |
| `dc-runtime.js`, `support.js` | Claude Design runtime files. They belong to Claude Design and are not part of this project. |
| Vector (SVG) logo master | **Does not exist.** The logo and mascot are raster PNGs from the supplied materials. A vector master is needed for print. |
| 5 unused draft boards (Cautare, Descrie, Gasit, Pret, Verifica) | Excluded on purpose: they were never placed on the canvas or published. |
| Final audit document | Unfinished: only sections 1–2 were written before it was stopped. Not exported. |
| `gen_roles.bak.py` and helper JSON file lists | Left out: a backup copy and publish manifests, not part of the design. |

## Known open issues (from the unfinished audit, not fixed here)

- `darkify.py` maps `#D1D1D6` to `#48484A` in a final pass, which darkens some text in 5 dark boards.
- White icons on orange have a contrast of 2.06:1.
- About 240 touch targets are smaller than 32 px.

These are recorded so they can be fixed in a separate change. The screens here are unchanged.
