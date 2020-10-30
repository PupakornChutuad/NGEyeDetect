import time

from PySide2.QtCore import QRunnable, QSignalTransition, Signal, QObject


class Coundown_msg:
    def __init__(self):
        self.CountDown_ObjectStart = False
        self.countdown_time = 10


class CoundownSignel(QObject) :
    finished = Signal(str)
    updateCountdown = Signal(str)


class countdownThread(QRunnable):

    def __init__(self, msg: Coundown_msg):
        super(countdownThread, self).__init__()
        self.msg = msg

        self.signel = CoundownSignel()

    def run(self):
        while self.msg.countdown_time > 0 and self.msg.CountDown_ObjectStart:
            self.signel.updateCountdown.emit("OK")
            time.sleep(1)
        self.msg.CountDown_ObjectStart=False
        self.signel.finished.emit("OK")
        #     mins, secs = divmod(self.msg.countdown_time, 60)
        #     hour, mins = divmod(mins, 60)
        #     self.msg.countdownFunc = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)

        #     self.msg.countdown_time -= 1
        #     # self.msg.countdownFunc()
