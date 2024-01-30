# date : 20240130
# desc : 흐름제어 if

## 조건이 참일때아 거짓일때로 나누어서 어떤일을 처리 if
## if 조건: - 참인 조건
## else: - 거짓인 조건
## 입력함수 input() - 문자

number = int(input('정수를 입력하세요 > '))  # int(input()) 문자로 된 입력값을 정수로 변경

if number > 0:
    print('양수입니다')
elif number == 0:
    print(number,'입니다')
else:
    print('음수입니다')
    