import time

from PySide2.QtCore import QRunnable

class Countup_msg:
    def __init__(self,countup_func):
        self.countup_ObjectStart= False
        self.countup_time= 0
        self.countUPFunc=countup_func

class countupThread(QRunnable):

    def __init__(self,msg:Countup_msg):
        super(countupThread,self).__init__()
        self.msg=msg

    def run(self):

        while self.msg.countup_time >= 0 and self.msg.countup_ObjectStart:
            self.msg.countUPFunc()
            time.sleep(1)