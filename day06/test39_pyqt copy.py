# file : test39_pyqt.py
# date : 20240205
# desc : qt디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/test app.ui', self) # QtDesigner에서 만든 Ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnstart.clicked.connect(self.btnstartClicked) # ui 파일내에 있는 위젯 접근은 VScode상에서 색상으로 표기가 안됨
        self.btnstop.clicked.connect(self.btnstopClicked)

    def btnstartClicked(self):
        print('시작 버튼 클릭')
        self.lblstatus.setText('상태 : 동작 시작')
        QMessageBox.about(self, '동작','***시스템이 시작되었습니다.')

    def btnstopClicked(self):
        print('종료버튼 클릭')
        self.lblstatus.setText('상태 : 동작 중지')



    def closeEvent(self,QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



if __name__=='__main__':


    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()
