class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = ""
        for c in s:
            if c.isalnum():
                string1 += c.lower()
        if string1 == string1[::-1]:
            return True
        return False
