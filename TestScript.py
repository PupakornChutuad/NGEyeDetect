# This Python file uses the following encoding: utf-8
import sys
import os
import pandas as pd
import datetime

from PyQt5.QtWidgets import QMainWindow
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QMessageBox, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class TestScript(QMainWindow):
    def __init__(self,parent=None):
        super(TestScript, self).__init__(parent)
        self.load_ui()


        self.btnSubmitTest: QPushButton = self.findChild(QPushButton,"btnSubmitTest")
        self.comboBox_1: QComboBox = self.findChild(QComboBox, "comboBox_1")
        self.comboBox_2: QComboBox = self.findChild(QComboBox, "comboBox_2")
        self.comboBox_3: QComboBox = self.findChild(QComboBox, "comboBox_3")
        self.comboBox_4: QComboBox = self.findChild(QComboBox, "comboBox_4")
        self.comboBox_5: QComboBox = self.findChild(QComboBox, "comboBox_5")
        self.comboBox_6: QComboBox = self.findChild(QComboBox, "comboBox_6")
        self.comboBox_7: QComboBox = self.findChild(QComboBox, "comboBox_7")
        self.comboBox_8: QComboBox = self.findChild(QComboBox, "comboBox_8")
        self.comboBox_9: QComboBox = self.findChild(QComboBox, "comboBox_9")
        self.comboBox_10: QComboBox = self.findChild(QComboBox, "comboBox_10")


        self.btnSubmitTest.clicked.connect(self.radioanswer)

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "Test_form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


    def radioanswer(self):


        msg = QMessageBox()
        if self.comboBox_1.currentText() == "---------" \
                or self.comboBox_2.currentText() == "---------" \
                or self.comboBox_3.currentText() == "---------" \
                or self.comboBox_4.currentText() == "---------" \
                or self.comboBox_5.currentText() == "---------" \
                or self.comboBox_6.currentText() == "---------" \
                or self.comboBox_7.currentText() == "---------" \
                or self.comboBox_8.currentText() == "---------" \
                or self.comboBox_9.currentText() == "---------" \
                or self.comboBox_10.currentText() == "---------":
            msg.setText("กรุณากรอกข้อมูลให้ครบ")
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Close)
            x=msg.exec_()
        else:
            c1 = int(self.comboBox_1.currentText())
            c2 = int(self.comboBox_2.currentText())
            c3 = int(self.comboBox_3.currentText())
            c4 = int(self.comboBox_4.currentText())
            c5 = int(self.comboBox_5.currentText())
            c6 = int(self.comboBox_6.currentText())
            c7 = int(self.comboBox_7.currentText())
            c8 = int(self.comboBox_8.currentText())
            c9 = int(self.comboBox_9.currentText())
            c10 = int(self.comboBox_10.currentText())
            avg1 = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10) / 10

            readDataframe = pd.read_excel(r'คะแนนแบบทดสอบสุขภาพสายตา.xlsx')
            today = pd.to_datetime("today")

            newDataframe = pd.DataFrame({'วันที่': [today], 'คะแนน': [avg1]})
            frames = [readDataframe, newDataframe]
            result = pd.concat(frames)
            writer = pd.ExcelWriter('คะแนนแบบทดสอบสุขภาพสายตา.xlsx', engine='xlsxwriter')

            # นำข้อมูลชุดใหม่เขียนลงไฟล์และจบการทำงาน
            result.to_excel(writer, index=False)
            writer.save()


            if avg1 >= 7.5:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหามาก")
                msg.setIcon(QMessageBox.Warning)
            elif avg1 <= 7.4 and avg1 >= 5:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหาปานกลาง")
                msg.setIcon(QMessageBox.Warning)
            elif avg1 <= 4.9 and avg1 >= 2.5:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหาเล็กน้อย")
                msg.setIcon(QMessageBox.Warning)
            else:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณไม่พบปัญหาใดๆ")
                msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Close)
            x = msg.exec_()
            # if msg == QMessageBox.Close :
            self.close()
            from main import MainWin
            MainWin.close(self)


if __name__ == "__main__":
    app = QApplication([])
    widget = TestScript()
    widget.show()
    sys.exit(app.exec_())