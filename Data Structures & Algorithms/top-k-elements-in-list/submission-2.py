# Approach: Hash Map (Frequency Counting) + Sorting
# Time Complexity: O(n + m log m)
# Space Complexity: O(m + k)
#
# n = total number of elements in nums
# m = number of unique elements in nums
# k = number of most frequent elements to return
#
# Use a hash map to count how often each number appears.
# Sort the (number, frequency) pairs by frequency in descending order.
# Return the first k numbers with the highest frequencies.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a dictionary to store number frequencies.
        # Key: number
        # Value: frequency
        count = {}

        # Step 1: Count the frequency of each number.
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Sort numbers by frequency in descending order.
        # count.items() returns (number, frequency) pairs.
        # x[0] = number, x[1] = frequency.
        # reverse=True sorts from highest to lowest frequency.
        sorted_count = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Step 3: Create a list to store the k most frequent numbers.
        result = []

        # Iterate through the first k pairs.
        for num, freq in sorted_count[:k]:

            # Append only the number, not its frequency.
            result.append(num)

        # Return the k most frequent elements.
        return result
            