# file : test12_dictionary.py
# date : 20240130
# desc : 복합자료형 딕셔너리

## 사전형 key와 value쌍을 나열해 놓은 자료형
# { key:value, key:value, key:value, ...}
dict_movie = { 'name': '어벤져스 엔드게임', 'type':'히어로 무비','year':2019, 'director':['안소리루소', '조 루소'],'cast':['아이언맨','타노스','헐크', '토르', '닥터스트레인지']}

print(dict_movie['name']) #조회
print(dict_movie['year'])

dict_movie['year']=2020 #수정
print(dict_movie['year'])

dict_movie['producer'] = '케빈 파이기' #추가
print(dict_movie)

if 'musician' in dict_movie:    # 딕셔너리에 키기 있는지 확인
    print(dict_movie['musician'])
else:
    print('음악감독 없음')


musician = dict_movie.get('musician') # 오류(예외) 발생x 확인 가능
print(musician)

print('반복문 ------------------------------------------')
# 반복문으로 출력
for key in dict_movie:
    print(key, ':', dict_movie[key])

print('반복문 다른 방법 -----------------------------')
for key, value in dict_movie.items():
    print(key, ':', value)