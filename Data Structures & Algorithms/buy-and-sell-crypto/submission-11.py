class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # nested loop
        # time complexity : O(N^2)
        # space complexity: O(1)

        max_profit = 0

        for i in range(len(prices)):

            for j in range(i+1, len(prices)):

                if max_profit < prices[j] - prices[i]:

                    max_profit = prices[j] - prices[i]
        
        return max_profit

    
        


