import os
import sys

username_info = open("name.txt")
password_info = open("password.txt")
usr_inf = username_info.read()
pas_inf = password_info.read()

username = input("User Name: ")

if username == usr_inf:
    password = input("Password: ")
    if password == pas_inf:
        print("Login Successful!! Press enter to load Chrone OS.")
        input("Press Enter To Continue.")
        os.startfile("main.py")
    else:
        print("Login Was Not Successful!!")
        input("Press Enter To Exit.")
        sys.exit()
else:
    print("Unrecognized Username.")
    input("Press Enter To Exit.")
    sys.exit()
