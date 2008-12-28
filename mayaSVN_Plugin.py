#mayaSVN_Plugin.py

from mayaSVN_Class import MayaSVN
import maya
import maya.mel as mel
import maya.cmds as cmds

#Maya Plugin Code
def initializePlugin(argument = "MayaSVN"):
    global svn
    svn = MayaSVN()
    setupMenus()
    print "MayaSVN plug-in loaded"

def uninitializePlugin(argument = "MayaSVN"):
    unloadMenus()
    print "MayaSVN plug-in unloaded"

#Maya Menus
def setupMenus():
    gMainWindow = mel.eval('$temp1=$gMainWindow')
    cmds.menuItem("openProject",command=OpenProject,edit=True)
    #Add Project Checkout Option
    try:
        cmds.menuItem("svnCheckout",parent="mainFileMenu",label='Checkout Project from SVN',command=CheckoutProject,ia="projectItems")
    except RuntimeError:
        cmds.menuItem("svnCheckout",parent="mainFileMenu",label='Checkout Project from SVN',command=CheckoutProject,ia="projectItems",edit=True) 

def unloadMenus():
    gMainWindow = mel.eval('$temp1=$gMainWindow')
    #Issues with setting Open command back
    cmds.menuItem("openProject",command="OpenScene",edit=True)
    cmds.deleteUI("svnCheckout")

#Menu Functions
def OpenProject(self):
    print "Open Scene"

def CheckoutProject(self):
    print "Checking Out"
    svn.checkoutProject()


