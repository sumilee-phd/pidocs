# -*- coding: utf-8 -*-
"""9·10장에 Colab 실행 화면 그림과 그래프 코드 블록을 추가한다(1회 실행용, 2026-11-09)."""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
F = chr(96) * 3  # 코드 펜스


def fig(name, alt, cap):
    return f'\n<figure markdown="span">\n  ![{alt}](../assets/img/{name}.png)\n  <figcaption>그림 N-? {cap}</figcaption>\n</figure>\n'


def code(src):
    return f'\n{F}python\n{src.strip()}\n{F}\n'


def add_output_figs(path, figs):
    """python 블록 + 실행 결과 text 블록 뒤에 그림을 차례로 삽입한다."""
    s = open(path, encoding='utf-8').read()
    pat = re.compile(F + r'python\n.*?' + F + r'\n\n\*\*실행 결과\*\*\n\n' + F + r'text\n.*?' + F + r'\n', re.S)
    ms = list(pat.finditer(s))
    assert len(ms) == len(figs), (path, len(ms), len(figs))
    for m, f in reversed(list(zip(ms, figs))):
        s = s[:m.end()] + fig(*f) + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)


def insert_after(path, anchor, text):
    s = open(path, encoding='utf-8').read()
    assert s.count(anchor) == 1, (path, anchor[:30])
    i = s.index(anchor) + len(anchor)
    open(path, 'w', encoding='utf-8').write(s[:i] + text + s[i:])


def replace(path, old, new):
    s = open(path, encoding='utf-8').read()
    assert s.count(old) == 1, (path, old[:30])
    open(path, 'w', encoding='utf-8').write(s.replace(old, new))


D9 = os.path.join(ROOT, 'docs', 'ch09')
D10 = os.path.join(ROOT, 'docs', 'ch10')

# ---------- 9장: 실행 결과 화면
add_output_figs(f'{D9}/9-2.md', [
    ('ch09_colab_load', '자료 불러오기 실행 화면', 'Colab에서 실행한 날씨 자료 불러오기'),
    ('ch09_colab_label', '레이블 생성 실행 화면', 'Colab에서 생성한 다음 날 평균기온 레이블'),
    ('ch09_colab_doy', '계절 위치 특징 실행 화면', 'Colab에서 산출한 계절 위치 특징 doy_sin·doy_cos'),
])
add_output_figs(f'{D9}/9-3.md', [('ch09_colab_split', '시간 순서 분할 실행 화면', 'Colab에서 실행한 학습·평가 데이터 분할')])
add_output_figs(f'{D9}/9-4.md', [
    ('ch09_colab_coef', '선형회귀 계수 실행 화면', 'Colab에서 학습한 선형회귀 계수와 절편'),
    ('ch09_colab_pred', '예측 결과 실행 화면', 'Colab에서 실행한 2025년 다음 날 평균기온 예측'),
])
add_output_figs(f'{D9}/9-5.md', [
    ('ch09_colab_metrics', '회귀 평가 지표 실행 화면', 'Colab에서 산출한 MAE·RMSE·R²'),
    ('ch09_colab_baseline', '기준선 MAE 실행 화면', 'Colab에서 산출한 기준선 모델의 MAE'),
    ('ch09_colab_errors', '오차 상위 날짜 실행 화면', 'Colab에서 출력한 오차 상위 3일'),
])

replace(f'{D9}/9-2.md', '자료실의 `seoul_weather_2021_2025.csv`를 Colab에 업로드한 뒤 다음 코드를 실행한다.',
        '장 노트북의 첫 셀로 자료를 내려받거나 자료실의 `seoul_weather_2021_2025.csv`를 Colab에 업로드한 뒤 다음 코드를 실행한다.')

insert_after(f'{D9}/9-2.md', '두 값을 함께 사용하면 1년의 모든 날짜가 원 위의 한 점으로 표현되고, 12월 31일과 1월 1일은 인접한 점이 된다.\n',
             '\n2021년 365일의 두 값을 산점도로 표시하고, 점의 색을 그날의 평균기온으로 지정해 원 위의 위치와 기온의 관계를 확인한다.\n'
             + code('''
import matplotlib.pyplot as plt

one = df[df["date"].dt.year == 2021]
plt.figure(figsize=(5, 4.5))
plt.scatter(one["doy_cos"], one["doy_sin"], c=one["temp_mean"], cmap="coolwarm", s=12)
plt.colorbar(label="temp_mean (C)")
plt.xlabel("doy_cos")
plt.ylabel("doy_sin")
plt.axis("equal")
plt.show()
''')
             + fig('ch09_colab_season_circle', '계절 위치 특징 산점도', 'Colab에서 출력한 2021년 날짜별 계절 위치와 평균기온(색)')
             + '\n1월 1일은 원의 오른쪽 (1, 0)에 위치하고, 날짜가 진행할수록 점은 시계 반대 방향으로 이동한다. 원의 오른쪽에는 겨울의 파란 점이, 왼쪽에는 여름의 빨간 점이 모인다. 원 위의 위치가 연속적으로 변화하면 기온의 색도 연속적으로 변화하므로, 두 특징이 계절 정보를 담고 있음을 확인할 수 있다.\n')

