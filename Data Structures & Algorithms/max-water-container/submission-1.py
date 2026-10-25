# Approach: Two Pointers (Greedy)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# n = number of elements in heights
#
# Use two pointers starting from both ends of the array.
# Calculate the container area using the distance between
# the pointers and the shorter of the two heights.
#
# Move the pointer with the shorter height inward,
# since moving the taller height cannot increase the area.
# Keep track of the maximum area found.

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Step 1: Initialize two pointers at both ends.
        left = 0
        right = len(heights) - 1

        # Initialize the maximum area.
        max_area = 0

        # Step 2: Continue until the pointers meet.
        while left < right:

            # Calculate the current container area.
            # Width = distance between the two pointers.
            # Height = shorter of the two vertical lines.
            area = (right - left) * min(heights[left], heights[right])

            # Step 3: Update the maximum area.
            if area > max_area:
                max_area = area

            # Step 4: Move the pointer with the shorter height.
            if heights[left] > heights[right]:

                # Right line is shorter, so move right inward.
                right -= 1

            else:

                # Left line is shorter or equal, so move left inward.
                left += 1

        # Return the maximum container area.
        return max_area


            