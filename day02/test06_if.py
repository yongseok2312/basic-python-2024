# date : 20240130
# desc : 여러조건 if문

date =input('날짜 입력(예: 12-31) > ')

month = date.split('-')[0] # '12'
day = date.split('-')[1] # '31'

if month == '12' and day == '25' :
    print('메리 크리스마스!!')
elif month == '01' and day == '01' :
    print('해피뉴이어')
elif month == '04' and day == '14' :
    print('짜장면이나 드셈')
else:
    print('보통날입니다')
    