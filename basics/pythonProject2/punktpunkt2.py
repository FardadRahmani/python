import os

folder = os.path.join(os.path.dirname(__file__),"Ordner")


#vielleicht aber hat es keine .txt endung:
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):#checken ob Ordner (oder zb Datei)
        print(file + " ist ein Ordner")
    else:
        print(file + " ist eine Datei")


print(os.listdir(folder))