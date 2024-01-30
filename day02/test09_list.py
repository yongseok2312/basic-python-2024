# date : 20240130
# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60
# index = 0,1,2,3,4 인덱스의 마지막 값은 n-1
# index = -5,-4, -3, -2, -1 파이썬만 사용가능
std = [80,90,100,50,60] #list
print(std)
list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3,4), std]
print(list_1)
print(list_1[5])
list_1[6] = '바꾼값' #리스트 변경
print(list_1)


print(list_1[:2]) # : 뒤의 수는 출력하고 싶은 index+1이 필수
## 이중리스트
print(list_1[4][2]) # 리스트 내에 리스트 [1,2,3,4] 중 3가져오기

## 리스트 연산 + *만 사용가능
list_2 = [1,2,3] 
list_3 = [7,8,9]
print(list_2 + list_3) # 리스트 연결
print( list_3 *2) # 리스트 반복

## 리스트 길이 함수 len
print(len(list_1))

## 리스트 마지막에 추가 append
## isert(index, val) 리스트의 index 이후에 val 추가
print(list_1)
list_1.append('Hello!!')

list_1.insert(2,100)
print(list_1)

## 기존 리스트 확장 extend 더하기와 거의 유사
list_1.extend(list_2)
print(list_1)
print(list_2)

## 리스트 삭제
del list_1[4]   #리스트의 인덱스만 삭제
print(list_1)
del list_2      #리스트 자체 삭제


val = list_1.pop()    #마지막 값을 꺼내오기
print(val)
print(list_1)

print(std)
val = std.pop(2)
print(std)

## clear() del과의 차이 clear는 내용만 삭제여서 출력 가능 del은 완전히 삭제
# list_3.clear()
# print(list_3)

##sort()
print(list_1)
# list_1.sort() # 문자열, 숫자, 불 등 섞여있는 리스트는 정렬안됨
list_3.sort()
print(list_3) # 오름차순 정렬
list_3.sort(reverse = True)
print(list_3)

# in, not in
print( 99 in std) # 값을 찾을 때 사용
print( 90 in std)

# reverse, copy, count 등 함수 더 있음
# *리스트 : 전개연산자
list_a = [1, 3, 5]
list_b = [2, 4, 8]

list_c = [*list_a, *list_b]
print(list_c)
list_d = [list_a,list_b]
print(list_d)
# Koreansum = s1 + s2 + s3 + s4 + s5
# print(Koreansum)
# print(Koreansum/5)

