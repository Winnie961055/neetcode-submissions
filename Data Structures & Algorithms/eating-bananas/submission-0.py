# Approach: Binary Search on Answer
# Time Complexity: O(n * log M)
# Space Complexity: O(1)
#
# n = number of banana piles
# M = maximum number of bananas in a single pile
#
# Use Binary Search to find the minimum eating speed k.
# The possible eating speeds range from 1 to max(piles).
#
# For each candidate speed (mid), calculate the total hours
# needed to finish all banana piles.
#
# If total_hours > h, the speed is too slow.
# Search the right half to find a faster speed.
#
# Otherwise, the speed is valid.
# Record it as the current answer and search the left half
# to find an even smaller valid speed.
#
# Each Binary Search iteration checks all n piles,
# and the search range is halved each time.

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Initialize the minimum possible eating speed.
        left = 1

        # Initialize the maximum possible eating speed.
        right = max(piles)

        # The maximum pile size is always a valid speed
        # because each pile can be finished in one hour.
        answer = right

        # Continue searching while the search range is valid.
        while left <= right:

            # Reset the total hours for each candidate speed.
            total_hours = 0

            # Calculate the middle speed.
            mid = (left + right) // 2

            # Calculate how many hours Koko needs
            # to finish all piles at the current speed.
            for pile in piles:

                # Round up because even a partially eaten pile
                # requires one full hour.
                hours = math.ceil(pile / mid)

                # Add the hours needed for this pile.
                total_hours += hours

            # Case 1: The current eating speed is too slow.
            if total_hours > h:

                # Increase the minimum speed.
                # All speeds <= mid are also too slow.
                left = mid + 1

            # Case 2: Koko can finish within h hours.
            else:

                # Record the current valid eating speed.
                answer = mid

                # Search for a smaller valid speed.
                right = mid - 1

        # Return the minimum valid eating speed.
        return answer