class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        cols = len(matrix)
        l, r = 0, cols - 1

        while l <= r:
            midRow = l + (r - l) // 2

            if matrix[midRow][-1] > target and matrix[midRow][0] > target:
                r = midRow - 1

            elif matrix[midRow][-1] < target and matrix[midRow][0] < target:
                l = midRow + 1

            else:
                l, r = 0, len(matrix[midRow])

                while l <= r:
                    midCol = l + (r - l) // 2

                    if matrix[midRow][midCol] > target:
                        r = midCol - 1
                    elif matrix[midRow][midCol] < target:
                        l = midCol + 1
                    else:
                        return True
        return False
