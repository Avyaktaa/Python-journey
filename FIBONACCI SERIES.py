First=0
second=1
number = int(input("How many FIBONACCI number you want to display?: "))
if number<=0:
    print("please Enter Positive Intiger")
else:
    print(First)
    print(second)
    for num in range(2, number):
        third = First+second
        First=second
        second=third
        print(third)