from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l=len(nums)
        lis=[]
        for i in range(l-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,l-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=l-1
                while left< right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        lis.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return lis



if __name__ in '__main__':
    obj=Solution()
    o=obj.fourSum([1,0,-1,0,-2,2],0)
    print(o)