# Approach: Hash Set + Sequence Start Detection
# Time Complexity: O(n) on average
# Space Complexity: O(n)
#
# n = number of elements in nums
#
# Store all numbers in a hash set for O(1) average lookup.
# Only start counting when num - 1 does not exist in the set.
# This ensures each consecutive sequence is counted only once.
# Keep track of the longest sequence length.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert the array into a set to remove duplicates
        # and allow O(1) average membership checks.
        num_set = set(nums)

        # Initialize the maximum sequence length.
        max_length = 0

        # Traverse all unique numbers.
        for num in num_set:

            # Only start counting if num is the start of a sequence.
            # If num - 1 exists, this number is not a starting point.
            if (num - 1) not in num_set:

                # Initialize the current number and sequence length.
                current_num = num
                current_length = 0

                # Count consecutive numbers from this starting point.
                while current_num in num_set:

                    # Count the current number.
                    current_length += 1

                    # Move to the next consecutive number.
                    current_num += 1

                # Update the maximum sequence length.
                if current_length > max_length:
                    max_length = current_length

        # Return the longest consecutive sequence length.
        return max_length