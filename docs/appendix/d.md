# D. 데이터셋 출처와 이용 조건

## 서울 일별 날씨 자료 2021~2025

| 항목 | 내용 |
|---|---|
| 파일 | [seoul_weather_2021_2025.csv](../data/seoul_weather_2021_2025.csv) (1,826행, 8열) |
| 사용 장 | 3.3절, 5~6장, 9장, 10장, 12.1절 |
| 원자료 | Open-Meteo Historical Weather API (<https://open-meteo.com/>) |
| 지점 | 위도 37.5665, 경도 126.978(서울 중구) 요청, 응답 격자 위도 37.57·경도 126.96 |
| 기간 | 2021-01-01 ~ 2025-12-31, 일 단위, 시간대 Asia/Seoul |
| 자료 성격 | 재분석 자료(관측값을 수치 모델로 보정해 격자별로 산출한 값). 기상청 관측소 실측값과 다를 수 있다. |
| 이용 조건 | CC BY 4.0. 출처를 「Open-Meteo.com」으로 표기한다. |
| 생성 방법 | 저자가 API 응답을 CSV로 변환(일조시간은 초 단위를 시간 단위로 환산). 생성 스크립트 `scripts/make_dataset.py` |

| 열 | 원자료 변수 | 단위 |
|---|---|---|
| `date` | `time` | |
| `temp_mean` | `temperature_2m_mean` | ℃ |
| `temp_max` | `temperature_2m_max` | ℃ |
| `temp_min` | `temperature_2m_min` | ℃ |
| `precip_mm` | `precipitation_sum` | mm |
| `humidity` | `relative_humidity_2m_mean` | % |
| `wind_max` | `wind_speed_10m_max` | km/h |
| `sunshine_h` | `sunshine_duration` ÷ 3600 | 시간 |

## 기상청 관측 자료로 실습하는 방법

기상청 관측소 실측값으로 같은 실습을 진행하려면 기상청 기상자료개방포털(<https://data.kma.go.kr>)의 종관기상관측(ASOS) 일자료에서 서울 지점(108)을 선택해 CSV로 내려받는다. 열 이름과 단위가 다르므로 5장의 방법으로 열 이름을 이 책의 형식으로 변경한 뒤 사용한다. 내려받기 절차와 이용 조건은 포털의 안내를 따른다.

## 예보 자료(12.1절)

| 항목 | 내용 |
|---|---|
| 원자료 | Open-Meteo Weather Forecast API |
| 사용 변수 | `precipitation_sum`(일강수량 예상값), `precipitation_probability_max`(일 최대 강수확률) |
| 이용 조건 | CC BY 4.0, 비상업적 이용은 인증키 없이 사용 가능(Open-Meteo 이용 조건 기준) |
