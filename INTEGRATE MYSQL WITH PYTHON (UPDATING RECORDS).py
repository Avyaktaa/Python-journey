import mysql.connector

def Insert_Records():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees"
    )
    if con.is_connected():
        cur=con.cursor()
        query="insert into employee values(%s,%s,%s,%s,%s)"
        cur.execute(query)
        print("Record inserted successfully")
    else:
        print("Table already exists")
        con.close()

def Display_Records():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees"
    )
    if con.is_connected():
        cur=con.cursor()
        query="select * from employee"
        cur.execute(query)
        print("Record displayed successfully")
    else:
        print("Table already exists")
        con.close()

choice="y"
while choice=="y" or choice=="Y":
    print()
    print("1. Insert Records")
    print("2. Display Records")
    opt = int(input("Enter your choice: "))
    if opt==1:
        Insert_Records()
    elif opt==2:
        Display_Records()
    else:
        print("Invalid Choice Try Again!!")
    choice = input("\nDo you want to perform another operation(y/n): ")