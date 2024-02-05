# file : test40_nothread.py
# date : 20240205
# desc : qt스레드 없이 동작

import sys
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner에서 만든 Ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnstart.clicked.connect(self.btnstartClicked) # ui 파일내에 있는 위젯 접근은 VScode상에서 색상으로 표기가 안됨


    def btnstartClicked(self):
        maxVal = 1000001
        self.pgbtask.setValue(0) # 프로그래스바 0부터 시작
        self.pgbtask.setRange(0, maxVal-1) # 0부터 100까지 범위를 잡는다
        for i in range(maxVal): # 0부터 100까지
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txblog.append(print_str)
            self.pgbtask.setValue(i)

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
