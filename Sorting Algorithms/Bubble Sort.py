# Bubble sort. Compare 2 elements and switch them if the right one is not greater than the left one.

def BubbleSort(n):
    l = len(n)
    i, j = 0, 1 # Traversing through the elements.

    # Only 1 element exists
    if l <= 1:
        return n
    
    while i < l:
        j = 1
        print(f"Sorting array: {n}")
        while j <= l-i-1: 
            # l-i-1 is used as whenever the inner loop is run through the whole array, the largest element is sent to the right most position.
            print(f"Comparing {j-1} and {j}") # Elements that are being compared
            if n[j-1] > n[j]:
                print(f"Swapping {n[j-1]} and {n[j]}") # Swapping 
                n[j-1], n[j] = n[j], n[j-1]
                print(f"New Array = {n}\n")
            j+=1
        print("\n-------------------------")
        i+=1

    return n


n = [19,2,31,45,6,11,121,27] 
# n = [] # Empty edge case
# n = [1] # Single Element Edge Case
# n = ["a","A","b","B"] # Different data type Edge Case
print(f"Before Sorting: {n}")
A = BubbleSort(n)
print(f"After  Sorting: {A}")