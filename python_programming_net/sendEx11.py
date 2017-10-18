# Exercise 20 Basic input game.
# INCOMPLETE: Rewrite this game with exception handling
# aka Try / Except / Finally

x = input('What is your name? ')

# Using addition doesn't add the spaces around the variable
print('Hello ' + x.title() + '. Lets play a game.')

y = input('What is your favorite color? ')
# Using this method DOES add spaces around the varible
print('Seriously?', y.title())

# A mix of both methods
print('Ok so your name is', x, 'and your favorite color is ' + y + '...')
print('Lets try something more interesting. '
      'You\'re walking alone through the woods')

z = input('when suddenly a wolf jumps out in front of you. What do you do? ')
print('..Sure you do.')
print('\nWell this game isn\'t going anywhere with someone who keeps lying.')
print('Goodbye \"' + x + "\".")
