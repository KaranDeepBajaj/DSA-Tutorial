from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            dict=Counter(i)
            for k,v in dict.items():
                if k!="." and v>1:
                    return False
        for i in range(9):
            dict2 = {}
            for j in range(9):
                dict2[board[j][i]]=dict2.get(board[j][i],0)+1
            for k,v in dict2.items():
                if k!="." and v>1:
                    return False
        dict3 = {}
        for i in range(0,9,3):
            for j in range (0,9):
                dict3[board[i][j]]=dict3.get(board[i][j],0)+1
                dict3[board[i+1][j]] = dict3.get(board[i+1][j], 0) + 1
                dict3[board[i+2][j]] = dict3.get(board[i+2][j], 0) + 1
                if j in [2,5,8]:
                    for k, v in dict3.items():
                        if k != "." and v > 1:
                            return False
                    dict3={}

        return True



if __name__ == '__main__':
    obj = Solution()
    o = obj.isValidSudoku([[".",".","5",".",".",".",".",".","6"],[".",".",".",".","1","4",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","9","2",".","."],["5",".",".",".",".","2",".",".","."],[".",".",".",".",".",".",".","3","."],[".",".",".","5","4",".",".",".","."],["3",".",".",".",".",".","4","2","."],[".",".",".","2","7",".","6",".","."]])
    print(o)
