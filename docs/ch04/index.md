# 4장 사이버파이 첫 실습

<span class="chip">4주차</span> <span class="chip off">오프라인</span> <span class="chip">사이버파이·USB 케이블·mBlock</span>

첫 등교일에 사이버파이를 처음 다룬다. 내장 센서와 출력 장치의 위치를 확인하고, mBlock을 설치해 기기를 연결한다. 1장에서 블록으로 작성한 반복 구조를 기기 블록으로 다시 작성하고, 같은 프로그램이 파이썬 코드로 어떻게 변환되는지 대조한다. 마지막으로 센서 3종의 측정값을 CSV 파일로 저장한다. 이 파일은 5~7주차 온라인 수업의 분석 자료로 사용한다.

## 절 구성

- [4.1 사이버파이 구성과 사양](4-1.md)
- [4.2 mBlock 설치와 펌웨어 관리](4-2.md)
- [4.3 Live 모드와 Upload 모드](4-3.md)
- [4.4 블록 코드와 파이썬 코드 대조](4-4.md)
- [4.5 화면·LED·버튼 제어](4-5.md)
- [4.6 센서값 측정과 CSV 저장](4-6.md)
- [4.7 LED 스트립 점등과 소등](4-7.md)

## 학습 목표

- 사이버파이의 내장 센서·출력 장치·입력 장치의 위치와 용도를 설명한다.
- mBlock을 설치하고 사이버파이를 연결한다.
- Live 모드와 Upload 모드의 차이를 이해하고 용도에 맞게 선택한다.
- 블록 프로그램과 변환된 파이썬 코드를 대조해 `cyberpi` 함수 이름을 익힌다.
- 센서 측정값을 CSV 파일로 저장한다.

## 준비물

- 사이버파이, USB 케이블(PC 연결용)
- mBlock PC 버전이 설치된 노트북
- 4.7절: 포켓쉴드, LED 스트립

## 장 종료 시 결과물

- 4.6절의 센서 측정 CSV 파일 1개 이상(5장 분석 자료)

!!! abstract "참고 링크"
    - [mBlock 내려받기](https://mblock.cc/pages/downloads)
    - [mBlock 웹 버전](https://ide.mblock.cc/)
    - [Makeblock mCode CyberPi API](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api)
