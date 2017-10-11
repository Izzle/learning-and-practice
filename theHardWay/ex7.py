# Exercise 7: More Printing
# aka Practice Practice Practice

# Prints the verses of "Mary had a little lamb"
print("Mary had a little lamb.")
# The end of the string has a parameter to pass an argument, in this case
# we use the '.format()' method to pass the string "snow", which appends it to the string.
print("Its fleece was white as {}.".format('snow'))
print("And everyhwere that Mary went.")
print("." * 10) # Prints 10 dots, creating a separating line.

# Assigns a variable to single letters so they can be appended together later.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Adds up each letter to spell out "Cheese Burger".
# Without end=' ' the second word would print on a newline.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') 
print(end7 + end8 + end9 + end10 + end11 + end12)