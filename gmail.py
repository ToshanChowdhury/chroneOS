import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        gmail = QWebEngineView()
        gmail.setUrl(QUrl("https://www.gmail.com/"))
        self.setCentralWidget(gmail)
        self.showMaximized()


app = QApplication(sys.argv)
app.setApplicationName("G-Mail")
app.setWindowIcon(QIcon("gmail.png"))
window = Main()
app.exec_()