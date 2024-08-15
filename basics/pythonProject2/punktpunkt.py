import os

folder = os.path.join(os.path.dirname(__file__),"Ordner")

file_path = os.path.join(folder, "file.txt")
print(file_path)#C:\Users\rahma\PycharmProjects\pythonProject2\Ordner\file.txt

#vielleicht aber hat es keine .txt endung:
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    print(file)#jeweiligen filename ausgeben
    print(file_path)#vollen Dateipfad des jeweiligen files ausgeben


print(os.listdir(folder))