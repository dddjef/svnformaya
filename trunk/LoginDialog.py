import sys
from PyQt4 import QtCore, QtGui
from login_dialog import Ui_dlgLogin

class LoginDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_dlgLogin()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnOk,QtCore.SIGNAL("clicked()"), self.OKClicked)
        QtCore.QObject.connect(self.ui.btnCancel,QtCore.SIGNAL("clicked()"),QtGui.qApp, QtCore.SLOT("quit()"))
        self.center()
        self.username  = ""
        self.password = ""
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def OKClicked(self):
        self.username =  str(self.ui.txtUsername.text())
        self.password =  str(self.ui.txtPassword.text())
        QtGui.QWidget.close(self)
        
    def getLoginDetails(self):
        return self.username, self.password
