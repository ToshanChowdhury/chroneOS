import sys
import os
from datetime import *
from tkinter import messagebox

datetime = datetime.now()
date = datetime.strftime("%d/%m/%y")
time = datetime.strftime("%I:%M %p")

def execute():
    print("Chrone OS CMD 1.2 released 13/4/2022")
    print("C Copyright Chrone OS 2022")
    print("")
    enter_line = input("Root:\>")
    if enter_line == "date":
        print("Date:" + " " + date)
    if enter_line == "time":
        print("Time:" + " " + time)
    if enter_line == "startpgrm":
        start_program = input("Program Name: ")
        os.startfile(start_program)
    if enter_line == "startfil":
        start_file = input("File Name: ")
        os.startfile(start_file)
    if enter_line == "mkfil":
        file = input("File Name: ")
        try:
            open(file, "a").close()
        except OSError:
            print("Failed creating the file")
        else:
            print("File created")
    if enter_line == "startfold":
        folder = input("Folder Name: ")
        os.mkdir(folder)
    if enter_line == "delfile":
        file = input("File Name: ")
        os.remove(file)
    if enter_line == "delfold":
        folder = input("Folder Name: ")
        os.rmdir(folder)
    if enter_line == "help":
        messagebox.showinfo("Command Prompt", "Open the default_cmd.py file to view the source code and learn how to use the command prompt")
    if enter_line == "exit":
        sys.exit()
    if enter_line == "rootcore /changeset.username":
        print("Do You Want To Change Your Username?")
        ask = input("Y / N: ")
        if ask == "Y":
            username = input("Enter Your New Username: ")
            with open("name.txt", "w") as u:
                u.writelines(username)
            print("Username was changed to " + username)
            input()
        if ask == "N":
            input()

while True:
    execute()