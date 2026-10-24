# Approach: Sorting + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(n) in the worst case for Python sorting
# (excluding the output list)
#
# n = number of elements in nums
#
# Sort the array, then fix one number and use two pointers
# to find two other numbers whose sum equals its negative.
# Skip duplicate values to avoid returning repeated triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Step 1: Sort the array in ascending order.
        nums.sort()

        result = []

        # Step 2: Fix the first number.
        for i in range(len(nums) - 2):

            # Skip duplicate fixed numbers.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Initialize two pointers after the fixed number.
            left = i + 1
            right = len(nums) - 1

            # Step 4: Search for pairs using two pointers.
            while left < right:

                # Calculate the sum of three numbers.
                total = nums[i] + nums[left] + nums[right]

                # Case 1: Found a valid triplet.
                if total == 0:

                    # Add the triplet to the result.
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward.
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Case 2: Sum is too small.
                # Move left to increase the sum.
                elif total < 0:
                    left += 1

                # Case 3: Sum is too large.
                # Move right to decrease the sum.
                else:
                    right -= 1

        # Return all unique triplets.
        return result
        
                