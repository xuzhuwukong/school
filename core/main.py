from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from urllib.parse import quote
from ui.login import Ui_MainWindow
from PyQt5 import QtWidgets
from ui.mainwindow import MainWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
