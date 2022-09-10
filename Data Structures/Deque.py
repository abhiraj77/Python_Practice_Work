# Implementation of Deque using Colelctions class.
# https://docs.python.org/3/library/collections.html#collections.deque

from collections import deque

# Make a new deque with three items
d = deque('ghi')

# Iterate over the deque's elements
for elem in d:
    print(elem.upper())

# Adding entries
d.append('j')
d.appendleft('f')

# Popping Elements
print(f"element popped: {d.pop()}")
print(f"element popped from left: {d.popleft()}")

# Printing all elements
print(f"Elements: {list(d)}")

# Peeking leftmost and rightmost items
print(f"printing leftmost: {d[0]}\
 and rightmost items: {d[-1]}")

# addng more items:
d.extend("jkl")
d.extendleft("abc")
d.insert(5,"Inserted")

print(list(d))