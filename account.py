import os

print("This Account which will be created is a local account, hence it will work only in Chrone OS and not anywhere else.")

name = input("Enter An Account Name: ")
password = input("Enter An Account Password: ")

with open("name.txt", "w") as write:
    write.writelines(name)

with open("password.txt", "w") as write:
    write.writelines(password)

print("Account Created!!!")
input("Press Enter To Exit.")
os.startfile("login.py")
