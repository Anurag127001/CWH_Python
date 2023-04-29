# Factorial(7) = 7*6*5*4*3*2*1
# factorial(0) = 1

def factorial(n) :
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
    
print(factorial(5))


# fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# f0 = 0
# f1 = 1
# f2 = f1 + f0
def fibonacci(n) : 
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(6)

    
for i in range(10):
    print(fibonacci(i), end=" ")
