from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        l=len(nums)
        for i in nums:
            if i!=val:
                nums[j]=i
                j=j+1
        return j





if __name__ in '__main__':
    obj = Solution()
    o = obj.removeElement( [3,2,2,3],3)
    print(o)