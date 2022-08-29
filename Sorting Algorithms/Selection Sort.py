# Selection Sort is where we maintain 2 subarrays. Sorted and Unsorted Subarray. We check for minimum element in the unsorted subarray and place it just after the last element of the Sorted Subarray.

def SelectionSort(arr):
    s = 0
    while s < len(arr):
        i = s
        while i < len(arr):
            if arr[i] < arr[s]:
                arr[s], arr[i] = arr[i], arr[s]
            i+=1
        # print(f"Sorted Array till {s}: {arr}\n")
        s+=1
    return arr


tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], # Descending Order
        [], # Empty list
        [1,5,8,9], # Ascending Order
        [234,3,1,56,34,12,9,12,1300], # Random Array
        [5] # Single element
    ]
for arr in tests:
    print(f"Before Sorting: {arr}")
    arr = SelectionSort(arr)
    print(f"After  Sorting: {arr}")