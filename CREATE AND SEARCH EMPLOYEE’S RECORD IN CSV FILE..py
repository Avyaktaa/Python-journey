import csv
def Create_Records():
    with open("employee.csv", "w", newline="") as file:
        writer = csv.writer(file)
        opt="y"
        while opt=="y":
            name=input("Enter name: ")
            age=int(input("Enter age: "))
            city=input("Enter city: ")
            writer.writerow([name,age,city])
            opt=input("Do you want to add more records? (y/n): ")
        file.close()

def Search_Records():
    with open("employee.csv", "r") as file:
        reader = csv.reader(file)
        name = input("Enter name to search: ")
        for row in reader:
            if row[0] == name:
                print("Name: ", row[0])
                print("Age: ", row[1])
                print("City: ", row[2])
                break

Create_Records()
Search_Records()
