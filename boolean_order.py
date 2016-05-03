# Boolean operators are not evaluated from left to right.
# There's an order of operations for boolean operators:
# "not" is evaluated first, "and" is evaluated next, "or" is evaluated last.
name = "John"
age = 17

print(name == "John" or not age > 17)

print(name == "John" or not age > 17)

print(name == "Ellie" or not name == "John" and age == 17)