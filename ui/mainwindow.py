import collections
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.login import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
