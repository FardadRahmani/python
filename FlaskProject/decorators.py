

#def outer(func):
 #   def inner():
  #      print("inner() wurde ausgeführt")
   #     func()
    #return inner

def outer(func):
    counter=0
    def inner():
        nonlocal counter
        print("Wurde bisher ausgeführt: " + str(counter))
        counter +=1
        func()
    return inner

#wir ersetzen hiermit eine Funktion durch diese Schreibweise:
#x= outer()
#print(x)
#print(x())

#Decorator: (sagt: return der anderen Funktion ist jetzt mein neues do_something()!)
@outer      #damit das klappt muss outer() ein param übergeben werden
def do_something():
    print("do_something() wurde ausgeführt")

#Decorator lässt sich auch so definieren:
# do_something = outer(do_something)

do_something()#Ausgabe: inner() wurde ausgeführt

#Wozu Decorators? siehe counter



do_something()
do_something()
do_something()