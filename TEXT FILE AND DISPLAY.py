with open("textfile.txt", "r") as file:
    contents = file.read()
    Vowels = 0
    Consonants = 0
    Lower_case = 0
    Upper_case = 0
    Digits = 0
    Special = 0
    for i in contents:
        if i.islower():
            Lower_case += 1
        elif i.isupper():
            Upper_case += 1
        elif i.isdigit():
            Digits += 1
        elif i.isalpha():
            if i in "aeiou":
                Vowels += 1
            else:
                Consonants += 1
        else:
            Special += 1
    print("Vowels: ", Vowels)
    print("Consonants: ", Consonants)
    print("Lower case: ", Lower_case)
    print("Upper case: ", Upper_case)
    print("Digits: ", Digits)
    print("Special: ", Special)