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
