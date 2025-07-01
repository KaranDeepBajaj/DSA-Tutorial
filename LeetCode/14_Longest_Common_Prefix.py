from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=""
        l=len(strs)
        for i in strs[0]:
            c += i
            l = len(strs)
            for j in strs:
                if c in j[:len(c)]:
                    l=l-1

            if l!=0:
                c=c[:len(c)-1]
        return c

if __name__ in '__main__':
    obj=Solution()
    o=obj.longestCommonPrefix(["aa","ab"])
    print(o)