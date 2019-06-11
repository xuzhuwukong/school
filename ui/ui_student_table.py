# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTableView, QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox, \
    QListWidget, QListWidgetItem, QStatusBar, QMenuBar, QMenu, QAction, QLineEdit, QStyle, QFormLayout, QVBoxLayout, \
    QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QCursor
from PyQt5.QtCore import QStringListModel, QAbstractListModel, QModelIndex, QSize, Qt
import sys

class Ui_TableWindow(object):
    def setupUi(self, TableWindow):
        TableWindow.setObjectName("TableWindow")
        TableWindow.resize(470, 305)
        self.centralwidget = QtWidgets.QWidget(TableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows);  # 设置只有行选中
        ##
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '地址', '年龄', '工资'])
        # 横向标题排列，如果使用setVerticalHeaderLabels则是纵向排列标题
        items = [['JONES', 'Beijing', '23', 2300], ['SMITH', 'SHAngHai', '23', '3000'], ['ZY', 'Tianjin', '23', '2000'],
                 ['Smith', 'SJT', '22', '1030']]
        for i in range(len(items)):  # 注意上面列表中数字加单引号，否则下面不显示(或者下面str方法转化一下即可)
            item = items[i]
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(i, j, item)
        ##
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        TableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 18))
        self.menubar.setObjectName("menubar")
        TableWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableWindow)
        self.statusbar.setObjectName("statusbar")
        TableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TableWindow)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        _translate = QtCore.QCoreApplication.translate
        TableWindow.setWindowTitle(_translate("TableWindow", "MainWindow"))
        self.pushButton.setText(_translate("TableWindow", "PushButton"))
        self.pushButton_2.setText(_translate("TableWindow", "PushButton"))

