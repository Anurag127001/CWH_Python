a = input("Enter the number here: ")
print(f"The multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
    
# except Exception as e:
#     # print(e)


except:
    print("Sorry some error has occurred!")

print("Some important lines of the code")
print("End of the code")




try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")