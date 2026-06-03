class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left ,right = 0, len(matrix) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                left1, right1 = 0, len(matrix[mid]) - 1
                while left1 <= right1:
                    mid1 = left1 + (right1 - left1) // 2
                    if matrix[mid][mid1] > target:
                        right1 = mid1 - 1
                    elif matrix[mid][mid1] < target:
                        left1 = mid1 + 1
                    elif matrix[mid][mid1] == target:
                        return True
                return False

        return False

            
                
