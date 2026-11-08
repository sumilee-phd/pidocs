# -*- coding: utf-8 -*-
"""장 안의 그림 캡션 번호를 절 순서대로 다시 매긴다.

<figcaption>그림 N-? …</figcaption> 또는 기존 번호(그림 9-3)를 장 번호-일련번호로 교체한다.
본문 안의 그림 번호 참조는 바꾸지 않으므로, 참조가 있으면 실행 후 확인한다.

    python scripts/number_figures.py ch09 ch10
"""
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from outline import PARTS  # noqa: E402

CAP = re.compile(r'<figcaption>그림 (?:N-\?|\d+-\?|\d+-\d+) ')


def number(cid):
    sections = next(s for _, chs in PARTS for c, _, _, _, s in chs if c == cid)
    n = 0
    for sid, _, _, _ in sections:
        path = os.path.join(ROOT, 'docs', cid, f'{sid}.md')
        text = open(path, encoding='utf-8').read()

        def repl(_m):
            nonlocal n
            n += 1
            return f'<figcaption>그림 {int(cid[2:])}-{n} '
        new = CAP.sub(repl, text)
        if new != text:
            open(path, 'w', encoding='utf-8').write(new)
    print(f'{cid}: 그림 {n}개')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for c in sys.argv[1:]:
        number(c)
