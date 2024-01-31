# file : test18_input.py
# date : 20240131
# desc : 다중 입력...
# 원래는 (in_a, in_b) 튜플형으로 데이터 받는게 정석 -> 생략

# 두 수를 받을 때 가장 원시적인 방법
# input_a, input_b = input('값을 두개 입력(공백으로 구분) > ').split(' ')
# input_a = int(input_a)
# input_b = int(input_b)

# map()함수 사용
input_a, input_b = map(int, input('값을 두개 입력(공백으로 구분) > ').split(' '))

print(f'입력값 {input_a}, {input_b}')
print(f'더하기 결과 {input_a + input_b}')

