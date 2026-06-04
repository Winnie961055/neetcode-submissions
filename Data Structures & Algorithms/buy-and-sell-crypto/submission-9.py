class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 # buy
        right = 1 # sell
        max = 0

        while left < right and len(prices) > 1 and right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            elif prices[left] < prices[right]:
                if prices[right] - prices[left] > max:
                    max = prices[right] - prices[left]
                    right += 1
                else:
                    right += 1
            else:
                right += 1
        return max     
            
    
        


