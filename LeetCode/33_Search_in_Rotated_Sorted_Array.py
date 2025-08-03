from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            key = nums.index(target)
            return key
        else:
            return -1


if __name__ == '__main__':
    obj = Solution()
    o = obj.search([1,2,3],3)
    print(o)