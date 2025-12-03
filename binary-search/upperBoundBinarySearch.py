arr = [1, 2, 3, 5, 5, 5, 8, 12, 56, 76, 100]


def lowerBound(arr, target):
    """
    Lower bound helper function for comparison
    Returns the index of the first element >= target
    """
    start = 0
    end = len(arr)
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    
    return start


def upperBound(arr, target):
    """
    Upper bound binary search implementation
    Returns the index of the first element > target
    If all elements are <= target, returns len(arr)
    """
    start = 0
    end = len(arr)
    
    while start < end:
        mid = (start + end) // 2
        
        # If mid element is <= target, search right half
        if arr[mid] <= target:
            start = mid + 1
        # If mid element is > target, search left half (including mid)
        else:
            end = mid
    
    return start


def upperBoundRecursive(arr, low, high, target):
    """
    Recursive upper bound binary search implementation
    Returns the index of the first element > target
    """
    if low >= high:
        return low
    
    mid = (low + high) // 2
    
    if arr[mid] <= target:
        return upperBoundRecursive(arr, mid + 1, high, target)
    else:
        return upperBoundRecursive(arr, low, mid, target)


# Test the functions
print("Array:", arr)
print()

# Test iterative version
print("Iterative Upper Bound:")
print(f"Upper bound of 5: index {upperBound(arr, 5)}")  # First element > 5 (which is 8 at index 6)
print(f"Upper bound of 4: index {upperBound(arr, 4)}")  # First element > 4 (which is 5 at index 3)
print(f"Upper bound of 1: index {upperBound(arr, 1)}")  # First element > 1 (which is 2 at index 1)
print(f"Upper bound of 100: index {upperBound(arr, 100)}")  # No element > 100, returns len(arr)
print(f"Upper bound of 0: index {upperBound(arr, 0)}")  # First element > 0 (which is 1 at index 0)
print(f"Upper bound of 200: index {upperBound(arr, 200)}")  # Beyond array

print()

# Test recursive version
print("Recursive Upper Bound:")
print(f"Upper bound of 5: index {upperBoundRecursive(arr, 0, len(arr), 5)}")
print(f"Upper bound of 4: index {upperBoundRecursive(arr, 0, len(arr), 4)}")
print(f"Upper bound of 1: index {upperBoundRecursive(arr, 0, len(arr), 1)}")
print(f"Upper bound of 100: index {upperBoundRecursive(arr, 0, len(arr), 100)}")
print(f"Upper bound of 0: index {upperBoundRecursive(arr, 0, len(arr), 0)}")
print(f"Upper bound of 200: index {upperBoundRecursive(arr, 0, len(arr), 200)}")

print()

# Comparison with lower bound
print("Comparison (Lower Bound vs Upper Bound):")
print(f"Target: 5")
print(f"  Lower bound (first >= 5): index {lowerBound(arr, 5)}")
print(f"  Upper bound (first > 5): index {upperBound(arr, 5)}")
print(f"  Range of 5: indices [{lowerBound(arr, 5)}, {upperBound(arr, 5)})")

