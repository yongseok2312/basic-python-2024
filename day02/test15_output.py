# file : test15_output.py
# date : 20240130
# desc : 콘솔 출력 포맷 양식 string format

string_1 = '{}'.format(10) # {}위치에 함수 뒤에 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = '이용석' # name = input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = ' {} {} {}'.format(4000, '만', '빌려주세요')
print(string_3)

string_4 = '{:4d}____'.format(100) # :d 정수 숫자 표현 d,5d,05d,010d, +양수음수 기호 첨가, =기호와 숫자 분리 
print(string_4)

#실수 문자열 포맷 f 기본 소수점 6자리
string_5 = '_____{:06.2f}_____'.format(35.141592)
print(string_5)

# 파이썬 3.6 이후 도입 format 함수 X f만 사용
val = 53.14
string_6 = f'{val:0.2f}'
print(string_6)

string_7= 'Hello, World!'
print(string_7.upper()) # 대문자 변환
print(string_7.lower()) # 소문자 변환
print(string_7.lower().capitalize()) # 시작 부분만 대문자 변환
print(string_7.split(' '))

st8 = 'Hello, I am MG Sung. I am a lecturer. Good Luck for your day.'
words = st8.split(' ')
print(words)
print(f'st8의 문장 단어개수는 {len(words)}개 입니다.')

st9 = 'a10'
print(st9.isalnum()) # 숫자와 알파벳
print(st9.isnumeric()) # int
st10 = '-10'            #소수점은 함수를만들어서 처리
print(st10.isdecimal()) # 정수
print('안냥' in '안녕하세요') #단어가 있는지 확인
