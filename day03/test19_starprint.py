# file : test19_starprint.py
# date : 20240131
# desc : 별찍기(피라미드 만들기)

for i in range(1,6):
    for j in range(1,6-i+1):
        print('*',end='') # 엔터대신 empty로 변환
    print()               # 안쪽 for문이 끝나면 엔터


# for i in range(1,6):
#     print('*'*i)

for i in range(1,6):
    for j in range(1,5-i+1):
        print(' ', end='')
    for j in range(1, i+1):
        print('*', end='')
    print()

for i in range(1,6):
    for j in range(1,5-i+1):
        print(' ', end='')
    for j in range(1, 2*i):
        print('*', end='')
    print()

