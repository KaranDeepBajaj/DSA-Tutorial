class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen =None
        l=None
        k=0
        for i in range(k,len(s)):
            for j in range(i,len(s)):
                if l is None:
                    l=s[j]
                    if seen is None:
                        seen=l
                elif s[j] not in l:
                    l=l+s[j]
                    if len(l) > len(seen):
                        seen=l
                else:
                    l=None
                    break
        if seen is None:
            return 0
        else:
            return(len(seen))


if __name__ == '__main__':
    obj=Solution()
    m=obj.lengthOfLongestSubstring("")
    print(m)
