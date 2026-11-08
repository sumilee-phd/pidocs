# 6장 시각화와 기술통계

<span class="chip">6주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span>

5장에서 정리한 날씨 자료와 수업 측정 자료를 그래프로 시각화하고, 평균·중앙값·표준편차·사분위수로 분포를 요약한다. 그룹별 분포를 비교한 결과는 7장에서 판정 기준을 정하는 근거로 사용한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch06.ipynb){ .md-button .md-button--primary }

## 절 구성

- [6.1 matplotlib 그래프](6-1.md)
- [6.2 기술통계와 분포](6-2.md)
- [6.3 실습: 계절별 기온 분포와 센서 분포](6-3.md)

## 학습 목표

- 선 그래프·막대 그래프·히스토그램을 용도에 맞게 작성한다.
- 평균과 중앙값의 차이로 분포의 치우침을 판단한다.
- 상자그림으로 사분위수와 이상치 후보를 해석한다.
- 그룹별 분포를 비교해 판정 기준 후보를 도출한다.

## 준비물

- [서울 일별 날씨 자료 2021~2025(CSV)](../data/seoul_weather_2021_2025.csv)
- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)

!!! abstract "참고 링크"
    - [matplotlib 공식 자습서](https://matplotlib.org/stable/tutorials/index.html)
    - [matplotlib boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)
    - [pandas describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
