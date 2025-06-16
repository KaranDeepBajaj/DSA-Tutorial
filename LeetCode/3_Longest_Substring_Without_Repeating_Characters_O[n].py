class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left =0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_length=max(right-left+1,max_length)
        return max_length

if __name__ == '__main__':
    obj=Solution()
    m=obj.lengthOfLongestSubstring("")
    print(m)
