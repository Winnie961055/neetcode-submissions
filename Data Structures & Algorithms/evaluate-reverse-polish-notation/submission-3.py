# Approach: Stack (Reverse Polish Notation)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# n = number of tokens
#
# Use a stack to evaluate the expression.
# Push numbers onto the stack.
# When an operator is encountered, pop two operands,
# perform the operation, and push the result back.
# Division must truncate toward zero.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Initialize a stack to store numbers and intermediate results.
        stack = []

        # Traverse each token in the expression.
        for token in tokens:

            # Case 1: Addition.
            if token == "+":

                # Pop the two most recent numbers.
                b = stack.pop()
                a = stack.pop()

                # Perform addition and push the result.
                stack.append(a + b)

            # Case 2: Subtraction.
            elif token == "-":

                b = stack.pop()
                a = stack.pop()

                # The order matters: a - b.
                stack.append(a - b)

            # Case 3: Multiplication.
            elif token == "*":

                b = stack.pop()
                a = stack.pop()

                stack.append(a * b)

            # Case 4: Division.
            elif token == "/":

                b = stack.pop()
                a = stack.pop()

                # Truncate division toward zero.
                # The order matters: a / b.
                stack.append(int(a / b))

            # Case 5: Number.
            else:

                # Convert the string token to an integer.
                stack.append(int(token))

        # Return the final result.
        return stack[-1]
