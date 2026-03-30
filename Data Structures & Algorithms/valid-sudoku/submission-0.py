class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # isRowValid
        for i in range(len(board)):
            seen = []
            for j in range(len(board)):
                if board[i][j] in seen:
                    print("row not valid")
                    return False
                elif board[i][j] != ".":
                    seen.append(board[i][j])
                
        # isColValid
        for i in range(len(board)):
            seen = []
            for j in range(len(board)):
                if board[j][i] in seen:
                    print("col not valid")
                    return False
                elif board[j][i] != ".":
                    seen.append(board[j][i])

        # isBoxValid
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = []
                for i in range(3):
                    for j in range(3):
                        if board[i+r][j+c] in seen:
                            print("box not valid")
                            return False
                        elif board[i+r][j+c] != ".":
                            seen.append(board[i+r][j+c])
        return True