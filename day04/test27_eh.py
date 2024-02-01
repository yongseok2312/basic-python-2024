# file : test27_eh.py
# date : 20240201
# desc : 예외발생 처리

def add(x,y):
    return x + y
def minus(x,y):
    return x - y
def mulitple(x,y):
    return x * y
def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print('오류!! 제수는 0이 될 수 없습니다.')
    return '오류' # zeroDivide 오류 발생

def getOperands(): # 계산할 수를 입력 받는 함수 -> 반복되는 것을 함수로 바꾸면 편함
    # 34. 을 넣었을 때 예외 발생 ValueError
    try:
        a,b=map(float,input('두 수를 입력 하세요(구분자 ,) > ').split(','))
        return a,b
    except ValueError as e:
        # print(e)
        print('입력 오류 : 정수만 입력하세요')
        return 1,1

while True:
    mnu = input('메뉴입력(p[덧셈],m[뺄셈],t[곱셈],d[나눗셈],x[종료] > ')

    if mnu == 'p':
        a,b=getOperands()
        print(f'{a} + {b} = {add(a,b)}')
    elif mnu == 'm':
        a,b=getOperands()
        print(f'{a} - {b} = {minus(a,b)}')
    elif mnu == 't':
        a,b=getOperands()
        print(f'{a} X {b} = {mulitple(a,b)}')
    elif mnu == 'd':
        a,b=getOperands()
        print(f'{a} / {b} = {divide(a,b)}')
        
    elif mnu == 'x':
        break
    else:
        continue    # 다시 메뉴 선택으로 올라감

