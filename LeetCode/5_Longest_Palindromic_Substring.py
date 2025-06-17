class Solution:
    def longestPalindrome(self, s: str) -> str:
        lt=0
        for i in range(len(s)):
            l=s[i]
            for k in range(i+1,len(s)):
                l=l+s[k]
                l=l
                if l==l[::-1]:
                    if(len(l)>lt):
                        lt=len(l)
                        final=l
        if (len(s)==1 or lt==0):
            final=s[0]
            return (final)
        else:
            return(final)

if __name__ == '__main__':
    obj=Solution()
    o= obj.longestPalindrome("ac")
    print(o)