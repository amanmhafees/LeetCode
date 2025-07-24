class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_check = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            col_check = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_check:
                        row_check.remove(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] in col_check:
                        col_check.remove(board[j][i])
                    else:
                        return False

        for curr_row in range(0, 9, 3):
            for curr_col in range(0, 9, 3):
                check = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
                for i in range(3):
                    for j in range(3):
                        val = board[curr_row + i][curr_col + j]
                        if val != ".":
                            if val in check:
                                check.remove(val)
                            else:
                                return False

        return True
