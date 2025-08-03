from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        left=0
        while left<=right:
            mid=(left+right)//2
            print(mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return (left)

if __name__ == '__main__':
    obj = Solution()
    o = obj.searchInsert([3,6,7,8,10],5)
    print(o)
