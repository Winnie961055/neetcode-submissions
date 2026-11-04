# Approach: Binary Search on a 2D Matrix
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
#
# m = number of rows
# n = number of columns
#
# Treat the 2D matrix as a sorted 1D array
# without actually flattening it.
#
# Use Binary Search to find the target.
# Convert the middle index into row and column:
#
# row = mid // cols
# col = mid % cols
#
# Eliminate half of the search range in each iteration.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Get the number of rows and columns.
        rows = len(matrix)
        cols = len(matrix[0])

        # Initialize the search boundaries.
        # The matrix has rows * cols elements in total.
        left = 0
        right = rows * cols - 1

        # Continue searching while the range is valid.
        while left <= right:

            # Calculate the middle index.
            mid = (left + right) // 2

            # Convert the 1D index into 2D coordinates.
            row = mid // cols
            col = mid % cols

            # If the middle value is smaller than the target,
            # search the right half.
            if matrix[row][col] < target:
                left = mid + 1

            # If the middle value is larger than the target,
            # search the left half.
            elif matrix[row][col] > target:
                right = mid - 1

            # The target is found.
            else:
                return True

        # Return False if the target does not exist.
        return False

            
                
