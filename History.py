# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class History_View(QMainWindow):
    def __init__(self,parent=None):
        super(History_View, self).__init__(parent)
        self.load_ui()

        self.Close_btn: QPushButton = self.findChild(QPushButton,"Close_btn")

        self.Pointper_mount: QLabel = self.findChild(QLabel, "Pointper_mount")
        self.Hourper_week: QLabel = self.findChild(QLabel, "Hourper_week")
        self.Hourover_week: QLabel = self.findChild(QLabel, "Hourover_week")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "History.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = History_View()
    widget.show()
    sys.exit(app.exec_())
