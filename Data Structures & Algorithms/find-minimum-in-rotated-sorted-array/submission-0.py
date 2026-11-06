# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# n = length of nums
#
# The array was originally sorted in ascending order
# and then rotated at some pivot.
#
# Use Binary Search to find the minimum element.
# Compare nums[mid] with nums[right] to determine
# which half contains the minimum.
#
# Keep shrinking the search range until
# left and right point to the same element.

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Initialize the search boundaries.
        left = 0
        right = len(nums) - 1

        # Continue until only one candidate remains.
        while left < right:

            # Calculate the middle index.
            mid = (left + right) // 2

            # Case 1: The minimum is to the right of mid.
            if nums[right] < nums[mid]:

                # Exclude mid and search the right half.
                left = mid + 1

            # Case 2: The minimum is at mid or to its left.
            else:

                # Keep mid because it might be the minimum.
                right = mid

        # Left and right now point to the minimum element.
        return nums[right] # either right and left works, but not mid, cause if there is only a number in the list,  e.g nums = [5], mid haven't been defined yet
            