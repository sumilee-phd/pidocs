# -*- coding: utf-8 -*-
"""본문의 「실행 결과」 자리 표시를 실제 실행 출력으로 채운다.

python 코드 블록 바로 뒤(사이에 **실행 결과** 줄 허용)의 ```text 블록 내용이 정확히 `OUT`이면,
그 장의 코드를 처음부터 순서대로 실행한 출력으로 교체한다. 이미 채운 블록은 건드리지 않는다.

    python scripts/fill_outputs.py ch03 ch05 ch06
"""
import contextlib
import io
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from outline import PARTS  # noqa: E402

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
BLOCK = re.compile(r'```(python|text)\n(.*?)```', re.S)


def run(code, ns):
    buf = io.StringIO()
    lines = code.rstrip('\n').split('\n')
    body, expr = code, None
    last = lines[-1]
    if last and not last.startswith((' ', '\t', '#')):
        try:
            compile(last, '<e>', 'eval')
            body, expr = '\n'.join(lines[:-1]), last
        except SyntaxError:
            pass
    with contextlib.redirect_stdout(buf):
        try:
            exec(body, ns)
            if expr:
                v = eval(expr, ns)
                name = type(v).__name__
                if v is not None and not any(k in name for k in ('Axes', 'Figure', 'Line2D', 'BarContainer', 'tuple')):
                    print(v)
        except Exception as e:  # noqa: BLE001
            print(f'{type(e).__name__}: {e}')
    plt.close('all')
    return buf.getvalue().rstrip('\n')


def fill_chapter(cid):
    sections = next(s for _, chs in PARTS for c, _, _, _, s in chs if c == cid)
    ns = {'input': lambda prompt='': (print(prompt + '45'), '45')[1]}
    cwd = os.getcwd()
    os.chdir(os.path.join(ROOT, 'docs', 'data'))
    changed = 0
    try:
        for sid, _, _, _ in sections:
            path = os.path.join(ROOT, 'docs', cid, f'{sid}.md')
            text = open(path, encoding='utf-8').read()
            out, pos, pending = [], 0, None
            for m in BLOCK.finditer(text):
                kind, content = m.group(1), m.group(2)
                if kind == 'python':
                    pending = None if 'import cyberpi' in content else run(content, ns)
                    continue
                if kind == 'text' and pending is not None and content.strip() == 'OUT':
                    gap = text[pos:m.start()] if False else None
                    out.append(text[pos:m.start()])
                    out.append(f'```text\n{pending}\n```')
                    pos = m.end()
                    changed += 1
                pending = None
            out.append(text[pos:])
            new = ''.join(out)
            if new != text:
                open(path, 'w', encoding='utf-8').write(new)
    finally:
        os.chdir(cwd)
    print(f'{cid}: 실행 결과 {changed}곳 채움')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for c in sys.argv[1:]:
        fill_chapter(c)
