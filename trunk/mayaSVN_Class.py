#Maya SVN Class
#mayaSVN_Class.py

#Maya Imports
import maya
import maya.utils as mu
import maya.cmds as cmds
import maya.mel
import pumpThread as pt
#PyQT4 Imports
from PyQt4 import QtCore, QtGui
from LoginDialog import LoginDialog
from MessageBox import MessageBox
#Other Imports
import pysvn
import sys
import time


class MayaSVN:
    #Class Contructor
    def __init__(self):
        #Setup Debugging Variables for outside of Maya
        self.maya_enabled = True
        #Setup Paths
        self.get_maya_project_path()
        svnPath = self.mayaProjectPath + "svn"
        #Setup pysvn
        self.client = pysvn.Client(svnPath)
        self.client.callback_get_login = self.get_login
        self.client.callback_ssl_server_trust_prompt = self.ssl_server_trust_prompt
        #Setup Message Box
        pt.initializePumpThread()
        app = QtGui.QApplication(sys.argv)
        self.msgBox = MessageBox()
        #Testing Variables
        self.svnURL = "https://192.168.0.22:8443/svn/Dalek/trunk/"

    #Get Project Path from Maya
    def get_maya_project_path(self):
        if(self.maya_enabled):
            self.mayaProjectPath = "E:\\MayaSVN\\testProject\\"
            #self.mayaProjectPath =  cmds.workspace(q=True,rd=True)
        else:
            self.mayaProjectPath = "E:\\MayaSVN\\testProject\\"
    
    #SVN Callbacks
    def get_login( self,realm, username, may_save):
        #Open Dialog ask for username & pass
        username, password = self.login_dialog()
        dialogRet = True
        return dialogRet, username, password, True

    def ssl_server_trust_prompt( self,trust_dict ):
        return True, 3, True

    #SVN Functions
    #Checkout project files from SVN
    def checkoutProject(self):
        #Open dialog for URL & Path
        url, path = self.checkout_dialog()
        #Perform SVN Checkout
        print "Started Checkout"
        self.client.checkout(url,path)
        print "Checkout Completed"
        self.msgBox.setMessage("SVN Checkout Completed")
        self.msgBox.showMessageBox()
        #Set Maya Project to path
        #

    #Perform an update of SVN Files
    def updateSVN(self):
        self.client.update(self.mayaProjectPath)
        print "SVN Update Completed"

    #Open file in Maya, SVN update & lock file
    def openFile(self,filename):
        #Update SVN before opening file
        filepath = self.mayaProjectPath + filename
        self.updateSVN()
        #Lock file on SVN so other users cant edit
        self.client.lock(filepath,'Maya Opened By user')
        #Open File in Maya
        #
        print "File Opened"

    #Save file commit to svn & unlock
    def saveFile(self, filename,comment):
        #Save & Close File in Maya
        #
        
        #Update SVN before saving file
        filepath = self.mayaProjectPath + filename
        self.updateSVN()
        #Work out whether this file is already under version control
        statusList = self.client.status(filepath)
        if(statusList):
            if(statusList[0].is_versioned == False):
                #Add New File to SVN
                self.client.add(filepath)
                print "New File Added to Repository"
            else:
                #Unlock so others may edit
                self.client.unlock(filepath)
            #Submit updated file to SVN
            self.client.checkin(filepath,comment)
            print "Check In Complete"
        else:
            print "Invalid File"

    #Import a Maya project into SVN
    def importProject(self):
        #Update Project Path Variable
        self.get_maya_project_path()
        #Import all project files into SVN
        url, path = self.import_dialog()
        self.client.import_(self.mayaProjectPath,url,'New Project Commit',recurse=True)
        print "Import Completed"

    #Dialogs
    #Dialog for login to SVN
    def login_dialog(self):
        global app
        if(self.maya_enabled):
            app = QtGui.QApplication(sys.argv)
            login = LoginDialog()
            login.show()
            time.sleep(0.02)
            app.exec_()
        return login.getLoginDetails()

    #Dialog for checkout from SVN - Asks for URL & Path
    def checkout_dialog(self):
        return self.svnURL,self.mayaProjectPath

    #Dialog for import into SVN - Asks for URL & Path
    def import_dialog(self):
        return self.svnURL,self.mayaProjectPath
