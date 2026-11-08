# E. 용어집

본문에서 정의한 주요 용어를 한글 가나다순, 숫자, 영문 알파벳순으로 정리한다. 대괄호의 번호는 용어를 정의하거나 주로 다루는 절이다.

## ㄱ

**가상 노드** 실제 기기 대신 기록 자료를 서버에 전송해 서버의 동작을 시험하는 프로그램. <span class="gref">[14.4절]</span>

**결정트리**(decision tree) 특징 값이 기준보다 작거나 같은지를 묻는 분기를 반복해 자료를 분할하고, 마지막 분할 영역마다 하나의 범주를 배정하는 모델. <span class="gref">[10.2·11.3절]</span>

**결측치**(missing value) 자료에서 값이 없는 칸. pandas에서는 `NaN`으로 표시한다. <span class="gref">[5.2절]</span>

**경계값 시험** 판정 구간의 경계, 범위의 양 끝, 범위 밖의 값을 입력해 판정 함수의 정확성을 확인하는 시험. <span class="gref">[2.4절]</span>

**과대적합**(overfitting) 학습 자료의 우연한 변동까지 학습해 학습 정확도는 높지만 평가 정확도는 낮은 상태. <span class="gref">[9.1·10.4절]</span>

**교차 평가** 일부 자료를 평가용으로 분리하고 나머지 자료로 학습하는 과정을 반복해, 처음 보는 자료에서의 성능을 확인하는 방법. <span class="gref">[12.3절]</span>

**교차표**(cross table) 두 열의 값 조합별 건수를 집계한 표. `pd.crosstab`으로 산출한다. <span class="gref">[7.1절]</span>

## ㄷ

**대체 보고** 생성형 AI 호출이나 출력 검증이 실패했을 때 요약 표로 결과를 전달하는 방법. <span class="gref">[15.1·15.3절]</span>

**데이터그램** UDP로 전송하는 데이터 묶음. <span class="gref">[8.2·15.1절]</span>

**데코레이터**(decorator) 함수 정의 바로 위에 `@`로 시작하는 줄. `@event.start`처럼 함수를 특정 사건에 등록한다. <span class="gref">[4.4절]</span>

**딕셔너리**(dictionary) 이름표(키)로 값을 찾는 자료구조. 중괄호 안에 `키: 값` 쌍을 나열한다. <span class="gref">[3.1절]</span>

## ㄹ

**레이블**(label) 지도학습에서 예측 대상인 정답값. <span class="gref">[9.1절]</span>

**리스트**(list) 순서가 있는 값의 묶음. 대괄호 안에 값을 쉼표로 구분해 나열한다. <span class="gref">[3.1절]</span>

## ㅁ

**매개변수**(parameter) 함수 정의의 괄호 안에 쓰는 이름. 함수를 호출할 때 전달한 값을 받는다. <span class="gref">[2.3절]</span>

**머신러닝**(machine learning) 명시적인 규칙을 작성하지 않고 자료에서 입력과 출력의 관계를 학습해, 새로운 입력의 출력을 예측하는 기술. <span class="gref">[9.1절]</span>

**미검출**(miss) 사건이 발생했는데 경보를 발생시키지 않는 오류. 혼동행렬의 거짓음성(FN)에 해당한다. <span class="gref">[7.3·10.3절]</span>

## ㅂ

**반복문** 같은 코드를 여러 번 실행하는 문장. `for`는 목록의 값을 하나씩 꺼내 반복하고, `while`은 조건이 참인 동안 반복한다. <span class="gref">[2.2절]</span>

**변수**(variable) 값에 이름을 붙여 저장하는 공간. <span class="gref">[1.4절]</span>

**분위수**(quantile) 크기 순으로 정렬한 자료에서 지정한 비율 위치에 있는 값. <span class="gref">[7.1절]</span>

## ㅅ

**사분위수 범위**(IQR, Interquartile Range) 3사분위수(Q3)와 1사분위수(Q1)의 차이. 1.5×IQR 규칙으로 이상치 후보를 판정한다. <span class="gref">[5.2절]</span>

**상충**(trade-off) 한쪽 오류를 줄이면 다른 쪽 오류가 증가하는 관계. <span class="gref">[7.3절]</span>

**상태 코드** 서버가 응답에 처리 결과를 표시하는 세 자리 숫자. 200은 정상 처리, 422는 요청 자료의 형식 오류를 의미한다. <span class="gref">[14.1절]</span>

**생성형 AI** 입력 문장에 따라 새로운 문장을 생성하는 AI 모델. 다음에 올 토큰을 확률에 따라 선택하므로 같은 입력에도 출력이 달라질 수 있다. <span class="gref">[1.5·13.1절]</span>

**스레드**(thread) 한 프로그램 안에서 동시에 실행되는 별도 실행 흐름. <span class="gref">[15.1절]</span>

## ㅇ

