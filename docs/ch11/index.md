# 11장 동작 분류와 엣지 AI

<span class="chip">11주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span>

8.5절에서 수집한 가속도 자료로 사이버파이를 들고 하는 동작 4종(정지·흔들기·기울이기·원 그리기)을 분류하는 모델을 학습한다. 원시 측정값을 일정 구간으로 나누어 통계 특징을 추출하고, kNN과 결정트리의 정확도와 해석 가능성을 비교한다. 학습한 결정트리를 외부 라이브러리 없는 if 문으로 변환해, 12장에서 사이버파이에 탑재할 수 있는 형태로 만든다. 학습한 모델을 서버가 아닌 기기에서 직접 실행하는 방식을 엣지 AI(edge AI)라고 한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch11.ipynb){ .md-button .md-button--primary }

!!! warning "이 장의 자료는 예시 자료다"
    이 장의 수치와 그래프는 8.5절 기록 규칙과 같은 형식으로 프로그램이 생성한 **예시 자료**(`gesture_example.csv`, 가상 수강생 4명)로 산출했다. 생성 코드는 저장소의 `scripts/make_gesture_example.py`에 공개했다. 2026-11-16 주에 수집하는 실측 자료로 교체하면 수치가 달라진다. 분석 절차와 코드는 그대로 사용한다.

## 절 구성

- [11.1 가속도 자료의 구간 특징](11-1.md)
- [11.2 kNN과 결정트리 비교](11-2.md)
- [11.3 결정트리의 조건문 변환](11-3.md)
- [11.4 트리 깊이와 정확도의 상충](11-4.md)

## 학습 목표

- 창 크기와 이동 간격을 정해 원시 측정값에서 구간 통계 특징을 추출한다.
- kNN과 결정트리를 학습하고 정확도와 해석 가능성을 비교한다.
- 결정트리를 외부 라이브러리 없는 if 문 함수로 변환하고 원래 모델과의 일치를 검증한다.
- 기기 탑재 조건을 고려해 트리 깊이를 결정한다.

## 준비물

- [제스처 예시 자료(CSV)](../data/gesture_example.csv)
- 8.5절에서 수집한 본인의 제스처 CSV(실측 자료로 실습하는 경우)

!!! abstract "참고 링크"
    - [scikit-learn KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
    - [scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
    - [scikit-learn export_text](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html)
