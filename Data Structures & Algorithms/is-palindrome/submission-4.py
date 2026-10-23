# Approach: Two Pointers (Opposite Direction)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# n = length of the input string
#
# Use two pointers starting from both ends of the string.
# Skip non-alphanumeric characters and compare the remaining
# characters in lowercase.
# Move both pointers inward when the characters match.
# Return False immediately if a mismatch is found.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Step 1: Initialize two pointers at both ends.
        left = 0
        right = len(s) - 1

        # Step 2: Continue until the pointers meet or cross.
        while left < right:

            # Step 3: Skip non-alphanumeric characters on the left.
            # Restart the loop to check the updated pointer.
            if not s[left].isalnum():
                left += 1
                continue

            # Step 4: Skip non-alphanumeric characters on the right.
            # Restart the loop to check the updated pointer.
            if not s[right].isalnum():
                right -= 1
                continue

            # Step 5: Compare both characters ignoring case.
            # Return False if the characters do not match.
            if s[left].lower() != s[right].lower():
                return False

            # Step 6: Move both pointers inward after a match.
            left += 1
            right -= 1

        # Step 7: All valid character pairs matched.
        return True