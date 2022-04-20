from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from tkinter import messagebox

import sys
import os
import psutil
from datetime import *

battery = psutil.sensors_battery()
percent = str(battery.percent)
date_time = datetime.now()
date = date_time.strftime("%d/%m/%y")
time = date_time.strftime("%I:%M %p")
username_info = open("name.txt")
password_info = open("password.txt")
user_info = username_info.read()
pass_info = password_info.read()
task_bar_colour = open("toolbar_colour.txt")
menu_bar_colour = open("menubar_colour.txt")
power_menu_colour = open("powermenu_colour.txt")
file_menu_colour = open("filemenu_colour.txt")
system_info_menu = open("systeminfomenu_colour.txt")
account_menu = open("accountmenu_colour.txt")
tbc = task_bar_colour.read()
mbc = menu_bar_colour.read()
pmc = power_menu_colour.read()
fmc = file_menu_colour.read()
sim = system_info_menu.read()
acm = account_menu.read()


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.console = QWebEngineView()
		self.console.setUrl(QUrl("C:/Users/Family/OneDrive/Desktop/Toshan/Python/Chrone OS/mainBackground.jpeg"))
		self.console.setStyleSheet("background-color: rgb(3, 255, 29)")
		self.setCentralWidget(self.console)
		self.showMaximized()

		menu_bar = QMenuBar()
		menu_bar.setStyleSheet("background-color: " + str(mbc) + ";")
		self.setMenuBar(menu_bar)

		account_menu = QMenu("Username:" + " " + user_info, self)
		account_menu.setStyleSheet("background-color: " + str(acm) + ";")
		menu_bar.addMenu(account_menu)

		log_out = QAction(QIcon("close.png"), "Log Out", self)
		log_out.triggered.connect(sys.exit)
		account_menu.addAction(log_out)

		change_password = QAction(QIcon("reload.png"), "Change Account Password", self)
		change_password.triggered.connect(self.account_file)
		account_menu.addAction(change_password)

		add_config_file = QAction(QIcon("file.png"), "Create Account Config File", self)
		add_config_file.triggered.connect(self.config_file)
		account_menu.addAction(add_config_file)

		file_menu = QMenu("File", self)
		file_menu.setStyleSheet("background-color: " + str(fmc) +";")
		menu_bar.addMenu(file_menu)

		power_menu = QMenu("Power", self)
		power_menu.setStyleSheet("background-color: " + str(pmc) +";")
		file_menu.addMenu(power_menu)

		shut_down = QAction(QIcon("power.png"), "Shut Down", self)
		shut_down.triggered.connect(sys.exit)
		power_menu.addAction(shut_down)

		restart = QAction(QIcon("reload.png"), "Restart", self)
		restart.triggered.connect(self.restart_os)
		power_menu.addAction(restart)

		apps = QMenu("Apps", self)
		apps.setStyleSheet("background-color: " + str(fmc) + ";")
		file_menu.addMenu(apps)

		browser = QAction(QIcon("mainIcon.jpeg"), "Browser", self)
		browser.triggered.connect(self.browser)
		apps.addAction(browser)

		files = QAction(QIcon("file-management.png"), "Files", self)
		files.triggered.connect(self.file_manager)
		apps.addAction(files)

		google_docs = QAction(QIcon("google_docs.jpeg"), "Google Docs", self)
		google_docs.triggered.connect(self.google_docs)
		apps.addAction(google_docs)

		google_sheets = QAction(QIcon("google_sheets.jpeg"), "Google Sheets", self)
		google_sheets.triggered.connect(self.google_sheets)
		apps.addAction(google_sheets)

		google_slides = QAction(QIcon("google_slides.jpeg"), "Google Slides", self)
		google_slides.triggered.connect(self.google_slides)
		apps.addAction(google_slides)

		google_drive = QAction(QIcon("google-drive.png"), "Google Drive", self)
		google_drive.triggered.connect(self.google_drive)
		apps.addAction(google_drive)

		google_photos = QAction(QIcon("photos.jpeg"), "Google Photos", self)
		google_photos.triggered.connect(self.photos)
		apps.addAction(google_photos)

		js_paint = QAction(QIcon("color.png"), "Paint Web", self)
		js_paint.triggered.connect(self.js_paint)
		apps.addAction(js_paint)

		stadia = QAction(QIcon("Stadia.jpg"), "Google Stadia", self)
		stadia.triggered.connect(self.google_stadia)
		apps.addAction(stadia)

		settings = QAction(QIcon("settings.png"), "Settings", self)
		settings.triggered.connect(self.settings_app)
		apps.addAction(settings)

		command_prompt = QAction(QIcon("Windows Terminal Logo.png"), "Command Prompt", self)
		command_prompt.triggered.connect(self.terminal)
		apps.addAction(command_prompt)

		Notes = QAction(QIcon("google_docs.jpeg"), "Notes", self)
		Notes.triggered.connect(self.notes)
		apps.addAction(Notes)

		assistant = QAction(QIcon("Speakassist.jpeg"), "Assistant", self)
		assistant.triggered.connect(self.assist)
		apps.addAction(assistant)

		search_app = QAction(QIcon("file_search.png"), "Search", self)
		search_app.triggered.connect(self.file_search)
		apps.addAction(search_app)

		youtube = QAction(QIcon("youtube.png"), "YouTube", self)
		youtube.triggered.connect(self.youtube)
		apps.addAction(youtube)

		antivirus = QAction(QIcon("antivirus.png"), "Antivirus", self)
		antivirus.triggered.connect(self.antivirus)
		apps.addAction(antivirus)

		meet = QAction(QIcon("meet.png"), "Google Meet", self)
		meet.triggered.connect(self.google_meet)
		apps.addAction(meet)

		g_mail = QAction(QIcon("gmail.png"), "Google Mail", self)
		g_mail.triggered.connect(self.google_mail)
		apps.addAction(g_mail)

		installer = QAction(QIcon("download.png"), "Installer", self)
		installer.triggered.connect(self.install)
		apps.addAction(installer)

		calendar = QAction(QIcon("calendar.png"), "Calendar", self)
		calendar.triggered.connect(self.clock)
		apps.addAction(calendar)

		calculator = QAction(QIcon("calculator.png"), "Calculator Basic", self)
		calculator.triggered.connect(self.calc)
		apps.addAction(calculator)

		time_app = QAction(QIcon("clock.png"), "Clock", self)
		time_app.triggered.connect(self.time)
		apps.addAction(time_app)

		rock_paper_scissors = QAction(QIcon("rock-paper-scissors.png"), "Rock, Paper, Scissors Game", self)
		rock_paper_scissors.triggered.connect(self.rock_game)
		apps.addAction(rock_paper_scissors)

		guess_word = QAction(QIcon("question.png"), "Guess The Word Game", self)
		guess_word.triggered.connect(self.guess_word_game)
		apps.addAction(guess_word)

		menu_bar.addSeparator()

		system_info_menu = QMenu("System", self)
		system_info_menu.setStyleSheet("background-color: " + str(sim) + ";")
		menu_bar.addMenu(system_info_menu)

		date_menu = QAction(QIcon("calendar.png"), "Date:" + " " + date, self)
		system_info_menu.addAction(date_menu)

		time_menu = QAction(QIcon("clock.png"), "Time:" + " " + time, self)
		system_info_menu.addAction(time_menu)

		battery_menu = QAction(QIcon("full-battery.png"), "Battery:" + " " + percent + "%", self)
		system_info_menu.addAction(battery_menu)

		customization = QAction(QIcon("color.png"), "UI Design Colour", self)
		customization.triggered.connect(self.colour)
		system_info_menu.addAction(customization)

		menu_bar.addSeparator()

		search_bar = QToolBar("Search Bar", self)
		search_bar.setIconSize(QSize(16, 16))
		search_bar.setStyleSheet("background-color: " + str(tbc) + ";")
		self.addToolBar(search_bar)

		back_btn = QAction(QIcon("undo.png"), "Back", self)
		back_btn.triggered.connect(self.console.back)
		search_bar.addAction(back_btn)

		forward_btn = QAction(QIcon("redo.png"), "Forward", self)
		forward_btn.triggered.connect(self.console.forward)
		search_bar.addAction(forward_btn)

		self.search_box = QLineEdit()
		self.search_box.setStyleSheet("background-color: rgb(255, 255, 255);")
		search_bar.addWidget(self.search_box)
		self.search_box.returnPressed.connect(self.navigate_to_url)
		self.console.urlChanged.connect(self.update_url)

		reload_btn = QAction(QIcon("reload.png"), "Reload", self)
		reload_btn.triggered.connect(self.console.reload)
		search_bar.addAction(reload_btn)

		home_btn = QAction(QIcon("home.png"), "Home", self)
		home_btn.triggered.connect(self.navigate_home)
		search_bar.addAction(home_btn)

		tool_bar = QToolBar("Taskbar", self)
		tool_bar.setIconSize(QSize(20, 20))
		tool_bar.setStyleSheet("background-color: " + str(tbc) + ";")
		self.addToolBar(Qt.BottomToolBarArea, tool_bar)

		browser = QAction(QIcon("mainIcon.jpeg"), "Browser", self)
		browser.triggered.connect(self.browser)
		tool_bar.addAction(browser)

		files = QAction(QIcon("file-management.png"), "Files", self)
		files.triggered.connect(self.file_manager)
		tool_bar.addAction(files)

		google_docs = QAction(QIcon("google_docs.jpeg"), "Google Docs", self)
		google_docs.triggered.connect(self.google_docs)
		tool_bar.addAction(google_docs)

		google_sheets = QAction(QIcon("google_sheets.jpeg"), "Google Sheets", self)
		google_sheets.triggered.connect(self.google_sheets)
		tool_bar.addAction(google_sheets)

		google_slides = QAction(QIcon("google_slides.jpeg"), "Google Slides", self)
		google_slides.triggered.connect(self.google_slides)
		tool_bar.addAction(google_slides)

		google_drive = QAction(QIcon("google-drive.png"), "Google Drive", self)
		google_drive.triggered.connect(self.google_drive)
		tool_bar.addAction(google_drive)

	def calc(self):
		os.startfile("calculator.py")

	def time(self):
		os.startfile("time.py")

	def google_docs(self):
		self.console.setUrl(QUrl("https://www.google.com/docs"))

	def google_sheets(self):
		self.console.setUrl(QUrl("https://www.google.com/sheets"))

	def google_slides(self):
		self.console.setUrl(QUrl("https://www.google.com/slides"))

	def google_drive(self):
		os.startfile("google-drive.py")

	def js_paint(self):
		self.console.setUrl(QUrl("https://jspaint.app/#local:b42a753063346"))

	def browser(self):
		os.startfile("browser.py")

	def antivirus(self):
		os.startfile("antivirus.bat")

	def google_meet(self):
		os.startfile("google-meet.py")

	def clock(self):
		os.startfile("calendarApp.py")

	def file_search(self):
		os.startfile("search.bat")

	def colour(self):
		os.startfile("UIColour.py")

	def photos(self):
		self.console.setUrl(QUrl("https://www.google.com/photos"))

	def file_manager(self):
		os.startfile("files.py")

	def settings_app(self):
		messagebox.showinfo("Settings", "You Should Edit The main.py file in order to change the settings.")

	def google_stadia(self):
		self.console.setUrl(QUrl("https://www.google.com/stadia"))

	def navigate_to_url(self):
		url = self.search_box.text()
		self.console.setUrl(QUrl(url))

	def youtube(self):
		os.startfile("youtube.py")

	def navigate_home(self):
		self.console.setUrl(QUrl("C:/Users/Family/OneDrive/Desktop/Toshan/Python/Chrone OS/mainBackground.jpeg"))

	def update_url(self, q):
                self.search_box.setText(q.toString())

	def restart_os(self):
		var = "main.py"
		os.startfile(var)
		os.abort(var)

	def terminal(self):
		os.startfile("default_cmd.py")

	def notes(self):
		os.startfile("Notes.py")

	def assist(self):
		os.startfile("assistant.py")

	def google_mail(self):
		os.startfile("gmail.py")

	def install(self):
		os.startfile("installer.py")

	def rock_game(self):
		os.startfile("rock, paper, scissors game.py")

	def guess_word_game(self):
		os.startfile("guessword.py")

	def account_file(self):
		os.startfile("password.txt")

	def config_file(self):
		file = "configfile.config"
		with open(file, "w") as wri:
			wri.writelines("config_file = True;")
		messagebox.showinfo("Config File", "File Created!!")


app = QApplication(sys.argv)
app.setApplicationName("chroneOS Beta 90.9.12.13")
app.setWindowIcon(QIcon("mainIcon.jpeg"))
window = MainWindow()
app.exec_()
