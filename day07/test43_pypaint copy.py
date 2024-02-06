# file : test43_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5 import uic   #Qt디자이너 호출시 필요
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day07/pyPaint.ui', self)
        self.setWindowIcon(QIcon('./image/그림판.jpg'))
        self.setWindowTitle('py 그림판')
        # 캔버스 초기화
        self.brushColor = Qt.GlobalColor.black
        self.canvas = QPixmap(self.lb_canvas)
        self.show()
        self.setCenter()


    def initSignal(self):

        self.btn_black.clicked.connect(self.btnBlackClicked)
        self.btn_red.clicked.connect(self.btnRedClicked)
        self.btn_blue.clicked.connect(self.btnBlueClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)

    def btnBlackClicked(self):
        btn_val = self.sender().objectName() # self.sender() -> btn_black
        print(btn_val)

    def btnRedClicked(self):
        btn_val = self.sender().objectName() 
        print(btn_val)

    def btnBlueClicked(self):
        btn_val = self.sender().objectName() 
        print(btn_val)

    def btnClearClicked(self):
        print('모두 지움')

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
    
    



    
    def setCenter(self): 
        gm = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        gm.moveCenter(cp)
        self.move(gm.topLeft())
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