**엔드포인트**(endpoint) 요청을 받는 주소의 경로. <span class="gref">[14.1절]</span>

**예외**(exception) 프로그램 실행 중 발생하는 오류 상황. <span class="gref">[15.2절]</span>

**예외 처리** `try` 블록에서 예외가 발생하면 프로그램을 정지하지 않고 `except` 블록으로 이동해 실행을 계속하는 문법. <span class="gref">[8.1·15.2절]</span>

**오경보**(false alarm) 사건이 발생하지 않았는데 경보를 발생시키는 오류. 혼동행렬의 거짓양성(FP)에 해당한다. <span class="gref">[7.3·10.3절]</span>

**요청**(request) 클라이언트가 서버에 보내는 메시지. <span class="gref">[14.1절]</span>

**응답**(response) 서버가 요청을 처리하고 돌려보내는 메시지. <span class="gref">[14.1절]</span>

**이동 간격** 구간 특징을 계산하는 창을 다음 위치로 옮기는 행 수. 이 책에서는 창 크기의 절반인 10행을 사용한다. <span class="gref">[11.1절]</span>

**이벤트 방식** 단추 누름처럼 특정 입력이 발생했을 때 함수를 실행하는 기기 프로그램 구조. <span class="gref">[8.1절]</span>

**이상치**(outlier) 다른 값들과 크게 떨어진 값. <span class="gref">[5.2절]</span>

**임계값**(threshold) 측정값을 단계로 판정하는 기준값. <span class="gref">[7.1절]</span>

## ㅈ

**자료형**(data type) 값의 종류. 파이썬은 저장한 값에 따라 정수(`int`)·실수(`float`)·문자열(`str`) 등의 자료형을 자동으로 결정한다. <span class="gref">[1.4절]</span>

**재분석 자료** 관측값을 수치 모델로 보정해 격자별로 산출한 자료. 이 책의 서울 날씨 자료가 해당한다(부록 D). <span class="gref">[3.3절]</span>

**재시도** 통신 실패 시 같은 요청을 다시 보내는 처리. 횟수를 제한하고 시도 사이에 대기 시간을 둔다. <span class="gref">[8.2·15.2절]</span>

**재현율**(recall) 실제 양성 중 양성으로 예측한 비율. TP ÷ (TP + FN). <span class="gref">[10.3절]</span>

**정규식**(regular expression) 문자열에서 특정 형태의 부분을 찾는 패턴 표기법. <span class="gref">[13.4절]</span>

**정밀도**(precision) 양성으로 예측한 것 중 실제 양성의 비율. TP ÷ (TP + FP). <span class="gref">[10.3절]</span>

**정확도**(accuracy) 전체 예측 중 맞힌 예측의 비율. <span class="gref">[10.3절]</span>

**조건문** 조건식의 참·거짓에 따라 실행할 코드를 선택하는 문장(`if`·`elif`·`else`). <span class="gref">[2.1절]</span>

**중앙값** 크기 순으로 정렬한 자료의 가운데 값. 평균보다 이상치의 영향을 적게 받는다. <span class="gref">[6.2절]</span>

**지도학습**(supervised learning) 입력과 정답이 짝을 이룬 자료로 학습하는 방식. <span class="gref">[9.1절]</span>

## ㅊ

**창 크기** 구간 특징을 계산하는 연속 측정값의 행 수. 이 책에서는 20행(1초)을 사용한다. <span class="gref">[11.1절]</span>

## ㅌ

**토큰** 생성형 AI 모델이 문장을 처리하는 단위. API 사용량 계산의 기준이다. <span class="gref">[13.1절]</span>

**특징**(feature) 모델에 입력하는 변수. <span class="gref">[9.1절]</span>

## ㅍ

**펌웨어**(firmware) 사이버파이 내부에서 동작하는 기본 프로그램. <span class="gref">[4.2절]</span>

**포켓쉴드**(Pocket Shield) 사이버파이 아래에 결합하는 확장 보드. 배터리 전원과 LED 스트립 연결 포트(S1·S2)를 제공한다. <span class="gref">[4.7절]</span>

**표준화** 각 값에서 평균을 빼고 표준편차로 나누어, 단위가 다른 값을 같은 척도로 변환하는 처리. <span class="gref">[7.2·11.2절]</span>

**퓨샷 프롬프트**(few-shot) 원하는 출력의 예시를 하나 이상 제시하는 프롬프트. <span class="gref">[13.2절]</span>

**프롬프트**(prompt) 생성형 AI 모델에 보내는 입력 문장. <span class="gref">[13.2절]</span>

**피지컬컴퓨팅**(physical computing) 센서로 실제 환경을 측정하고, 측정값을 프로그램으로 처리한 뒤, 결과를 빛·소리·움직임 같은 물리적 출력으로 변환하는 컴퓨팅. <span class="gref">[1.1절]</span>

