def entries(a):
    n = int(input("Enter Number of student:"))
    for i in range(n):
        m = float(input("Enter percentage of student:"))
        a.append(m)
    print("Array Entries are Recorded\n\n")


def display(a):
    n = len(a)
    if n == 0:
        print("No records entered\n")
    else:
        print("Array of percentage:  ", end='  ')
        for i in range(len(a)):
            print(a[i], end='  ')
    print("\n")


def Insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    print("Array of Percentage is sorted by Insertion sort\n", a)



a = []
while True:
    print("sort by Insertion sort")
    entries(a)
    display(a)
    print("\n")
    Insertion_sort(a)
    n = len(a)
    if n >= 5:
            print("------------Top five scores----------\n")
            for i in range(n - 1, n - 6, -1):
                print(a[i], "\n")
    else:
            print("----------Top scores-----------\n")
            for j in range(n - 1, -1, -1):
                print(a[j], "\n")
