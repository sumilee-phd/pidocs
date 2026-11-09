# 8장 무선 전송과 실기 과제

<span class="chip">8주차</span> <span class="chip off">오프라인</span> <span class="chip">사이버파이·포켓쉴드·교내 Wi-Fi</span>

두 번째 등교일에는 사이버파이를 USB에서 분리해 독립적으로 동작시킨다. Upload 모드 프로그램의 구조를 익히고, 교내 Wi-Fi에 접속해 측정값을 수업 서버로 전송한다. 10대가 동시에 전송한 결과를 수업 서버의 실시간 화면에서 확인한 뒤, 측정·판정·표시를 결합한 실기 과제를 수행한다. 마지막으로 11장 동작 분류 실습에 사용할 제스처 자료를 수집한다.

## 절 구성

- [8.1 Upload 모드 프로그램 구조](8-1.md)
- [8.2 Wi-Fi 접속과 측정값 전송](8-2.md)
- [8.3 수업 서버 실시간 화면](8-3.md)
- [8.4 실기 과제: 수집·판정·표시 프로그램](8-4.md)
- [8.5 제스처 데이터 수집](8-5.md)

## 학습 목표

- 초기화·반복·이벤트로 구성된 Upload 모드 프로그램을 작성한다.
- 교내 Wi-Fi에 접속하고 측정값을 JSON 형식으로 수업 서버에 전송한다.
- 수업 서버의 실시간 화면에서 지점별 중앙값과 노드별 진행 현황을 해석한다.
- 측정·판정·표시 프로그램을 제한 시간 안에 완성한다.
- 동작 4종의 가속도 자료를 정해진 규칙에 따라 수집한다.

## 준비물

- 사이버파이, 포켓쉴드(배터리 충전), USB 케이블
- 교내 Wi-Fi 이름(SSID)·비밀번호, 수업 서버 주소(수업 당일 교수자 안내)

## 장 종료 시 결과물

- 8.4절 실기 과제 프로그램 파일
- 8.5절 제스처 CSV 파일(동작 4종)

!!! abstract "참고 링크"
    - [MicroPython network 모듈(WLAN)](https://docs.micropython.org/en/latest/library/network.WLAN.html)
    - [MicroPython socket 모듈](https://docs.micropython.org/en/latest/library/socket.html)
    - [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
