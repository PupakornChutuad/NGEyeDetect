# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton,QSpinBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class TestScript(QWidget):
    def __init__(self):
        super(TestScript, self).__init__()
        self.load_ui()

        self.btnSubmitTest: QPushButton = self.findChild(QPushButton,"btnSubmitTest")
        self.radio10: QRadioButton = self.findChild(QRadioButton,"radio10")
        self.radio11: QRadioButton = self.findChild(QRadioButton, "radio11")
        self.radio12: QRadioButton = self.findChild(QRadioButton, "radio12")
        self.radio13: QRadioButton = self.findChild(QRadioButton, "radio13")
        self.radio14: QRadioButton = self.findChild(QRadioButton, "radio14")
        self.radio15: QRadioButton = self.findChild(QRadioButton, "radio15")
        self.radio16: QRadioButton = self.findChild(QRadioButton, "radio16")
        self.radio17: QRadioButton = self.findChild(QRadioButton, "radio17")
        self.radio18: QRadioButton = self.findChild(QRadioButton, "radio18")
        self.radio19: QRadioButton = self.findChild(QRadioButton, "radio19")
        self.radio110: QRadioButton = self.findChild(QRadioButton, "radio110")
        self.radio20: QRadioButton = self.findChild(QRadioButton, "radio20")
        self.radio21: QRadioButton = self.findChild(QRadioButton, "radio21")
        self.radio22: QRadioButton = self.findChild(QRadioButton, "radio22")
        self.radio23: QRadioButton = self.findChild(QRadioButton, "radio23")
        self.radio24: QRadioButton = self.findChild(QRadioButton, "radio24")
        self.radio25: QRadioButton = self.findChild(QRadioButton, "radio25")
        self.radio26: QRadioButton = self.findChild(QRadioButton, "radio26")
        self.radio27: QRadioButton = self.findChild(QRadioButton, "radio27")
        self.radio28: QRadioButton = self.findChild(QRadioButton, "radio28")
        self.radio29: QRadioButton = self.findChild(QRadioButton, "radio29")
        self.radio210: QRadioButton = self.findChild(QRadioButton, "radio210")
        self.radio30: QRadioButton = self.findChild(QRadioButton, "radio30")
        self.radio31: QRadioButton = self.findChild(QRadioButton, "radio31")
        self.radio32: QRadioButton = self.findChild(QRadioButton, "radio32")
        self.radio33: QRadioButton = self.findChild(QRadioButton, "radio33")
        self.radio34: QRadioButton = self.findChild(QRadioButton, "radio34")
        self.radio35: QRadioButton = self.findChild(QRadioButton, "radio35")
        self.radio36: QRadioButton = self.findChild(QRadioButton, "radio36")

        self.radio60: QRadioButton = self.findChild(QRadioButton, "radio30")
        self.radio61: QRadioButton = self.findChild(QRadioButton, "radio31")
        self.radio62: QRadioButton = self.findChild(QRadioButton, "radio32")
        self.radio63: QRadioButton = self.findChild(QRadioButton, "radio33")
        self.radio64: QRadioButton = self.findChild(QRadioButton, "radio34")
        self.radio65: QRadioButton = self.findChild(QRadioButton, "radio35")
        self.radio66: QRadioButton = self.findChild(QRadioButton, "radio36")

        self.btnSubmitTest.clicked.connect(self.radioanswer)
        self.radio60.clicked.connect(self.radioanswer)
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "Test_form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


    def radioanswer(self):
        p = self.sender()

        print(p)


if __name__ == "__main__":
    app = QApplication([])
    widget = TestScript()
    widget.show()
    sys.exit(app.exec_())