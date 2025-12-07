def Push_Stack(Stack,D):
    for i in D:
        Stack.append(i)

def Pop_Stack(Stack):
    if Stack==[]:
        print("Stack is Empty")
    else:
        print("The deleted doctor details is: ",Stack.pop())

def Peek_Stack(Stack):
    if Stack==[]:
        print("Stack is empty")
    else:
        top=len(Stack)-1
        print("The top of the stack is: ",Stack[top])

def Disp_Stack(Stack):
    if Stack==[]:
        print("Stack is empty")
    else:
        top=len(Stack)-1
        for i in range(top-1, -1):
            print(Stack)

Choice ="y"
D = {}
Stack = []
print("Performing Stack Operations using Dictionary\n")
while Choice=="y" or Choice=="Y":
    print()
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    opt = int(input("Enter your choice: "))
    if opt==1:
        Push_Stack(Stack,D)
    elif opt==2:
        Pop_Stack(Stack)
    elif opt==3:
        Peek_Stack(Stack)
    elif opt==4:
        Disp_Stack(Stack)
    else:
        print("Invalid Choice Try Again!!")
    Choice = input("\nDo you want to perform another operation(y/n): ")