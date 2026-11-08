import cyberpi
import json
import math
import urllib.request
from datetime import date

PORT = "s1"
URL = ("https://api.open-meteo.com/v1/forecast"
       "?latitude=37.5665&longitude=126.978"
       "&daily=precipitation_sum,precipitation_probability_max"
       "&timezone=Asia%2FSeoul&forecast_days=2")


def my_model(precip_mm, doy_sin, doy_cos):
    """10.4절 가중치 적용 결정트리(깊이 3)의 조건문 변환. 1 = 다음 날 강수"""
    if precip_mm <= 2.35:
        if doy_cos <= -0.1425 and doy_sin <= 0.4189:
            return 1
        return 0
    if doy_cos <= 0.1912:
        return 1
    if precip_mm <= 11.25:
        return 0
    return 1


# 1) 예보 수신
with urllib.request.urlopen(URL, timeout=10) as r:
    daily = json.loads(r.read().decode("utf-8"))["daily"]
today_precip = daily["precipitation_sum"][0]                 # 오늘 예상 강수량(mm)
tomorrow_prob = daily["precipitation_probability_max"][1]    # 내일 최대 강수확률(%)

# 2) 내 모델 판정
d = date.today().timetuple().tm_yday
doy_sin = math.sin(2 * math.pi * d / 365.25)
doy_cos = math.cos(2 * math.pi * d / 365.25)
mine = my_model(today_precip, doy_sin, doy_cos)

# 3) LED 표시: 1~6번 = 예보 강수확률 막대, 7~12번 = 내 모델 판정
n = round(tomorrow_prob / 100 * 6)
left = ["b"] * n + ["k"] * (6 - n)
right = ["b" if mine == 1 else "y"] * 6
cyberpi.pocket.led_set_bri(30, PORT)
cyberpi.pocket.led_show(" ".join(left + right), PORT)

cyberpi.display.clear()
cyberpi.console.println("forecast {}%".format(tomorrow_prob))
cyberpi.console.println("my model: {}".format("RAIN" if mine == 1 else "DRY"))
