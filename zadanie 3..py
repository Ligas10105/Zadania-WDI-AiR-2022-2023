"""Napisz funkcję znajdującą wspólne elementy dwóch sekwencji (list, krotek lub napisów).
 Znalezione wspólne elementy mają być zwracane jako lista (każdy element w tej liście ma wystąpić tylko raz!)
Uzupełnienie wykładu:
W list comprehension może wystąpć pętla zagnieżdżona np.:
[x**y for x in range (1,4) for y in range (2,5) ]
stworzy listę liczb będących 2, 3 i 4 potęgą  liczb z zakresu 1-3"""

def common_elements(sequence1, sequence2):
    return list(set(sequence1).intersection(set(sequence2)))

def common_elements2(sequence1, sequence2):
    return [x for x in sequence1 for y in sequence2 if x == y]

def main():
    print(common_elements2(("1", "2", 3, "4", 10, 4), [1, 10, 3, 11, 12]))
    print(common_elements2(("1", "2", 3, "4", 10, 4), ["1", "10", "3", "11", "12"]))

if __name__ == "__main__":
    main()

