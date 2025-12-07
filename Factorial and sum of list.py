def Factorial(number):
    F=1
    if number<=0:
        print("Sorry, we cannot take Factorial For Negative number")
    elif number==0:
        print("The FActorial of 0 is 1")
    else:
        for i in range(1, number+1):
            F= F+1
    print("The Factorial of",number,"is: ",F)

def Sum_List(L):
    SUm=0
    for i in range(n):
        Sum=Sum+L[i]
    print("The Sum of LIst is: ",Sum)

# Main Program

print(". To FInd Factorial")
print("2. To find sum of LIst elements")
opt= int(input("Enter your Choice: "))

if opt==1:
    n= int(input("Enter a number to find Factorial: "))
    Factorial(n)

elif opt==2:
    L=[]
    n= int(input(" Enter how many elemnts you want to store in list: "))
    for i in range(n):
        ele=int(input())
        L.append(ele)
    Sum_List(L)