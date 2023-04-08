'''# Practice Set 1

num = int(input("Enter the number : " ))
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(i*num))


# Practice Set 2

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello, " + name +".")


# Practice Set 4

num = int(input("Enter the Number: " ))
prime = True
for i in range(2, num):
    if (num%i == 0):
        prime = False
        break
if prime:    
    print("This number is Prime")
else:
    print("This number is not Prime")


# Practice Set 6

# n! = 1 x 2 x 3 x 4 x 5 x....x n
# 5! = 1 x 2 x 3 x 4 x 5

num = int(input("Enter the number: " ))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")


# Practice Set 8
n = 4
for i in range(4):
    print("*" * (i+1))

'''
# Practice Set 7
n = 3
for i in range (3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))