from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from os import listdir,getcwd,remove,mkdir
from time import sleep
from shutil import rmtree

from files.apps.sdk.sdk import *

standardSegs = ["Clock","Battery","CPU Usage","Available Memory"]

class settingsWidget(QWidget):
    def __init__(self):
        super(settingsWidget, self).__init__()

        self.setFixedSize(450, 540)
        self.setWindowTitle(u"AOS-GUI/settings")
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.tabs = QTabWidget(self)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 10, 431, 521))
        self.tabs.setMovable(False)
        self.general = QWidget()
        self.general.setObjectName(u"general")
        self.user = QGroupBox(self.general)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(10, 0, 261, 81))
        self.user.setTitle(u"User")
        self.uLabel = QLabel(self.user)
        self.uLabel.setObjectName(u"uLabel")
        self.uLabel.setGeometry(QRect(20, 20, 81, 21))
        self.uLabel.setText(u"Username:")
        self.uLE = QLineEdit(self.user)
        self.uLE.setObjectName(u"uLE")
        self.uLE.setGeometry(QRect(100, 20, 141, 21))
        self.uLE.setText(u"")
        self.pLabel = QLabel(self.user)
        self.pLabel.setObjectName(u"pLabel")
        self.pLabel.setGeometry(QRect(20, 50, 81, 21))
        self.pLabel.setText(u"Password:")
        self.pLE = QLineEdit(self.user)
        self.pLE.setObjectName(u"pLE")
        self.pLE.setGeometry(QRect(100, 50, 141, 21))
        self.pLE.setEchoMode(QLineEdit.Password)
        self.eBg = QPushButton(self.general)
        self.eBg.setObjectName(u"eBg")
        self.eBg.setGeometry(QRect(170, 460, 81, 28))
        self.eBg.setText(u"Ok")
        self.clockBox = QGroupBox(self.general)
        self.clockBox.setObjectName(u"clockBox")
        self.clockBox.setGeometry(QRect(280, 0, 141, 51))
        self.clockBox.setTitle(u"Clock")
        self.clockMode = QCheckBox(self.clockBox)
        self.clockMode.setObjectName(u"clockMode")
        self.clockMode.setGeometry(QRect(10, 20, 131, 17))
        self.clockMode.setText(u"24 hour clock")
        self.startup = QGroupBox(self.general)
        self.startup.setObjectName(u"startup")
        self.startup.setGeometry(QRect(10, 80, 261, 51))
        self.startup.setTitle(u"Startup")
        self.playStartupSound = QCheckBox(self.startup)
        self.playStartupSound.setObjectName(u"playStartupSound")
        self.playStartupSound.setGeometry(QRect(10, 20, 121, 20))
        self.playStartupSound.setText(u"Play sound")
        self.showSplashOnStartup = QCheckBox(self.startup)
        self.showSplashOnStartup.setObjectName(u"showSplashOnStartup")
        self.showSplashOnStartup.setGeometry(QRect(110, 20, 161, 20))
        self.showSplashOnStartup.setText(u"Show splash window")
        self.tabs.addTab(self.general, "")
        self.tabs.setTabText(self.tabs.indexOf(self.general), u"General")
        self.customization = QWidget()
        self.customization.setObjectName(u"customization")
        self.colors = QGroupBox(self.customization)
        self.colors.setObjectName(u"colors")
        self.colors.setGeometry(QRect(10, 0, 401, 241))
        self.colors.setTitle(u"Colors (all colors/hex codes valid)")
        self.cL = QLabel(self.colors)
        self.cL.setObjectName(u"cL")
        self.cL.setGeometry(QRect(10, 30, 71, 16))
        self.cL.setText(u"Text Color:")
        self.cL_2 = QLabel(self.colors)
        self.cL_2.setObjectName(u"cL_2")
        self.cL_2.setGeometry(QRect(10, 60, 71, 16))
        self.cL_2.setText(u"BG Color:")
        self.cL_3 = QLabel(self.colors)
        self.cL_3.setObjectName(u"cL_3")
        self.cL_3.setGeometry(QRect(10, 90, 91, 16))
        self.cL_3.setText(u"Taskbar Color:")
        self.cL_4 = QLabel(self.colors)
        self.cL_4.setObjectName(u"cL_4")
        self.cL_4.setGeometry(QRect(10, 120, 121, 16))
        self.cL_4.setText(u"Taskbar Text Color:")
        self.cL_5 = QLabel(self.colors)
        self.cL_5.setObjectName(u"cL_5")
        self.cL_5.setGeometry(QRect(10, 150, 121, 16))
        self.cL_5.setText(u"Button Color:")
        self.cL_6 = QLabel(self.colors)
        self.cL_6.setObjectName(u"cL_6")
        self.cL_6.setGeometry(QRect(10, 180, 121, 16))
        self.cL_6.setText(u"Button Text Color:")
        self.cLE = QLineEdit(self.colors)
        self.cLE.setObjectName(u"cLE")
        self.cLE.setGeometry(QRect(130, 30, 81, 22))
        self.cLE_2 = QLineEdit(self.colors)
        self.cLE_2.setObjectName(u"cLE_2")
        self.cLE_2.setGeometry(QRect(130, 60, 81, 22))
        self.cLE_3 = QLineEdit(self.colors)
        self.cLE_3.setObjectName(u"cLE_3")
        self.cLE_3.setGeometry(QRect(130, 90, 81, 22))
        self.cLE_4 = QLineEdit(self.colors)
        self.cLE_4.setObjectName(u"cLE_4")
        self.cLE_4.setGeometry(QRect(130, 120, 81, 22))
        self.cLE_5 = QLineEdit(self.colors)
        self.cLE_5.setObjectName(u"cLE_5")
        self.cLE_5.setGeometry(QRect(130, 150, 81, 22))
        self.cLE_6 = QLineEdit(self.colors)
        self.cLE_6.setObjectName(u"cLE_6")
        self.cLE_6.setGeometry(QRect(130, 180, 81, 22))
        self.themes = QGroupBox(self.colors)
        self.themes.setObjectName(u"themes")
        self.themes.setGeometry(QRect(220, 20, 171, 151))
        self.themes.setTitle(u"Color Theme")
        self.themeCB = QComboBox(self.themes)
        self.themeCB.setObjectName(u"themeCB")
        self.themeCB.setGeometry(QRect(20, 20, 131, 22))
        self.themeCB.setCurrentText(u"")
        self.tApply = QPushButton(self.themes)
        self.tApply.setObjectName(u"tApply")
        self.tApply.setGeometry(QRect(40, 50, 93, 28))
        self.tApply.setText(u"Apply")
        self.tSave = QPushButton(self.themes)
        self.tSave.setObjectName(u"tSave")
        self.tSave.setGeometry(QRect(40, 80, 93, 28))
        self.tSave.setText(u"Save")
        self.appsUseTheme = QCheckBox(self.themes)
        self.appsUseTheme.setObjectName(u"appsUseTheme")
        self.appsUseTheme.setGeometry(QRect(40, 120, 231, 21))
        self.appsUseTheme.setText(u"Use in apps")
        self.guiThemes = QGroupBox(self.colors)
        self.guiThemes.setObjectName(u"guiThemes")
        self.guiThemes.setGeometry(QRect(220, 180, 171, 51))
        self.guiThemes.setTitle(u"GUI Style")
        self.guiThemeCB = QComboBox(self.guiThemes)
        self.guiThemeCB.setObjectName(u"guiThemeCB")
        self.guiThemeCB.setGeometry(QRect(10, 20, 151, 22))
        self.cL_7 = QLabel(self.colors)
        self.cL_7.setObjectName(u"cL_7")
        self.cL_7.setGeometry(QRect(10, 210, 121, 16))
        self.cL_7.setText(u"Window BG Color:")
        self.cLE_7 = QLineEdit(self.colors)
        self.cLE_7.setObjectName(u"cLE_7")
        self.cLE_7.setGeometry(QRect(130, 210, 81, 22))
        self.showOnDesktop = QGroupBox(self.customization)
        self.showOnDesktop.setObjectName(u"showOnDesktop")
        self.showOnDesktop.setGeometry(QRect(10, 250, 131, 201))
        self.showOnDesktop.setTitle(u"Show On Desktop")
        self.dCHB = QCheckBox(self.showOnDesktop)
        self.dCHB.setObjectName(u"dCHB")
        self.dCHB.setGeometry(QRect(10, 30, 81, 20))
        self.dCHB.setText(u"Settings")
        self.dCHB_2 = QCheckBox(self.showOnDesktop)
        self.dCHB_2.setObjectName(u"dCHB_2")
        self.dCHB_2.setGeometry(QRect(10, 50, 91, 20))
        self.dCHB_2.setText(u"appLauncher")
        self.dCHB_3 = QCheckBox(self.showOnDesktop)
        self.dCHB_3.setObjectName(u"dCHB_3")
        self.dCHB_3.setGeometry(QRect(10, 70, 91, 20))
        self.dCHB_3.setText(u"FileSystem")
        self.dCHB_4 = QCheckBox(self.showOnDesktop)
        self.dCHB_4.setObjectName(u"dCHB_4")
        self.dCHB_4.setGeometry(QRect(10, 90, 101, 20))
        self.dCHB_4.setText(u"camelInstall")
        self.dCHB_5 = QCheckBox(self.showOnDesktop)
        self.dCHB_5.setObjectName(u"dCHB_5")
        self.dCHB_5.setGeometry(QRect(10, 110, 81, 20))
        self.dCHB_5.setText(u"Editor")
        self.dCHB_6 = QCheckBox(self.showOnDesktop)
        self.dCHB_6.setObjectName(u"dCHB_6")
        self.dCHB_6.setGeometry(QRect(10, 130, 81, 20))
        self.dCHB_6.setText(u"AOSHelp")
        self.dCHB_7 = QCheckBox(self.showOnDesktop)
        self.dCHB_7.setObjectName(u"dCHB_7")
        self.dCHB_7.setGeometry(QRect(10, 150, 81, 20))
        self.dCHB_7.setText(u"Terminal")
        self.dCHB_8 = QCheckBox(self.showOnDesktop)
        self.dCHB_8.setObjectName(u"dCHB_8")
        self.dCHB_8.setGeometry(QRect(10, 170, 81, 20))
        self.dCHB_8.setText(u"Calculator")
        self.eBc = QPushButton(self.customization)
        self.eBc.setObjectName(u"eBc")
        self.eBc.setGeometry(QRect(170, 460, 81, 28))
        self.eBc.setText(u"Ok")
        self.font = QGroupBox(self.customization)
        self.font.setObjectName(u"font")
        self.font.setGeometry(QRect(150, 250, 151, 51))
        self.font.setTitle(u"Font")
        self.fSB = QSpinBox(self.font)
        self.fSB.setObjectName(u"fSB")
        self.fSB.setGeometry(QRect(20, 20, 51, 22))
        self.fSB.setSuffix(u"px")
        self.fL = QLabel(self.font)
        self.fL.setObjectName(u"fL")
        self.fL.setGeometry(QRect(80, 23, 61, 16))
        self.fL.setText(u"Font Size")
        self.btnSizeBox = QGroupBox(self.customization)
        self.btnSizeBox.setObjectName(u"btnSizeBox")
        self.btnSizeBox.setGeometry(QRect(150, 300, 151, 151))
        self.btnSizeBox.setTitle(u"Buttons")
        self.btnW = QSpinBox(self.btnSizeBox)
        self.btnW.setObjectName(u"btnW")
        self.btnW.setGeometry(QRect(10, 20, 61, 22))
        self.btnW.setMaximum(999999)
        self.btnH = QSpinBox(self.btnSizeBox)
        self.btnH.setObjectName(u"btnH")
        self.btnH.setGeometry(QRect(10, 50, 61, 22))
        self.btnH.setMaximum(999999)
        self.btnX = QSpinBox(self.btnSizeBox)
        self.btnX.setObjectName(u"btnX")
        self.btnX.setGeometry(QRect(10, 80, 61, 22))
        self.btnX.setMaximum(999999)
        self.btnY = QSpinBox(self.btnSizeBox)
        self.btnY.setObjectName(u"btnY")
        self.btnY.setGeometry(QRect(10, 110, 61, 22))
        self.btnY.setMaximum(999999)
        self.btnWL = QLabel(self.btnSizeBox)
        self.btnWL.setObjectName(u"btnWL")
        self.btnWL.setGeometry(QRect(80, 20, 55, 16))
        self.btnWL.setText(u"Width")
        self.btnHL = QLabel(self.btnSizeBox)
        self.btnHL.setObjectName(u"btnHL")
        self.btnHL.setGeometry(QRect(80, 50, 55, 16))
        self.btnHL.setText(u"Height")
        self.btnXL = QLabel(self.btnSizeBox)
        self.btnXL.setObjectName(u"btnXL")
        self.btnXL.setGeometry(QRect(80, 80, 81, 16))
        self.btnXL.setText(u"X Spacing")
        self.btnYL = QLabel(self.btnSizeBox)
        self.btnYL.setObjectName(u"btnYL")
        self.btnYL.setGeometry(QRect(80, 110, 81, 16))
        self.btnYL.setText(u"Y Spacing")
        self.tabs.addTab(self.customization, "")
        self.tabs.setTabText(self.tabs.indexOf(self.customization), u"Customization")
        self.menubar = QWidget()
        self.menubar.setObjectName(u"menubar")
        self.segments = QListWidget(self.menubar)
        self.segments.setObjectName(u"segments")
        self.segments.setGeometry(QRect(30, 120, 161, 231))
        self.segments.setDragDropMode(QAbstractItemView.DragDrop)
        self.segments.setDefaultDropAction(Qt.MoveAction)
        self.menubarSegments = QListWidget(self.menubar)
        self.menubarSegments.setObjectName(u"menubarSegments")
        self.menubarSegments.setGeometry(QRect(230, 120, 161, 231))
        self.menubarSegments.setDragDropMode(QAbstractItemView.DragDrop)
        self.menubarSegments.setDefaultDropAction(Qt.MoveAction)
        self.labelSegments = QLabel(self.menubar)
        self.labelSegments.setObjectName(u"labelSegments")
        self.labelSegments.setGeometry(QRect(24, 90, 171, 20))
        self.labelSegments.setText(u"Segments Available")
        self.labelSegments.setAlignment(Qt.AlignCenter)
        self.labelMB = QLabel(self.menubar)
        self.labelMB.setObjectName(u"labelMB")
        self.labelMB.setGeometry(QRect(230, 90, 161, 20))
        self.labelMB.setText(u"Segments In Menu Bar")
        self.labelMB.setAlignment(Qt.AlignCenter)
        self.eBm = QPushButton(self.menubar)
        self.eBm.setObjectName(u"eBm")
        self.eBm.setGeometry(QRect(170, 460, 81, 28))
        self.eBm.setText(u"Ok")
        self.tabs.addTab(self.menubar, "")
        self.tabs.setTabText(self.tabs.indexOf(self.menubar), u"Menu Bar")
        self.shortcuts = QWidget()
        self.shortcuts.setObjectName(u"shortcuts")
        self.sDesktop = QGroupBox(self.shortcuts)
        self.sDesktop.setObjectName(u"sDesktop")
        self.sDesktop.setGeometry(QRect(10, 0, 401, 451))
        self.sDesktop.setTitle(u"Desktop")
        self.KS = QKeySequenceEdit(self.sDesktop)
        self.KS.setObjectName(u"KS")
        self.KS.setGeometry(QRect(90, 30, 113, 22))
        self.KS.setKeySequence(u"Ctrl+R")
        self.sL = QLabel(self.sDesktop)
        self.sL.setObjectName(u"sL")
        self.sL.setGeometry(QRect(20, 30, 55, 16))
        self.sL.setText(u"Run...")
        self.KS_2 = QKeySequenceEdit(self.sDesktop)
        self.KS_2.setObjectName(u"KS_2")
        self.KS_2.setGeometry(QRect(90, 60, 113, 22))
        self.KS_2.setKeySequence(u"Ctrl+R")
        self.sL_2 = QLabel(self.sDesktop)
        self.sL_2.setObjectName(u"sL_2")
        self.sL_2.setGeometry(QRect(20, 60, 55, 16))
        self.sL_2.setText(u"Terminal")
        self.KS_3 = QKeySequenceEdit(self.sDesktop)
        self.KS_3.setObjectName(u"KS_3")
        self.KS_3.setGeometry(QRect(90, 90, 113, 22))
        self.KS_3.setKeySequence(u"Ctrl+Shift+S")
        self.sL_3 = QLabel(self.sDesktop)
        self.sL_3.setObjectName(u"sL_3")
        self.sL_3.setGeometry(QRect(20, 90, 55, 16))
        self.sL_3.setText(u"Settings")
        self.sL_4 = QLabel(self.sDesktop)
        self.sL_4.setObjectName(u"sL_4")
        self.sL_4.setGeometry(QRect(20, 120, 55, 16))
        self.sL_4.setText(u"Help")
        self.KS_4 = QKeySequenceEdit(self.sDesktop)
        self.KS_4.setObjectName(u"KS_4")
        self.KS_4.setGeometry(QRect(90, 120, 113, 22))
        self.KS_4.setKeySequence(u"Ctrl+H")
        self.eBs = QPushButton(self.shortcuts)
        self.eBs.setObjectName(u"eBs")
        self.eBs.setGeometry(QRect(170, 460, 81, 28))
        self.eBs.setText(u"Ok")
        self.tabs.addTab(self.shortcuts, "")
        self.tabs.setTabText(self.tabs.indexOf(self.shortcuts), u"Shortcuts")
        self.reset = QWidget()
        self.reset.setObjectName(u"reset")
        self.rAOS = QPushButton(self.reset)
        self.rAOS.setObjectName(u"rAOS")
        self.rAOS.setGeometry(QRect(130, 50, 161, 28))
        self.rAOS.setText(u"Reset AOS...")
        self.tabs.addTab(self.reset, "")
        self.tabs.setTabText(self.tabs.indexOf(self.reset), u"Reset")

        self.retranslateUi()

        self.tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def resetAOS(self, andmodules = False):
        retval = msgBox(f"Are you sure you want to reset AOS to its default settings?","Reset AOS?",QMessageBox.Warning,QMessageBox.Yes|QMessageBox.No)

        if retval == 16384:
            retval2 = msgBox(f"Are you SURE? All of your documents and user data will be erased!","Are you SURE?",QMessageBox.Warning,QMessageBox.Yes|QMessageBox.No)
            if retval2 == 16384:
                retval3 = msgBox("If you say so...","Whatever you say!",QMessageBox.Warning,QMessageBox.Yes|QMessageBox.No)
                if retval3 == 16384:
                    self.eraseAllData()


    def retranslateUi(self):
        self.pLE.setInputMask("")
        self.tabs.setTabText(self.tabs.indexOf(self.customization), QCoreApplication.translate("settings", u"Customization", None))
        self.tabs.setTabText(self.tabs.indexOf(self.shortcuts), QCoreApplication.translate("settings", u"Shortcuts", None))

        self.tApply.clicked.connect(self.applyTheme)
        self.tSave.clicked.connect(self.saveTheme)
        self.eBg.clicked.connect(self.getmeout)
        self.eBc.clicked.connect(self.getmeout)
        self.eBs.clicked.connect(self.getmeout)
        self.eBm.clicked.connect(self.getmeout)
        self.rAOS.clicked.connect(self.resetAOS)
        self.getCurrentSettings()

    def eraseAllData(self):
        cwd = getcwd().replace("\\","/")
        sdkFile = open(cwd+"/files/apps/sdk/sdk.py","r")
        sdk = sdkFile.read()
        sdkFile.close()

        remove(cwd+"/files/system/data/user/data.aos")
        remove(getcwd().replace("\\","/")+"/files/system/data/user/desktop.aos")
        rmtree(cwd+"/files/home/")
        rmtree(cwd+"/files/apps/")
        sleep(2)
        mkdir(cwd+"/files/home/")
        mkdir(cwd+"/files/apps/")
        mkdir(cwd+"/files/apps/assets/")
        mkdir(cwd+"/files/apps/sdk/")
        f = open(cwd+"/files/apps/sdk/sdk.py","w+")
        f.write(sdk)
        f.close()
        f = open(cwd+"/files/system/data/user/desktop.aos","w+")
        f.close()
        f = open(cwd+"/files/system/data/user/menubar.aos","w+")
        f.close()
        msgBox("AOS has been factory reset.","Done.",QMessageBox.Information,QMessageBox.Ok)
        exit()

    def toBool(self, string):
        if string == "True":
            return True
        elif string == "False":
            return False
        
    # retranslateUi
    def getCurrentSettings(self):
        global standardSegs
        # pass

        f = open("files/system/data/user/data.aos","r")
        content = f.read()
        content = content.split("\n")

        try:
            themeText = open("files/system/data/user/themes/"+content[2]+".theme","r")
        except FileNotFoundError:
            themeText = open("files/system/data/user/themes/default-dark.theme","r")
        themeText = themeText.read()
        themeColors = themeText.split("\n")

        self.guiThemeCB.clear()
        self.themeCB.clear()

        for _ in listdir(getcwd().replace("\\","/")+"/files/system/data/user/themes/"):
            self.themeCB.addItem(_.split(".theme")[0])

        self.uLE.setText(content[0])
        self.pLE.setText(content[1])
        self.themeCB.setCurrentText(content[2])
        self.cLE.setText(themeColors[0])
        self.cLE_2.setText(themeColors[1])
        self.cLE_3.setText(themeColors[2])
        self.cLE_4.setText(themeColors[3])
        self.cLE_5.setText(themeColors[4])
        self.cLE_6.setText(themeColors[5])
        self.cLE_7.setText(themeColors[6])
        self.fSB.setValue(int(content[3]))
        self.KS.setKeySequence(content[4])
        self.KS_2.setKeySequence(content[5])
        self.KS_3.setKeySequence(content[6])
        self.KS_4.setKeySequence(content[7])

        desktopCheckmarkVals = content[8].split("|")

        self.dCHB.setChecked(self.toBool(desktopCheckmarkVals[0]))
        self.dCHB_2.setChecked(self.toBool(desktopCheckmarkVals[1]))
        self.dCHB_3.setChecked(self.toBool(desktopCheckmarkVals[2]))
        self.dCHB_4.setChecked(self.toBool(desktopCheckmarkVals[3]))
        self.dCHB_5.setChecked(self.toBool(desktopCheckmarkVals[4]))
        self.dCHB_6.setChecked(self.toBool(desktopCheckmarkVals[5]))
        self.dCHB_7.setChecked(self.toBool(desktopCheckmarkVals[6]))
        self.dCHB_8.setChecked(self.toBool(desktopCheckmarkVals[7]))

        self.showSplashOnStartup.setChecked(not self.toBool(content[9]))
        
        for i in QStyleFactory.keys():
            if i != "windowsvista":
                self.guiThemeCB.addItem(i)
        
        self.guiThemeCB.setCurrentText(content[10])

        self.clockMode.setChecked(self.toBool(content[11]))

        self.btnW.setValue(int(content[12].split("|")[0]))
        self.btnH.setValue(int(content[12].split("|")[1]))
        self.btnX.setValue(int(content[12].split("|")[2]))
        self.btnY.setValue(int(content[12].split("|")[3]))

        self.playStartupSound.setChecked(self.toBool(content[13]))
        self.appsUseTheme.setChecked(self.toBool(content[14]))

        f = open("files/system/data/user/menubar.aos","r")
        menubarSegs = f.read()

        if menubarSegs == "":
            self.segments.addItems(standardSegs)
        else:
            for i in menubarSegs.split("|"):
                if i != "":
                    self.menubarSegments.addItem(i)

            for z in standardSegs: # cycle through segments in menubar already
                if not z in menubarSegs.split("|"):
                    self.segments.addItem(z)

        f.close()

    def applyTheme(self):
        tFile = open("files/system/data/user/themes/"+self.themeCB.currentText()+".theme","r")
        colors = tFile.read()
        themeColors = colors.split("\n")

        self.cLE.setText(themeColors[0])
        self.cLE_2.setText(themeColors[1])
        self.cLE_3.setText(themeColors[2])
        self.cLE_4.setText(themeColors[3])
        self.cLE_5.setText(themeColors[4])
        self.cLE_6.setText(themeColors[5])
        self.cLE_7.setText(themeColors[6])

        if self.appsUseTheme.isChecked():
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(themeColors[6]))
            palette.setColor(QPalette.WindowText, QColor(themeColors[0]))
            palette.setColor(QPalette.Base, QColor(themeColors[1]))
            palette.setColor(QPalette.AlternateBase, QColor(themeColors[6]))
            palette.setColor(QPalette.ToolTipBase, QColor(themeColors[1]))
            palette.setColor(QPalette.ToolTipText, QColor(themeColors[0]))
            palette.setColor(QPalette.Text, QColor(themeColors[0]))
            palette.setColor(QPalette.Button, QColor(themeColors[1]))
            palette.setColor(QPalette.ButtonText, QColor(themeColors[5]))
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(themeColors[4]))
            palette.setColor(QPalette.HighlightedText, QColor(themeColors[0]))
            QGuiApplication.setPalette(palette)


    def saveTheme(self):
        currentColors = [self.cLE.text(),self.cLE_2.text(),self.cLE_3.text(),self.cLE_4.text(),self.cLE_5.text(),self.cLE_6.text(),self.cLE_7.text()] # edit all others with new color

        tFile,check = QFileDialog.getSaveFileName(None, "Save to theme", getcwd().replace("\\","/")+"/files/system/data/user/themes/", "AOS theme (*.theme)")
        if check:
            themeFile = open(tFile,"w")

            for i in range(6):
                themeFile.write(currentColors[i]+"\n")
            themeFile.write(currentColors[6])

            themeFile.close()
        self.getCurrentSettings()

    def getmeout(self):
        retval = 0

        f = open("files/system/data/user/data.aos","w")
        themeFile = open("files/system/data/user/themes/"+self.themeCB.currentText()+".theme","r")
        tFile = getcwd().replace("\\","/")+"/files/system/data/user/themes/"+self.themeCB.currentText()+".theme"

        tFsplit = themeFile.read().split("\n")

        currentColors = [self.cLE.text(),self.cLE_2.text(),self.cLE_3.text(),self.cLE_4.text(),self.cLE_5.text(),self.cLE_6.text(),self.cLE_7.text()]

        if currentColors != tFsplit:
            tFile = getcwd().replace("\\","/")+"/files/system/data/user/themes/"+self.themeCB.currentText()+".theme"

            retval = msgBox(f"You have unsaved color changes. Would you like to save them to a new theme?", "Save changes to theme?", QMessageBox.Warning, QMessageBox.Yes|QMessageBox.No)

            if retval == 16384: # yes value
                tFile,check = QFileDialog.getSaveFileName(None, "Save to theme", getcwd().replace("\\","/")+"/files/system/data/user/themes/", "AOS theme (*.theme)")
                if check:
                    themeFile.close()
                    themeFile = open(tFile,"w")

                    for i in range(6):
                        themeFile.write(currentColors[i]+"\n")
                    themeFile.write(currentColors[6])

                    themeFile.close()

        f.write(self.uLE.text()+"\n")
        f.write(self.pLE.text()+"\n")
        if retval == 16384:
            tFile = tFile.split("/")
            tFile = tFile[len(tFile)-1].split(".")
            tFile = tFile[0]
            f.write(tFile+"\n")
        else:
            f.write(self.themeCB.currentText()+"\n")
        f.write(str(self.fSB.value())+"\n")
        f.write(self.KS.keySequence().toString()+"\n")
        f.write(self.KS_2.keySequence().toString()+"\n")
        f.write(self.KS_3.keySequence().toString()+"\n")
        f.write(self.KS_4.keySequence().toString()+"\n")
        f.write(str(self.dCHB.isChecked())+"|")
        f.write(str(self.dCHB_2.isChecked())+"|")
        f.write(str(self.dCHB_3.isChecked())+"|")
        f.write(str(self.dCHB_4.isChecked())+"|")
        f.write(str(self.dCHB_5.isChecked())+"|")
        f.write(str(self.dCHB_6.isChecked())+"|")
        f.write(str(self.dCHB_7.isChecked())+"|")
        f.write(str(self.dCHB_8.isChecked())+"\n")
        f.write(str(not self.showSplashOnStartup.isChecked())+"\n")
        f.write(self.guiThemeCB.currentText()+"\n")
        f.write(str(self.clockMode.isChecked())+"\n")
        f.write(str(self.btnW.value())+"|"+str(self.btnH.value())+"|"+str(self.btnX.value())+"|"+str(self.btnY.value())+"\n")
        f.write(str(self.playStartupSound.isChecked())+"\n")
        f.write(str(self.appsUseTheme.isChecked()))
        f.close()

        f = open("files/system/data/user/menubar.aos","w")
        for i in range(self.menubarSegments.count()):
            f.write(self.menubarSegments.item(i).text()+"|")
        f.close()

        msgBox("Your settings have been applied! Please restart AOS-GUI to see your changes to the desktop.", "Settings set!", QMessageBox.Information, QMessageBox.Ok)
        self.close()