class Solution:
    def reverse(self, x: int) -> int:
        c=1
        if x<0:
            x=x*-1
            c=-1
        x1=str(x)
        x2=int(x1[::-1])*c
        if (x2>((2**31)-1) or x2<((2**32)*-1)):
            return 0
        return (x2)


if __name__ == '__main__':
    obj=Solution()
    o= obj.reverse(123)
    print(o)