# file : test37_pyqt.py
# date : 20240205
# desc : PyQt5 기본 화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
## GUI : 그래픽 유저 인터페이스 -> 윈도우 운영체제와 같음
## CLI : 커멘드 라인 인터페이스 -> 명령프롬프트
from PyQt5.QtWidgets import QApplication, QWidget
# print(sys.argv)  # 현재 파이썬 파일의 경로 표시 실행 파일위치 확인

class qtwin_exam(QWidget): #QWidget 상속. QWidget이 가진 모든것을 사용할 수 있음
    # 생성자
    def __init__(self)-> None:
        super().__init__() # super 부모
        self.initUI() # 화면 초기화 함수를 호출


    def initUI(self):
        self.setGeometry((1920 - 400) //2,(1080-300)//2, 400, 300) # x, y, widt, height
        self.setWindowTitle('QT5 Hello world!')
        self.text=''
        self.show()
    
    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) #0~255
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText(400//2,300//2,'Hell World')
        paint.drawText(event.rect(), Qt.AlignCenter, self.text) # AlignLeft, AlignCenter, AlignRight
    
    def paintEvent(self, event) -> None: # 재정의(override)
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫는다
        


loop = QApplication(sys.argv) # 내 소스 위치로 앱을 생성
isinstance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()