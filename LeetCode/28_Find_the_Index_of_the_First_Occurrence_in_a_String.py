class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(needle)
        l1=len(haystack)
        for i in range(l1):
            result=haystack[i:i+l]
            if result==needle:
                return i
        if i+1==l1:
            return -1



if __name__ == '__main__':
    obj=Solution()
    o=obj.strStr("hello","ll")
    print(o)