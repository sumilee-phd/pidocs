# -*- coding: utf-8 -*-
"""12.1절 조건문 모델이 10.4절 가중치 결정트리(깊이 3)와 같은 판정을 하는지 대조하고, 예보 수신 코드를 가짜 cyberpi로 시험한다."""
import json, math, os, sys, types, urllib.request
from datetime import date
import numpy as np, pandas as pd
from sklearn.tree import DecisionTreeClassifier
HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, '..', 'docs', 'data', 'seoul_weather_2021_2025.csv'), parse_dates=['date'])
day = df['date'].dt.day_of_year
df['doy_sin'] = np.sin(2*np.pi*day/365.25); df['doy_cos'] = np.cos(2*np.pi*day/365.25)
df['target_rain'] = (df['precip_mm'].shift(-1) >= 1.0).astype(int); df['temp_range'] = df['temp_max']-df['temp_min']
data = df.iloc[:-1]
feats = ['precip_mm','humidity','temp_range','sunshine_h','wind_max','doy_sin','doy_cos']
train = data[data['date'] < '2025-01-01']; test = data[data['date'] >= '2025-01-01']
clf_b = DecisionTreeClassifier(max_depth=3, random_state=0, class_weight='balanced').fit(train[feats], train['target_rain'])
t = clf_b.tree_
for i in range(t.node_count):
    if t.feature[i] >= 0:
        print(i, feats[t.feature[i]], repr(round(float(t.threshold[i]), 4)))

def my_model(precip_mm, doy_sin, doy_cos):
    if precip_mm <= 2.35:
        if doy_cos <= -0.1425 and doy_sin <= 0.4189:
            return 1
        return 0
    if doy_cos <= 0.1912:
        return 1
    if precip_mm <= 11.25:
        return 0
    return 1

mine = np.array([my_model(r.precip_mm, r.doy_sin, r.doy_cos) for r in data.itertuples()])
print('agreement all 2021-2025:', (mine == clf_b.predict(data[feats])).mean())

# 예보 수신 + 표시 코드 시험(가짜 cyberpi)
calls = []
fake = types.SimpleNamespace(
    pocket=types.SimpleNamespace(led_set_bri=lambda *a: calls.append(('led_set_bri',)+a), led_show=lambda *a: calls.append(('led_show',)+a)),
    display=types.SimpleNamespace(clear=lambda: calls.append(('clear',))), console=types.SimpleNamespace(println=lambda *a: calls.append(('println',)+a)))
sys.modules['cyberpi'] = fake
src = open(os.path.join(HERE, 'ch12_weather_signal.py'), encoding='utf-8').read()
exec(compile(src, 'ch12_weather_signal.py', 'exec'), {'__name__': '__main__'})
for c in calls: print(c)
