class Solution:
    def isValid(self, s: str) -> bool:
        lis=[]
        for i in s:
            if i == "{" or i =="[" or i=="(":
              lis.append(i)
            else:
                if len(lis)==0:
                    return False
                if i=="}" and lis[-1]=="{" or i=="]" and lis[-1]=="[" or i==")" and lis[-1]=="(" :
                    lis=lis[:len(lis)-1]
                else:
                    return False
        if len(lis)==0:
            return True
        else:
            return False



if __name__ in '__main__':
    obj=Solution()
    o=obj.isValid("{}[]")
    print(o)