## ㅎ

**함수**(function) 자주 사용하는 코드에 이름을 붙여 묶은 것. <span class="gref">[2.3절]</span>

**형 변환**(type conversion) 값의 자료형을 다른 자료형으로 변경하는 처리. 예: `int("63")`. <span class="gref">[1.4절]</span>

**혼동행렬**(confusion matrix) 실제 범주와 예측 범주의 조합별 건수를 표로 정리한 것. <span class="gref">[10.3절]</span>

**회고**(retrospective) 프로젝트가 끝난 뒤 진행 과정을 되짚어 유지할 점, 문제점, 개선 사항을 정리하는 활동. <span class="gref">[16.3절]</span>

## A

**API**(Application Programming Interface) 프로그램이 다른 프로그램의 기능을 사용할 수 있도록 정한 호출 규칙. <span class="gref">[13.1·14.1절]</span>

**API 키** API를 호출하는 사용자를 식별하는 문자열. 코드에 기입하지 않고 보안 비밀이나 환경 변수에 보관한다. <span class="gref">[13.1·16.2절]</span>

## C

**Colab**(Google Colaboratory) 웹 브라우저에서 파이썬 코드를 작성하고 실행하는 구글의 노트북 서비스. <span class="gref">[1.3절]</span>

**CSV**(Comma-Separated Values) 한 행에 한 건의 기록을, 쉼표로 구분한 열에 항목을 저장하는 텍스트 파일 형식. <span class="gref">[3.2절]</span>

## D

**DataFrame** 행과 열로 구성된 pandas의 표 자료구조. <span class="gref">[5.1절]</span>

**dBm** 1 mW를 기준으로 전력을 데시벨로 표시한 단위. Wi-Fi 신호 세기는 0 dBm보다 작은 음수로 나타난다. <span class="gref">[5.2절]</span>

## F

**FastAPI** 파이썬으로 웹 API 서버를 작성하는 프레임워크. <span class="gref">[14.2절]</span>

## H

**HTTP** 웹에서 요청과 응답을 주고받는 규약. 요청마다 메서드(GET·POST 등)로 수행할 작업을 지정한다. <span class="gref">[14.1절]</span>

## I

**IQR** → 사분위수 범위

## J

**JSON**(JavaScript Object Notation) 딕셔너리와 같은 「이름: 값」 구조를 문자열로 표현하는 자료 형식. <span class="gref">[8.2·14.1절]</span>

## K

**kNN**(k-Nearest Neighbors) 새 자료와 가장 가까운 학습 자료 k개를 찾고, 그중 가장 많은 범주로 분류하는 모델. k-최근접 이웃. <span class="gref">[11.2절]</span>

**KPT**(Keep·Problem·Try) 유지할 점, 문제점, 시도할 개선 사항으로 정리하는 회고 방식. <span class="gref">[16.3절]</span>

## L

**LED 스트립**(LED strip) 여러 개의 RGB LED를 연결한 띠 형태의 출력 장치. 포켓쉴드의 포트에 연결한다. <span class="gref">[4.7절]</span>

**Live 모드** PC에서 프로그램을 실행하면서 USB로 연결한 사이버파이를 실시간으로 제어하는 mBlock 실행 모드. <span class="gref">[4.3절]</span>

**LOSO**(Leave-One-Subject-Out) 한 사람의 자료를 평가용으로 남기고 나머지 사람의 자료로 학습하는 과정을 사람마다 반복하는 교차 평가. <span class="gref">[12.3절]</span>

## M

**mBlock** Makeblock이 제공하는 블록 코딩·파이썬 개발 환경. <span class="gref">[4.2절]</span>

**MicroPython** 마이크로컨트롤러에서 동작하도록 구성한 경량 파이썬. Upload 모드의 기기 프로그램이 이 환경에서 실행된다. <span class="gref">[4.3절]</span>

## P

**pydantic** 자료의 형식을 모델로 정의하고 검증하는 파이썬 라이브러리. FastAPI가 요청 자료 검증에 사용한다. <span class="gref">[14.2절]</span>

## T

**TestClient** 서버를 실행하지 않고 FastAPI 엔드포인트에 요청을 보내 동작을 확인하는 시험 도구. <span class="gref">[14.2절]</span>

## U

**UDP**(User Datagram Protocol) 연결 절차 없이 데이터그램을 바로 보내는 전송 방식. 전송 성공을 보장하지 않으므로 서버의 응답으로 성공 여부를 확인한다. <span class="gref">[8.2절]</span>

**Upload 모드** 프로그램을 사이버파이에 저장해 기기가 단독으로 실행하도록 하는 mBlock 실행 모드. <span class="gref">[4.3절]</span>

## Z

**z-점수**(z-score) 측정값이 평균에서 표준편차의 몇 배만큼 떨어져 있는지를 나타내는 값. <span class="gref">[7.2절]</span>
