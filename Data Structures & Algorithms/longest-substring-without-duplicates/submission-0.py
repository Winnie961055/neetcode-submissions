class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set() # use to see if there is duplicate
        left = 0
        maxCount = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxCount = max(maxCount, right - left + 1)
        return maxCount
