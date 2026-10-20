# Approach: Frequency Counting + Hash Map (Grouping)
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)
#
# Count the frequency of each character using a list of 26 integers.
# Convert the frequency list into a tuple to use as a dictionary key.
# Anagrams have identical character frequencies, so they share the same key.
# Group words with the same key and return all groups as a list of lists.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a dictionary to store groups of anagrams.
        groups = {}

        for word in strs:

            # Step 1: Initialize a frequency list for 26 lowercase letters.
            count = [0] * 26

            # Step 2: Count the frequency of each character.
            for letter in word:
                # Convert the character to an index from 0 to 25.
                index = ord(letter) - ord("a")

                # Increment the frequency of the corresponding letter.
                count[index] += 1

            # Step 3: Convert the list into a hashable tuple.
            key = tuple(count)

            # Step 4: Group words with identical character frequencies.
            if key in groups:
                # Add the word to an existing group.
                groups[key].append(word)
            else:
                # Create a new group containing the word.
                groups[key] = [word]

        # Step 5: Return all grouped lists.
        return list(groups.values())


                