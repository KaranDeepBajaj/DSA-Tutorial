# Problem 2: Validate String of Parentheses
# Difficulty: Medium
#
# Problem Statement:
# Given a string containing only the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.
#
# A string is valid if:
#
# Open brackets are closed by the same type of brackets.
#
# Open brackets are closed in the correct order.
# Example:
#
# Input: "()[]{}"
# Output: True
#
# Input: "([)]"
# Output: False

class Soultion:
    def validateParenthesis(self,s)->bool:
        l=[]
        for c in s:
            if (c=="{" or c=="[" or c=="("):
                l.append(c)
            else:
                if (len(l)==0):
                    return False
                elif (c == "}" and l[-1] == "{" or c == "]" and l[-1] == "[" or c == ")" and l[-1] == "(") :
                    l=l[:len(l)-1]
        if (len(l)==0):
            return True
        else:
            return False





if __name__ in '__main__':
    obj=Soultion()
    o=obj.validateParenthesis("{}[]")
    print(o)
