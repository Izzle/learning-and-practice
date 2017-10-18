print('This is an example of a print function')

print('He said "Hi."')

print("We're going to the store!")
# Used single quotes, requires the \ escape character.
print('We\'re going to the store!')

# print('Hi' + 5) WONT WORK, can't add Str to Int
print('Hi', 5)  # Correct way to format it
print('Hi ' + str(5))  # Converts the 5 to a string

# print('8' + 5) WONT WORK, cant add a Str to Int
print(int('8') + 5)  # converts the str '8' to an integer

# print(int('8.5') + 5) WONT WORK, must be converted from Str -> Float
print(float('8.5') + 5)
