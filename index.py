operation = input()

a = input()
b = input()

exitMessage = "Press any key to exit: "

if operation == "+":
    print(int(a)+(int(b)))
    input(exitMessage)

if operation == "-":
    print(int(a)-(int(b)))
    input(exitMessage)

if operation == "*":
    print(int(a)*(int(b)))
    input(exitMessage)

if operation == "/":
    print(int(a)/(int(b)))
    input(exitMessage)