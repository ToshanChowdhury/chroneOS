from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.calendar = QCalendarWidget()
		self.setCentralWidget(self.calendar)
		self.statusBar = QStatusBar()
		self.statusBar.setStyleSheet("background-color: rgb(3, 255, 29);")
		self.setStatusBar(self.statusBar)

		menu_bar = QMenuBar()
		menu_bar.setStyleSheet("background-color: rgb(3, 255, 29)")
		self.setMenuBar(menu_bar)

		file_menu = QMenu("File", self)
		file_menu.setFont(QFont("Segoe UI", 12))
		file_menu.setStatusTip("File Menu")
		file_menu.setStyleSheet("background-color: rgb(3, 255, 29);")
		menu_bar.addMenu(file_menu)

		quit_action = QAction(QIcon("close.png"), "Quit", self)
		quit_action.setStatusTip("Quit The Window")
		quit_action.triggered.connect(sys.exit)
		file_menu.addAction(quit_action)


app = QApplication(sys.argv)
app.setApplicationName("Calendar")
app.setWindowIcon(QIcon("calendar.png"))
window = Window()
window.showMaximized()
app.exec_()