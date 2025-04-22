# def display():
#     print('Welcome')

# display()

# -----------------------------------------

# def getdata():
#     name = input("Enter Name : ")
#     rollnum = int(input("Enter roll number : "))
#     print(name, rollnum)

# getdata()

# ---------------------------------------------

# def show():
#     print('welcome')
#     show()

# show()

# ---------------------------------------------

# def show():
#     print("Welcome with print")

# show()


# def show():
#     return "Welcome with return"

# print(show())

# ---------------------------------------------


def division():
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    if b == 0:
        print("Cannot divide by zero")
        division()
    else:
        print(a / b)


division()
