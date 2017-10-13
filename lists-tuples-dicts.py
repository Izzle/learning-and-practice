# Lists are created with brackets, similar to an array in JavaScript
# "homogeneous sequences" - mutable

stats = [22, 33, 53, 253.2, 9595, 6]
print(stats[3])

# Tuples are created with parentheses and commas
# A single item tuple must have a trailing comma
# "heterogeneous data structures" - immutable

info = ("USA", 1776, "George Washington")
print(info[0:2])  # tuples are indexed

# Dictionaries are created using curly brackets and use key:value pairs
# Dict items are referenced by key instead of index

employeeNum = {"Ron": 924, "Jeff": 208, "Vache": 313, "Jess": 842, "Justin": 667}

print(employeeNum["Ron"])

print(employeeNum.keys())  # D.keys() lists all keys in a dict; D.values() does the same for values
del employeeNum['Justin']  # 'Justin' & "Justin" both work
print(employeeNum.keys())