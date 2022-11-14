"""Napisz funkcję tworzącą listę wszystkich lat przestępnych z podanego przedziału. Przypominam,
że rok jest przestępny, jeżeli jest podzielny przez 4, ale nie jest podzielny przez 100, chyba,
że jest podzielny przez 400. Ciało funkcji ma się składać z jednej linijki kodu zawierającej list comprehension.
Wywołaj napisaną funkcję do wygenerowania listy lat przestępnych w latach 1900-2000."""

def leap_years(start, end):
    return [year for year in range(start, end + 1) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)]

def main():
    print("Wszystkie lata przestępne z zakresu 1900 - 2000: ", leap_years(1900, 2000))

if __name__ == "__main__":
    main()






