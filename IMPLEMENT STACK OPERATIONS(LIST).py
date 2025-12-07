def Push_Stack():
    Doc_ID = int(input("Enter Document ID: "))
    Doc_Name = input("Enter The name of the Doctor: ")
    MOb = int(input("Enter the mobile Number of the doctore: "))
    Special = input("Enter the specialization: ")
    if Special=="ENT":
        Stack.append([Doc_ID,Doc_Name])

def Pop():
    if Stack==[]:
        print("Stack is Empty")
    else:
        print("The deleted doctor details is: ",Stack.pop())

def Peek():
    if Stack==[]:
        print("Stack is empty")
    else:
        top=len(Stack)-1
        print("The top of the stack is: ",Stack[top])

def Disp():
    if Stack==[]:
        print("Stack is empty")
    else:
        top=len(Stack)-1
        for i in range(top-1, -1):
            print(Stack)

Stack=[]
choice="y"
while choice=="y" or choice=="Y":
    print()
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. Disp")
    opt = int(input("Enter your choice: "))
    if opt==1:
        Push_Stack()
    elif opt==2:
        Pop()
    elif opt==3:
        Peek()
    elif opt==4:
        Disp()
    else:
        print("Invalid Choice Try Again!!")
    choice = input("\nDo you want to perform another operation(y/n): ")
    