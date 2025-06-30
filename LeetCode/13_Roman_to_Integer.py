class Solution:
    def romanToInt(self, s: str) -> int:
        intrmn={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        c=0
        while s:
            if (s[:2] in intrmn.keys()):
                c=c+intrmn[s[:2]]
                s=s[2:]
            else:
                c=c+intrmn[s[0]]
                s=s[1:]
        return c

if __name__ in '__main__':
    obj=Solution()
    o=obj.romanToInt("MCMXCIV")
    print(o)