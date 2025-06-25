from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        len1=len(height)
        left=0
        right =len1-1
        maxarea=0
        while left<right:
            h=min(height[left],height[right])
            w=right-left
            ar=h*w
            maxarea=max(maxarea,ar)
            if (height[left]<height[right]):
                left+=1
            else:
                right-=1

        return maxarea


if __name__ in '__main__':
    obj=Solution()
    o=obj.maxArea([1,8,6,2,5,4,8,3,7])
    print(o)
