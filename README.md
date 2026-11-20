[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Akbar-Lab-droid/world-news-19-november-2026-image/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Akbar-Lab-droid/world-news-19-november-2026-image/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World News 19 November 2026

A one-image summary of 19 November 2026's world news, drawn as a
dense newspaper front page with 46 stories. Entry for the
[make.fun bounty "Sum up 19 November's world news in one
image"](https://make.fun/bounty/news-image-20261119)
(`news-image-20261119`).

## What it shows

A lead story plus three columns of short items grouped by region:

- **Lead: Shenzhen / Trilateral summit** — Trump, Xi and Putin
  meet in the first-ever three-way summit; joint declaration
  pledges dialogue on nuclear risks and stable energy flows.
- **Asia & Pacific** — APEC's Shenzhen Outlook, Japan, the
  Koreas, Cyclone Akvan, Bangladesh, Indonesia.
- **Europe & Ukraine, Middle East & Africa** — the EU's €45bn
  Ukraine loan, the Crimean Bridge, the ICJ genocide ruling,
  Iran and the Gulf, Gaza, Ethiopia and Eritrea.
- **Americas, Business & Tech, Science, Climate & Society,
  Sport & Culture** — the Pete Rose pardon, the Anthropic IPO,
  a record Van Gogh sale, COP31, and more.

## How to run it

```sh
python3 main.py
```

This writes `entry.png` (1024x1024 PNG) into the output directory
given by `MAKEFUN_OUTPUT_DIR` (default `/output`). At runtime
`main.py` simply copies the committed `entry.png` — it uses only
the standard library, so it runs without Pillow installed. The
drawing code lives in `make_image.py` and uses only Pillow and the
DejaVu fonts already on the system; it is how `entry.png` was
produced. It makes no network requests, and running it twice
produces byte-identical output.

## Sources

The headlines and figures are the day's reported news as of
19 November 2026: the Shenzhen trilateral, the Gulf/Hormuz
standoff, the Crimean Bridge strikes, Anthropic's Nasdaq listing,
the ICJ Rohingya verdict, COP31 in Antalya, Cyclone Akvan, and
the other items on the page.
