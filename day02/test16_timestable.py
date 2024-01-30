# file : test16_timestable.py
# date : 20240130
# desc : 구구단 프로그램
# spec : for문 잘 써야함. 2중 for문의 이해
# i * j
# 디버깅 -> f5(디버그 시작), f10(한 줄씩 실행), f11(함수안으로 진입), f9(중단점 토글)
# 조사식 확인
# shift + F5 디버깅 종료
print('---------------------------------------구구단 시작--------------------------------------------')
for j in range(2,10):
     print(f'{j}단')
     for i in range(1,10):
        print(f'{j} x {i} = {i*j:2d}', end='  ') # end = 엔터대신 공백으로 변경
     print()                                     # for문이 끝나면 엔터



