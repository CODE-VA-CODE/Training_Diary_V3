import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QDialog, QTableWidgetItem

from table import traingsHistoryTable, changeUserTable, userChanged, setNewUser, delUser, tableDataEdit, \
    setNewTraining, setNewWeight, weightHistoryTable
from user_interfaces.mainForm import Ui_MainWindow
from user_interfaces.startTrainingDialog import Ui_Dialog_start_training
from user_interfaces.userDataDialog import Ui_Dialog_Data
from user_interfaces.setup import Ui_Dialog_Setup
from user_interfaces.trainingsHistory import Ui_MainWindow_History
from user_interfaces.userChangeDialog import Ui_Dialog_User_Change

from confirmDialogs import confirmDialogUserDel, confirmDialogUserNoneId, confirmDialogUserEdit, \
    confirmDialogTrainingSave, confirmDialogWeightSave
from confirmDialogs import confirmDialogUserName

LOGO = "logo.png"


class startDialogClass(QDialog, Ui_Dialog_Setup):
    def __init__(self, parent=None):
        super(startDialogClass, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Начать")
        self.closeTrigger = False
        self.btnOk.clicked.connect(self.accept)


class mainWindowClass(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.inintUI()
        self.mainFunc()

    def inintUI(self):
        self.vars()
        self.setupUi(self)
        self.setFixedHeight(494)
        self.setFixedWidth(661)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Дневник тренировок")
        self.trainingWidget.hide()
        self.btnHistory.clicked.connect(self.trainingsHistory)
        self.btnUserChange.clicked.connect(self.userFunc)
        self.btnDataReset.clicked.connect(self.resetData)
        self.btnUserEdit.clicked.connect(self.userEditFunc)
        self.btnStartTraining.clicked.connect(self.startTraining)
        self.btnWeightEdit.clicked.connect(self.weightEdit)
        self.btnWeightHistory.clicked.connect(self.weightHistory)
        self.dataFileCheck()

    def vars(self):
        self.userDataFile = "UserData.txt"
        self.userName = "None"
        self.userWeight = "1"
        self.userHeight = "1"
        self.userAge = "18"

    def userFunc(self):
        self.dialog = userChangeDialog()
        self.dialog.exec()
        if(self.dialog.result() == 0):
            self.dialog = dataDialog()
            self.dialog.exec()
            if(self.dialog.resultat == 1):
                self.userFunc()
            if(self.dialog.result() == 0 and self.userName != ""):
                return
            try:
                while (self.dialog.userNameEdit.text() == ""):
                    self.confirmDailog = confirmDialogUserName()
                    self.confirmDailog.exec()
                    self.dialog.exec()
                setNewUser(self.dialog.userNameEdit.text(), int(self.dialog.userWeightEdit.text()),
                           int(self.dialog.userHeightEdit.text()), int(self.dialog.userAgeEdit.text()))

                self.userName = self.dialog.userNameEdit.text()
                self.userWeight = self.dialog.userWeightEdit.text()
                self.userHeight = self.dialog.userHeightEdit.text()
                self.userAge = self.dialog.userAgeEdit.text()
            except:
                pass
        else:
            self.userChangeFromTable()
            self.userName = self.userDataList[0]  # ['Андрей', 15, 64, 178]
            self.userWeight = self.userDataList[2]
            self.userHeight = self.userDataList[3]
            self.userAge = self.userDataList[1]
        with open(self.userDataFile, "w", encoding='utf-8') as f:
            print("True", self.userName, self.userHeight, self.userWeight, self.userAge, sep="\n", file=f)
        self.mainFunc()

    def dataFileCheck(self):
        with open(self.userDataFile, mode="r", encoding="utf8") as dataFile:
            read = dataFile.readline()
            if(read[:4] != "True"):
                self.dialog = startDialogClass()
                self.dialog.exec()
                self.userFunc()
            else:
                read = dataFile.read().strip().split("\n")
                self.userName = read[0]
                self.userWeight = read[2]
                self.userHeight = read[1]
                self.userAge = read[3]

    def mainFunc(self):
        self.heightLabel.setText(str(self.userHeight))
        self.weightLabel.setText(str(self.userWeight))
        self.nameLabel.setText(self.userName)
        self.ageLabel.setText(str(self.userAge))
        self.bmi = "%.2f" % (int(self.userWeight) / ((int(self.userHeight) / 100) ** 2))
        if(float(self.bmi) <= 18.5):
            self.bmi += " > Малый вес"
        elif(float(self.bmi) <= 25):
            self.bmi += " > Ок"
        else:
            self.bmi += " > Избыточный вес"

        self.bmiLabel.setText(self.bmi)

    def trainingsHistory(self):
        trainigsHistoryWid.userName = self.userName
        self.historyWid = trainigsHistoryWid()
        self.historyWid.show()

    def userChangeFromTable(self):
        try:
            self.userDataList = list(userChanged(int(self.dialog.userIdSpinBox.text()))[0])
        except:
            self.dialog = confirmDialogUserNoneId()
            self.dialog.exec()
            self.userFunc()

    def resetData(self):
        self.dialog = confirmDialogUserDel()
        self.dialog.exec()
        if(self.dialog.result() == 1):
            delUser(self.userName)
            self.userFunc()

    def userEditFunc(self):
        self.dialog = confirmDialogUserEdit()
        self.dialog.exec()
        if(self.dialog.result() == 1):
            oldName = self.userName
            self.userName = self.dialog.userNameEdit.text()
            self.userAge = self.dialog.userAgeEdit.text()
            tableDataEdit(oldName, self.userName, self.userAge)
            with open(self.userDataFile, "w", encoding='utf-8') as f:
                print("True", self.userName, self.userHeight, self.userWeight, self.userAge, sep="\n", file=f)
            self.mainFunc()

    def startTraining(self):
        self.dialog = startTrainingDialog()
        self.dialog.exec()
        if(self.dialog.result() == 1):
            self.trainingType = self.dialog.trainingType.currentText()
            self.exSet = self.dialog.spinBoxAppr.text()
            self.exers = self.dialog.spinBoxExcer.text()
            self.training()

    def training(self):
        self.exercDataLabel.setText(self.trainingType)
        self.apprDataLabel.setText(self.exSet)
        self.exercInApprDataLabel.setText(self.exers)
        self.trainingWidget.show()
        self.btnEndTraining.clicked.connect(self.trainingEnd)

    def trainingEnd(self):
        self.dialog = confirmDialogTrainingSave()
        self.dialog.exec()
        if(self.dialog.result() == 1):
            dateTime = self.dialog.dateTimeEdit.text()
            setNewTraining(dateTime, self.userName, self.trainingType, self.exers, self.exSet)
            self.trainingWidget.hide()

    def weightEdit(self):
        self.dialog = confirmDialogWeightSave()
        self.dialog.exec()
        if (self.dialog.result() == 1):
            dateTime = self.dialog.dateTimeEdit.text()
            self.userWeight = self.dialog.weightSpinBox.text()
            setNewWeight(dateTime, self.userWeight, self.userName)
            self.mainFunc()

    def weightHistory(self):
        weightHistoryWid.userName = self.userName
        self.historyWid = weightHistoryWid()
        self.historyWid.show()


class startTrainingDialog(QDialog, Ui_Dialog_start_training):
    def __init__(self, parent=None):
        super(startTrainingDialog, self).__init__(parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Начать тренировку")


class trainigsHistoryWid(QMainWindow, Ui_MainWindow_History):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.userName = None

    def initUi(self):
        self.setupUi(self)
        self.setWindowTitle("История тренировок")
        self.setWindowIcon(QIcon(LOGO))
        self.btnClose.clicked.connect(self.closing)
        self.historyTableInit()

    def historyTableInit(self):
        res = traingsHistoryTable(self.userName)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closing(self):
        self.close()

    class trainigsHistoryWid(QMainWindow, Ui_MainWindow_History):
        def __init__(self):
            super().__init__()
            self.initUi()
            self.userName = None

        def initUi(self):
            self.setupUi(self)
            self.setWindowTitle("История тренировок")
            self.setWindowIcon(QIcon(LOGO))
            self.btnClose.clicked.connect(self.closing)
            self.historyTableInit()

        def historyTableInit(self):
            res = traingsHistoryTable(self.userName)
            for i, row in enumerate(res):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))

        def closing(self):
            self.close()


class weightHistoryWid(QMainWindow, Ui_MainWindow_History):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.userName = None

    def initUi(self):
        self.setupUi(self)
        self.setWindowTitle("История взвешиваний")
        self.setWindowIcon(QIcon(LOGO))
        self.btnClose.clicked.connect(self.closing)
        self.historyTableInit()

    def historyTableInit(self):
        res = weightHistoryTable(self.userName)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closing(self):
        self.close()


class dataDialog(QDialog, Ui_Dialog_Data):
    def __init__(self, parent=None):
        super(dataDialog, self).__init__(parent)
        self.resultat = 0
        self.parent = parent
        self.initUi()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Введите данные")
        self.btnChangeUser.clicked.connect(self.changeUser)

    def changeUser(self):
        self.resultat = 1
        self.close()


class userChangeDialog(QDialog, Ui_Dialog_User_Change):
    def __init__(self, parent=None):
        super(userChangeDialog, self).__init__(parent)
        self.parent = parent
        self.initUi()
        self.usersTableInit()

    def initUi(self):
        # uic.loadUi("mainForm.ui", self)
        self.setupUi(self)
        self.setModal(True)
        self.btnNewUser.clicked.connect(self.reject)
        self.btnTableChange.clicked.connect(self.accept)
        self.setWindowIcon(QIcon(LOGO))
        self.setWindowTitle("Выберите пользователя")

    def usersTableInit(self):
        res = changeUserTable()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainWindowClass()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
