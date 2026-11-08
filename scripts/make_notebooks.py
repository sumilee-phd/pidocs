# -*- coding: utf-8 -*-
"""본문 코드 블록으로 장별 Colab 노트북(notebooks/chNN.ipynb)을 생성한다.

- 집필한 절(STUB 표식 없는 페이지)의 ```python 블록을 절 순서대로 추출한다.
- 사이버파이 기기 코드(import cyberpi)는 Colab에서 실행할 수 없으므로 제외한다.
- 자료가 필요한 장은 첫 셀에 자료 내려받기 명령을 넣는다.

    python scripts/make_notebooks.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from outline import PARTS  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DOCS = os.path.join(ROOT, 'docs')
OUT = os.path.join(ROOT, 'notebooks')
SITE = 'https://pidocs.aifusionlab.org/ai-python/'
RAW = 'https://raw.githubusercontent.com/sumilee-phd/pidocs/main/docs/'  # 자료 내려받기는 저장소 원본에서
W, R = 'data/seoul_weather_2021_2025.csv', 'data/class_rssi_20261104.csv'
GX = 'data/gesture_example.csv'
DATA = {  # 장 → 내려받을 자료
    'ch03': [W, R], 'ch05': [W, R], 'ch06': [W, R], 'ch07': [W, R], 'ch09': [W], 'ch10': [W], 'ch11': [GX], 'ch12': [GX], 'ch13': [R], 'ch14': [R],
}
CODE = re.compile(r'```python\n(.*?)```', re.S)


def md_cell(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': text.splitlines(keepends=True)}


def code_cell(code):
    return {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [],
            'source': code.rstrip('\n').splitlines(keepends=True)}


def build(cid, ctitle, sections):
    cells = [md_cell(f'# {ctitle}\n\n이 노트북은 웹 교재 [{ctitle}]({SITE}{cid}/)의 본문 코드를 절 순서대로 담고 있습니다. '
                     '위에서부터 차례로 실행하면서 본문의 실행 결과와 비교합니다.')]
    if cid in DATA:
        cmds = '\n'.join(f'!wget -q -nc {RAW}{p}' for p in DATA[cid])
        cells.append(md_cell('## 실습 자료 내려받기'))
        cells.append(code_cell(cmds + '\n!ls *.csv'))
    n = 0
    for sid, stitle, _, _ in sections:
        path = os.path.join(DOCS, cid, f'{sid}.md')
        if not os.path.exists(path):
            continue
        text = open(path, encoding='utf-8').read()
        if 'STUB' in text.split('\n', 3)[2] if text.count('\n') > 2 else False:
            continue
        blocks = [b for b in CODE.findall(text) if 'import cyberpi' not in b]
        if not blocks:
            continue
        cells.append(md_cell(f'## {sid.replace("-", ".")} {stitle}\n\n[본문 보기]({SITE}{cid}/{sid}/)'))
        for b in blocks:
            cells.append(code_cell(b))
            n += 1
    if n == 0:
        return 0
    nb = {'cells': cells, 'metadata': {'colab': {'provenance': []}, 'kernelspec': {'name': 'python3', 'display_name': 'Python 3'},
                                       'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 5}
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, f'{cid}.ipynb'), 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    return n


def main():
    for _, chapters in PARTS:
        for cid, week, mode, ctitle, sections in chapters:
            if cid == 'appendix':
                continue
            n = build(cid, f'{int(cid[2:])}장 {ctitle}', sections)
            if n:
                print(f'{cid}.ipynb  코드 셀 {n}개')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
