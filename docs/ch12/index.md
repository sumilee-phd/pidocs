# 12장 기기 탑재와 날씨 신호등

<span class="chip">12주차</span> <span class="chip off">오프라인</span> <span class="chip">사이버파이·포켓쉴드·LED 스트립</span>

세 번째 등교일에는 온라인 주에 학습한 모델을 사이버파이에 탑재한다. 10장의 강수 분류 모델과 공개 예보를 LED 스트립에 함께 표시하는 날씨 신호등을 구성하고, 11장의 동작 분류 모델을 Upload 모드로 탑재해 기기 단독으로 동작을 판정한다. 다른 학생의 동작으로 모델을 평가하는 교차 평가로 일반화 성능을 확인한 뒤, 최종 프로젝트 주제를 정한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch12.ipynb){ .md-button .md-button--primary }

## 절 구성

- [12.1 날씨 신호등](12-1.md)
- [12.2 제스처 인식기 Upload 탑재](12-2.md)
- [12.3 교차 평가](12-3.md)
- [12.4 프로젝트 주제 선정](12-4.md)

## 학습 목표

- 결정트리를 조건문으로 변환한 모델을 기기에 탑재해 실시간으로 판정한다.
- 다른 학생의 동작으로 모델을 평가하고 정확도 하락의 원인을 분석한다.
- 직무 현장의 문제에서 측정·판정·표시 프로젝트 주제를 도출한다.

## 준비물

- 사이버파이, 포켓쉴드, LED 스트립(12.1절), USB 케이블
- 11.3절의 `classify` 함수와 특징 계산 함수
- [제스처 예시 자료(CSV)](../data/gesture_example.csv)(12.3절)

!!! abstract "참고 링크"
    - [Open-Meteo 예보 API](https://open-meteo.com/en/docs)
    - [scikit-learn 교차 검증](https://scikit-learn.org/stable/modules/cross_validation.html)
