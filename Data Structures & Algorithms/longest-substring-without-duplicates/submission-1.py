# Approach: Sliding Window + Hash Set
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))
#
# n = length of the input string
# k = number of possible unique characters
#
# Use two pointers (left and right) to maintain a sliding window.
# Use a Hash Set to track the unique characters in the window.
#
# Expand the window by moving the right pointer.
# If a duplicate character is found, shrink the window
# from the left until the duplicate is removed.
#
# Keep track of the maximum length of a valid window.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Initialize a set to store unique characters
        # in the current sliding window.
        seen = set()

        # Initialize the left pointer and maximum length.
        left = 0
        max_length = 0

        # Move the right pointer through the entire string.
        for right in range(len(s)):

            # If the current character already exists in the window,
            # shrink the window until the duplicate is removed.
            while s[right] in seen:

                # Remove the leftmost character from the set.
                seen.remove(s[left])

                # Move the left pointer one position to the right.
                left += 1

            # Add the current character to the window.
            seen.add(s[right])

            # Update the maximum length of a valid window.
            if len(seen) > max_length:
                max_length = len(seen)

        # Return the length of the longest substring
        # without repeating characters.
        return max_length