import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        meet = QWebEngineView()
        meet.setUrl(QUrl("https://www.google.com/meet"))
        self.setCentralWidget(meet)
        self.showMaximized()


app = QApplication(sys.argv)
app.setApplicationName("Google Meet")
app.setWindowIcon(QIcon("meet.png"))
window = Main()
app.exec_()