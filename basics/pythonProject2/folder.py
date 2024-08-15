import os

print(__file__)#vollen Ordnerpfad des Files ausgeben (mit datei.txt am Ende)
print(os.path.dirname(__file__))#Ordnerpfad des Files ausgeben (ohne datei.txt)

#unpraktisch, wenn ich mein Projekt verschieben möchte aber trz
#auf datei.txt zugreifen will:
#with open(r"C:\Users\rahma\PycharmProjects\pythonProject2\datei.txt", "r") as file:

#besser:
#aber nicht perfekt, da zb unter mac nicht backslash\ sondern / verwendet wird
with open(os.path.dirname(__file__)+r"\datei.txt", "r") as file:
    for line in file:
        print(line)

#perfektioniert (auch für mac):
full_file_path = os.path.join(os.path.dirname(__file__), "datei.txt")
with open(full_file_path, "r") as file:
    for line in file:
        print(line)

print(os.listdir("."))
