#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#thislist = ["apples", "bananas", "starfruits"]

#print(thislist)

#a, b, c = "Orange", "Batag", "Pinuso"
#x = 5
#y = "name"
#print (y)

#y = 8

#print (y)

# getting user input
#user = input ("Enter a number")
#print(user)

#x = str(3)
#y = int(3)
#z = float(3)

#print(type(z))
#print(x)

#conditions
#a = 200
#b = 200
#if b > a:
#    print("b is greater than a")
#elif b < a:
#    print("b is lesser than a")
#else:
#    print("The values of the numbers cannot be compared!")

#loops
#While loop
#i = 0
#while i < 6:
#     print(i)
#     i += 1

#For loop
#fruits = ["apples", "starfruits", "melon"]
#i = 0
#j = 0
#for x in fruits:
#    print(x)
#for x in "bananas":
#    print(x)
    
#for x in range(4):
#    print(x)
    
#i = 0
#while i < 6:
#    i += 1
#    if i == 5:
#        break
#    print(i)

#i = 0
#while i < 6:
#    i += 1
#    if i == 5:
#        continue
#    print(i)

#i = 0
#j = 0
#x = "*"
#while i < 4:
#    i += 1
#    while j != 4:
#        j += 1
#        print(x * j)

#Importing modules
#import math
#import random

#functions
#def my_function(printvalue):
#    print(printvalue + "Refresher Orb")
#    return printvalue

#my_function("Axe uses ")
#my_function("Enigma uses ")
#my_function("Tidehunter uses ")

#Open and read a file
#f = open("sample.txt", "w")
#f.write("Opening a file and Writing text inside the file!")
#f.close()

#Deleting a File

#import os
#os.remove("sample.txt")

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