# Prblm 1
# num1 = int(input("enter number 1:\n"))
# num2 = int(input("enter number 2:\n"))
# num3 = int(input("enter number 3:\n"))
# num4 = int(input("enter number 4:\n"))

# if num1 > num4:
#     f1 = num1
# else:
#     f1 = num4

# if num2 > num3:
#     f2 = num2
# else:
#     f2 = num3
    
# if f1 > f2:
#     print(f"{f1} is the greatest number.")
# else:
#     print(f"{f2} is the greatest number.")
    
    
    
# Prblm 2

# marks1 = int(input("Enter the marks in maths (out of 100) :\n"))
# marks2 = int(input("Enter the marks in physics (out of 100):\n"))
# marks3 = int(input("Enter the marks in chemistry (out of 100):\n"))
# total_percent = (marks1+marks2+marks3)/3
# if marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and total_percent >= 40:
#     print("YOU HAVE BEEN PROMOTED TO NEXT CLASS !")
# else:
#     print("You have been failed ! ")
    
    
    
    
# Prblm 3
    
# cmmnt = input("Enter your comment here :\n")
# spam = False

# if ("make a lot of money" in cmmnt ) :
#     spam = True
# elif("buy now" in cmmnt) :
#     spam = True
# elif("subscribe this" in cmmnt) :
#     spam = True
# elif("click this" in cmmnt) :
#     spam = True
    
# if spam == True:
#     print("This is a spam comment")
# else:
#     print("Thank you for your comment. ")



# Prblm 4

# usrNme = input("Enter username:\n")
# len_usrnme = len(usrNme)

# if len_usrnme < 10:
#     print("Enter username more than 10 characters")



# Prblm 5

# lst = ["anurag", "shiom", 'ved', "hariom", "chetan", "aniket", "swaraj"]
# usrnme = (input("Enter your name here:\n"))

# if usrnme not in lst:
#     print("Your name is not present in the list.")
# else:
#     print("Your name is present in the list.")



# Prblm 6

# mrks = int(input("Enter your marks here:\n"))

# if 100>= mrks >90 :
#     print("Excellent")
# elif 90 >= mrks >80 :
#     print("'A' Grade")
# elif 80 >=  mrks >70 :
#     print("'B' Grade")
# elif 70 >= mrks >60 :
#     print("'C' Grade")
# elif 60 >= mrks >50 :
#     print("'D' Grade")
# else :
#     print("Failed")




# Prblm 7

post = input("Write a POST here:\n")

if ("harry" or "Harry" in post ):
    print("The post is talking about Harry.")
else:
    print("The post isn't talking about Harry")