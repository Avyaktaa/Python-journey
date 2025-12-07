FIle = open("textfile.txt", "w")
contents = FIle.readlines()
words = line.split()
for i in contents:
    print(i+'#',end='')
print("")
FIle.close()
