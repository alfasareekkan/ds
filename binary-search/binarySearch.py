from math import log


arr = [1, 2, 3, 5, 8, 12, 56, 76, 100]

def binarySearch(arr, target):
    """
    Iterative binary search implementation
    Returns the index of target if found, otherwise returns -1
    """
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is larger, ignore left half
        elif arr[mid] < target:
            start = mid + 1
        # If target is smaller, ignore right half
        else:
            end = mid - 1
    
    # Target not found
    return -1


# Test the function
# result = binarySearch(arr, 56)
# if result != -1:
#     print(f"Target found at index {result}")
# else:
#     print("Target not found")

# # Additional test cases
# print(f"\nSearching for 1: {binarySearch(arr, 1)}")
# print(f"Searching for 100: {binarySearch(arr, 100)}")
# print(f"Searching for 12: {binarySearch(arr, 12)}")
# print(f"Searching for 99 (not in array): {binarySearch(arr, 99)}")





def binarySearchRecursive(arr, low,high, target):
    if low > high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarySearchRecursive(arr, mid+1, high, target)
    else:
        return binarySearchRecursive(arr, low, mid-1, target)


print(binarySearchRecursive(arr,0,len(arr)-1,199))