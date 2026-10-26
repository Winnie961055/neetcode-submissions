# Approach: Two Stacks (Main Stack + Min Stack)
# Time Complexity: O(1) for all operations (amortized for push)
# Space Complexity: O(n)
#
# n = number of elements in the stack
#
# Use two stacks:
# 1. Main Stack: stores all pushed values.
# 2. Min Stack: stores the minimum value at each position.
#
# Both stacks are updated together during push() and pop().
# This allows getMin() to return the current minimum in O(1)
# without searching through the entire stack.

class MinStack:

    def __init__(self):

        # Initialize the main stack to store all values.
        self.stack = []

        # Initialize the auxiliary stack to track minimum values.
        self.min_stack = []

    def push(self, val: int) -> None:

        # Step 1: Push the new value onto the main stack.
        self.stack.append(val)

        # Step 2: Update the minimum stack.

        # Case 1: The min stack is empty.
        # The first value becomes the current minimum.
        if not self.min_stack:
            self.min_stack.append(val)

        # Case 2: The new value is smaller than the current minimum.
        # Store the new value as the minimum.
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)

        # Case 3: The new value is greater than or equal to
        # the current minimum, so keep the previous minimum.
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:

        # Remove the top element from both stacks.
        # This restores the previous minimum automatically.
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:

        # Return the top element without removing it.
        return self.stack[-1]

    def getMin(self) -> int:

        # Return the current minimum from the top of min_stack.
        return self.min_stack[-1]


        
