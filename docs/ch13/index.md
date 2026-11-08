# 13장 생성형 AI API

<span class="chip">13주차</span> <span class="chip on">온라인</span> <span class="chip">기기 불필요</span> <span class="chip">Gemini API 키 필요</span>

측정 시스템의 마지막 단계는 결과를 사람이 읽을 수 있는 보고 문장으로 정리하는 일이다. 이 장에서는 파이썬에서 생성형 AI인 Gemini API를 호출하고, 목적·형식·제약을 명시한 프롬프트를 작성한다. 수치 계산은 코드로 하고 문장 작성만 AI에 맡기는 구조로 오류를 줄이며, 생성된 문장의 수치가 원자료와 일치하는지 코드로 자동 점검한다.

[Colab에서 열기](https://colab.research.google.com/github/sumilee-phd/pidocs/blob/main/notebooks/ch13.ipynb){ .md-button .md-button--primary }

## 절 구성

- [13.1 Gemini API 호출](13-1.md)
- [13.2 프롬프트 설계](13-2.md)
- [13.3 수치 계산과 문장 생성의 분리](13-3.md)
- [13.4 출력 검증](13-4.md)

## 학습 목표

- API 키를 발급·보관하고 파이썬에서 Gemini API를 호출한다.
- 역할·입력·출력 형식·제약을 명시한 프롬프트를 작성한다.
- 측정 요약 통계는 코드로 산출하고, 요약값만 AI에 입력하는 구조를 구성한다.
- 생성된 문장의 수치를 정규식으로 추출해 원자료와 대조한다.

## 준비물

- Google 계정과 Gemini API 키(13.1절)
- [11/4 수업 Wi-Fi 신호 세기 기록(CSV)](../data/class_rssi_20261104.csv)

!!! warning "실행 결과 기입 상태"
    이 장의 Gemini 호출 결과는 수업용 API 키를 확인한 뒤 실제 응답으로 기입한다. 키 없이 실행되는 부분(요약 통계, 프롬프트 구성, 출력 검증)의 실행 결과는 실제 출력이다. Colab 노트북은 키가 없어도 오류 없이 끝까지 실행되도록 작성했다.

!!! abstract "참고 링크"
    - [Gemini API 빠른 시작](https://ai.google.dev/gemini-api/docs/quickstart)
    - [Google AI Studio API 키](https://aistudio.google.com/apikey)
    - [Gemini API 텍스트 생성](https://ai.google.dev/gemini-api/docs/text-generation)
    - [Python 정규식(re)](https://docs.python.org/3/library/re.html)
