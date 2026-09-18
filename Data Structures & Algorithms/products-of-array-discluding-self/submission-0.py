## Prefix／suffix product：前後綴乘積

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums) # the product of all numbers from the left of i
        suffix = [1] * len(nums) # the product of all numbers from the right of i
        ans = []

        # create prefix from left to right
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # create suffix from right to left
        for i in range(len(nums)-2, -1, -1): # (start, stop(don't include this number), step) #why len(nums)-2? 
            suffix[i] = suffix[i+1] * nums[i+1]   

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i]) 

        return ans