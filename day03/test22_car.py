# file : test22_car.py
# date : 20240131
# desc : 카 클래스 만들기

class car:
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__plate_num}가 전진합니다')

    def moveBackward(self):
        print(f'{self.__plate_num}가 후진합니다')

    def moveLeft(self):
        print(f'{self.__plate_num}가 좌회전합니다')

    def moveRight(self):
        print(f'{self.__plate_num}가 우회전합니다')

    def __init__(self, __plate_num, company, color, gear) -> None:
        self.__plate_num = __plate_num
        self.company = company
        self.color = color
        self.gear = gear

    def __str__(self) -> str:
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다'

    def getplatenumber(self): # 외부에서는 접근 할 수 없도록 막는 조치 (캡슐화)
        return self.__plate_num
    def setplatenumber(self, new_platenumber):
        self.__plate_num = new_platenumber
    


sarah = car('1234','현대','화이트','자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있다.
print(sarah)
print(f'차 번호는 {sarah.getplatenumber}')
print(f'차 색상은 {sarah.color}')
sarah.moveForward()

csuv = car('5464','현대','회색','자동')
print(csuv)

sarah.__plate_num = '9812' #악의적인 의도를 가지고 변경
print(sarah)

sarah.setplatenumber('231245')  # 캡슐화!
print(sarah)

