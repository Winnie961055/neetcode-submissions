# Approach: Sliding Window + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# n = length of the input string
#
# Use a sliding window with two pointers (left and right).
# Use a Hash Map to count the frequency of each character
# in the current window.
#
# To make all characters in the window the same,
# we keep the most frequent character and replace the others.
#
# Replacements needed = Window Length - Maximum Frequency
#
# If the number of replacements exceeds k,
# shrink the window from the left until it becomes valid.
#
# Keep track of the maximum length of a valid window.
#
# Since the string contains only 26 uppercase letters,
# finding the maximum frequency takes O(1) time.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Initialize a Hash Map to store character frequencies.
        count = {}

        # Initialize the left pointer and maximum length.
        left = 0
        max_length = 0

        # Expand the sliding window by moving the right pointer.
        for right in range(len(s)):

            # Add the current character to the window.
            # Increase its frequency in the Hash Map.
            count[s[right]] = count.get(s[right], 0) + 1

            # Calculate the number of replacements needed:
            # Window Length - Maximum Character Frequency.
            #
            # If replacements exceed k, the window is invalid.
            # Keep shrinking until the window becomes valid.
            while (right - left + 1) - max(count.values()) > k:

                # Remove the leftmost character from the window
                # by decreasing its frequency.
                count[s[left]] -= 1

                # Move the left pointer to shrink the window.
                left += 1

            # The window is now valid.
            # Update the maximum length found so far.
            max_length = max(max_length, right - left + 1)

        # Return the length of the longest valid substring.
        return max_length