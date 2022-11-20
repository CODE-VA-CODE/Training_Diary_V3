from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from user_interfaces.confirms.confirmDialog_trainingSave import Ui_Dialog_Confirm_Training_Save
from user_interfaces.confirms.confirmDialog_userDel import Ui_Dialog_Confirm_User_Del
from user_interfaces.confirms.confirmDialog_userEdit import Ui_Dialog_Confirm_User_Edit
from user_interfaces.confirms.confirmDialog_userName import Ui_Dialog_User_Name
from user_interfaces.confirms.confirmDialog_userNoneId import Ui_Dialog_User_None_Id
from user_interfaces.confirms.confirmDialog_weightSave import Ui_Dialog_Confirm_Weight_Save

LOGO = "logo.png"

# pyuic5 user_interfaces\x.ui -o user_interfaces\x.py
class confirmDialogUserDel(QDialog, Ui_Dialog_Confirm_User_Del):
    def __init__(self, parent=None):
        super(confirmDialogUserDel, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Подтверждение")


class confirmDialogUserName(QDialog, Ui_Dialog_User_Name):
    def __init__(self, parent=None):
        super(confirmDialogUserName, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Ошибка")


class confirmDialogUserNoneId(QDialog, Ui_Dialog_User_None_Id):
    def __init__(self, parent=None):
        super(confirmDialogUserNoneId, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Ошибка")

class confirmDialogUserEdit(QDialog, Ui_Dialog_Confirm_User_Edit):
    def __init__(self, parent=None):
        super(confirmDialogUserEdit, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Редактирование")

class confirmDialogTrainingSave(QDialog, Ui_Dialog_Confirm_Training_Save):
    def __init__(self, parent=None):
        super(confirmDialogTrainingSave, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Сохранение")

class confirmDialogWeightSave(QDialog, Ui_Dialog_Confirm_Weight_Save):
    def __init__(self, parent=None):
        super(confirmDialogWeightSave, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Сохранение")
