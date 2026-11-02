# Approach: Fixed-size Sliding Window + Hash Map
# Time Complexity: O(m + n)
# Space Complexity: O(1)
#
# m = length of s1
# n = length of s2
#
# Use two Hash Maps to store character frequencies:
# 1. count1 stores the frequencies of characters in s1.
# 2. count2 stores the frequencies of characters in the current window of s2.
#
# Maintain a sliding window with a maximum size of len(s1).
# Expand the window by moving the right pointer.
# If the window becomes too large, remove the leftmost character
# and move the left pointer forward.
#
# Remove keys with zero frequency to ensure accurate
# dictionary comparisons.
#
# If count1 == count2, the current window is a permutation of s1.
#
# Since the strings contain only 26 lowercase English letters,
# dictionary comparisons take O(1) time.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Initialize two Hash Maps to track character frequencies.
        count1 = {}
        count2 = {}

        # Initialize the left pointer of the sliding window.
        left = 0

        # Step 1: Count the frequency of each character in s1.
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1

        # Step 2: Expand the sliding window through s2.
        for right in range(len(s2)):

            # Add the current character to the window.
            # Increase its frequency in count2.
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            # Step 3: Keep the window size at most len(s1).
            if right - left + 1 > len(s1):

                # Decrease the frequency of the outgoing character.
                count2[s2[left]] -= 1

                # Remove the key if its frequency becomes zero.
                # Otherwise, dictionary equality may fail.
                if count2[s2[left]] == 0:
                    del count2[s2[left]]

                # Move the left pointer one position forward.
                left += 1

            # Step 4: Compare the character frequencies.
            # Equal dictionaries mean the window contains
            # exactly the same characters as s1.
            if count1 == count2:
                return True

        # No permutation of s1 was found in s2.
        return False
            
