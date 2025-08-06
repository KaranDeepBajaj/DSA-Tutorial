from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        l = len(candidates)
        def backtrack(start,total,path:List[int]):
            if total == target:
                result.append(path[:])
                return
            elif total>target:
                return

            prev=-1
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num==prev:
                    continue
                elif num+total>target:
                    break
                path.append(num)
                backtrack(i+1, total+num, path)
                path.pop()
                prev=candidates[i]

        backtrack(0,0,[])
        return result

if __name__ == '__main__':
    obj = Solution()
    o = obj.combinationSum2([10,1,2,7,6,1,5],8)
    print(o)