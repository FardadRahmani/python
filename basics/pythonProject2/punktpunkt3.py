import os
#ich möchte datei2.txt in Ordner/Unterordner öffnen:
filename = os.path.join(os.path.dirname(__file__),"Ordner","UnterOrdner","datei2.txt")
print(filename)


with open(filename, "r") as file:
    for line in file:
        print(line)





#vielleicht aber hat es keine .txt endung:
# for file in os.listdir(folder):
#     file_path = os.path.join(folder, file)
#     if os.path.isdir(file_path):#checken ob Ordner (oder zb Datei)
#         print(file + " ist ein Ordner")
#     else:
#         print(file + " ist eine Datei")
#
#
# print(os.listdir(folder))