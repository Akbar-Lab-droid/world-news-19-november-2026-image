"""Draw a 1024x1024 dense newspaper front page summing up 19 November 2026.

Deterministic: fixed fonts, fixed colours, no timestamps, no randomness.
A lead story plus three columns of short items grouped by region, so
the day's breadth (48 stories) is visible at a glance. Run directly
to write entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (253, 251, 244)
INK = (20, 20, 20)
RULE = (60, 60, 60)
ACCENT = (139, 0, 0)

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


# (region, headline, detail). Region shown as a header when it changes.
# Details are kept short so each fits on one line.
COLUMNS = [
    [  # Asia & Pacific
        ("ASIA & PACIFIC",
         "APEC adopts Shenzhen Outlook on trade and AI",
         "Leaders adopt shared economic and digital agenda."),
        ("ASIA & PACIFIC",
         "Xi showcases China's tech rise at summit",
         "Shenzhen meeting puts China's technology on display."),
        ("ASIA & PACIFIC",
         "Japan PM Takaichi meets Putin at APEC",
         "Agrees to keep talking at various levels."),
        ("ASIA & PACIFIC",
         "Xi greets Takaichi as China-Japan feud simmers",
         "Leaders meet a year into the Taiwan dispute."),
        ("ASIA & PACIFIC",
         "Russian Tu-95 bombers return to Vietnam",
         "Flights near Taiwan and Japan raise concern."),
        ("ASIA & PACIFIC",
         "North Korea expanding Yongbyon enrichment",
         "IAEA calls it a 'cause for serious concern'."),
        ("ASIA & PACIFIC",
         "Vietnam & Russia deepen energy cooperation",
         "Leaders agree closer energy ties at APEC."),
        ("ASIA & PACIFIC",
         "South Korea sees no sign of US-North talks",
         "No indication of imminent dialogue, Seoul says."),
        ("ASIA & PACIFIC",
         "Trump presses Xi on farm buys, Hormuz oil",
         "US seeks more farm purchases, oil flows kept open."),
        ("ASIA & PACIFIC",
         "US-China tariff truce expires on 10 January",
         "Trade truce lapses in January, talks continue."),
        ("ASIA & PACIFIC",
         "Xi: nuclear weapons should be eliminated",
         "China's leader pushes full disarmament at summit."),
        ("ASIA & PACIFIC",
         "Cyclone Akvan to make landfall weaker on Friday",
         "Storm to cross Andhra-Odisha coast at 90-100 km/h."),
        ("ASIA & PACIFIC",
         "Bangladesh shutdown; Yunus home set ablaze",
         "Four killed as opposition shutdown turns violent."),
        ("ASIA & PACIFIC",
         "UNHCR halts refugee registration in Malaysia",
         "Agency backs stronger asylum management."),
        ("ASIA & PACIFIC",
         "Indonesia passes asset-forfeiture bill",
         "Parliament approves seizures without conviction."),
        ("ASIA & PACIFIC",
         "Rio Tinto pays $250m for PNG mine fund",
         "Fund addresses mine's environmental legacy."),
    ],
    [  # Europe, Ukraine, Middle East, Africa
        ("EUROPE & UKRAINE",
         "EU proposes €45bn loan to Ukraine",
         "Loan covers part of a €70bn shortfall in 2027."),
        ("EUROPE & UKRAINE",
         "Ukraine hits Crimean Bridge a third time",
         "Rail traffic suspended; Russia vows to rebuild."),
        ("EUROPE & UKRAINE",
         "Russian strikes kill 5; power grid hit",
         "Five regions lose power after infrastructure attacks."),
        ("EUROPE & UKRAINE",
         "Denmark approves Greenland defence deal 109-0",
         "Parliament backs Arctic security agreement."),
        ("EUROPE & UKRAINE",
         "Meloni urges China to push Moscow to peace",
         "Italy presses Beijing on Ukraine."),
        ("EUROPE & UKRAINE",
         "EU hit by AI-assisted cyberattack",
         "Commission confirms attack on internal systems."),
        ("EUROPE & UKRAINE",
         "EU delays methane rules for fossil imports",
         "Rules pushed back to 2029."),
        ("EUROPE & UKRAINE",
         "Serbia elects Cupic speaker with 140 votes",
         "Student List candidate wins parliament vote."),
        ("MIDDLE EAST & AFRICA",
         "ICJ: Myanmar committed genocide",
         "Court rules 9-6; about 10,000 Rohingya killed."),
        ("MIDDLE EAST & AFRICA",
         "US strikes Iran's Qeshm island",
         "Iran retaliates against Kuwait and Bahrain."),
        ("MIDDLE EAST & AFRICA",
         "Houthi missile damages Riyadh PIF Tower",
         "Saudi wealth fund tower hit in the attack."),
        ("MIDDLE EAST & AFRICA",
         "Israel ground operation in central Gaza",
         "Troops cross the Yellow Line after evacuation orders."),
        ("MIDDLE EAST & AFRICA",
         "Gaza aid groups rate peace plan 4 out of 26",
         "Five agencies say implementation is lagging."),
        ("MIDDLE EAST & AFRICA",
         "Ethiopia & Eritrea mass troops on border",
         "Fears of renewed war as Tigray fighting grows."),
        ("MIDDLE EAST & AFRICA",
         "Migrant boat sinks off Senegal; dozens missing",
         "About 100 people aboard; dozens unaccounted for."),
        ("MIDDLE EAST & AFRICA",
         "IEA: Middle East crisis biggest threat to energy",
         "IEA calls it the largest threat ever to energy security."),
    ],
    [  # Americas, business, science, sport
        ("AMERICAS",
         "Trump pardons baseball legend Pete Rose",
         "Posthumous pardon for the late baseball star."),
        ("AMERICAS",
         "Fiona the hippo dies after swallowing a hat",
         "Cincinnati Zoo mourns its beloved hippo."),
        ("AMERICAS",
         "US Senate rejects Iran war-powers limit 51-48",
         "Three Republicans backed it; one Democrat opposed."),
        ("AMERICAS",
         "House Democrats nominate Jeffries for Speaker",
         "Jeffries nominated as majority era begins."),
        ("AMERICAS",
         "Trump asks top court to block Venezuelan TPS",
         "Administration seeks stay on deportation protections."),
        ("AMERICAS",
         "Musk distances himself from Republicans",
         "Breaks with party after election losses."),
        ("BUSINESS & TECH",
         "Anthropic IPO raises $81-100bn, largest ever",
         "Valued at $1.5tn as shares begin Nasdaq trading."),
        ("BUSINESS & TECH",
         "Van Gogh painting sells for record $190.4m",
         "'Châtaigniers en fleurs' sets artist record at Sotheby's."),
        ("BUSINESS & TECH",
         "Warner Bros TV & Paramount TV to merge in 2027",
         "Studios combine in a 2027 merger."),
        ("SCIENCE",
         "New pulsar discovery method 1,000,000x faster",
         "Pulsar found in public NASA data by new method."),
        ("SCIENCE",
         "48 pepper genomes map chilli domestication",
         "Study traces where chillies got their heat."),
        ("CLIMATE & SOCIETY",
         "COP31 final stage; fossil-fuel text unresolved",
         "Ministers meet in Antalya to unblock negotiations."),
        ("CLIMATE & SOCIETY",
         "Save the Children: 589m children in conflict zones",
         "Nearly a quarter of the world's children affected."),
    ],
]


def build_image():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    M = 28

    # Masthead
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_BOLD, 46)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 16), title, font=tf, fill=INK)
    draw.line([(M, 72), (W - M, 72)], fill=RULE, width=2)
    date = "THURSDAY 19 NOVEMBER 2026  •  46 STORIES"
    df = font(SANS_BOLD, 18)
    dw = draw.textlength(date, font=df)
    draw.text(((W - dw) / 2, 80), date, font=df, fill=INK)
    draw.line([(M, 106), (W - M, 106)], fill=RULE, width=3)

    # Lead story, full width
    lx0, ly0, lx1, ly1 = M, 114, W - M, 206
    draw.rectangle((lx0, ly0, lx1, ly1), fill=(255, 255, 255), outline=RULE, width=1)
    kf = font(SANS_BOLD, 15)
    draw.text((lx0 + 14, ly0 + 8), "SHENZHEN  •  TRILATERAL SUMMIT", font=kf, fill=ACCENT)
    hf = font(SANS_BOLD, 26)
    draw.text((lx0 + 14, ly0 + 30), "Trump, Xi & Putin meet in first-ever three-way summit",
              font=hf, fill=INK)
    bf = font(SANS, 15)
    lead_body = ("Joint declaration pledges dialogue on nuclear risks and "
                 "stable energy flows; 'a nuclear war cannot be won'.")
    by = ly0 + 62
    for line in wrap(draw, lead_body, bf, lx1 - lx0 - 28)[:2]:
        draw.text((lx0 + 14, by), line, font=bf, fill=INK)
        by += 19

    # Columns
    col_w = (W - 2 * M - 2 * 12) // 3
    col_x = [M, M + col_w + 12, M + 2 * (col_w + 12)]
    top = 214
    bottom = H - 14
    hf_item = font(SANS_BOLD, 13)
    bf_item = font(SANS, 11)
    rf = font(SANS_BOLD, 12)

    for ci, items in enumerate(COLUMNS):
        x = col_x[ci]
        y = top
        region = None
        for reg, head, detail in items:
            if reg != region:
                region = reg
                draw.text((x, y), region, font=rf, fill=ACCENT)
                draw.line([(x, y + 17), (x + col_w, y + 17)], fill=ACCENT, width=1)
                y += 24
            head_lines = wrap(draw, head, hf_item, col_w)
            for line in head_lines[:2]:
                draw.text((x, y), line, font=hf_item, fill=INK)
                y += 16
            det_lines = wrap(draw, detail, bf_item, col_w)
            for line in det_lines[:1]:
                draw.text((x, y), line, font=bf_item, fill=(70, 70, 70))
                y += 14
            y += 6
        if ci < 2:
            draw.line([(x + col_w + 6, top), (x + col_w + 6, bottom)],
                      fill=(200, 200, 190), width=1)

    return img


if __name__ == "__main__":
    build_image().save("entry.png", format="PNG")
    print("wrote entry.png")
