# file : test41_thread.py
# date : 20240205
# desc : qt스레드로 동작


import sys
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int)    # 시그널을 UI스레드로 전달하기위한 변수 객체
    setSignal = pyqtSignal(int)
    textsignal = pyqtSignal(str)
    

    def __init__(self,parent) -> None:  
        super().__init__(parent)
        self.parent = parent # BackWorker에서 사용할 멤버변수
    
    def run(self) -> None: # 스레드 실행
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        # 스레드로 동작할 내용
        # self.parent.pgbtask.setValue(0) # QThread에선 UI관련된 처리를 할 수 없음
        # self.parent.pgbtask.setRange(0, maxVal-1)
        for i in range(maxVal+1):
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.textsignal.emit(print_str)
            # self.parent.txblog.append(print_str)
            # self.parent.pgbtask.setValue(i)

class qtwin_exam(QWidget): #UI 스레드
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner에서 만든 Ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnstart.clicked.connect(self.btnstartClicked) # ui 파일내에 있는 위젯 접근은 VScode상에서 색상으로 표기가 안됨
    
    
    def btnstartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        th.initSignal.connect(self.initPgbtask) # 스레드에서 초기화 시그널이 오면 initPgbtask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setPgbtask)
        th.textsignal.connect(self.setTxblog)
        

    def closeEvent(self,QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료할래?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
    
    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 슬롯 함수
    @pyqtSlot(int) # 데코레이터 # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def initPgbtask(self, maxVal):
        self.pgbtask.setValue(0)
        self.pgbtask.setRange(0,maxVal-1)

    @pyqtSlot(str)  # BackWorker 스레드에서 self.setSignal.emit() 동작해서 실행
    def setTxblog(self,msg):
        self.txblog.append(msg)

    @pyqtSlot(int)  # BackWorker 스레드에서 self.lastSignal.emit() 동작해서 실행
    def setPgbtask(self, val):
        self.pgbtask.setValue(val)

if __name__=='__main__':


    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()           




