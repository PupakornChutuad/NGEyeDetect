# This Python file uses the following encoding: utf-8
import sys
import os
import time
import win32api

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PySide2.QtCore import QFile, QThreadPool
from PySide2.QtUiTools import QUiLoader

from Countdown import Coundown_msg, countdownThread
from Countup import Countup_msg, countupThread

class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.load_ui()

        self.btnStart: QPushButton = self.findChild(QPushButton, "btnStart")
        self.btnStop: QPushButton = self.findChild(QPushButton, "btnStop")
        self.btnVH: QPushButton = self.findChild(QPushButton, "btnVH")

        self.lbCountdowner: QLabel = self.findChild(QLabel, "lbCountdowner")
        self.lbCountUP: QLabel = self.findChild(QLabel, "lbCountUP")
        self.FacePosi: QLabel = self.findChild(QLabel, "FacePosi")

        self.btnStart.clicked.connect(self.getstart)
        self.btnStart.clicked.connect(self.getupstart)
        self.btnStop.clicked.connect(self.stopit)
        self.btnStop.clicked.connect(self.stopup)
        self.threadPool = QThreadPool()

        self.Coundown_msg = Coundown_msg(self.countdown_update)
        self.Countup_msg = Countup_msg(self.countup_Update)

        self.messageBox: QMessageBox = QMessageBox()
        self.messageBox.setText("Hello ")
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), 'form2.ui')
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()



    def getupstart(self):
        self.Countup_msg.countup_ObjectStart = True
        Countup_Thread = countupThread(self.Countup_msg)
        self.threadPool.start(Countup_Thread)

    def getstart(self):
        self.Coundown_msg.CountDown_ObjectStart = True
        Countd_Thread = countdownThread(self.Coundown_msg)
        self.threadPool.start(Countd_Thread)

    def countdown_update(self):
        self.Coundown_msg.countdown_time -= 1
        minss, secss = divmod(self.Coundown_msg.countdown_time, 60)
        hours, minss = divmod(minss, 60)
        x = '{:02d}:{:02d}:{:02d}'.format(hours, minss, secss)
        self.lbCountdowner.setText(x)
        if self.Coundown_msg.countdown_time==0:
            win32api.MessageBox(None, 'hello', 'title')

    def countup_Update(self):
        self.Countup_msg.countup_time += 1
        mins, secs = divmod(self.Countup_msg.countup_time, 60)
        hour, mins = divmod(mins, 60)
        y = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.lbCountUP.setText(y)

        if  self.Countup_msg.countup_ObjectStart == False:
            self.lbCountUP.setText(y)

    def stopit(self):
        self.Coundown_msg.CountDown_ObjectStart = False
        self.Coundown_msg.countdown_time=5
        # self.lbCountdowner.setText(str("00:30:00"))
    def stopup(self):
        self.Countup_msg.countup_ObjectStart = False


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
