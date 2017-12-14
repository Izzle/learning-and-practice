"""
*************************************************

This function shows why we use decorators.
Decorators simple wrap a fucntion, modifying its behavior.

*************************************************
"""

def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper

def just_some_function():
    print("Whee!")

# Instead of using this syntax we can use 
# the @something syntax instead as seen below
just_some_function = my_decorator(just_some_function)
just_some_function()


"""
*************************************************

The function below will do the same thing
but uses the decorator syntax.

*************************************************
"""

import time

def timing_decorator(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run function: " + str ((t2 - t1)) + "\n"
    return wrapper

# Far cleaner than our previous examples syntax
@timing_decorator
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function())


"""
*************************************************

One more real world example of decorators

*************************************************
"""

from time import sleep

def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))


"""
*************************************************
Combining everything I've learned.
I want to call a decorator instead of a decorator,
but mine only take 0 or 1 parameter. 

Since decorators are just wrapppers, I only had to think
about it for a minute. Here is my answer!
Decorators are awesome.
*************************************************
"""

"""
I had tried to use two decorators one after another and it didnt work.
for example:

    @timing_decorator
    @sleep_decorator
    def foobar():
        pass
Threw an error because timing_decorator only takes 1 function 
as a parameter. Below is my solution.
"""

@timing_decorator  # Wraps 1 function
def decorator_inception():
    print("\nHello world of decorators!")
    print(print_number(1337))  # @sleep_decorator is called by print_number()

# Our time will be over 2 seconds due to @sleep_decorator
# being inside @timing_decorator. Hurray!
print(decorator_inception())
