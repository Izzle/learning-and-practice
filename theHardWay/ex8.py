# Exercise 8: Printing, Printing
# In this exercise we are using the .format() function to turn 
# the variable 'formatter' into other strings.

# Creates a string that takes 4 arguments. Looks like an array!
formatter = "{} {} {} {}"

# Uses the .format() function to pass 4 arguments to the 
# string contained in the 'formatter' variable.
print(formatter.format(1, 2, 3, 4))

# Same as before: Passes 4 arguments to the variable 'formatter' using the .format() function
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# Passes the variable 'formatter' using the .format() function to the original 'formatter'
# variable. Since the original variable consists of 4 brackets, this should print 16 brackets!
print(formatter.format(formatter, formatter, formatter, formatter))

# The correct way to format so much information uses standard practices
print(formatter.format(
    "And the moral of the story is",
    "WORK",
    "Everybody get together with a study buddy",
    "and to talk about the FUCK that I don't give."
))

# Printing out the explanation at the end of the example.
part_intro = "In this exercise we are telling python to:"
part1 = "Take the 'formatter' string defined on line 6."
part2 = "Call its 'format' function, which is similar to telling it to do a command line command named 'format'."
part3 = "Pass to 'format' four arguments, which match up with the four {} in the 'formatter' variable. This is like passing arguments to the command line command 'format'."
part4 = "The result of calling 'format' on 'formatter' is a new string that has the {} replaced with four variables. This is what 'print' is now printing out."

# Prints out the variables containing strings of sentences and formats them with numbers and spacing.
print(f"\n{part_intro}")
print(f"1) {part1}")
print(f"2) {part2}")
print(f"3) {part3}")
print(f"4) {part4}")