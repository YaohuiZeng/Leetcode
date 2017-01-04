"""

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

"""


class Solution(object):

    def isValidSudoku(self, board):
        # soln 2: 75 ms
        # row
        for i in range(9):
            valid = {}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in valid:
                    return False
                else:
                    valid[board[i][j]] = 1
        # col
        for i in range(9):
            valid = {}
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in valid:
                    return False
                else:
                    valid[board[j][i]] = 1
        # sub
        for i in range(3):
            for j in range(3):
                valid = {}
                for k in range(3*i, 3*i+3):
                    for l in range(3*j, 3*j+3):
                        if board[k][l] != '.' and board[k][l] in valid:
                            return False
                        else:
                            valid[board[k][l]] = 1
        return True


    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [dict() for i in range(9)]
        col = [dict() for i in range(9)]
        sub = [dict() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i]:
                        return False
                    else:
                        row[i][board[i][j]] = 1
                    if board[i][j] in col[j]:
                        return False
                    else:
                        col[j][board[i][j]] = 1

                    if i < 3:
                        if j < 3:
                            if board[i][j] in sub[0]:
                                return False
                            else:
                                sub[0][board[i][j]] = 1
                        elif j < 6:
                            if board[i][j] in sub[1]:
                                return False
                            else:
                                sub[1][board[i][j]] = 1
                        elif j < 9:
                            if board[i][j] in sub[2]:
                                return False
                            else:
                                sub[2][board[i][j]] = 1
                    elif i < 6:
                        if j < 3:
                            if board[i][j] in sub[3]:
                                return False
                            else:
                                sub[3][board[i][j]] = 1
                        elif j < 6:
                            if board[i][j] in sub[4]:
                                return False
                            else:
                                sub[4][board[i][j]] = 1
                        elif j < 9:
                            if board[i][j] in sub[5]:
                                return False
                            else:
                                sub[5][board[i][j]] = 1
                    elif i < 9:
                        if j < 3:
                            if board[i][j] in sub[6]:
                                return False
                            else:
                                sub[6][board[i][j]] = 1
                        elif j < 6:
                            if board[i][j] in sub[7]:
                                return False
                            else:
                                sub[7][board[i][j]] = 1
                        elif j < 9:
                            if board[i][j] in sub[8]:
                                return False
                            else:
                                sub[8][board[i][j]] = 1

        return True