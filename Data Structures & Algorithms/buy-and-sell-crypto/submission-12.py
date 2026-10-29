# Approach: Brute Force (Nested Loops)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# n = number of days (length of prices)
#
# Use two nested loops to check every possible
# pair of buying and selling days.
#
# The outer loop selects the buying day.
# The inner loop selects a selling day after the buying day.
#
# Calculate the profit for each transaction and
# keep track of the maximum profit found.
#
# If no profitable transaction exists, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Initialize the maximum profit to 0.
        # Return 0 if all possible transactions result in a loss.
        max_profit = 0

        # Iterate through each possible buying day.
        for i in range(len(prices)):

            # Check every possible selling day after buying.
            # Starting from i + 1 ensures we buy before selling.
            for j in range(i + 1, len(prices)):

                # Calculate the profit from buying on day i
                # and selling on day j.
                # Update the maximum profit if the current
                # transaction produces a higher profit.
                if max_profit < prices[j] - prices[i]:
                    max_profit = prices[j] - prices[i]

        # Return the maximum profit across all transactions.
        return max_profit

    
        


