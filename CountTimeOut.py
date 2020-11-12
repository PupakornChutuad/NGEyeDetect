import time

from PySide2.QtCore import QRunnable, QSignalTransition, Signal, QObject


class CounTimeOut_msg:
    def __init__(self):
        self.CountTimeOut_ObjectStart = False
        self.countTimeOut_time = 0


class CounTimeOutSignel(QObject) :
    finished = Signal(str)
    updateCountTimeOut = Signal(str)
    timeout = Signal(str)

class countTimeOutThread(QRunnable):

    def __init__(self, msg: CounTimeOut_msg):
        super(countTimeOutThread, self).__init__()
        self.msg = msg

        self.signel = CounTimeOutSignel()

    def run(self):
        while self.msg.countTimeOut_time >= 0 and self.msg.CountTimeOut_ObjectStart:
            self.signel.updateCountTimeOut.emit("OK")
            time.sleep(1)

        if self.msg.countTimeOut_time == 0:
            self.signel.timeout.emit("OK")
            self.msg.CountTimeOut_ObjectStart = False
        self.msg.CountTimeOut_ObjectStart=False
        self.signel.finished.emit("OK")
        #     mins, secs = divmod(self.msg.countdown_time, 60)
        #     hour, mins = divmod(mins, 60)
        #     self.msg.countdownFunc = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        #     self.msg.countdown_time -= 1
        #     # self.msg.countdownFunc()
