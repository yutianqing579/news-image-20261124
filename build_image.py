#!/usr/bin/env python3
"""Build entry.png: a one-page newspaper front page summing up the world news
of Tuesday 24 November 2026. Pure Pillow, no network, deterministic output."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (20, 24, 29)
RED = (179, 32, 42)
NAVY = (16, 36, 62)
NAVY_LIGHT = (127, 178, 217)
GOLD = (160, 118, 20)
GRAY = (92, 96, 100)
SEA = (220, 235, 245)
LAND = (120, 165, 110)

NOTO = "/usr/share/fonts/truetype/noto/"
SERIF_B = NOTO + "NotoSerif-Bold.ttf"
SERIF = NOTO + "NotoSerif-Regular.ttf"
SANS_B = NOTO + "NotoSans-Bold.ttf"
SANS = NOTO + "NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=1.25):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 40  # margin

# ---------- masthead ----------
d.text((W // 2, 30), "THE WORLD TODAY", font=font(SERIF_B, 64), fill=INK, anchor="ma")
d.line([(M, 108), (W - M, 108)], fill=INK, width=3)
d.line([(M, 114), (W - M, 114)], fill=INK, width=1)
d.text((M, 122), "Tuesday, 24 November 2026", font=font(SANS_B, 21), fill=INK)
d.text((W - M, 122), "ONE DAY · ONE PAGE · THE WHOLE WORLD", font=font(SANS, 19), fill=GRAY, anchor="ra")
d.line([(M, 152), (W - M, 152)], fill=INK, width=1)

# ---------- lead story: COP31 ----------
LY = 168
d.text((M, LY), "CLIMATE  ·  COP31 SUMMIT", font=font(SANS_B, 20), fill=RED)
lead_head = "COP31 TALKS COLLAPSE WITH NO DEAL"
hy = text_block(d, M, LY + 30, lead_head, font(SERIF_B, 44), INK, 610, leading=1.12)
lead_deck = ("After two weeks of negotiations the summit ends in deadlock: the EU and its "
             "allies reject a final text that dropped any mention of moving away from "
             "fossil fuels. \u201cDid all that we could,\u201d one negotiator says.")
text_block(d, M, hy + 10, lead_deck, font(SERIF, 23), (40, 44, 48), 596, leading=1.3)

# globe visual (right of lead)
cx, cy, r = 822, 300, 108
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SEA, outline=INK, width=3)
for i, lat in enumerate((-58, -20, 20, 58)):
    w_ = int(r * (1 - (lat / 90) ** 2) ** 0.5)
    yy = cy + int(lat * r / 90)
    d.arc([cx - w_, yy - 14, cx + w_, yy + 14], 0, 360, fill=(150, 180, 200), width=1)
d.ellipse([cx - 78, cy - 62, cx - 18, cy - 8], fill=LAND)          # americas blob
d.ellipse([cx + 6, cy - 40, cx + 66, cy + 16], fill=LAND)          # europe/asia blob
d.ellipse([cx - 30, cy + 26, cx + 26, cy + 78], fill=LAND)         # africa blob
crack = [(cx - 60, cy - 100), (cx - 30, cy - 55), (cx - 48, cy - 12), (cx - 8, cy + 30),
         (cx - 26, cy + 66), (cx + 6, cy + 104)]
d.line(crack, fill=RED, width=6, joint="curve")
d.polygon([(cx + 58, cy + 96), (cx + 76, cy + 58), (cx + 94, cy + 96)], fill=(232, 120, 40))
d.polygon([(cx + 68, cy + 96), (cx + 76, cy + 74), (cx + 84, cy + 96)], fill=(245, 180, 60))
d.text((cx, cy + r + 10), "A PLANET, DEADLOCKED", font=font(SANS_B, 17), fill=GRAY, anchor="ma")

d.line([(M, 486), (W - M, 486)], fill=INK, width=1)

# ---------- second story: sea drones ----------
SY = 502
d.rectangle([M, SY, W - M, SY + 176], fill=NAVY)
d.text((M + 24, SY + 16), "WAR AT SEA  ·  LIBYA", font=font(SANS_B, 19), fill=(240, 190, 90))
text_block(d, M + 24, SY + 44, "UKRAINE SEA DRONES HIT RUSSIAN WARSHIP OFF LIBYA",
           font(SERIF_B, 33), (245, 247, 250), 640, leading=1.15)
text_block(d, M + 24, SY + 118, "Kyiv says unmanned boats sank a Russian warship at Benghazi; "
                                "the UN mission demands an independent investigation.",
           font(SANS, 19), (205, 218, 232), 636, leading=1.25)
# ship silhouette
sx, sy = 730, SY + 96
d.polygon([(sx, sy), (sx + 210, sy), (sx + 182, sy + 26), (sx + 26, sy + 26)], fill=(10, 22, 40))
d.rectangle([sx + 60, sy - 22, sx + 130, sy], fill=(10, 22, 40))
d.line([(sx + 150, sy - 40), (sx + 150, sy)], fill=(10, 22, 40), width=5)
for i in range(3):
    d.arc([sx - 10 + i * 74, sy + 30, sx + 60 + i * 74, sy + 52], 0, 180, fill=NAVY_LIGHT, width=3)
d.polygon([(sx + 30, sy - 74), (sx + 52, sy - 62), (sx + 30, sy - 52)], fill=(240, 190, 90))
d.polygon([(sx + 120, sy - 88), (sx + 142, sy - 76), (sx + 120, sy - 66)], fill=(240, 190, 90))

# ---------- grid of four ----------
GY = 700
items = [
    ("SPACE", RED, "NATO VOWS TO COUNTER SPACE THREAT",
     "Rutte says the alliance will defend against any threat in orbit, after reports Russia is preparing a nuclear-armed satellite."),
    ("HUMAN COST", GOLD, "LANDMINES KILL OR MAIM 7,000",
     "Casualties hit a five-year high in a new global report; Myanmar and Syria top the list."),
    ("TECH & LAW", NAVY, "U.S. STATES SUE OVER GROK IMAGES",
     "States sue Elon Musk's companies over sexualised images generated by the Grok chatbot."),
    ("CULTURE", (90, 60, 140), "GTA VI HACKER GETS 7 YEARS",
     "The hacker behind the Grand Theft Auto VI leaks is sentenced in a UK court \u2014 but walks free."),
]
col_w = (W - 2 * M - 24) // 2
row_y = GY
for row in range(2):
    row_h = 0
    for col in range(2):
        kick, color, head, deck = items[row * 2 + col]
        x = M + col * (col_w + 24)
        y = row_y
        d.text((x + 18, y), kick, font=font(SANS_B, 16), fill=color)
        hy = text_block(d, x + 18, y + 22, head, font(SERIF_B, 21), INK, col_w - 22, leading=1.1)
        dy = text_block(d, x + 18, hy + 3, deck, font(SANS, 15), (52, 56, 60), col_w - 22, leading=1.2)
        d.rectangle([x, y, x + 6, dy - 4], fill=color)
        row_h = max(row_h, dy - row_y)
    row_y += row_h + 10

# ---------- footer ----------
FY = 948
d.line([(M, FY), (W - M, FY)], fill=INK, width=2)
also = ("ALSO TODAY:  Russian strikes kill at least 15 in the Kyiv region  ·  Germany first to "
        "gain access to Ukraine's Delta battle system  ·  Israeli strikes kill six in Gaza  ·  "
        "Armenia unveils draft constitution in peace push with Azerbaijan")
text_block(d, M, FY + 10, also, font(SANS, 16), (52, 56, 60), W - 2 * M, leading=1.25)
d.text((W - M, H - 24), "Compiled from Reuters, BBC, UN News, SCMP and Kyiv Independent reports, 24 Nov 2026",
       font=font(SANS, 14), fill=GRAY, anchor="ra")

img.save("/home/hatch/workspace/makefun/repos/news-image-20261124/entry.png", optimize=True)
print("saved")
