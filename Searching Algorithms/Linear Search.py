# Linear Search. Traverses item by item and compares them.

def LinearSearch(arr, item):
    for i,j in enumerate(arr):
        if(j==item):
            print(f"Element found at {i}: {j}")
            return -1
    print("Element not found.")

array = [2, 4, 0, 1, 9]
x = 1
LinearSearch(array, x)