insert_after(f'{D9}/9-3.md', '레이블 열 `target_temp`와 날짜 열 `date`는 특징에 포함하지 않는다.\n',
             '\n학습 데이터와 평가 데이터를 서로 다른 색의 선으로 표시하면 분할 구조를 확인할 수 있다.\n'
             + code('''
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 3))
plt.plot(train["date"], train["temp_mean"], lw=0.8, label="train (2021-2024)")
plt.plot(test["date"], test["temp_mean"], lw=0.8, label="test (2025)")
plt.ylabel("temperature (C)")
plt.legend()
plt.show()
''')
             + fig('ch09_colab_split_plot', '학습·평가 데이터 분할 그래프', 'Colab에서 출력한 학습 데이터(2021~2024년)와 평가 데이터(2025년)')
             + '\n파란 선의 4년으로 계수를 결정하고, 주황 선의 1년으로 오차를 측정한다. 평가 구간은 학습 구간 이후에 위치하므로 모델은 평가 기간의 정보를 학습에 사용하지 않는다.\n')

insert_after(f'{D9}/9-4.md', '세 기온 계수의 합(0.545 + 0.419 − 0.223 = 0.741)이 "오늘 기온 전체가 1℃ 높을 때의 증가량"에 가깝다.\n',
             '\n계수를 가로 막대그래프로 표시한다.\n'
             + code('''
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 3.5))
coef.sort_values().plot.barh()
plt.axvline(0, color="gray", lw=1)
plt.xlabel("coefficient")
plt.show()
''')
             + fig('ch09_colab_coef_plot', '선형회귀 계수 막대그래프', 'Colab에서 출력한 선형회귀 계수')
             + '\n`doy_cos`의 막대가 가장 길지만, 이 결과만으로 가장 중요한 특징이라고 판단할 수는 없다. 계수의 크기는 특징의 단위에 좌우되기 때문이다. `doy_cos`는 −1~1 범위의 값이고 기온 특징은 −20~40 범위의 값이므로, 계수 크기는 단위가 같은 기온 특징끼리만 비교한다.\n')

replace(f'{D9}/9-5.md', '![2025년 다음 날 평균기온의 실제값과 선형회귀 예측값](../assets/img/ch09_pred_vs_actual.png)\n',
        code('''
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 3.5))
plt.plot(result["date"], result["actual"], lw=1, label="actual")
plt.plot(result["date"], result["pred"], lw=1, label="pred")
plt.ylabel("next-day mean temperature (C)")
plt.legend()
plt.show()
''').lstrip('\n')
        + fig('ch09_colab_pred_plot', '2025년 다음 날 평균기온의 실제값과 선형회귀 예측값', 'Colab에서 출력한 2025년 다음 날 평균기온의 실제값과 예측값'))

insert_after(f'{D9}/9-5.md', '기온이 하루 만에 급변하는 날에는 예측값이 실제값보다 늦게 반응한다.\n',
             '\n실제값을 가로축, 예측값을 세로축으로 한 산점도에서는 오차의 크기를 대각선에서 떨어진 거리로 확인할 수 있다.\n'
             + code('''
plt.figure(figsize=(4.5, 4.5))
plt.scatter(result["actual"], result["pred"], s=8)
plt.plot([-15, 35], [-15, 35], color="gray", lw=1)   # 예측값 = 실제값인 대각선
plt.xlabel("actual (C)")
plt.ylabel("pred (C)")
plt.show()
''')
             + fig('ch09_colab_pred_scatter', '실제값과 예측값 산점도', 'Colab에서 출력한 실제값과 예측값의 산점도(회색 선: 예측값 = 실제값)')
             + '\n점이 대각선 근처에 모여 있으면 예측이 정확하다는 의미다. 대각선 아래의 점은 실제보다 낮게, 위의 점은 실제보다 높게 예측한 날이다. 대각선에서 크게 벗어난 소수의 점이 다음 항목에서 분석하는 오차 상위 날짜다.\n')

