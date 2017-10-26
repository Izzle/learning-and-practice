# Exercise 43
# Threading in Python 3
# I'm using time.sleep() in place of some function calculation

import threading
from queue import Queue
import time


# Threading should be done when you have 2 or more tasks that need
# to access the same variable at the same time; if 2 tasks try to
# Add to the var at the same time, only the final value will be saved!
# A key concept in threading is of a 'lock': a function can 'lock'
# the variable while it is using it, and 'unlock' it when its done.

# foo

print_lock = threading.Lock()


def exampleJob(worker):
    # Simulating the time to run an intensive process
    time.sleep(0.5)
    # We 'lock' the print operation
    with print_lock:
        print(threading.current_thread().name, worker)


# Threading
def threader():
    # This will continue until the main thread dies and all daemons die
    while True:
        worker = q.get()    # Gets a worker from the Queue
        exampleJob(worker)  # Puts worker to work!
        q.task_done()       # Task is complete.


# Our Queue
q = Queue()

# Allowing 10 threads
for x in range(10):
    t = threading.Thread(target=threader)
# This step is REQUIRED by threading before you can start a thread
    t.daemon = True  # A daemon will die when its thread dies.
    t.start()

# Gets time so we can measure performance of our program.
start = time.time()

# Job assignment
for worker in range(20):
    q.put(worker)


q.join()

print('Entire job took:', time.time() - start)
