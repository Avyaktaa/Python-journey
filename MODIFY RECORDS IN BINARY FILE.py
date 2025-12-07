import pickle
def Create_Records():
    with open("binaryfile.dat", "wb") as file:
        while True:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            record = [name, age, city]
            pickle.dump(record, file)
            choice = input("Do you want to add more records? (y/n): ")
            if choice.lower() != "y":
                break

def Search_Records():
    with open("binaryfile.dat", "rb") as file:
        name = input("Enter name to search: ")
        while True:
            try:
                record = pickle.load(file)
                if record[0] == name:
                    print("Name: ", record[0])
                    print("Age: ", record[1])
                    print("City: ", record[2])
                    break
            except EOFError:
                break

def Modify_Records():
    with open("binaryfile.dat", "rb+") as file:
        name = input("Enter name to modify: ")
        while True:
            try:
                record = pickle.load(file)
                if record[0] == name:
                    record[1] = int(input("Enter new age: "))
                    record[2] = input("Enter new city: ")
                    file.seek(-len(record), 1)
                    pickle.dump(record, file)
                    break
            except EOFError:
                break

def Delete_Records():
    with open("binaryfile.dat", "rb+") as file:
        name = input("Enter name to delete: ")
        while True:
            try:
                record = pickle.load(file)
                if record[0] == name:
                    file.seek(-len(record), 1)
                    file.write(b"\0")
                    break
            except EOFError:
                break

def Display_Records():
    with open("binaryfile.dat", "rb") as file:
        while True:
            try:
                record = pickle.load(file)
                print("Name: ", record[0])
                print("Age: ", record[1])
                print("City: ", record[2])
            except EOFError:
                break

Create_Records()
Search_Records()
Modify_Records()
Delete_Records()
Display_Records()
