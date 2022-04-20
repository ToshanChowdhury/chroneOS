tool_bar_colour = input("Taskbar Colour: ")
menu_bar_colour = input("Menu Bar Colour: ")
power_menu_colour = input("Power Menu Colour: ")
file_menu_colour = input("File Menu Colour: ")
system_info_menu_colour = input("System Info Menu Colour: ")
account_menu_colour = input("Account Menu Colour: ")

with open("toolbar_colour.txt", "w") as tool_bar:
	tool_bar.writelines(tool_bar_colour)

with open("menubar_colour.txt", "w") as menu_bar:
	menu_bar.writelines(menu_bar_colour)

with open("powermenu_colour.txt", "w") as power_menu:
	power_menu.writelines(power_menu_colour)

with open("filemenu_colour.txt", "w") as file_menu:
	file_menu.writelines(file_menu_colour)

with open("systeminfomenu_colour.txt", "w") as system_info:
	system_info.writelines(system_info_menu_colour)

with open("accountmenu_colour.txt", "w") as account_menu:
	account_menu.writelines(account_menu_colour)