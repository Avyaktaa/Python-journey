import math

def Square(num):
    result = math.pow(num, 2)
    print("The Square of",num,"is: ",result)
    return result

def Cube(num):
    result = math.pow(num, 3)
    print("The Cube of",num,"is: ",result)
    return result

def SquareRoot(num):
    result = math.sqrt(num)
    print("The Square Root of",num,"is: ",result)
    return result

def Factorial(num):
    result = math.factorial(num)
    print("The Factorial of",num,"is: ",result)
    return result

def Log(num):
    result = math.log(num)
    print("The Log of",num,"is: ",result)
    return result

def Quad(X,Y):
    result = math.sqrt(X**2 + Y**2)
    print("The Quad of",X,"and",Y,"is: ",result)
    return result

options = int(input("Enter your choice: "))
if options == 1:
    num = int(input("Enter a number: "))
    Square(num)
elif options == 2:
    num = int(input("Enter a number: "))
    Cube(num)
elif options == 3:
    num = int(input("Enter a number: "))
    SquareRoot(num)
elif options == 4:
    num = int(input("Enter a number: "))
    Factorial(num)
elif options == 5:
    num = int(input("Enter a number: "))
    Log(num)
elif options == 6:
    X = int(input("Enter a number: "))
    Y = int(input("Enter a number: "))
    Quad(X,Y)
else:
    print("Invalid choice")
    