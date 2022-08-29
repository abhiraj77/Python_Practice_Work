# In Shell Sort, we first implement Insertion Sort and then change the gap between elements by wrapping the Insertion Sort Algorithm around another loop.
# There are many Sequences for the gap and we use the n//2, n//4,...1 approach.

# Shell sort is a generalized version of the insertion sort algorithm. 
# It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted.

def ShellSort(arr):
    size = len(arr)
    gap = size//2
    while gap > 0:
        i = gap
        while i < size:
            anchor = arr[i]
            j = i-gap
            while j >= 0 and arr[j] > anchor:
                arr[j+gap] = arr[j]
                j-=gap
            arr[j+gap] = anchor
            i+=1
        gap = gap//2


tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], # Descending Order
        [], # Empty list
        [1,5,8,9], # Ascending Order
        [234,3,1,56,34,12,9,12,1300], # Random Array
        [5] # Single element
    ]
    
for arr in tests:
    print(f"Before Sorting: {arr}")
    ShellSort(arr)
    print(f"After  Sorting: {arr}")