# Exercise 23 Statistics in Python

import statistics as s

example_list = [17, 2, 9, 0, 33, 2, 26, 7, 42, 2, 12, 64]
print('The data:', example_list)

x = s.mean(example_list)
print('The mean is:', x)

y = s.median(example_list)
print('The median is:', y)

z = s.mode(example_list)
print('The mode is:', z)

sd = s.stdev(example_list)
print('Standard deviation:', sd)

v = s.variance(example_list)
print('Variance:', v)
