from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Search Insert Position - LeetCode 35
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
        where it would be if it were inserted in order.
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return start


# Test the Solution class
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Target exists in array
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"nums = {nums1}, target = {target1}")
    print(f"Output: {solution.searchInsert(nums1, target1)}")  # Expected: 2
    print()
    
    # Test case 2: Target should be inserted at beginning
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"nums = {nums2}, target = {target2}")
    print(f"Output: {solution.searchInsert(nums2, target2)}")  # Expected: 1
    print()
    
    # Test case 3: Target should be inserted at end
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"nums = {nums3}, target = {target3}")
    print(f"Output: {solution.searchInsert(nums3, target3)}")  # Expected: 4
    print()
    
    # Test case 4: Target should be inserted at position 0
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(f"nums = {nums4}, target = {target4}")
    print(f"Output: {solution.searchInsert(nums4, target4)}")  # Expected: 0
    print()
    
    # Test case 5: Single element - found
    nums5 = [1]
    target5 = 1
    print(f"nums = {nums5}, target = {target5}")
    print(f"Output: {solution.searchInsert(nums5, target5)}")  # Expected: 0
    print()
    
    # Test case 6: Single element - insert before
    nums6 = [1]
    target6 = 0
    print(f"nums = {nums6}, target = {target6}")
    print(f"Output: {solution.searchInsert(nums6, target6)}")  # Expected: 0
    print()
    
    # Test case 7: Single element - insert after
    nums7 = [1]
    target7 = 2
    print(f"nums = {nums7}, target = {target7}")
    print(f"Output: {solution.searchInsert(nums7, target7)}")  # Expected: 1
    print()
    
    # Test case 8: Target exists at first position
    nums8 = [1, 3, 5, 6]
    target8 = 1
    print(f"nums = {nums8}, target = {target8}")
    print(f"Output: {solution.searchInsert(nums8, target8)}")  # Expected: 0
    print()
    
    # Test case 9: Target exists at last position
    nums9 = [1, 3, 5, 6]
    target9 = 6
    print(f"nums = {nums9}, target = {target9}")
    print(f"Output: {solution.searchInsert(nums9, target9)}")  # Expected: 3
