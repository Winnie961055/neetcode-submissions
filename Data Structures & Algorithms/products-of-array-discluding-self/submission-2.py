# Approach: Prefix Product + Running Suffix Product
# Time Complexity: O(n)
# Extra Space Complexity: O(1) (excluding the output array)
#
# n = number of elements in nums
#
# First, store the prefix product directly in the output array.
# output[i] represents the product of all elements to the left of i.
#
# Then, traverse from right to left while maintaining a running
# suffix product (right_product). Multiply output[i] by
# right_product to include the product of all elements to the right.
#
# This avoids building separate prefix and suffix arrays.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Get the length of the input array.
        n = len(nums)

        # Initialize the output array with 1s.
        # output[i] will first store prefix products.
        output = [1] * n

        # Step 1: Store prefix products directly in output.
        # output[i] = product of all elements to the left of i
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # Step 2: Traverse from right to left and maintain
        # the product of all elements to the right of i.
        right_product = 1

        for i in range(n - 1, -1, -1):

            # Multiply the prefix product by the suffix product.
            output[i] = output[i] * right_product

            # Update the suffix product for the next iteration.
            right_product = right_product * nums[i]

        # Return the final result.
        return output