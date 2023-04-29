def Add_function(a, b):
    c = a + b
    print("the sum of the two numbers is: ", c, "\n")
    return c

def Sub_function(a, b):
    c = a - b
    print("the sum of the two numbers is: ", c, "\n")
    return c

def Mul_function(a, b):
    c = a * b
    print("the sum of the two numbers is: ", c, "\n")
    return c

def Div_function(a, b):
    c = a / b
    print("the sum of the two numbers is: ", c , "\n")
    return c

while input != "X":
    x = input("Choose a key to Calculate two Numbers!\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n-->")

    if x == "1":
        user = int((input ("Enter first number: ")))
        user1 = int((input ("Enter Second number: ")))
        Add_function(user, user1)
    elif x == "2":
        user = int((input ("Enter first number: ")))
        user1 = int((input ("Enter Second number: ")))
        Sub_function(user, user1)
    elif x == "3":
        user = int((input ("Enter first number: ")))
        user1 = int((input ("Enter Second number: ")))
        Mul_function(user, user1)
    elif x == "4":
        user = int((input ("Enter first number: ")))
        user1 = int((input ("Enter Second number: ")))
        Div_function(user, user1)
    else:
        print("\nThank you for using my calculator!")
        exit()