import mysql.connector

def Create_DB():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    try:
        if con.is_connected():
            cur=con.cursor()
            qurey="create database employees"
            cur.execute(qurey)
            print("Database created successfully")
    except:
        print("Database already exists")
        con.close()

def Create_Table():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employees"
    )
    if con.is_connected():
        cur=con.cursor()
        query="create table employee(id int(10) primary key, name varchar(20), age int(10), gender varchar(10), salary int(10))"
        cur.execute(query)
        print("Table created successfully")
    else:
        print("Table already exists")
        con.close()

choice="y"
while choice=="y" or choice=="Y":
    print()
    print("1. Create Database")
    print("2. Create Table")
    opt = int(input("Enter your choice: "))
    if opt==1:
        Create_DB()
    elif opt==2:
        Create_Table()
    else:
        print("Invalid Choice Try Again!!")
    choice = input("\nDo you want to perform another operation(y/n): ")