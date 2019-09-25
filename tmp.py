#tmp.py
from PySide2.QtWidgets import (QApplication, QMainWindow, QMenu, QMessageBox)
from PySide2.QtCore import Slot

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.setupHelpMenu()

    def setupHelpMenu(self):
        helpMenu = QMenu("&Help", self)
        self.menuBar().addMenu(helpMenu)
        helpMenu.addAction("&About", lambda:self.about())

    @Slot()
    def about(self):
        QMessageBox.about(self,"About", "I think this will work on Mac OSX professor!")

import sys

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
