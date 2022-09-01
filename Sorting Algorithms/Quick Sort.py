# Quick Sort is a Divide and Conquer Algorithm.
# Follow video for perfect explaination: https://www.youtube.com/watch?v=9KBwdDEwal8
# Time Complexity = nlogn, worst case = n^2

def QuickSort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)    # partition function to break an array and check conditions
        QuickSort(arr, left, partition_pos-1)          # Recursive function on the left side of the array
        QuickSort(arr, partition_pos+1, right)         # Recursive function on the right side of the array

def partition(arr, left, right):
    i = left            # Left Pointer
    j = right - 1       # Right Pointer
    p = arr[right]      # Pivot Pointer
    
    # We need to check i<j multiple times as their values are increasing inside another while loop

    while i < j:
        while i < right and arr[i] < p:
            i+=1
        while j > left and arr[j] > p:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > p:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i    # We need positional information as to which position has the element been sorted

array = [22,11,88,66,55,77,33,44]
QuickSort(array, 0, len(array)-1)
print(array)