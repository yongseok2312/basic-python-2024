# file : test10_for.py
# date : 20240130
# desc : for 반복문

std = [80,90,100,50,60]
kor_sum = 0

for i in std: # std 리스트에 값을 하나씩 i에 넣어서 반복할 요소가 있을때까지
    kor_sum += i

print(kor_sum)
print(kor_sum/len(std))

list_a = [[1,3,5],[2,4,8],[10,15,20]] # 2차원 리스트

for in_list in list_a:
   for item in in_list:
    print(item)

for in_list in list_a:
    print(in_list)
   