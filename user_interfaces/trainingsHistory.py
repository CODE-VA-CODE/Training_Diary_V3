# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interfaces\trainingsHistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_History(object):
    def setupUi(self, MainWindow_History):
        MainWindow_History.setObjectName("MainWindow_History")
        MainWindow_History.setWindowModality(QtCore.Qt.NonModal)
        MainWindow_History.resize(478, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow_History)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 311, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(330, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")
        MainWindow_History.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_History)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_History.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_History)
        self.statusbar.setObjectName("statusbar")
        MainWindow_History.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_History)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_History)

    def retranslateUi(self, MainWindow_History):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_History.setWindowTitle(_translate("MainWindow_History", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_History", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_History", "Калории"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_History", "Упражнение"))
        self.btnClose.setText(_translate("MainWindow_History", "Закрыть окно"))
