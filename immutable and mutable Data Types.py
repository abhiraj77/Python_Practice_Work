# Immutable Objects: Int, String, Tuples, Float, Frozenset, etc
# Mutable Objects: List, Dictionaries, Set, etc

# Mutable Objects:

# The object state can be changed once created	
# Mutable objects are not regarded as thread-safe in nature.	
# The mutable objects are not made final, and hence the programmer can keep changing mutable objects and use the same objects.	

# Immutable Objects:

# The object state cannot be changed once created
# Immutable objects are regarded as thread-safe in nature.
# It is critical to make classes final when there is the creation of the immutable object

x3 = 2  # This is an Immutable object
y3 = [5] # This is a Mutable Object
def test3(x, y):
    y[0] += x 
    x = 12
test3(x3, y3)
print(x3)
print(y3[0])