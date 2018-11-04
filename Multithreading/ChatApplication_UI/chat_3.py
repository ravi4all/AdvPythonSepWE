from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):

    users = ['Ram', 'Shyam', 'BMPL', 'Amit', 'Akash']

    chatData = [
        {
            "Ram" : [{'msg':'hello'},
                     {'rply':'hey'},
                     {'msg':'hi'},
                     {'msg':'what is python'},
                     {'rply':'programming'},
                     {'msg':'nice'},
                     {'rply':'yup'},
                     {'rply':'where are you ?'},
                     {'rply':'take care'},
                     {'msg':'delhi'},
                     {'msg' : 'lets meet'},
                     {'rply':'nope'},
                     {'rply':'very busy'},
                     {'msg' :'ok'},
                     {'rply':'yes'}
                     ],
        }
    ]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 401, 741))
        self.listWidget.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)

        for i in range(len(self.users)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 10, 801, 521))
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setObjectName("frame")

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(455, 15, 800, 520))
        self.listWidget_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget_2.setObjectName("listWidget")

        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(450, 10, 801, 521))
        # self.textEdit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        # self.textEdit.setObjectName("textEdit")
        # self.textEdit.setAlignment(QtCore.Qt.AlignLeft)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 560, 801, 107))
        self.textEdit_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 690, 351, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textEdit_2.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("MainWindow", "User_1"))
        # item = self.listWidget.item(1)
        # item.setText(_translate("MainWindow", "User_2"))
        # item = self.listWidget.item(2)
        # item.setText(_translate("MainWindow", "User_3"))

        for i in range(len(self.users)):
            item = self.listWidget.item(i)
            item.setText(_translate("MainWindow", self.users[i]))

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton.clicked.connect(self.sendMessage)

        # self.listWidget.itemClicked(self.listWidget.clicked)
        self.listWidget.itemClicked.connect(self.changeUser)

    def changeUser(self, item):
        # print(item.text())
        self.textEdit_2.setReadOnly(False)
        self.userName = item.text()
        self.conversation()

    def sendMessage(self):
        user = 'rply'
        for data in self.chatData:
            for key in data.keys():
                if key == self.userName:
                    # print(data[key])
                    if user == 'rply':
                        chat = {'rply':self.textEdit_2.toPlainText()}
                        data[key].append(chat)
                    print(data[key])
        self.conversation()

    def conversation(self):
        # self.textEdit.setText("")
        for data in self.chatData:
            for key in data.keys():
                if key == self.userName:
                    # print(data[userName])
                    chat = data[self.userName]
                    for i in range(len(chat)):
                        item = QtWidgets.QListWidgetItem()
                        self.listWidget_2.addItem(item)
                        item = self.listWidget_2.item(i)

                        for k in chat[i].keys():
                            if k == 'msg':
                                item.setText(chat[i][k])
                                item.setTextAlignment(QtCore.Qt.AlignLeft)
                            else:
                                item.setText(chat[i][k])
                                item.setTextAlignment(QtCore.Qt.AlignRight)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())