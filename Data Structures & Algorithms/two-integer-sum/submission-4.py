# This is a brute force and the time complexity is O(n2), space complexity is O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]