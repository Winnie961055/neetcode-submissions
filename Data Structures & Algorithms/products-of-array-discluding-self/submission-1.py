# Approach: Prefix Product + Suffix Product
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# n = number of elements in nums
#
# Use two arrays to store prefix and suffix products.
# prefix[i] stores the product of all elements to the left of i.
# suffix[i] stores the product of all elements to the right of i.
# Multiply prefix[i] and suffix[i] to get the product of all
# elements except nums[i], without using division.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Get the length of the input array.
        n = len(nums)

        # Initialize prefix and suffix arrays with 1s.
        # 1 is the identity element for multiplication.
        prefix = [1] * n
        suffix = [1] * n

        # Step 1: Calculate prefix products from left to right.
        # Exclude the current element by using nums[i - 1].
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Step 2: Calculate suffix products from right to left.
        # Exclude the current element by using nums[i + 1].
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Step 3: Combine prefix and suffix products.
        output = []

        for i in range(len(nums)):
            # Multiply the products of all elements
            # to the left and right of the current index.
            output.append(prefix[i] * suffix[i])

        # Return the product of array except self.
        return output