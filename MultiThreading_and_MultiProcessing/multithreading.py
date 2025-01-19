### Multithreading
## when to use Multi Threading 
### I/O-bound tasks: Tasks that spends more time wating for I/O operations(e.g file operations, requests)
#### Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time


def print_numbers():
    for i in range(5):
        
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        
        time.sleep(2)
        print(f"Letter: {letter}")

## creating 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t=time.time()

## start the thread
t1.start()
t2.start()

## these 2 threads are having 1 main thread
t1.join()
t2.join()


# print_numbers()
# print_letters()
finished_time=time.time()-t
print(finished_time)