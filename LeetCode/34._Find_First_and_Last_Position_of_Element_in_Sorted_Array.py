from collections import Counter
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
           return [-1,-1]
        else:
            count=Counter(nums)
            result=[]
            second=0
            if count[target]==1:
                first = nums.index(target)
                result.append(first)
                result.append(first)
            else:
                for i in range(count[target]-1):
                    if i==0:
                        first=nums.index(target)
                        result.append(first)
                    nums=nums[nums.index(target)+1:]
                    second=second+nums.index(target)+1
                result.append(second+first)
            return (result)

if __name__ == '__main__':
    obj = Solution()
    o = obj.searchRange([5,7,7,8,8,10],8)
    print(o)

