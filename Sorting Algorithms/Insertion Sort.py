# Insertion Sort is where we insert an element to it's correct position while comparing 2 adjacent elements and pushing the larger one ahead.

def InsertionSort(arr):
    i = 1
    while i < len(arr):
        a = arr[i]
        j = i-1
        print(f"Comparing {j}, {i}")
        while j >= 0 and a < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            print(f"Pushing element up: {arr}")
        arr[j+1] = a
        i+=1
        print(arr)
        print("--------------\n")
    return arr

arr = [2, 19,31,45,30,11,121,27]
print(f"Before Sorting: {arr}")
arr = InsertionSort(arr)
print(f"After  Sorting: {arr}")