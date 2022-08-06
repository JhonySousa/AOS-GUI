# required imports

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# next line is the project description, format is '#(tilde){name}|{desc}|{ver}'
#~template|template project|v0.1


# class name can be anything

class main_print(QWidget):
    # this can be your normal PyQt5 code, go crazy!
    def __init__(self):
        super(main_print, self).__init__()
        self.setFixedSize(500, 400)
        self.setWindowTitle("AOS-GUI")
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint) # this line is needed for the program to stay on top of desktop

# these last two lines must be included for the app to launch.

window = main_print()
window.show()