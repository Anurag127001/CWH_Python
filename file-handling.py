#   READING A FILE

f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()


# WRITING A FILE

f = open('myfile.txt', 'w')
f.write('Hello, world!')
f.close()


#  Appending a File



f = open('myfile.txt', 'a')
f.write('Hello, world! ')
f.close()


