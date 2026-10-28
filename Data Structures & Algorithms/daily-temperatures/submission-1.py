# Approach: Monotonic Decreasing Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# n = number of daily temperatures
#
# Use a stack to store indices of days that have not
# found a warmer future day.
#
# The temperatures at these indices are maintained
# in non-increasing order from bottom to top.
#
# Each index is pushed once and popped at most once,
# so the overall time complexity is O(n).

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        # Initialize the answer array with zeros.
        # Days without a warmer future temperature remain 0.
        answer = [0] * n

        # Store indices of days waiting for warmer temperatures.
        stack = []

        # Traverse each day's temperature.
        for i in range(n):

            # While the current day is warmer than the day
            # represented by the index at the top of the stack.
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Remove the previous colder day's index.
                prev_day = stack.pop()

                # Calculate how many days it takes
                # to reach the current warmer day.
                answer[prev_day] = i - prev_day

            # Push the current day's index onto the stack.
            # It will wait for a warmer future temperature.
            stack.append(i)

        # Return the waiting days for all temperatures.
        return answer