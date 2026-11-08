# 7장 규칙 기반 판정과 LED 신호

<span class="chip">7주차</span> <span class="chip on">온라인</span> <span class="chip">7.4절 기기 대여 시 실습</span>

6장에서 확인한 분포를 근거로 판정 임계값을 정하고, z-점수로 이상 측정값을 검출한다. 판정 규칙이 발생시키는 오경보와 미검출을 집계해 임계값 조정에 따른 상충을 확인한다. 마지막 절에서는 사이버파이의 소리 크기 측정값을 정상·주의·경고 3단계로 판정해 LED 스트립에 표시한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch07.ipynb){ .md-button .md-button--primary }

## 절 구성

- [7.1 임계값 설계](7-1.md)
- [7.2 z-점수 이상 탐지](7-2.md)
- [7.3 오경보와 미검출](7-3.md)
- [7.4 실습: 소음 단계 LED 스트립 신호등](7-4.md)

## 학습 목표

- 분위수로 판정 임계값을 정하고 단계 판정 함수를 작성한다.
- z-점수와 이동평균·이동 표준편차로 이상 측정값을 검출한다.
- 오경보와 미검출을 집계하고 임계값에 따른 상충을 설명한다.
- 측정값을 단계별 색으로 LED 스트립에 표시한다.

## 준비물

- [서울 일별 날씨 자료 2021~2025(CSV)](../data/seoul_weather_2021_2025.csv)
- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)
- 7.4절(기기 대여 시): 사이버파이, 포켓쉴드, LED 스트립(S1 포트), USB 케이블, mBlock

기기를 대여하지 않은 경우 7.1~7.3절과 7.4절의 판정 함수 부분은 Colab에서 모두 실행할 수 있다.

!!! abstract "참고 링크"
    - [pandas quantile](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)
    - [pandas rolling](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
    - [pandas crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)
    - [Makeblock mCode CyberPi API](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api)
