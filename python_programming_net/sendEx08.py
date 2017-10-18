# Exercise 13
# Global and Local variables in Python 3

# Local variable a
a = 6


def example():
    b = 5
    print(b)
    print(a)  # Works, we can ACCESS 'a'
    print(a + 5)  # Also works
    # a += 6 ERROR, 'a'  is not a global variable


example()

# Global variable z
z = 3


def example_two():
    global z  # makes 'z' a global variable
    print(z)
    z += 5   # This now works!
    print(z)


example_two()

# IMPORTANT!
# If you CAN'T set Global variables (big projects, sometimes bad practice)
# This is how to get around not being able to SET Global variables,
# but still harness the power of them.

x = 2


def example_three():
    globx = x    # Sets the value of x to globx, since x can still be ACCESSED
    print(globx)  # 2
    globx += 4   # Works because globx is a local variable
    print(globx)  # 6

    return globx  # returns the value of globx


x = example_three()  # x is now equal to globx!

print(x)  # 6
