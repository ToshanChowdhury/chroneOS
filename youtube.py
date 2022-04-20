import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        youtube = QWebEngineView()
        youtube.setUrl(QUrl("https://www.youtube.com/"))
        self.setCentralWidget(youtube)
        self.showMaximized()


app = QApplication(sys.argv)
app.setApplicationName("YouTube")
app.setWindowIcon(QIcon("youtube.png"))
window = Main()
app.exec_()
