try:
    l=[1, 2, 5, 8]
    i = int(input("Enter the index: "))
    print(l[i])
except IndexError:
    print("Index Error")

finally:
    print("I am always executed.")