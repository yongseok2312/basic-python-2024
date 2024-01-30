# file : test13_range.py
# date : 20240130
# desc : 리스트 범위 지정

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a)

# 범위 지정 range(n), 0부터 n개의 범위의 수를 생성
print(range(5))
print(list(range(5)))
print(list(range(1,6))) # 1~5
print(list(reversed(range(2, 21, 2)))) # 2 부터 20까지 2씩 증가
print(list(range(1, 20, 2))) # 1 부터 19까지 2씩증가
print(list(range(10, -1, -1))) # countdown reversed 사용가능

list_a = list(range(1,101))
print(list_a)

list_a = [ i for i in range(1,101)]
print(list_a)

