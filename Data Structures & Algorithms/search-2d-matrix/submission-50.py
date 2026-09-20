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

            l, r = 0, len(matrix[midRow]) - 1

            while l <= r:
                midCol = (l + r) // 2
                print(l, r, midCol)
                if target < matrix[midRow][midCol]:
                    r = midCol - 1
                elif target > matrix[midRow][midCol]:
                    l = midCol + 1
                else:
                    return True

        return False