import os

folder = os.path.join(os.path.dirname(__file__),"names")

list=[]

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            list.append(line)

counter= 0

for name in list:
    if "Max " in name:
        counter += 1


print (counter)