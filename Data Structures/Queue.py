# Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

# Basic Operations in Queue:
# Enqueue: Add an element to the end of the Queue
# Dequeue: Remove an element from the front of the Queue
# isEmpty: Check if Queue is empty
# Peek: Get the value of the front of the Queue without removing it

# We implement Queues using queue.Queue class as if we were to use lists, 
# we would get O(N) time complexity for dequeue due to the function Q.pop(0) that is pop by position which is an O(N) function.

# Methods in queue.Queue class:
# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue

q = Queue(maxsize = 3)

print(f"Is Queue empty or not? {q.empty()}")

print("Adding elements.")
q.put(3)
q.put(2)
q.put(1)

print(f"Full queue: {q}") # Returns Queue address

print(f"Is queue full? {q.full()}")

print(f"Checking size before get element: {q.qsize()}")

print(f"Getting first element: {q.get()}")

print(f"Checking size after get element: {q.qsize()}")