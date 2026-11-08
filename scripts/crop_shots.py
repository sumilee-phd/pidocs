# -*- coding: utf-8 -*-
"""브라우저 캡처(_raw/ 또는 지정 경로)에서 필요한 영역을 잘라 docs/assets/img/에 저장한다.
계정 사진 영역(오른쪽 위)이 포함되면 회색 원으로 가린다.

    python scripts/crop_shots.py 원본경로 출력이름 x0 y0 x1 y1
"""
import os, sys
from PIL import Image, ImageDraw
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'assets', 'img')
AVATAR = (1398, 8, 1448, 56)   # 1462x812 캡처 기준 Colab 계정 사진 위치


def crop(src, name, box):
    im = Image.open(src).convert('RGB')
    x0, y0, x1, y1 = box
    if x0 < AVATAR[2] and x1 > AVATAR[0] and y0 < AVATAR[3] and y1 > AVATAR[1]:
        d = ImageDraw.Draw(im)
        d.ellipse(AVATAR, fill=(200, 204, 210))
    im.crop(box).save(os.path.join(OUT, name), optimize=True)
    print('saved', name, im.crop(box).size)


if __name__ == '__main__':
    crop(sys.argv[1], sys.argv[2], tuple(int(v) for v in sys.argv[3:7]))
