# Binary Search.

def BinarySearchIterative(arr,item):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = left + (right - left)//2
        if (arr[mid]<item):
            left = mid + 1
        elif (arr[mid]>item):
            right = mid - 1
        else:
            return mid
    return "Element not found"

def BinarySearchRecursive(arr,left,right,item):
    if left > right:
        return -1
    else:
        mid = left + (right-left)//2
        if (arr[mid] == item):
            return mid
        elif (arr[mid]<item):
            return BinarySearchRecursive(arr,mid+1,right,item)
        else:
            return BinarySearchRecursive(arr,left,mid-1,item)

array = [-1,0,3,5,9,12]
print("Calling Binary Iterative function")
print(BinarySearchIterative(array,9))
print("Calling Binary Recursive function")
print(BinarySearchRecursive(array,0,len(array),-1))