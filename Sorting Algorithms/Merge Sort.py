# Merge Sort

def MergeSort(arr):
    pass

tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], # Descending Order
        [], # Empty list
        [1,5,8,9], # Ascending Order
        [234,3,1,56,34,12,9,12,1300], # Random Array
        [5] # Single element
    ]
for arr in tests:
    print(f"Before Sorting: {arr}")
    MergeSort(arr)
    print(f"After  Sorting: {arr}")