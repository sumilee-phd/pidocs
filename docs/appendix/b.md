# B. 사이버파이 API 요약

이 책의 기기 코드에서 사용하는 함수를 정리한다. 「확인 근거」 열은 각 함수를 무엇으로 확인했는지 표시한다. 「실기기 확인 전」인 함수는 문서 기준으로 작성했으며, 실습 기기에서 동작을 확인한 뒤 확정한다.

| 확인 근거 | 의미 |
|---|---|
| 블록 변환 | mBlock 웹 버전 Upload 모드에서 블록을 파이썬으로 변환해 함수 이름과 인자를 확인(4.4·4.6절) |
| 측정 노드 | 2026-11-04 측정 노드 실습의 기기 프로그램(v4.6)에서 동작 확인(8.1·8.2절) |
| 문서 기준 | Makeblock mCode 공식 문서 기준, 실기기 확인 전 |

## 이벤트

| 함수 | 기능 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `@event.start` | 전원을 켜면 아래 함수를 실행 | 4.4, 8.1 | 블록 변환 |
| `@event.is_press('a')` | A 단추를 누르면 아래 함수를 실행 | 4.6, 8.1 | 블록 변환 |
| `@event.is_press('b')`, `@event.is_press('middle')` | B 단추, 조이스틱 가운데를 누르면 실행 | 8.1 | 문서 기준 |

## 화면

| 함수 | 기능 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `cyberpi.console.println(값)` | 값을 출력하고 줄 바꿈 | 4.5 이후 | 블록 변환 |
| `cyberpi.console.clear()` | 화면 지우기 | 4.5, 4.6, 8장, 12.2 | 측정 노드 |
| `cyberpi.console.print(값)` | 값을 출력하고 줄을 바꾸지 않음 | 4.5 | 실기기 확인 전 |
| `cyberpi.display.show_label(문자열, 크기, 위치)` | 지정 위치에 문자열 표시 | 4.7, 7.4 | 문서 기준 |
| `cyberpi.display.clear()` | 표시 영역 지우기 | 4.7, 7.4 | 문서 기준 |

## 본체 LED

| 함수 | 기능 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `cyberpi.led.on(r, g, b, "all")` | LED 5개를 RGB 색으로 점등 | 4.4, 4.5 | 블록 변환 |
| `cyberpi.led.off("all")` | LED 5개 소등 | 4.4, 4.5 | 블록 변환 |
| `cyberpi.led.on(r, g, b, 번호)` | 1~5번 중 지정한 LED만 점등 | 4.5 | 실기기 확인 전 |

## 센서와 단추

| 함수 | 반환값 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `cyberpi.get_bri()` | 주변 조도(0~100) | 2.4, 4.6, 4.7, 8.1 | 블록 변환 |
| `cyberpi.get_loudness("maximum")` | 짧은 시간 동안 측정한 소리 크기의 최댓값 | 4.6, 4.7, 7.4 | 블록 변환 |
| `cyberpi.get_acc('x')` | 지정 축(`'x'`·`'y'`·`'z'`)의 가속도 | 4.6, 8.5, 12.2 | 블록 변환 |
| `cyberpi.controller.is_press("a")` | 단추를 누르고 있으면 `True`(`"a"`·`"b"`·`"middle"`) | 4.5, 7.4, 8.1, 8.5, 12.2 | 측정 노드 |

## 소리

| 함수 | 기능 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `cyberpi.audio.play_tone(주파수, 시간)` | 지정한 주파수의 음을 지정 시간 동안 출력 | 7.4(확인 문제) | 문서 기준 |

## 포켓쉴드 LED 스트립

`port`는 `"s1"`, `"s2"`, `"all"` 중 하나다. LED 위치 번호는 1부터 시작한다(4.7절).

| 함수 | 기능 | 사용 절 | 확인 근거 |
|---|---|---|---|
| `cyberpi.pocket.led_on(r, g, b, id, port)` | `id` 위치(1~36 또는 `"all"`)의 LED를 RGB 색으로 점등 | 4.7 | 문서 기준 |
| `cyberpi.pocket.led_show(color, port)` | 색 약어 문자열(`"r o y g …"`)로 전체 색 지정 | 4.7, 7.4, 12.1 | 문서 기준 |
| `cyberpi.pocket.led_off(id, port)` | `id` 위치의 LED 소등 | 4.7, 7.4 | 문서 기준 |
| `cyberpi.pocket.led_set_bri(밝기, port)` | 밝기 0~100(%) 지정 | 4.7, 7.4, 12.1 | 문서 기준 |
| `cyberpi.pocket.led_move(step, cycle, port)` | 색 배열을 `step`칸 이동 | 4.7 | 문서 기준 |

## Wi-Fi와 UDP 전송

Upload 모드의 MicroPython 모듈이다(8.2절).

| 함수 | 기능 | 확인 근거 |
|---|---|---|
| `network.WLAN(network.STA_IF)` | 공유기에 접속하는 단말 모드의 Wi-Fi 객체 생성 | 측정 노드 |
| `wlan.active(True)` | Wi-Fi 기능 켜기 | 측정 노드 |
| `wlan.connect(이름, 비밀번호)` | 공유기 접속 시작(완료를 기다리지 않음) | 측정 노드 |
| `wlan.isconnected()` | 접속 완료 여부 | 측정 노드 |
| `wlan.ifconfig()[0]` | 기기에 배정된 IP 주소 | 측정 노드 |
| `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)` | UDP 소켓 생성 | 측정 노드 |
| `s.settimeout(초)` | 응답 대기 시간 제한 | 측정 노드 |
| `s.sendto(바이트, (IP, 포트))` | 데이터그램 전송 | 측정 노드 |
| `s.recv(크기)` | 응답 수신 | 측정 노드 |

## 기타

| 함수 | 기능 | 사용 절 |
|---|---|---|
| `time.sleep(초)` | 지정 시간 동안 대기 | 4장 이후 |

!!! abstract "참고 문서"
    - [Makeblock mCode CyberPi API 문서](https://www.yuque.com/makeblock-help-center-en/mcode/cyberpi-api)
    - [MicroPython network 모듈](https://docs.micropython.org/en/latest/library/network.html)
    - [MicroPython socket 모듈](https://docs.micropython.org/en/latest/library/socket.html)
