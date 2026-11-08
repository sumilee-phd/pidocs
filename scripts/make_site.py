# -*- coding: utf-8 -*-
"""outline.py 목차로 mkdocs.yml(nav 포함)과 장 표지·미집필 절 초안을 생성한다.

- 'STUB' 표식이 있는 페이지만 다시 생성한다. 집필한 페이지는 표식이 없으므로 보존된다.
- 사용: python scripts/make_site.py  →  mkdocs serve / mkdocs build
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from outline import PARTS  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
DOCS = os.path.join(ROOT, 'docs')
STUB = '<!-- STUB: make_site.py가 생성한 초안. 집필 후 이 줄을 지운다. -->'

YML_HEAD = """# make_site.py가 생성하는 파일. 목차는 scripts/outline.py에서 수정한다.
site_name: AI 파이썬 피지컬컴퓨팅
site_description: 사이버파이 기반 센서 측정·머신러닝·기기 반응 실습서
site_author: 이수미
site_url: https://pidocs.aifusionlab.org/ai-python/
repo_url: https://github.com/sumilee-phd/pidocs
repo_name: sumilee-phd/pidocs
edit_uri: ''
copyright: '© 2026 이수미 · 날씨 자료 <a href="https://open-meteo.com/">Open-Meteo.com</a> (CC BY 4.0)'

theme:
  name: material
  language: ko
  font: false
  palette:
    - scheme: default
      primary: custom
      accent: custom
  features:
    - navigation.indexes
    - navigation.footer
    - navigation.top
    - navigation.tracking
    - toc.follow
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.tabs.link
  icon:
    logo: material/book-open-page-variant

extra_css:
  - https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css
  - assets/css/book.css

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.keys

extra:
  homepage: https://pidocs.aifusionlab.org/
  generator: false

plugins:
  - search:
      lang: ko

nav:
  - 시작하며: index.md
"""


def num(sid):
    return sid.replace('-', '.')


def write_if_stub(path, text):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            if STUB not in f.read():
                return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return True


def main():
    nav = [YML_HEAD.rstrip('\n')]
    made = 0
    for part, chapters in PARTS:
        nav.append(f'  - {part}:')
        for cid, week, mode, ctitle, sections in chapters:
            if cid == 'appendix':
                for sid, stitle, goals, topics in sections:
                    rel = f'appendix/{sid}.md'
                    nav.append(f'    - "{stitle}": {rel}')
                    body = [f'# {stitle}', '', STUB, '', '!!! note "집필 예정"', '    이 페이지는 목차 초안입니다.', '']
                    body += [f'- {g}' for g in goals]
                    made += write_if_stub(os.path.join(DOCS, rel), '\n'.join(body) + '\n')
                continue
            n = int(cid[2:])
            nav.append(f'    - "{n}장 {ctitle}":')
            nav.append(f'      - {cid}/index.md')
            # 장 표지
            lines = [f'# {n}장 {ctitle}', '', STUB, '',
                     f'<span class="chip">{week}주차</span> <span class="chip {"off" if mode == "오프라인" else "on"}">{mode}</span>', '',
                     '## 절 구성', '']
            for sid, stitle, goals, topics in sections:
                lines.append(f'- [{num(sid)} {stitle}]({sid}.md)')
            goals_all = [g for _, _, gs, _ in sections for g in gs]
            if goals_all:
                lines += ['', '## 학습 목표', ''] + [f'- {g}' for g in goals_all]
            made += write_if_stub(os.path.join(DOCS, cid, 'index.md'), '\n'.join(lines) + '\n')
            for sid, stitle, goals, topics in sections:
                rel = f'{cid}/{sid}.md'
                nav.append(f'      - "{num(sid)} {stitle}": {rel}')
                body = [f'# {num(sid)} {stitle}', '', STUB, '',
                        '!!! note "집필 예정"', '    이 절은 목차 초안입니다. 학습 목표와 다룰 내용만 정리되어 있습니다.', '']
                if goals:
                    body += ['## 학습 목표', ''] + [f'- {g}' for g in goals] + ['']
                if topics:
                    body += ['## 다룰 내용', ''] + [f'- {t}' for t in topics] + ['']
                made += write_if_stub(os.path.join(DOCS, rel), '\n'.join(body))
    with open(os.path.join(ROOT, 'mkdocs.yml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(nav) + '\n')
    print('mkdocs.yml 갱신, 초안 페이지 생성/갱신', made, '건')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
