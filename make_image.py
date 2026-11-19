"""Draw a 1024x1024 newspaper front page summing up 19 November 2026.

Deterministic: fixed fonts, fixed colours, no timestamps, no randomness.
Run directly to write entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 251, 244)
INK = (20, 20, 20)
RULE = (60, 60, 60)
ACCENT = (139, 0, 0)
PANEL_BG = (255, 255, 255)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap by measured width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        line = words[0]
        for word in words[1:]:
            trial = line + " " + word
            if draw.textlength(trial, font=fnt) <= max_width:
                line = trial
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def draw_panel(draw, box, kicker, headline, body, head_size=27, body_size=20):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL_BG, outline=RULE, width=1)
    pad = 16
    x = x0 + pad
    w = x1 - x0 - 2 * pad
    y = y0 + 12
    kf = font(SANS_BOLD, 17)
    draw.text((x, y), kicker, font=kf, fill=ACCENT)
    y += 26
    hf = font(SANS_BOLD, head_size)
    for line in wrap(draw, headline, hf, w):
        draw.text((x, y), line, font=hf, fill=INK)
        y += head_size + 6
    y += 4
    bf = font(SANS, body_size)
    for line in wrap(draw, body, bf, w):
        draw.text((x, y), line, font=bf, fill=INK)
        y += body_size + 6


def build_image():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    M = 28

    # Masthead
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_BOLD, 56)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 26), title, font=tf, fill=INK)
    draw.line([(M, 100), (W - M, 100)], fill=RULE, width=2)
    date = "THURSDAY 19 NOVEMBER 2026"
    df = font(SANS_BOLD, 26)
    dw = draw.textlength(date, font=df)
    draw.text(((W - dw) / 2, 110), date, font=df, fill=INK)
    draw.line([(M, 148), (W - M, 148)], fill=RULE, width=3)

    # Lead story, full width
    draw_panel(
        draw, (M, 162, W - M, 338),
        "SHENZHEN  •  APEC",
        "Trump, Xi & Putin hold first-ever trilateral summit",
        "Three nuclear powers meet in Shenzhen; nuclear cuts, Ukraine "
        "and Iran on the table \u2014 no breakthrough expected.",
        head_size=34, body_size=21,
    )

    # Row 2: Gulf and Ukraine
    mid = (W - 12) // 2
    draw_panel(
        draw, (M, 350, mid, 514),
        "GULF  •  HORMUZ",
        "US denies Iran claim of Navy ship hit",
        "IEA calls Hormuz crisis the greatest threat ever to energy "
        "security; tanker hit again.",
    )
    draw_panel(
        draw, (mid + 12, 350, W - M, 514),
        "UKRAINE",
        "Crimean Bridge hit a third time this week",
        "UK to send 1,000 long-range drones; EU proposes \u20ac45bn "
        "loan to Kyiv.",
    )

    # Row 3: AI/Markets and The Hague
    draw_panel(
        draw, (M, 526, mid, 690),
        "AI  •  MARKETS",
        "Anthropic lists on Nasdaq today as ANT",
        "Priced at $83, $81.3bn raise \u2014 largest IPO ever; "
        "~$1.5tn valuation.",
    )
    draw_panel(
        draw, (mid + 12, 526, W - M, 690),
        "THE HAGUE  •  JUSTICE",
        "ICJ delivers Rohingya genocide verdict today",
        "Gambia v. Myanmar: 2017 crackdown drove 730,000+ Rohingya "
        "to Bangladesh.",
    )

    # Panel 6: Climate, full width
    draw_panel(
        draw, (M, 702, W - M, 842),
        "CLIMATE  •  STORMS",
        "COP31 deal elusive in Antalya; Cyclone Akvan nears India",
        "Ministers push for a final text; 100,000+ evacuated in Odisha.",
        head_size=28, body_size=19,
    )

    # Footer: Also today
    fx0, fy0, fx1, fy1 = M, 854, W - M, 996
    draw.rectangle((fx0, fy0, fx1, fy1), fill=PANEL_BG, outline=RULE, width=1)
    kf = font(SANS_BOLD, 17)
    draw.text((fx0 + 16, fy0 + 10), "ALSO TODAY", font=kf, fill=ACCENT)
    footer = (
        "Bangladesh: Yunus's home torched, 28 districts hit by violence  \u2022  "
        "Van Gogh sells for $190.4m, an artist record  \u2022  "
        "589m children lived in conflict zones in 2025  \u2022  "
        "Indonesia passes asset-forfeiture bill"
    )
    bf = font(SANS, 19)
    y = fy0 + 38
    for line in wrap(draw, footer, bf, fx1 - fx0 - 32):
        draw.text((fx0 + 16, y), line, font=bf, fill=INK)
        y += 25

    return img


if __name__ == "__main__":
    build_image().save("entry.png", format="PNG")
    print("wrote entry.png")
