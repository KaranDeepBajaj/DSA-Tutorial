class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if (x[::-1]==x):
            return True
        else:
            return False

if __name__ in '__main__':
    obj=Solution()
    o=obj.isPalindrome(121)
    print(o)