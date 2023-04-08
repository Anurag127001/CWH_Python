a = input("Enter the first number : " )
b = input("Enter the operation (+, -, *, /, % ) : " )
c = input("Enter the second number : " )
a = int(a) 
c = int(c)
if b == "+" :
    print("The result is : ", a+c)
elif b == "-" :
    print("The result is : ", a-c)
elif b == "*" :
    print("The result is : ", a*c)
elif b == "/" :
    print("The result is : ", a/c)
elif b == "%" :
    print("The result is : ", a%c)
else :
    print("Invalid Operation")
