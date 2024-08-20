
def outer(func):
    counter=0
    def inner(x):
        nonlocal counter
        print("Wurde bisher ausgeführt: " + str(counter))
        counter +=1
        return func(x)
    return inner


@outer
def calculate_something(x):
    print("calculate_something(" + str(x) + ")")
    return x*x



print(calculate_something(5))