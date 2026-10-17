# This method time complexity is O(n log n),
# there is a better way using Hash set

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort()

        if len(nums) == 0:
            return False

        num_now = nums[0]

        for i in range(1, len(nums)):
            if num_now == nums[i]:
                return True

            num_now = nums[i]

        return False
