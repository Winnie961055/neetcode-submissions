# Approach: Two Pointers (Opposite Direction)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# n = number of elements in numbers
#
# Since the array is sorted in ascending order,
# use two pointers starting from both ends.
#
# If the sum is smaller than the target, move the left pointer
# to increase the sum.
#
# If the sum is larger than the target, move the right pointer
# to decrease the sum.
#
# Return the 1-based indices when the target is found.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Step 1: Initialize two pointers at both ends.
        left = 0
        right = len(numbers) - 1

        # Step 2: Continue until the two pointers meet.
        while left < right:

            # Calculate the sum of the current pair.
            current_number = numbers[left] + numbers[right]

            # Case 1: The sum equals the target.
            # Return 1-based indices as required by the problem.
            if current_number == target:
                return [left + 1, right + 1]

            # Case 2: The sum is too small.
            # Move the left pointer right to increase the sum.
            elif current_number < target:
                left += 1

            # Case 3: The sum is too large.
            # Move the right pointer left to decrease the sum.
            else:
                right -= 1
        