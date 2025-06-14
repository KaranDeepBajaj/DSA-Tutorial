class Solution:
    def twoSum(self,nums,target):
        l=len(nums)
        list=[]
        for i in range(0,l):
            for k in range (i+1,l):
                if (i<l+1):
                    sum= nums[i]+nums[k]
                    if(sum==target):
                        list.append(i)
                        list.append(k)
                        return list

if __name__ == '__main__':
    obj=Solution()
    list=obj.twoSum([3,3],6)
    # list=obj.twoSum([-1,-2,-3,-4,-5],-8)
    print(list)