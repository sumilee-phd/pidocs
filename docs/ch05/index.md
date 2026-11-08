# 5장 pandas 데이터 정리

<span class="chip">5주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span>

3장에서 `csv` 모듈로 작성한 집계를 pandas로 다시 작성하고, 실제 측정 자료의 결측치·이상치를 찾아 처리 방법을 결정한다. 날짜 열에서 연·월을 추출해 월별 통계를 산출한다. 4주차 오프라인 수업에서 사이버파이로 수집한 자료도 같은 방법으로 정리한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch05.ipynb){ .md-button .md-button--primary }

## 절 구성

- [5.1 DataFrame 기초](5-1.md)
- [5.2 결측치·이상치 처리](5-2.md)
- [5.3 날짜 열과 월별 집계](5-3.md)

## 학습 목표

- CSV를 DataFrame으로 불러와 구조와 기술통계를 확인한다.
- 열 선택·행 필터·정렬로 필요한 자료를 추출한다.
- 결측치·이상치를 찾아내고 분석 목적에 맞는 처리 방법을 결정한다.
- 날짜 열에서 연·월을 추출해 그룹별로 집계한다.

## 준비물

- [서울 일별 날씨 자료 2021~2025(CSV)](../data/seoul_weather_2021_2025.csv)
- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)

!!! abstract "참고 링크"
    - [pandas 공식 문서: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
    - [pandas read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
    - [pandas 결측치 처리](https://pandas.pydata.org/docs/user_guide/missing_data.html)
    - [pandas groupby](https://pandas.pydata.org/docs/user_guide/groupby.html)
