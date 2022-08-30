# Merge Sort is based on Divide and Conquer Algorithm.
# Follow video for perfect explaination: https://www.youtube.com/watch?v=cVZMah9kEjI
# Time Complexity = nlogn
# Space Complexity = n

def MergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Recursion
        MergeSort(left_arr)
        MergeSort(right_arr)

        # Merge
        i = 0 # indx of left_array
        j = 0 # indx of right_array
        k = 0 # indx of merged array
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1], # Descending Order
        [], # Empty list
        [1,5,8,9], # Ascending Order
        [234,3,1,56,34,12,9,12,1300], # Random Array
        [5], # Single element
        [2,3,5,1,7,4,4,4,2,6,0] # Repeated Elements array
    ]
for arr in tests:
    print(f"Before Sorting: {arr}")
    MergeSort(arr)
    print(f"After  Sorting: {arr}")