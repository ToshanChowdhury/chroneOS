def exec():
    print("""Calculator
    
    + = Add
    - = Subtract
    * = Multiply
    / = Divide
    
    """)
    choice = input("Operation: ")

    if choice == "+":
        x = int(input("First Number: "))
        print("+")
        y = int(input("Second Number: "))
        z = str(x + y)
        print("")
        print("The Answer Is: " + z)
        input()

    if choice == "-":
        x = int(input("First Number: "))
        print("-")
        y = int(input("Second Number: "))
        z = str(x - y)
        print("")
        print("The Answer Is: " + z)
        input()

    if choice == "*":
        x = int(input("First Number: "))
        print("*")
        y = int(input("Second Number: "))
        z = str(x * y)
        print("")
        print("The Answer Is: " + z)
        input()

    if choice == "/":
        x = int(input("First Number: "))
        print("/")
        y = int(input("Second Number: "))
        z = str(x / y)
        print("")
        print("The Answer Is: " + z)
        input()


while True:
    exec()