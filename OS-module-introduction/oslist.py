import os
folders = os.listdir("data")

print(folders,"\n")

for folder in folders:
    print(os.listdir(f"data/{folder}"))