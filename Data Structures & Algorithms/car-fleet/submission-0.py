# Approach: Sorting + Stack
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# n = number of cars
#
# Sort cars by position in descending order,
# starting from the car closest to the target.
#
# Calculate each car's time to reach the target.
# Use a stack to track the arrival time of each fleet.
#
# If a car behind takes less than or equal time
# to reach the target than the fleet ahead,
# it will catch up and become part of that fleet.
#
# Otherwise, it forms a new fleet.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Pair each car's position with its speed.
        # Sort by position from closest to farthest from the target.
        cars = sorted(zip(position, speed), reverse=True)

        # Store the arrival times of separate car fleets.
        stack = []

        # Process cars from front to back.
        for p, s in cars:

            # Calculate the time needed to reach the target.
            time = (target - p) / s

            # Push the current car's arrival time.
            stack.append(time)

            # Check if the current car can catch up
            # with the fleet directly ahead.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                # Merge with the fleet ahead by removing
                # the current car's individual arrival time.
                stack.pop()

        # Each remaining arrival time represents one fleet.
        return len(stack)