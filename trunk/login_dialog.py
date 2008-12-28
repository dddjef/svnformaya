# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created: Sun Dec 28 19:11:31 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgLogin(object):
    def setupUi(self, dlgLogin):
        dlgLogin.setObjectName("dlgLogin")
        dlgLogin.resize(391, 192)
        self.grpLogin = QtGui.QGroupBox(dlgLogin)
        self.grpLogin.setGeometry(QtCore.QRect(10, 10, 371, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.grpLogin.setFont(font)
        self.grpLogin.setObjectName("grpLogin")
        self.lblUsername = QtGui.QLabel(self.grpLogin)
        self.lblUsername.setGeometry(QtCore.QRect(20, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtGui.QLabel(self.grpLogin)
        self.lblPassword.setGeometry(QtCore.QRect(20, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.btnOk = QtGui.QPushButton(self.grpLogin)
        self.btnOk.setGeometry(QtCore.QRect(130, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnCancel = QtGui.QPushButton(self.grpLogin)
        self.btnCancel.setGeometry(QtCore.QRect(240, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.txtPassword = QtGui.QLineEdit(self.grpLogin)
        self.txtPassword.setGeometry(QtCore.QRect(130, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtUsername = QtGui.QLineEdit(self.grpLogin)
        self.txtUsername.setGeometry(QtCore.QRect(130, 40, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")

        self.retranslateUi(dlgLogin)
        QtCore.QMetaObject.connectSlotsByName(dlgLogin)
        dlgLogin.setTabOrder(self.txtUsername, self.txtPassword)
        dlgLogin.setTabOrder(self.txtPassword, self.btnOk)
        dlgLogin.setTabOrder(self.btnOk, self.btnCancel)

    def retranslateUi(self, dlgLogin):
        dlgLogin.setWindowTitle(QtGui.QApplication.translate("dlgLogin", "SVN Login", None, QtGui.QApplication.UnicodeUTF8))
        self.grpLogin.setTitle(QtGui.QApplication.translate("dlgLogin", "SVN Login Details", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUsername.setText(QtGui.QApplication.translate("dlgLogin", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPassword.setText(QtGui.QApplication.translate("dlgLogin", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("dlgLogin", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("dlgLogin", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

