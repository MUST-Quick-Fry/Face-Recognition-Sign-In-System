from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UI.utils import MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setMinimumSize(951,522)
    window.setMaximumSize(951,522)
    window.show()
    app.exec_()

    sys.exit(0)