# -*- coding: utf-8 -*-
"""브라우저 캡처 여러 장의 영역을 잘라 세로로 이어 붙인다.

한 화면에 들어가지 않는 긴 코드 셀을 위·아래 캡처로 나누어 찍은 경우에 사용한다.
영역이 하나면 crop_shots.py와 같다. 계정 사진 영역(1398~1448, 8~56)은 회색 원으로 가린다.

    python scripts/stitch_shots.py 이름.png 원본1.jpg:x0,y0,x1,y1 원본2.jpg:x0,y0,x1,y1
"""
import os
import sys

from PIL import Image, ImageDraw

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'docs', 'assets', 'img')
AVATAR = (1398, 8, 1448, 56)


def piece(spec):
    src, box = spec.rsplit(':', 1)
    x0, y0, x1, y1 = (int(v) for v in box.split(','))
    im = Image.open(src).convert('RGB')
    if x0 < AVATAR[2] and x1 > AVATAR[0] and y0 < AVATAR[3] and y1 > AVATAR[1]:
        ImageDraw.Draw(im).ellipse(AVATAR, fill=(200, 200, 200))
    return im.crop((x0, y0, x1, y1))


def stitch(name, specs):
    parts = [piece(s) for s in specs]
    w = max(p.width for p in parts)
    out = Image.new('RGB', (w, sum(p.height for p in parts)), (255, 255, 255))
    y = 0
    for p in parts:
        out.paste(p, (0, y))
        y += p.height
    out.save(os.path.join(OUT, name), optimize=True)
    print('saved', name, out.size)


if __name__ == '__main__':
    stitch(sys.argv[1], sys.argv[2:])
