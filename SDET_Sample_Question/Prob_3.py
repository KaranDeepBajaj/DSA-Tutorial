# Problem 3: Count Pairs with Given Sum
# Difficulty: Medium
#
# Problem Statement:
# Given an array of integers nums and an integer k, return the number of unique pairs (i, j) such that nums[i] + nums[j] == k.
#
# Example:
#
# Input: nums = [1, 2, 3, 4, 3], k = 6
# Output: 2  // (2,4) and (3,3)
from typing import List


class Solution:
    def countPair(self,nums:List[int],k)-> int:
        seen=[]
        unique=[]
        complement=0
        for num in nums:
            complement=k-num
            if (complement in seen):
                small=min(num,complement)
                large=max(num,complement)
                unique.append([small,large])
            else:
                seen.append(num)
        return (len(unique))





if __name__ in '__main__':
    obj=Solution()
    o=obj.countPair([1,2,3,4,3],6)
    print(o)
