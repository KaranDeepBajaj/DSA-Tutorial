from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l.sort()
        ln=len(l)
        avg=(ln+1)/2
        if (ln%2!=0):
            return float(l[int(avg)-1])
        else:
            f1 =l[((int(avg+0.5))-1)]+l[((int(avg-0.5))-1)]
            return float(f1/2)

if __name__ in '__main__':
    obj = Solution()
    o=obj.findMedianSortedArrays([1,2],[4])
    print(o)