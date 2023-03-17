# https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8

animals           = ['python','gopher']
more_animals      = animals
print(animals == more_animals) #=> True
print(animals is more_animals) #=> True
even_more_animals = ['python','gopher']
print(animals == even_more_animals) #=> True
print(animals is even_more_animals) #=> False

print('The first president of the organization..'.count('t')) #=> 4, it doesn't count the first T as it is capital

print(''.join(reversed("hello world"))) # reversed function on string needs to be joined
