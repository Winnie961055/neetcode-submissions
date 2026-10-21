# Approach: Length Prefix Encoding + String Parsing
# Time Complexity: O(L) for both encode and decode
# Space Complexity: O(L) for both encode and decode
#
# L = total length of the encoded string
#
# Encode:
# Use the format "length#word" to encode each string.
# Store each encoded segment in a list, then join them into
# a single string to avoid repeated string concatenation.
#
# Decode:
# Use two pointers (i and j) to locate the delimiter '#'.
# Extract the length and use string slicing to recover
# each original word. Repeat until the entire string is decoded.

class Solution:

    def encode(self, strs: List[str]) -> str:

        # Create a list to store encoded segments.
        parts = []

        for word in strs:

            # Step 1: Get the length of the word.
            length = len(word)

            # Step 2: Convert the length to a string.
            length_str = str(length)

            # Step 3: Encode the word using "length#word".
            list_str = length_str + "#" + word

            # Step 4: Append the encoded segment to the list.
            parts.append(list_str)

        # Join all encoded segments into a single string.
        return "".join(parts)

    def decode(self, s: str) -> List[str]:

        # Create a list to store the decoded strings.
        result = []

        # Initialize the pointer at the beginning of the string.
        i = 0

        # Continue until the entire encoded string is processed.
        while i < len(s):

            # Step 1: Use j to find the delimiter '#'.
            j = i

            # Move j forward until it reaches '#'.
            while s[j] != "#":
                j += 1

            # Step 2: Extract the word length.
            # s[i:j] contains the characters before '#'.
            length = int(s[i:j])

            # Step 3: Extract the original word using slicing.
            # The word starts after '#' and contains length characters.
            word = s[j + 1:j + 1 + length]

            # Step 4: Append the decoded word to the result.
            result.append(word)

            # Step 5: Move i to the beginning of the next segment.
            i = j + 1 + length

        # Return the list of decoded strings.
        return result
