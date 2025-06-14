class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            print(complement)
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            print(seen)

if __name__ == '__main__':
    obj=Solution()
    # list=obj.twoSum([3,3],6)
    list=obj.twoSum([-1,-2,-3,-4,-5],-8)
    print(list)