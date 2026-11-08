# -*- coding: utf-8 -*-
"""서울 일별 날씨 자료(2021~2025) 생성 — Open-Meteo Historical Weather API(재분석 자료, CC BY 4.0).

출력: docs/data/seoul_weather_2021_2025.csv
열: date, temp_mean, temp_max, temp_min, precip_mm, humidity, wind_max, sunshine_h
"""
import csv
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'docs', 'data', 'seoul_weather_2021_2025.csv')
URL = ('https://archive-api.open-meteo.com/v1/archive?latitude=37.5665&longitude=126.978'
       '&start_date=2021-01-01&end_date=2025-12-31'
       '&daily=temperature_2m_mean,temperature_2m_max,temperature_2m_min,precipitation_sum,'
       'relative_humidity_2m_mean,wind_speed_10m_max,sunshine_duration&timezone=Asia%2FSeoul')


def main(src=None):
    if src:
        data = json.load(open(src, encoding='utf-8'))
    else:
        with urllib.request.urlopen(URL, timeout=60) as r:
            data = json.load(r)
    d = data['daily']
    rows = zip(d['time'], d['temperature_2m_mean'], d['temperature_2m_max'], d['temperature_2m_min'],
               d['precipitation_sum'], d['relative_humidity_2m_mean'], d['wind_speed_10m_max'],
               d['sunshine_duration'])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    n = 0
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['date', 'temp_mean', 'temp_max', 'temp_min', 'precip_mm', 'humidity', 'wind_max', 'sunshine_h'])
        for t, tm, tx, tn, p, h, wd, s in rows:
            w.writerow([t, tm, tx, tn, p, h, wd, '' if s is None else round(s / 3600, 1)])
            n += 1
    print('rows', n, '->', os.path.normpath(OUT))


if __name__ == '__main__':
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else None)
