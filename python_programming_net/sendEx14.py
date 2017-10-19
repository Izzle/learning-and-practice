# Exercise 27
# Multi-dimensional Lists and Built-in String methods

example_str = 'hello cruel world'
print(example_str)

example_str = example_str.title()
print(example_str)

x = '!'
example_str += x
print(example_str)

# Multi-dimensional lists
a = [[3, 2], [22, 12], [56, 57], [8, 9], [7, 13]]
print(a)
# Prints the third element ie the first nested list
# i.e. [56, 57]
print(a[2])
# Targets the third element, then targets the second element of that list
# i.e. [57]
print(a[2][1])

# Three dimensional list
b = [
    [[2, 2], [4, 6]],
    [[7, 2], [9, 42]],
    [[3, 13], [7, 7]]
    ]
print(b)
print('First element of the first list:', b[0])
print('Second element of previous list:', b[0][1])
print('First element of previous list:', b[0][1][0])
