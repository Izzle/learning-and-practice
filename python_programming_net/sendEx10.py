# Exercise 19 Classes


class calculator:

    def addition(x, y):
        added = x + y
        print(added)

    def subtraction(x, y):
        sub = x - y
        print(sub)

    def multiplication(x, y):
        mult = x * y
        print(mult)

    def division(x, y):
        div = x / y
        print(div)


# calls the calculator class and multiplication function
calculator.multiplication(7, 9)
calculator.division(28, 0.99)
