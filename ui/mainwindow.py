import collections
from PyQt5 import QtWidgets, QtCore, QtGui
from ui.ui_student_table import Ui_TableWindow

class MainWindow(QtWidgets.QMainWindow, Ui_TableWindow):

    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
