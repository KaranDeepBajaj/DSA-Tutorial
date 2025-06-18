class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows==1 or numRows>=len(s)):
            return s
        res=[""]*numRows
        cr=0
        toggle_flow=False
        for i in s:
            res[cr]=res[cr]+i
            if (cr ==0 or  cr == numRows-1):
                toggle_flow=not toggle_flow
            cr=cr+1 if toggle_flow else cr-1
        return "".join(res)


if __name__ =='__main__':
    obj=Solution()
    o=obj.convert("karan",3)
    print(o)