# This Python file uses the following encoding: utf-8
import sys
import os
import time


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PySide2.QtCore import QFile, QThreadPool
from PySide2.QtUiTools import QUiLoader

from Countdown import Coundown_msg, countdownThread
from Countup import Countup_msg, CountupThread
from eye_detection import Eyedetec_msg, Eyedetec_Thread

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
        self.btnStart.clicked.connect(self.Eye_start)

        self.btnStop.clicked.connect(self.stopit)
        self.btnStop.clicked.connect(self.stopup)
        self.btnStop.clicked.connect(self.StopDetec)
        self.threadPool : QThreadPool = QThreadPool()

        self.Coundown_msg = Coundown_msg()
        self.Eyedetec_msg = Eyedetec_msg()
        self.Countup_msg = Countup_msg()



    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), 'form2.ui')
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()



    def getupstart(self):
        self.Countup_msg.countup_ObjectStart = True
        Countup_Thread = CountupThread(self.Countup_msg)
        Countup_Thread.signel.updateCountup.connect(self.countup_update)
        self.threadPool.start(Countup_Thread)

    def getstart(self):
        self.Coundown_msg.CountDown_ObjectStart = True
        Countd_Thread = countdownThread(self.Coundown_msg)
        Countd_Thread.signel.finished.connect(self.countdown_messagebox)
        Countd_Thread.signel.updateCountdown.connect(self.countdown_update)
        self.threadPool.start(Countd_Thread)

    def Eye_start(self):
        self.Eyedetec_msg.Eyedetec_start = True
        eye_thread = Eyedetec_Thread(self.Eyedetec_msg)
        eye_thread.signel.updateEyedetec.connect(self.Eyedect_Update)
        self.threadPool.start(eye_thread)

    def countup_update(self):
        self.Countup_msg.countup_time += 1
        mins, secs = divmod(self.Countup_msg.countup_time, 60)
        hour, mins = divmod(mins, 60)
        y = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.lbCountUP.setText(y)

    def countdown_update(self):
        self.Coundown_msg.countdown_time -= 1
        minss, secss = divmod(self.Coundown_msg.countdown_time, 60)
        hours, minss = divmod(minss, 60)
        x = '{:02d}:{:02d}:{:02d}'.format(hours, minss, secss)
        self.lbCountdowner.setText(x)


    def countdown_messagebox(self):

        message = QMessageBox()
        message.setText("Alert")
        message.exec_()


    def countup_Update(self):
        self.Countup_msg.countup_time += 1
        mins, secs = divmod(self.Countup_msg.countup_time, 60)
        hour, mins = divmod(mins, 60)
        y = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.lbCountUP.setText(y)


        if  self.Countup_msg.countup_ObjectStart == False:
            self.lbCountUP.setText(y)

    def Eyedect_Update(self,position):
        TotalRight = 0
        TotalCenter = 0
        TotalLeft = 0
        self.FacePosi.setText(position)
        if self.Coundown_msg.countdown_time != 0 :
            if position == "Right" :
                TotalRight += 1
            elif position == "Center" :
                TotalCenter += 1
            elif position == "Left" :
                TotalLeft += 1
        else:
            self.FacePosi.setText("Off")
        print(TotalRight,TotalCenter,TotalLeft)


    def stopit(self):
        self.Coundown_msg.CountDown_ObjectStart = False
        self.Coundown_msg.countdown_time=5
        # self.lbCountdowner.setText(str("00:30:00"))
    def stopup(self):
        self.Countup_msg.countup_ObjectStart = False

    def StopDetec(self):
        self.Eyedetec_msg.Eyedetec_start = False
        self.Eyedetec_msg.eye_positiont = "Off"
        # self.FacePosi.setText("Off")


    def closeEvent(self, event):
        x= QMessageBox.question(self,"hello","Helloworld",QMessageBox.No,QMessageBox.Yes)
        if x == QMessageBox.Yes :
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QApplication([])
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
