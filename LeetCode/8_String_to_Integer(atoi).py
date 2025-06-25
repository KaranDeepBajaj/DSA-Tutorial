class Solution:
    def myAtoi(self, s: str) -> int:
        k=s.strip(" ")
        if (len(k)==0):
            return 0
        lis=["0","1","2","3","4","5","6","7","8","9"]
        j=1
        fin=""
        if (k[0] == "-"):
            j=-1
            k=k[1:]
        elif (k[0] == "+"):
            j=1
            k=k[1:]
        for char in k:
            if (char in lis ):
                fin+=char
            else:
                break
        final=int(fin)*j if fin else 0
        if (final < -(2**31)):
            return -2147483648
        elif (final > ((2**31)-1)):
            return 2147483647
        return(final)



if __name__ in '__main__':
    obj=Solution()
    o=obj.myAtoi(" ++1")
    print(o)