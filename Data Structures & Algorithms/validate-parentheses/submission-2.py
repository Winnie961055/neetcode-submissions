# Approach: Stack + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# n = length of the input string
#
# Use a stack to keep track of opening brackets.
# Use a dictionary to map each closing bracket to its
# corresponding opening bracket.
#
# Push opening brackets onto the stack.
# When encountering a closing bracket, check whether it matches
# the most recent opening bracket at the top of the stack.
# Return False if the stack is empty or the brackets do not match.
# Finally, check whether all opening brackets have been matched.

class Solution:
    def isValid(self, s: str) -> bool:

        # Map each closing bracket to its matching opening bracket.
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # Initialize an empty stack to store opening brackets.
        stack = []

        # Step 1: Traverse each character in the string.
        for i in range(len(s)):

            # Step 2: Push opening brackets onto the stack.
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])

            else:
                # Step 3: Check whether the stack is empty.
                # A closing bracket without an opening bracket is invalid.
                if len(stack) == 0:
                    return False

                # Step 4: Check whether the top opening bracket matches.
                elif stack[-1] == matching[s[i]]:

                    # Remove the matched opening bracket.
                    stack.pop()

                else:
                    # Return False if the brackets do not match.
                    return False

        # Step 5: Return True only if no unmatched brackets remain.
        return not stack

        