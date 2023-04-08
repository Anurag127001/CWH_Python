 # a = None
# if (a is None):
#     print("Yes")
# else :
#     print("No")

'''---------------------------------------------------------------------------------------------------------------------'''

# Practice Set 1

a = int(input("Enter the first number: " ))
b = int(input("Enter the second number: " ))
c = int(input("Enter the third number: " ))
d = int(input("Enter the fourth number: " ))
if (a>b and a>c and a>d):
    print("The greatest number is",a)
elif (b>a and b>c and b>d):
    print("The greatest number is",b)
elif (c>b and c>a and c>d):
    print("The greatest number is",c)
else:
    print("The greatest number is",d)

'''----------------------------------------------------------------------------------------------------------------------'''
# Practice set 2

print("Please enter the percentage obtained in each of the following subjects")
math = int(input("Maths : "))
phy = int(input("Physics : "))
chem = int(input("Chemistry : "))
if(math+phy+chem>=40 and phy>=33 and math>=33 and chem>=33):
        print("The respective student has successfully Passed !")
else:
    print("Fail.")


'''------------------------------------------------------------------------------------------------------------------------'''

# Practice set 3

cmmnt= input("Please enter your Comment here:\n" )
if("make a lot of money" in cmmnt):
    spam=True
elif("buy now" in cmmnt):
    spam=True
elif("subscribe this" in cmmnt):
    spam=True
elif("click this" in cmmnt):
    spam=True
else:
    spam=False
print("\n")
if(spam):
    print("This is a SPAM Comment")
else:
    print("Thank You!")


'''-----------------------------------------------------------------------------------------------------------------------------'''

# Practice set 4

e=(input("Please enter username here : " ))
f=int(len(a))
if(f<10):
    print("Username is less than 10 characters")
else:
    print("Username is not less than 10 characters")


'''----------------------------------------------------------------------------------------------------------------------------------'''


# Practice set 5

g = input("Enter your name here : " )
myList = ['anurag', 'arya', 'shreyas', 'rohit', 'rakesh', 'atharva', 'aditya', 'ajay', 'gayatri', 'kunal', 'nitin', 'mohit', 'sanket' ]
if(g in myList):
    print('Congrats !, Your name is available in the list')
else:
    print('Sorry :( , your name is not available in the list')
    
'''-------------------------------------------------------------------------------------------------------------------------------------'''

# Practice set 6

h = int(input("Please enter the marks of the student here : \n"))
if(h<50):
    print("the respective student has obtained 'F' grade")
elif(60>h>=50):
    print("the respective student has obtained 'D' grade")
elif(70>h>=60):
    print("the respective student has obtained 'C' grade")
elif(80>h>=70):
    print("the respective student has obtained 'B' grade")
elif(90>h>=80):
    print("the respective student has obtained 'A' grade")
elif(100>h>=90):
    print("the respective student has obtained 'Excellent' grade")

'''-----------------------------------------------------------------------------------------------------------------------------------------'''

# Practice set 7

post = input("Write your post here :\n")
print("\n")
if('harry' in post):
    print("Your post is talking about harry")
else:
    print("Your post isn't talking about harry")
