# Approach: Hash Set
# Time Complexity: O(n) on average
# Space Complexity: O(n)
#
# A hash set allows us to check whether an element
# has already appeared in O(1) time on average.
# This improves the time complexity from O(n log n)
# (sorting approach) to O(n).

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create an empty set to store previously seen numbers.
        # Note: {} creates an empty dictionary, not an empty set.
        seen = set() 

        for num in nums:
            
            # If the number has been seen before, a duplicate exists.
            if num in seen:
                return True
            # Otherwise, add the number to the set.
            seen.add(num)
        
        # No duplicates were found.
        return False

    

        
