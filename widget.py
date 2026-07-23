import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

import recieve
import send
from PyQt6.QtGui import QPixmap, QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 597)
        Form.setStyleSheet("#Form{border-image:url(background.png)}")
        Form.setWindowIcon(QIcon('logo.jpg'))
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 861, 631))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
                                     "    background-color: #e4ecf5;\n"
                                     "    font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                     "    font-size:11pt;\n"
                                     "    color:black;    /*设置tab中的文本的颜色*/\n"
                                     "    border-top-left-radius: 5px;    /*设置tab的边框的圆角（左上圆角）*/\n"
                                     "    border-top-right-radius: 5px;    /*设置tab的边框的圆角（右上圆角）*/\n"
                                     "    min-width: 13px;\n"
                                     "    padding-top: 7px;\n"
                                     "    padding-bottom: 7px;\n"
                                     "    padding-left: 16px;\n"
                                     "    padding-right: 16px;\n"
                                     "}\n"
                                     " \n"
                                     "/*设置TabWidget中QTabBar的tab被选中时的样式*/\n"
                                     "QTabBar::tab:selected{\n"
                                     "    background-color: #9fbcde;\n"
                                     "}\n"
                                     " \n"
                                     "/*设置TabWidget中鼠标悬浮在QTabBar的tab上，但未选中该Tab的样式*/\n"
                                     "QTabBar::tab:hover:!selected {\n"
                                     "    background-color: #9fbcde;\n"
                                     "}\n"
                                     " \n"
                                     "/*设置TabWidget的边框的样式*/\n"
                                     "QTabWidget::pane {\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(19, 19))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("background-color:#e4ecf5")
        self.tab_1.setObjectName("tab_1")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 871, 41))
        self.label_2.setStyleSheet("background-color:#9fbcde")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.tab_1)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 681, 31))
        self.lineEdit.setStyleSheet("background-color:white;\n"
                                    "border:1px solid #F2F2F2")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 54, 16))
        self.label_4.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.tab_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 110, 681, 31))
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
                                      "border:1px solid #F2F2F2")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(40, 120, 54, 16))
        self.label_5.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(40, 170, 54, 16))
        self.label_6.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 160, 681, 31))
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
                                      "border:1px solid #F2F2F2")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 54, 16))
        self.label_7.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(parent=self.tab_1)
        self.textEdit.setGeometry(QtCore.QRect(120, 220, 681, 271))
        self.textEdit.setStyleSheet("background-color:white;\n"
                                    "border:1px solid #F2F2F2")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 24))
        self.pushButton.setStyleSheet("font-family:Consolas;  \n"
                                      "font-size:13px;\n"
                                      "border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sendFunction)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color:#e4ecf5")
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 881, 41))
        self.label_3.setStyleSheet("background-color:#9fbcde")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 75, 24))
        self.pushButton_2.setStyleSheet("font-family:Consolas;  \n"
                                        "font-size:13px;\n"
                                        "border-radius: 5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getFunction)

        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(40, 60, 61, 31))
        self.label_8.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(410, 60, 61, 31))
        self.label_9.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                   "font-size:13px")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 60, 351, 31))
        self.lineEdit_4.setStyleSheet("background-color:white;\n"
                                      "border:1px solid #F2F2F2")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(120, 60, 61, 31))
        self.label_11.setStyleSheet("font-family:Consolas;    /*设置tab中的文本的字体*/\n"
                                    "font-size:13px")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(50, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:white")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(50, 160, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:white")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(50, 190, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:white")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(50, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:white")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(50, 250, 741, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:white;\n"
                                    "")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 120, 801, 361))
        self.label_16.setStyleSheet("background-color:white")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.line = QtWidgets.QFrame(parent=self.tab_2)
        self.line.setGeometry(QtCore.QRect(40, 236, 781, 20))
        self.line.setStyleSheet("background-color:white;\n"
                                "color:#e4ecf5")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_16.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.lineEdit_4.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_12.raise_()
        self.label_10.raise_()
        self.label_13.raise_()
        self.line.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(390, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "简易邮件系统"))
        self.label_4.setText(_translate("Form", "发件人"))
        self.label_5.setText(_translate("Form", "收件人"))
        self.label_6.setText(_translate("Form", "主题"))
        self.label_7.setText(_translate("Form", "正文"))
        self.pushButton.setText(_translate("Form", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "写信"))
        self.pushButton_2.setText(_translate("Form", "接收"))
        self.label_8.setText(_translate("Form", "总邮件数"))
        self.label_9.setText(_translate("Form", "接收序号"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "收信"))
        self.label.setText(_translate("Form", "Welcome!"))
        self.lineEdit.setPlaceholderText("1804817170@qq.com")

    def sendFunction(self):
        toAddress = self.lineEdit_2.text()
        subject = self.lineEdit_3.text()
        msg = self.textEdit.toPlainText()
        print(toAddress,subject,msg)
        send.sendData(subject,msg,toAddress)

    def getFunction(self):
        _translate = QtCore.QCoreApplication.translate
        j=self.lineEdit_4.text()
        lists,content=recieve.getEmail(int(j))
        self.label_11.setText(_translate("Form", str(len(lists))+'封'))
        self.label_10.setText(_translate("Form", content[3]))
        self.label_12.setText(_translate("Form", content[0]))
        self.label_13.setText(_translate("Form", content[1]))
        self.label_14.setText(_translate("Form", content[2]))
        self.label_15.setText(_translate("Form", content[4]))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())