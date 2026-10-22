# Approach: Hash Set + Row, Column, and Box Validation
# Time Complexity: O(1) - Fixed 9x9 Sudoku board
# Space Complexity: O(1) - Each set stores at most 9 numbers
#
# Validate the Sudoku board by checking:
# 1. Each row contains no duplicate digits.
# 2. Each column contains no duplicate digits.
# 3. Each 3x3 box contains no duplicate digits.
#
# Use a hash set to detect duplicates in each group.
# Ignore empty cells represented by ".".
# Return False immediately when a duplicate is found.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Step 1: Validate all 9 rows.
        for r in range(9):

            # Return False if the current row is invalid.
            if not self.validRow(board[r]):
                return False

        # Step 2: Validate all 9 columns.
        for c in range(9):

            # Return False if the current column is invalid.
            if not self.validColumn(board, c):
                return False

        # Step 3: Validate all 9 sub-boxes.
        # Move 3 positions at a time to visit each box's top-left corner.
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                # Return False if the current 3x3 box is invalid.
                if not self.validBox(board, r, c):
                    return False

        # All rows, columns, and boxes are valid.
        return True

    def validRow(self, row):

        # Track numbers already seen in this row.
        seen = set()

        for num in row:

            # Skip empty cells.
            if num == ".":
                continue

            # Return False if the number has appeared before.
            if num in seen:
                return False

            # Record the current number.
            seen.add(num)

        # No duplicates found in this row.
        return True

    def validColumn(self, board, col):

        # Track numbers already seen in this column.
        seen = set()

        # Traverse the rows while keeping the column fixed.
        for r in range(len(board)):
            num = board[r][col]

            # Skip empty cells.
            if num == ".":
                continue

            # Return False if the number has appeared before.
            if num in seen:
                return False

            # Record the current number.
            seen.add(num)

        # No duplicates found in this column.
        return True

    def validBox(self, board, start_row, start_col):

        # Track numbers already seen in this 3x3 box.
        seen = set()

        # Traverse all 9 cells within the current 3x3 box.
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):

                # Get the current cell's value.
                num = board[r][c]

                # Skip empty cells.
                if num == ".":
                    continue

                # Return False if the number has appeared before.
                if num in seen:
                    return False

                # Record the current number.
                seen.add(num)

        # No duplicates found in this box.
        return True