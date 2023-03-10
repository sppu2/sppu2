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


def Shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    print("Array of Percentage is Sorted by Shell sort\n\n", a)


a = []
while True:
    print("sort by Shell sort and Display top scores")
    entries(a)
    display(a)
    print("\n")
    Shell_sort(a)
    n = len(a)
    if n >= 5:
            print("------------Top five scores----------\n")
            for i in range(n - 1, n - 6, -1):
                print(a[i], "\n")
    else:
            print("----------Top scores-----------\n")
            for j in range(n - 1, -1, -1):
                print(a[j], "\n")
