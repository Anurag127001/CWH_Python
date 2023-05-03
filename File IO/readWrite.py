# READING A FILE

m = open('myfile.txt', 'r')
# print(f)
text = m.read()
print(text)
m.close()

# WRITING A FILE

f = open('myfile.txt', 'a')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")