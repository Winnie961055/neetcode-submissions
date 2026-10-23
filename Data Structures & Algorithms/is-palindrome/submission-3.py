# Approach: String Cleaning + Reversal
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# n = length of the input string
#
# Remove all non-alphanumeric characters and convert
# the remaining characters to lowercase.
# Then, reverse the cleaned string and compare it
# with the original cleaned string to check if it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Step 1: Initialize a list to store valid characters.
        chars = []

        # Step 2: Traverse each character in the input string.
        for char in s:

            # Keep only alphanumeric characters (letters and digits).
            if char.isalnum():

                # Convert the character to lowercase and add it to the list.
                chars.append(char.lower())

        # Step 3: Join the characters into a single string.
        cleaned = "".join(chars)

        # Step 4: Reverse the cleaned string and compare.
        # Return True if both strings are identical.
        return cleaned == cleaned[::-1]
