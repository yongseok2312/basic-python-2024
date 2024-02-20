# file : test43_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5 import uic   #Qt디자이너 호출시 필요
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        # uic.loadUi('./day07/pyPaint_1.ui', self)
        uic.loadUi('C:/sources/basic-python-2024/day07/pyPaint_1.ui',self)    # 실행 파일 생성시 경로에 절대경로를 사용
        # self.setWindowIcon(QIcon('image/그림판.jpg'))
        self.setWindowIcon(QIcon('C:/sources/basic-python-2024/day07/그림판.jpg'))

        self.setWindowTitle('py 그림판')
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')

        self.show()
        self.setCenter()


    def initSignal(self):

        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        self.btn_load.clicked.connect(self.buttonClicked) # 버튼 추가
        self.btn_save.clicked.connect(self.btnsaveClicked) # 버튼 추가

    # def btnloadClicked(self):
    #     image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
    #     imagePath = image[0]
    #     pixmap = Qpixmap(imagePath) 파일 경로에 있는 이미지를 읽어서 pixmap객체에 담기 
    #     pixmap.scaledToHeight(381)
    #     self.lb_canvas.setPixmap(pixmap)
    #     self.lb_canvas.adjustSize()
    
    def btnsaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지 저장', '', 'Image file(*.jpg;*.png)')
        if filePath == '':return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)


    def buttonClicked(self):
        btn_val = self.sender().objectName() # self.sender() -> btn_black
        print(btn_val)
        if btn_val == 'btn_black':
            self.brushColor= Qt.black # QColor('#ff0000')
        elif btn_val == 'btn_red':
            self.brushColor= Qt.red
        elif btn_val == 'btn_blue':
            self.brushColor= Qt.blue
        elif btn_val == 'btn_load':
            image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
            imagePath = image[0]
            pixmap = QPixmap(imagePath)
            pixmap.scaledToHeight(381)
            self.lb_canvas.setPixmap(pixmap)
            self.lb_canvas.adjustSize()
        else:
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)
        

    
    # def btnBlackClicked(self):
    #     btn_val = self.sender().objectName() # self.sender() -> btn_black
    #     print(btn_val)
    #     self.brushColor= Qt.black

    # def btnRedClicked(self):
    #     btn_val = self.sender().objectName() 
    #     print(btn_val)
    #     self.brushColor= Qt.red


    # def btnBlueClicked(self):
    #     btn_val = self.sender().objectName() 
    #     print(btn_val)
    #     self.brushColor= Qt.blue


    # def btnClearClicked(self):
    #     btn_val = self.sender().objectName() 
    #     print(btn_val)
    #     self.canvas.fill(QColor('white'))
    #     self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(),e.y())
        brush.end()
        self.update()
    



    
    def setCenter(self): 
        gm = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        gm.moveCenter(cp)
        self.move(gm.topLeft())
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
