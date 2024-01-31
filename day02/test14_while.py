# file : test14_while.py
# date : 20240130
# desc : while 문

## while 참인조건:
## 공통점 if 조건: elif 조건:, else:, for in range():, while 조건:
count = 0

# while count < 10:  #count 변수 값이 10보다 작거나 같은 동안 반복
#     count += 1
#     print('나무 찍기 ', count)

# 무한 루프 : window OS, 모바일 OS, 자동차네비게이션, 라즈베리파이, 아두이노, 게임
#            winform 개발...
while True: #참인동안  True 항상 참
    count += 1
    print('나무 찍기 ', count)
    if count == 10:
        break # while 반복문 정지


number = 0
while True:
    number += 1
    
    if str(number) in ['3','6','9']:
        print('짝')
        print(type(str(number)))
    
    else:
        print(number)
    if number ==30: break
    

i = ['3','6','9']
print(type(i[1]))


# number = 0
# while True:
#     number += 1
#     if str(number).count('3') >= 1 or \
#         str(number).count('6') >= 1 or \
#         str(number).count('9') >= 1:
#         # continue 는 반복에서 제외
#         print('짝')
#         print(type(number))
    
#     else:
#         print(number)
#     if number > 31: break


# number = 0
# while True:
#     number += 1
#     if  number.count('3') == 1 or \
#         number.count('6') == 1 or \
#         number.count('9') == 1:
#         print('짝')
#         print(type(number))
    
#     else:
#         print(number)
#     if number ==30: break