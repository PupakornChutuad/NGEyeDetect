import time

from PySide2.QtCore import QRunnable, QSignalTransition, Signal, QObject


class Countup_msg:
    def __init__(self):
        self.countup_ObjectStart = False
        self.countup_time = 0


class CountupSignel(QObject):
    finished = Signal(str)
    updateCountup = Signal(str)


class CountupThread(QRunnable):
    def __init__(self, msg: Countup_msg):
        super(CountupThread, self).__init__()
        self.msg = msg

        self.signel = CountupSignel()

    def run(self):
        while self.msg.countup_time >= 0 and self.msg.countup_ObjectStart:
            self.signel.updateCountup.emit("OK")
            time.sleep(1)

        self.signel.finished.emit("OK")
