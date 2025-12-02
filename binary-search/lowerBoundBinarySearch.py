arr = [1, 2, 3, 5, 5, 5, 8, 12, 56, 76, 100]


def lowerBound(arr, target):
    """
    Lower bound binary search implementation
    Returns the index of the first element >= target
    If all elements are smaller than target, returns len(arr)
    """
    start = 0
    end = len(arr)
    
    while start < end:
        mid = (start + end) // 2
        
        # If mid element is less than target, search right half
        if arr[mid] < target:
            start = mid + 1
        # If mid element is >= target, search left half (including mid)
        else:
            end = mid
    
    return start


def lowerBoundRecursive(arr, low, high, target):
    """
    Recursive lower bound binary search implementation
    Returns the index of the first element >= target
    """
    if low >= high:
        return low
    
    mid = (low + high) // 2
    
    if arr[mid] < target:
        return lowerBoundRecursive(arr, mid + 1, high, target)
    else:
        return lowerBoundRecursive(arr, low, mid, target)


# Test the functions
print("Array:", arr)
print()

# Test iterative version
print("Iterative Lower Bound:")
print(f"Lower bound of 5: index {lowerBound(arr, 5)}")  # First occurrence of 5
print(f"Lower bound of 4: index {lowerBound(arr, 4)}")  # 4 not in array, returns index of 5
print(f"Lower bound of 1: index {lowerBound(arr, 1)}")  # First element
print(f"Lower bound of 100: index {lowerBound(arr, 100)}")  # Last element
print(f"Lower bound of 200: index {lowerBound(arr, 200)}")  # Beyond array

print()

# Test recursive version
print("Recursive Lower Bound:")
print(f"Lower bound of 5: index {lowerBoundRecursive(arr, 0, len(arr), 5)}")
print(f"Lower bound of 4: index {lowerBoundRecursive(arr, 0, len(arr), 4)}")
print(f"Lower bound of 1: index {lowerBoundRecursive(arr, 0, len(arr), 1)}")
print(f"Lower bound of 100: index {lowerBoundRecursive(arr, 0, len(arr), 100)}")
print(f"Lower bound of 200: index {lowerBoundRecursive(arr, 0, len(arr), 200)}")

