# file : test28_fileio.py
# date : 20240201
# desc : 텍스트 파일 입출력
# mode 쓸건지 말건지 mode : a(append) r(reed) w(write)
# endcoding: cp949(한글), utf-8(만국공통어)

f = open('sample.txt', mode='w', encoding='utf-8')
# 뭔가를 한다.
f.write('안녕하세요. 우리는 IoT개발자 과정입니다.\n')
f.write('반갑습니다.')
f.close() # 파일은 무조건 마지막에 닫는다
print('파일이 생성되었습니다.')
