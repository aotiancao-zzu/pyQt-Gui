# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        LoginDialog.setFont(font)
        self.usernamelabel = QtWidgets.QLabel(LoginDialog)
        self.usernamelabel.setGeometry(QtCore.QRect(120, 70, 72, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setObjectName("usernamelabel")
        self.usernamelineEdit = QtWidgets.QLineEdit(LoginDialog)
        self.usernamelineEdit.setGeometry(QtCore.QRect(200, 80, 113, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.usernamelineEdit.setFont(font)
        self.usernamelineEdit.setObjectName("usernamelineEdit")
        self.passwordlabel = QtWidgets.QLabel(LoginDialog)
        self.passwordlabel.setGeometry(QtCore.QRect(120, 140, 72, 21))
        self.passwordlabel.setObjectName("passwordlabel")
        self.passwordlineEdit = QtWidgets.QLineEdit(LoginDialog)
        self.passwordlineEdit.setGeometry(QtCore.QRect(200, 140, 113, 21))
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.loginpushButton = QtWidgets.QPushButton(LoginDialog)
        self.loginpushButton.setGeometry(QtCore.QRect(100, 200, 93, 28))
        self.loginpushButton.setObjectName("loginpushButton")
        self.registerpushButton = QtWidgets.QPushButton(LoginDialog)
        self.registerpushButton.setGeometry(QtCore.QRect(240, 200, 93, 28))
        self.registerpushButton.setObjectName("registerpushButton")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog"))
        self.usernamelabel.setText(_translate("LoginDialog", "账号："))
        self.passwordlabel.setText(_translate("LoginDialog", "密码："))
        self.loginpushButton.setText(_translate("LoginDialog", "登入"))
        self.registerpushButton.setText(_translate("LoginDialog", "注册"))
