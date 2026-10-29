# Approach: One Pass (Running Minimum)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# n = number of days (length of prices)
#
# Traverse the prices array from left to right.
# Keep track of the lowest buying price seen so far.
#
# For each day, calculate the profit if we sell
# at the current price.
#
# Update the maximum profit whenever we find
# a more profitable transaction.
#
# Since we only consider past and current prices,
# the buying day always comes before the selling day.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Initialize the minimum price with the first day's price.
        min_price = prices[0]

        # Initialize the maximum profit to 0.
        # Return 0 if no profitable transaction exists.
        max_profit = 0

        # Traverse each day's stock price.
        for i in range(len(prices)):

            # Update the minimum buying price if
            # the current price is lower.
            if prices[i] < min_price:
                min_price = prices[i]

            # Calculate the profit if we sell today.
            # Update the maximum profit if it is higher.
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        # Return the maximum profit found.
        return max_profit

    
        


