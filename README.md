# AI 파이썬 피지컬컴퓨팅 (웹 전자책 원본)

2027 P-TECH 토요일 과정 AI 파이썬 융합과목의 주교재. MkDocs Material로 위키독스형 사이트를 생성한다. 게시 예정 위치는 aifusionlab.org(주소·게시 방식 미정).

## 구조

| 경로 | 내용 |
|---|---|
| `scripts/outline.py` | 목차 원본(부·장·절, 주차, 수업 방식, 절별 학습 목표) |
| `scripts/make_site.py` | 목차로 `mkdocs.yml` nav와 미집필 절 초안 생성. `STUB` 표식이 없는 페이지는 덮어쓰지 않음 |
| `scripts/make_dataset.py` | Open-Meteo 재분석 자료로 `docs/data/seoul_weather_2021_2025.csv` 생성 |
| `scripts/capture_ch09_ch10.py` | 9·10장 코드 블록을 실행해 본문 실행 결과의 근거 출력 |
| `scripts/verify_ch09_ch10.py` | 9장 그림(`ch09_pred_vs_actual.png`) 생성과 수치 검증 |
| `scripts/verify_ch12_rule.py`, `ch12_weather_signal.py` | 12.1절 조건문 모델과 원래 결정트리의 일치 검증, 가짜 cyberpi로 예보 수신 시험 |
| `docs/` | 페이지 원고(md), 자료, 그림, CSS |

## 작업 순서

```bash
python scripts/make_site.py
python -m mkdocs serve -a 127.0.0.1:8770
python -m mkdocs build --strict
```

목차를 바꿀 때는 `outline.py`를 수정하고 `make_site.py`를 다시 실행한다. 절을 집필하면 페이지 첫머리의 `<!-- STUB ... -->` 줄을 지운다.

## 집필 현황(2026-11-08)

집필: 시작하며, 1.2, 4.7, 9장 전체, 10장 전체, 12.1, 부록 D. 나머지는 학습 목표·다룰 내용만 있는 초안.

실기기 확인 전: 4.7·12.1절의 LED 스트립 점등, mBlock 내장 파이썬 3.6.5의 HTTPS 접속, 1.2절 mBlock 웹 편집기 메뉴 이름.
