print ("     |", end=" ")
for i in range (1,11):
    print("{:5d}".format(i),end="")
print("")
print("----------------------------------------------------------")
for wiersz in range (1,11):
    print("{:5d}".format(wiersz), "|", sep="", end='')

    for kolumna in range(1, 11):
        print("{:5d}".format(kolumna * wiersz), end='')
    print("")



