from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        l=len(nums)
        for i in range(1,l):
            if nums[j]!=nums[i]:
                j=j+1
                nums[j]=nums[i]
        return j+1


if __name__ in '__main__':
    obj=Solution()
    o=obj.removeDuplicates([1,1,2])
    print(o)