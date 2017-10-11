# Tricks for learning Python and troubleshooting
# 1) Write a comment above each line explaining to yourself what it does in English.
# 2) Read your ".py" file backward.
# 3) Read your ".py" file out loud, saying even the characters.

# Exercise 4: Variables and Names

# Declaring variable for number of cars
cars = 100

# Declaring variable for the number of seats per car
space_in_a_car = 4.0

# Declaring variable for the number of drivers who carpool
drivers = 30

# Declaring variable for the total number of passengers for cars
passengers = 90

# A car can only have 1 driver. By subtracting the number of drivers
# from the number of cars, you end up with the number of cars that aren't being driven
cars_not_driven = cars - drivers

# The number of cars driven must be equal to the total number of drivers
cars_driven = drivers

# Total carpool space a product of the number of cars with drivers and the
# space per car.
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers carpooling is given by the total 
# number of passengers divided by the total number of drivers who carpool.
average_passengers_per_car = passengers / cars_driven

# Outputs to user the value of each variable in context
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")