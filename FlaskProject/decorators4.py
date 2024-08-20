def repeat(n):
    def deco(func):
        def inner():
            for i in range(0, n):
                func()

        return inner
    return deco

#f = outer()

@repeat(3)
def do_something():
    print("do_something() wurde ausgeführt")


do_something()

