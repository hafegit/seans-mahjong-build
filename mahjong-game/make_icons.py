#!/usr/bin/env python3
"""Generate PWA icons for Sean's AI New Year Mahjong.
Run once: python3 make_icons.py
Outputs: icons/icon-192.png  icons/icon-512.png
"""
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

GOLD      = (212, 160,  23)
GOLD_DK   = (100,  70,   8)
GOLD_SHAD = ( 80,  50,   5)
BG        = (  8,   8,   8)
TILE_BG   = ( 18,   8,   0)

def make_icon(size):
    img  = Image.new('RGB', (size, size), BG)
    draw = ImageDraw.Draw(img)

    # ── Tile dimensions (3:4 ratio, centred) ──────────────────────────────
    pad  = size // 7
    tw   = size - pad * 2
    th   = int(tw * 4 / 3)
    if th > size - pad * 2:
        th = size - pad * 2
        tw = int(th * 3 / 4)
    tx = (size - tw) // 2
    ty = (size - th) // 2
    r  = size // 11

    # ── 3-D shadow layers ─────────────────────────────────────────────────
    shad = max(2, size // 60)
    for off in range(shad, 0, -1):
        alpha = int(180 * off / shad)
        draw.rounded_rectangle(
            [tx + off*2, ty + off*2, tx + tw + off*2, ty + th + off*2],
            radius=r, fill=GOLD_SHAD)

    # ── Gold outer tile ───────────────────────────────────────────────────
    draw.rounded_rectangle([tx, ty, tx + tw, ty + th], radius=r, fill=GOLD)

    # ── Dark inner fill ───────────────────────────────────────────────────
    m = max(4, size // 22)
    draw.rounded_rectangle(
        [tx + m, ty + m, tx + tw - m, ty + th - m],
        radius=max(2, r - m // 2), fill=TILE_BG)

    # ── Inner gold frame ──────────────────────────────────────────────────
    m2    = m + max(2, size // 50)
    frame = (160, 110, 12)
    lw    = max(1, size // 90)
    draw.rounded_rectangle(
        [tx + m2, ty + m2, tx + tw - m2, ty + th - m2],
        radius=max(1, r - m2 // 2), outline=frame, width=lw)

    # ── Central character 蛇 (Snake) ──────────────────────────────────────
    font_size = int(tw * 0.62)
    font = None
    for path in [
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/STHeiti Light.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
        '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
    ]:
        try:
            font = ImageFont.truetype(path, font_size)
            break
        except Exception:
            pass

    char = '蛇'
    if font:
        bb   = draw.textbbox((0, 0), char, font=font)
        cw   = bb[2] - bb[0]
        ch   = bb[3] - bb[1]
        cx   = tx + (tw - cw) // 2 - bb[0]
        cy   = ty + (th - ch) // 2 - bb[1] - size // 40
        # subtle glow
        for dx, dy in [(-1,-1),(1,-1),(-1,1),(1,1)]:
            draw.text((cx+dx, cy+dy), char, font=font, fill=GOLD_DK)
        draw.text((cx, cy), char, font=font, fill=GOLD)
    else:
        # Fallback: concentric diamonds
        cx, cy = tx + tw // 2, ty + th // 2
        for d, col in [(tw//3, GOLD), (tw//5, TILE_BG), (tw//8, GOLD)]:
            draw.polygon([(cx, cy-d),(cx+d,cy),(cx,cy+d),(cx-d,cy)], fill=col)

    # ── Corner dots (decorative) ──────────────────────────────────────────
    dot_r  = max(2, size // 55)
    dot_off = m2 + dot_r + max(1, size // 60)
    for dx, dy in [(dot_off, dot_off), (tw-dot_off, dot_off),
                   (dot_off, th-dot_off), (tw-dot_off, th-dot_off)]:
        draw.ellipse([tx+dx-dot_r, ty+dy-dot_r, tx+dx+dot_r, ty+dy+dot_r],
                     fill=frame)

    return img

for sz in [192, 512]:
    make_icon(sz).save(f'icons/icon-{sz}.png')
    print(f'  ✓  icons/icon-{sz}.png')

print('Done.')
