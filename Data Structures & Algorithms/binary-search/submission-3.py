# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# n = length of nums
#
# The array is sorted in ascending order.
# Use two pointers to maintain the search range.
# Compare the middle element with the target.
# Eliminate half of the search range in each iteration.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize the left and right boundaries.
        left = 0
        right = len(nums) - 1

        # Continue searching while the range is valid.
        while left <= right:

            # Calculate the middle index of the current range.
            mid = (left + right) // 2

            # If the middle value is smaller than the target,
            # search the right half.
            if nums[mid] < target:
                left = mid + 1

            # If the middle value is larger than the target,
            # search the left half.
            elif nums[mid] > target:
                right = mid - 1

            # The target is found.
            else:
                return mid

        # Return -1 if the target does not exist.
        return -1
