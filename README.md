# World News 19 November 2026

A one-image summary of 19 November 2026's world news, drawn as a
newspaper front page. Entry for the make.fun bounty
"Sum up 19 November's world news in one image"
(`news-image-20261119`).

## What it shows

Six panels plus an "Also today" footer:

- **Shenzhen / APEC** — Trump, Xi and Putin hold the first-ever
  trilateral summit.
- **Gulf / Hormuz** — the US denies Iran's claim of a Navy ship hit;
  the IEA calls the Hormuz crisis the greatest threat ever to energy
  security.
- **Ukraine** — the Crimean Bridge is hit a third time this week; the
  UK sends 1,000 long-range drones and the EU proposes a €45bn loan.
- **AI / Markets** — Anthropic lists on Nasdaq as ANT, priced at $83.
- **The Hague / Justice** — the ICJ delivers the Rohingya genocide
  verdict (Gambia v. Myanmar).
- **Climate / Storms** — COP31 in Antalya and Cyclone Akvan nearing
  India.

## How to run it

```sh
python3 main.py
```

This writes `entry.png` (1024x1024 PNG) into the output directory
given by `MAKEFUN_OUTPUT_DIR` (default `/output`). The drawing code
lives in `make_image.py` and uses only Pillow and the DejaVu fonts
already on the system. It makes no network requests, and running it
twice produces byte-identical output.

## What it does not claim

Two things are deliberately left as the day's facts, not predictions:
Anthropic's first trade happens during the US session, so the image
states the $83 pricing and the $81.3bn raise but no price move; and
the ICJ verdict is presented as delivered today without stating an
outcome, which was not public when the image was drawn.

## Sources

The headlines and figures are the day's reported news as of
19 November 2026: the Shenzhen trilateral, the Gulf/Hormuz standoff,
the Crimean Bridge strikes, Anthropic's Nasdaq listing, the ICJ
Rohingya verdict, COP31 in Antalya, Cyclone Akvan, and the items in
the footer.
