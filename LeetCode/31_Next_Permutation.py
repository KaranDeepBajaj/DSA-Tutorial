from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l =len(nums)
        i=l-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=l-1
            print(nums[i])
            while nums[j] <= nums[i]:
                j -= 1
            print(j)
            nums[i],nums[j]=nums[j],nums[i]
        print(nums)
        left=i+1
        right=l-1
        while left <right:
            print(nums[left],nums[right])
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
if __name__ == '__main__':
    obj = Solution()
    o = obj.nextPermutation([1,2,3,4])
    print(o)