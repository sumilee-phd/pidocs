# -*- coding: utf-8 -*-
"""11·12장 제스처 예시 자료 생성기 (실측 자료 수집 전 임시 자료, 2026-11-09).

8.5절 기록 규칙(동작 4종, 1인 30회, 2초 × 0.05초 간격 = 40행, 열 rep·t·ax·ay·az)과 같은 형식으로
가상의 수강생 4명(S01~S04)의 가속도 기록을 생성한다. 8.5절 파일 16개를 합친 결과와 같도록
student·gesture 열을 추가한 하나의 파일로 저장한다.

- 단위는 m/s²로 가정하고, 화면이 위를 향하면 az ≈ 9.8(중력)로 둔다.
- 학생마다 동작의 세기·빠르기·손 기울기를 다르게 한다.
- 학생 S04는 흔들기를 좌우가 아니라 앞뒤(y축)로 하고, 기기를 약간 세워 쥐는 습관을 갖도록 생성한다.
  12.3절 교차 평가에서 다른 사람의 동작으로 학습한 모델의 정확도가 낮아지는 사례를 보이기 위한 설정이다.

    python scripts/make_gesture_example.py
"""
import os

import numpy as np
import pandas as pd

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
OUT = os.path.join(ROOT, 'docs', 'data', 'gesture_example.csv')
G = 9.8
N, DT = 40, 0.05
t = np.arange(N) * DT

STUDENTS = {   # 세기, 빠르기, 손 기울기(rad, x축 기준), 흔들기 축
    'S01': dict(amp=1.00, speed=1.00, tilt0=0.05, shake_axis='x'),
    'S02': dict(amp=1.25, speed=1.15, tilt0=-0.08, shake_axis='x'),
    'S03': dict(amp=0.80, speed=0.85, tilt0=0.12, shake_axis='x'),
    'S04': dict(amp=1.05, speed=1.05, tilt0=0.45, shake_axis='y'),
}


def gravity(theta):
    """x축 기준으로 theta만큼 앞으로 기울였을 때의 중력 성분(ay, az)."""
    return G * np.sin(theta), G * np.cos(theta)


def one_rep(rng, gesture, p):
    amp, speed, tilt0 = p['amp'] * rng.uniform(0.55, 1.35), p['speed'] * rng.uniform(0.8, 1.2), p['tilt0']
    ax = np.zeros(N)
    theta = np.full(N, tilt0 + rng.normal(0, 0.03))
    if gesture == 'still':
        noise = rng.uniform(0.05, 0.45)          # 손 떨림 정도가 회차마다 다름
    elif gesture == 'shake':
        f = 2.4 * speed
        wave = 11.0 * amp * np.sin(2 * np.pi * f * t + rng.uniform(0, 2 * np.pi))
        noise = 1.0
        if p['shake_axis'] == 'x':
            ax = wave
        else:
            theta = theta + 0.0
    elif gesture == 'tilt':
        dur = 1.8 / speed
        phase = np.clip(t / dur, 0, 1)
        theta = theta + np.deg2rad(45 * amp) * np.sin(np.pi * phase)
        noise = rng.uniform(0.15, 0.5)
    elif gesture == 'circle':
        w = 2 * np.pi / (1.6 / speed)
        a = 2.2 * amp
        ph = rng.uniform(0, 2 * np.pi)
        ax = a * np.cos(w * t + ph)
        noise = 0.5
    else:
        raise ValueError(gesture)
    ay, az = gravity(theta)
    if gesture == 'circle':
        az = az + 2.2 * amp * np.sin(2 * np.pi / (1.6 / speed) * t + ph)
    if gesture == 'shake' and p['shake_axis'] == 'y':
        ay = ay + 11.0 * amp * np.sin(2 * np.pi * 2.4 * speed * t + rng.uniform(0, 2 * np.pi))
    ax = ax + rng.normal(0, noise, N)
    ay = ay + rng.normal(0, noise, N)
    az = az + rng.normal(0, noise, N)
    return np.round(ax, 2), np.round(ay, 2), np.round(az, 2)


def main():
    rng = np.random.default_rng(20261109)
    rows = []
    for sid, p in STUDENTS.items():
        for g in ['still', 'shake', 'tilt', 'circle']:
            for rep in range(1, 31):
                ax, ay, az = one_rep(rng, g, p)
                for i in range(N):
                    rows.append((sid, g, rep, round(t[i], 2), ax[i], ay[i], az[i]))
    df = pd.DataFrame(rows, columns=['student', 'gesture', 'rep', 't', 'ax', 'ay', 'az'])
    df.to_csv(OUT, index=False)
    print(OUT, df.shape)


if __name__ == '__main__':
    main()
