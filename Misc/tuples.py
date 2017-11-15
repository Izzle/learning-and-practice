""" Notes to self:
Unlike lists, tuples are immutable (also see named tuples).
Tuples are constructed by a comma operator enclosed in parentheses,
for example (a, b, c). A single item tuple must have a trailing comma, such as (d,).
"""
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print(len(alphabet))
print(alphabet[17], alphabet[14], alphabet[13])