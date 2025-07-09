from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        final=float('inf')
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if (total==target):
                    return total
                if abs(total-target)<abs(final-target):
                    final=total
                if total<target:
                    left+=1
                else:
                    right-=1
        return final
if __name__ in '__main__':
    obj=Solution()
    o=obj.threeSumClosest([-4,2,2,3,3,3],0)
    print(o)