# ---------- 10장
add_output_figs(f'{D10}/10-1.md', [('ch10_colab_label', '강수일 레이블 분포 실행 화면', 'Colab에서 실행한 다음 날 강수일 레이블 분포')])
add_output_figs(f'{D10}/10-2.md', [('ch10_colab_rules', '결정트리 규칙 출력 실행 화면', 'Colab에서 출력한 깊이 3 결정트리의 분기 규칙')])
add_output_figs(f'{D10}/10-3.md', [('ch10_colab_metrics', '분류 성능 실행 화면', 'Colab에서 산출한 정확도·혼동행렬·재현율·정밀도')])
add_output_figs(f'{D10}/10-4.md', [
    ('ch10_colab_balanced', '가중치 적용 결정트리 실행 화면', 'Colab에서 산출한 가중치 적용 결정트리의 성능'),
    ('ch10_colab_depth', '트리 깊이별 정확도 실행 화면', 'Colab에서 실행한 트리 깊이별 정확도와 재현율'),
])

insert_after(f'{D10}/10-2.md', '## 규칙의 해석\n',
             '\n`plot_tree`는 같은 트리를 그림으로 표시한다. `filled=True`는 각 상자를 다수 범주의 색으로 칠한다.\n'
             + code('''
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(14, 6))
plot_tree(clf, feature_names=feats, class_names=["0", "1"], filled=True, impurity=False, fontsize=8)
plt.show()
''')
             + fig('ch10_colab_tree_plot', '깊이 3 결정트리 그림', 'Colab에서 출력한 깊이 3 결정트리')
             + '\nTREE_NOTE\n\n')

insert_after(f'{D10}/10-3.md', '나머지 77일은 비가 왔는데도 "비 안 옴"으로 예측한 미검출이다.\n',
             '\n`ConfusionMatrixDisplay`는 혼동행렬을 색으로 구분한 그림으로 표시한다.\n'
             + code('''
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(test["target_rain"], p, display_labels=["no rain", "rain"], cmap="Blues")
plt.show()
''')
             + fig('ch10_colab_cm_plot', '혼동행렬 그림', 'Colab에서 출력한 기본 결정트리의 혼동행렬')
             + '\n행이 실제값(True label), 열이 예측값(Predicted label)이며, 색이 진할수록 건수가 많다. 왼쪽 아래 칸의 77이 미검출, 오른쪽 위 칸의 30이 오경보다. 7.3절의 습도 경보 규칙에서 집계한 두 오류와 같은 구조다.\n')

insert_after(f'{D10}/10-4.md', '미검출과 오경보는 상충(trade-off) 관계이므로, 모델의 사용 목적에 따라 어느 쪽을 우선할지 결정한다.\n',
             code('''
ConfusionMatrixDisplay.from_predictions(test["target_rain"], pb, display_labels=["no rain", "rain"], cmap="Blues")
plt.show()
''')
             + fig('ch10_colab_cm_balanced', '가중치 적용 결정트리의 혼동행렬', 'Colab에서 출력한 가중치 적용 결정트리의 혼동행렬')
             + '\n10.3절의 기본 결정트리 혼동행렬과 비교하면 왼쪽 아래 칸(미검출)이 77에서 46으로 감소하고, 오른쪽 위 칸(오경보)이 30에서 72로 증가했다.\n')

insert_after(f'{D10}/10-4.md', '깊이가 증가할수록 학습 정확도와 평가 정확도의 차이가 확대되는지 확인하는 것이 과대적합 판정의 기본 절차다.\n',
             '\n깊이별 학습 정확도와 평가 정확도를 그래프로 비교한다. 깊이 제한 없음(`None`)은 그래프의 가로축에 표시할 수 없으므로 깊이 20까지 산출한다.\n'
             + code('''
depths = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]
tr_acc, te_acc = [], []
for d in depths:
    c = DecisionTreeClassifier(max_depth=d, random_state=0, class_weight="balanced")
    c.fit(train[feats], train["target_rain"])
    tr_acc.append(accuracy_score(train["target_rain"], c.predict(train[feats])))
    te_acc.append(accuracy_score(test["target_rain"], c.predict(test[feats])))

plt.figure(figsize=(7, 3.5))
plt.plot(depths, tr_acc, marker="o", label="train accuracy")
plt.plot(depths, te_acc, marker="o", label="test accuracy")
plt.axhline(0.703, color="gray", linestyle="--", label="baseline (always 0)")
plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.legend()
plt.show()
''')
             + fig('ch10_colab_depth_plot', '트리 깊이별 정확도 그래프', 'Colab에서 출력한 트리 깊이별 학습 정확도와 평가 정확도(회색 점선: 기준선)')
             + '\n깊이가 증가할수록 학습 정확도(파란 선)는 1.0에 접근하지만 평가 정확도(주황 선)는 0.65 부근에 머물고, 두 선의 간격이 확대된다. 깊이 제한이 없는 트리의 실제 깊이는 16이므로, 깊이 20의 결과는 `None`과 같다. 평가 정확도는 어느 깊이에서도 기준선(회색 점선)을 넘지 못한다.\n')
print('done')
