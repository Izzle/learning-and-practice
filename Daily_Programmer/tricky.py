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
# Extended unpacking
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Trick 4
# Transpoing a Matrix
matrix_A = [[1, 2, 3], [4, 5, 6]]
zipped = zip(*matrix_A)

# Trick 5
# Swap two numbers with one line of code (don't get too fancy kid)
m = 89
n = 19
n, m = m, n
print("n =", n)  # 89
print("m =", m)  # 19

# 'Trick' 6
# Negative indexing
ex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ex_list[-1])  # 10
print(ex_list[-4])  # 7

# Trick 7
# List slices with a step (a[start:end:step])
print(ex_list[::2])  # [0, 2, 4, 6, 8, 10]
print(ex_list[::3])  # [0, 3, 6, 9]
print(ex_list[::5])  # [0, 5, 10]

# Trick 8
# Naming slices (slice(start, end, step))
LASTFOUR = slice(-4, None)
print(LASTFOUR)  # slice(-4, None, None)
print(ex_list[LASTFOUR])  # [7, 8, 9, 10]
