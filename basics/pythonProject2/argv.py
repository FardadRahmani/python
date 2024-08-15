#Parameter von Terminal abfangen:
import sys

print(sys.argv)
name=""
if len(sys.argv) >= 2:

    if len(sys.argv[1]) >= 10:
        name= sys.argv[1]
        with open(name, "r") as file:
            counter=0
            for line in file:
                counter +=1

            print(counter)

    else:
        name = sys.argv[1]



s= input(f"Möchtest du die Datenbank wirklich löschen, {name}? J/N")

if s == "j" or s=="J":
    print("Du hast die Datenbank gelöscht!")
    s = input("Gratulation Dummkopf!")

elif s=="n" or s=="N":
    print("Du hast die Datenbank heil gelassen!!")
    s = input("Well done!")