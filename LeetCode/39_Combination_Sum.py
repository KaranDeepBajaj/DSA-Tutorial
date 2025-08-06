from typing import List


class Solution:
    def combinationSum(self,candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, total,path:List[int]):
            if total==target:
                result.append(path[:])
                return
            elif total>target:
                return
            for i in range(start,len(candidates)):
                num=candidates[i]
                path.append(num)
                backtrack(i,total+num,path)
                path.pop()
        backtrack(0,0,[])
        return result



if __name__ == '__main__':
    obj = Solution()
    o = obj.combinationSum([2,3,6,7],7)
    print(o)