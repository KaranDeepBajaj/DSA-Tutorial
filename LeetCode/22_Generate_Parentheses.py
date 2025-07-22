from typing import List


class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(s='', left=0, right=0): #((,1,0) ,#(((,2,0),#(((),2,1),#((()),2,2),
            if len(s) == 2 * n:  # 2 not = 4
                result.append(s)
                return
            if left < n:  # left=0<2,  1<2,2
                backtrack(s + '(', left + 1, right)
            if right < left: # right=0<2,1<2
                backtrack(s + ')', left, right + 1)

        backtrack()
        return result



if __name__ in '__main__':
    obj=Solution()
    o=obj.generateParenthesis(2)
    print(o)