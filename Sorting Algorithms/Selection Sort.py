# Selection Sort is where we maintain 2 subarrays. Sorted and Unsorted Subarray. We check for minimum element in the unsorted subarray and place it just after the last element of the Sorted Subarray.

def SelectionSort(arr):
    s = 0
    while s < len(arr):
        i = s
        while i < len(arr):
            if arr[i] < arr[s]:
                arr[s], arr[i] = arr[i], arr[s]
            i+=1
        print(f"Updated array with least item at {s}: {arr}\n")
        s+=1
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [] # Empty edge case
# arr = [1] # Single Element Edge Case
# arr = ["a","A","b","B"] # Different data type Edge Case
print(f"Before Sorting: {arr}")
arr = SelectionSort(arr)
print(f"After  Sorting: {arr}")