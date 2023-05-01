



'''Enumerate function is a built-in function in python that allows you to loop over a sequence such as list, tuple or string and get index and value of each element in the sequence at the same time. '''







marks = [12, 56, 32, 98, 15, 45, 4, 1]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index ==3):
#         print("Anurag, Awesome!")
#     index +=1
    



for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index ==3):
        print("Anurag, Awesome!")
    
    
    