# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interfaces\confirms\confirmDialog_trainingSave.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Confirm_Training_Save(object):
    def setupUi(self, Dialog_Confirm_Training_Save):
        Dialog_Confirm_Training_Save.setObjectName("Dialog_Confirm_Training_Save")
        Dialog_Confirm_Training_Save.resize(369, 92)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Confirm_Training_Save)
        self.buttonBox.setGeometry(QtCore.QRect(190, 50, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog_Confirm_Training_Save)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 347, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)

        self.retranslateUi(Dialog_Confirm_Training_Save)
        self.buttonBox.accepted.connect(Dialog_Confirm_Training_Save.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Confirm_Training_Save.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Confirm_Training_Save)

    def retranslateUi(self, Dialog_Confirm_Training_Save):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Confirm_Training_Save.setWindowTitle(_translate("Dialog_Confirm_Training_Save", "Dialog"))
        self.label.setText(_translate("Dialog_Confirm_Training_Save", "Укажите дату тренировки:"))
