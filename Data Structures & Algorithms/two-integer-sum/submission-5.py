# Approach: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Use nested loops to check every possible pair of numbers.
# If their sum equals the target, return their indices.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Iterate through each number in the array.
        for i, num in enumerate(nums):

            # Check the numbers after the current index.
            # This prevents using the same element twice.
            for j in range(i + 1, len(nums)):

                # Return the indices if the sum equals the target.
                if num + nums[j] == target:
                    return [i, j]

        return []