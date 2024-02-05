# file : test38_pyqt.py
# date : 20240205
# desc : PyQt5 event(Signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('클릭', self)
        btn01.setGeometry(50, 100, 100, 40)
        btn01.clicked.connect(self.btn01_clicked) # 버튼 클릭하면(signal) btn01_clicked 함수를 실행

        self.setGeometry(300,200,400,200)
        self.setWindowTitle('버튼 이벤트')
        self.show()

    def btn01_clicked(self):
        QMessageBox.about(self, '버튼 클릭', '버튼이 클릭 되었습니다.')

    def closeEvent(self,QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__=='__main__': # main entry 확인 조건 추가


    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    loop.exec_()
