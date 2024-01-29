# date : 29249129
# desc : 연산자

# 사칙연산: + - * / //(정수로 나누기) %(나눈 나머지), **(제승)
# 비교 연산: =(값 할당), ==(비교), >, <, >=, <=, !=(같지 않다)
# 논리 연산: and, or, not

print(2*4)
print(2**4)

print(5/2) # 실수
print(5//2) # 정수
print(5%2) # 나머지

# print(5/0) 0으로 나눌 수 없다

print (5 == 4)
#print (5 = 4) =은 집어 넣는 개념
print ( 5 > 4 )
print (5>=4)
print (5<4)
print (5<=4)
print (5!=4)

print(5<=4 and (5/2 < 3)) # False and 기준으로 왼쪽 / 오른쪽 모두 참이어야 함
print( 5 <= 4 or (5/2 <3)) # True 한쪽만 참이어도 참
print(not(5<4))