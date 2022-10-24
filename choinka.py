p = int(input("Podaj liczbę poziomów choinki: "))

for i in range(1, p + 1):
    for x in range(p - i):
        print(" ", end="")
    for x in range(2 * i - 1):
        print("*", end="")
    print("")


