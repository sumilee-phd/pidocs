# -*- coding: utf-8 -*-
"""9장(회귀)·10장(분류) 본문 코드 실행 검증 — 출력 수치와 그림을 본문에 그대로 옮긴다."""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', 'docs', 'assets', 'img')
df = pd.read_csv(os.path.join(HERE, '..', 'docs', 'data', 'seoul_weather_2021_2025.csv'), parse_dates=['date'])

# ── 9장 ──
print('== 9.2 shape', df.shape)
df['doy_sin'] = np.sin(2 * np.pi * df['date'].dt.day_of_year / 365.25)
df['doy_cos'] = np.cos(2 * np.pi * df['date'].dt.day_of_year / 365.25)
df['target_temp'] = df['temp_mean'].shift(-1)
data = df.dropna(subset=['target_temp']).copy()
features = ['temp_mean', 'temp_max', 'temp_min', 'humidity', 'precip_mm', 'wind_max', 'sunshine_h', 'doy_sin', 'doy_cos']
train = data[data['date'] < '2025-01-01']
test = data[data['date'] >= '2025-01-01']
print('== 9.3 train', len(train), 'test', len(test))
base = test['temp_mean']
print('== 9.5 baseline MAE', round(mean_absolute_error(test['target_temp'], base), 2))
model = LinearRegression().fit(train[features], train['target_temp'])
pred = model.predict(test[features])
mae = mean_absolute_error(test['target_temp'], pred)
rmse = mean_squared_error(test['target_temp'], pred) ** 0.5
print('== 9.5 linear MAE', round(mae, 2), 'RMSE', round(rmse, 2), 'R2', round(r2_score(test['target_temp'], pred), 3))
print('== 9.4 coef'); print(pd.Series(model.coef_, index=features).round(3).to_string()); print('intercept', round(model.intercept_, 3))
err = (test['target_temp'] - pred).abs()
print('== 9.5 max error', round(err.max(), 1), 'on', test.loc[err.idxmax(), 'date'].date())
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.plot(test['date'], test['target_temp'], label='actual (next day)', lw=1.2)
ax.plot(test['date'], pred, label='predicted', lw=1.0)
ax.set_ylabel('mean temperature (C)'); ax.legend(); ax.grid(alpha=0.3)
ax.set_title('Seoul 2025: next-day mean temperature, linear regression')
fig.tight_layout(); fig.savefig(os.path.join(IMG, 'ch09_pred_vs_actual.png'), dpi=130)

# ── 10장 ──
df['target_rain'] = (df['precip_mm'].shift(-1) >= 1.0).astype('float')
df.loc[df.index[-1], 'target_rain'] = np.nan
df['temp_range'] = df['temp_max'] - df['temp_min']
data = df.dropna(subset=['target_rain']).copy()
data['target_rain'] = data['target_rain'].astype(int)
feats = ['precip_mm', 'humidity', 'temp_range', 'sunshine_h', 'wind_max', 'doy_sin', 'doy_cos']
train = data[data['date'] < '2025-01-01']
test = data[data['date'] >= '2025-01-01']
print('== 10.1 rain share train', round(train['target_rain'].mean(), 3), 'test', round(test['target_rain'].mean(), 3))
print('== 10.3 baseline(always 0) acc', round((test['target_rain'] == 0).mean(), 3))
clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(train[feats], train['target_rain'])
p = clf.predict(test[feats])
print('== 10.3 tree d3 acc', round(accuracy_score(test['target_rain'], p), 3), 'recall', round(recall_score(test['target_rain'], p), 3), 'precision', round(precision_score(test['target_rain'], p), 3))
print('cm', confusion_matrix(test['target_rain'], p).tolist())
print(export_text(clf, feature_names=feats, decimals=1))
clf_b = DecisionTreeClassifier(max_depth=3, random_state=0, class_weight='balanced').fit(train[feats], train['target_rain'])
pb = clf_b.predict(test[feats])
print('== 10.4 balanced acc', round(accuracy_score(test['target_rain'], pb), 3), 'recall', round(recall_score(test['target_rain'], pb), 3), 'precision', round(precision_score(test['target_rain'], pb), 3))
print('cm', confusion_matrix(test['target_rain'], pb).tolist())
print(export_text(clf_b, feature_names=feats, decimals=1))
print('== 10.4 depth sweep (train acc / test acc / test recall)')
for d in (1, 2, 3, 4, 6, 10, None):
    c = DecisionTreeClassifier(max_depth=d, random_state=0, class_weight='balanced').fit(train[feats], train['target_rain'])
    print(d, round(accuracy_score(train['target_rain'], c.predict(train[feats])), 3), round(accuracy_score(test['target_rain'], c.predict(test[feats])), 3), round(recall_score(test['target_rain'], c.predict(test[feats])), 3))
