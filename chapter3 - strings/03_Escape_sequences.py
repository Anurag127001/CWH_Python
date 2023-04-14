# story = "Harry is good.\nHe is very good."
# print(story) 


# \n for new line character
# print(i, end='')      ---->   this prints values of i in same line

# Practice set
a = (input('Please enter your name: '))
print(a)
print('Good Afternoon,',a)


letter = '''Dear |name|,
You are selected !

Date: |date|'''

name =input("Enter your Name : ")
date =input("Enter today's date: ")

letter=letter.replace('|name|', name)
letter=letter.replace('|date|', date)

print(letter)


