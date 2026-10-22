# Approach: One-Pass Hash Set (Dictionary of Sets)
# Time Complexity: O(1) for a fixed 9x9 board
# Space Complexity: O(1) for a fixed 9x9 board
#
# Use three dictionaries of sets to track numbers seen in:
# 1. Each row
# 2. Each column
# 3. Each 3x3 box
#
# Traverse the board once and return False if any duplicate
# is found in the current row, column, or box.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Initialize dictionaries to store sets of seen numbers.
        rows = {}
        cols = {}
        boxes = {}

        # Create an empty set for each row and column.
        for i in range(9):
            rows[i] = set()
            cols[i] = set()

        # Create an empty set for each 3x3 box.
        # Each box is identified by a tuple (box_row, box_col).
        for r in range(3):
            for c in range(3):
                boxes[(r, c)] = set()

        # Traverse all 81 cells of the Sudoku board.
        for r in range(9):
            for c in range(9):

                # Get the current cell's value.
                num = board[r][c]

                # Ignore empty cells.
                if num == ".":
                    continue

                # Identify the 3x3 box containing this cell.
                box_key = (r // 3, c // 3)

                # Return False if the number already exists
                # in the current row, column, or 3x3 box.
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_key]):
                    return False

                # Record the number in all three sets.
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_key].add(num)

        # No duplicates were found.
        return True