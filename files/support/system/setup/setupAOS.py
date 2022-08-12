from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from os.path import exists
from os import listdir,getcwd

from files.support.system.helpers.funcs import msgBox

titleText = u"welcome to AOS-GUI!"
endButtonText = u"Setup AOS-GUI"

class installform(QMainWindow):
    def __init__(self):
        super(installform, self).__init__()

        global titleText,endButtonText

        self.setFixedSize(450, 540)
        self.setWindowTitle(u"AOS-GUI/setupAOS")
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.tabs = QTabWidget(self)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 10, 431, 521))
        self.tabs.setMovable(False)
        self.general = QWidget()
        self.general.setObjectName(u"general")
        self.user = QGroupBox(self.general)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(10, 0, 251, 81))
        self.user.setTitle(u"User")
        self.uLabel = QLabel(self.user)
        self.uLabel.setObjectName(u"uLabel")
        self.uLabel.setGeometry(QRect(20, 20, 81, 21))
        self.uLabel.setText(u"Username:")
        self.uLE = QLineEdit(self.user)
        self.uLE.setObjectName(u"uLE")
        self.uLE.setGeometry(QRect(100, 20, 131, 21))
        self.uLE.setText(u"")
        self.pLabel = QLabel(self.user)
        self.pLabel.setObjectName(u"pLabel")
        self.pLabel.setGeometry(QRect(20, 50, 81, 21))
        self.pLabel.setText(u"Password:")
        self.pLE = QLineEdit(self.user)
        self.pLE.setObjectName(u"pLE")
        self.pLE.setGeometry(QRect(100, 50, 131, 21))
        self.pLE.setText(u"")
        self.pLE.setEchoMode(QLineEdit.Password)
        self.eBg = QPushButton(self.general)
        self.eBg.setObjectName(u"eBg")
        self.eBg.setGeometry(QRect(170, 460, 91, 28))
        self.eBg.setText(u"Ok")
        self.tabs.addTab(self.general, "")
        self.tabs.setTabText(self.tabs.indexOf(self.general), u"General")
        self.customization = QWidget()
        self.customization.setObjectName(u"customization")
        self.colors = QGroupBox(self.customization)
        self.colors.setObjectName(u"colors")
        self.colors.setGeometry(QRect(10, 0, 401, 211))
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
        self.themes.setGeometry(QRect(220, 10, 171, 191))
        self.themes.setTitle(u"Themes")
        self.themeCB = QComboBox(self.themes)
        self.themeCB.setObjectName(u"themeCB")
        self.themeCB.setGeometry(QRect(20, 50, 131, 22))
        self.themeCB.setCurrentText(u"")
        self.tApply = QPushButton(self.themes)
        self.tApply.setObjectName(u"tApply")
        self.tApply.setGeometry(QRect(40, 80, 93, 28))
        self.tApply.setText(u"Apply")
        self.tSave = QPushButton(self.themes)
        self.tSave.setObjectName(u"tSave")
        self.tSave.setGeometry(QRect(40, 110, 93, 28))
        self.tSave.setText(u"Save")
        self.showOnDesktop = QGroupBox(self.customization)
        self.showOnDesktop.setObjectName(u"showOnDesktop")
        self.showOnDesktop.setGeometry(QRect(10, 220, 121, 261))
        self.showOnDesktop.setTitle(u"Show On Desktop")
        self.dCHB = QCheckBox(self.showOnDesktop)
        self.dCHB.setObjectName(u"dCHB")
        self.dCHB.setGeometry(QRect(10, 30, 81, 20))
        self.dCHB.setText(u"Settings")
        self.dCHB_2 = QCheckBox(self.showOnDesktop)
        self.dCHB_2.setObjectName(u"dCHB_2")
        self.dCHB_2.setGeometry(QRect(10, 50, 81, 20))
        self.dCHB_2.setText(u"Run .rndr")
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
        self.dCHB_7.setText(u"ATerm")
        self.eBc = QPushButton(self.customization)
        self.eBc.setObjectName(u"eBc")
        self.eBc.setGeometry(QRect(170, 460, 91, 28))
        self.eBc.setText(u"Ok")
        self.font = QGroupBox(self.customization)
        self.font.setObjectName(u"font")
        self.font.setGeometry(QRect(140, 220, 131, 51))
        self.font.setTitle("Font")
        self.fSB = QSpinBox(self.font)
        self.fSB.setObjectName(u"fSB")
        self.fSB.setGeometry(QRect(10, 20, 51, 22))
        self.fSB.setSuffix(u"px")
        self.fL = QLabel(self.font)
        self.fL.setObjectName(u"fL")
        self.fL.setGeometry(QRect(70, 23, 61, 16))
        self.fL.setText(u"Font Size")
        self.splash = QGroupBox(self.customization)
        self.splash.setObjectName(u"splash")
        self.splash.setGeometry(QRect(280, 220, 141, 51))
        self.splash.setTitle(u"Splash")
        self.showSplashOnStartup = QCheckBox(self.splash)
        self.showSplashOnStartup.setObjectName(u"showSplashOnStartup")
        self.showSplashOnStartup.setGeometry(QRect(10, 20, 131, 20))
        self.showSplashOnStartup.setText(u"Show on startup")
        self.tabs.addTab(self.customization, "")
        self.shortcuts = QWidget()
        self.shortcuts.setObjectName(u"shortcuts")
        self.sDesktop = QGroupBox(self.shortcuts)
        self.sDesktop.setObjectName(u"groupBox")
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
        self.KS_2.setKeySequence(u"Ctrl+T")
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
        self.eBs.setGeometry(QRect(170, 460, 91, 28))
        self.eBs.setText(u"Ok")
        self.tabs.addTab(self.shortcuts, "")

        self.retranslateUi()

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def showWelcomeMessage(self):
        msgBox("Before you start using AOS, please configure it to your liking. (You can always change these settings later!)","Welcome to AOS-GUI!",QMessageBox.Information,QMessageBox.Ok)

    def retranslateUi(self):
        self.pLE.setInputMask("")
        self.tabs.setTabText(self.tabs.indexOf(self.customization), QCoreApplication.translate("settings", u"Customization", None))
        self.tabs.setTabText(self.tabs.indexOf(self.shortcuts), QCoreApplication.translate("settings", u"Shortcuts", None))

        self.tApply.clicked.connect(self.applyTheme)
        self.tSave.clicked.connect(self.saveTheme)
        self.eBg.clicked.connect(self.getmeout)
        self.eBc.clicked.connect(self.getmeout)
        self.eBs.clicked.connect(self.getmeout)
        self.getCurrentSettings()
        self.showWelcomeMessage()
    # retranslateUi
    def getCurrentSettings(self):
        # pass
        themeText = open("files/support/data/user/themes/default-dark.theme","r")
        themeText = themeText.read()
        themeColors = themeText.split("\n")

        for _ in listdir(getcwd().replace("\\","/")+"/files/support/data/user/themes/"):
            self.themeCB.addItem(_.split(".theme")[0])

        self.themeCB.setCurrentText("default-dark")
        self.cLE.setText(themeColors[0])
        self.cLE_2.setText(themeColors[1])
        self.cLE_3.setText(themeColors[2])
        self.cLE_4.setText(themeColors[3])
        self.cLE_5.setText(themeColors[4])
        self.cLE_6.setText(themeColors[5])
        self.fSB.setValue(12)

    def applyTheme(self):
        tFile = open("files/support/data/user/themes/"+self.themeCB.currentText()+".theme","r")
        colors = tFile.read()
        themeColors = colors.split("\n")

        self.cLE.setText(themeColors[0])
        self.cLE_2.setText(themeColors[1])
        self.cLE_3.setText(themeColors[2])
        self.cLE_4.setText(themeColors[3])
        self.cLE_5.setText(themeColors[4])
        self.cLE_6.setText(themeColors[5])
        


    def saveTheme(self):
        currentColors = [self.cLE.text(),self.cLE_2.text(),self.cLE_3.text(),self.cLE_4.text(),self.cLE_5.text(),self.cLE_6.text()]

        tFile,check = QFileDialog.getSaveFileName(None, "Save to theme", getcwd().replace("\\","/")+"/files/support/data/user/themes/", "AOS theme (*.theme)")
        if check:
            themeFile = open(tFile,"w")

            for i in range(5):
                themeFile.write(currentColors[i]+"\n")
            themeFile.write(currentColors[5])

            themeFile.close()

    def getmeout(self):
        retval = 0

        f = open("files/support/data/user/data.aos","w")
        themeFile = open("files/support/data/user/themes/"+self.themeCB.currentText()+".theme","r")
        tFile = getcwd().replace("\\","/")+"/files/support/data/user/themes/"+self.themeCB.currentText()+".theme"

        tFsplit = themeFile.read().split("\n")

        currentColors = [self.cLE.text(),self.cLE_2.text(),self.cLE_3.text(),self.cLE_4.text(),self.cLE_5.text(),self.cLE_6.text()]

        if currentColors != tFsplit:
            tFile = getcwd().replace("\\","/")+"/files/support/data/user/themes/"+self.themeCB.currentText()+".theme"

            retval = msgBox(f"You have unsaved color changes. Would you like to save them to a new theme?","Save?",QMessageBox.Warning,QMessageBox.Yes|QMessageBox.No)

            if retval == 16384:
                tFile,check = QFileDialog.getSaveFileName(None, "Save to theme", getcwd().replace("\\","/")+"/files/support/data/user/themes/", "AOS theme (*.theme)")
                if check:
                    themeFile.close()
                    themeFile = open(tFile,"w")

                    for i in range(5):
                        themeFile.write(currentColors[i]+"\n")
                    themeFile.write(currentColors[5])

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
        f.write(str(self.dCHB_7.isChecked())+"\n")
        f.write(str(not self.showSplashOnStartup.isChecked()))

        msgBox("Your settings have been applied! Please reopen AOS-GUI.","Settings set!",QMessageBox.Information,QMessageBox.Ok)
        self.close()