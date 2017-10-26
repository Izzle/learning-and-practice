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
    # We 'lock' the print operation, when print is done it releases the lock
    with print_lock:
        print(threading.current_thread().name, worker)


# Threading
def threader():
    """This will continue until the main thread dies and all daemons die.
    1) Gets a worker (Thread) from the Queue
    2) Runs that worker through exampleJob()
    3) Daemon released, worker (Thread) is sent back
    to the Queue to be given more work.
    """
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


# Our Queue
q = Queue()

# Allows 10 threads
for x in range(10):
    t = threading.Thread(target=threader)
    # This step is REQUIRED, it must be set before .start() is called.
    t.daemon = True  # A daemon will die when its thread dies.
    t.start()

# Gets time so we can measure performance of our program.
start = time.time()

# Job assignment
for worker in range(20):
    q.put(worker)


# Blocks until all items in the Queue have been gotten and processed.
#
# The count of unfinished tasks goes up whenever an item is added to the
# queue. The count goes down whenever a consumer thread calls task_done()
# to indicate the item was retrieved and all work on it is complete.
#
# When the count of unfinished tasks drops to zero, join() unblocks.
q.join()


print('\nWe had 20 processes to run that take 0.5 seconds each.\n'
      'Running linearly would take 10 seconds, but by threading...')
print('Entire job took:', time.time() - start)  # ~1 second. Damnnnnn!
