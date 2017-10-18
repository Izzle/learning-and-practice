# Alternative version of sendEx12.py

from statistics import mean, median, mode, variance as v, stdev

example_list = [17, 2, 9, 0, 33, 2, 26, 7, 42, 2, 12, 64]
print('Our numbers are:', example_list)


def stats(stat_rule, list=example_list):

    ans = stat_rule(list)
    # __name__ gives you the name attribute of any class, function, or module
    print('The ', stat_rule.__name__, ' of our list is: ', ans)


stats(mean)
stats(median)
stats(mode)
stats(v)
stats(stdev)
