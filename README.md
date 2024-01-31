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



    - 객체지향(나중에...)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속
        - 추상클래스, 인터페이스...