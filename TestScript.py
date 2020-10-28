# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class TestScript(QWidget):
    def __init__(self):
        super(TestScript, self).__init__()
        self.load_ui()

        self.btnSubmitTest: QPushButton = self.findChild(QPushButton,"btnSubmitTest")
        self.comboBox_1: QComboBox = self.findChild(QComboBox, "comboBox_1")
        self.comboBox_2: QComboBox = self.findChild(QComboBox, "comboBox_2")
        self.comboBox_3: QComboBox = self.findChild(QComboBox, "comboBox_3")
        self.comboBox_4: QComboBox = self.findChild(QComboBox, "comboBox_4")
        self.comboBox_5: QComboBox = self.findChild(QComboBox, "comboBox_5")
        self.comboBox_6: QComboBox = self.findChild(QComboBox, "comboBox_6")


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
                or self.comboBox_5.currentText() == "---------"\
                or self.comboBox_6.currentText() == "---------":
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
            avg1 = (c1 + c2 + c3 + c4 + c5 + c6 ) / 6
            if avg1 >= 5.1:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหามาก")
                msg.setIcon(QMessageBox.Warning)
            elif avg1 <= 5 and avg1 >= 1.1:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหาปานกลาง")
                msg.setIcon(QMessageBox.Warning)
            elif avg1 <= 1 and avg1 >= 0.1:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณอยู่ในระดับที่มีปัญหาเล็กน้อย")
                msg.setIcon(QMessageBox.Warning)
            else:
                msg.setText("คุณได้คะแนน " + str(avg1) + " ตอนนี้คุณไม่พบปัญหาใดๆ")
                msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Close)
            x = msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    widget = TestScript()
    widget.show()
    sys.exit(app.exec_())