# Problem 4: Longest Substring Without Repeating Characters
# Difficulty: Medium
#
# Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example:
#
# Input: "abcabcbb"
# Output: 3

class Solution:
    def longSubstring(self,s)->int:
        charset=set()
        maxlen=0
        left = 0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            maxlen=max(maxlen,len(charset))
        return (maxlen)


if __name__ in '__main__':
    obj=Solution()
    o=obj.longSubstring("abcabcbb")
    print(o)