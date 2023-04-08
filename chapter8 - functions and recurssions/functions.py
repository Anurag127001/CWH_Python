'''marks1 = [45, 78, 86, 77]
percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100

marks2 = [55, 98, 83, 57]
percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100

print (percentage1, percentage2)

'''
# Instead of writing above code, since it is so lengthy, we can define a common function as follows

def percentage(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

marks1 = [45, 78, 86, 77]

marks2 = [55, 98, 83, 57]

print(percentage(marks1),  percentage(marks2))

