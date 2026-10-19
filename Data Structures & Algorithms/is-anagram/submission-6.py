# Approach: Hash Map (Frequency Counting)
# Time Complexity: O(n + m) on average
# Space Complexity: O(n + m)
#
# Use two hash maps to count the frequency of each character
# in both strings. Then, compare the dictionaries directly.
# Two strings are anagrams if they contain the same characters
# with the same frequencies.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Initialize two dictionaries to store character frequencies.
        seen_s = {}
        seen_t = {}

        # Count the frequency of each character in s.
        for s_char in s:
            seen_s[s_char] = seen_s.get(s_char, 0) + 1

        # Count the frequency of each character in t.
        for t_char in t:
            seen_t[t_char] = seen_t.get(t_char, 0) + 1

        # Compare both dictionaries.
        # The keys and their corresponding frequencies must match.
        if seen_s == seen_t:
            return True

        return False