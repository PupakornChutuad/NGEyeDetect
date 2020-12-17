# This Python file uses the following encoding: utf-8
import sys
import os
import time
import pandas as pd
import datetime


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
from PySide2.QtCore import QFile, QThreadPool, QCoreApplication
from PySide2.QtUiTools import QUiLoader

from TestScript import TestScript
from Countdown import Coundown_msg, countdownThread
from Countup import Countup_msg, CountupThread
from CountTimeOut import CounTimeOut_msg, countTimeOutThread
from eye_detection import Eyedetec_msg, Eyedetec_Thread

class MainWin(QWidget):

    def __init__(self,parent=None):
        super(MainWin, self).__init__(parent)
        self.load_ui()

        self.btnStart: QPushButton = self.findChild(QPushButton, "btnStart")
        self.btnStop: QPushButton = self.findChild(QPushButton, "btnStop")
        self.btnVH: QPushButton = self.findChild(QPushButton, "btnVH")
        self.TestForm_btn: QPushButton = self.findChild(QPushButton, "TestForm_btn")

        self.lbCountdowner: QLabel = self.findChild(QLabel, "lbCountdowner")
        self.lbCountUP: QLabel = self.findChild(QLabel, "lbCountUP")
        self.lbCountTimeOut: QLabel = self.findChild(QLabel, "lbCountTimeOut")
        self.FacePosi: QLabel = self.findChild(QLabel, "FacePosi")

        self.btnStart.clicked.connect(self.getstart)
        self.btnStart.clicked.connect(self.getupstart)
        self.btnStart.clicked.connect(self.Eye_start)

        self.btnStop.clicked.connect(self.stopit)
        self.btnStop.clicked.connect(self.stopup)
        self.btnStop.clicked.connect(self.stopTimeOut)
        self.btnStop.clicked.connect(self.StopDetec)

        self.TestForm_btn.clicked.connect(self.OpenTestForm)

        self.threadPool : QThreadPool = QThreadPool()

        self.TestScript = TestScript()

        self.Coundown_msg = Coundown_msg()
        self.Countup_msg = Countup_msg()
        self.CounTimeOut_msg = CounTimeOut_msg()
        self.Eyedetec_msg = Eyedetec_msg()




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
        Countd_Thread.signel.timeout.connect(self.getTimeOutstart)
        Countd_Thread.signel.timeout.connect(self.countdown_messagebox)
        Countd_Thread.signel.timeout.connect(self.stopit)
        Countd_Thread.signel.updateCountdown.connect(self.countdown_update)
        self.threadPool.start(Countd_Thread)

    def getTimeOutstart(self):
        self.CounTimeOut_msg.CountTimeOut_ObjectStart = True
        CountTimeOut_Thread = countTimeOutThread(self.CounTimeOut_msg)
        CountTimeOut_Thread.signel.updateCountTimeOut.connect(self.countTimeOut_update)
        self.threadPool.start(CountTimeOut_Thread)



    def Eye_start(self):
        self.Eyedetec_msg.Eyedetec_start = True
        eye_thread = Eyedetec_Thread(self.Eyedetec_msg)
        eye_thread.signel.updateEyedetec.connect(self.Eyedect_Update)
        # eye_thread.signel.updateMissing.connect(self.stopit)
        # eye_thread.signel.updateMissing.connect(self.stopup)
        # eye_thread.signel.updateArrive.connect(self.getstart)
        # eye_thread.signel.updateArrive.connect(self.getupstart)
        self.threadPool.start(eye_thread)

    def countdown_update(self):
        self.Coundown_msg.countdown_time -= 1
        minss, secss = divmod(self.Coundown_msg.countdown_time, 60)
        hours, minss = divmod(minss, 60)
        x = '{:02d}:{:02d}:{:02d}'.format(hours, minss, secss)
        self.lbCountdowner.setText(x)

    def countdown_messagebox(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)

        message.setWindowTitle("คำเตือน")
        message.setText("ขณะนี้คุณได้ใช้เวลาอยู่กับหน้าจอคอมพิวเตอร์นานเกินไป ")
        message.setInformativeText("กรุณาละสายตาออกห่างจากคอมพิวเตอร์เป็นเวลา 20 วินาที"
                                   "หากท่านต้องการที่จะพักกรุณากดปุ่ม 'หยุด' ")

        # c=QPushButton(message)

        message.exec_()

    def countTimeOut_update(self):

        self.CounTimeOut_msg.countTimeOut_time += 1
        mins, secs = divmod(self.CounTimeOut_msg.countTimeOut_time, 60)
        hour, mins = divmod(mins, 60)
        z = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.lbCountTimeOut.setText(z)



    def countup_update(self):
        self.Countup_msg.countup_time += 1
        mins, secs = divmod(self.Countup_msg.countup_time, 60)
        hour, mins = divmod(mins, 60)
        y = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.lbCountUP.setText(y)

    def Eyedect_Update(self, position ):
        self.FacePosi.setText(position)
        TotalRight = 0
        TotalCenter = 0
        TotalLeft = 0
        # if self.Coundown_msg.countdown_time != 0:
        if position == "Right":
            # self.Eyedetec_msg.CountEyeRight += 1
            TotalRight += 1
            print("Right",TotalRight)

        elif position == "Center":
            # self.Eyedetec_msg.CountEyeCenter += 1
            TotalCenter += 1
            print("Center",TotalCenter)

        elif position == "Left":
            # self.Eyedetec_msg.CountEyeLeft +=1
            TotalLeft += 1
            print("Left",TotalLeft)

    def stopit(self):
        self.Coundown_msg.CountDown_ObjectStart = False
        self.Coundown_msg.countdown_time=50
        self.lbCountdowner.setText(str("00:20:00"))


    def stopTimeOut(self):
        self.CounTimeOut_msg.CountTimeOut_ObjectStart = False
        # readTimeOut = pd.read_excel('เวลาที่เกินมา.xlsx')
        # Today = pd.to_datetime("today")
        # newDataframeTimeout = pd.DataFrame(
        #     {'วันที่':[Today],'Time Out': [self.CounTimeOut_msg.countTimeOut_time]}
        # )
        # frames = [readTimeOut, newDataframeTimeout]
        # result = pd.concat(frames)
        # writer = pd.ExcelWriter('เวลาที่เกินมา.xlsx', engine='xlsxwriter')
        # result.to_excel(writer, index=False)
        # writer.save()

        time.sleep(2)

        self.CounTimeOut_msg.countTimeOut_time=0
        self.lbCountTimeOut.setText(str("00:00:00"))

    def stopup(self):
        self.Countup_msg.countup_ObjectStart = False

    def StopDetec(self):
        self.Eyedetec_msg.Eyedetec_start = False
        self.Eyedetec_msg.eye_positiont = "Off"
        self.FacePosi.setText(str("TAKE A BREAK"))


        # self.FacePosi.setText("Off")

    def OpenTestForm(self):
        test = TestScript(self)
        test.resize(650 * 2, 800)
        test.show()

    # def closeEvent(self, event ):
    #    x= QMessageBox.question(self,"hello","ต้องการออกจากโปรแกรมใช่หรือไม่",QMessageBox.No,QMessageBox.Yes)
    #    if x == QMessageBox.Yes and self.CounTimeOut_msg.CountTimeOut_ObjectStart == False:
    #        if self.Countup_msg.countup_time > 0 :
    #            readEyeandTimeout = pd.read_excel(r'เวลาทั้งหมดและตาในแต่ละครั้ง.xlsx')
    #            today = pd.to_datetime("today")
    #            newDataframe = pd.DataFrame(
    #                 {'วันที่': [today],
    #                 'เวลาที่ใช้ทั้งหมด': [self.Countup_msg.countup_time],
    #                 'มองทางขวา':[self.Eyedetec_msg.CountEyeRight],
    #                 'มองตรงกลาง':[self.Eyedetec_msg.CountEyeCenter],
    #                 'มองทางซ้าย':[self.Eyedetec_msg.CountEyeLeft]})
    #            frames = [readEyeandTimeout, newDataframe]
    #            result = pd.concat(frames)
    #            writer = pd.ExcelWriter('เวลาทั้งหมดและตาในแต่ละครั้ง.xlsx', engine='xlsxwriter')
    #             # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
    #            result.to_excel(writer, index=False)
    #            writer.save()
    #            time.sleep(1)
    #
    #        event.ignore()
    #        QCoreApplication.quit()
    #    else:
    #        time.sleep(1)
    #        event.ignore()

    def close(self):
        QCoreApplication.quit()


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
