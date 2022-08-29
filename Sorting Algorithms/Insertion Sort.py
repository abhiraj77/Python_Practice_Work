# Insertion Sort is where we insert an element to it's correct position while comparing 2 adjacent elements and pushing the larger one ahead.

def InsertionSort(arr):
    i = 1
    while i < len(arr):
        anchor = arr[i]
        j = i-1
        # print(f"Comparing {j}, {i}")
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            # print(f"Pushing element up: {arr}")
        arr[j+1] = anchor
        i+=1
        # print(arr)
        # print("--------------\n")
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
    arr = InsertionSort(arr)
    print(f"After  Sorting: {arr}")