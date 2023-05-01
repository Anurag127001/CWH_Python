import random
a = input("Enter your message here: ")

    # Encoding

word = list(a)
# print(word)
first_ltr = word[0]
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if(len(a)>=3):
    word.append(first_ltr)
    word=word[1:] 
    for i in range(3):
        ltr_end_num = random.randrange(26)
        word.append(char[ltr_end_num])
        ltr_start_num = random.randrange(26)
        word.insert(0, char[ltr_start_num])
    for j in word:
        print(j,end="") 
    print(" :is your encoded message.")
    print("\n")
else:
    code_word = a [::-1]
    print(f"Your encoded message is: {code_word}")
print("\n")
    
to_decode_word = input("Enter the word to decode: ")    
  
    # Decoding

if (len(to_decode_word)<3):
        decode_word = code_word [::-1]
        print(f"Decoded message is {decode_word}")    
else:
    for i in range (4):
        decode1=to_decode_word[i:]
        decode2=decode1[:-i]
    # print(decode1)
    # print(decode2)
    last_ltr=decode2[-1]
    decode_word= last_ltr+decode2
    decode_word=decode_word[:-1]
    print(f"Decoded answer is: {decode_word}")