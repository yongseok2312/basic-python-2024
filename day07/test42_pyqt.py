# file : test42_pyqt.py
# date : 20240206
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 삽입 .scaledToWidth(800) 큰 해상도를 w800으로 고정
        pixmap = QPixmap('./image/kitty cat.png').scaledToWidth(800)
        
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(self)
        lblSize.setFont(QFont('NanumGothicCoding', 20)) # 폰트 사이즈 변경
        lblSize.setStyleSheet('Color: blue;')
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}')    # kitty.png의 width x height 출력
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)     # 가로 중앙 정렬 | 세로 중앙 정렬

        vbox = QVBoxLayout(self)    # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblImage)    # VL에 위젯 생성
        vbox.addWidget(lblSize)     
        self.setLayout(vbox)        # 폼에 VL 추가 동일

        lblSize.setSizeIncrement(200, 50)

        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300,300,300,300)   # x,y,w,h 
        self.setGeometry(rect)  # 같은 이름의 함수를 여러개 선언해놓고 입맛에 맞게 골라쓸 수 있음 overloading
        # self.setGeometry(300,300,300,300)
        self.show()
        self.setCenter()

    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
        

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    print(width, 'x', height) # 활용도 높음 screen size
    ins = WinApp()
    # showFullScreen() 모니터를 꽉 채워서 출력
    sys.exit(app.exec_()) # 종료시 리소스 반환등 효율
