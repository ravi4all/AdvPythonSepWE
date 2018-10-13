from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql

connection = pymysql.connect(host = 'localhost',
                            port = 3306,
                            user = 'root',
                            db = 'testEngine_2',
                            autocommit = True)

cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1271, 761))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(350, 30, 581, 61))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 430, 361, 91))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 430, 361, 91))
        self.pushButton_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(110, 250, 251, 71))
        self.comboBox.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(840, 240, 251, 71))
        self.comboBox_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.register_frame = QtWidgets.QFrame(self.frame)
        self.register_frame.setGeometry(QtCore.QRect(0, 0, 1261, 751))
        self.register_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_frame.setObjectName("register_frame")
        self.label_2 = QtWidgets.QLabel(self.register_frame)
        self.label_2.setGeometry(QtCore.QRect(410, 60, 381, 71))
        self.label_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.register_frame)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 411, 51))
        self.label_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.register_frame)
        self.label_4.setGeometry(QtCore.QRect(150, 300, 411, 51))
        self.label_4.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.register_frame)
        self.label_5.setGeometry(QtCore.QRect(150, 410, 411, 51))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.register_frame)
        self.label_6.setGeometry(QtCore.QRect(150, 520, 411, 51))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.register_frame)
        self.lineEdit.setGeometry(QtCore.QRect(590, 190, 451, 61))
        self.lineEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.register_frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 290, 451, 61))
        self.lineEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.register_frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(590, 510, 451, 61))
        self.lineEdit_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.register_frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 650, 341, 61))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.register_frame)
        self.comboBox_3.setGeometry(QtCore.QRect(590, 400, 451, 71))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.login_frame = QtWidgets.QFrame(self.register_frame)
        self.login_frame.setGeometry(QtCore.QRect(0, 0, 1271, 751))
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.login_frame)
        self.label_7.setGeometry(QtCore.QRect(510, 50, 231, 71))
        self.label_7.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.login_frame)
        self.label_8.setGeometry(QtCore.QRect(180, 210, 251, 71))
        self.label_8.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.login_frame)
        self.label_9.setGeometry(QtCore.QRect(180, 350, 311, 71))
        self.label_9.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.login_frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(620, 210, 471, 71))
        self.lineEdit_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.login_frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(620, 350, 471, 71))
        self.lineEdit_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.login_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 530, 351, 81))
        self.pushButton_4.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.login_frame.hide()
        self.register_frame.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to Test Engine"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Student"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Student"))
        self.label_2.setText(_translate("MainWindow", "Registration Form"))
        self.label_3.setText(_translate("MainWindow", "Enter ID"))
        self.label_4.setText(_translate("MainWindow", "Enter Name"))
        self.label_5.setText(_translate("MainWindow", "Enter Department"))
        self.label_6.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "CS/IT"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "EC"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "ME"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "EE"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "EEE"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Civil"))
        self.label_7.setText(_translate("MainWindow", "Login Form"))
        self.label_8.setText(_translate("MainWindow", "Enter ID"))
        self.label_9.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Login"))

        self.pushButton_2.clicked.connect(self.showRegister)
        self.pushButton.clicked.connect(self.showLogin)
        self.pushButton_3.clicked.connect(self.registerUser)

    def showRegister(self):
        self.register_frame.show()
        # self.registerUser()

    def showLogin(self):
        self.register_frame.show()
        self.login_frame.show()
        # self.loginUser()

    def registerUser(self):
        try:
            user = self.comboBox_2.currentText()
            # print(user)
            user_id = self.lineEdit.text()
            user_name = self.lineEdit_2.text()
            user_course = self.comboBox_3.currentText()
            user_pwd = self.lineEdit_4.text()

            if user == 'Student':
                query = 'INSERT INTO students VALUES (%s, %s, %s, %s)'
            else:
                query = 'INSERT INTO teachers VALUES (%s, %s, %s, %s)'

            cursor.execute(query, (user_id, user_name, user_course, user_pwd))
            QMessageBox.about(self,"Success","Data Inserted Successfully...")

        except BaseException as ex:
            print(ex)

    def loginUser(self):
        try:
            user = self.comboBox_2.currentText()
            # print(user)
            user_id = self.lineEdit_3.text()
            user_pwd = self.lineEdit_5.text()

            if user == 'Student':
                query = 'SELECT * FROM students WHERE s_id = %s AND s_pwd = %s'
            else:
                query = 'SELECT * FROM teachers WHERE t_id = %s AND t_pwd = %s'

            cursor.execute(query, (user_id, user_pwd))

        except BaseException as ex:
            print(ex)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

