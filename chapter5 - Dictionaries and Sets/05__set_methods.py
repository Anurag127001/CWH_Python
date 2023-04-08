'''# Creating an empty set



b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6)) 

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())
print(b)

'''

# b.clear() : empties the set b
# b.uninon({8,11}) : returns a set with all items from both sets => {4,5,6,8,11}
# b.intersection({8,11}) : returns a set which contain only items in both sets => {8}
  
#   Practice Set 1
'''
d={
    "angoor" : "grapes",
    "kela" : "banana",
    "jameen" : "floor",
    "pankha" : "fan",
    "Mitti" : "soil"
    }
print("Options are ", d.keys())
m = input("Enter th hindi word from above : " )
print("The meaning of your word is : ",d.get(m))

'''

'''
# Practice set 2
o = int (input("Enter the first number : " ))
p = int( input("Enter the second number : " ))
q = int( input("Enter the third number : " ))
r = int( input("Enter the fourth number : " ))
s = int (input("Enter the fifth number : " ))
t = int (input("Enter the sixth number : " ))
u = int (input("Enter the seventh number : " ))
v = int (input("Enter the eighth number : " ))

n = {o, p, q, r, s, t, u, v}
print("The numbers you have entered are", n)'''


# Practice set 3




favLang = {}
a =input("Enter your favourite language Anurag : " )
b =input("Enter your favourite language Ajay : " )
c =input("Enter your favourite language Arya : " )
d =input("Enter your favourite language Akanksha : " )

favLang['Anurag'] = a
favLang['Ajay'] = b
favLang['Arya'] = c
favLang['Akanksha'] = d

print(favLang)
