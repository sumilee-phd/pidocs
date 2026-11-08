# AI 파이썬 피지컬컴퓨팅 (웹 전자책 원본)

2027 P-TECH 토요일 과정 AI 파이썬 융합과목의 주교재. MkDocs Material로 위키독스형 사이트를 생성한다. 게시 주소는 <https://pidocs.aifusionlab.org/ai-python/>(허브 <https://pidocs.aifusionlab.org/>), 저장소 <https://github.com/sumilee-phd/pidocs>.

## 구조

| 경로 | 내용 |
|---|---|
| `scripts/outline.py` | 목차 원본(부·장·절, 주차, 수업 방식, 절별 학습 목표) |
| `scripts/make_site.py` | 목차로 `mkdocs.yml` nav와 미집필 절 초안 생성. `STUB` 표식이 없는 페이지는 덮어쓰지 않음 |
| `scripts/make_dataset.py` | Open-Meteo 재분석 자료로 `docs/data/seoul_weather_2021_2025.csv` 생성 |
| `scripts/capture_ch09_ch10.py` | 9·10장 코드 블록을 실행해 본문 실행 결과의 근거 출력 |
| `scripts/verify_ch09_ch10.py` | 9장 그림(`ch09_pred_vs_actual.png`) 생성과 수치 검증 |
| `scripts/verify_ch12_rule.py`, `ch12_weather_signal.py` | 12.1절 조건문 모델과 원래 결정트리의 일치 검증, 가짜 cyberpi로 예보 수신 시험 |
| `scripts/fill_outputs.py` | 장별 python 블록을 순서대로 실행해 내용이 `OUT`인 ```text 블록에 실제 출력 기입(`python scripts/fill_outputs.py ch03 ch05`) |
| `scripts/make_notebooks.py` | 본문 ```python 블록으로 장별 Colab 노트북(`notebooks/chNN.ipynb`) 생성 |
| `scripts/crop_shots.py` | 브라우저 캡처에서 필요한 영역을 잘라 그림으로 저장 |
| `scripts/stitch_shots.py` | 한 화면에 들어가지 않는 셀을 위·아래 캡처에서 잘라 세로로 이어 붙임(`이름.png 원본.jpg:x0,y0,x1,y1 …`) |
| `scripts/number_figures.py` | 장 안의 그림 캡션 번호(`그림 N-?` 포함)를 절 순서대로 다시 매김 |
| `scripts/diagrams.py` | 캡처로 대체할 수 없는 구조도만 SVG로 생성 |
| `docs/` | 페이지 원고(md), 자료, 그림, CSS |

## 작업 순서

```bash
python scripts/make_site.py
python -m mkdocs serve -a 127.0.0.1:8770
python -m mkdocs build --strict
python scripts/publish.py --push   # _site 조립 후 gh-pages 가지로 공개 게시
```

## 게시 구조

| 항목 | 값 |
|---|---|
| 저장소 | `sumilee-phd/pidocs`(공개), 원고는 `main`, 게시본은 `gh-pages` |
| 게시본 구성 | `/` = `hub/index.html`(piDocs 허브), `/ai-python/` = 이 책 |
| 사용자 도메인 | `pidocs.aifusionlab.org`(GitHub Pages, `CNAME` 파일은 publish.py가 생성) |
| DNS | Cloudflare에 CNAME `pidocs` → `sumilee-phd.github.io`, 프록시 끔(DNS only) |
| 푸시 계정 | 푸시 전 `gh auth switch --user sumilee-phd` |

목차를 바꿀 때는 `outline.py`를 수정하고 `make_site.py`를 다시 실행한다. 절을 집필하면 페이지 첫머리의 `<!-- STUB ... -->` 줄을 지운다.

## 집필 현황(2026-11-09)

집필: 시작하며, 1장·2장 전체(11/8, Colab·mBlock 실행 화면 캡처 18장), 3장·5장·6장 전체(11/9, Colab 캡처 12장), 7장 전체(11/9, Colab 캡처 13장), 4.7, 9장·10장(11/9 그래프 코드 7개 추가, Colab 캡처 23장), 12.1, 부록 D. 나머지는 학습 목표·다룰 내용만 있는 초안.

실물 사진이 필요한 자리는 본문에 `<!-- PHOTO: 이름 — 장면 -->` 표식으로 남긴다(`grep -rn "PHOTO:" docs`). 촬영 목록은 업무 저장소의 `ICT폴리텍_piDocs_실물사진촬영목록_20261109.md`, 사진은 `_raw/photos/`에 둔다.

그림 원칙(사용자 지시): 직접 그리지 않고 실제 실행 화면을 캡처한다. 캡처 원본은 `_raw/`(git 제외), 자르기는 `scripts/crop_shots.py`(계정 사진 자동 가림). 노트북은 `scripts/make_notebooks.py`가 본문 코드로 생성한다.

실기기 확인 전: 4.7·12.1절의 LED 스트립 점등, mBlock 내장 파이썬 3.6.5의 HTTPS 접속, 1.2절 mBlock 웹 편집기 메뉴 이름.
