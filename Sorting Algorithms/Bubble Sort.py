# Bubble sort. Compare 2 elements and switch them if the right one is not greater than the left one.

def BubbleSort(n):
    l = len(n)
    i, j = 0, 1 # Traversing through the elements.

    # Only 1 element exists
    if l <= 1:
        return n
    
    while i < l:
        j = 1
        # print(f"Sorting array: {n}")
        while j <= l-i-1: 
            # l-i-1 is used as whenever the inner loop is run through the whole array, the largest element is sent to the right most position.
            # print(f"Comparing {j-1} and {j}") # Elements that are being compared
            if n[j-1] > n[j]:
                # print(f"Swapping {n[j-1]} and {n[j]}") # Swapping 
                n[j-1], n[j] = n[j], n[j-1]
                # print(f"New Array = {n}\n")
            j+=1
        # print("\n-------------------------")
        i+=1

    return n

tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], # Descending Order
        [], # Empty list
        [1,5,8,9], # Ascending Order
        [234,3,1,56,34,12,9,12,1300], # Random Array
        [5] # Single element
    ]
for n in tests:
    print(f"Before Sorting: {n}")
    A = BubbleSort(n)
    print(f"After  Sorting: {A}")