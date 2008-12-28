#MessageBox.py

import sys
from PyQt4 import QtGui


class MessageBox(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Maya SVN')

    def setMessage(self,msgText):
        self.msg = msgText

    def showMessageBox(self):
        msgBox = QtGui.QMessageBox.question(self, 'Maya SVN',
            self.msg, QtGui.QMessageBox.Ok)
        QtGui.QWidget.close(self)
