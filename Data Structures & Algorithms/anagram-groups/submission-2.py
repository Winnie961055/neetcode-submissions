# Approach: Sorting + Hash Map (Grouping)
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)
#
# Sort each word to create a grouping key.
# Anagrams will have the same sorted characters.
# Use a hash map to group words with the same key.
# Finally, return all grouped words as a list of lists.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a dictionary to store groups of anagrams.
        # Key: sorted characters
        # Value: list of words belonging to the same group
        groups = {}

        # Iterate through each word in the input list.
        for word in strs:

            # Sort the characters and join them into a string.
            # Anagrams will produce the same key.
            key = "".join(sorted(word)) # eg. sorted(word) -> ['a', 'e', 't']

            # If the key already exists, add the word to its group.
            if key in groups:
                groups[key].append(word)

            # Otherwise, create a new group containing the word.
            else:
                groups[key] = [word]

        # Convert dictionary values into a list of lists.
        # Return all groups without their keys.
        return list(groups.values())


                