# Problem 1: Find the First Non-Repeating Character
# Difficulty: Easy/Medium
#
# Problem Statement:
# Given a string s, return the index of the first non-repeating character in it. If it doesn't exist, return -1.
#
# Example:
#
# Input: "amazon"
# Output: 0  // 'a' is the first non-repeating character
#
# Input: "aabb"
# Output: -1


class Solution:
    def findNonRepeat(self,s )->int:
        j=0
        for  c in s :
            if (s.count(c)==1):
                return j
            else:
                j+=1
        if len(s)==j:
            return -1



if __name__ in '__main__':
    obj=Solution()
    o= obj.findNonRepeat("kaka")
    print (o)
