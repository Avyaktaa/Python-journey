print("1. Addition")
print("2. Subraction")
print("3. Multiplication")
print("4. Division")
opt = int(input("Enter your choice: "))
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))

if opt==1:
    result = num1+num2
    print("The Addition of two number is: ",result)

elif opt==2:
    result = num1-num2
    print("The Subraction of two number is: ",result)

elif opt==3:
    result = num1*num2
    print("The Subraction of two number is: ",result)

elif opt==4:
    if num2==0:
        print("Enter any other number other than 0")
    else:
        print("The Division of two number is: ",result)
else:
    print("Invalid option")