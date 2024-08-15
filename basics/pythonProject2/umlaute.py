import os
filename = os.path.join(os.path.dirname(__file__),"umlaute.txt")
print(filename)

with open(filename, "r", encoding= "utf-8") as file:
    for line in file:
        print(line)

filename_out = os.path.join(os.path.dirname(__file__),"umlaute_out.txt")
with open(filename_out, "w", encoding= "utf-8") as file:
    counter=0
    while counter < 10 :
        file.write("Müller\n")
        counter+=1