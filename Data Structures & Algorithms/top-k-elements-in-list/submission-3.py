# Approach: Hash Map (Frequency Counting) + Bucket Sort
# Time Complexity: O(n) on average
# Space Complexity: O(n)
#
# n = total number of elements in nums
# k = number of most frequent elements to return
#
# Use a hash map to count the frequency of each number.
# Create buckets where each index represents a frequency.
# Group numbers with the same frequency into the same bucket.
# Traverse the buckets from highest to lowest frequency
# and return the first k numbers.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count the frequency of each number.
        # Key: number, Value: frequency
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Create n + 1 empty buckets.
        # The maximum possible frequency is n.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Group numbers by their frequencies.
        # Bucket index = frequency
        # Bucket value = list of numbers with that frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 4: Collect the k most frequent numbers.
        result = []

        # Traverse buckets from highest to lowest frequency.
        for i in range(len(buckets) - 1, -1, -1):

            # Iterate through each number in the current bucket.
            for j in range(len(buckets[i])):

                # Add the number to the result.
                result.append(buckets[i][j])

                # Return once k numbers have been collected.
                if len(result) == k:
                    return result
                    

        
            