n = int(input("Podaj liczbę:"))

while True:
    if n == 1 or n == 0:
        print(1)
        break
    else:
        silnia = 1
        for i in range(1, n+1):
            silnia *= n
        print(silnia)





