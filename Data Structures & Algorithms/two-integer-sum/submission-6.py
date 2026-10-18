# Approach: Hash Map (Dictionary)
# Time Complexity: O(n) on average
# Space Complexity: O(n)
#
# Use a hash map to store previously seen numbers and their indices.
# For each number, calculate the complement (target - num).
# If the complement exists in the hash map, return both indices.
# Hash map lookups take O(1) time on average, reducing
# the overall time complexity from O(n^2) to O(n).

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store numbers as keys and their indices as values.
        seen = {}

        # Iterate through the array with both index and value.
        for i, num in enumerate(nums):

            # Calculate the number needed to reach the target.
            complement = target - num

            # Check if the complement has been seen before.
            if complement in seen:

                # Return the complement's index and current index.
                return [seen[complement], i]

            # Store the current number and its index.
            seen[num] = i
        
        return []