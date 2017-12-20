'''Python tricks, hacks, and work-arounds
   
   A living document by Ron Martin
'''


# Trick 1
# Create a single string from all the elements in a list
a = ['Ron', 'loves', 'to', 'code', 'in', 'Python']
print(" ".join(a))

# Trick 2 (less of a trick, more of a reminder)
# Multi-variable assignment
b = [3, 2, 1]
x, y, z = b
print(x, y, z)

# Trick 3
# Transpoing a Matrix
matrix_A = [[1, 2, 3], [4, 5, 6]]
zipped = zip(*matrix_A)
