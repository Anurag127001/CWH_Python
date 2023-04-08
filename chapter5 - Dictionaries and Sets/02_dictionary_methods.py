
from turtle import update


myDict={
    'fast': 'In a quick manner',
    "harry": "A Coder",
    "anotherdict":{'harry':'Player'},
    1:2
}

# Dictionary Methods
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {"Lovish":"Friend"}
myDict.update(updateDict)
print(myDict)      

print(myDict['harry'])  

print(myDict.get('harry'))

# print(myDict['harry2'])     # Throws an error as harry2 is not present in the dictionary

# print(myDict.get('harry2')) # Returns None as harry2 is not present in the dictionary


