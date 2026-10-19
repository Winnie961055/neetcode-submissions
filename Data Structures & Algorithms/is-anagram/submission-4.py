# Approach: Hash Map (Frequency Counting)
# Time Complexity: O(n + m) on average
# Space Complexity: O(n + m)
#
# Use two hash maps to count the frequency of each character
# in both strings. Then, compare the character frequencies
# to determine whether the strings are anagrams.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Initialize two dictionaries to store character frequencies.
        seen_s = {}
        seen_t = {}

        # Count how many times each character appears in s.
        for s_char in s:

            # Increment the count if the character already exists.
            if s_char in seen_s:
                seen_s[s_char] += 1
            else:
                # Otherwise, initialize its count to 1.
                seen_s[s_char] = 1

        # Count how many times each character appears in t.
        for t_char in t:

            if t_char in seen_t:
                seen_t[t_char] += 1
            else:
                seen_t[t_char] = 1

        # Anagrams must have the same string length.
        if len(s) != len(t):
            return False

        # Compare the character frequencies in both dictionaries.
        for s_char1 in seen_s:

            # Check whether the character exists in t.
            if s_char1 not in seen_t:
                return False

            # Check whether the character counts match.
            if seen_s[s_char1] != seen_t[s_char1]:
                return False

        # All characters exist in both strings with equal frequencies.
        return True