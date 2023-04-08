name1 = 'Ava', 'Emma', 'Olivia'
name2 = 'Ava', 'Emma', 'Sophia'
n = set()
def unique_name(array1,array2):
    array = array1+array2
    for name in array:
        n.add(name)
    set_to_lst = list(n)    
    print(set_to_lst)      

unique_name(name1,name2)