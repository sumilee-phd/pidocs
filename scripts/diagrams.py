# -*- coding: utf-8 -*-
"""전자책 공용 도식 생성기 — 상자·마름모·화살표·막대를 같은 규격으로 SVG에 그린다.

원칙(2026-11-08 사용자 지시): 직접 그리는 도식은 화면 캡처로 대체할 수 없는 구조도에만 사용한다.
코드 실행·도구 사용 장면은 Colab·mBlock 실제 화면을 캡처한다.

    python scripts/diagrams.py          # 전체 도식 생성
    python scripts/diagrams.py ch02     # 이름이 ch02로 시작하는 도식만 생성

색: 남색 #1f4e79(기본), 청록 #2b6b3f(온라인·정상), 적색 #9b2d2a(오프라인·경고), 회색 #5b6470(보조)
글꼴: SVG를 <img>로 넣으면 사이트 글꼴이 적용되지 않으므로 운영체제 한글 글꼴 목록을 지정한다.
"""
import os
import sys
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'assets', 'img')
FONT = "'Pretendard','Malgun Gothic','Apple SD Gothic Neo','Noto Sans KR',sans-serif"
C = {
    'navy': ('#1f4e79', '#eef3f9'), 'green': ('#2b6b3f', '#e8f3ec'), 'red': ('#9b2d2a', '#fbecea'),
    'gray': ('#5b6470', '#f3f4f6'), 'amber': ('#8a5a00', '#fff4dc'),
}


def text_w(s, size):
    """대략적인 글자 폭(한글 1.0, 그 외 0.56 비율)."""
    return sum(size if ord(ch) > 0x3000 else size * 0.56 for ch in s)


class SVG:
    def __init__(self, w, h):
        self.w, self.h, self.items = w, h, []

    def text(self, x, y, s, size=15, color='#1a1a1a', weight=400, anchor='middle'):
        lines = s.split('\n')
        y0 = y - (len(lines) - 1) * size * 0.65
        for i, ln in enumerate(lines):
            self.items.append(f'<text x="{x}" y="{y0 + i * size * 1.3:.1f}" font-size="{size}" fill="{color}" '
                              f'font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="middle">{escape(ln)}</text>')

    def box(self, x, y, w, h, label, tone='navy', size=15, sub=None, r=8, weight=600):
        line, fill = C[tone]
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{line}" stroke-width="1.6"/>')
        if sub:
            subs = sub.split('\n')
            ss = size - 3
            block = size * 1.4 + len(subs) * ss * 1.3
            top = y + (h - block) / 2
            self.text(x + w / 2, top + size * 0.6, label, size, line, weight)
            for i, ln in enumerate(subs):
                self.text(x + w / 2, top + size * 1.4 + ss * 0.65 + i * ss * 1.3, ln, ss, '#333', 400)
        else:
            self.text(x + w / 2, y + h / 2, label, size, line, weight)

    def diamond(self, cx, cy, w, h, label, tone='amber', size=14):
        line, fill = C[tone]
        pts = f'{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}'
        self.items.append(f'<polygon points="{pts}" fill="{fill}" stroke="{line}" stroke-width="1.6"/>')
        self.text(cx, cy, label, size, line, 600)

    def arrow(self, pts, label=None, lx=None, ly=None, color='#5b6470', size=13):
        d = ' '.join(f'{"M" if i == 0 else "L"}{x},{y}' for i, (x, y) in enumerate(pts))
        self.items.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6" marker-end="url(#ah)"/>')
        if label:
            self.text(lx, ly, label, size, color, 600)

    def rect(self, x, y, w, h, fill, stroke='none'):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>')

    def save(self, name):
        os.makedirs(OUT, exist_ok=True)
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
                f'font-family="{FONT}"><defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#5b6470"/></marker></defs>'
                f'<rect width="100%" height="100%" fill="#ffffff"/>')
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(head + ''.join(self.items) + '</svg>')
        print('saved', name)


# ── 1장 ──────────────────────────────────────────────
def ch01_ipo():
    s = SVG(760, 230)
    s.box(20, 50, 200, 120, '입력', 'green', 18, '센서 측정\n조도·소리·가속도\n공개 자료(날씨)')
    s.box(280, 50, 200, 120, '처리', 'navy', 18, '파이썬 프로그램\n판정 규칙\n머신러닝 모델')
    s.box(540, 50, 200, 120, '출력', 'red', 18, 'LED 스트립\n화면·스피커\n보고서·서버 전송')
    s.arrow([(220, 110), (278, 110)])
    s.arrow([(480, 110), (538, 110)])
    s.arrow([(640, 172), (640, 205), (120, 205), (120, 174)], '출력 결과가 다음 측정 조건에 영향', 380, 218, size=12)
    s.save('ch01_ipo.svg')


def ch01_16weeks():
    s = SVG(820, 190)
    parts = [('1부 파이썬 기초', 1), ('2부 분석·규칙 판정', 5), ('3부 머신러닝·탑재', 9), ('4부 생성형 AI·프로젝트', 13)]
    cw, x0 = 48, 22
    for name, start in parts:
        x = x0 + (start - 1) * cw
        s.items.append(f'<rect x="{x + 2}" y="18" width="{cw * 4 - 4}" height="30" rx="6" fill="#eef3f9" stroke="#1f4e79" stroke-width="1.2"/>')
        s.text(x + cw * 2, 33, name, 13, '#1f4e79', 600)
    for w in range(1, 17):
        x = x0 + (w - 1) * cw
        off = w % 4 == 0
        line, fill = C['red'] if off else C['green']
        s.items.append(f'<rect x="{x + 2}" y="62" width="{cw - 4}" height="56" rx="6" fill="{fill}" stroke="{line}" stroke-width="1.4"/>')
        s.text(x + cw / 2, 82, f'{w}주', 13, line, 700)
        s.text(x + cw / 2, 102, '오프' if off else '온라인', 11, line, 400)
    s.items.append('<rect x="250" y="142" width="18" height="14" rx="3" fill="#e8f3ec" stroke="#2b6b3f"/>')
    s.text(276, 149, '온라인: Colab 분석·모델 학습', 13, '#2b6b3f', 400, 'start')
    s.items.append('<rect x="500" y="142" width="18" height="14" rx="3" fill="#fbecea" stroke="#9b2d2a"/>')
    s.text(526, 149, '오프라인: 기기 측정·탑재', 13, '#9b2d2a', 400, 'start')
    s.save('ch01_16weeks.svg')


ALL = [ch01_ipo, ch01_16weeks]

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    pref = sys.argv[1] if len(sys.argv) > 1 else ''
    for fn in ALL:
        if fn.__name__.startswith(pref):
            fn()
