# 3장 자료구조와 파일

<span class="chip">3주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span>

측정값 여러 건을 리스트와 딕셔너리로 다루고, CSV 파일로 저장하고 읽는 방법을 실습한다. 이 장부터 실제 자료 두 가지를 사용한다. 하나는 11/4 정보통신학과 수업에서 측정 노드 14대가 측정한 Wi-Fi 신호 세기 기록이고, 다른 하나는 9·10장의 머신러닝에 사용할 서울 일별 날씨 자료다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch03.ipynb){ .md-button .md-button--primary }

## 절 구성

- [3.1 리스트와 딕셔너리](3-1.md)
- [3.2 파일 입출력과 CSV](3-2.md)
- [3.3 실습: 서울 날씨 자료 첫 분석](3-3.md)

## 학습 목표

- 리스트의 색인·슬라이싱·추가·정렬을 사용한다.
- 딕셔너리로 기록을 표현하고 항목별 개수·합계를 집계한다.
- CSV 파일을 쓰고, `csv.DictReader`로 기록을 읽어 집계한다.
- 날씨 자료에서 연도별 평균기온·강수일수·연강수량을 산출한다.

## 준비물

- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)
- [서울 일별 날씨 자료 2021~2025(CSV)](../data/seoul_weather_2021_2025.csv)

!!! abstract "참고 링크"
    - [파이썬 자습서: 자료 구조](https://docs.python.org/ko/3/tutorial/datastructures.html)
    - [csv 모듈 문서](https://docs.python.org/ko/3/library/csv.html)
    - [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)
