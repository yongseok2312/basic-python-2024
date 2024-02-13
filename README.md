# 파이썬 기초 2024
부경대 2024 IOT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
   - 코딩 폰트 - 나눔고딕코딩
   - Notepad++ 설치
   - Python 설치
   - visual studio code 설치
   - Git 설치
        - Tortoise Git 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔 출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # \ <class of 'int' >

    print( 5 + 4 / 2 ) # 7.0
    print(5==4) # Fasle
    ```
    

## 2일차
- 파이썬 기초
    - 흐름제어
        - if     (switch)
        - for    (foreach)  : 반복문 기본
        - while  (do~while) : 반복문 변형
    - 복합자료형 + 연산자(연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단, 디버깅

    ```python
   
    print('구구단 시작')
    for j in range(2,10):
     print(f'{j}단')
     for i in range(1,10):
        print(f'{j} x {i} = {i*j:2d}', end='  ') # end = 엔터대신 공백으로 변경
     print()                                     # for문이 끝나면 엔터
    # 디버깅 -> F5(디버그 시작), F10(한 줄씩 실행), F11(함수안으로 진입), F9(중단점 토글), shift + F5 디버깅 종료
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기('피라미드 만들기')
    - 함수, 람다함수는 나중에...
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화 (__plateNumber)
    - 패키지, 모듈

## 4일차
-  파이썬 기초
     - 패키지, 모듈 계속
        - pip 사용
        
        ```shell
        > pip --version # 버전확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제
        ```
     - 예외 처리 : 비정상적 프로그램 종료 막기

        ```python
        def divide(x,y):
            try:
             return x/y
            except ZeroDivisionError as e:
                print('오류!! 제수는 0이 될 수 없습니다.')
                return '오류' # zeroDivide 오류 발생
        ```
     - 텍스트 파일 입출력
    ```python
    f = open('파일명', mode='r/w/a', encoding='cp949/utf-8')
    f.read()
    f.readlines()   # 읽기
    f.writh('text') # 쓰기
    f.close()       # 파일은 반드시 닫는다
    ```


- 파이썬 응용
    - 주피터 노트북
        - ctrl + shift + p (명령팔레트) 로 시작
        - test31_jupyternotebook 참조
    - folium 기본 사용

    ![forium 사용법](https://raw.githubusercontent.com/yongseok2312/basic-python-2024/main/image/2024-02-01%2017%2016%2001.png)

## 5일차
- 파이썬 응용
    - 주피터 노트북 호라용 - 구글 코랩(Colab)
    - folium 계속
    - json 입출력
    - 응용 예제 연습
        - iP 주소 확인
        - qr code 만들기
    
## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages
- 파이썬 응용
    - window App(PyQt) 만들기

    ```shell
    >pip install PyQt5 
    >pip isntall PyQt5Designer
    ```
    - PyQt5 기본 실행
    - QtDesigner 사용법
    - ※쓰레드 학습 : UI쓰레드와 Background쓰레드 분리
        - [ ] GIL, 병렬프로세싱 더 학습할 것


    ![쓰레드예제](https://raw.githubusercontent.com/yongseok2312/basic-python-2024/main/image/KakaoTalk_20240205_165406789.gif)

    ```python
    # 쓰레드 클래스에서 시그널 선언
    class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
        setSignal = pyqtSignal(int)
        # ...

        def run(self) -> None: # 스레드 실행
            # 스레드로 동작할 내용
            maxVal = 1000001
            self.initSignal.emit(maxVal) # UI쓰레드로 보내기...
            # ...

    class qtwin_exam(QWidget):  # UI 스레드
        # ...
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...    
    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 슬롯 함수
    @pyqtSlot(int) # 데코레이터 # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def initPgbtask(self, maxVal):
        self.pgbtask.setValue(0)
        self.pgbtask.setRange(0,maxVal-1)
    ```

## 7일차
- 파이썬 응용
    - 객체지향 w정리
        - 상속, 오버라이딩(재정의: 본래의 함수를 다른 의미로 바꿈), 오버로딩(같은 이름의 함수를 여러개 활용, 매개변수는 다르게)
    - 가상환경 -> virtualenv
        - 다른 버전 파이썬도 설치해야 사용가능
        - 현재 3.11에서 3.9 가상환경 만들려면 3.9 파이썬 설치 필요
    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터

    ![PyQt예제](https://raw.githubusercontent.com/yongseok2312/basic-python-2024/main/image/PyQt그림판.jpg)

## 8일차
- 파이썬 응용
    - PyQt5 응용예제 계속
- 파이썬 기본 코딩테스트
    - 주피터노트북 활용