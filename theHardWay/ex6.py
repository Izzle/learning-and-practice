# Example 6

# Declares variable for the '2 types of people' joke
types_of_people = 10
# Saves a Format string which inputs the variable to make a joke about binary
x = f"There are {types_of_people} types of people."

# Declaring variables to show how to insert variables into strings.
binary = "binary"
do_not = "don't"
# Saves another Format string which is the punchline of the joke.
y = f"Those who know {binary} and those who {do_not}."

# Prints the joke and the punchline.
print(x)
print(y)

# Prints a format string including the previous variables that contain strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Declares a variable 'hilarious' and sets it to the Bool value 'False'
hilarious = False
# A variable that contains a sentence with a parameter to insert a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the joke and passes the value of 'hilarious' as an argument to the variable 'joke_evalution'
print(joke_evaluation.format(hilarious))

# Sets up two variables, one for the West/Left side and the other for the East/Right side
w = "This is the left side of..."
e = "a string with a right side."

# Prints two strings that form a complete sentence.
print(w + e)

#
# Study Drills
#
# 1) Added comments
# 2) There are only 4 places where a string is inside of a string:
#    line 12, 19, and 20. 
# 3) Yes there are only 4 places. On line 28 we are passing a 'bool' to 
#    the string - NOT a string inside a string.

not_a_string = type(hilarious)
print(f"Proof that line 28 is passing a bool: {not_a_string}")

# 4) Adding 'w' and 'e' creates a longer string because in python strings
#    can be added together. It does so by concatenating the second string to the first.