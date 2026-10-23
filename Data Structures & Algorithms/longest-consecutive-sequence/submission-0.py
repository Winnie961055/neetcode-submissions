# Approach: Sorting + Traversal
# Time Complexity: O(n log n)
# Space Complexity: O(n) in the worst case due to Python's sorting
#
# n = number of elements in nums
#
# Sort the array so consecutive numbers become adjacent.
# Traverse the sorted array and count the length of each
# consecutive sequence while ignoring duplicate numbers.
# Keep track of the maximum sequence length.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Step 1: Handle an empty array.
        if not nums:
            return 0

        # Step 2: Sort the array in ascending order.
        nums.sort()

        # Step 3: Initialize the current and maximum lengths.
        current_length = 1
        max_length = 1

        # Step 4: Traverse the sorted array from the second element.
        for i in range(1, len(nums)):

            # Case 1: Consecutive numbers.
            # Increase the current sequence length.
            if nums[i] - nums[i - 1] == 1:
                current_length += 1

            # Case 2: Duplicate numbers.
            # Skip without changing the current sequence length.
            elif nums[i] == nums[i - 1]:
                continue

            # Case 3: Sequence is broken.
            # Reset the current sequence length to 1.
            else:
                current_length = 1

            # Step 5: Update the maximum sequence length.
            if current_length > max_length:
                max_length = current_length

        # Return the length of the longest consecutive sequence.
        return max_length