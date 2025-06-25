class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        left =0
        max_length=0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left]) # this will remove element form char_set unitl duplicate value is removed
                left+=1
            char_set.add(s[right])
            max_length=max(len(char_set),max_length)
        return max_length

if __name__ == '__main__':
    obj=Solution()
    m=obj.lengthOfLongestSubstring("abcdabcde")
    print(m)
