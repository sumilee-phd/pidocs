# 14장 FastAPI 수신 서버

<span class="chip">14주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span>

8장에서는 교수자가 준비한 수업 서버로 측정값을 전송했다. 이 장에서는 같은 역할을 하는 수신 서버를 직접 작성한다. 웹 API의 기본 구조를 이해하고, FastAPI로 측정값 수신 엔드포인트를 작성한 뒤, 7장의 판정 함수를 서버에 연결한다. 기기 없이 11/4 수업 기록을 서버에 다시 전송하는 가상 노드로 서버의 동작을 시험한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch14.ipynb){ .md-button .md-button--primary }

## 절 구성

- [14.1 웹 API의 구조](14-1.md)
- [14.2 FastAPI 엔드포인트](14-2.md)
- [14.3 판정 모듈 연결](14-3.md)
- [14.4 가상 노드로 서버 시험](14-4.md)

## 학습 목표

- 요청·응답·엔드포인트·HTTP 메서드·상태 코드의 의미를 설명한다.
- FastAPI와 pydantic으로 측정값 수신 엔드포인트와 자료 검증 모델을 작성한다.
- 판정 함수를 별도 모듈로 분리하고 서버 응답에 판정 결과를 포함한다.
- 기록 자료를 재생해 서버의 동작과 판정 결과를 검증한다.

## 준비물

- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)
- PC에서 서버를 실행하는 경우: 파이썬, `pip install fastapi uvicorn`

!!! abstract "참고 링크"
    - [FastAPI 공식 자습서](https://fastapi.tiangolo.com/tutorial/)
    - [FastAPI 테스트(TestClient)](https://fastapi.tiangolo.com/tutorial/testing/)
    - [pydantic 필드 제약](https://docs.pydantic.dev/latest/concepts/fields/)
