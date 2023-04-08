# fruits=['Banana', 'Melon','Apple', 'Mango', 'Grapes', 'Chickoo', 'Litchi', 'Orange', 'Pear', 'Strawberry']
# for item in fruits:
#     print(item)





list = [1, 25, 45, 86, 98]

greatest_number = 0
for number in list:
    if  greatest_number < number:
        greatest_number = number

print(greatest_number)