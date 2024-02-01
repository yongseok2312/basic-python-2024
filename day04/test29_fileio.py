# file : test29_fileio.py
# date : 20240201
# desc : 텍스트 파일 읽기

f = open('sample.txt', mode='r', encoding='utf-8')
# 다 읽었다
text = f.read()
print(text)
f.close
