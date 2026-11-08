# -*- coding: utf-8 -*-
"""9·10장 본문 코드 블록을 순서대로 실행해 출력 원문을 기록한다(본문 실행 결과 상자의 근거)."""
import contextlib, io, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'data'))
import pandas as pd
pd.set_option('display.width', 100)
BLOCKS = {}
BLOCKS['9-2a'] = '''
import pandas as pd

df = pd.read_csv("seoul_weather_2021_2025.csv", parse_dates=["date"])
print(df.shape)
print(df.head(3))
'''
BLOCKS['9-2b'] = '''
df["target_temp"] = df["temp_mean"].shift(-1)
print(df[["date", "temp_mean", "target_temp"]].tail(3))
'''
BLOCKS['9-2c'] = '''
import numpy as np

day = df["date"].dt.day_of_year
df["doy_sin"] = np.sin(2 * np.pi * day / 365.25)
df["doy_cos"] = np.cos(2 * np.pi * day / 365.25)
print(df.loc[[0, 90, 181, 273], ["date", "doy_sin", "doy_cos"]].round({"doy_sin": 2, "doy_cos": 2}))
'''
BLOCKS['9-3'] = '''
data = df.dropna(subset=["target_temp"])
features = ["temp_mean", "temp_max", "temp_min", "humidity",
            "precip_mm", "wind_max", "sunshine_h", "doy_sin", "doy_cos"]

train = data[data["date"] < "2025-01-01"]
test = data[data["date"] >= "2025-01-01"]
print(len(train), len(test))
'''
BLOCKS['9-4a'] = '''
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(train[features], train["target_temp"])

coef = pd.Series(model.coef_, index=features).round(3)
print(coef)
print("절편:", round(model.intercept_, 3))
'''
BLOCKS['9-4b'] = '''
pred = model.predict(test[features])
result = pd.DataFrame({"date": test["date"], "actual": test["target_temp"], "pred": pred.round(1)})
print(result.head(5))
'''
BLOCKS['9-5a'] = '''
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(test["target_temp"], pred)
rmse = mean_squared_error(test["target_temp"], pred) ** 0.5
r2 = r2_score(test["target_temp"], pred)
print(f"MAE  {mae:.2f}")
print(f"RMSE {rmse:.2f}")
print(f"R2   {r2:.3f}")
'''
BLOCKS['9-5b'] = '''
base = test["temp_mean"]          # 오늘 평균기온을 그대로 내일 예측값으로 사용
base_mae = mean_absolute_error(test["target_temp"], base)
print(f"기준선 MAE {base_mae:.2f}")
'''
BLOCKS['9-5c'] = '''
result["error"] = (result["actual"] - result["pred"]).abs()
print(result.sort_values("error", ascending=False).head(3))
'''
BLOCKS['10-1a'] = '''
df["target_rain"] = (df["precip_mm"].shift(-1) >= 1.0).astype(int)
df["temp_range"] = df["temp_max"] - df["temp_min"]
data = df.iloc[:-1]                 # 마지막 날은 다음 날 자료가 없으므로 제외

feats = ["precip_mm", "humidity", "temp_range", "sunshine_h",
         "wind_max", "doy_sin", "doy_cos"]
train = data[data["date"] < "2025-01-01"]
test = data[data["date"] >= "2025-01-01"]
print(train["target_rain"].value_counts())
print(round(test["target_rain"].mean(), 3))
'''
BLOCKS['10-2a'] = '''
from sklearn.tree import DecisionTreeClassifier, export_text

clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(train[feats], train["target_rain"])
print(export_text(clf, feature_names=feats, decimals=1))
'''
BLOCKS['10-3a'] = '''
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score

p = clf.predict(test[feats])
print("정확도", round(accuracy_score(test["target_rain"], p), 3))
print("기준선", round((test["target_rain"] == 0).mean(), 3))
print(confusion_matrix(test["target_rain"], p))
print("재현율", round(recall_score(test["target_rain"], p), 3))
print("정밀도", round(precision_score(test["target_rain"], p), 3))
'''
BLOCKS['10-4a'] = '''
clf_b = DecisionTreeClassifier(max_depth=3, random_state=0, class_weight="balanced")
clf_b.fit(train[feats], train["target_rain"])
pb = clf_b.predict(test[feats])
print("정확도", round(accuracy_score(test["target_rain"], pb), 3))
print(confusion_matrix(test["target_rain"], pb))
print("재현율", round(recall_score(test["target_rain"], pb), 3))
print("정밀도", round(precision_score(test["target_rain"], pb), 3))
'''
BLOCKS['10-4b'] = '''
for d in [1, 2, 3, 4, 6, 10, None]:
    c = DecisionTreeClassifier(max_depth=d, random_state=0, class_weight="balanced")
    c.fit(train[feats], train["target_rain"])
    tr = accuracy_score(train["target_rain"], c.predict(train[feats]))
    te = accuracy_score(test["target_rain"], c.predict(test[feats]))
    rc = recall_score(test["target_rain"], c.predict(test[feats]))
    print(f"깊이 {str(d):>4}  학습 정확도 {tr:.3f}  평가 정확도 {te:.3f}  평가 재현율 {rc:.3f}")
'''
ns = {}
for k, code in BLOCKS.items():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, ns)
    print(f'##### {k}'); print(buf.getvalue().rstrip())
