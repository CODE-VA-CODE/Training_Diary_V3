# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interfaces\confirms\confirmDialog_weightSave.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Confirm_Weight_Save(object):
    def setupUi(self, Dialog_Confirm_Weight_Save):
        Dialog_Confirm_Weight_Save.setObjectName("Dialog_Confirm_Weight_Save")
        Dialog_Confirm_Weight_Save.resize(369, 110)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Confirm_Weight_Save)
        self.buttonBox.setGeometry(QtCore.QRect(190, 70, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog_Confirm_Weight_Save)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 349, 52))
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.weightSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.weightSpinBox.setProperty("value", 50)
        self.weightSpinBox.setObjectName("weightSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.weightSpinBox)

        self.retranslateUi(Dialog_Confirm_Weight_Save)
        self.buttonBox.accepted.connect(Dialog_Confirm_Weight_Save.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_Confirm_Weight_Save.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_Confirm_Weight_Save)

    def retranslateUi(self, Dialog_Confirm_Weight_Save):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Confirm_Weight_Save.setWindowTitle(_translate("Dialog_Confirm_Weight_Save", "Dialog"))
        self.label.setText(_translate("Dialog_Confirm_Weight_Save", "Укажите дату взвешивания:"))
        self.label_2.setText(_translate("Dialog_Confirm_Weight_Save", "Укажите вес:"))
