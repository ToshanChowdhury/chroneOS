from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        drive = QWebEngineView()
        drive.setUrl(QUrl("https://accounts.google.com/ServiceLogin/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2F&followup=https%3A%2F%2Fdrive.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"))
        self.setCentralWidget(drive)
        self.showMaximized()


app = QApplication(sys.argv)
app.setApplicationName("Google Drive")
app.setWindowIcon(QIcon("google-drive.png"))
window = Main()
app.exec_()