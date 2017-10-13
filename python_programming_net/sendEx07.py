# Exercise 10, 11, & 12 
# Functions and Fuction Parameters

# Basic function. Must started with 'def' to define the function
# This function has no parameters
def example():
	print('basic function')
	z = 3 + 9
	print(z)

example() # calling the function

###########################
# Function with Parameters
def simple_addition(num1, num2):
	answer = num1 + num2
	print('num1 is', num1)
	print(answer)

simple_addition(7, 3) # calling the function and passing 2 parameters.
# simple_addition() ERROR no variables passed
# simple_addition(6) ERROR not enough variables passed
# simple_addition(6, 5, 7) ERROR too many variables passed

# CAREFUL with the order of your parameters. If you need to change the order
# you can specify the variables explicitly. Example below
simple_addition(num2=7, num1=3)

##########################
# Functions with default Parameters

def simple(num1,num2):
	pass # pass allows the compiler (interpreter?) to 
		 # skip this line instead of throwing an error
		 # since it expects there to be an Indent after defining a function

def simple(num1,num2=5): # sets a default parameter for num2
	print(num1,num2)

simple(2) # CORRECT - no error when passing only 1 parameter
		  # because there is a default value for num2
simple(2, 7) # Also works

# I'm dumb 
def practice_this_shit(remember, the, colon_at_the_end):
	pass

def seriously_its_easy(dont, forget, a_colon):
	pass

def when_defining_functions(end_it, with_a_motherfucking_colon):
	print('I think I\'ll remember this now')

# Back to the lesson
def basic_window(width, height, font="TNR", 
				 bgc='white', scrollbar=True):
	print(width,height,font,bgc) 

basic_window(500, 350) # Only really have to specify width and height
basic_window(500, 350, 'a') # WORKS - but bad idea. 
basic_window(500, 350, bgc='black') # BETTER way than the previous line