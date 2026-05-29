class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        nums = {} # value : index

        for i, n in enumerate(numbers):
            if target - n in nums:
                return [nums[target - n]+1, i+1]
            nums[n] = i