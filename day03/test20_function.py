# file : test20_function.py
# date : 20240131
# desc : 함수 만들기(계산기 기능)

def add(x,y) -> int:
    result = x + y
    return result

def minus(x,y) -> int:
    result = x - y
    return result

def multiple(x,y) -> int:
    result = x * y
    return result

def divide(x,y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('Hello')
    # return None 의미가 없기에 생략 가능

say_hello()
print(' 두 수 연산-> ')
a,b =map(int, input('두 정수 입력 > ').split(' '))

결과 = add(a, b)
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a,b)}')
print(f'{a} x {b} = {multiple(a,b)}')
print(f'{a} / {b} = {divide(a,b)}')

