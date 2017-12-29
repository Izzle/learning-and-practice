# Countdown to a specific date
# In this case, the date that I should be prepared as a developer
# in order to start applying for jobs.

from datetime import datetime as dt


delta = dt(2018, 6, 1) - dt.now()

print(delta)
