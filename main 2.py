book_Library = {'1984 Orvel': 1949,
             'The Science of Interstellar': 2014,
             'Dorohedoro': 1999,
             'Dune': 1965
             }
list = list(book_Library.values())
def Sort(array):
    a = len(list)
    for i in range(a - 1):
        for j in range(0, a - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = list
Sort(array)
print("The Library is sorted by order from:")
for i in range(len(array)):
    print("%d" % array[i])