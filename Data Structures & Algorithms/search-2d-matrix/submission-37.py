class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        l = 0
        r = rows - 1

        while l <= r:
            midRow = (l + r) // 2
            print("l: ", l, "r: ", r, "midRow: ", midRow)
            if target < matrix[midRow][0]:
                r = midRow - 1
                continue

            if target > matrix[midRow][len(matrix[midRow]) - 1]:
                l = midRow + 1
                continue

            if (target >= matrix[midRow][0] and target <= matrix[midRow] [len(matrix[midRow]) - 1]):
                return target in matrix[midRow]

        return False